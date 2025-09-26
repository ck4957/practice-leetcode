ReactJS

React.JS is a Javascript library for building user interfaces. It’s fast, easy to learn and fun to work with.
————————————————————————————————————————————————————————————————————————

## Components

React is built around components, not templates.
You create a component by calling the createClass method on the React object — the entry point into the library.
————————————————————————————————————————————————————————————————————————

## JSX — Javascript Syntax Extension

The HTML’ish syntax is not actually HTML, but something called JSX.
This is simply a syntax extension for Javascript which enables you to write JS with XML-like tags.
So the tags are actually function calls, which are transformed into React.JS code, and
finally end up as HTML and Javascript in the DOM.

————————————————————————————————————————————————————————————————————————

## Props & State

There are two types of data in React; props and state.
The key difference is that state is private and can be changed from within the component itself.
Props are external, and not controlled by the component itself.
It’s passed down from components higher up the hierarchy, whom also control the data.

### State

The other way of storing data in React is in the component’s state.
And unlike props — which are immutable from the components perspective — the state is mutable.

Initializing state
To initialize the state simply pass a getInitialState() to the component, and
return whatever state you want your component to be initialized with.

Changing state
To modify the state, simply call this.setState(), passing in the new state as the argument.
————————————————————————————————————————————————————————————————————————

## Lifecycle Methods:

componentWillMount

- is executed before rendering, on both the server and the client side.

componentDidMount:

- is executed after the first render only on the client side.
  This is where AJAX requests and DOM or state updates should occur.
  This method is also used for integration with other JavaScript frameworks and
  any functions with delayed execution such as setTimeout or setInterval.
  We are using it to update the state so we can trigger the other lifecycle methods.

componentWillReceiveProps:

- is invoked as soon as the props are updated before another render is called.
  We triggered it from setNewNumber when we updated the state.

shouldComponentUpdate should return true or false value.
This will determine if the component will be updated or not.
This is set to true by default.
If you are sure that the component doesnt need to render after state or props are updated,
you can return false value.

componentWillUpdate: is called just before rendering.

componentDidUpdate: is called just after rendering.

componentWillUnmount: is called after the component is unmounted from the dom.
We are unmounting our component in main.js.

## Context API

The React Context API is a way for a React app to effectively produce global variables that can be passed around.
This is the alternative to "prop drilling" or moving props from grandparent to child to parent to child, and so on.
Context is also touted as an easier, lighter approach to state management using Redux.
————————————————————————————————————————————————————————————————————————

- Creating a Context
  To create a context, you use the React.createContext() function.
  This function returns a context object with a Provider and a Consumer component.
  The Provider component is used to provide the context value to its child components.
  The Consumer component is used to consume the context value in a child component.
  ————————————————————————————————————————————————————————————————————————
- Using the Context Provider
  To use the Provider component, you wrap it around the components that need access to the context value.
  You pass the context value as a prop to the Provider component.
  ————————————————————————————————————————————————————————————————————————
- Using the Context Consumer
  To use the Consumer component, you wrap it around the component that needs access to the context value.
  You use a render prop to access the context value and render the component accordingly.
  ————————————————————————————————————————————————————————————————————————
- Example

```javascript
import React, { createContext, useState } from "react";
// Create a Context
const MyContext = createContext();
const MyProvider = ({ children }) => {
  const [value, setValue] = useState("Hello, World!");
  return (
    <MyContext.Provider value={{ value, setValue }}>
      {children}
    </MyContext.Provider>
  );
};
const MyComponent = () => {
  return (
    <MyContext.Consumer>
      {({ value, setValue }) => (
        <div>
          <p>{value}</p>
          <button onClick={() => setValue("Hello, React Context!")}>
            Change Value
          </button>
        </div>
      )}
    </MyContext.Consumer>
  );
};
const App = () => {
  return (
    <MyProvider>
      <MyComponent />
    </MyProvider>
  );
};
export default App;
```

————————————————————————————————————————————————————————————————————————

- Conclusion
  The React Context API is a powerful tool for managing global state in a React application.
  It allows you to avoid prop drilling and makes it easier to share data between components.
  By using the Provider and Consumer components, you can easily create and consume context values in your components

What is Memoization?
Memoization is an optimization technique used to speed up function calls by caching the results of expensive function calls and returning the cached result when the same inputs occur again.

Memoization Examples:

````javaScript
// Simple memoization function
function memoize(fn) {
  const cache = {};
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache[key]) {
      return cache[key];
    } else {
      const result = fn(...args);
      cache[key] = result;
      return result;
    }
  };
}
// Example usage
const add = (a, b) => a + b;
const memoizedAdd = memoize(add);
console.log(memoizedAdd(1, 2)); // Computes and caches result
console.log(memoizedAdd(1, 2)); // Returns cached result


# React Hooks

React Hooks are functions that let you use state and other React features without writing a class.
They were introduced in React 16.8 and have become a popular way to manage state and side effects in functional components.


```javaScript

// useState Hook
const [count, setCount] = useState(0);

// useEffect Hook
useEffect(() => {
  // Code to run on component mount
  fetchData();
}, [])

// useContext Hook
const value = useContext(MyContext);

// useReducer Hook
const [state, dispatch] = useReducer(reducer, initialState);

// useRef Hook
const inputRef = useRef(null);

// useMemo Hook
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a
, b]);

// useCallback Hook
const memoizedCallback = useCallback(() => { doSomething(a, b); }, [a, b]);

// useLayoutEffect Hook
useLayoutEffect(() => { measureLayout(); }, []);


````

## Commonly used React Hooks

| Hook Name            | Description                                                                                     | Example Usage                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| useState             | Allows you to add state to functional components.                                               | const [count, setCount] = useState(0);                                            |
| useEffect            | Lets you perform side effects in functional components, such as data fetching or subscriptions. | useEffect(() => { fetchData(); }, []);                                            |
| useContext           | Provides a way to access context values in functional components.                               | const value = useContext(MyContext);                                              |
| useReducer           | An alternative to useState for managing complex state logic.                                    | const [state, dispatch] = useReducer(reducer, initialState);                      |
| useRef               | Allows you to create a mutable reference that persists across renders.                          | const inputRef = useRef(null);                                                    |
| useMemo              | Memoizes a computed value to optimize performance.                                              | const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);         |
| useCallback          | Memoizes a callback function to prevent unnecessary re-renders.                                 | const memoizedCallback = useCallback(() => { doSomething(a, b); }, [a, b]);       |
| useLayoutEffect      | Similar to useEffect, but fires synchronously after all DOM mutations.                          | useLayoutEffect(() => { measureLayout(); }, []);                                  |
| useImperativeHandle  | Customizes the instance value that is exposed when using ref in parent components.              | useImperativeHandle(ref, () => ({ focus: () => { inputRef.current.focus(); } })); |
| useDebugValue        | Used to display a label for custom hooks in React DevTools.                                     | useDebugValue(value);                                                             |
| useTransition        | Allows you to manage concurrent rendering and prioritize updates.                               | const [isPending, startTransition] = useTransition();                             |
| useDeferredValue     | Defers a value until the next render to improve performance.                                    | const deferredValue = useDeferredValue(value);                                    |
| useId                | Generates a unique ID that is stable across server and client renders.                          | const id = useId();                                                               |
| useSyncExternalStore | Subscribes to an external store and updates the component when the store changes.               | const state = useSyncExternalStore(subscribe, getSnapshot);                       |
| useInsertionEffect   | Similar to useLayoutEffect, but fires before any DOM mutations.                                 | useInsertionEffect(() => { insertStyles(); }, []);                                |
| useEvent             | Creates a stable event handler that doesn't change between renders.                             | const handleClick = useEvent((event) => { console.log(event); });                 |
| useMutableSource     | Subscribes to a mutable source and updates the component when the source changes.               | const state = useMutableSource(source, getSnapshot, subscribe);                   |
| useCache             | Caches a value based on dependencies to optimize performance.                                   | const cachedValue = useCache(() => computeValue(a, b), [a, b]);                   |
