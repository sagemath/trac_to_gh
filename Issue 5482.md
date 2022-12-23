# Issue 5482: Quotient ring can be created without generator names

Issue created by migration from https://trac.sagemath.org/ticket/5482

Original creator: justin

Original creation time: 2009-03-11 06:44:39

Assignee: was

The following code works:

```
sage: R.<x> = PolynomialRing(QQ)
sage: f = x^2-1
sage: S = R.quotient_by_principal_ideal(f)
```

but then this fails:

```
sage: S
 ---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...[snip]
/Users/tmp/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/category_object.so in sage.structure.category_object.CategoryObject.variable_names (sage/structure/category_object.c:3530)()

ValueError: variable names have not yet been set using self._assign_names(...)
```

The routine should require that the name(s) be provided.




---

Attachment

The fix is to require the generator name at creation time, not when the ring is used.


---

Comment by cremona created at 2009-03-14 20:42:05

Why do you change the parameter name from "names" to "name"?  Is this function only used for univariate polynomial rings?  If so, fine.


---

Comment by was created at 2009-03-15 23:52:40

REFEREE REPORT:

 1. It *must* be "names" not "name", so the R.<x> = foo notation works.

 2. Every patch has to have a doctest that illustrates that it fixes the bug.


---

Comment by justin created at 2009-03-16 03:16:40

Changing status from new to assigned.


---

Comment by justin created at 2009-03-16 03:16:40

Changing assignee from was to justin.


---

Comment by justin created at 2009-03-16 03:16:40

Replying to [comment:4 was]:
> REFEREE REPORT:
> 
>  1. It *must* be "names" not "name", so the R.<x> = foo notation works.

I discovered that while adding doctests.  I'll reverse that change.

>  2. Every patch has to have a doctest that illustrates that it fixes the bug.

Doctests?


---

Comment by AlexGhitza created at 2009-11-15 11:53:13

Changing component from algebraic geometry to algebra.


---

Comment by AlexGhitza created at 2009-11-15 12:35:50

I attached a new patch that assigns names automatically if they are not specified by the user, e.g. a quotient of `R.<x>` will have variable name `xbar`.  This is standard behaviour in other places in Sage.

Apply trac_5482.patch only.


---

Comment by AlexGhitza created at 2009-11-15 12:35:50

Changing status from needs_work to needs_review.


---

Attachment

apply this patch only


---

Comment by mhansen created at 2009-11-17 08:02:57

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-17 08:02:57

Looks good to me.


---

Comment by mhansen created at 2009-11-17 08:03:08

Resolution: fixed
