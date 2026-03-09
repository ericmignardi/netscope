# Netscope Interview Talking Points

Use these points to confidently explain the systems engineering challenges you solved while building this project!

## 1. Bridging the Gap (The High-Level Pitch)

> "Coming from a JavaScript and React background, I wanted to dive into lower-level systems programming and network engineering. I built `netscope`—a real-time, terminal-based network topology mapper and analyzer in Python—to prove I could build robust, asynchronous applications outside the browser."

## 2. Managing the UI Thread & Concurrency (The Technical Deep Dive)

> "The defining architectural challenge was managing the UI thread. By default, raw socket timeouts (like waiting for a Scapy ICMP ping to return) are blocking I/O operations. If I ran those network calls on the same thread as my 60fps terminal dashboard, the entire UI would completely freeze while waiting for packets."

## 3. The Asynchronous Solution

> "To solve the freezing issue, I had to implement asynchronous worker threads. I completely decoupled the packet sniffing, ARP scanning, and ICMP logic from Textual's UI event loop. This ensured the dashboard stayed completely snappy and responsive, while the heavy network I/O executed safely in isolated background routines."

## 4. Systems-Level Networking (Raw Sockets)

> "Instead of relying on high-level Python libraries to abstract the networking away, I used Scapy to construct packets at the raw socket level. I built layer 2 (ARP/Ethernet) and layer 3 (IP/ICMP/TCP) packets from scratch to perform device discovery, route tracing, and passive anomaly detection (like flagging SYN floods)."
