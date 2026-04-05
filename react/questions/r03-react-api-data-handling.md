# How do you handle data coming from an API in React?

## Why recruiters ask this
- Evaluates practical frontend data-flow discipline.
- Checks loading, error, and success state handling.

## Answer structure (keep it concise)
1. Fetch data in `useEffect` (or a dedicated data hook/library).
2. Manage `loading`, `error`, and `data` states explicitly.
3. Handle cancellation/race conditions where needed.
4. Mention retry and caching strategy for better UX.

