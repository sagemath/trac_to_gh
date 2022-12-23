# Issue 9880: fix the symbolic csgn function on complex input

Issue created by migration from https://trac.sagemath.org/ticket/9881

Original creator: burcin

Original creation time: 2010-09-09 09:04:30

Assignee: burcin

Keywords: pynac

Our wrapper of the csgn function from GiNaC (in `sage/symbolic/expression.pyx`) doesn't reflect it's real definition:


```
  /** Return the complex half-plane (left or right) in which the number lies.
   *  csgn(x)==0 for x==0, csgn(x)==1 for Re(x)>0 or Re(x)=0 and Im(x)>0,
   *  csgn(x)==-1 for Re(x)<0 or Re(x)=0 and Im(x)<0.
   *  */
```


Fix this and add doctests.

We should also consider using GiNaC's `csgn()` function for the top level `sgn()` and `sign()` functions. This should be on a different ticket though.


---

Attachment


---

Comment by burcin created at 2010-09-12 12:22:53

The new pynac package at #9201 changes the `csgn()` function according to the description. attachment:trac_9881-csgn.patch adds doctests for the new specification.

The pynac package includes patches for #9394, #9834, #9878, #9879, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.


---

Comment by burcin created at 2010-09-12 12:22:53

Changing status from new to needs_review.


---

Comment by burcin created at 2010-09-12 12:25:38

Replying to [comment:1 burcin]:
> The new pynac package at #9201 changes the `csgn()` function according to the description. 

That should have been "at #9901".


---

Comment by kcrisman created at 2010-10-05 00:38:36

Just FYI - this appears to still apply cleanly after the review patch at #9879.


---

Comment by kcrisman created at 2010-10-05 00:42:46

Okay, this looks good on both Pynac and Sage side - with the exception that I think the documentation needed slightly more clarity, and that some of the examples got misplaced to `binomial` for some reason.  Positive review; apply reviewer patch after initial patch.


---

Comment by kcrisman created at 2010-10-05 00:42:46

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-10-05 00:43:17

Apply after initial patch.


---

Comment by mpatel created at 2010-10-06 03:20:19

Resolution: fixed


---

Attachment
