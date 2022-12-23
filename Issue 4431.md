# Issue 4431: [with patch, needs review] conversion of maxima matrices to sage matrices

Issue created by migration from https://trac.sagemath.org/ticket/4431

Original creator: whuss

Original creation time: 2008-11-03 19:37:18

Assignee: whuss

This patch implements conversion of Maxima matrices, to Sage matrices. The patch is based on
sage-3.2alpha1.

A sample session:

```
sage: var('x,y')
sage: v = maxima('v: vandermonde_matrix([x, y, 1/2])')
sage: v
matrix([1,x,x^2],[1,y,y^2],[1,1/2,1/4])
sage: type(v)
<class 'sage.interfaces.maxima.MaximaElement'>
sage: v.sage()

[  1   x x^2]
[  1   y y^2]
[  1 1/2 1/4]
sage: mlist = maxima('[v, sin(x), 1, v.v]').sage()
sage: mlist

[[  1   x x^2]
[  1   y y^2]
[  1 1/2 1/4],
    sin(x),
    1,
    [       x^2 + x + 1    x*y + x^2/2 + x    x*y^2 + 5*x^2/4]
[       y^2 + y + 1        3*y^2/2 + x  y^3 + y^2/4 + x^2]
[               7/4      y/2 + x + 1/8 y^2/2 + x^2 + 1/16]]
sage: [parent(i) for i in mlist]

[Full MatrixSpace of 3 by 3 dense matrices over Symbolic Ring,
    Symbolic Ring,
    Symbolic Ring,
    Full MatrixSpace of 3 by 3 dense matrices over Symbolic Ring]
```




---

Comment by mhansen created at 2008-11-04 20:48:44

This patch looks good, but you should add the Vandermonde matrix as a test / example in the appropriate spot.  Also, I think the following construction is a bit cleaner than the string one:


```
sage: v = maxima.vandermonde_matrix([x,y,1/2])
```



---

Attachment

I updated the patch with some doctests.


---

Comment by was created at 2008-11-27 18:07:08

I pinged mhansen to look at this.  He should finish the review instead of this bitrotting.


---

Comment by mhansen created at 2008-11-27 18:21:24

Looks fine to me.


---

Comment by mabshoff created at 2008-11-28 07:50:27

Merged in Sage 3.2.1.rc0

Since this is a diff I checked in the changes in Wilfried's name.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-28 07:50:27

Resolution: fixed
