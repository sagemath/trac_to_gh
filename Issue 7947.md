# Issue 7947: iteration error in QuadraticForm.vectors_by_length()

Issue created by migration from https://trac.sagemath.org/ticket/7947

Original creator: tornaria

Original creation time: 2010-01-16 14:24:23

Assignee: tornaria

CC:  jonhanke

After the fix in #7100 (rounding issues), there's still a bug in `the vectors_by_length()` code:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Q = QuadraticForm(ZZ, 4, [1,-1,-1,-1, 1,0,0, 4,-3, 4])
sage: Q.vectors_by_length(3)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
| Sage Version 4.3, Release Date: 2009-12-24                         |
| Type notebook() for the GUI, and license() for information.        |
/home/tornaria/.sage/temp/sage/9609/_home_tornaria__sage_init_sage_0.py in <module>()

/home/tornaria/sage/sage-4.3/local/lib/python2.6/site-packages/sage/quadratic_forms/quadratic_form__split_local_covering.pyc in vectors_by_length(self, bound)
    213             ## Now go back and compute the bounds...
    214             ## 2. Compute bounds
--> 215             Z = (T[i] / Q[i][i]).sqrt(extend=False)
    216             L[i] = ( Z - U[i]).floor()
    217             x[i] = (-Z - U[i]).ceil()

/home/tornaria/sage/sage-4.3/local/lib/python2.6/site-packages/sage/rings/real_double.so in sage.rings.real_double.RealDoubleElement.sqrt (sage/rings/real_double.c:10382)()

ValueError: negative number -0.888887555556 does not have a square root in the real field
```

You can tell this is not a rounding issue from the error message.


---

Attachment

fix iteration error in QuadraticForm.vectors_by_length()


---

Comment by tornaria created at 2010-01-16 14:35:37

Changing status from new to needs_review.


---

Comment by jonhanke created at 2010-02-06 10:02:25

Changing status from needs_review to positive_review.


---

Comment by jonhanke created at 2010-02-06 10:02:25

This is a subtle bug which arises because negative numbers are created when the round and ceil functions cause upper and lower bounds to inadvertently move past each other.  The patch discards partial vectors where this happens by incrementing (successively if necessary) to the next possible partial vector, which is the correct thing to do.  Also the patch omits using a condition (i<n-1) as in Comment 3a slightly below the patch, which is ok because zero will always be an allowed value for the (n-1)st entry since that first allowed interval is not shifted at all.

The patch looks good. =)


---

Comment by mpatel created at 2010-02-11 14:54:29

Resolution: fixed
