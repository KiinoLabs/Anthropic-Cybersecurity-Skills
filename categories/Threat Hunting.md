# Threat Hunting Skills

*Generated category with 55 skills*


- **analyzing-persistence-mechanisms-in-linux**
  Detect and analyze Linux persistence mechanisms including crontab entries, systemd service units, LD_PRELOAD hijacking, bashrc modifications, and authorized_keys backdoors using auditd and file integrity monitoring


- **analyzing-powershell-empire-artifacts**
  Detect PowerShell Empire framework artifacts in Windows event logs by identifying Base64 encoded launcher patterns, default user agents, staging URL structures, stager IOCs, and known Empire module signatures in Script Block Logging events.


- **analyzing-ransomware-network-indicators**
  Identify ransomware network indicators including C2 beaconing patterns, TOR exit node connections, data exfiltration flows, and encryption key exchange via Zeek conn.log and NetFlow analysis


- **building-threat-hunt-hypothesis-framework**
  Build a systematic threat hunt hypothesis framework that transforms threat intelligence, attack patterns, and environmental data into testable hunting hypotheses.


- **detecting-credential-dumping-with-edr**
  Detect OS credential dumping techniques including LSASS access, SAM extraction, and DCSync using EDR telemetry and Sysmon logs.


- **detecting-dcsync-attack-in-active-directory**
  Detect DCSync attacks where adversaries abuse Active Directory replication privileges to extract password hashes by monitoring for non-domain-controller accounts requesting directory replication via DsGetNCChanges.


- **detecting-dll-sideloading-attacks**
  Detect DLL side-loading attacks where adversaries place malicious DLLs alongside legitimate applications to hijack execution flow for defense evasion.


- **detecting-email-forwarding-rules-attack**
  Detect malicious email forwarding rules created by adversaries to maintain persistent access to email communications for intelligence collection and BEC attacks.


- **detecting-golden-ticket-attacks-in-kerberos-logs**
  Detect Golden Ticket attacks in Active Directory by analyzing Kerberos TGT anomalies including mismatched encryption types, impossible ticket lifetimes, non-existent accounts, and forged PAC signatures in domain controller event logs.


- **detecting-insider-threat-behaviors**
  Detect insider threat behavioral indicators including unusual data access, off-hours activity, mass file downloads, privilege abuse, and resignation-correlated data theft.


- **detecting-kerberoasting-attacks**
  Detect Kerberoasting attacks by monitoring for anomalous Kerberos TGS requests targeting service accounts with SPNs for offline password cracking.


- **detecting-lateral-movement-with-splunk**
  Detect adversary lateral movement across networks using Splunk SPL queries against Windows authentication logs, SMB traffic, and remote service abuse.


- **detecting-malicious-scheduled-tasks-with-sysmon**
  Detect malicious scheduled task creation and modification using Sysmon Event IDs 1 (Process Create for schtasks.exe), 11 (File Create for task XML), and Windows Security Event 4698/4702. The analyst correlates task creation with suspicious parent processes, public directory paths, and encoded command arguments to identify persistence and lateral movement via scheduled tasks. Activates for requests involving scheduled task detection, Sysmon persistence hunting, or T1053.005 Scheduled Task/Job analysis.


- **detecting-mimikatz-execution-patterns**
  Detect Mimikatz execution through command-line patterns, LSASS access signatures, binary indicators, and in-memory detection of known modules.


- **detecting-pass-the-hash-attacks**
  Detect Pass-the-Hash attacks by analyzing NTLM authentication patterns, identifying Type 3 logons with NTLM where Kerberos is expected, and correlating with credential dumping.


- **detecting-privilege-escalation-attempts**
  Detect privilege escalation attempts including token manipulation, UAC bypass, unquoted service paths, kernel exploits, and sudo/doas abuse across Windows and Linux.


- **detecting-process-hollowing-technique**
  Detect process hollowing (T1055.012) by analyzing memory-mapped sections, hollowed process indicators, and parent-child process anomalies in EDR telemetry.


- **detecting-service-account-abuse**
  Detect abuse of service accounts through anomalous interactive logons, privilege escalation, lateral movement, and unauthorized access patterns.


- **detecting-suspicious-powershell-execution**
  Detect suspicious PowerShell execution patterns including encoded commands, download cradles, AMSI bypass attempts, and constrained language mode evasion.


- **detecting-t1003-credential-dumping-with-edr**
  Detect OS credential dumping techniques targeting LSASS memory, SAM database, NTDS.dit, and cached credentials using EDR telemetry, Sysmon process access monitoring, and Windows security event correlation.


- **detecting-t1055-process-injection-with-sysmon**
  Detect process injection techniques (T1055) including classic DLL injection, process hollowing, and APC injection by analyzing Sysmon events for cross-process memory operations, remote thread creation, and anomalous DLL loading patterns.


- **detecting-t1548-abuse-elevation-control-mechanism**
  Detect abuse of elevation control mechanisms including UAC bypass, sudo exploitation, and setuid/setgid manipulation by monitoring registry modifications, process elevation flags, and unusual parent-child process relationships.


- **detecting-wmi-persistence**
  Detect WMI event subscription persistence by analyzing Sysmon Event IDs 19, 20, and 21 for malicious EventFilter, EventConsumer, and FilterToConsumerBinding creation.


- **hunting-for-anomalous-powershell-execution**
  Hunt for malicious PowerShell activity by analyzing Script Block Logging (Event 4104), Module Logging (Event 4103), and process creation events. The analyst parses Windows Event Log EVTX files to detect obfuscated commands, AMSI bypass attempts, encoded payloads, credential dumping keywords, and suspicious download cradles. Activates for requests involving PowerShell threat hunting, script block analysis, encoded command detection, or AMSI bypass identification.


- **hunting-for-beaconing-with-frequency-analysis**
  Identify command-and-control beaconing patterns in network traffic by applying statistical frequency analysis, jitter calculation, and coefficient of variation scoring to detect periodic callbacks from compromised endpoints.


- **hunting-for-cobalt-strike-beacons**
  Detect Cobalt Strike beacon network activity using default TLS certificate signatures (serial 8BB00EE), JA3/JA3S/JARM fingerprints, HTTP C2 profile pattern matching, beacon jitter analysis, and named pipe detection via Zeek, Suricata, and Python PCAP analysis.


- **hunting-for-command-and-control-beaconing**
  Detect C2 beaconing patterns in network traffic using frequency analysis, jitter detection, and domain reputation to identify compromised endpoints communicating with adversary infrastructure.


- **hunting-for-data-exfiltration-indicators**
  Hunt for data exfiltration through network traffic analysis, detecting unusual data flows, DNS tunneling, cloud storage uploads, and encrypted channel abuse.


- **hunting-for-data-staging-before-exfiltration**
  Detect data staging activity before exfiltration by monitoring for archive creation with 7-Zip/RAR, unusual temp folder access, large file consolidation, and staging directory patterns via EDR and process telemetry


- **hunting-for-dcsync-attacks**
  Detect DCSync attacks by analyzing Windows Event ID 4662 for unauthorized DS-Replication-Get-Changes requests from non-domain-controller accounts.


- **hunting-for-defense-evasion-via-timestomping**
  Detect NTFS timestamp manipulation (MITRE T1070.006) by comparing $STANDARD_INFORMATION vs $FILE_NAME timestamps in the MFT. Uses analyzeMFT and Python to identify files with anomalous temporal patterns indicating anti-forensic timestomping activity.


- **hunting-for-dns-based-persistence**
  Hunt for DNS-based persistence mechanisms including DNS hijacking, dangling CNAME records, wildcard DNS abuse, and unauthorized zone modifications using passive DNS databases, SecurityTrails API, and DNS audit log analysis.


- **hunting-for-dns-tunneling-with-zeek**
  Detect DNS tunneling and data exfiltration by analyzing Zeek dns.log for high-entropy subdomain queries, excessive query volume, long query lengths, and unusual DNS record types indicating covert channel communication.


- **hunting-for-domain-fronting-c2-traffic**
  Detect domain fronting C2 traffic by analyzing SNI vs HTTP Host header mismatches in proxy logs and TLS certificate discrepancies using pyOpenSSL for certificate inspection


- **hunting-for-lateral-movement-via-wmi**
  Detect WMI-based lateral movement by analyzing Windows Event ID 4688 process creation and Sysmon Event ID 1 for WmiPrvSE.exe child process patterns, remote process execution, and WMI event subscription persistence.


- **hunting-for-living-off-the-cloud-techniques**
  Hunt for adversary abuse of legitimate cloud services for C2, data staging, and exfiltration including abuse of Azure, AWS, GCP services, and SaaS platforms.


- **hunting-for-living-off-the-land-binaries**
  Proactively hunt for adversary abuse of legitimate system binaries (LOLBins) to execute malicious payloads while evading detection.


- **hunting-for-lolbins-execution-in-endpoint-logs**
  Hunt for adversary abuse of Living Off the Land Binaries (LOLBins) by analyzing endpoint process creation logs for suspicious execution patterns of legitimate Windows system binaries used for malicious purposes.


- **hunting-for-ntlm-relay-attacks**
  Detect NTLM relay attacks by analyzing Windows Event 4624 logon type 3 with NTLMSSP authentication, identifying IP-to-hostname mismatches, Responder traffic signatures, SMB signing status, and suspicious authentication patterns across the domain.


- **hunting-for-persistence-mechanisms-in-windows**
  Systematically hunt for adversary persistence mechanisms across Windows endpoints including registry, services, startup folders, and WMI subscriptions.


- **hunting-for-persistence-via-wmi-subscriptions**
  Hunt for adversary persistence through Windows Management Instrumentation event subscriptions by monitoring WMI consumer, filter, and binding creation events that execute malicious code triggered by system events.


- **hunting-for-process-injection-techniques**
  Detect process injection techniques (T1055) including CreateRemoteThread, process hollowing, and DLL injection via Sysmon Event IDs 8 and 10 and EDR process telemetry


- **hunting-for-registry-persistence-mechanisms**
  Hunt for registry-based persistence mechanisms including Run keys, Winlogon modifications, IFEO injection, and COM hijacking in Windows environments.


- **hunting-for-registry-run-key-persistence**
  Detect MITRE ATT&CK T1547.001 registry Run key persistence by analyzing Sysmon Event ID 13 logs and registry queries to identify malicious auto-start entries.


- **hunting-for-scheduled-task-persistence**
  Hunt for adversary persistence via Windows Scheduled Tasks by analyzing task creation events, suspicious task actions, and unusual scheduling patterns.


- **hunting-for-shadow-copy-deletion**
  Hunt for Volume Shadow Copy deletion activity that indicates ransomware preparation or anti-forensics by monitoring vssadmin, wmic, and PowerShell shadow copy commands.


- **hunting-for-spearphishing-indicators**
  Hunt for spearphishing campaign indicators across email logs, endpoint telemetry, and network data to detect targeted email attacks.


- **hunting-for-startup-folder-persistence**
  Detect T1547.001 startup folder persistence by monitoring Windows startup directories for suspicious file creation, analyzing autoruns entries, and using Python watchdog for real-time filesystem monitoring.


- **hunting-for-supply-chain-compromise**
  Hunt for supply chain compromise indicators including trojanized software updates, compromised dependencies, unauthorized code modifications, and tampered build artifacts.


- **hunting-for-suspicious-scheduled-tasks**
  Hunt for adversary persistence and execution via Windows scheduled tasks by analyzing task creation events, suspicious task properties, and unusual execution patterns that indicate T1053.005 abuse.


- **hunting-for-t1098-account-manipulation**
  Hunt for MITRE ATT&CK T1098 account manipulation including shadow admin creation, SID history injection, group membership changes, and credential modifications using Windows Security Event Logs.


- **hunting-for-unusual-network-connections**
  Hunt for unusual network connections by analyzing outbound traffic patterns, rare destinations, non-standard ports, and anomalous connection frequencies from endpoints.


- **hunting-for-unusual-service-installations**
  Detect suspicious Windows service installations (MITRE ATT&CK T1543.003) by parsing System event logs for Event ID 7045, analyzing service binary paths, and identifying indicators of persistence mechanisms.


- **hunting-for-webshell-activity**
  Hunt for web shell deployments on internet-facing servers by analyzing file creation in web directories, suspicious process spawning from web servers, and anomalous HTTP patterns.


- **performing-threat-hunting-with-yara-rules**
  Use YARA pattern-matching rules to hunt for malware, suspicious files, and indicators of compromise across filesystems and memory dumps. Covers rule authoring, yara-python scanning, and integration with threat intel feeds.
