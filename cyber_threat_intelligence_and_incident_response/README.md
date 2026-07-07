# 43010 - Cyber Threat Intelligence and Incident Response

> **UTS** · Autumn 2026 · 6 credit points · **Final grade: Distinction**

A SecOps-focused subject that pairs **cyber threat intelligence (CTI)** with the full **incident response (IR)** lifecycle - prepare, detect, analyse, contain, eradicate, recover, and learn. Most of the work is hands-on: log analysis in real SIEM/EDR tooling, mapping adversary behaviour to MITRE ATT&CK, threat hunting over emulated APT data, and writing a full incident response plan for a case study breach.

This folder collects my lab portfolio and the final case study report. Everything here is academic coursework using emulation / fictional data (e.g. the MITRE APT29 evals dataset and a made-up bank).

---

## What's in this repo

| #   | Work                                                                      | What I did                                                                                                                                                                                                                                                                                                                    | Tools / Frameworks                                                                |
| --- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 1   | **Splunk SIEM Lab** *(portfolio – Part 1)*                                | Investigated Windows Sysmon logs to spot LSASS credential dumping via `procdump`, then pivoted to Linux `auditd` data to detect an unauthorised **root crontab** edit by a standard user. Refined a raw query into a proper detection rule and explained the SOC impact.                                                      | Splunk Enterprise 9.2, SPL, Sysmon, Linux auditd, Kali Linux, Cyber Kill Chain    |
| 2   | **Elastic Stack Lab** *(portfolio – Part 2)*                              | Stood up and configured the Elastic Stack: loaded Packetbeat dashboards, explored network logs in Discover, built security rules that fired alerts, connected an Elastic Agent on a Windows VM, and captured PowerShell script-execution logs. Wrote up how GenAI (Attack Discovery / AI Assistant) speeds up threat hunting. | Elasticsearch, Kibana, Packetbeat, Elastic Agent, Windows VM, PowerShell, KQL     |
| 3   | **MITRE ATT&CK for CTI Lab**                                              | Analysed threat reports (Cybereason **Cobalt Kitty**, **APT39**) and SOC tickets, annotating tactics/techniques in ATT&CK Navigator with rationales. Did a comparative analysis of the two actors and wrote defensive recommendations (technical / policy / risk acceptance) for a chosen technique.                          | MITRE ATT&CK v18.1, ATT&CK Navigator, Enterprise ATT&CK                           |
| 4   | **APT29 Adversary Emulation / Threat Hunt** *(Day 1 + Day 2)*             | Worked through the MITRE **APT29** evaluation scenario end-to-end, documenting each stage (initial breach → C2 → cred dumping → lateral movement) and, for every step, *how I hunted and found it* in the telemetry.                                                                                                          | Pupy C2, PoshC2, RDP, PowerShell, ATT&CK, threat-hunting methodology              |
| 5   | **Case Study Report – LockBit 3.0 CIRP** *(group, individually assessed)* | Team incident response plan for a **LockBit 3.0** ransomware attack on a fictional bank (Sydney Virtual Bank). **My contribution: Technical Analysis & Recovery plan** - attack walkthrough, IoCs, root-cause analysis, ATT&CK mapping, and the full system-restoration / stand-down plan.                                    | MITRE ATT&CK, ACSC Cyber Incident Response Plan template, NIST SP 800-61, PPOSTTE |

---

## The work in a bit more detail

### 1. Splunk SIEM Lab (Part 1)
Two investigations in Splunk. First, hunting through Windows Sysmon logs to catch a `procdump` grab of LSASS memory (credential theft). Second, spotting Linux persistence: a low-privileged user (`ubuntu`, UID 1000) editing the **root** crontab, which trips the `rootcmd` alarm. The reflection section turns the ad-hoc search into a reusable detection rule  filtering on `exe="/usr/bin/crontab"` with `auid>=1000 success=yes` - and explains why a human user touching a crontab is anomalous and maps to the Installation/Persistence phase of the Kill Chain.

### 2. Elastic Stack Lab (Part 2)
Full walk from setup to detection: Packetbeat capturing network traffic, Kibana Discover on the `packetbeat-*` index, security rules generating alerts (UDP traffic detection) and building an event timeline, then extending visibility to endpoints with an Elastic Agent on a Windows VM. Includes verifying connectivity to Elasticsearch (the `curl` 401 that confirms the box is reachable but auth-gated) and PowerShell script-block logging showing full script contents. Closes with a short piece on how GenAI helps analysts cut through alert noise.

### 3. MITRE ATT&CK for CTI Lab
Report and ticket analysis mapped to ATT&CK v18.1. Cobalt Kitty (OceanLotus) and APT39 were each broken down into 18–21 technique entries with rationales and annotated in Navigator. The comparative layer highlights the split: Cobalt Kitty leans on stealth / "living off the land" (e.g. `mshta.exe`, Outlook persistence), while APT39 leans on valid-account abuse, web shells, and data theft. Wrapped up with defensive recommendations across technical controls, policy, and accepted risk.

### 4. APT29 Adversary Emulation / Threat Hunt
Two-day exercise running the MITRE APT29 evals scenario against Windows hosts, using Pupy (Day 1) and PoshC2 (Day 2) as the C2. For each stage and technique I logged the hands-on command, the source/target host, and - the important bit for a threat hunter - the exact way I located the activity in the logs. Submitted as structured workbooks (`day1` / `day2`).

### 5. Case Study Report – LockBit 3.0 (Sydney Virtual Bank)
A complete Cyber Incident Response Plan following the ACSC template. My sections were the **Technical Analysis** (initial access via phishing → VPN with no MFA, discovery, Mimikatz LSASS dump, pass-the-hash lateral movement, Rclone exfil to MEGA, LockBit deployment via GPO), the **IoC / root-cause** write-up, the **ATT&CK mapping**, and the **Recovery** plan (RTOs, backup verification, krbtgt double-reset, staged re-imaging, and stand-down criteria).

---


