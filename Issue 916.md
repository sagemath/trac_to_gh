# Issue 916: [with patch] remove structure.sequence._combinations

Issue created by migration from https://trac.sagemath.org/ticket/916

Original creator: malb

Original creation time: 2007-10-18 11:10:39

Assignee: was

CC:  sage-combinat

`_combinations` does the same as `combinations_iterator` but is slower. The attached patch therefor removes it and replaces all calls to it by calls to `combinations_iterator`.


```
sage: time l1 = list(combinations_iterator(range(100),3))
CPU times: user 0.91 s, sys: 0.01 s, total: 0.91 s
Wall time: 0.93
sage: time l2 = list(_combinations(range(100),3))
CPU times: user 3.96 s, sys: 0.13 s, total: 4.09 s
Wall time: 4.13
sage: l1 == l2
```



---

Attachment


---

Comment by malb created at 2007-10-21 22:44:57

Changing assignee from was to malb.


---

Comment by malb created at 2007-10-21 22:44:57

Changing status from new to assigned.


---

Comment by malb created at 2007-10-23 19:46:34

Resolution: fixed


---

Comment by malb created at 2007-10-23 19:46:34

applied to 2.8.9.alpha0
