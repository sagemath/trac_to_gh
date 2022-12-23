# Issue 1132: error inverting matrix over RQDF

Issue created by migration from https://trac.sagemath.org/ticket/1132

Original creator: mhansen

Original creation time: 2007-11-09 03:51:57

Assignee: was

I've attached b.sobj which you can load to reproduce the error.


```
sage: ~b
---------------------------------------------------------------------------
<type 'exceptions.ZeroDivisionError'>     Traceback (most recent call last)

/home/mike/<ipython console> in <module>()

/home/mike/matrix0.pyx in sage.matrix.matrix0.Matrix.__invert__()

<type 'exceptions.ZeroDivisionError'>: self is not invertible
sage: c = b.change_ring(RDF)
sage: ~c

[ 0.0277777777778  0.0277777777778  0.0277777777778  0.0277777777778  0.0277777777778  0.0277777777778]
[  0.111111111111  -0.111111111111  0.0555555555556 -0.0555555555556  0.0555555555556 -0.0555555555556]
[             0.0              0.0  0.0962250448649  0.0962250448649 -0.0962250448649 -0.0962250448649]
[            -0.0             -0.0  0.0962250448649 -0.0962250448649 -0.0962250448649  0.0962250448649]
[  0.111111111111   0.111111111111 -0.0555555555556 -0.0555555555556 -0.0555555555556 -0.0555555555556]
[ 0.0277777777778 -0.0277777777778 -0.0277777777778  0.0277777777778 -0.0277777777778  0.0277777777778]

```



---

Attachment


---

Comment by mhansen created at 2007-12-22 17:21:22

This is due to the following:


```
sage: b = load('/home/mike/Desktop/b.sobj')
sage: A = b.augment(b.parent().identity_matrix())
sage: B = A.echelon_form()
sage: B[5,5]
1.000000000000000000000000000000000000000000000000000000000000000
sage: B[5,5] == 1
False
```



---

Comment by mabshoff created at 2007-12-29 17:44:52

This ought to be solved. Maybe it is fodder fir Bug Day 8.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-14 05:38:44

Wontfix since we will remove RQDF - see #3762.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-14 05:38:44

Resolution: wontfix
