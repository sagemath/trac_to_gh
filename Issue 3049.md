# Issue 3049: combinatorics -- lame overflow with Compositions(n).count() (very easy to fix)

Issue created by migration from https://trac.sagemath.org/ticket/3049

Original creator: was

Original creation time: 2008-04-28 15:24:02

Assignee: mhansen

CC:  sage-combinat

The following calculation is trivial, so shouldn't overflow:

```
sage: len(Compositions(30))
536870912
sage: len(Compositions(40))
Traceback (most recent call last):
...
OverflowError: long int too large to convert to int
```



---

Comment by was created at 2008-04-28 15:27:30

This is also


---

Comment by was created at 2008-04-28 19:20:30

This is caused by a stupid limitation in Python's len.  Use .count, etc. instead.


---

Comment by was created at 2008-04-28 19:20:30

Resolution: invalid
