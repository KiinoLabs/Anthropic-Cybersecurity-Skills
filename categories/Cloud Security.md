# Cloud Security Skills

*Generated category with 60 skills*


- **analyzing-cloud-storage-access-patterns**
  Detect abnormal access patterns in AWS S3, GCS, and Azure Blob Storage by analyzing CloudTrail Data Events, GCS audit logs, and Azure Storage Analytics. Identifies after-hours bulk downloads, access from new IP addresses, unusual API calls (GetObject spikes), and potential data exfiltration using statistical baselines and time-series anomaly detection.


- **analyzing-office365-audit-logs-for-compromise**
  Parse Office 365 Unified Audit Logs via Microsoft Graph API to detect email forwarding rule creation, inbox delegation, suspicious OAuth app grants, and other indicators of account compromise.


- **auditing-aws-s3-bucket-permissions**
  Systematically audit AWS S3 bucket permissions to identify publicly accessible buckets, overly permissive ACLs, misconfigured bucket policies, and missing encryption settings using AWS CLI, S3audit, and Prowler to enforce least-privilege data access controls.


- **auditing-azure-active-directory-configuration**
  Auditing Microsoft Entra ID (Azure Active Directory) configuration to identify risky authentication policies, overly permissive role assignments, stale accounts, conditional access gaps, and guest user risks using AzureAD PowerShell, Microsoft Graph API, and ScoutSuite.


- **auditing-cloud-with-cis-benchmarks**
  This skill details how to conduct cloud security audits using Center for Internet Security benchmarks for AWS, Azure, and GCP. It covers interpreting CIS Foundations Benchmark controls, running automated assessments with tools like Prowler and ScoutSuite, remediating failed controls, and maintaining continuous compliance monitoring against CIS v5 for AWS, v4 for Azure, and v4 for GCP.


- **auditing-gcp-iam-permissions**
  Auditing Google Cloud Platform IAM permissions to identify overly permissive bindings, primitive role usage, service account key proliferation, and cross-project access risks using gcloud CLI, Policy Analyzer, and IAM Recommender.


- **auditing-kubernetes-cluster-rbac**
  Auditing Kubernetes cluster RBAC configurations to identify overly permissive roles, wildcard permissions, dangerous ClusterRoleBindings, service account abuse, and privilege escalation paths using kubectl, rbac-tool, KubiScan, and Kubeaudit.


- **auditing-terraform-infrastructure-for-security**
  Auditing Terraform infrastructure-as-code for security misconfigurations using Checkov, tfsec, Terrascan, and OPA/Rego policies to detect overly permissive IAM policies, public resource exposure, missing encryption, and insecure defaults before cloud deployment.


- **building-cloud-security-posture-management**
  This skill guides security architects through designing and implementing a cloud security posture management program that continuously monitors infrastructure configurations across AWS, Azure, and GCP. It covers selecting CSPM tooling such as Wiz, Prisma Cloud, or native services, defining policy baselines, automating drift detection, and integrating posture findings into SOC workflows.


- **building-cloud-siem-with-sentinel**
  This skill covers deploying Microsoft Sentinel as a cloud-native SIEM and SOAR platform for centralized security operations. It details configuring data connectors for multi-cloud log ingestion, writing KQL detection queries, building automated response playbooks with Logic Apps, and leveraging the Sentinel data lake for petabyte-scale threat hunting across AWS, Azure, and GCP security telemetry.


- **conducting-cloud-penetration-testing**
  This skill outlines methodologies for performing authorized penetration testing against AWS, Azure, and GCP cloud environments. It covers understanding the shared responsibility model for testing scope, leveraging cloud-specific attack tools like Pacu and ScoutSuite, exploiting IAM misconfigurations, testing for SSRF to cloud metadata services, and reporting findings aligned to MITRE ATT&CK Cloud matrix.


- **detecting-aws-cloudtrail-anomalies**
  Detect unusual API call patterns in AWS CloudTrail logs using boto3, statistical baselining, and behavioral analysis to identify credential compromise, privilege escalation, and unauthorized resource access.


- **detecting-aws-credential-exposure-with-trufflehog**
  Detecting exposed AWS credentials in source code repositories, CI/CD pipelines, and configuration files using TruffleHog, git-secrets, and AWS-native detection mechanisms to prevent credential theft and unauthorized account access.


- **detecting-aws-guardduty-findings-automation**
  Automate AWS GuardDuty threat detection findings processing using EventBridge and Lambda to enable real-time incident response, automatic quarantine of compromised resources, and security notification workflows.


- **detecting-aws-iam-privilege-escalation**
  Detect AWS IAM privilege escalation paths using boto3 and Cloudsplaining policy analysis to identify overly permissive policies, dangerous permission combinations, and least-privilege violations


- **detecting-azure-lateral-movement**
  Detect lateral movement in Azure AD/Entra ID environments using Microsoft Graph API audit logs, Azure Sentinel KQL hunting queries, and sign-in anomaly correlation to identify privilege escalation, token theft, and cross-tenant pivoting.


- **detecting-azure-service-principal-abuse**
  Detect and investigate Azure service principal abuse including privilege escalation, credential compromise, admin consent bypass, and unauthorized enumeration in Microsoft Entra ID environments.


- **detecting-azure-storage-account-misconfigurations**
  Audit Azure Blob and ADLS storage accounts for public access exposure, weak or long-lived SAS tokens, missing encryption at rest, disabled HTTPS-only traffic, and outdated TLS versions using the azure-mgmt-storage Python SDK.


- **detecting-cloud-cryptomining-activity**
  Detecting unauthorized cryptocurrency mining activity in cloud environments by analyzing compute usage anomalies, network traffic to mining pools, GuardDuty findings, and container workload behavior using AWS, Azure, and GCP native security services.


- **detecting-cloud-threats-with-guardduty**
  This skill teaches security teams how to deploy and operationalize Amazon GuardDuty for continuous threat detection across AWS accounts and workloads. It covers enabling protection plans for S3, EKS, EC2 runtime monitoring, and Lambda, interpreting finding severity levels, and building automated response workflows using EventBridge and Lambda.


- **detecting-compromised-cloud-credentials**
  Detecting compromised cloud credentials across AWS, Azure, and GCP by analyzing anomalous API activity, impossible travel patterns, unauthorized resource provisioning, and credential abuse indicators using GuardDuty, Defender for Identity, and SCC Event Threat Detection.


- **detecting-cryptomining-in-cloud**
  This skill teaches security teams how to detect and respond to unauthorized cryptocurrency mining operations in cloud environments. It covers identifying cryptomining indicators through compute usage anomalies, network traffic patterns to mining pools, GuardDuty CryptoCurrency findings, and runtime process monitoring on EC2, ECS, EKS, and Azure Automation workloads.


- **detecting-misconfigured-azure-storage**
  Detecting misconfigured Azure Storage accounts including publicly accessible blob containers, missing encryption settings, overly permissive SAS tokens, disabled logging, and network access violations using Azure CLI, PowerShell, and Microsoft Defender for Storage.


- **detecting-s3-data-exfiltration-attempts**
  Detecting data exfiltration attempts from AWS S3 buckets by analyzing CloudTrail S3 data events, VPC Flow Logs, GuardDuty findings, Amazon Macie alerts, and S3 access patterns to identify unauthorized bulk downloads and cross-account data transfers.


- **detecting-shadow-it-cloud-usage**
  Detect unauthorized SaaS and cloud service usage (shadow IT) by analyzing proxy logs, DNS query logs, and netflow data using Python pandas for traffic pattern analysis and domain classification.


- **detecting-suspicious-oauth-application-consent**
  Detect risky OAuth application consent grants in Azure AD / Microsoft Entra ID using Microsoft Graph API, audit logs, and permission analysis to identify illicit consent grant attacks.


- **implementing-aws-config-rules-for-compliance**
  Implementing AWS Config rules for continuous compliance monitoring of AWS resources, deploying managed and custom rules aligned to CIS and PCI DSS frameworks, configuring automatic remediation with SSM Automation, and aggregating compliance data across accounts.


- **implementing-aws-macie-for-data-classification**
  Implement Amazon Macie to automatically discover, classify, and protect sensitive data in S3 buckets using machine learning and pattern matching for PII, financial data, and credentials detection.


- **implementing-aws-security-hub**
  This skill covers deploying AWS Security Hub as a centralized cloud security posture management platform that aggregates findings from GuardDuty, Inspector, Macie, and third-party tools. It details enabling security standards like CIS AWS Foundations Benchmark, configuring automated remediation, and building executive dashboards for compliance tracking across multi-account AWS organizations.


- **implementing-aws-security-hub-compliance**
  Implementing AWS Security Hub to aggregate security findings across AWS accounts, enable compliance standards like CIS AWS Foundations and PCI DSS, configure automated remediation with EventBridge and Lambda, and create custom security insights for organizational risk management.


- **implementing-azure-defender-for-cloud**
  Implementing Microsoft Defender for Cloud to enable cloud security posture management, workload protection across VMs, containers, databases, and storage, configure security recommendations, and set up adaptive security controls with automated remediation.


- **implementing-cloud-dlp-for-data-protection**
  Implementing Cloud Data Loss Prevention (DLP) using Amazon Macie, Azure Information Protection, and Google Cloud DLP API to discover, classify, and protect sensitive data across cloud storage, databases, and data pipelines.


- **implementing-cloud-security-posture-management**
  Implementing Cloud Security Posture Management (CSPM) to continuously monitor multi-cloud environments for misconfigurations, compliance violations, and security risks using Prowler, ScoutSuite, AWS Security Hub, Azure Defender, and GCP Security Command Center.


- **implementing-cloud-trail-log-analysis**
  Implementing AWS CloudTrail log analysis for security monitoring, threat detection, and forensic investigation using Athena, CloudWatch Logs Insights, and SIEM integration to identify unauthorized access, privilege escalation, and suspicious API activity.


- **implementing-cloud-waf-rules**
  This skill covers deploying and tuning Web Application Firewall rules on AWS WAF, Azure WAF, and Cloudflare to protect cloud-hosted applications against OWASP Top 10 attacks. It details configuring managed rule sets, creating custom rules for business logic protection, implementing rate limiting, deploying bot management, and reducing false positives through rule tuning and logging analysis.


- **implementing-cloud-workload-protection**
  Implements cloud workload protection using boto3 and google-cloud APIs for runtime security monitoring, process anomaly detection, and file integrity checking on EC2/GCE instances. Scans for cryptomining, reverse shells, and unauthorized binaries. Use when building runtime security controls for cloud compute workloads.


- **implementing-gcp-binary-authorization**
  Implement GCP Binary Authorization to enforce deploy-time security controls that ensure only trusted, attested container images are deployed to Google Kubernetes Engine and Cloud Run.


- **implementing-gcp-organization-policy-constraints**
  Implement GCP Organization Policy constraints to enforce security guardrails across the entire resource hierarchy, restricting risky configurations and ensuring compliance at organization, folder, and project levels.


- **implementing-gcp-vpc-firewall-rules**
  Implementing and auditing GCP VPC firewall rules to enforce network segmentation, restrict ingress and egress traffic, apply hierarchical firewall policies across the organization, and monitor firewall rule effectiveness using VPC Flow Logs.


- **implementing-secrets-management-with-vault**
  This skill covers deploying HashiCorp Vault for centralized secrets management across cloud environments, including dynamic secret generation for databases and cloud providers, transit encryption, PKI certificate management, and Kubernetes integration. It addresses eliminating hardcoded credentials from application code and CI/CD pipelines by implementing short-lived, automatically rotated secrets.


- **implementing-zero-trust-in-cloud**
  This skill guides organizations through implementing zero trust architecture in cloud environments following NIST SP 800-207 and Google BeyondCorp principles. It covers identity-centric access controls, micro-segmentation, continuous verification, device trust assessment, and deploying Identity-Aware Proxy to eliminate implicit network trust in AWS, Azure, and GCP environments.


- **implementing-zero-trust-network-access**
  Implementing Zero Trust Network Access (ZTNA) in cloud environments by configuring identity-aware proxies, micro-segmentation, continuous verification with conditional access policies, and replacing traditional VPN-based access with BeyondCorp-style architectures across AWS, Azure, and GCP.


- **managing-cloud-identity-with-okta**
  This skill covers implementing Okta as a centralized identity provider for cloud environments, configuring SSO integration with AWS, Azure, and GCP, deploying phishing- resistant MFA with Okta FastPass, managing lifecycle automation for user provisioning and deprovisioning, and enforcing adaptive access policies based on device posture and risk signals.


- **performing-aws-account-enumeration-with-scout-suite**
  Perform comprehensive security posture assessment of AWS accounts using ScoutSuite to enumerate resources, identify misconfigurations, and generate actionable security reports.


- **performing-aws-privilege-escalation-assessment**
  Performing authorized privilege escalation assessments in AWS environments to identify IAM misconfigurations that allow users or roles to elevate their permissions using Pacu, CloudFox, Principal Mapper, and manual IAM policy analysis techniques.


- **performing-cloud-asset-inventory-with-cartography**
  Perform comprehensive cloud asset inventory and relationship mapping using Cartography to build a Neo4j security graph of infrastructure assets, IAM permissions, and attack paths across AWS, GCP, and Azure.


- **performing-cloud-forensics-with-aws-cloudtrail**
  Perform forensic investigation of AWS environments using CloudTrail logs to reconstruct attacker activity, identify compromised credentials, and analyze API call patterns.


- **performing-cloud-native-forensics-with-falco**
  Uses Falco YAML rules for runtime threat detection in containers and Kubernetes, monitoring syscalls for shell spawns, file tampering, network anomalies, and privilege escalation. Manages Falco rules via the Falco gRPC API and parses Falco alert output. Use when building container runtime security or investigating k8s cluster compromises.


- **performing-cloud-penetration-testing-with-pacu**
  Performing authorized AWS penetration testing using Pacu, the open-source AWS exploitation framework, to enumerate IAM configurations, discover privilege escalation paths, test credential harvesting, and validate security controls through systematic attack simulation.


- **performing-gcp-penetration-testing-with-gcpbucketbrute**
  Perform GCP security testing using GCPBucketBrute for storage bucket enumeration, gcloud IAM privilege escalation path analysis, and service account permission auditing


- **performing-gcp-security-assessment-with-forseti**
  Performing comprehensive security assessments of Google Cloud Platform environments using Forseti Security, Security Command Center, and gcloud CLI to audit IAM policies, firewall rules, storage permissions, and compliance against CIS GCP Foundations Benchmark.


- **performing-serverless-function-security-review**
  Performing security reviews of serverless functions across AWS Lambda, Azure Functions, and GCP Cloud Functions to identify overly permissive execution roles, insecure environment variables, injection vulnerabilities, and missing runtime protections.


- **remediating-s3-bucket-misconfiguration**
  This skill provides step-by-step procedures for identifying and remediating Amazon S3 bucket misconfigurations that expose sensitive data to unauthorized access. It covers enabling S3 Block Public Access at account and bucket levels, auditing bucket policies and ACLs, enforcing encryption, configuring access logging, and deploying automated remediation using AWS Config and Lambda.


- **securing-api-gateway-with-aws-waf**
  Securing API Gateway endpoints with AWS WAF by configuring managed rule groups for OWASP Top 10 protection, creating custom rate limiting rules, implementing bot control, setting up IP reputation filtering, and monitoring WAF metrics for security effectiveness.


- **securing-aws-iam-permissions**
  This skill guides practitioners through hardening AWS Identity and Access Management configurations to enforce least privilege access across cloud accounts. It covers IAM policy scoping, permission boundaries, Access Analyzer integration, and credential rotation strategies to reduce the blast radius of compromised identities.


- **securing-aws-lambda-execution-roles**
  Securing AWS Lambda execution roles by implementing least-privilege IAM policies, applying permission boundaries, restricting resource-based policies, using IAM Access Analyzer to validate permissions, and enforcing role scoping through SCPs.


- **securing-azure-with-microsoft-defender**
  This skill instructs security practitioners on deploying Microsoft Defender for Cloud as a cloud-native application protection platform for Azure, multi-cloud, and hybrid environments. It covers enabling Defender plans for servers, containers, storage, and databases, configuring security recommendations, managing Secure Score, and integrating with the unified Defender portal for centralized threat management.


- **securing-container-registry-images**
  Securing container registry images by implementing vulnerability scanning with Trivy and Grype, enforcing image signing with Cosign and Sigstore, configuring registry access controls, and building CI/CD pipelines that prevent deploying unscanned or unsigned images.


- **securing-kubernetes-on-cloud**
  This skill covers hardening managed Kubernetes clusters on EKS, AKS, and GKE by implementing Pod Security Standards, network policies, workload identity, RBAC scoping, image admission controls, and runtime security monitoring. It addresses cloud-specific security features including IRSA for EKS, Workload Identity for GKE, and Managed Identities for AKS.


- **securing-serverless-functions**
  This skill covers security hardening for serverless compute platforms including AWS Lambda, Azure Functions, and Google Cloud Functions. It addresses least privilege IAM roles, dependency vulnerability scanning, secrets management integration, input validation, function URL authentication, and runtime monitoring to protect against injection attacks, credential theft, and supply chain compromises.
