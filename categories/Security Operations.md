# Security Operations Skills

*Generated category with 36 skills*


- **analyzing-api-gateway-access-logs**
  Parses API Gateway access logs (AWS API Gateway, Kong, Nginx) to detect BOLA/IDOR attacks, rate limit bypass, credential scanning, and injection attempts. Uses pandas for statistical analysis of request patterns and anomaly detection. Use when investigating API abuse or building API-specific threat detection rules.


- **analyzing-azure-activity-logs-for-threats**
  Queries Azure Monitor activity logs and sign-in logs via azure-monitor-query to detect suspicious administrative operations, impossible travel, privilege escalation, and resource modifications. Builds KQL queries for threat hunting in Azure environments. Use when investigating suspicious Azure tenant activity or building cloud SIEM detections.


- **analyzing-cobalt-strike-malleable-profiles**
  Parses Cobalt Strike malleable C2 profiles using pyMalleableC2 to extract beacon configuration, HTTP communication patterns, and sleep/jitter settings. Combines with JARM TLS fingerprinting to detect C2 servers on the network. Use when investigating suspected Cobalt Strike infrastructure or building detection signatures for C2 traffic.


- **analyzing-memory-forensics-with-lime-and-volatility**
  Performs Linux memory acquisition using LiME (Linux Memory Extractor) kernel module and analysis with Volatility 3 framework. Extracts process lists, network connections, bash history, loaded kernel modules, and injected code from Linux memory images. Use when performing incident response on compromised Linux systems.


- **analyzing-powershell-script-block-logging**
  Parse Windows PowerShell Script Block Logs (Event ID 4104) from EVTX files to detect obfuscated commands, encoded payloads, and living-off-the-land techniques. Uses python-evtx to extract and reconstruct multi-block scripts, applies entropy analysis and pattern matching for Base64-encoded commands, Invoke-Expression abuse, download cradles, and AMSI bypass attempts.


- **analyzing-tls-certificate-transparency-logs**
  Queries Certificate Transparency logs via crt.sh and pycrtsh to detect phishing domains, unauthorized certificate issuance, and shadow IT. Monitors newly issued certificates for typosquatting and brand impersonation using Levenshtein distance. Use for proactive phishing domain detection and certificate monitoring.


- **analyzing-web-server-logs-for-intrusion**
  Parse Apache and Nginx access logs to detect SQL injection attempts, local file inclusion, directory traversal, web scanner fingerprints, and brute-force patterns. Uses regex-based pattern matching against OWASP attack signatures, GeoIP enrichment for source attribution, and statistical anomaly detection for request frequency and response size outliers.


- **configuring-microsegmentation-for-zero-trust**
  Configuring Microsegmentation For Zero Trust


- **deploying-software-defined-perimeter**
  Deploying Software Defined Perimeter


- **detecting-beaconing-patterns-with-zeek**
  Performs statistical analysis of Zeek conn.log connection intervals to detect C2 beaconing patterns. Uses the ZAT library to load Zeek logs into Pandas DataFrames, calculates inter-arrival time standard deviation, and flags periodic connections with low jitter. Use when hunting for command-and-control callbacks in network data.


- **detecting-golden-ticket-attacks**
  Detect Kerberos golden ticket attacks by analyzing Windows Security event logs for anomalous TGT usage patterns. Parses Event IDs 4624, 4672, and 4768 from EVTX files to identify tickets with abnormal lifetimes, domain SID mismatches, and privilege escalation sequences where non-admin accounts receive admin-level privileges without corresponding group membership changes.


- **detecting-insider-data-exfiltration-via-dlp**
  Detects insider data exfiltration by analyzing DLP policy violations, file access patterns, upload volume anomalies, and off-hours activity in endpoint and cloud logs. Uses pandas for behavioral analytics and statistical baselines. Use when investigating insider threats or building user behavior analytics for data loss prevention.


- **detecting-sql-injection-via-waf-logs**
  Analyze WAF (ModSecurity/AWS WAF/Cloudflare) logs to detect SQL injection attack campaigns. Parses ModSecurity audit logs and JSON WAF event logs to identify SQLi patterns (UNION SELECT, OR 1=1, SLEEP(), BENCHMARK()), tracks attack sources, correlates multi-stage injection attempts, and generates incident reports with OWASP classification.


- **detecting-supply-chain-attacks-in-ci-cd**
  Scans GitHub Actions workflows and CI/CD pipeline configurations for supply chain attack vectors including unpinned actions, script injection via expressions, dependency confusion, and secrets exposure. Uses PyGithub and YAML parsing for automated audit. Use when hardening CI/CD pipelines or investigating compromised build systems.


- **extracting-memory-artifacts-with-rekall**
  Uses Rekall memory forensics framework to analyze memory dumps for process hollowing, injected code via VAD anomalies, hidden processes, and rootkit detection. Applies plugins like pslist, psscan, vadinfo, malfind, and dlllist to extract forensic artifacts from Windows memory images. Use during incident response memory analysis.


- **hunting-credential-stuffing-attacks**
  Detects credential stuffing attacks by analyzing authentication logs for login velocity anomalies, ASN diversity, password spray patterns, and geographic distribution of failed logins. Uses statistical analysis on Splunk or raw log data. Use when investigating account takeover campaigns or building detection rules for auth abuse.


- **hunting-for-webshells-in-web-servers**
  Detect webshells planted on web servers by scanning for high-entropy files, suspicious PHP/JSP/ASP patterns (eval, base64_decode, system, passthru), recently modified files in web roots, and anomalous file sizes. Uses Shannon entropy calculation to flag obfuscated payloads and regex pattern matching against known webshell signatures.


- **hunting-living-off-the-land-binaries**
  Detects abuse of Living Off The Land Binaries (LOLBAS) such as certutil, wmic, mshta, regsvr32, and rundll32 in Windows event logs and Sysmon telemetry. Builds detection rules by cross-referencing process creation events against the LOLBAS project database. Use when threat hunting for fileless attack techniques or building SIEM detection rules.


- **implementing-email-security-with-dmarc-dkim-spf**
  Audit and validate email authentication configurations by checking SPF, DKIM, and DMARC DNS records for a domain. Uses dnspython to query TXT records, validates SPF syntax and lookup counts, verifies DKIM selector records, parses DMARC policies, and identifies misconfigurations that enable email spoofing. Generates remediation recommendations.


- **implementing-endpoint-detection-with-wazuh**
  Deploy and configure Wazuh SIEM/XDR for endpoint detection including agent management, custom decoder and rule XML creation, alert querying via the Wazuh REST API, and automated response actions.


- **implementing-honeytokens-for-breach-detection**
  Deploys canary tokens and honeytokens (fake AWS credentials, DNS canaries, document beacons, database records) that trigger alerts when accessed by attackers. Uses the Canarytokens API and custom webhook integrations for breach detection. Use when building deception-based early warning systems for intrusion detection.


- **implementing-identity-verification-for-zero-trust**
  Implementing Identity Verification For Zero Trust


- **implementing-log-forwarding-with-fluentd**
  Configure Fluentd and Fluent Bit for centralized log aggregation, routing, filtering, and enrichment across distributed infrastructure


- **implementing-log-integrity-with-blockchain**
  Build an append-only log integrity chain using SHA-256 hash chaining for tamper detection. Each log entry is hashed with the previous entry's hash to create a blockchain-like structure where modifying any entry invalidates all subsequent hashes. Implements log ingestion, chain verification, tamper detection with pinpoint identification, and periodic checkpoint anchoring to external timestamping services.


- **implementing-mtls-for-zero-trust-services**
  Configures mutual TLS (mTLS) authentication between microservices using Python cryptography library for certificate generation and ssl module for TLS verification. Validates certificate chains, checks expiration, and audits mTLS deployment status. Use when implementing zero-trust service-to-service authentication.


- **implementing-osquery-for-endpoint-monitoring**
  Deploy osquery scheduled queries for continuous endpoint monitoring covering process inventory, network connections, file integrity, and persistence mechanisms. Generates osquery.conf with query packs, configures differential result logging, and analyzes query results to detect suspicious processes, unauthorized listeners, and file modifications in system directories.


- **implementing-security-chaos-engineering**
  Implements security chaos engineering experiments that deliberately disable or degrade security controls to verify detection and response capabilities. Tests WAF bypass, firewall rule removal, log pipeline disruption, and EDR disablement scenarios using boto3 and subprocess. Use when validating SOC detection coverage and resilience.


- **implementing-security-monitoring-with-datadog**
  Implement security monitoring using Datadog's Cloud SIEM, log analysis, and threat detection capabilities to identify and respond to security events across cloud infrastructure.


- **implementing-siem-correlation-rules-for-apt**
  Write multi-event correlation rules that detect APT lateral movement by chaining Windows authentication events, process execution telemetry, and network connection logs across hosts. Uses Splunk SPL and Sigma rule format to correlate Event IDs 4624, 4648, 4688, and Sysmon Events 1/3 within sliding time windows to surface attack sequences invisible to single-event detections.


- **implementing-siem-use-case-tuning**
  Tune SIEM detection rules to reduce false positives by analyzing alert volumes, creating whitelists, adjusting thresholds, and measuring detection efficacy metrics in Splunk and Elastic


- **implementing-soar-playbook-for-phishing**
  Automate phishing incident response using Splunk SOAR REST API to create containers, add artifacts, and trigger playbooks


- **implementing-syslog-centralization-with-rsyslog**
  Configure rsyslog for centralized log collection with TLS encryption, custom templates, and log rotation. Generates server and client configuration files with GnuTLS stream drivers, x509 certificate authentication, per-host log segregation, and reliable queue settings for high-availability syslog infrastructure.


- **implementing-zero-trust-network-access-with-zscaler**
  Implementing Zero Trust Network Access With Zscaler


- **performing-dns-tunneling-detection**
  Detects DNS tunneling by computing Shannon entropy of DNS query names, analyzing query length distributions, inspecting TXT record payloads, and identifying high subdomain cardinality. Uses scapy for packet capture analysis and statistical methods to distinguish legitimate DNS from covert channels. Use when hunting for data exfiltration.


- **performing-red-team-phishing-with-gophish**
  Automate GoPhish phishing simulation campaigns using the Python gophish library. Creates email templates with tracking pixels, configures SMTP sending profiles, builds target groups from CSV, launches campaigns, and analyzes results including open rates, click rates, and credential submission statistics for security awareness assessment.


- **performing-ssrf-vulnerability-exploitation**
  Test for Server-Side Request Forgery vulnerabilities by probing cloud metadata endpoints, internal network services, and protocol handlers through user-controllable URL parameters. Tests AWS/GCP/Azure metadata APIs (169.254.169.254), internal port scanning via HTTP, URL scheme bypass techniques, and DNS rebinding detection.
