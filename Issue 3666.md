# Issue 3666: pari(infinity) looks like it works, but it doesn't

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-07-16 05:12:04

Assignee: mabshoff

This looks like `pari(infinity)` works:

```
sage: pari(infinity)
Infinity
```


but it's actually just creating a Pari variable named Infinity.

```
sage: (pari(infinity)-1)^2
Infinity^2 - 2*Infinity + 1
```


We should make pari(infinity) raise an exception, instead.  (As far as I can tell, Pari has no built-in notion of infinity, so we can't actually make it work.)


---

Comment by AlexGhitza created at 2009-10-24 12:22:03

Changing component from packages to interfaces.


---

Comment by AlexGhitza created at 2009-10-24 12:22:03

See attached patch.


---

Comment by AlexGhitza created at 2009-10-24 12:22:03

Changing status from new to needs_review.


---

Attachment


---

Comment by kcrisman created at 2009-10-29 18:51:13

Seems like Pari actually has INFINITY as a user-settable constant, which we probably would not want to make our oo equal to.  So nice patch and docs.

It's a little annoying that pari(maxima(inf)) still 'works', but Sage is only supposed to be the go-between, not to check that one doesn't do silly things with strings, so that's okay.  Positive review.


---

Comment by kcrisman created at 2009-10-29 18:51:13

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 05:23:11

Resolution: fixed
