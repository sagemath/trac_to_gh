# Issue 2256: matrix inverse over CC raises ZeroDivisionError

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-02-22 08:00:07

Assignee: was

CC:  ncalexan jason cwitty robertwb

Keywords: matrix inverse CC complex


```
sage: M = matrix(CC, 2, 2, [(-1.00000000000000 - 2.00000000000000*I, 5.00000000000000 - 6.00000000000000*I), (-2.00000000000000 - 2.00000000000000*I, 7.00000000000000 - 8.00000000000000*I)])
sage: M

[-1.00000000000000 - 2.00000000000000*I  5.00000000000000 - 6.00000000000000*I]
[-2.00000000000000 - 2.00000000000000*I  7.00000000000000 - 8.00000000000000*I]
sage: M.determinant()
-1.00000000000000 - 8.00000000000000*I
sage: M.inverse()
---------------------------------------------------------------------------
<type 'exceptions.ZeroDivisionError'>     Traceback (most recent call last)

/Users/ncalexan/sage-2.10.2.alpha0/devel/sage-genus2cm/sage/schemes/plane_curves/<ipython console> in <module>()

/Users/ncalexan/sage-2.10.2.alpha0/devel/sage-genus2cm/sage/schemes/plane_curves/matrix2.pyx in sage.matrix.matrix2.Matrix.inverse()

/Users/ncalexan/sage-2.10.2.alpha0/devel/sage-genus2cm/sage/schemes/plane_curves/matrix0.pyx in sage.matrix.matrix0.Matrix.__invert__()

<type 'exceptions.ZeroDivisionError'>: self is not invertible
sage: M.parent().change_ring(CDF)(M).inverse()

[ 0.876923076923 + 0.984615384615*I -0.661538461538 - 0.707692307692*I]
[-0.276923076923 + 0.215384615385*I 0.261538461538 - 0.0923076923077*I]
```



---

Comment by mhansen created at 2008-02-22 21:33:15

I made a similar ticket with the same issue with RQDF.  I think the following is the underlying problem:


```
sage: me = M.echelon_form()
sage: me

[                         1.00000000000000                     -2.22044604925031e-16]
[                                        0 1.00000000000000 - 5.55111512312578e-17*I]
sage: me[0,0] == 1
True
sage: me[1,1] == 1
False
```



---

Comment by dunfield created at 2008-05-12 02:46:07

mhansen's comment is right on.  Indeed, SAGE is successfully computing the inverse, but the __invert__ method is throwing an exception because of the diagonal elements of the echelon form are not all ones.   This is simply because:


```
sage: a = CC(-1, -2); b = CC(5, -6); c = CC(-2,-2); d = CC(7, -8)
sage: z = d - b*c/a
sage: z * z^-1
1.00000000000000 - 5.55111512312578e-17*I
```


Ah, the joys of inexact fields.   See also the ticket #3162.


---

Comment by craigcitro created at 2009-06-09 09:13:08

I'm attaching a patch which doesn't *completely* fix this, but makes it better -- I think. 

First, a brief description of the problem: the code creates an augmented matrix, puts it in echelon form, and asks if the lower right entry of the left half is equal to 1. This is correct over an exact field, but over an inexact ring like `CC`, this causes trouble. 

Now, if we're working over a base ring which we know is a field (or at least models a field), then we know the lower right entry of the matrix must be either 1 or 0. So rather than test to see if something equals 1, I simply test that the lower right entry is *not* 0. 

A better solution would be to ask that the determinant is nonzero -- unfortunately, our determinant over general inexact fields is a joke, and can't even deal with a `10x10` example, so that's a no-go. 

Comments:

This still isn't perfect -- it's easy enough to imagine cases where numerical instability causes trouble. Note that the current behavior is basically always wrong (since it almost always claims the matrix isn't invertible when it is), and it's also pretty confusing to newcomers. The new code has the disadvantage that it can now offer to return an inverse for non-invertible matrices, based on numerical issues. However, I think that to someone who's used matrices over inexact rings before in their life, this isn't so surprising -- it's just the way it goes with approximations. 

I don't know what the "right" solution is -- we should probably ask someone who studies numerical analysis.

I'm adding `jason`, `cwitty`, and `robertwb` to the ticket, because they're all likely to have interesting commentary and/or review the patch.


---

Attachment

The LU decomposition patch at #3048 may go a long ways towards helping this.  At least the determinant then is much, much better.  Or even better, just examine the U of the LU decomposition and decide if a diagonal entry is zero (which avoids the overhead of a product).

The LU decomposition patch (#3048) also changes the inverse function to use sove_right (which uses LU decomposition) as in general, that should be faster anyway.

The real way to do this is to have a rank function which works by looking at the smallest singular value.  That requires having a singular value decomposition...


---

Comment by ncalexan created at 2009-06-14 22:49:07

Resolution: fixed


---

Comment by ncalexan created at 2009-06-14 22:49:07

The LU stuff is not ready and this at least improves the situation.
