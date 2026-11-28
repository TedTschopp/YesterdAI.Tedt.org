---
title: Q.ANT’s photonic energy savings still need a hardware demonstration
summary: Q.ANT’s CEO describes energy savings in simulation, with a hardware demonstration still pending.
  A pilot needs to measure the whole task.
section: Vendors
topics:
- infrastructure
- economics-adoption
reader_job: What does Q.ANT’s current evidence establish about energy savings, and what would a procurement
  pilot still need to measure?
takeaways:
- The CEO describes fourfold to fivefold energy reductions in simulation and says the reduction has not
  yet been demonstrated in real hardware.
- The IONOS pilot creates a place to measure completed-task energy, including conventional processors
  and software adaptation.
leader_action: Keep projected savings separate from measured whole-task energy before approving a larger
  hardware purchase.
individual_action: Compare the same task and output quality across the complete conventional and photonic
  pipelines.
rank: 1
article_id: art_8a7bedc20d3b6ed3
story_key: https://www.wired.com/story/a-new-breed-of-chip-runs-ai-models-using-waves-of-light
edition_date: '2026-11-28'
published_at: '2026-11-28T13:08:08.433591Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: reporting
sources:
- url: https://www.wired.com/story/a-new-breed-of-chip-runs-ai-models-using-waves-of-light/
  title: A New Breed of Chip Runs AI Models Using Waves of Light
  publisher: WIRED
  published_at: '2026-11-27T07:00:00Z'
  kind: reporting
eligibility:
  url: https://www.wired.com/story/a-new-breed-of-chip-runs-ai-models-using-waves-of-light/
  published_at: '2026-11-27T07:00:00Z'
  precision: second
  verification: meta
  evidence: The original WIRED interview has article:published_time and article:modified_time both 2026-11-27T07:00:00.000Z;
    JSON-LD agrees at 2026-11-27T02:00:00.000-05:00. Read the complete Joel Khalili interview, including
    the CEO’s explicit distinction between simulated savings and hardware demonstration.
  verified_at: '2026-11-28T13:08:08.433591Z'
  event: original_publication
feed_name: TedTschopp News Graph - Top Stories
feed_id: sty_3dbabf9ed7e3213f
feed_title: Q.ANT develops photonic processors using light waves to reduce energy consumption in AI model
  computations, piloting chips with cloud provider IONOS [ * ] [ ◼ ]
feed_summary: German company Q.ANT is developing photonic processors that use waves of light instead of
  electrons to perform complex, nonlinear AI calculations more energy-efficiently. These chips aim to
  complement traditional GPUs by handling tasks like image recognition and robotics, potentially reducing
  energy use by four to five times under simulation. Q.ANT has launched a pilot program deploying its
  photonic chips in data centers operated by cloud provider IONOS, with over 30 engineering teams working
  on AI models optimized for this hardware. The company sees photonic processors as a co-processor rather
  than a GPU replacement, addressing the rising energy costs and cooling demands of AI workloads.
feed_published_at: '2026-11-27T07:00:00Z'
feed_snapshot: docs/runs/2026-11-28-feed-snapshot.json
rating: Important
technical_rating: Important
---

Q.ANT’s projected energy savings still need a hardware demonstration. In a [new WIRED interview](https://www.wired.com/story/a-new-breed-of-chip-runs-ai-models-using-waves-of-light/), founder and chief executive Michael Förtsch describes roughly fourfold to fivefold energy reductions in simulation. He explicitly says the company has not yet demonstrated that reduction in real hardware.

That qualification matters because the proposed machine shares the work. Förtsch describes a photonic coprocessor handling complex, nonlinear calculations while conventional processors handle other operations. His target applications include images, video and robotics. The claim concerns a particular way of dividing computation, rather than a measured saving available to every existing AI model.

WIRED reports that Q.ANT has placed chips in IONOS data centers for a pilot. The company says more than 30 engineering teams are developing models for photonic computing. Those activities establish an opportunity to test the approach; they do not supply the missing energy measurement.

Software also affects the comparison. Förtsch says existing C++ or Python code can run, but code optimized for GPUs should not be expected to become faster automatically. Adaptation is needed. He also identifies assembly and supplier capacity as obstacles to producing the hardware at a much larger scale.

For a procurement trial, ask for the energy used to finish the same task at the same acceptable output quality. Include the conventional processors, movement of data and any preparation required by the photonic part. Keep the simulation estimate beside the measured result, with each clearly labeled.

Then account for the engineering needed to adapt and maintain the workload. A component that performs one calculation efficiently may still leave substantial work elsewhere in the system. The person funding a pilot needs a measured path from the proposed division of work to the electricity used by the completed job.
