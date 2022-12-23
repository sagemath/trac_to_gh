# Issue 6224: sage startup takes way to long

Issue created by migration from https://trac.sagemath.org/ticket/6224

Original creator: robertwb

Original creation time: 2009-06-05 10:16:36

Assignee: tbd

This is after the cache is warm, otherwise it's even worse: 


```
Robert-Bradshaws-Laptop:~/sage robert$ echo "" | time sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: referee
sage: sage: 
Exiting SAGE (CPU time 0m0.08s, Wall time 0m0.17s).
        2.58 real         1.23 user         1.19 sys
| Sage Version 4.0, Release Date: 2009-05-29                         |
| Type notebook() for the GUI, and license() for information.        |
```


We need to go through and audit the startup imports again. 


---

Comment by robertwb created at 2009-06-05 10:17:34

I should mention, this is OS X 10.4 with a 2.33 core duo. (OS X is known to be particularly bad, but < 1 second shouldn't be unreasonable.)
