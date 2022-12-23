# Issue 2680: Modular forms for Gamma1(N) have wrong Sturm bound

Issue created by migration from https://trac.sagemath.org/ticket/2680

Original creator: craigcitro

Original creation time: 2008-03-26 23:00:25

Assignee: craigcitro

There are several issues with modular forms for Gamma1. In particular, this breaks:


```
sage: ModularForms(Gamma1(22))._q_expansion_module()
```


It's happening because the Sturm bound is getting calculated incorrectly (if you look at the code, it just looks at the level and takes the index of Gamma0 for that level, which is clearly wrong). This is probably an easy fix, but I don't want to do this hastily and make a mistake, so I'll look at it next week.

I don't think we're going to produce any wrong answers right now -- I think there are just several places where we'll throw errors instead of producing answers.


---

Comment by craigcitro created at 2008-03-26 23:01:06

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-04-06 06:27:51

Patch attached. The fix was what I described above, but apparently I was pessimistic about this breaking things -- I tried a handful of examples, and nothing seems broken. It also passes all doctests. If someone can find something I missed, let me know.


---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-04-06 07:13:58

Resolution: fixed


---

Comment by mabshoff created at 2008-04-06 07:13:58

Merged in Sage 3.0.alpha2
