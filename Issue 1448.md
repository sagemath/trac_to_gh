# Issue 1448: iterate over MatrixSpace

Issue created by migration from https://trac.sagemath.org/ticket/1448

Original creator: malb

Original creation time: 2007-12-10 14:20:20

Assignee: was

This should work:

```
sage: MS = MatrixSpace(GF(2),2)
sage: for A in MS:
...     print A
```



---

Comment by mhansen created at 2007-12-14 07:10:18

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-12-14 07:10:18

Changing status from new to assigned.


---

Attachment


---

Attachment

I've been reviewing this patch. Generally pretty good (I like the implementation for infinite base rings, very neat)... a few minor issues to address:

 * I'd like to see more (i.e. nonzero) documentation in the docstring, in particular giving the definition of what ordering is being produced, and explaining what's going on in the case of an infinite base ring

 * The doctests should show more than that just the number of generated matrices is correct; currently they only give the number of matrices and the first matrix (which is all zero)

 * I'm a bit puzzled by the order of iteration. It starts by incrementing in the bottom right and then moves upwards. To me the other direction seems more natural. Maybe I'm "wrong" about this though.

 * There are some corner cases to address:


```
sage: MS = MatrixSpace(ZZ, 2, 0)
sage: i = iter(MS)
sage: i.next()
[]
sage: i.next()
(boom)
```


 * The doctests should include examples for 0xN, Nx0, 0x0 matrices.


---

Attachment

ok, I'm happy with this now.


---

Comment by rlm created at 2007-12-22 17:55:06

merged in 2.9.1 rc0


---

Comment by rlm created at 2007-12-22 17:55:06

Resolution: fixed
