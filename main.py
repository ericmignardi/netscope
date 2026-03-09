from scapy.all import *
import typer
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, RichLog
from textual import work
from textual.containers import Horizontal

app = typer.Typer()

destination_subnet = "192.168.1.0/24"

# ==========================================
# DAY 1: Foundation (ARP Scanning)
# ==========================================
@app.command()
def scan():
    print("Running scan...")
    
    eth = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=destination_subnet)
    
    print(f"Sending packet to {destination_subnet}")
    
    answered, unanswered = srp(eth, timeout=2, verbose=0)
    
    for sent, received in answered:
        print(f"IP: {received.psrc} MAC: {received.hwsrc}")

# ==========================================
# DAY 2: Route Tracing (Traceroute)
# ==========================================
@app.command()
def trace(target: str):
    for i in range(1, 30):
        print("Running trace...")

        pkt = IP(dst=target, ttl=i) / ICMP()

        reply = sr1(pkt, timeout=2, verbose=0)

        if reply is None:
            print("* * *")
            continue

        print(f"{i}: {reply.src} | Duration: {(reply.time - pkt.sent_time) * 1000}")

        if reply.src == target:
            print("Destination reched!")
            break

# ==========================================
# DAY 3: Textual UI (Dashboard)
# ==========================================
class NetscopeApp(App):
    CSS = """
    #sidebar {
        width: 40%;
        border-right: solid green;
    }
    """

    @work(exclusive=True, thread=True)
    def run_scan(self):
        eth = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=destination_subnet)
                
        answered, unanswered = srp(eth, timeout=2, verbose=0)
        
        for sent, received in answered:
            self.device_table.add_row(received.psrc, received.hwsrc)

    @work(exclusive=True, thread=True)
    def run_trace(self, target: str):
        for i in range(1, 30):
            pkt = IP(dst=target, ttl=i) / ICMP()

            reply = sr1(pkt, timeout=2, verbose=0)

            if reply is None:
                continue

            latency = (reply.time - pkt.sent_time) * 1000
            
            self.trace_log.write(f"Hop {i}: {reply.src} | Latency: {latency}ms")

            if reply.src == target:
                self.trace_log.write(f"[bold green]Traceroute complete![/] Reached {target}")
                break

    # ==========================================
    # DAY 4: Live Monitoring
    # ==========================================
    @work(exclusive=True, thread=True)
    def live_monitor(self):
        sniff(prn=self.analyze_packet, store=False)

    def analyze_packet(self, packet):
        if packet.haslayer(TCP):
            if packet[TCP].flags == "S": # S: Sync
                self.trace_log.write(f"[yellow]Anomaly:[/] SYN packet from {packet[IP].src} to port {packet[TCP].dport}")

    def compose(self) -> ComposeResult:
        yield Header()
        
        self.device_table = DataTable(id="sidebar")
        self.trace_log = RichLog(id="main", markup=True)
        
        with Horizontal():
            yield self.device_table
            yield self.trace_log

        yield Footer()

    def on_mount(self) -> None:
        self.device_table.add_columns("IP Address", "MAC Address")

        self.run_scan()
        self.trace_log.write("[bold red]Starting live monitoring...[/]")
        self.live_monitor()
        self.run_trace("8.8.8.8")

@app.command()
def ui():
    ui_app = NetscopeApp()
    ui_app.run()
    
if __name__ == "__main__":
    app()
