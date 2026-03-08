# netscope 🔭

A real-time network topology mapper and analyzer for your terminal. Discover devices, trace routes, visualize your network, and monitor live traffic — all from the CLI.

---

## Features

### Device Discovery

ARP-scans the local subnet to identify active hosts, resolving hostnames and MAC addresses where possible. Outputs a clean table of every device on the network with IP, MAC, and vendor info.

### Route Tracing & Latency Mapping

Sends ICMP probes to map the hop-by-hop path to any target host, measuring round-trip latency at each step — traceroute logic built from scratch at the socket level.

### Topology Visualization

Renders a live ASCII/TUI diagram of discovered network topology directly in the terminal. Nodes represent devices, edges represent routes, and latency is annotated inline.

### Traffic Monitoring & Anomaly Detection

Captures live packets on a specified interface and flags suspicious patterns — port scans, unusual burst traffic, and unexpected protocol usage — with configurable thresholds.

### Export & Reporting

Saves scan results and traffic summaries as structured JSON or plain-text reports for offline review, logging, or piping into other tools.

---

## Tech Stack

| Library                                       | Role                                                               |
| --------------------------------------------- | ------------------------------------------------------------------ |
| [Scapy](https://scapy.net/)                   | Packet crafting, ARP scanning, ICMP probes, and live capture       |
| [Rich](https://github.com/Textualize/rich)    | Terminal UI — tables, live displays, ASCII diagrams, styled output |
| [Typer](https://typer.tiangolo.com/)          | CLI interface — commands, flags, and argument parsing              |
| [psutil](https://github.com/giampaolo/psutil) | Network interface enumeration and system-level network stats       |
| Python 3.12+                                  | Core language                                                      |
| [uv](https://github.com/astral-sh/uv)         | Package and environment management                                 |

---

## Requirements

- Python 3.12+
- Root / sudo privileges required for raw socket operations (ARP scan, packet capture)
- Linux or macOS recommended — Windows support is limited due to raw socket restrictions
