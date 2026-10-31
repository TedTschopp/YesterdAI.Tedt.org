---
title: Cursor’s extension warning puts host recovery beyond the marketplace
summary: Cursor’s October 30 update clarifies affected Claude Code packages; its notice and Phorion’s investigation
  explain why removal alone leaves recovery work.
section: Security
rank: 1
evidence_type: vendor
reader_job: How should a team scope and verify recovery from the malicious Claude Code packages distributed
  through Cursor’s marketplace?
takeaways:
- Cursor identifies affected macOS and Windows packages as versions 2.1.312 and 2.1.313; its notice distinguishes
  them from Anthropic’s official distribution.
- Persistence and credential recovery require host evidence even after a package and its attacker server are
  removed.
topics:
- security
- governance
eligibility:
  url: https://cursor.com/blog/claude-code-extension-security-notice
  published_at: '2026-10-30T18:30:00Z'
  precision: second
  verification: visible
  basis: substantive_update
  original_published_date: '2026-10-29'
  evidence: 'The original notice visibly dates the incident and publication October 29. Its explicit update
    states Oct 30, 2026, 11:30 am PT and identifies the substantive change: updated indicators of compromise
    and clarified affected versions. PDT is UTC-07, so the update is 18:30Z and qualifies independently of
    the older original. Phorion discovery is not the date basis. Its October 31 date-only update is not assumed
    to precede cutoff; affected-version claims are supported by Cursor’s eligible October 30 update.'
  discovered_url: https://phorion.io/blog/offical-claude-code-vsx-compromise/
  verified_at: '2026-10-31T12:08:59.648271Z'
sources:
- url: https://cursor.com/blog/claude-code-extension-security-notice
  title: Claude Code extension security notice
  publisher: Cursor Team
  published_at: '2026-10-29T00:00:00Z'
  kind: vendor
  date_precision: day
  modified_at: '2026-10-30T18:30:00Z'
  date_basis: Visible original date only; midnight UTC stores that date and is not an observed instant. Eligibility
    uses the expressly dated substantive update, not this placeholder.
- url: https://phorion.io/blog/offical-claude-code-vsx-compromise/
  title: Claude Code extension compromise investigation
  publisher: Phorion / Calum Hall
  published_at: '2026-10-30T00:00:00Z'
  kind: research
  date_precision: day
  date_basis: Publisher meta explicitly uses midnight Z for October 30, treated conservatively as the complete
    UTC day, wholly inside the window. The subsequent October 31 date-only revision is not treated as an eligible
    precise instant; only mechanisms corroborated in Cursor’s in-window notice are used.
leader_action: Assign ownership for endpoint evidence, persistence removal and trusted-system credential recovery
  as separate incident outcomes.
individual_action: Preserve the actual marketplace, package version and installation evidence, then follow
  current official response guidance for affected hosts.
article_id: art_b11cb5d74cc4c058
story_key: https://cursor.com/blog/claude-code-extension-security-notice
edition_date: '2026-10-31'
published_at: '2026-10-31T12:08:59.648271Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Phorion discovered a backdoor in the official Claude Code extension for Visual Studio Code distributed
  via the Cursor Marketplace, which installs a persistent SSH backdoor on macOS, Linux, and Windows systems.
  The compromised extension was removed from the marketplace and related registries after the discovery, and
  organizations using version 2.1.313 are urged to review their environments and engage incident response.
  The backdoor operates by appending an attacker-controlled SSH public key to the authorized_keys file and
  attempts to enable SSH services on affected systems, though some platform-specific bugs limit its effectiveness,
  such as a macOS check that fails to enable Remote Login without root privileges. The extension runs malicious
  code immediately upon loading, granting attackers potential long-term interactive access to local files and
  developer tools without user interaction. Despite some implementation errors that reduce impact on macOS
  and Windows, the malware remains a significant threat due to its persistence mechanisms and host reconnaissance
  capabilities. Users and administrators should monitor for signs of compromise and take appropriate remediation
  steps.
feed_title: Phorion detects persistent SSH backdoor in official Claude Code VS Code extension on Cursor Marketplace,
  prompting removal and incident response advisories
feed_published_at: '2026-10-30T07:09:12Z'
feed_id: sty_03425160c6f2a9f4
---
An extension can disappear from a marketplace while the changes it made remain on a developer’s machine. Cursor’s updated security notice makes that distinction concrete.

The [October 30 update](https://cursor.com/blog/claude-code-extension-security-notice) identifies malicious Claude Code extension versions 2.1.312 and 2.1.313 distributed through Cursor’s marketplace for macOS and Windows. Cursor says these packages were not developed by Anthropic. Its account concerns an October 29 incident, with affected-version and indicator guidance clarified the following day. The company reports no evidence that the official distribution or other versions were affected.

[Phorion’s technical investigation](https://phorion.io/blog/offical-claude-code-vsx-compromise/) describes injected code that executes when the extension module loads, before normal activation. It plants an SSH key and persistence, gathers host information and attempts a reverse tunnel. On a standard-user Mac, a faulty permission check can prevent it from enabling Remote Login. That limits one access path; it does not establish that the machine escaped the other changes.

Cursor says it removed the packages and worked with the hosting provider to disable the attacker’s server. It still directs affected users to investigate and remediate their hosts. Removing the extension alone can leave separate persistence behind.

For a response team, the first useful record connects the marketplace, installed package bytes, version, operating system and installation time. A familiar extension name leaves the distribution route unresolved. Preserve those records before cleanup, then use the published indicators alongside endpoint and network evidence to determine what ran.

Keep containment, removal and credential recovery as separate outcomes. Cursor’s guidance calls for isolating hosts with execution evidence and rotating exposed credentials from a trusted system. Someone must verify each outcome rather than closing the incident when the editor’s extension list looks clean.

The marketplace can withdraw a package centrally. The organization still has to account for the state it left on each affected machine.
