# React — interview questions

## Table of contents

- [1. What is the difference between state and props?](#1-what-is-the-difference-between-state-and-props)
- [2. What is a React hook and why is it useful?](#2-what-is-a-react-hook-and-why-is-it-useful)
- [3. What is lifting state up?](#3-what-is-lifting-state-up)
- [4. What is the difference between controlled and uncontrolled components?](#4-what-is-the-difference-between-controlled-and-uncontrolled-components)
- [5. How do you manage forms in React?](#5-how-do-you-manage-forms-in-react)
- [6. What's the Virtual DOM ? Why does React use a Virtual DOM?](#6-whats-the-virtual-dom-why-does-react-use-a-virtual-dom)
- [7. What causes a React component to re-render?](#7-what-causes-a-react-component-to-re-render)
- [8. What is the difference between useEffect, useMemo, and useCallback?](#8-what-is-the-difference-between-useeffect-usememo-and-usecallback)
- [9. How do you handle loading, error, and empty states?](#9-how-do-you-handle-loading-error-and-empty-states)
- [10. How do you handle data coming from an API in React?](#10-how-do-you-handle-data-coming-from-an-api-in-react)
- [11. How do you test React components?](#11-how-do-you-test-react-components)
- [12. How do you avoid unnecessary re-renders?](#12-how-do-you-avoid-unnecessary-re-renders)
- [13. How do you optimize rendering for a very long list in React?](#13-how-do-you-optimize-rendering-for-a-very-long-list-in-react)
- [14. When memoization can be counter-productive ?](#14-when-memoization-can-be-counter-productive-)

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

#### 3. What is lifting state up?

<details>
<summary>Reveal answer</summary>

Lifting state up means moving a component's state from a component to its parent and passing it as props. The component passes from managing the data in its own state to merely consuming it. It's often useful when you want to share data between siblings components - you lift the data up to the closest common parent so they can all receive the data as props.

</details>

---

#### 4. What is the difference between controlled and uncontrolled components?

<details>
<summary>Reveal answer</summary>

A component is controlled when its important state is owned by a parent and passed to the component through props. It is uncontrolled when the component owns that state internally.

A common example is form inputs.

A form input can be controlled, meaning its state is managed by the parent component:

```typescript
<input value={email} onChange={...} />
```

Or it can be uncontrolled, meaning the DOM manages the value itself and the parent component merely reads it when needed:
```typescript
<input defaultValue="test@example.com" ref={emailRef} />
```

</details>

---

#### 5. How do you manage forms in React?

<details>
<summary>Reveal answer</summary>

For simple forms, I would manage the values with controlled inputs and React state. For larger forms, I would use a form library like React Hook Form or Formik to manage values, validation, touched fields, and submission state.

I would initialize the form with default values when needed, validate the values with a schema library like Yup or Zod, and display validation errors near the relevant fields.

On submit, I would call the API or callback, handle success and error states, and reset the form after a successful submission if that makes sense for the user flow.

</details>

---

#### 6. What's the Virtual DOM ? Why does React use a Virtual DOM?

<details>
<summary>Reveal answer</summary>

The Virtual DOM is a lightweight JavaScript representation of the UI. It is made of React elements that describe what should appear on the screen.

When state or props change, React creates a new Virtual DOM tree and compares it with the previous one. This process helps React figure out what changed and update the real DOM accordingly.

React uses this approach because direct DOM updates can be expensive. The Virtual DOM lets React update only the part of the real DOM that have changed.

</details>

---

#### 7. What causes a React component to re-render?

<details>
<summary>Reveal answer</summary>

A React component is re-rendered when one of its props changes, when its own state changes or when its parent re-renders. 

A component can also re-render because a hook it uses received new data or when a context it consumes changes.

</details>

---

#### 8. What is the difference between useEffect, useMemo, and useCallback?

<details>
<summary>Reveal answer</summary>

All of them are React hooks that use a dependency array to decide when their logic should run again.

useEffect is used to perform side-effects logic - fetching data, listening to events, etc.

useMemo is used to memoize a calculated value.

useCallback is used to memoize a function reference.

</details>

---

#### 9. How do you handle loading, error, and empty states?

<details>
<summary>Reveal answer</summary>

I would explicitly handle each possible state of the request. While data is loading, I could show a loading message, spinner, or skeleton. If the request fails, I would show an error message, notification, or retry action. If the request succeeds but returns no data, I would show an empty state explaining that there is nothing to display.

Once the data is available, I would render the normal UI. The goal is to avoid showing a broken or confusing interface while the data is not ready.

</details>

---

#### 10. How do you handle data coming from an API in React?

<details>
<summary>Reveal answer</summary>

I would fetch the data from the API, usually inside a `useEffect` or using an external library. I would store the result into component state. Or, if I want caching, I'd integrate it with a caching library such as TanStack Query. 

When I receive the data, I would use an external library to validate the data against a predefined schema. For example, Zod or Yup. That way, I'd could be sure about the data I am receiving and get type hints.

I would also handle loading, error and empty states inside my components to make sure all scenarios are covered. 

Finally, once the edge cases are covered and the data has been validated, I'd use it in the business logic.


</details>

---

#### 11. How do you test React components?

<details>
<summary>Reveal answer</summary>

I would test React components with React Testing Library and a test runner like Jest or Vitest.

The goal is to test the component from the user's perspective: render it, query elements by accessible text or role, simulate user interactions, and assert that the expected UI appears.

I would test important states such as loading, error, empty, and success states, and mock API calls or external dependencies when needed.

</details>

---

#### 12. How do you avoid unnecessary re-renders?

<details>
<summary>Reveal answer</summary>

You avoid unnecessary re-renders of a component by:
1. Keeping its props minimal and stable.
2. Avoiding unnecessary state updates in parent components.
3. Using `React.memo` for components that receive the same props often.
4. Subscribing to minimal contexts and hooks.
5. Updating state only when the value really changed.

</details>

---

#### 13. How do you optimize rendering for a very long list in React?

<details>
<summary>Reveal answer</summary>

First, I'd make sure that each element has a unique stable identifier so React match existing elements correctly between renders. 

Then, I wouldn't display the entire list at once. Depending on the situation, I'd use either pagination, infinite scrolling or list virtualization.

I would also make sure that the list component is not re-rendered inefficiently. For this, I would keep props minimal and stable, and memoize components when it makes sense. 

</details>

---

#### 14. When can memoization be counter-productive?

<details>
<summary>Reveal answer</summary>

A common mistake is to memoize everything thinking it will optimize the performance of your application.

A golden rule of performance is: not doing something is always faster than doing something.

Because memoization has a cost: React has to compare each dependency to its previous value on every render. This comparison takes time.

If the calculation is cheap or if the component doesn't render often, the overhead of the memoization can exceed the gains and actually reduce the overall performance.

Memoization should not be the default. It is useful when a calculation or component is expensive, when it re-renders frequently, or when a stable reference is needed to avoid re-rendering memoized children.

</details>