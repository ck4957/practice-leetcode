# BigO Notations

Big O notation is a mathematical representation used to describe the performance or complexity of an algorithm.
It provides an upper bound on the time or space complexity in terms of the size of the input data (n). Big O notation helps to analyze how an algorithm scales as the input size increases.

## Common Big O Algos

| Name        | Big O Notation | Example       |
| ----------- | -------------- | ------------- |
| Constant    | O(1)           | return true;  |
| Logarithmic | O(log n)       | binary search |

| Linear | O(n) | for or while loop |
| Quadratic | O(n^2) | loop in a loop |
| Exponential | O(c^n) | recursive calls over n and looing over c in the function |
| Factorial | O(n!) | looping over n and recursive call in the loop to n-1 |

| nlogn - O(n log n) - Merge sort, Quick sort

## Data Structure Performance

### for Average case

| Name        | Access   | Search   | Insert   | Delete   |
| ----------- | -------- | -------- | -------- | -------- |
| Stack       | O(n)     | O(n)     | O(1)     | O(1)     |
| Queue       | O(n)     | O(n)     | O(1)     | O(1)     |
| LinkedList  | O(n)     | O(n)     | O(1)     | O(1)     |
| Hash Tables | O(1)     | O(1)     | O(1)     | O(1)     |
| Binary Tree | O(log n) | O(log n) | O(log n) | O(log n) |

## Time complexity (Efficiency)

is a way to represent how the runtime of an algorithm grows as the input size increases. It helps us understand the efficiency of algorithms and make informed decisions about which algorithms to use in different scenarios.

Example:

```function printFirstItem(arr) {
  console.log(arr[0]);
}
```

The time complexity of this function is O(1) because it always takes the same amount of time to execute, regardless of the size of the input array.

## Space complexity (Memory Efficiency)

is a way to represent how the memory usage of an algorithm grows as the input size increases. It helps us understand the efficiency of algorithms in terms of memory usage and make informed decisions about which algorithms to use in different scenarios.

Example:

```function printFirstItem(arr) {
  console.log(arr[0]);
}
```

The space complexity of this function is O(1) because it only uses a constant amount of memory, regardless of the size of the input array.
