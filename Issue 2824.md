# Issue 2824: [with patch, needs review] sturm_bound incorrect for GammaH

Issue created by migration from https://trac.sagemath.org/ticket/2824

Original creator: craigcitro

Original creation time: 2008-04-06 07:19:22

Assignee: craigcitro

The Sturm bound is being calculated incorrectly for GammaH (we're just returning the bound for Gamma0, which is wrong). This fixes it.

We're actually producing wrong answers, so this is getting listed as critical.


---

Attachment

Very good.


---

Comment by mabshoff created at 2008-04-06 14:16:22

Merged in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-06 14:16:22

Resolution: fixed
