# Issue 5639: minpoly of symbolic matrices is broken

Issue created by migration from https://trac.sagemath.org/ticket/5639

Original creator: was

Original creation time: 2009-03-30 03:03:04

Assignee: burcin

CC:  kcrisman


```
sage: m = matrix(2,[1,sqrt(2), 3, -5/2])
sage: m.minpoly()
```



---

Comment by mhansen created at 2009-06-05 02:52:06

This is because the charpoly method needs to return a univariate polynomial rather than an Expression.


---

Comment by mhansen created at 2009-06-05 02:52:06

Changing keywords from "" to "".


---

Comment by mhansen created at 2009-09-30 07:49:56

Changing assignee from burcin to mhansen.


---

Comment by mhansen created at 2009-09-30 07:49:56

Changing status from new to assigned.


---

Comment by jason created at 2009-10-06 21:34:47

in the docstring, "polynomial" is misspelled "polynomail"


---

Comment by jason created at 2009-10-06 21:35:26

Consider applying #6936, which also implements a generic way to test this fix!


---

Comment by jason created at 2009-10-06 21:41:46

Changing status from needs_review to needs_work.


---

Comment by jason created at 2009-10-06 21:41:46

I think this patch broke charpoly.  See the doctest around line 280 of matrix_symbolic_dense.pyx:


```
sage: M = matrix(SR, 2, 2, var('a,b,c,d'))
sage: M.charpoly('t')
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (288, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/.sage/temp/sage.math.washington.edu/17572/_home_jason__sage_init_sage_0.py in <module>()

/home/jason/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix_symbolic_dense.so in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense.charpoly (sage/matrix/matrix_symbolic_dense.c:2620)()
    289         # correct for the discrepancy.
    290         cp = self._maxima_(maxima).charpoly(var)._sage_()
--> 291         cp = cp.expand().polynomial(None, ring=SR[var])
    292         if self.nrows() % 2 == 1:
    293             cp = -cp

/home/jason/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.polynomial (sage/symbolic/expression.cpp:17292)()

/home/jason/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in polynomial(ex, base_ring, ring)
    985          1.87813065119873*x^2 + 20.0855369231877
    986     """
--> 987     converter = PolynomialConverter(ex, base_ring=base_ring, ring=ring)
    988     res = converter()
    989     return converter.ring(res)

/home/jason/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __init__(self, ex, base_ring, ring)
    843             G = ring.variable_names_recursive()
    844             if any([repr(v) not in G for v in ex.variables()]):
--> 845                 raise TypeError, "%s is not a variable of %s" %(v, ring)
    846             self.ring = ring
    847             self.base_ring = ring.base_ring()

TypeError: t is not a variable of Univariate Polynomial Ring in t over Symbolic Ring
```



---

Comment by kcrisman created at 2009-10-07 01:52:21

Hey, might that last error be related to the ticket which implements getting variables out of polynomial rings (e.g. 1.00*t was a variable but t wasn't)?


---

Comment by jason created at 2009-10-07 02:56:20

Replying to [comment:10 kcrisman]:
> Hey, might that last error be related to the ticket which implements getting variables out of polynomial rings (e.g. 1.00*t was a variable but t wasn't)?

That doesn't seem likely to me.  I'm wondering if the error has to do with the variable in the symbolic expression coming from maxima being a different variable than what is requested in SR[var] (i.e., the "t"s in the TypeError are not the same object).  This is just a guess, though.


---

Comment by jason created at 2009-10-07 03:01:06

I believe this shows the error more clearly, maybe:


```
sage: var('s,t')
(s, t)
sage: expr=t^2-2*s*t+1
sage: expr.expand()
-2*s*t + t^2 + 1
sage: expr.polynomial(None,ring=SR['t'])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/.sage/temp/littleone/25931/_home_jason__sage_init_sage_0.py in <module>()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.polynomial (sage/symbolic/expression.cpp:17284)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in polynomial(ex, base_ring, ring)
    985          1.87813065119873*x^2 + 20.0855369231877
    986     """
--> 987     converter = PolynomialConverter(ex, base_ring=base_ring, ring=ring)
    988     res = converter()
    989     return converter.ring(res)

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __init__(self, ex, base_ring, ring)
    843             G = map(repr, ring.gens())
    844             if any([repr(v) not in G for v in ex.variables()]):
--> 845                 raise TypeError, "%s is not a variable of %s" %(v, ring)
    846             self.ring = ring
    847             self.base_ring = ring.base_ring()

TypeError: t is not a variable of Univariate Polynomial Ring in t over Symbolic Ring

```



---

Comment by jason created at 2009-10-07 03:14:21

Yep, the problem is in this code in `PolynomialConverter` in `sage/symbolic/expression_conversions.py`:


```
        if ring is not None:
            G = map(repr, ring.gens())
            if any([repr(v) not in G for v in ex.variables()]):
                raise TypeError, "%s is not a variable of %s" %(v, ring)
            self.ring = ring
            self.base_ring = ring.base_ring()
```


Note that this does not allow for coefficients to have variables, but coefficients may have variables if the base ring is the symbolic ring!

Note that the error message in the last comment is misleading: it should say that "s is not a variable of ...", but since the test uses "any", it doesn't know which variable is bad.


---

Comment by mhansen created at 2009-10-19 18:21:56

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2009-10-19 18:21:56

I've posted a patch which address the issues above.


---

Comment by jason created at 2009-10-28 21:30:33

Looks great!  Doctests pass in matrix/*.py[x]


---

Comment by jason created at 2009-10-28 21:30:33

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 05:30:57

Resolution: fixed


---

Comment by mhansen created at 2009-10-31 09:10:55

There were a few failures cauesed by this in wester and coerce_maps for example.  I've backed out the patch.

I'll post a new patch addressing these issues.


---

Comment by mhansen created at 2009-10-31 09:10:55

Changing status from closed to needs_work.


---

Attachment

I've posted a new patch which takes care of these issues.


---

Comment by mhansen created at 2009-11-03 10:14:48

Changing status from needs_work to needs_review.


---

Comment by jason created at 2009-11-03 10:36:05

Hmmm, generating a new variable based on a name that is not likely to be used is questionable.  Does symbolics not have a gensym-like function that generates a new variable that is not currently being used?


---

Comment by mhansen created at 2009-11-03 12:50:54

Not right now, but there's a patch on trac which adds that functionality.

I'm just left the current behavior in this patch.


---

Comment by jason created at 2009-11-10 04:36:48

apply on top of previous patch


---

Attachment

Looks okay, doctests pass on affected files.  I posted a patch with a doctest as well, as a reviewer patch.  Positive review.


---

Comment by jason created at 2009-11-10 04:37:32

Changing status from needs_review to positive_review.
