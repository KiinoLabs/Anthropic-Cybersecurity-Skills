# Ransomware Defense Skills

*Generated category with 7 skills*


- **deploying-ransomware-canary-files**
  Deploys and monitors ransomware canary files across critical directories using Python's watchdog library for real-time filesystem event detection. Places strategically named decoy files that mimic high-value targets (financial records, credentials, database exports) in locations ransomware typically enumerates first. Monitors for any read, modify, rename, or delete operations on canary files and triggers immediate alerts via email, Slack webhook, or syslog when interaction is detected, providing early warning before full encryption begins.


- **detecting-ransomware-precursors-in-network**
  Detects early-stage ransomware indicators in network traffic before encryption begins, including initial access broker activity, command-and-control beaconing, credential harvesting, reconnaissance scanning, and staging behavior. Uses network detection tools (Zeek, Suricata, Arkime), SIEM correlation rules, and threat intelligence feeds to identify ransomware precursor patterns such as Cobalt Strike beacons, Mimikatz network signatures, and RDP brute-force attempts. Activates for requests involving pre-ransomware detection, network-based ransomware indicators, or early warning ransomware monitoring.


- **implementing-honeypot-for-ransomware-detection**
  Deploys canary files, honeypot shares, and decoy systems to detect ransomware activity at the earliest possible stage. Configures canary tokens embedded in strategic file locations that trigger alerts when ransomware attempts encryption, uses honeypot network shares that mimic high-value targets, and deploys Thinkst Canary appliances for comprehensive deception-based detection. Activates for requests involving ransomware honeypots, canary files, deception technology for ransomware, or early ransomware alerting.


- **implementing-immutable-backup-with-restic**
  Implements immutable backup strategy using restic with S3-compatible storage and object lock for ransomware-resistant data protection. Automates backup creation, integrity verification via restic check --read-data, snapshot retention policy enforcement, and restore testing. Integrates with AWS S3 Object Lock, MinIO, and Backblaze B2 for WORM (Write Once Read Many) storage that prevents backup deletion or encryption by ransomware actors.


- **implementing-ransomware-backup-strategy**
  Designs and implements a ransomware-resilient backup strategy following the 3-2-1-1-0 methodology (3 copies, 2 media types, 1 offsite, 1 immutable/air-gapped, 0 errors on restore verification). Configures backup schedules aligned to RPO/RTO requirements, implements backup credential isolation to prevent ransomware from compromising backup infrastructure, and establishes automated restore testing. Activates for requests involving ransomware backup planning, backup resilience, air-gapped backup design, or backup recovery point objective configuration.


- **performing-ransomware-tabletop-exercise**
  Plans and facilitates tabletop exercises simulating ransomware incidents to test organizational readiness, decision-making, and communication procedures. Designs realistic scenarios based on current ransomware threat actors (LockBit, ALPHV/BlackCat, Cl0p), injects covering double extortion, backup destruction, and regulatory notification requirements. Evaluates participant responses against NIST CSF and CISA guidelines. Activates for requests involving ransomware tabletop, incident response exercise, or ransomware readiness drill.


- **recovering-from-ransomware-attack**
  Executes structured recovery from a ransomware incident following NIST and CISA frameworks, including environment isolation, forensic evidence preservation, clean infrastructure rebuild, prioritized system restoration from verified backups, credential reset, and validation against re-infection. Covers Active Directory recovery, database restoration, and application stack rebuild in dependency order. Activates for requests involving ransomware recovery, post-encryption restoration, or disaster recovery from ransomware.
