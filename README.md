# netscope 🔭

A real-time network topology mapper and analyzer for your terminal. Discover devices, trace routes, visualize your network, and monitor live traffic — all from the CLI.

---

## Features

- **Device Discovery**: ARP-scans the local subnet to identify active hosts, outputting IP and MAC address pairs.
- **Route Tracing**: Measures hop-by-hop latency to target hosts using custom ICMP/IP packets.
- **Terminal UI**: Live, interactive dashboard to visualize network state. _(In development)_
- **Traffic Monitoring**: Passively sniffs packets to detect anomalies like port scans. _(In development)_

## Tech Stack

- **Python 3.12+**: Core language.
- **Scapy**: Packet crafting, sending, and raw socket manipulation.
- **Typer**: CLI application framework.
- **Textual / Rich**: Terminal User Interface (TUI) and styling.
- **uv**: Project and dependency management.

---

## Installation & Setup

**Prerequisites:**

- Python 3.12+
- `uv` installed (`pip install uv`)
- **Windows Users**: Must install [Npcap](https://npcap.com/) for raw socket support.
- **Admin Privileges**: Running network scans requires Administrator/sudo privileges.

```bash
# Clone the repository
git clone https://github.com/yourusername/netscope.git
cd netscope

# Install dependencies and setup the virtual environment using uv
uv sync
```

## Usage

_Note: You must run your terminal as an Administrator._

**Scan Local Network:**

```bash
uv run main.py scan
```

**Trace Route to a Host:**

```bash
uv run main.py trace <target_ip_or_domain>
```

---

## Things Learned

Throughout the development of netscope, several core systems and networking concepts were explored:

- **OSI Model in Practice**: Manipulating Layer 2 (Ethernet/ARP) and Layer 3 (IP/ICMP) protocols directly.
- **Raw Sockets**: Bypassing standard OS networking abstractions to craft and send byte-level packets.
- **Asynchronous Execution**: Managing background threads for non-blocking packet sniffing.
- **CLI Architecture**: Designing an intuitive command-line interface with `typer`.
- **TUI Development**: Building responsive, event-driven terminal dashboards using `textual`.
