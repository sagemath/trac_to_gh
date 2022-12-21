# Issue 2456: matrix_symbolic_dense doctest failures

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-03-10 13:53:55

Assignee: was


```
File "matrix_symbolic_dense.pyx", line 873:
    sage: list(a.fcp())
Expected:
    [(x^2 - 65*x - 250, 1), (x, 3)]
Got:
    [(x, 3), (x^2 - 65*x - 250, 1)]
```

But inside sage:

```
sage: a = matrix(SR, 5, [1..5^2]) 
sage: a.fcp()
(x^2 - 65*x - 250) * x^3
sage: list(a.fcp())
[(x^2 - 65*x - 250, 1), (x, 3)]
```



---

Comment by gfurnish created at 2008-03-10 14:01:06

This patch is correct because of changes in #2206


---

Comment by gfurnish created at 2008-03-10 14:01:31

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-03-10 14:01:31

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-10 15:59:01

This patch fixes problems in factorization that cause problems here.


---

Comment by was created at 2008-03-10 16:06:15

REFEREE REPORT:

 * The second chunk in trac_2456.patch, which swaps the order of sort and simplify, breaks things.  This is because simplify assumes its input is sorted, as it combines adjacent pairs.

 * The rest of the patch looks fine.


---

Attachment

replaced patch addresses my concern.


---

Comment by mabshoff created at 2008-03-10 17:19:46

Resolution: fixed


---

Comment by mabshoff created at 2008-03-10 17:19:46

Merged in Sage 2.10.3.rc4
