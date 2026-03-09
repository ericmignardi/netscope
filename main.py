from scapy.all import *
import typer

app = typer.Typer()

destination_subnet = "192.168.1.0/24"

@app.command()
def scan():
    print("Running scan...")
    eth = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=destination_subnet)
    print(f"Sending packet to {destination_subnet}")
    answered, unanswered = srp(eth, timeout=2, verbose=0)
    for sent, received in answered:
        print(f"IP: {received.psrc} MAC: {received.hwsrc}")
    
if __name__ == "__main__":
    app()
