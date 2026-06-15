# 1. Two Sum

**Difficulty:** Easy
**Topic:** Arrays, Hash Table

## 📝 Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input has **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### Example 1

```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

### Example 2

```text
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3

```text
Input: nums = [3,3], target = 6
Output: [0,1]
```

## 💡 Approach

Use a hash map (dictionary) to store each number and its index as we iterate through the array.

For every element:

1. Calculate the complement:

   ```python
   complement = target - nums[i]
   ```

2. Check whether the complement already exists in the hash map.

3. If it exists, return the stored index and the current index.

4. Otherwise, store the current number and its index in the hash map.

This approach allows us to find the solution in a single pass.


## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

## 🔑 Key Concepts

* Hash Table (Dictionary)
* One-Pass Algorithm
* Array Traversal

---

🔗 Problem Link: https://leetcode.com/problems/two-sum/
