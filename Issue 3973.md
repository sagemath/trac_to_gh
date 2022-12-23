# Issue 3973: [with patch, needs review] short_weierstrass_model in characteristic 2 and 3

Issue created by migration from https://trac.sagemath.org/ticket/3973

Original creator: wuthrich

Original creation time: 2008-08-28 11:51:02

Assignee: was

CC:  cremona

this is to correct a small thing in short_weierstrass_model. It used to return an error in characteristic 3 for each curve, even if the curve was given in short weierstrass form.


---

Attachment

correcting the behaviour of short_weierstrass_model in characteristic 3


---

Comment by mabshoff created at 2008-08-28 12:03:00

Chris,

please assign a milestone to all tickets you open. Usually the next release is the one that should be selected.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-28 12:04:31

One small comment on the patch: Please escape the hash in the docstring since otherwise TeX will be unhappy when building the documentation:

```
This used to be different see trac #3973
```


John: I assume this patch is right up your alley.

Cheers,

Michael


---

Attachment


---

Comment by cremona created at 2008-08-28 13:39:09

Looks good to me -- Chris had already pointed out to me this missing case (in code I wrote).

I fixed the hash, and also made a couple of small other changes to the docstring which makes it clearer (I hope).  

Applies cleanly to 3.1.1, and all doctests in elliptic_curves pass.  I think this (both patches) can be merged.


---

Comment by mabshoff created at 2008-08-28 20:39:47

Resolution: fixed


---

Comment by mabshoff created at 2008-08-28 20:39:47

Merged both patches in Sage 3.1.2.alpha2
