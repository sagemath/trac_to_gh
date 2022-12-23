# Issue 2888: matrix slicing fails in degenerate cases

Issue created by migration from https://trac.sagemath.org/ticket/2888

Original creator: AlexGhitza

Original creation time: 2008-04-12 00:47:43

Assignee: was

Keywords: slice

The following should return [] but it throws an exception instead:


```
sage: M = matrix(3, 4, range(12))
sage: M[0:3, 2:2]
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/opt/sage-3.0.alpha2/devel/sage-main/<ipython console> in <module>()

/opt/sage-3.0.alpha2/devel/sage-main/matrix0.pyx in sage.matrix.matrix0.Matrix.__getitem__()

<type 'exceptions.ValueError'>: max() arg is an empty sequence
```


Same problem if I try M[0:0, 0:0].  This is an obstacle in doing #2616, since submatrix() does handle these cases properly.



---

Comment by dfdeshom created at 2008-04-12 16:47:54

Changing assignee from was to dfdeshom.


---

Attachment

patch against alpha3


---

Comment by dfdeshom created at 2008-04-13 03:11:24

A patch has been made against 3.0-alpha3


---

Comment by AlexGhitza created at 2008-04-13 03:41:29

Looks good.


---

Comment by mabshoff created at 2008-04-13 04:10:30

Hi,

the patch doesn't apply cleanly against my merge tree:

```
sage-3.0.alpha4/devel/sage$ patch -p1 --dry-run < trac_2888.patch
patching file sage/matrix/matrix0.pyx
Hunk #1 FAILED at 613.
Hunk #2 succeeded at 694 (offset 21 lines).
1 out of 2 hunks FAILED -- saving rejects to file sage/matrix/matrix0.pyx.rej
```

The first hunk are the added doctests, so it is easy enough to do. I won't mind if somebody beasts me to it.

Cheers,

Michael


---

Attachment

patch against upcoming alpha release


---

Comment by mabshoff created at 2008-04-13 05:09:50

Merged 2888-incoming-alpha4.patch in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-13 05:09:50

Resolution: fixed
