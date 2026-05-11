# React — interview questions

## Table of contents

- [1. What is the difference between state and props?](#1-what-is-the-difference-between-state-and-props)
- [2. What is a React hook and why is it useful?](#2-what-is-a-react-hook-and-why-is-it-useful)
- [3. What's the Virtual DOM ? Why does React use a Virtual DOM?](#3-whats-the-virtual-dom-why-does-react-use-a-virtual-dom)
- [4. How do you handle data coming from an API in React?](#4-how-do-you-handle-data-coming-from-an-api-in-react)
- [5. How do you optimize rendering for a very long list in React?](#5-how-do-you-optimize-rendering-for-a-very-long-list-in-react)
- [6. What is the difference between controlled and uncontrolled components?](#6-what-is-the-difference-between-controlled-and-uncontrolled-components)
- [7. What causes a React component to re-render?](#7-what-causes-a-react-component-to-re-render)
- [8. What is the difference between useEffect, useMemo, and useCallback?](#8-what-is-the-difference-between-useeffect-usememo-and-usecallback)
- [9. How do you avoid unnecessary re-renders?](#9-how-do-you-avoid-unnecessary-re-renders)
- [10. What is lifting state up?](#10-what-is-lifting-state-up)
- [11. How do you manage forms in React?](#11-how-do-you-manage-forms-in-react)
- [12. How do you handle loading, error, and empty states?](#12-how-do-you-handle-loading-error-and-empty-states)
- [13. How do you test React components?](#13-how-do-you-test-react-components)

---

#### 1. What is the difference between state and props?

<details>
<summary>Reveal answer</summary>

State are data owned by a component and preserved between re-renders. It's usually created throught hooks such as `useState`. It can be updated using the associated setter. When the state changes, React re-renders the component.

Props are data passed to a component by its parent. The child component should not modify the props.

The main difference is ownership: the state is owned by the component whereas the props are owned by the parent component.

</details>

---

#### 2. What is a React hook and why is it useful?

<details>
<summary>Reveal answer</summary>

A React hook is a function that lets a function component use React features such as state, effects, refs, context, or memoization. Built-in hooks include useState, useEffect, and useRef, and custom hooks must start with use.

Hooks are useful because they let you reuse stateful logic between components without using class components.

They must follow the rules of hooks: only call hooks at the top level, and only call them from React components or custom hooks.

</details>

---

#### 3. What's the Virtual DOM ? Why does React use a Virtual DOM?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 4. How do you handle data coming from an API in React?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 5. How do you optimize rendering for a very long list in React?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 6. What is the difference between controlled and uncontrolled components?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 7. What causes a React component to re-render?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 8. What is the difference between useEffect, useMemo, and useCallback?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 9. How do you avoid unnecessary re-renders?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 10. What is lifting state up?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 11. How do you manage forms in React?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 12. How do you handle loading, error, and empty states?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---

#### 13. How do you test React components?

<details>
<summary>Reveal answer</summary>

*TODO: draft answer.*

</details>

---
