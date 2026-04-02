# How do you handle a database that becomes very large?

## Why recruiters ask this
- Assesses scalability strategy and operational maturity.
- Relevant to long-term repository growth.

## Answer structure (keep it concise)
1. Start with bottleneck identification (queries, storage, contention).
2. Apply foundational levers:
   - Indexing and query tuning
   - Pagination/read patterns
   - Partitioning/archiving
   - Caching for hot reads
3. Mention monitoring and capacity planning.
4. Explain incremental rollout with measurable checkpoints.
