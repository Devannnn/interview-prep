# How do you migrate millions of records safely?

## Why recruiters ask this
- Assesses your production mindset for scale, reliability, and recovery.
- Verifies that you can balance safety, speed, and observability.

## Answer structure (keep it concise)
1. Start with migration goals and failure risks.
2. Describe execution strategy:
   - Batch processing and idempotency
   - Checkpoints and retry logic
   - Shadow/dual writes if needed
3. Explain validation:
   - Row counts and checksums
   - Sampling and business-rule verification
4. End with rollout, monitoring, and rollback plan.

