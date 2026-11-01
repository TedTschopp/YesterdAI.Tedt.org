---
title: Fortanix’s container controls make GPU attestation a configuration decision
summary: New reporting on Fortanix’s Confidential Containers integration highlights conditional key operations
  and a GPU setting that changes what the verifier checks.
section: Enterprise Ops
rank: 2
evidence_type: reporting
reader_job: Which evidence does Fortanix verify before a confidential AI workload can decrypt its image,
  and what remains outside that assurance?
takeaways:
- Fortanix’s Intel TDX guide distinguishes GPU evidence collection from validation through NVIDIA’s attestation
  service.
- Confidential Containers still trusts the guest software and requires separate attention to application
  interfaces and container verification.
topics:
- infrastructure
- security
sources:
- url: https://www.infoq.com/news/2026/10/k8s-confidential-containers/
  title: Kubernetes Confidential Containers get Fortanix attestation and key management
  publisher: InfoQ / Mark Silvester
  published_at: '2026-10-31T08:18:00Z'
  kind: reporting
- url: https://www.fortanix.com/company/pr/2026/10/fortanix-announces-confidential-ai-for-enterprise-grade-kubernetes-workloads-on-cncf-confidential-containers-coco
  title: Fortanix announces Confidential AI for Kubernetes workloads on Confidential Containers
  publisher: Fortanix
  published_at: '2026-10-18T18:30:00Z'
  kind: vendor
- url: https://support.fortanix.com/docs/deploy-confidential-container-coco-workloads-on-intel-tdx-platform
  title: Deploy Confidential Container workloads on Intel TDX platform
  publisher: Fortanix
  published_at: '2026-09-18T16:08:16.206Z'
  kind: vendor
  modified_at: '2026-09-26T01:51:19.217Z'
  date_basis: Document360 embedded firstPublishedDate and lastPublishedDate; visible page agrees on September
    18 and 26. The guide labels the deployment Beta.
- url: https://confidentialcontainers.org/docs/architecture/trust-model/trust-model/
  title: Trust model for Confidential Containers
  publisher: Confidential Containers project
  published_at: '2024-01-23T00:00:00Z'
  kind: practitioner
  date_precision: day
  modified_at: '2024-12-19T16:51:33Z'
  date_basis: Publisher datePublished and dateModified metadata; older architectural context, not eligibility.
leader_action: Require the proposed confidential-AI deployment to identify its verified hardware, trusted
  guest software and key-authorization policy.
individual_action: Inspect the GPU attestation setting and demonstrate both an accepted measurement and
  a refused mismatch using disposable test data.
article_id: art_666d65fb5c8d82e4
story_key: https://www.infoq.com/news/2026/10/k8s-confidential-containers
edition_date: '2026-11-01'
published_at: '2026-11-01T13:08:11.450990Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
eligibility:
  url: https://www.infoq.com/news/2026/10/k8s-confidential-containers/
  published_at: '2026-10-31T08:18:00Z'
  precision: second
  verification: jsonld
  evidence: InfoQ NewsArticle JSON-LD datePublished and dateModified both equal 2026-10-31T08:18:00+0000.
    This new report, not the older product announcement, controls eligibility. Fortanix’s announcement
    is October 18; its deployment guide was first published September 18 and last published September
    26.
  discovered_url: https://www.infoq.com/news/2026/10/k8s-confidential-containers/
  verified_at: '2026-11-01T13:08:11.450990Z'
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Fortanix has added support for Confidential Containers in its Confidential AI platform,
  linking Kubernetes workload attestation to encryption key release to protect sensitive AI models and
  data within hardware-based trusted execution environments (TEEs). This integration ensures that only
  workloads meeting security policies can decrypt protected data, enhancing data-in-use security beyond
  traditional container isolation methods. The integration uses Fortanix's Confidential Computing Manager
  (CCM) to verify the environment and Data Security Manager (DSM) to release keys conditionally, with
  options to validate GPU attestation through NVIDIA services. Alternative attestation and key release
  mechanisms exist in open-source Trustee components and Microsoft's Azure Secure Key Release. Fortanix
  offers this as a hosted or on-premises service with 24x7 support, and its deployment guide details necessary
  configurations and Helm chart installation.
feed_title: Fortanix integrates attestation and key management with Kubernetes Confidential Containers
  for AI workloads using hardware-based trusted execution environments [ * ] [ ◼ ]
feed_published_at: '2026-10-31T08:18:00Z'
feed_id: sty_eb5b6bc81c047dc2
rating: Important
technical_rating: Important
---
A confidential container needs more than encrypted memory. Someone must decide which evidence is good enough before protected software can obtain the key operation it needs.

[InfoQ’s October 31 report](https://www.infoq.com/news/2026/10/k8s-confidential-containers/) examines that decision in Fortanix’s integration with Confidential Containers, the Kubernetes project that places pods inside hardware-protected virtual machines. The product announcement dates to [October 18](https://www.fortanix.com/company/pr/2026/10/fortanix-announces-confidential-ai-for-enterprise-grade-kubernetes-workloads-on-cncf-confidential-containers-coco). The useful detail in the new reporting is what the configuration actually verifies.

Fortanix’s [Intel TDX deployment guide](https://support.fortanix.com/docs/deploy-confidential-container-coco-workloads-on-intel-tdx-platform), labeled Beta, describes two services. Confidential Computing Manager checks workload measurements and issues a short-lived certificate. The workload uses that certificate to authenticate to Data Security Manager, which authorizes the key-unwrapping operation needed to decrypt the container image. The key-encryption key remains in the manager.

For a graphics processor, the guide distinguishes `Required` from `Ignored`. The first validates GPU evidence through NVIDIA’s remote attestation service. The second requires evidence to be present but ignores its result. A record showing that evidence arrived therefore leaves open whether the GPU was verified.

The hardware boundary also has limits. The project’s [trust model](https://confidentialcontainers.org/docs/architecture/trust-model/trust-model/) places the guest kernel and helper processes inside the trusted environment. It explains that hardware measurements usually cover the guest, while container verification is a separate stage. An application can still expose a dangerous interface from inside the protected machine.

A useful acceptance check would pair a permitted workload with one whose measurements fail policy, then record the certificate and key-operation outcomes. That is a proposed check, not testing performed by this publication. The deployment also needs its host firmware and kernel prepared separately; the Helm chart does not configure them.

The handoff to an operator should name what was measured, what was validated and which policy authorized decryption. An encrypted memory boundary becomes useful when those decisions remain inspectable.
