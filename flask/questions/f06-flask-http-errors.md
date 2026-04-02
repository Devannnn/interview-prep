# How do you handle HTTP errors in a Flask API?

## Why recruiters ask this
- Tests production API behavior and consistency.
- Checks user-facing error quality for clients and integrators.

## Answer structure (keep it concise)
1. Use explicit aborts (e.g., `abort(404)`) where appropriate.
2. Define centralized error handlers for consistent JSON responses.
3. Separate client errors (4xx) from server errors (5xx).
4. Add logging and correlation context for troubleshooting.

