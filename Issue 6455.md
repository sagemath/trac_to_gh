# Issue 6455: Bug in twisting for p_primary_bound on Tate-Shafarevich groups

Issue created by migration from Trac.

Original creator: wuthrich

Original creation time: 2009-07-01 13:57:06

Assignee: was

CC:  was

Keywords: Tate Sharafevich group, Elliptic curves

William Stein found a bug in `p_primary_part`, namely


```
sage: E = EllipticCurve([-19,34]); E.cremona_label()  # y^2 = x^3 - 19*x + 34
'944e1'
sage: S = E.sha(); S
Shafarevich-Tate group for the Elliptic Curve defined by y^2 = x^3 -
19*x + 34 over Rational Field
sage: E.ap(5)
-3
sage: factor(944)
2^4 * 59
sage: S.an_padic(5)
Traceback (most recent call last):
...
ValueError: can not twist a curve of conductor (=472) by the quadratic
twist (=-4).
```


The problem is at 2 and 3, we have to check if we are allowed to twist.


And John Cremona suggested 

_Is it possible to add a doctest illustrating the suggestion to "try an_padic instead"? That would be useful for the reference manual._




---

Comment by davidloeffler created at 2009-07-20 19:51:21

Changing component from number theory to elliptic curves.


---

Comment by davidloeffler created at 2009-07-20 19:51:21

Changing assignee from was to davidloeffler.


---

Comment by wuthrich created at 2009-07-21 21:37:09

I believe that the patch chooses now the correct twist. 

William : could you use it for the table, before it goes in ? so that I am sure that there are no further problems with it. I have tested it only on a few examples.


---

Attachment


---

Comment by cremona created at 2009-08-17 19:54:54

Patch applies fine to 4.1.1, and tests run ok.  The code looks ok to me too.  I'm not quite expert enough to be 100% confident, but enough to pass this!


---

Comment by jason created at 2009-10-06 19:00:23

Changing status from new to needs_review.


---

Comment by jason created at 2009-10-06 19:00:33

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2009-10-09 09:12:10

Remove assignee davidloeffler.


---

Comment by mhansen created at 2009-10-19 06:02:35

Resolution: fixed
