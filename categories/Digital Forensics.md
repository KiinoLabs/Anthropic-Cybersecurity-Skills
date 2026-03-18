# Digital Forensics Skills

*Generated category with 37 skills*


- **acquiring-disk-image-with-dd-and-dcfldd**
  Create forensically sound bit-for-bit disk images using dd and dcfldd while preserving evidence integrity through hash verification.


- **analyzing-browser-forensics-with-hindsight**
  Analyze Chromium-based browser artifacts using Hindsight to extract browsing history, downloads, cookies, cached content, autofill data, saved passwords, and browser extensions from Chrome, Edge, Brave, and Opera for forensic investigation.


- **analyzing-disk-image-with-autopsy**
  Perform comprehensive forensic analysis of disk images using Autopsy to recover files, examine artifacts, and build investigation timelines.


- **analyzing-docker-container-forensics**
  Investigate compromised Docker containers by analyzing images, layers, volumes, logs, and runtime artifacts to identify malicious activity and evidence.


- **analyzing-email-headers-for-phishing-investigation**
  Parse and analyze email headers to trace the origin of phishing emails, verify sender authenticity, and identify spoofing through SPF, DKIM, and DMARC validation.


- **analyzing-linux-kernel-rootkits**
  Detect kernel-level rootkits in Linux memory dumps using Volatility3 linux plugins (check_syscall, lsmod, hidden_modules), rkhunter system scanning, and /proc vs /sys discrepancy analysis to identify hooked syscalls, hidden kernel modules, and tampered system structures.


- **analyzing-linux-system-artifacts**
  Examine Linux system artifacts including auth logs, cron jobs, shell history, and system configuration to uncover evidence of compromise or unauthorized activity.


- **analyzing-lnk-file-and-jump-list-artifacts**
  Analyze Windows LNK shortcut files and Jump List artifacts to establish evidence of file access, program execution, and user activity using LECmd, JLECmd, and manual binary parsing of the Shell Link Binary format.


- **analyzing-mft-for-deleted-file-recovery**
  Analyze the NTFS Master File Table ($MFT) to recover metadata and content of deleted files by examining MFT record entries, $LogFile, $UsnJrnl, and MFT slack space using MFTECmd, analyzeMFT, and X-Ways Forensics.


- **analyzing-outlook-pst-for-email-forensics**
  Analyze Microsoft Outlook PST and OST files for email forensic evidence including message content, headers, attachments, deleted items, and metadata using libpff, pst-utils, and forensic email analysis tools for legal investigations and incident response.


- **analyzing-prefetch-files-for-execution-history**
  Parse Windows Prefetch files to determine program execution history including run counts, timestamps, and referenced files for forensic investigation.


- **analyzing-slack-space-and-file-system-artifacts**
  Examine file system slack space, MFT entries, USN journal, and alternate data streams to recover hidden data and reconstruct file activity on NTFS volumes.


- **analyzing-usb-device-connection-history**
  Investigate USB device connection history from Windows registry, event logs, and setupapi logs to track removable media usage and potential data exfiltration.


- **analyzing-windows-amcache-artifacts**
  Parse and analyze Windows Amcache.hve registry hive to extract program execution evidence, file metadata, SHA-1 hashes, and device connection history for digital forensics and incident response investigations.


- **analyzing-windows-lnk-files-for-artifacts**
  Parse Windows LNK shortcut files to extract target paths, timestamps, volume information, and machine identifiers for forensic timeline reconstruction.


- **analyzing-windows-prefetch-with-python**
  Parse Windows Prefetch files using the windowsprefetch Python library to reconstruct application execution history, detect renamed or masquerading binaries, and identify suspicious program execution patterns.


- **analyzing-windows-registry-for-artifacts**
  Extract and analyze Windows Registry hives to uncover user activity, installed software, autostart entries, and evidence of system compromise.


- **analyzing-windows-shellbag-artifacts**
  Analyze Windows Shellbag registry artifacts to reconstruct folder browsing activity, detect access to removable media and network shares, and establish user interaction with directories even after deletion using SBECmd and ShellBags Explorer.


- **extracting-browser-history-artifacts**
  Extract and analyze browser history, cookies, cache, downloads, and bookmarks from Chrome, Firefox, and Edge for forensic evidence of user web activity.


- **extracting-credentials-from-memory-dump**
  Extract cached credentials, password hashes, Kerberos tickets, and authentication tokens from memory dumps using Volatility and Mimikatz for forensic investigation.


- **extracting-windows-event-logs-artifacts**
  Extract, parse, and analyze Windows Event Logs (EVTX) using Chainsaw, Hayabusa, and EvtxECmd to detect lateral movement, persistence, and privilege escalation.


- **investigating-ransomware-attack-artifacts**
  Identify, collect, and analyze ransomware attack artifacts to determine the variant, initial access vector, encryption scope, and recovery options.


- **performing-cloud-forensics-investigation**
  Conduct forensic investigations in cloud environments by collecting and analyzing logs, snapshots, and metadata from AWS, Azure, and GCP services.


- **performing-cloud-storage-forensic-acquisition**
  Perform forensic acquisition and analysis of cloud storage services including Google Drive, OneDrive, Dropbox, and Box by collecting both API-based remote data and local sync client artifacts from endpoint devices.


- **performing-file-carving-with-foremost**
  Recover files from disk images and unallocated space using Foremost's header-footer signature carving to extract evidence regardless of file system state.


- **performing-linux-log-forensics-investigation**
  Perform forensic investigation of Linux system logs including syslog, auth.log, systemd journal, kern.log, and application logs to reconstruct user activity, detect unauthorized access, and establish event timelines on compromised Linux systems.


- **performing-log-analysis-for-forensic-investigation**
  Collect, parse, and correlate system, application, and security logs to reconstruct events and establish timelines during forensic investigations.


- **performing-malware-persistence-investigation**
  Systematically investigate all persistence mechanisms on Windows and Linux systems to identify how malware survives reboots and maintains access.


- **performing-memory-forensics-with-volatility3**
  Analyze volatile memory dumps using Volatility 3 to extract running processes, network connections, loaded modules, and evidence of malicious activity.


- **performing-mobile-device-forensics-with-cellebrite**
  Acquire and analyze mobile device data using Cellebrite UFED and open-source tools to extract communications, location data, and application artifacts.


- **performing-network-forensics-with-wireshark**
  Capture and analyze network traffic using Wireshark and tshark to reconstruct network events, extract artifacts, and identify malicious communications.


- **performing-network-packet-capture-analysis**
  Perform forensic analysis of network packet captures (PCAP/PCAPNG) using Wireshark, tshark, and tcpdump to reconstruct network communications, extract transferred files, identify malicious traffic, and establish evidence of data exfiltration or command-and-control activity.


- **performing-sqlite-database-forensics**
  Perform forensic analysis of SQLite databases to recover deleted records from freelists and WAL files, decode encoded timestamps, and extract evidence from browser history, messaging apps, and mobile device databases.


- **performing-steganography-detection**
  Detect and extract hidden data embedded in images, audio, and other media files using steganalysis tools to uncover covert communication channels.


- **performing-timeline-reconstruction-with-plaso**
  Build comprehensive forensic super-timelines using Plaso (log2timeline) to correlate events across file systems, logs, and artifacts into a unified chronological view.


- **performing-windows-artifact-analysis-with-eric-zimmerman-tools**
  Perform comprehensive Windows forensic artifact analysis using Eric Zimmerman's open-source EZ Tools suite including KAPE, MFTECmd, PECmd, LECmd, JLECmd, and Timeline Explorer for parsing registry hives, prefetch files, event logs, and file system metadata.


- **recovering-deleted-files-with-photorec**
  Recover deleted files from disk images and storage media using PhotoRec's file signature-based carving engine regardless of file system damage.
