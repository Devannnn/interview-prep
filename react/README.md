# React — interview questions

## Table of contents

- [1. What is the difference between state and props?](#1-what-is-the-difference-between-state-and-props)
- [2. What's the Virtual DOM ? Why does React use a Virtual DOM?](#2-whats-the-virtual-dom-why-does-react-use-a-virtual-dom)
- [3. How do you handle data coming from an API in React?](#3-how-do-you-handle-data-coming-from-an-api-in-react)
- [4. How do you optimize rendering for a very long list in React?](#4-how-do-you-optimize-rendering-for-a-very-long-list-in-react)
- [5. What is a React hook and why is it useful?](#5-what-is-a-react-hook-and-why-is-it-useful)

---

#### 1. What is the difference between state and props?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Verifies React fundamentals and component design clarity.
- Ensures you can reason about data flow predictably.

## Answer structure (keep it concise)
1. Define `props` as external, read-only inputs.
2. Define `state` as internal, mutable component data.
3. Explain one-way data flow and re-render triggers.
4. Give a practical example with parent-child interaction.

</details>

---

#### 2. What's the Virtual DOM ? Why does React use a Virtual DOM?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Tests conceptual understanding of rendering performance.
- Checks if you can explain diffing and UI update efficiency.

## Answer structure (keep it concise)
1. Explain that React compares virtual trees before real DOM updates.
2. Describe diffing at a high level and why fewer DOM operations matter.
3. Clarify that Virtual DOM helps, but architecture and state design still matter.
4. Give one real optimization example from your projects.

</details>

---

#### 3. How do you handle data coming from an API in React?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Evaluates practical frontend data-flow discipline.
- Checks loading, error, and success state handling.

## Answer structure (keep it concise)
1. Fetch data in `useEffect` (or a dedicated data hook/library).
2. Manage `loading`, `error`, and `data` states explicitly.
3. Handle cancellation/race conditions where needed.
4. Mention retry and caching strategy for better UX.

</details>

---

#### 4. How do you optimize rendering for a very long list in React?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Tests front-end performance mindset at scale.
- Relevant for interfaces showing large scientific datasets.

## Answer structure (keep it concise)
1. Start with list virtualization (`react-window` / `react-virtualized`).
2. Add pagination or infinite scrolling when appropriate.
3. Ensure stable keys and avoid unnecessary re-renders.
4. Explain how you measured performance improvements.

</details>

---

#### 5. What is a React hook and why is it useful?

<details>
<summary>Reveal answer</summary>

## Why recruiters ask this
- Validates modern React knowledge and composability skills.
- Checks if you can separate reusable logic from UI.

## Answer structure (keep it concise)
1. Define hooks as functions enabling state/lifecycle in function components.
2. Give common examples: `useState`, `useEffect`, `useMemo`, `useCallback`.
3. Explain custom hooks for reusable business logic.
4. Mention hook rules and common pitfalls.

</details>

---
