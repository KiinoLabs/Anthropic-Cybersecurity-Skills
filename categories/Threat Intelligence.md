# Threat Intelligence Skills

*Generated category with 50 skills*


- **analyzing-apt-group-with-mitre-navigator**
  Analyze advanced persistent threat (APT) group techniques using MITRE ATT&CK Navigator to create layered heatmaps of adversary TTPs for detection gap analysis and threat-informed defense.


- **analyzing-campaign-attribution-evidence**
  Campaign attribution analysis involves systematically evaluating evidence to determine which threat actor or group is responsible for a cyber operation. This skill covers collecting and weighting attr


- **analyzing-certificate-transparency-for-phishing**
  Monitor Certificate Transparency logs using crt.sh and Certstream to detect phishing domains, lookalike certificates, and unauthorized certificate issuance targeting your organization.


- **analyzing-cyber-kill-chain**
  Analyzes intrusion activity against the Lockheed Martin Cyber Kill Chain framework to identify which phases an adversary has completed, where defenses succeeded or failed, and what controls would have interrupted the attack at earlier phases. Use when conducting post-incident analysis, building prevention-focused security controls, or mapping detection gaps to kill chain phases. Activates for requests involving kill chain analysis, intrusion kill chain, attack phase mapping, or Lockheed Martin kill chain framework.


- **analyzing-indicators-of-compromise**
  Analyzes indicators of compromise (IOCs) including IP addresses, domains, file hashes, URLs, and email artifacts to determine maliciousness confidence, campaign attribution, and blocking priority. Use when triaging IOCs from phishing emails, security alerts, or external threat feeds; enriching raw IOCs with multi-source intelligence; or making block/monitor/whitelist decisions. Activates for requests involving VirusTotal, AbuseIPDB, MalwareBazaar, MISP, or IOC enrichment pipelines.


- **analyzing-malware-family-relationships-with-malpedia**
  Use the Malpedia platform and API to research malware family relationships, track variant evolution, link families to threat actors, and integrate YARA rules for detection across malware lineages.


- **analyzing-ransomware-leak-site-intelligence**
  Monitor and analyze ransomware group data leak sites (DLS) to track victim postings, extract threat intelligence on group tactics, and assess sector-specific ransomware risk for proactive defense.


- **analyzing-threat-actor-ttps-with-mitre-attack**
  MITRE ATT&CK is a globally-accessible knowledge base of adversary tactics, techniques, and procedures (TTPs) based on real-world observations. This skill covers systematically mapping threat actor beh


- **analyzing-threat-actor-ttps-with-mitre-navigator**
  Map advanced persistent threat (APT) group tactics, techniques, and procedures (TTPs) to the MITRE ATT&CK framework using the ATT&CK Navigator and attackcti Python library. The analyst queries STIX/TAXII data for group-technique associations, generates Navigator layer files for visualization, and compares defensive coverage against adversary profiles. Activates for requests involving APT TTP mapping, ATT&CK Navigator layers, threat actor profiling, or MITRE technique coverage analysis.


- **analyzing-threat-intelligence-feeds**
  Analyzes structured and unstructured threat intelligence feeds to extract actionable indicators, adversary tactics, and campaign context. Use when ingesting commercial or open-source CTI feeds, evaluating feed quality, normalizing data into STIX 2.1 format, or enriching existing IOCs with campaign attribution. Activates for requests involving ThreatConnect, Recorded Future, Mandiant Advantage, MISP, AlienVault OTX, or automated feed aggregation pipelines.


- **analyzing-threat-landscape-with-misp**
  Analyze the threat landscape using MISP (Malware Information Sharing Platform) by querying event statistics, attribute distributions, threat actor galaxy clusters, and tag trends over time. Uses PyMISP to pull event data, compute IOC type breakdowns, identify top threat actors and malware families, and generate threat landscape reports with temporal trends.


- **analyzing-typosquatting-domains-with-dnstwist**
  Detect typosquatting, homograph phishing, and brand impersonation domains using dnstwist to generate domain permutations and identify registered lookalike domains targeting your organization.


- **automating-ioc-enrichment**
  Automates the enrichment of raw indicators of compromise with multi-source threat intelligence context using SOAR platforms, Python pipelines, or TIP playbooks to reduce analyst triage time and standardize enrichment outputs. Use when building automated enrichment workflows integrated with SIEM alerts, email submission pipelines, or bulk IOC processing from threat feeds. Activates for requests involving SOAR enrichment, Cortex XSOAR, Splunk SOAR, TheHive, Python enrichment pipelines, or automated IOC processing.


- **building-adversary-infrastructure-tracking-system**
  Build an automated system to track adversary infrastructure using passive DNS, certificate transparency, WHOIS data, and IP enrichment to map and monitor threat actor command-and-control networks.


- **building-attack-pattern-library-from-cti-reports**
  Extract and catalog attack patterns from cyber threat intelligence reports into a structured STIX-based library mapped to MITRE ATT&CK for detection engineering and threat-informed defense.


- **building-ioc-defanging-and-sharing-pipeline**
  Build an automated pipeline to defang indicators of compromise (URLs, IPs, domains, emails) for safe sharing and distribute them in STIX format through TAXII feeds and threat intelligence platforms.


- **building-ioc-enrichment-pipeline-with-opencti**
  OpenCTI is an open-source platform for managing cyber threat intelligence knowledge, built on STIX 2.1 as its native data model. This skill covers building an automated IOC enrichment pipeline using O


- **building-threat-actor-profile-from-osint**
  Build comprehensive threat actor profiles using open-source intelligence (OSINT) techniques to document adversary motivations, capabilities, infrastructure, and TTPs for proactive defense.


- **building-threat-feed-aggregation-with-misp**
  Deploy MISP (Malware Information Sharing Platform) to aggregate, correlate, and distribute threat intelligence feeds from multiple sources for centralized IOC management and automated SIEM integration.


- **building-threat-intelligence-platform**
  Building a Threat Intelligence Platform (TIP) involves deploying and integrating multiple CTI tools into a unified system for collecting, analyzing, enriching, and disseminating threat intelligence. T


- **collecting-open-source-intelligence**
  Collects and synthesizes open-source intelligence (OSINT) about threat actors, malicious infrastructure, and attack campaigns using publicly available data sources, passive reconnaissance tools, and dark web monitoring. Use when investigating external threat actor infrastructure, performing pre-engagement reconnaissance for authorized red team assessments, or enriching CTI reports with publicly available adversary context. Activates for requests involving Maltego, Shodan, OSINT framework, SpiderFoot, or infrastructure reconnaissance.


- **collecting-threat-intelligence-with-misp**
  MISP (Malware Information Sharing Platform) is an open-source threat intelligence platform for gathering, sharing, storing, and correlating Indicators of Compromise (IOCs) of targeted attacks, threat


- **correlating-threat-campaigns**
  Correlates disparate security incidents, IOCs, and adversary behaviors across time and organizations to identify unified threat campaigns, attribute them to common threat actors, and extract shared indicators for improved detection. Use when multiple incidents exhibit overlapping indicators, when sector-wide attack campaigns require cross-organizational analysis, or when building campaign-level intelligence products. Activates for requests involving campaign analysis, incident clustering, cross-organizational IOC correlation, or MISP correlation engine.


- **evaluating-threat-intelligence-platforms**
  Evaluates and selects Threat Intelligence Platform (TIP) products based on organizational requirements including feed integration capability, STIX/TAXII support, workflow automation, analyst interface, and total cost of ownership. Use when conducting a TIP procurement, migrating between TIP solutions, or assessing whether the current TIP meets program maturity requirements. Activates for requests involving ThreatConnect, MISP, OpenCTI, Anomali, EclecticIQ, or TIP procurement decisions.


- **executing-diamond-model-analysis**
  Applies the Diamond Model of Intrusion Analysis to structure adversary activity into its four core vertices (adversary, capability, infrastructure, victim) and identifies relationships between them to pivot investigations and attribute campaigns. Use when analyzing a completed intrusion, linking disparate incidents to a common threat actor, or building structured analytic products for threat intelligence dissemination. Activates for requests involving Diamond Model, intrusion analysis, campaign clustering, or adversary attribution methodology.


- **generating-threat-intelligence-reports**
  Generates structured cyber threat intelligence reports at strategic, operational, and tactical levels tailored to specific audiences including executives, security operations teams, and technical analysts. Use when producing finished intelligence products from raw collection data, creating sector threat briefings, or delivering post-incident intelligence assessments. Activates for requests involving CTI report writing, threat briefings, intelligence products, finished intelligence, or executive security reporting.


- **hunting-advanced-persistent-threats**
  Proactively hunts for Advanced Persistent Threat (APT) activity within enterprise environments using hypothesis-driven searches across endpoint telemetry, network logs, and memory artifacts. Use when conducting scheduled threat hunting cycles, investigating anomalous behavior flagged by UEBA, or validating that known APT TTPs are not present in the environment. Activates for requests involving MITRE ATT&CK, Velociraptor, osquery, Zeek, or threat hunting playbooks.


- **implementing-diamond-model-analysis**
  The Diamond Model of Intrusion Analysis provides a structured framework for analyzing cyber intrusions by examining four core features: Adversary, Capability, Infrastructure, and Victim. This skill co


- **implementing-security-information-sharing-with-stix2**
  Create, validate, and share STIX 2.1 threat intelligence objects using the stix2 Python library. Covers indicators, malware, campaigns, relationships, bundles, and TAXII 2.1 publishing.


- **implementing-stix-taxii-feed-integration**
  STIX (Structured Threat Information eXpression) and TAXII (Trusted Automated eXchange of Intelligence Information) are OASIS open standards for representing and transporting cyber threat intelligence.


- **implementing-taxii-server-with-opentaxii**
  Deploy and configure an OpenTAXII server to share and consume STIX-formatted cyber threat intelligence using the TAXII 2.1 protocol for automated indicator exchange between organizations.


- **implementing-threat-intelligence-lifecycle-management**
  Implement a structured threat intelligence lifecycle encompassing planning, collection, processing, analysis, dissemination, and feedback stages to produce actionable intelligence for organizational decision-making.


- **implementing-threat-intelligence-platform**
  Build a MISP-backed threat intelligence platform that ingests IOCs from multiple feeds, correlates events with galaxy clusters, and enriches indicators via VirusTotal and AbuseIPDB. Uses PyMISP to create events, add attributes with IDS flags, tag with MITRE ATT&CK techniques, and export STIX 2.1 bundles for downstream SIEM consumption.


- **managing-intelligence-lifecycle**
  Manages the end-to-end cyber threat intelligence lifecycle from planning and direction through collection, processing, analysis, dissemination, and feedback to ensure intelligence products meet stakeholder requirements and continuously improve. Use when establishing or maturing a CTI program, defining intelligence requirements with business stakeholders, or building feedback loops between intelligence consumers and producers. Activates for requests involving CTI program maturity, intelligence requirements, PIRs, or intelligence lifecycle management.


- **mapping-mitre-attack-techniques**
  Maps observed adversary behaviors, security alerts, and detection rules to MITRE ATT&CK techniques and sub-techniques to quantify detection coverage and guide control prioritization. Use when building an ATT&CK-based coverage heatmap, tagging SIEM alerts with technique IDs, aligning security controls to adversary playbooks, or reporting threat exposure to executives. Activates for requests involving ATT&CK Navigator, Sigma rules, MITRE D3FEND, or coverage gap analysis.


- **monitoring-darkweb-sources**
  Monitors dark web forums, marketplaces, paste sites, and ransomware leak sites for mentions of organizational assets, leaked credentials, threatened attacks, and threat actor communications to provide early warning intelligence. Use when establishing dark web monitoring coverage, investigating specific data breach claims, or enriching incident investigations with dark web context. Activates for requests involving dark web OSINT, leak site monitoring, credential exposure, Recorded Future dark web, or Tor hidden service intelligence.


- **performing-brand-monitoring-for-impersonation**
  Monitor for brand impersonation attacks across domains, social media, mobile apps, and dark web channels to detect phishing campaigns, fake sites, and unauthorized brand usage targeting your organization.


- **performing-dark-web-monitoring-for-threats**
  Dark web monitoring involves systematically scanning Tor hidden services, underground forums, paste sites, and dark web marketplaces to identify threats targeting an organization, including leaked cre


- **performing-indicator-lifecycle-management**
  Indicator lifecycle management tracks IOCs from initial discovery through validation, enrichment, deployment, monitoring, and eventual retirement. This skill covers implementing systematic processes f


- **performing-ip-reputation-analysis-with-shodan**
  Analyze IP address reputation using the Shodan API to identify open ports, running services, known vulnerabilities, and hosting context for threat intelligence enrichment and incident triage.


- **performing-malware-hash-enrichment-with-virustotal**
  Enrich malware file hashes using the VirusTotal API to retrieve detection rates, behavioral analysis, YARA matches, and contextual threat intelligence for incident triage and IOC validation.


- **performing-malware-ioc-extraction**
  Malware IOC extraction is the process of analyzing malicious software to identify actionable indicators of compromise including file hashes, network indicators (C2 domains, IP addresses, URLs), regist


- **performing-osint-with-spiderfoot**
  Automate OSINT collection using SpiderFoot REST API and CLI for target profiling, module-based reconnaissance, and structured result analysis across 200+ data sources


- **performing-paste-site-monitoring-for-credentials**
  Monitor paste sites like Pastebin and GitHub Gists for leaked credentials, API keys, and sensitive data dumps using automated scraping and keyword matching to detect breaches early.


- **performing-threat-emulation-with-atomic-red-team**
  Executes Atomic Red Team tests for MITRE ATT&CK technique validation using the atomic-operator Python framework. Loads test definitions from YAML atomics, runs attack simulations, and validates detection coverage. Use when testing SIEM detection rules, validating EDR coverage, or conducting purple team exercises.


- **performing-threat-intelligence-sharing-with-misp**
  Use PyMISP to create, enrich, and share threat intelligence events on a MISP platform, including IOC management, feed integration, STIX export, and community sharing workflows.


- **performing-threat-landscape-assessment-for-sector**
  Conduct a sector-specific threat landscape assessment by analyzing threat actor targeting patterns, common attack vectors, and industry-specific vulnerabilities to inform organizational risk management.


- **processing-stix-taxii-feeds**
  Processes STIX 2.1 threat intelligence bundles delivered via TAXII 2.1 servers, normalizing objects into platform-native schemas and routing them to appropriate consuming systems. Use when onboarding new TAXII collection endpoints, automating bi-directional intelligence sharing with ISACs, or building pipeline validation for malformed STIX bundles. Activates for requests involving OASIS STIX, TAXII server configuration, MISP TAXII, or Cortex XSOAR feed integrations.


- **profiling-threat-actor-groups**
  Develops comprehensive threat actor profiles for APT groups, criminal organizations, and hacktivist collectives by aggregating TTP documentation, historical campaign data, tooling fingerprints, and attribution indicators from multiple intelligence sources. Use when briefing executives on sector-specific threats, updating threat model assumptions, or prioritizing defensive controls against specific adversaries. Activates for requests involving MITRE ATT&CK Groups, Mandiant APT profiles, CrowdStrike adversary naming, or sector-specific threat briefings.


- **tracking-threat-actor-infrastructure**
  Threat actor infrastructure tracking involves monitoring and mapping adversary-controlled assets including command-and-control (C2) servers, phishing domains, exploit kit hosts, bulletproof hosting, a
