# 704. Binary Search

**Difficulty:** Easy
**Topic:** Array, Binary Search

## 📝 Problem Statement

Given an array of integers `nums` sorted in **ascending order** and an integer `target`, return the index of `target` if it exists in the array. Otherwise, return `-1`.

You must write an algorithm with **`O(log n)`** runtime complexity.

### Example 1

```text
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4.
```

### Example 2

```text
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums, so return -1.
```

## 💡 Key Idea

Binary Search works by repeatedly dividing the search space into two halves.

At each step:

1. Find the middle element.
2. If the middle element equals the target, return its index.
3. If the target is smaller, search the left half.
4. If the target is larger, search the right half.

> **Prerequisite:** The array must be sorted.

---

## 🧠 Iterative Approach

### ⏱️ Complexity Analysis

* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

## Recursive Approch

### ⏱️ Complexity Analysis

* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(log n)` due to the recursive call stack.

---

## ⚖️ Iterative vs Recursive

| Feature          | Iterative      | Recursive       |
| ---------------- | -------------- | --------------- |
| Time Complexity  | `O(log n)`     | `O(log n)`      |
| Space Complexity | `O(1)`         | `O(log n)`      |
| Performance      | Faster         | Slightly slower |
| Implementation   | More efficient | More intuitive  |

---

## 🔑 Key Concepts

* Divide and Conquer
* Recursion
* Iteration
* Two Pointers (`left`, `right`)
* Midpoint Calculation


