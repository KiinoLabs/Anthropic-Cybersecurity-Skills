# Network Security Skills

*Generated category with 40 skills*


- **analyzing-network-flow-data-with-netflow**
  Parse NetFlow v9 and IPFIX records to detect volumetric anomalies, port scanning, data exfiltration, and C2 beaconing patterns. Uses the Python netflow library to decode flow records, builds traffic baselines, and applies statistical analysis to identify flows with abnormal byte counts, connection durations, and periodic timing patterns.


- **analyzing-network-packets-with-scapy**
  Craft, send, sniff, and dissect network packets using Scapy for protocol analysis, network reconnaissance, and traffic anomaly detection in authorized security testing


- **analyzing-network-traffic-with-wireshark**
  Captures and analyzes network packet data using Wireshark and tshark to identify malicious traffic patterns, diagnose protocol issues, extract artifacts, and support incident response investigations on authorized network segments.


- **conducting-man-in-the-middle-attack-simulation**
  Simulates man-in-the-middle attacks using Ettercap, mitmproxy, and Bettercap in authorized environments to intercept, analyze, and modify network traffic for testing encryption enforcement, certificate validation, and detection capabilities.


- **configuring-network-segmentation-with-vlans**
  Designs and implements VLAN-based network segmentation on managed switches to isolate network zones, enforce access control between segments, and reduce the attack surface by limiting lateral movement paths in enterprise network environments.


- **configuring-pfsense-firewall-rules**
  Configures pfSense firewall rules, NAT policies, VPN tunnels, and traffic shaping to enforce network segmentation, control traffic flow, and protect internal network zones in enterprise and small-to-medium business environments.


- **configuring-snort-ids-for-intrusion-detection**
  Installs, configures, and tunes Snort 3 intrusion detection system to monitor network traffic for malicious activity using custom and community rulesets, preprocessors, and alert output plugins on authorized network segments.


- **configuring-suricata-for-network-monitoring**
  Deploys and configures Suricata IDS/IPS with Emerging Threats rulesets, EVE JSON logging, and custom rules for real-time network traffic inspection, threat detection, and integration with SIEM platforms for centralized security monitoring.


- **detecting-arp-poisoning-in-network-traffic**
  Detect and prevent ARP spoofing attacks using ARPWatch, Dynamic ARP Inspection, Wireshark analysis, and custom monitoring scripts to protect against man-in-the-middle interception.


- **detecting-dns-exfiltration-with-dns-query-analysis**
  Detect data exfiltration through DNS tunneling by analyzing query entropy, subdomain length, query volume, TXT record abuse, and response payload sizes using passive DNS monitoring.


- **detecting-exfiltration-over-dns-with-zeek**
  Detect DNS-based data exfiltration by analyzing Zeek dns.log for high-entropy subdomains and anomalous query patterns


- **detecting-lateral-movement-in-network**
  Identifies lateral movement techniques in enterprise networks by analyzing authentication logs, network flows, SMB traffic, and RDP sessions using Zeek, Velociraptor, and SIEM correlation rules to detect attackers moving between systems.


- **detecting-network-anomalies-with-zeek**
  Deploys and configures Zeek (formerly Bro) network security monitor to passively analyze network traffic, generate structured logs, detect anomalous behavior, and create custom detection scripts for threat hunting and incident response.


- **detecting-network-scanning-with-ids-signatures**
  Detect network reconnaissance and port scanning using Suricata and Snort IDS signatures, threshold-based detection rules, and traffic anomaly analysis to identify Nmap, Masscan, and custom scanning activity.


- **detecting-port-scanning-with-fail2ban**
  Configures Fail2ban with custom filters and actions to detect port scanning activity, SSH brute force attempts, and network reconnaissance, automatically banning offending IP addresses and alerting security teams to suspicious network probing.


- **exploiting-bgp-hijacking-vulnerabilities**
  Analyzes and simulates BGP hijacking scenarios in authorized lab environments to assess route origin validation, RPKI deployment, and BGP monitoring defenses against prefix hijacking and route leak attacks on internet routing infrastructure.


- **exploiting-ipv6-vulnerabilities**
  Identifies and exploits IPv6-specific vulnerabilities including SLAAC spoofing, Router Advertisement flooding, and IPv6 tunneling during authorized assessments to test dual-stack security controls and IPv6-aware network defenses.


- **exploiting-smb-vulnerabilities-with-metasploit**
  Identifies and exploits SMB protocol vulnerabilities using Metasploit Framework during authorized penetration tests to demonstrate risks from unpatched Windows systems, misconfigured shares, and weak authentication in enterprise networks.


- **implementing-bgp-security-with-rpki**
  Implement BGP route origin validation using RPKI with Route Origin Authorizations, RPKI-to-Router protocol, and ROV policies on Cisco and Juniper routers to prevent route hijacking.


- **implementing-ddos-mitigation-with-cloudflare**
  Configure Cloudflare DDoS protection with managed rulesets, rate limiting, WAF rules, Bot Management, and origin protection to mitigate volumetric, protocol, and application-layer attacks.


- **implementing-network-access-control**
  Implements 802.1X port-based network access control using RADIUS authentication, PacketFence NAC, and switch configurations to enforce identity-based access policies, posture assessment, and automatic VLAN assignment for authorized devices.


- **implementing-network-access-control-with-cisco-ise**
  Deploy Cisco Identity Services Engine for 802.1X wired and wireless authentication, MAC Authentication Bypass, posture assessment, and dynamic VLAN assignment for network access control.


- **implementing-network-intrusion-prevention-with-suricata**
  Deploy and configure Suricata as a network intrusion prevention system with custom rules, Emerging Threats rulesets, and inline traffic inspection for real-time threat blocking.


- **implementing-network-segmentation-with-firewall-zones**
  Design and implement network segmentation using firewall security zones, VLANs, ACLs, and microsegmentation policies to restrict lateral movement and enforce least-privilege network access.


- **implementing-network-traffic-analysis-with-arkime**
  Deploy and query Arkime (formerly Moloch) for full packet capture network traffic analysis. Uses the Arkime API v3 to search sessions, download PCAPs, analyze connection patterns, detect beaconing behavior, and identify suspicious network flows. Monitors DNS queries, HTTP traffic, and TLS certificate anomalies across captured traffic.


- **implementing-network-traffic-baselining**
  Build network traffic baselines from NetFlow/IPFIX data using Python pandas for statistical analysis, z-score anomaly detection, and hourly/daily traffic pattern profiling


- **implementing-next-generation-firewall-with-palo-alto**
  Configure and deploy Palo Alto Networks next-generation firewalls with App-ID, User-ID, zone-based policies, SSL decryption, and threat prevention profiles for enterprise network security.


- **performing-arp-spoofing-attack-simulation**
  Simulates ARP spoofing attacks in authorized lab or pentest environments using arpspoof, Ettercap, and Scapy to demonstrate man-in-the-middle risks, test network detection capabilities, and validate ARP inspection countermeasures.


- **performing-bandwidth-throttling-attack-simulation**
  Simulates bandwidth throttling and network degradation attacks using tc, iperf3, and Scapy in authorized environments to test quality-of-service controls, application resilience, and network monitoring detection of traffic manipulation attacks.


- **performing-dns-enumeration-and-zone-transfer**
  Enumerates DNS records, attempts zone transfers, brute-forces subdomains, and maps DNS infrastructure during authorized reconnaissance to identify attack surface, misconfigurations, and information disclosure in target domains.


- **performing-network-traffic-analysis-with-tshark**
  Automate network traffic analysis using tshark and pyshark for protocol statistics, suspicious flow detection, DNS anomaly identification, and IOC extraction from PCAP files


- **performing-network-traffic-analysis-with-zeek**
  Deploy Zeek network security monitor to capture, parse, and analyze network traffic metadata for threat detection, anomaly identification, and forensic investigation.


- **performing-packet-injection-attack**
  Crafts and injects custom network packets using Scapy, hping3, and Nemesis during authorized security assessments to test firewall rules, IDS detection, protocol handling, and network stack resilience against malformed and spoofed traffic.


- **performing-ssl-stripping-attack**
  Simulates SSL stripping attacks using sslstrip, Bettercap, and mitmproxy in authorized environments to test HSTS enforcement, certificate validation, and HTTPS upgrade mechanisms that protect users from downgrade attacks on encrypted connections.


- **performing-ssl-tls-inspection-configuration**
  Configure SSL/TLS inspection on network security devices to decrypt, inspect, and re-encrypt HTTPS traffic for threat detection while managing certificates, exemptions, and privacy compliance.


- **performing-ssl-tls-security-assessment**
  Assess SSL/TLS server configurations using the sslyze Python library to evaluate cipher suites, certificate chains, protocol versions, HSTS headers, and known vulnerabilities like Heartbleed and ROBOT.


- **performing-vlan-hopping-attack**
  Simulates VLAN hopping attacks using switch spoofing and double tagging techniques in authorized environments to test VLAN segmentation effectiveness and validate switch port security configurations against Layer 2 bypass attacks.


- **performing-wifi-password-cracking-with-aircrack**
  Captures WPA/WPA2 handshakes and performs offline password cracking using aircrack-ng, hashcat, and dictionary attacks during authorized wireless security assessments to evaluate passphrase strength and wireless network security posture.


- **performing-wireless-security-assessment-with-kismet**
  Conduct wireless network security assessments using Kismet to detect rogue access points, hidden SSIDs, weak encryption, and unauthorized clients through passive RF monitoring.


- **scanning-network-with-nmap-advanced**
  Performs advanced network reconnaissance using Nmap's scripting engine, timing controls, evasion techniques, and output parsing to discover hosts, enumerate services, detect vulnerabilities, and fingerprint operating systems across authorized target networks.
