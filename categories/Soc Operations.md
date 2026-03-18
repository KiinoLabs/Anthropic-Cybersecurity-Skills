# Soc Operations Skills

*Generated category with 33 skills*


- **analyzing-dns-logs-for-exfiltration**
  Analyzes DNS query logs to detect data exfiltration via DNS tunneling, DGA domain communication, and covert C2 channels using entropy analysis, query volume anomalies, and subdomain length detection in SIEM platforms. Use when SOC teams need to identify DNS-based threats that bypass traditional network security controls.


- **analyzing-windows-event-logs-in-splunk**
  Analyzes Windows Security, System, and Sysmon event logs in Splunk to detect authentication attacks, privilege escalation, persistence mechanisms, and lateral movement using SPL queries mapped to MITRE ATT&CK techniques. Use when SOC analysts need to investigate Windows-based threats, build detection queries, or perform forensic timeline analysis of Windows endpoints and domain controllers.


- **building-automated-malware-submission-pipeline**
  Builds an automated malware submission and analysis pipeline that collects suspicious files from endpoints and email gateways, submits them to sandbox environments and multi-engine scanners, and generates verdicts with IOCs for SIEM integration. Use when SOC teams need to scale malware analysis beyond manual sandbox submissions for high-volume alert triage.


- **building-detection-rule-with-splunk-spl**
  Build effective detection rules using Splunk Search Processing Language (SPL) correlation searches to identify security threats in SOC environments.


- **building-detection-rules-with-sigma**
  Builds vendor-agnostic detection rules using the Sigma rule format for threat detection across SIEM platforms including Splunk, Elastic, and Microsoft Sentinel. Use when creating portable detection logic from threat intelligence, mapping rules to MITRE ATT&CK techniques, or converting community Sigma rules into platform-specific queries using sigmac or pySigma backends.


- **building-incident-response-dashboard**
  Builds real-time incident response dashboards in Splunk, Elastic, or Grafana to provide SOC analysts and leadership with situational awareness during active incidents, tracking affected systems, containment status, IOC spread, and response timeline. Use when IR teams need unified visibility during incident coordination and post-incident reporting.


- **building-soc-escalation-matrix**
  Build a structured SOC escalation matrix defining severity tiers, response SLAs, escalation paths, and notification procedures for security incidents.


- **building-soc-metrics-and-kpi-tracking**
  Builds SOC performance metrics and KPI tracking dashboards measuring Mean Time to Detect (MTTD), Mean Time to Respond (MTTR), alert quality ratios, analyst productivity, and detection coverage using SIEM data. Use when SOC leadership needs operational visibility, continuous improvement tracking, or executive-level reporting on security operations effectiveness.


- **building-soc-playbook-for-ransomware**
  Builds a structured SOC incident response playbook for ransomware attacks covering detection, containment, eradication, and recovery phases with specific SIEM queries, isolation procedures, and decision trees. Use when SOC teams need formalized response procedures for ransomware incidents aligned to NIST SP 800-61 and MITRE ATT&CK ransomware techniques.


- **building-threat-intelligence-enrichment-in-splunk**
  Build automated threat intelligence enrichment pipelines in Splunk Enterprise Security using lookup tables, modular inputs, and the Threat Intelligence Framework.


- **building-threat-intelligence-feed-integration**
  Builds automated threat intelligence feed integration pipelines connecting STIX/TAXII feeds, open-source threat intel, and commercial TI platforms into SIEM and security tools for real-time IOC matching and alerting. Use when SOC teams need to operationalize threat intelligence by automating feed ingestion, normalization, scoring, and distribution to detection systems.


- **building-vulnerability-scanning-workflow**
  Builds a structured vulnerability scanning workflow using tools like Nessus, Qualys, and OpenVAS to discover, prioritize, and track remediation of security vulnerabilities across infrastructure. Use when SOC teams need to establish recurring vulnerability assessment processes, integrate scan results with SIEM alerting, and build remediation tracking dashboards.


- **correlating-security-events-in-qradar**
  Correlates security events in IBM QRadar SIEM using AQL (Ariel Query Language), custom rules, building blocks, and offense management to detect multi-stage attacks across network, endpoint, and application log sources. Use when SOC analysts need to investigate QRadar offenses, build correlation rules, or tune detection logic for reducing false positives.


- **implementing-alert-fatigue-reduction**
  Implements strategies to reduce SOC alert fatigue by tuning detection rules, consolidating duplicate alerts, implementing risk-based alerting, and measuring alert quality metrics to maintain analyst effectiveness and prevent critical alert dismissal. Use when SOC teams face overwhelming alert volumes, high false positive rates, or declining analyst performance.


- **implementing-mitre-attack-coverage-mapping**
  Implement MITRE ATT&CK coverage mapping to identify detection gaps, prioritize rule development, and measure SOC detection maturity against adversary techniques.


- **implementing-siem-use-cases-for-detection**
  Implements SIEM detection use cases by designing correlation rules, threshold alerts, and behavioral analytics mapped to MITRE ATT&CK techniques across Splunk, Elastic, and Sentinel. Use when SOC teams need to expand detection coverage, formalize use case lifecycle management, or build a detection library aligned to organizational threat profile.


- **implementing-soar-automation-with-phantom**
  Implements Security Orchestration, Automation, and Response (SOAR) workflows using Splunk SOAR (formerly Phantom) to automate alert triage, IOC enrichment, containment actions, and incident response playbooks. Use when SOC teams need to reduce manual analyst work, standardize response procedures, or integrate multiple security tools into automated workflows.


- **implementing-soar-playbook-with-palo-alto-xsoar**
  Implement automated incident response playbooks in Cortex XSOAR to orchestrate security workflows across SOC tools and reduce manual response time.


- **implementing-threat-modeling-with-mitre-attack**
  Implements threat modeling using the MITRE ATT&CK framework to map adversary TTPs against organizational assets, assess detection coverage gaps, and prioritize defensive investments. Use when SOC teams need to align detection engineering with threat landscape, conduct threat assessments for new environments, or justify security tool procurement.


- **implementing-ticketing-system-for-incidents**
  Implements an integrated incident ticketing system connecting SIEM alerts to ServiceNow, Jira, or TheHive for structured incident tracking, SLA management, escalation workflows, and compliance documentation. Use when SOC teams need formalized incident lifecycle management with automated ticket creation, assignment routing, and resolution tracking.


- **investigating-insider-threat-indicators**
  Investigates insider threat indicators including data exfiltration attempts, unauthorized access patterns, policy violations, and pre-departure behaviors using SIEM analytics, DLP alerts, and HR data correlation. Use when SOC teams receive insider threat referrals from HR, detect anomalous data movement by employees, or need to build investigation timelines for potential insider threats.


- **investigating-phishing-email-incident**
  Investigates phishing email incidents from initial user report through header analysis, URL/attachment detonation, impacted user identification, and containment actions using SOC tools like Splunk, Microsoft Defender, and sandbox analysis platforms. Use when a reported phishing email requires full incident investigation to determine scope and impact.


- **performing-alert-triage-with-elastic-siem**
  Perform systematic alert triage in Elastic Security SIEM to rapidly classify, prioritize, and investigate security alerts for SOC operations.


- **performing-deception-technology-deployment**
  Deploys deception technology including honeypots, honeytokens, and decoy systems to detect attackers who have bypassed perimeter defenses, providing high-fidelity alerts with near-zero false positive rates. Use when SOC teams need early warning of lateral movement, credential abuse, or internal reconnaissance by deploying convincing traps across the network.


- **performing-false-positive-reduction-in-siem**
  Perform systematic SIEM false positive reduction through rule tuning, threshold adjustment, correlation refinement, and threat intelligence enrichment to combat alert fatigue.


- **performing-ioc-enrichment-automation**
  Automates Indicator of Compromise (IOC) enrichment by orchestrating lookups across VirusTotal, AbuseIPDB, Shodan, MISP, and other intelligence sources to provide contextual scoring and disposition recommendations. Use when SOC analysts need rapid multi-source enrichment of IPs, domains, URLs, and file hashes during alert triage or incident investigation.


- **performing-lateral-movement-detection**
  Detects lateral movement techniques including Pass-the-Hash, PsExec, WMI execution, RDP pivoting, and SMB-based spreading using SIEM correlation of Windows event logs, network flow data, and endpoint telemetry mapped to MITRE ATT&CK Lateral Movement (TA0008) techniques.


- **performing-log-source-onboarding-in-siem**
  Perform structured log source onboarding into SIEM platforms by configuring collectors, parsers, normalization, and validation for complete security visibility.


- **performing-purple-team-exercise**
  Performs purple team exercises by coordinating red team adversary emulation with blue team detection validation using MITRE ATT&CK-mapped attack scenarios, real-time detection testing, and collaborative gap remediation. Use when SOC teams need to validate detection capabilities, improve analyst skills, and close detection gaps through structured offensive-defensive collaboration.


- **performing-soc-tabletop-exercise**
  Performs tabletop exercises for SOC teams simulating security incidents through discussion-based scenarios to test incident response procedures, communication workflows, and decision-making under pressure without impacting production systems. Use when organizations need to validate IR playbooks, train analysts, or meet compliance requirements for incident response testing.


- **performing-threat-hunting-with-elastic-siem**
  Performs proactive threat hunting in Elastic Security SIEM using KQL/EQL queries, detection rules, and Timeline investigation to identify threats that evade automated detection. Use when SOC teams need to hunt for specific ATT&CK techniques, investigate anomalous behaviors, or validate detection coverage gaps using Elasticsearch and Kibana Security.


- **performing-user-behavior-analytics**
  Performs User and Entity Behavior Analytics (UEBA) to detect anomalous user activities including impossible travel, unusual access patterns, privilege abuse, and insider threats using SIEM-based behavioral baselines and statistical analysis. Use when SOC teams need to identify compromised accounts or insider threats through deviation from established behavioral norms.


- **triaging-security-alerts-in-splunk**
  Triages security alerts in Splunk Enterprise Security by classifying severity, investigating notable events, correlating related telemetry, and making escalation or closure decisions using SPL queries and the Incident Review dashboard. Use when SOC analysts face queued alerts from correlation searches, need to prioritize investigation order, or must document triage decisions for handoff to Tier 2/3 analysts.
