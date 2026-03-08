# netscope Project Specifications

## 1. Project Breakdown & Milestones

We will build **netscope** in four distinct phases. Networking can get overwhelming quickly, so each phase builds on the success of the previous one.

- **Phase 1: Foundation & Discovery (The "Who is here?" phase)**
  - _Goal:_ Set up the project structure, CLI entry points, and build the ARP scanner to discover active devices on your local Wi-Fi or Ethernet.
  - _Why start here?_ ARP (Address Resolution Protocol) is the simplest way to see who is on your local subnet. It's a confidence booster and gets your feet wet with raw packets.
- **Phase 2: Routing & Latency (The "How do we get there?" phase)**
  - _Goal:_ Implement traceroute functionality to map out the hops between your machine and a target (like Google's servers or another device on your network).
  - _Dependency:_ Relies on the CLI foundation from Phase 1.
- **Phase 3: Visualization (The "Make it look good" phase)**
  - _Goal:_ Take the raw data from Phases 1 and 2 and render it into a beautiful, interactive Terminal User Interface (TUI).
  - _Dependency:_ Needs the data generation logic from prior phases so we have something to visualize.
- **Phase 4: Live Monitoring & Export (The "Pro Features" phase)**
  - _Goal:_ Add a live packet sniffer running in a background thread to flag anomalies (like port scans) and add a command to save the current network state to JSON.

---

## 2. Technology Stack

As a web developer, you're used to picking the right frontend framework and utility libraries. Here is the modern, powerful Python stack we will use, tailored for your goals:

- **Package Management:** `uv`
  - _Why:_ You're used to `npm` or `pnpm` being reasonably fast. Historically, Python's `pip` was slow and virtual environments were confusing. `uv` is written in Rust—it is blisteringly fast, handles virtual environments automatically, and resolves dependencies flawlessly.
- **CLI Framework:** `typer`
  - _Why:_ `typer` is to Python CLIs what standard React is to web pages. It uses Python type hints (very similar to TypeScript) to automatically generate help menus and parse command-line arguments. It is incredibly developer-friendly.
- **Networking Core:** `scapy`
  - _Why:_ This is the engine of `netscope`. Scapy is a powerful packet manipulation toolkit. Instead of writing raw C sockets, Scapy lets you craft, send, receive, and dissect network packets natively in Python.
- **Terminal UI:** `textual` (and `rich`)
  - _Why:_ `rich` gives us beautiful terminal colors, tables, and progress bars. `textual` builds on `rich` to give us a full browser-like DOM in the terminal (think CSS, flexbox, and event listeners, but for the CLI). Given your React background, `textual`'s layout engine will feel brilliantly familiar.

---

## 3. Install Commands & Local Setup (uv)

With `uv`, dependency management is handled directly without explicitly activating the virtual environment.

```bash
# 1. Initialize a new Python project/app using uv
uv init netscope

# 2. Move into the new directory
cd netscope

# 3. Add our core dependencies.
# uv will automatically detect/create a virtual environment (.venv) and install these inside it.
uv add scapy typer textual rich
```

> **Windows/Cross-Platform Note for Scapy:**
> Because you are on Windows, standard Python sockets cannot capture raw network packets out of the box. **You must install Npcap** (the packet capture library used by Wireshark) at the OS level for Scapy to work. You can download and install it from the official Npcap website.
>
> _Also Note:_ Sending raw packets (ARP, ICMP) requires Administrator privileges. When you run your scripts to test networking features, you will need to run your terminal as an Administrator.

---

## 4. Feature Breakdown

Here is the technical spec for exactly what you will be building.

### Feature 1: Local Network Discovery

- **Description:** Scans the local subnet to find all connected physical devices.
- **Inputs:** A subnet string (e.g., `192.168.1.0/24`).
- **Outputs:** A list of IP addresses mapping to their physical MAC addresses.
- **Edge Cases:** Firewalls often block ping (ICMP) requests, which is why we use ARP (Address Resolution Protocol) for local discovery instead—devices _must_ respond to ARP to route traffic locally. You'll also need to handle multiple network interfaces (e.g., VPNs, Ethernet, Wi-Fi) by allowing the user to specify an interface.

### Feature 2: Route Tracing & Latency Mapping

- **Description:** Measures the hop-by-hop path packets take to reach a destination.
- **Inputs:** A target IP address or hostname (e.g., `8.8.8.8` or `google.com`).
- **Outputs:** A sequence of router IPs, the time it took to reach each one (latency), and the final destination.
- **Edge Cases:** Many modern routers drop traceroute packets for security reasons. Your code needs to gracefully handle timeouts—usually represented as `* * *` in standard traceroute tools—without crashing the script.

### Feature 3: Terminal UI Dashboard

- **Description:** An interactive dashboard that stays open in the terminal, updating as data comes in.
- **Inputs:** Real-time data streams from your discovery and tracing functions.
- **Outputs:** A multi-pane terminal window (e.g., a table of devices on the left, a visual tree of the route on the right).
- **Edge Cases:** Terminal windows change size. Because we are using `textual`, you will need to ensure your UI is responsive (just like CSS media queries) so it doesn't break if the user resizes their window.

### Feature 4: Traffic Sniffing & Anomaly Detection

- **Description:** Passively listens to traffic on the user's interface to flag weird behavior.
- **Inputs:** Raw packets flowing through the active network interface.
- **Outputs:** Alerts in the UI based on heuristics (e.g., "Received 50 connection requests to different ports in 1 second from IP X").
- **Edge Cases:** Network traffic is incredibly fast. If you try to process every single packet heavily on the main thread, your app will freeze. You will need to learn how to sniff packets asynchronously or in a background thread so the UI remains responsive.

### Feature 5: JSON Export

- **Description:** Saves a snapshot of the current network profile to the filesystem.
- **Inputs:** A file path and the in-memory data structures representing the network.
- **Outputs:** A cleanly formatted `network_state.json` file.
- **Edge Cases:** Write permission errors, or the user inputting an invalid directory path.
