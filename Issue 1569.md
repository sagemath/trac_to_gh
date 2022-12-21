# Issue 1569: solve() fails if one list element is True

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-12-19 18:45:46

Assignee: was

As reported by Brandon Barker at http://groups.google.com/group/sage-devel/browse_thread/thread/52683f508ccefb39#:

```
sage: solve([3==3, 1.00000000000000*x^3 == 0], x)
[]
sage: solve([1.00000000000000*x^3 == 0], x)
[x == 0]
sage: solve([1==3, 1.00000000000000*x^3 == 0], x)
[]
```


The first result is wrong; it should be the same as the second.

Note that "3==3" will immediately evaluate to a Python boolean True; probably solve() should just strip list elements that are True.


---

Comment by was created at 2007-12-20 20:12:38

Changing status from new to assigned.


---

Attachment


---

Comment by rlm created at 2007-12-21 01:44:59

Resolution: fixed


---

Comment by rlm created at 2007-12-21 01:44:59

merged in 2.9.1 alpha2
