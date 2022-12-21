# Issue 2642: doctest failure in polynomial_modn_dense_ntl.pyx: .small_roots()

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-03-22 01:44:36

Assignee: malb

The doctest for .small_roots() randomly fails in 2.11.alpha0.


---

Attachment


---

Comment by cwitty created at 2008-03-22 01:48:44

I've attached a patch with one possible fix for the .small_roots() problem.

Evidently the current algorithm can return roots much larger than X, which breaks the doctest.  Under the assumption that more roots==good, I left that behavior (and documented it), and fixed the doctest to search for the root it wants.  Another possible fix would be to filter the roots and discard roots larger than X.


---

Comment by malb created at 2008-03-22 14:21:19

What exactly is the failure? The code shouldn't return any roots larger than X afaik iff you take into account that e.g. -1 === (N -1). Probably the representation of finite field elements for which the concept of small makes sense should be clarified in the docstring.


---

Comment by cremona created at 2008-03-23 17:15:49

This does not answer the outstanding question, but while looking at this code (and I did not get past the docstring, this is really not something I am familiar with) I found the following:

```
sage: N=10001
sage: p,q = map(lambda (r,m): r, N.factor())
```

which is so opaque that I could not ignore it.  Pleasr replace that last line with

```
sage: p,q = N.prime_divisors()
```

!!!


---

Attachment


---

Comment by malb created at 2008-03-24 00:51:22

Changing status from new to assigned.


---

Comment by malb created at 2008-03-24 00:51:22

The attached patch
 * replaces the opaque doctest line with `N.prime_divisors()`
 * enforces roots <= X

This should fix the issue (it does for me on sage.math).


---

Comment by malb created at 2008-03-24 00:52:27

To be precise this patch is a replacement for Carl's patch because I don't think it is correct.


---

Comment by was created at 2008-03-28 07:21:55

REVIEW:

Looks good (though I don't understand/know this LLL algorithm).  One thing -- cwitty's patch fixed some latexing/formating issues around line 320, and your patch doesn't fix those same issue.  You should remake your patch so that it fixes those formatting issues too, though this isn't at all critical.


---

Comment by mabshoff created at 2008-03-28 07:43:23

Applied small_roots_fix.patch and the "latex only" portion from trac2642-small-roots.patch to Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-28 07:43:23

Resolution: fixed
