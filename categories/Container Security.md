# Container Security Skills

*Generated category with 30 skills*


- **analyzing-kubernetes-audit-logs**
  Parses Kubernetes API server audit logs (JSON lines) to detect exec-into-pod, secret access, RBAC modifications, privileged pod creation, and anonymous API access. Builds threat detection rules from audit event patterns. Use when investigating Kubernetes cluster compromise or building k8s-specific SIEM detection rules.


- **auditing-kubernetes-rbac-permissions**
  Kubernetes Role-Based Access Control (RBAC) auditing systematically reviews roles, cluster roles, bindings, and service account permissions to identify overly permissive access, privilege escalation p


- **detecting-container-drift-at-runtime**
  Detect unauthorized modifications to running containers by monitoring for binary execution drift, file system changes, and configuration deviations from the original container image.


- **detecting-container-escape-attempts**
  Container escape is a critical attack technique where an adversary breaks out of container isolation to access the host system or other containers. Detection involves monitoring for escape indicators


- **detecting-container-escape-with-falco-rules**
  Detect container escape attempts in real-time using Falco runtime security rules that monitor syscalls, file access, and privilege escalation.


- **detecting-privilege-escalation-in-kubernetes-pods**
  Detect and prevent privilege escalation in Kubernetes pods by monitoring security contexts, capabilities, and syscall patterns with Falco and OPA policies.


- **hardening-docker-containers-for-production**
  Hardening Docker containers for production involves applying security best practices aligned with CIS Docker Benchmark v1.8.0 to minimize attack surface, prevent privilege escalation, and enforce leas


- **hardening-docker-daemon-configuration**
  Harden the Docker daemon by configuring daemon.json with user namespace remapping, TLS authentication, rootless mode, and CIS benchmark controls.


- **implementing-container-image-minimal-base-with-distroless**
  Reduce container attack surface by building application images on Google distroless base images that contain only the application runtime with no shell, package manager, or unnecessary OS utilities.


- **implementing-container-network-policies-with-calico**
  Enforce Kubernetes network segmentation using Calico CNI network policies and global network policies to control pod-to-pod traffic, restrict egress, and implement zero-trust microsegmentation.


- **implementing-image-provenance-verification-with-cosign**
  Sign and verify container image provenance using Sigstore Cosign with keyless OIDC-based signing, attestations, and Kubernetes admission enforcement.


- **implementing-kubernetes-network-policy-with-calico**
  Implement Kubernetes network segmentation using Calico NetworkPolicy and GlobalNetworkPolicy for zero-trust pod-to-pod communication.


- **implementing-kubernetes-pod-security-standards**
  Pod Security Standards (PSS) define three levels of security policies -- Privileged, Baseline, and Restricted -- enforced by the Pod Security Admission (PSA) controller built into Kubernetes 1.25+. PS


- **implementing-network-policies-for-kubernetes**
  Kubernetes NetworkPolicies provide pod-level network segmentation by defining ingress and egress rules that control traffic flow between pods, namespaces, and external endpoints. Combined with CNI plu


- **implementing-opa-gatekeeper-for-policy-enforcement**
  Enforce Kubernetes admission policies using OPA Gatekeeper with ConstraintTemplates, Rego rules, and the Gatekeeper policy library.


- **implementing-pod-security-admission-controller**
  Implement Kubernetes Pod Security Admission to enforce baseline and restricted security profiles at namespace level using built-in admission controller.


- **implementing-rbac-hardening-for-kubernetes**
  Harden Kubernetes Role-Based Access Control by implementing least-privilege policies, auditing role bindings, eliminating cluster-admin sprawl, and integrating external identity providers.


- **implementing-runtime-security-with-tetragon**
  Implement eBPF-based runtime security observability and enforcement in Kubernetes clusters using Cilium Tetragon for kernel-level threat detection and policy enforcement.


- **implementing-supply-chain-security-with-in-toto**
  Implement software supply chain integrity verification for container builds using the in-toto framework to create cryptographically signed attestations across CI/CD pipeline steps.


- **performing-container-escape-detection**
  Detects container escape attempts by analyzing namespace configurations, privileged container checks, dangerous capability assignments, and host path mounts using the kubernetes Python client. Identifies CVE-2022-0492 style escapes via cgroup abuse. Use when auditing container security posture or investigating escape attempts.


- **performing-container-security-scanning-with-trivy**
  Scan container images, filesystems, and Kubernetes manifests for vulnerabilities, misconfigurations, exposed secrets, and license compliance issues using Aqua Security Trivy with SBOM generation and CI/CD integration.


- **performing-docker-bench-security-assessment**
  Docker Bench for Security is an open-source script that checks dozens of common best practices around deploying Docker containers in production. Based on the CIS Docker Benchmark, it audits host confi


- **performing-kubernetes-cis-benchmark-with-kube-bench**
  Audit Kubernetes cluster security posture against CIS benchmarks using kube-bench with automated checks for control plane, worker nodes, and RBAC.


- **performing-kubernetes-etcd-security-assessment**
  Assess the security posture of Kubernetes etcd clusters by evaluating encryption at rest, TLS configuration, access controls, backup encryption, and network isolation.


- **performing-kubernetes-penetration-testing**
  Kubernetes penetration testing systematically evaluates cluster security by simulating attacker techniques against the API server, kubelet, etcd, pods, RBAC, network policies, and secrets. Using tools


- **scanning-container-images-with-grype**
  Scan container images for known vulnerabilities using Anchore Grype with SBOM-based matching and configurable severity thresholds.


- **scanning-docker-images-with-trivy**
  Trivy is a comprehensive open-source vulnerability scanner by Aqua Security that detects vulnerabilities in OS packages, language-specific dependencies, misconfigurations, secrets, and license violati


- **scanning-kubernetes-manifests-with-kubesec**
  Perform security risk analysis on Kubernetes resource manifests using Kubesec to identify misconfigurations, privilege escalation risks, and deviations from security best practices.


- **securing-container-registry-with-harbor**
  Harbor is an open-source container registry that provides security features including vulnerability scanning (integrated Trivy), image signing (Notary/Cosign), RBAC, content trust policies, replicatio


- **securing-helm-chart-deployments**
  Secure Helm chart deployments by validating chart integrity, scanning templates for misconfigurations, and enforcing security contexts in Kubernetes releases.
