# Issue 5267: bug in plotting the zero locus of an ideal in an mpoly ring

Issue created by migration from https://trac.sagemath.org/ticket/5267

Original creator: AlexGhitza

Original creation time: 2009-02-14 10:46:56

Assignee: malb

I just ran into this (on 3.3.rc0):


```
sage: S.<u, v> = QQ[]
sage: I = Ideal(-u^2*v+1)
sage: I.plot()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/ghitza/.sage/temp/artin/23695/_home_ghitza__sage_init_sage_0.py in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.pyc in plot(self, *args, **kwds)
   2387                     v, mi, ma = variables[var_index], -10, 10
   2388                     for i in range(mi, ma):
-> 2389                         roots = f.subs({v:i}).univariate_polynomial().change_ring(RR).roots()
   2390                         if len(roots) > 0:
   2391                             mi = i - 1

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.univariate_polynomial (sage/rings/polynomial/multi_polynomial_libsingular.cpp:21299)()

IndexError: list index out of range
```




---

Comment by AlexGhitza created at 2009-02-14 11:04:22

Tracked it down to a bug in turning a constant multivariate polynomial into a univariate one, as in the following example:


```
sage: S.<u, v> = QQ[]
sage: f = S(1)
sage: f.univariate_polynomial()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/ghitza/.sage/temp/artin/769/_home_ghitza__sage_init_sage_0.py in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.univariate_polynomial (sage/rings/polynomial/multi_polynomial_libsingular.cpp:21299)()

IndexError: list index out of range
```


In light of this, I'm changing the summary of the ticket.  I'll have a patch up soon.


---

Comment by AlexGhitza created at 2009-02-14 11:21:37

The attached patch fixes the bug causing all this, and adds doctests for both the bug and the initial (plotting) issue.

The fix is quite trivial, so should be easy to review.


---

Attachment


---

Comment by AlexGhitza created at 2009-02-14 11:53:00

Changing assignee from malb to AlexGhitza.


---

Comment by AlexGhitza created at 2009-02-14 11:53:09

Changing status from new to assigned.


---

Comment by malb created at 2009-02-14 15:35:10

Looks good.


---

Comment by mabshoff created at 2009-02-14 16:09:35

Merged in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 16:09:35

Resolution: fixed
