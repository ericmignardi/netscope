# netscope: One-Week Development Timeline

**Assume ~2-3 hours of focused coding per day.**

### Monday: The Foundation (Structure & ARP Scanning)

- _Objective:_ Get the CLI framework running and find devices on the local network.
- _Tasks:_
  1.  Set up the `typer` CLI skeleton in `main.py` (e.g., creating a `netscope scan` command).
  2.  Write a simple Scapy function to broadcast an ARP request to your subnet (e.g., `192.168.1.0/24`).
  3.  Parse the ARP responses and print the IP and MAC addresses to the terminal.
- _Deliverable by End of Day:_ Running `py main.py scan` prints a raw list of devices connected to your Wi-Fi.

### Tuesday: Route Tracing (The "Traceroute" Logic)

- _Objective:_ Send packets into the internet and map the hops.
- _Tasks:_
  1.  Add a new Typer command: `netscope trace <target_ip>`.
  2.  Use Scapy to send ICMP (ping) packets with incrementing Time-To-Live (TTL) values.
  3.  Capture the "Time Exceeded" ICMP responses from routers along the path.
  4.  Calculate the latency (Time Received - Time Sent) for each hop.
- _Deliverable by End of Day:_ Running `py main.py trace google.com` prints a list of router IPs and their latency in milliseconds.

### Wednesday: The Dashboard (Textual UI)

- _Objective:_ Move out of the raw terminal output and into a beautiful Dashboard.
- _Tasks:_
  1.  Initialize a basic `textual` app instance.
  2.  Design the layout: A sidebar (for the device list) and a main view (for the traceroute/logs).
  3.  Connect your ARP scan and Trace functions to update the `textual` UI state (conceptually similar to `setState` in React).
- _Deliverable by End of Day:_ Running `py main.py dashboard` opens a responsive terminal UI holding the data you gathered on Monday and Tuesday.

### Thursday: Live Monitoring (Background Threads & Packet Sniffing)

- _Objective:_ Watch traffic in real-time without freezing the UI.
- _Tasks:_
  1.  Use Python's `threading` or `asyncio` to run a continuous packet capture loop (using Scapy's `sniff()` function).
  2.  Filter the packets (e.g., only look at TCP/UDP traffic).
  3.  Write simple heuristics: "If I see 10 connection attempts to different ports from the same IP in 1 second, flag a Port Scan."
  4.  Send these alerts to a scrolling "Log" pane in your Textual Dashboard.
- _Deliverable by End of Day:_ The dashboard now features a live, updating log of network events and anomalies.

### Friday: Exporting, Polish, & Documentation

- _Objective:_ Wrap the project up to be portfolio-ready.
- _Tasks:_
  1.  Add a `--json` or `--export` flag to your Typer commands to dump the network state into a `results.json` file.
  2.  Clean up variable names and add Python docstrings (comments) to your functions.
  3.  Flesh out the `README.md` with instructions on how to install and use the tool (specifically noting the Administrator privilege requirement).
- _Deliverable by End of Day:_ A finished, polished CLI tool that you can push to GitHub.
