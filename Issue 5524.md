# Issue 5524: attrcall missing __cmp__

Issue created by migration from https://trac.sagemath.org/ticket/5524

Original creator: nthiery

Original creation time: 2009-03-15 05:03:19

Assignee: cwitty

CC:  sage-combinat jbandlow

sage: f = attrcall("bla")
sage: dumps(f)
sage: loads(dumps(f)) == f
False

This is because AttrCallObject doesn't have a __cmp__ method:


---

Comment by nthiery created at 2010-01-26 21:29:54

Changing keywords from "" to "attrcall, pickling".


---

Comment by nthiery created at 2010-01-26 21:29:54

Changing status from new to needs_review.


---

Attachment


---

Comment by nthiery created at 2010-01-26 21:30:50

Changing assignee from cwitty to nthiery.


---

Comment by jbandlow created at 2010-01-26 21:41:00

I'm getting a failing doctest:

```
sage -t  "devel/sage-trac/sage/misc/misc.py"                
**********************************************************************
File "/usr/local/src/sage/devel/sage-trac/sage/misc/misc.py", line 2103:
    sage: TestSuite(f).run()
Exception raised:
...
AttributeError: 'AttrCallObject' object has no attribute '_tester'
```


I'm applying on top of 4.3.1 plus #7976, #7921, #7938, #8028.  Am I missing something?


---

Comment by jbandlow created at 2010-01-26 21:41:00

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2010-01-26 21:46:57

Replying to [comment:4 jbandlow]:
> I'm getting a failing doctest:
> I'm applying on top of 4.3.1 plus #7976, #7921, #7938, #8028.  Am I missing something?

I should have mentioned it depends on #8001.


---

Comment by nthiery created at 2010-01-26 21:46:57

Changing status from needs_work to needs_review.


---

Comment by jbandlow created at 2010-01-26 21:56:11

Changing status from needs_review to positive_review.


---

Comment by jbandlow created at 2010-01-26 21:56:11

Thanks.  That fixes it.  Passes tests and looks good to me.


---

Comment by mvngu created at 2010-01-30 23:45:49

Resolution: fixed
