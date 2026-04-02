# How do you handle JSON data in Flask?

## Why recruiters ask this
- Tests practical API implementation basics.
- Checks that you know request parsing and response serialization.

## Answer structure (keep it concise)
1. Parse request payload with `request.get_json()`.
2. Validate required fields and types before processing.
3. Return responses with `jsonify(...)` and proper HTTP status codes.
4. Mention content-type expectations and error handling for invalid JSON.

