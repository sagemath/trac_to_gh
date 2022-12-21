# Issue 9053: Sage's new generic HNF doesn't quite work right wrt the free modules code

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-05-26 08:41:23

Assignee: AlexGhitza

CC:  minz

The last output below should obviously be True, but it is False.


```
sage: R.<x> = GF(7)[]
sage: A = R^3
sage: L = A.span([x*A.0 + (x^3 + 1)*A.1, x*A.2]); L
Free module of degree 3 and rank 2 over Univariate Polynomial Ring in x over Finite Field of size 7
Echelon basis matrix:
[      x x^3 + 1       0]
[      0       0       x]
sage: M = A.span([x*L.0]); M
Free module of degree 3 and rank 1 over Univariate Polynomial Ring in x over Finite Field of size 7
Echelon basis matrix:
[    x^2 x^4 + x       0]
sage: M.0 in L
False
```



---

Comment by AlexGhitza created at 2010-09-02 10:59:27

Changing assignee from AlexGhitza to jason, was.


---

Comment by AlexGhitza created at 2010-09-02 10:59:27

Changing component from algebra to linear algebra.


---

Attachment

The bug was a single line in _echelon_form_PID which returned the wrong pivot element for matrices of one row. The attached patch should fix that.

While doctesting all of Sage I received two errors (that seem unrelated?):

```
The following tests failed:

        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/gal_reps.py # Time out
        sage -t  -long -force_lib devel/sage/sage/interfaces/sage0.py # 2 doctests failed
```


The first apparently also came up during discussions on [#9390](http://trac.sagemath.org/sage_trac/ticket/9390). The doctest failure in sage0.py "randomly" appeared or not when I reran the test mutiple times. I'm not quite sure what to make of this...


---

Comment by minz created at 2011-03-18 10:47:06

Changing status from new to needs_review.


---

Comment by minz created at 2011-03-21 23:01:51

I just reran the above two doctests on a different machine and receieved no doctest failures. *shrug*


---

Comment by kini created at 2011-03-22 00:05:38

line wrapping


---

Attachment

I can't replicate your doctest failures. Everything passes on sage.math, except the ever-troublesome devel/sage/sage/tests/startup.py , which I tried again individually with no problems. The fix itself looks good. Reference builds, though how that could be affected I don't know. IIRC all code should be within 79 columns, so I split some lines in this function for you while you're at it. Feel free to rewrite it if it looks ugly, haha.


---

Comment by kini created at 2011-03-22 00:06:10

Changing status from needs_review to positive_review.


---

Comment by kini created at 2011-03-22 00:06:59

(for patchbot...)


---

Comment by jdemeyer created at 2011-04-07 13:48:21

Resolution: fixed
