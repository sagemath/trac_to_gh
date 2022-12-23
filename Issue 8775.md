# Issue 8775: Bug in conjugate of symbolic ring

Issue created by migration from https://trac.sagemath.org/ticket/8775

Original creator: kcrisman

Original creation time: 2010-04-27 01:02:12

Assignee: burcin

From [http://groups.google.com/group/sage-devel/browse_thread/thread/9f941378a95c0191](http://groups.google.com/group/sage-devel/browse_thread/thread/9f941378a95c0191):

```
sage: a = sqrt(-3) 
sage: a 
sqrt(-3) 
sage: a.conjugate() 
sqrt(-3) 
sage: bool(a==a.conjugate()) 
True 
```

Could this be related to #6244?  Anyway, presumably conjugate should remain unevaluated on this sort of thing, while still being evaluated on things like a+I or 33.


---

Comment by kcrisman created at 2010-04-27 13:46:26

From Burcin Erocal on the same thread:

```
This is a bug in GiNaC: 
ginsh - GiNaC Interactive Shell (ginac V1.5.7) 
  __,  _______  Copyright (C) 1999-2010 Johannes Gutenberg University Mainz, 
 (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY. 
  ._) i N a C | You are welcome to redistribute it under certain conditions. 
<-------------' For details type `warranty;'. 
Type ?? for a list of help topics. 
> sqrt(-3); 
sqrt(-3) 
> conjugate(sqrt(-3)); 

sqrt(-3) 
For conjugation, power objects just compute the conjugate of the basis 
and the exponent, and construct a new power object from these. Here is 
the relevant function: 
http://pynac.sagemath.org/hg/file/3ece9ba22005/ginac/power.cpp#l805 
```

I'm changing this to "not yet reported upstream".


---

Comment by kcrisman created at 2010-04-27 15:06:33

Changing upstream report - too early for feedback at this point.


---

Comment by burcin created at 2010-05-06 03:35:59

add doctests


---

Comment by burcin created at 2010-05-06 04:27:18

Changing keywords from "" to "pynac".


---

Attachment

This is fixed by the new pynac package at #8903. attachment:trac_8775-conjugate.patch contains doctest fixes.

Note that the new pynac version also fixes #8542, #8651, and #8688. Patches from these tickets should be applied before running doctests.


---

Comment by burcin created at 2010-05-06 04:27:18

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-06-10 01:49:46

For some reason, although Sage 4.4.4.alpha0 has pynac-0.2.0.p3

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: N(sqrt(-2),200)
8.0751148893563733350506651837615871941533119425962889089783e-62 + 1.4142135623730950488016887242096980785696718753769480731767*I
sage: conjugate(sqrt(-3))
sqrt(-3)
```

Did this change not end up making it into the Pynac package after all?  According to [http://pynac.sagemath.org/hg/rev/60acd6985820](http://pynac.sagemath.org/hg/rev/60acd6985820), it should be in there, but now I find it hard to explain the above.


---

Comment by kcrisman created at 2010-06-10 01:49:46

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-09-12 16:47:51

Replying to [comment:4 kcrisman]:
> Did this change not end up making it into the Pynac package after all?  According to [http://pynac.sagemath.org/hg/rev/60acd6985820](http://pynac.sagemath.org/hg/rev/60acd6985820), it should be in there, but now I find it hard to explain the above.

That patched was backed out since it caused some problems with doctests in `sage/rings/qqbar.py`.

I merged the upstream patch from GiNaC fixing this problem in the latest version of pynac. I will upload a new patch with doctest fixes later.


---

Comment by burcin created at 2010-09-12 22:13:49

apply only this patch


---

Comment by burcin created at 2010-09-12 22:16:08

Changing status from needs_work to needs_review.


---

Attachment

I uploaded a new patch to add doctests for the fixes in Pynac. Only attachment:trac_8775-conjugate.take2.patch should be applied.

This depends on #9901.


---

Comment by lftabera created at 2010-11-06 11:00:24

The issue seems to be solved. I have tried other examples and it works as expected. The doctest passes.
Positive review


---

Comment by lftabera created at 2010-11-06 11:00:24

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-07 10:38:19

There is a typo in the ticket number in the commit message :-)


---

Comment by jdemeyer created at 2010-11-07 10:38:19

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2010-11-11 13:41:25

Same patch with fixed commit message


---

Comment by jdemeyer created at 2010-11-11 13:42:34

Resolution: fixed


---

Attachment
