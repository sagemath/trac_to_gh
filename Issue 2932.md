# Issue 2932: matrix.is_invertible() has inconsisten behavior over CDF

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-04-15 14:52:28

Assignee: was

From Alex Ghitza:


```
sage: M = matrix(CDF, 2, 2, [(-1 - 2*I, 5 - 6*I), (-2 - 4*I, 10 - 12*I)])
sage: M.is_invertible()
True
sage: M.determinant()
5.3290705182e-15 + 1.7763568394e-15*I
sage: M.inverse()
[ 1.01330991616e+15 - 2.58956978574e+15*I -5.06654958079e+14 +
1.29478489287e+15*I]
[ 5.62949953421e+14 + 5.62949953421e+14*I -2.81474976711e+14 -
2.81474976711e+14*I]

So because of roundoff errors, Sage thinks that we have an invertible
matrix.  But the code for echelon_form knows that it's not invertible:

sage: M.echelon_form()
[                                    1.0                             1.4
+ 3.2*I]
[-2.22044604925e-16 - 4.4408920985e-16*I
~       0]
sage: M.rank()
1
```



---

Comment by jason created at 2008-04-15 23:34:27

Using numpy gives the following:


```
sage: M = matrix(CDF, 2, 2, [(-1 - 2*I, 5 - 6*I), (-2 - 4*I, 10 - 12*I)])
sage: n=M.numpy()
sage: import numpy
sage: numpy.linalg.det(n)
0.0
sage: numpy.linalg.inv(n)
---------------------------------------------------------------------------
<class 'numpy.linalg.linalg.LinAlgError'> Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/misc/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/numpy/linalg/linalg.py in inv(a)
    244 def inv(a):
    245     a, wrap = _makearray(a)
--> 246     return wrap(solve(a, identity(a.shape[0], dtype=a.dtype)))
    247
    248 # Cholesky decomposition

/home/grout/sage/local/lib/python2.5/site-packages/numpy/linalg/linalg.py in solve(a, b)
    187     results = lapack_routine(n_eq, n_rhs, a, n_eq, pivots, b, n_eq, 0)
    188     if results['info'] > 0:
--> 189         raise LinAlgError, 'Singular matrix'
    190     if one_eq:
    191         return b.ravel().astype(result_t)

<class 'numpy.linalg.linalg.LinAlgError'>: Singular matrix
```



---

Comment by broune created at 2008-05-10 21:04:36

I propose that this code is working as intended - it cannot be expected that floating point calculations always provide the same results as would be obtained using precise calculations. It cannot either be assumed that two calculations that are equivalent using precise numbers are equivalent when using approximations. The attached patch adds docstring explanations of this to real and complex number classes and fields.

Other than that, I get this using Sage version 3.0:


```
sage: M = matrix(CDF, 2, 2, [(-1 - 2*I, 5 - 6*I), (-2 - 4*I, 10 - 12*I)])
sage: M.is_invertible()
False
```



---

Comment by broune created at 2008-05-10 21:04:36

Changing priority from critical to major.


---

Comment by broune created at 2008-05-10 21:04:36

Changing assignee from was to broune.


---

Comment by broune created at 2008-05-10 21:05:01

Changing status from new to assigned.


---

Attachment


---

Comment by jason created at 2008-05-11 01:14:18

I am curious what algorithms are used for is_invertible and inverse().  Apparently determinant() uses GSL; how does GSL compare with numpy generally for numeric algorithms?  Numpy uses the standard blas libraries an awful lot; what does GSL do?

If is_invertible and inverse() do not use standard numerical linear algebra functions (e.g., use ATLAS), then why not?  If it's an issue of NotImplemented, then let's open a ticket.  I would probably get to it by sometime this summer, since we have a numerical linear algebra workshop where I'm at.


---

Comment by jason created at 2008-05-11 01:24:22

From IRC (with editing out of other unrelated conversation):


```
[20:15] <jason--> re: 2932; what algorithms are used for numerical linear algebra over CDF for inverse() and is_invertible()?
[20:15] <jason--> I don't find those functions in matrix_complex_double_dense.pyx
[20:16] <jason--> are they the generic algorithms in matrix*.pyx?
[20:16] <wstein-3053> If they aren't in matrix_complex_double_dense then they are the generic ones.
[20:17] <jason--> thanks; also, does anyone have any feelings for GSL compared to numpy for numerical linear algebra?
[20:17] <wstein-3053> numpy is usually better.
[20:18] <jason--> okay; do you mind if we switch the determinant function to numpy for matrices over CDF?
[20:18] <wstein-3053> jason-- please do.
[20:19] <jason--> okay; ticket coming right up.
```



---

Comment by craigcitro created at 2008-06-15 21:40:02

Changing keywords from "" to "editor_ncalexan".


---

Comment by craigcitro created at 2008-06-20 04:11:26

Changing keywords from "editor_ncalexan" to "editor_malb".


---

Comment by malb created at 2008-06-23 17:48:57

What is the current status of this ticket? I just to over being the editor for this ticket so please speak up :-)


---

Comment by jason created at 2008-06-23 22:39:45

I just got back into town (been gone for a month).  I'd still like to make numpy the default backend for CDF and RDF and I'll probably work on that this week.


---

Comment by jason created at 2008-06-23 22:41:41

Since the patch is just documentation telling the user not to expect exact results, I like it.  +1 from me.  Even when I convert things to numpy, it would still be good to have such a disclaimer, I think.


---

Comment by jason created at 2008-06-23 22:53:05

See ticket #3498 for switching the backend to numpy.


---

Comment by mabshoff created at 2008-06-25 07:47:40

Merged in Sage 3.0.4.alpha1


---

Comment by mabshoff created at 2008-06-25 07:47:40

Resolution: fixed
