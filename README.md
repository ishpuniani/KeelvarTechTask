# KeelvarTechTest
Submission for Keelvar tech test

## Problem Statement
Given a list of integers, check if the sum of any two integers in the list is not contained in the list.
For example with the list [4, 5, 15, 2, 8], there is no pair of integers where their sum is in the list. The list [8, 7, 5, 3] does not satisfy the criteria since the sum of 5 and 3 is in the list.
Write a python function which takes a list of integers and returns True if the list satisfies the criteria above, or False otherwise.

## To run test cases 
```shell script
python suite.py
```

## Approach
There are two approaches implemented in the solution:

### 1. Using a set
Check for each element present in the array.

Use a set to store elements present in the array. 
Before inserting the element, check if the difference of target and element exists in the array.

Time Complexity : O(n^2) <br>
Space Complexity : O(n)

### 2. Using 2 pointers
Sort the input array once and run the two pointer approach for every element in the array. 

Time Complexity : O(n^2) <br>
Space Complexity : O(1)