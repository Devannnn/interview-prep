# How do you implement efficient pagination in an API?

## Why recruiters ask this
- Tests API performance and client usability thinking.
- Important for large catalogs and search results.

## Answer structure (keep it concise)
1. Explain baseline `LIMIT/OFFSET` approach and its limits at scale.
2. Introduce cursor/keyset pagination for large datasets.
3. Define stable sort order and consistent page tokens.
4. Mention metadata (`next_cursor`, total count when needed) and edge cases.

