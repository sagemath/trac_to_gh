# Issue 9028: Basic Stats - Standard Deviation

Issue created by migration from https://trac.sagemath.org/ticket/9028

Original creator: amhou

Original creation time: 2010-05-24 06:53:23

Assignee: amhou

Fixes the calculation of standard deviation. 

Previously, sample standard deviation had returned a denominator of n, this fix gives a denominator of n-1. 


---

Attachment


---

Comment by was created at 2010-05-24 07:11:15

Changing status from new to needs_review.


---

Comment by was created at 2010-05-24 07:11:22

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-05-24 20:33:32

Changing status from positive_review to needs_work.


---

Comment by was created at 2010-05-24 20:33:48

Please add a new example to the docstring that illustrates that this bug has been fixed.


---

Comment by benjaminfjones created at 2010-11-18 22:12:06

fix plus an example to test it


---

Attachment

I've attached a new patch witch includes the fix plus an example to test the affected block of code. I couldn't think of a better way to access the block than to define a toy class that has its own mean() function which returns a Python long. If the mean() function from basic_stats.py has to be called, the type of 'x' at line 289 won't ever be 'int' or 'long' so the code block in question is never reached.

Maybe someone can suggest a better example?

Here is a before / after log to show that the fix works and that the example tests it.


```

sage: R = SillyPythonList()
sage: list(R)
[2L, 4L]
sage: len(R)
2
sage: mean(R)
3L
sage: variance(R)
1
sage: variance(R, bias=True)
1

sage: R = [2,4]
sage: mean(R)
3
sage: variance(R)
2
sage: variance(R,bias=True)
1

### LOG (after patch)
sage: R=SillyPythonList()
sage: len(R)
2
sage: mean(R)
3L
sage: variance(R)
2
sage: variance(R, bias=True)
1
sage: R = [2,4]
sage: variance(R)
2
sage: variance(R, bias=True)
1
```



---

Comment by benjaminfjones created at 2010-11-18 22:19:10

Changing status from needs_work to needs_review.


---

Comment by benjaminfjones created at 2010-11-18 22:20:53

Replying to [comment:5 benjaminfjones]:

... and I made sure the doctest passes for the new example. I'm applying the patch to Sage Version 4.6.1.alpha1.


---

Comment by spice created at 2011-03-22 01:14:07

Changing status from needs_review to positive_review.


---

Comment by spice created at 2011-03-22 01:14:07

Changing keywords from "" to "standard deviation".


---

Comment by spice created at 2011-03-22 01:14:07

All good (reviewed trac_9028_stats_fix+example.patch; trac_9028_stats.patch is obsolete).


---

Comment by jdemeyer created at 2011-04-13 07:42:40

Resolution: fixed
