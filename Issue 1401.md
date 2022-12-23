# Issue 1401: deprecate A[n] for n a matrix (easy to implement usability improvement)

Issue created by migration from https://trac.sagemath.org/ticket/1401

Original creator: was

Original creation time: 2007-12-04 23:57:36

Assignee: was

Sage currently works this way:

```
sage: a = matrix(ZZ, 2, [1..4])
sage: a[1]
(3, 4)
sage: a.row(1)
(3, 4)
sage: a[1][0] = 5
sage: a
[1 2]
[3 4]
```


Instead Sage should do this:


```
sage: a = matrix(ZZ, 2, [1..4])
sage: a[1]
boom!
sage: a.row(1)
(3, 4)
sage: a[1][0] = 5
boom!
```


Where boom explains that one should use a.row(...) to get a row, or a[i,j] to get/set the ij entry.

This confuses the heck out of TONS of people!!!  (Not me, but others.)


---

Comment by mhansen created at 2007-12-06 21:17:00

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-06 21:17:00

Changing assignee from was to mhansen.


---

Attachment


---

Comment by mhansen created at 2007-12-06 23:15:55

Patch attached.


---

Comment by was created at 2007-12-15 12:57:15

I just realized that a much better solution is to finish implementing immutable vectors and make the return of A[n] be an immutable row.  It accomplishes the same thing and is more usable.  So I did this.

That said, the above patch is fine -- using .row(...) all over in code is fine and faster.


---

Attachment


---

Comment by mabshoff created at 2007-12-15 13:32:06

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 13:32:06

Resolution: fixed
