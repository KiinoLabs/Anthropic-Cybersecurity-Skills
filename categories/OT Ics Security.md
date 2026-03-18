# OT Ics Security Skills

*Generated category with 28 skills*


- **detecting-anomalies-in-industrial-control-systems**
  This skill covers deploying anomaly detection systems for industrial control environments using machine learning models trained on OT network baselines, physics-based process models, and behavioral analysis of industrial protocol communications. It addresses building normal behavior profiles for SCADA polling patterns, detecting deviations in Modbus/DNP3/OPC UA traffic, identifying rogue devices, and correlating network anomalies with physical process data from historians.


- **detecting-attacks-on-historian-servers**
  Detect cyber attacks targeting OT historian servers (OSIsoft PI, Ignition, Wonderware) that sit at the IT/OT boundary and serve as pivot points for lateral movement between enterprise and control networks, including data manipulation, unauthorized queries, and exploitation of historian-specific vulnerabilities.


- **detecting-attacks-on-scada-systems**
  This skill covers detecting cyber attacks targeting Supervisory Control and Data Acquisition (SCADA) systems including man-in-the-middle attacks on industrial protocols, unauthorized command injection into PLCs, HMI compromise, historian data manipulation, and denial-of-service against control system communications. It leverages OT-specific intrusion detection systems, industrial protocol anomaly detection, and process data analytics to identify attacks that traditional IT security tools miss.


- **detecting-dnp3-protocol-anomalies**
  Detect anomalies in DNP3 (Distributed Network Protocol 3) communications used in SCADA systems by monitoring for unauthorized control commands, firmware update attempts, protocol violations, and deviations from baseline traffic patterns using deep packet inspection and machine learning approaches.


- **detecting-modbus-command-injection-attacks**
  Detect command injection attacks against Modbus TCP/RTU protocol in ICS environments by monitoring for unauthorized write operations, anomalous function codes, malformed frames, and deviations from established communication baselines using ICS-aware IDS and protocol deep packet inspection.


- **detecting-modbus-protocol-anomalies**
  This skill covers detecting anomalies in Modbus/TCP and Modbus RTU communications in industrial control systems. It addresses function code monitoring, register range validation, timing analysis, unauthorized client detection, and deep packet inspection for malformed Modbus frames. The skill leverages Zeek with Modbus protocol analyzers, Suricata IDS with OT rules, and custom Python-based detection using Markov chain models for normal Modbus transaction sequences.


- **detecting-stuxnet-style-attacks**
  This skill covers detecting sophisticated cyber-physical attacks that follow the Stuxnet attack pattern of modifying PLC logic while spoofing sensor readings to hide the manipulation from operators. It addresses PLC logic integrity monitoring, physics-based process anomaly detection, engineering workstation compromise indicators, USB-borne attack vectors, and multi-stage attack chain detection spanning IT-to-OT lateral movement through to process manipulation.


- **implementing-conduit-security-for-ot-remote-access**
  Implement secure conduit architecture for OT remote access following IEC 62443 zones and conduits model, deploying jump servers, MFA-enabled gateways, session recording, and approval-based workflows to control vendor and engineer access to industrial control systems without exposing OT networks directly.


- **implementing-dragos-platform-for-ot-monitoring**
  Deploy and configure the Dragos Platform for OT network monitoring, leveraging its 600+ industrial protocol parsers, intelligence-driven threat detection analytics, and asset visibility capabilities to protect ICS environments against threat groups like VOLTZITE, GRAPHITE, and BAUXITE.


- **implementing-ics-firewall-with-tofino**
  Deploy and configure Tofino industrial firewalls from Belden/Hirschmann to protect SCADA systems and PLCs using deep packet inspection for OT protocols including Modbus, EtherNet/IP, OPC, and S7comm, enforcing granular access control between ICS security zones.


- **implementing-iec-62443-security-zones**
  This skill covers designing and implementing security zones and conduits for industrial automation and control systems (IACS) per IEC 62443-3-2. It addresses zone partitioning based on risk assessment, assigning Security Level targets (SL-T), designing conduit security controls, implementing microsegmentation with industrial firewalls, and validating zone architecture through traffic analysis and penetration testing against the Purdue Reference Model.


- **implementing-nerc-cip-compliance-controls**
  This skill covers implementing North American Electric Reliability Corporation Critical Infrastructure Protection (NERC CIP) compliance controls for Bulk Electric System (BES) cyber systems. It addresses asset categorization (CIP-002), electronic security perimeters (CIP-005), system security management (CIP-007), configuration management (CIP-010), supply chain risk management (CIP-013), and the 2025 updates including mandatory MFA for remote access and expanded low-impact asset requirements.


- **implementing-network-segmentation-for-ot**
  This skill covers implementing network segmentation in Operational Technology environments using VLANs, industrial firewalls, data diodes, and software-defined networking. It addresses the Purdue Model-based segmentation strategy, migration from flat networks to segmented architectures without disrupting operations, configuring OT-aware firewalls with industrial protocol deep packet inspection, and validating segmentation effectiveness through traffic analysis.


- **implementing-ot-incident-response-playbook**
  Develop and implement OT-specific incident response playbooks aligned with SANS PICERL framework, IEC 62443, and NIST SP 800-82 that address unique ICS challenges including safety-critical systems, limited downtime tolerance, and coordination between IT SOC, OT engineering, and plant operations teams.


- **implementing-ot-network-traffic-analysis-with-nozomi**
  Deploy Nozomi Networks Guardian sensors for passive OT network traffic analysis to achieve comprehensive asset visibility, real-time threat detection, and vulnerability assessment across industrial control systems without disrupting operations, leveraging behavioral anomaly detection and protocol-aware monitoring.


- **implementing-patch-management-for-ot-systems**
  This skill covers implementing a structured patch management program for OT/ICS environments where traditional IT patching approaches can cause process disruption or safety hazards. It addresses vendor compatibility testing, risk-based patch prioritization, staged deployment through test environments, maintenance window coordination, rollback procedures, and compensating controls when patches cannot be applied due to operational constraints or vendor restrictions.


- **implementing-purdue-model-network-segmentation**
  Implement network segmentation based on the Purdue Enterprise Reference Architecture (PERA) model to separate industrial control system networks into hierarchical security zones from Level 0 physical process through Level 5 enterprise, enforcing strict traffic control between OT and IT domains.


- **performing-ics-asset-discovery-with-claroty**
  Perform comprehensive ICS/OT asset discovery using Claroty xDome platform, leveraging passive monitoring, Claroty Edge active queries, and integration ecosystem to gain full visibility into industrial control system assets including PLCs, RTUs, HMIs, and network infrastructure across Purdue Model levels.


- **performing-oil-gas-cybersecurity-assessment**
  This skill covers conducting cybersecurity assessments specific to oil and gas facilities including upstream (exploration/production), midstream (pipeline/transport), and downstream (refining/distribution) operations. It addresses SCADA systems controlling pipeline operations, DCS for refinery process control, safety instrumented systems for hazardous processes, remote terminal units at unmanned wellhead sites, and compliance with API 1164, TSA Pipeline Security Directives, IEC 62443, and NIST Cybersecurity Framework for critical infrastructure.


- **performing-ot-network-security-assessment**
  This skill covers conducting comprehensive security assessments of Operational Technology (OT) networks including SCADA systems, DCS architectures, and industrial control system communication paths. It addresses the Purdue Reference Model layers, identifies IT/OT convergence risks, evaluates firewall rules between zones, and maps industrial protocol traffic (Modbus, DNP3, OPC UA, EtherNet/IP) to detect misconfigurations, unauthorized connections, and attack surfaces in critical infrastructure.


- **performing-ot-vulnerability-assessment-with-claroty**
  This skill covers performing vulnerability assessments in OT environments using the Claroty xDome platform for comprehensive asset discovery, risk scoring, vulnerability correlation, and remediation prioritization. It addresses passive vulnerability identification through traffic analysis, active safe querying of OT devices, integration with CVE databases and ICS-CERT advisories, and risk-based prioritization that accounts for operational impact and compensating controls.


- **performing-ot-vulnerability-scanning-safely**
  Perform vulnerability scanning in OT/ICS environments safely using passive monitoring, native protocol queries, and carefully controlled active scanning with Tenable OT Security to identify vulnerabilities without disrupting industrial processes or crashing legacy controllers.


- **performing-plc-firmware-security-analysis**
  This skill covers analyzing Programmable Logic Controller (PLC) firmware for security vulnerabilities including hardcoded credentials, insecure update mechanisms, backdoor functions, memory corruption flaws, and undocumented debug interfaces. It addresses firmware extraction from common PLC platforms (Siemens S7, Allen-Bradley, Schneider Modicon), static analysis of firmware images, dynamic analysis in emulated environments, and comparison against known-good baselines to detect tampering.


- **performing-power-grid-cybersecurity-assessment**
  This skill covers conducting cybersecurity assessments of electric power grid infrastructure including generation facilities, transmission substations, distribution systems, and energy management system (EMS) control centers. It addresses NERC CIP compliance verification, substation automation security, IEC 61850 protocol analysis, synchrophasor (PMU) network security, and the unique threat landscape targeting power grid operations as demonstrated by Industroyer/CrashOverride and related attacks.


- **performing-s7comm-protocol-security-analysis**
  Perform security analysis of Siemens S7comm and S7CommPlus protocols used by SIMATIC S7 PLCs to identify vulnerabilities including replay attacks, integrity bypass, unauthorized CPU stop commands, and program download manipulation exploiting weaknesses in S7-300, S7-400, S7-1200, and S7-1500 controllers.


- **performing-scada-hmi-security-assessment**
  Perform security assessments of SCADA Human-Machine Interface (HMI) systems to identify vulnerabilities in web-based HMIs, thin-client configurations, authentication mechanisms, and communication channels between HMI and PLCs, aligned with IEC 62443 and NIST SP 800-82 guidelines.


- **securing-historian-server-in-ot-environment**
  This skill covers hardening and securing process historian servers (OSIsoft PI, Honeywell PHD, GE Proficy, AVEVA Historian) in OT environments. It addresses network placement across Purdue levels, access control for historian interfaces, data replication through DMZ using data diodes or PI-to-PI connectors, SQL injection prevention in historian queries, and integrity protection of process data used for safety analysis, regulatory reporting, and process optimization.


- **securing-remote-access-to-ot-environment**
  This skill covers implementing secure remote access to OT/ICS environments for operators, engineers, and vendors while preventing unauthorized access that could compromise industrial operations. It addresses jump server architecture, multi-factor authentication, session recording, privileged access management, vendor remote access controls, and compliance with IEC 62443 and NERC CIP-005 remote access requirements.
