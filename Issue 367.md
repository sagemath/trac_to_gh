# Issue 367: Text output from the notebook should indent after ... more.

Issue created by migration from https://trac.sagemath.org/ticket/367

Original creator: was

Original creation time: 2007-05-17 23:14:09

Assignee: boothby

This text output is confusing!

```
sage: def sum_of_two_squares_naive(n): 
...    for i in range(int(sqrt(n))): 
...        if is_square(n 


---

Comment by was created at 2007-05-18 15:42:54

Resolution: fixed
