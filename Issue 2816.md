# Issue 2816: unify eigen* functions for different matrix classes

Issue created by migration from https://trac.sagemath.org/ticket/2816

Original creator: jason

Original creation time: 2008-04-05 22:17:44

Assignee: was

See the conclusions from the discussion: 

http://groups.google.com/group/sage-devel/browse_thread/thread/c8d2001f2b19a9bc#


---

Attachment


---

Comment by jason created at 2008-07-19 18:49:04

The documentation isn't all there, but you can see the functions.


---

Comment by jason created at 2008-07-19 18:49:44

This depends on #3654


---

Comment by jason created at 2008-07-19 18:52:09

See http://groups.google.com/group/sage-devel/browse_thread/thread/3ef6da9c8fa7db36 for "documentation" on the functions.


---

Comment by wdj created at 2008-07-20 02:39:28

I know this is preliminary but just wanted to report for others testers that this has a boat-load of doctest failures:


```
...
        sage -t  devel/sage/sage/calculus/wester.py
        sage -t  devel/sage/sage/matrix/matrix2.pyx
        sage -t  devel/sage/sage/matrix/tests.py
        sage -t  devel/sage/sage/modular/modform/half_integral.py
        sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx
        sage -t  devel/sage/sage/misc/functional.py
```

I ran testall twice and it seems that I did not pick up the failure of sage -t  devel/sage/sage/calculus/wester.py or of devel/sage/sage/modular/modform/half_integral.py the first time. These aside, looks like it will eventually be a valuable contribution to SAGE.


---

Comment by jason created at 2008-07-20 03:32:01

Thanks for running testall.  Some doctests are fixed in the current patch; I'll fix the other doctests in an updated patch.


---

Comment by jason created at 2009-01-22 01:52:20

This is part of the linear algebra SEP: http://wiki.sagemath.org/LinearAlgebraSEP


---

Comment by mabshoff created at 2009-04-18 22:37:55

What is going on here?

Cheers,

Michael


---

Comment by jason created at 2009-04-19 00:00:24

Well, it probably needs massive rebasing because of the rest transition, for one.  It's on my back burner; I'll probably get to it before June, since I'm teaching linear algebra for the first part of the summer.  However, if someone else is interested in working on this, don't hesitate to post a message here and start working!
