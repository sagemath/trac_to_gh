# Issue 54: guaranteed correct result for log(integer, integer)

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-09-13 20:40:38

Assignee: somebody

In a current project, I often want to know the largest power of a prime p that is less than or equal to a given integer n. I used int(log(n, p)) in these cases, but I'm concerned that there might be precision issues in this floating point calculation. It would be nice to have some function that was guaranteed to return the correct result for floor(log(n, p)), where n and p are integers. Perhaps call it floor_log or something.



---

Comment by dmharvey created at 2006-09-22 01:21:33

fixed -- added Integer.exact_log()


---

Comment by dmharvey created at 2006-09-22 01:21:33

Resolution: fixed
