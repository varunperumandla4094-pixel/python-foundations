# Python Foundations

Welcome to my Python learning journey!

I'm learning Python to improve my programming, problem-solving, and software development skills. This repository contains my daily practice exercises, coding challenges, and projects as I progress toward learning data structures, algorithms, and AI development.

## Day 1: Basic Calculator

### Project Description

This is my first Python project. I built a simple calculator that takes two numbers from the user and performs an arithmetic operation based on their choice.

The calculator also handles common errors, such as dividing by zero, entering an invalid operator, or entering text instead of a number.

### Features

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Division-by-zero handling
- Invalid operator handling
- Invalid number input handling using try/except

### Technologies Used

- Python 3
- Visual Studio Code
- Git and GitHub

### How to Run

1. Make sure Python 3 is installed.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run the following command:

`python day-01/calculator.py`

### Example Output

```text
Enter first number: 10
Enter second number: 5
Enter operation: +

Result: 15.0
```

### What I Learned

While building this calculator, I practiced:

- Variables and data types
- Taking user input with input()
- Converting strings to numbers using float()
- Arithmetic operators
- Conditional statements using if, elif, and else
- Python indentation
- Error handling using try and except
- Testing and debugging code

I also learned how to identify mistakes and improve my code step by step.

## My Learning Goals

My goal is to become confident in Python programming and technical problem-solving.

I plan to:

- Practice Python consistently.
- Learn data structures and algorithms.
- Solve LeetCode problems and understand common patterns.
- Build real-world Python and AI projects.
- Improve my software engineering and technical interview skills.

## Progress

| Day | Topic | Project | Status |
|---|---|---|---|
| 1 | Python fundamentals, conditions, error handling | Basic Calculator | Completed |

I'll continue updating this repository as I learn new concepts and build more projects.

## Day 2: Strings and Loops

### What I Learned

On Day 2, I learned how to work with strings and loops in Python.

I practiced string indexing, negative indexing, slicing, and reversing strings. I also learned how to use `for` loops and `while` loops to solve basic programming problems.

### Problems I Solved

- Extracting characters using string indexing and slicing
- Reversing strings using slicing
- Counting characters without using `len()`
- Counting vowels and consonants in a string
- Printing numbers using a while loop
- Calculating the sum of numbers from 1 to N

### Key Takeaways

I learned how indentation affects loop execution, why counters should be initialized outside loops, and how to combine conditions with loops.

I also practiced debugging mistakes and improving my solutions without copying the answers.

### Files

- `day-02/strings_practice.py`
- `day-02/for_loops.py`
- `day-02/while_loops.py`

## Day 3 - Python Lists and Array Fundamentals

### Topics Learned
- List creation, indexing, and updating elements
- List methods: append(), remove(), and pop()
- Traversing lists using for loops
- Counting elements and calculating running totals
- Finding the sum of even numbers
- Finding maximum and minimum values
- Counting occurrences of the largest number

### Programs Completed

1. **list_basics.py**
   - List indexing and updating
   - Adding and removing list elements

2. **list_traversal.py**
   - Traversing lists
   - Counting elements
   - Calculating the sum of even numbers

3. **max_min.py**
   - Finding maximum and minimum using one loop

4. **largest_occurrences.py**
   - Finding the largest number
   - Counting its occurrences

### Key Takeaways
- Learned to solve array problems using one-pass traversal.
- Practiced using counters, conditions, and running totals.
- Understood how to handle negative numbers and duplicates.
- Practiced O(n) time and O(1) extra-space algorithms.


## Day 4 - Python Functions

### Topics Learned
- Defining and calling functions
- Parameters and arguments
- Return values versus print()
- Functions with if/elif/else conditions
- Functions with for loops and lists
- Early return and function execution order

### Programs Completed

1. **functions_basics.py**
   - Defining and calling functions
   - Rectangle area calculation
   - Returning calculated values
   - Checking even and odd numbers

2. **functions_with_lists.py**
   - Calculating the sum of even numbers
   - Finding the largest number in a list
   - Returning results from loop-based functions

### Key Takeaways
- Functions allow code to be reused.
- Parameters receive arguments from function calls.
- return sends a result back to the caller.
- return ends the current function execution.
- Functions can process lists using loops.
- Practiced O(n) array algorithms.

**Status:** Completed

# Day 05 — Python Dictionaries

## Topics Covered

- Creating dictionaries using key-value pairs
- Accessing dictionary values using keys
- Adding and updating dictionary entries
- Handling missing keys using `get()`
- Checking key existence using `in`
- Iterating through dictionaries using `for` loops
- Using `.values()` and `.items()`
- Counting frequencies using dictionaries

## Mini Project: AI Request Monitoring System

Built a Python application that simulates monitoring AI service requests using dictionaries.

### Features

- Store AI job details in a dictionary
- Update job status and priority
- Count successful, failed, and pending requests
- Handle missing owner information
- Display event counts using `.items()`
- Calculate total events using `.values()`

## Technologies Used

- Python 3
- Dictionaries
- For Loops
- Conditional Statements

## Project File

`ai_request_monitor.py`

## How to Run

From the repository root:

```bash
python day-05/ai_request_monitor.py
```

## Expected Output

```text
Job: 501
Model: GPT-6
Status: Completed
Priority: High
Owner: Not assigned
success 3
failed 2
pending 1
Total events: 6
```

## Key Learnings

- Dictionaries store data as key-value pairs.
- `get()` safely retrieves missing keys with default values.
- `in` checks whether a key exists.
- `.items()` allows iteration through keys and values.
- `.values()` provides dictionary values for calculations.
- Dictionaries can efficiently count repeated events.


# Day 6 - Python Sets, Tuples, and LeetCode

## Overview

On Day 6 of my Python learning journey, I explored sets, tuples, and their practical applications in software engineering.

I also solved two LeetCode-style problems and built an AI Request Deduplication System.

## Concepts Learned

### 1. Python Sets
- Creating sets and removing duplicates
- Adding and removing elements
- Membership checking with `in`
- Union, intersection, and difference
- Using sets for efficient duplicate detection

### 2. Python Tuples
- Creating tuples
- Positive and negative indexing
- Understanding tuple immutability
- Reassigning tuple variables
- Using tuples to group configuration values

## LeetCode Problems

### Problem 217 - Contains Duplicate

**Objective:** Determine whether a list contains duplicate numbers.

**Approach:**
- Convert the list into a set.
- Compare the lengths of the list and set.
- Return True if the lengths differ, otherwise False.

**File:** `contains_duplicate.py`

**Time Complexity:** O(n) average case

**Space Complexity:** O(n)

### Problem 349 - Intersection of Two Arrays

**Objective:** Find unique numbers common to two arrays.

**Approach:**
- Convert both lists into sets.
- Use set intersection to find common elements.
- Convert the result back into a list.

**File:** `intersection_two_arrays.py`

**Time Complexity:** O(n + m) average case

**Space Complexity:** O(n + m)

## Mini-Project: AI Request Deduplication System

### Business Problem

AI applications may receive repeated request IDs due to retries or duplicate submissions.

Processing an already completed request again can waste computing resources and increase AI API costs.

### Solution

I developed a Python program that:

1. Accepts incoming request IDs.
2. Identifies unique request IDs using sets.
3. Finds previously processed requests using intersection.
4. Identifies new requests using set difference.
5. Stores AI model configuration in a tuple.
6. Generates a monitoring report using a reusable function.

### Technologies and Concepts

- Python
- Lists
- Sets
- Tuples
- Functions
- Set intersection and difference

### Sample Output

    AI Request Monitoring Report
    Total requests received: 7
    Unique request IDs: 5
    Previously processed requests: 2
    New requests to process: 3
    AI Model: GPT-6
    Max Tokens: 1000
    Environment: Production

### File

`ai_request_deduplication.py`

### Note

This is a learning project that identifies requests requiring processing. It does not yet connect to a real AI API or persist processing history.

## How to Run

From the repository root:

    python day-06/contains_duplicate.py
    python day-06/intersection_two_arrays.py
    python day-06/ai_request_deduplication.py

## Key Takeaways

- Sets are useful for handling unique values.
- Set intersection identifies shared elements.
- Set difference identifies missing or new elements.
- Tuples help group values that should not be reassigned individually.
- Functions improve code reusability.
- Python data structures can solve practical backend problems.

## Learning Goal

Build strong Python fundamentals, improve problem-solving skills through LeetCode, and prepare for AI Engineer and Forward Deployed Engineer roles.
