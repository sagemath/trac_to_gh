# Issue 9172: cygwin: numerical noise in sage/rings/integer.pyx

Issue created by migration from https://trac.sagemath.org/ticket/9172

Original creator: was

Original creation time: 2010-06-07 04:52:04

Assignee: tbd

CC:  jpflori


```

sage -t  "devel/sage/sage/rings/integer.pyx"                
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/rings/integer.pyx", line 1681:
    sage: 2^float(1.5)       # python float
Expected:
    2.8284271247461903
Got:
    2.8284271247461898
**********************************************************************
1 items had failures:
   1 of  26 in __main__.example_42
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_integer.py
	 [15.2 s]
```



---

Comment by drkirkby created at 2011-02-09 17:12:20

The correct answer is 2*sqrt(2), which is `2.8284271247461900976033774484193961...`  

So the expected value is `2.0239x10`<sup>-16</sup> high, and result on Cygwin is 2.9760x10<sup>-16</sup> low. So the errors on Linux/OSX/Solaris is not much lower than on Cygwin. We can't really expect any more from a floating point number. 

We could change the Expected value to `2.8284271247461...` What I don't like about that, is then much larger errors can exist and them not be detected. But this is far from the only such case, so I suggest just changing the test to `2.8284271247461...`, which will solve this. 

Dave


---

Comment by kcrisman created at 2011-08-02 02:26:51

This file passed doctests on a build of mine on XP.


---

Comment by kcrisman created at 2011-08-19 14:46:24

But when doing the test by hand, the same thing happens.


---

Comment by kcrisman created at 2013-01-15 15:40:19

Changing priority from major to minor.


---

Comment by kcrisman created at 2013-01-15 15:40:19

This now fails with

```
2.82842712474619
```

which I suppose is an improvement.  Maybe we can use `abs tol`?


---

Comment by jpflori created at 2013-01-15 18:06:30

And the test passes for me (64bits W7 + 5.6.rc0).


---

Comment by kcrisman created at 2013-01-15 18:10:43

> And the test passes for me (64bits W7 + 5.6.rc0).
In which case it might just be a 32-bit versus 64-bit issue.  Did you try it by hand as well?


---

Comment by dimpase created at 2013-01-27 10:04:02

Changing status from new to needs_review.


---

Comment by dimpase created at 2013-01-27 10:04:02

Replying to [comment:6 kcrisman]:
> > And the test passes for me (64bits W7 + 5.6.rc0).
> In which case it might just be a 32-bit versus 64-bit issue.  Did you try it by hand as well?

works for me, both ways. I think we can close this one.


---

Comment by kcrisman created at 2013-01-28 02:10:45

Hmm, I'm reluctant to not just change this a bit for 32-bit...


---

Comment by jpflori created at 2013-01-30 10:45:26

Yeah, I think we should make sure this passes on 32 bits.
I'll double check when I have the time to build on such a computer.


---

Comment by jpflori created at 2013-01-30 10:45:39

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2013-02-08 12:44:19

Changing status from needs_work to positive_review.


---

Comment by jpflori created at 2013-02-08 12:44:19

I have no problems on my 32 bits Windows 7 install, so Cygwin must have gotten better.
I really doubt Cygwin on XP would have a different behavior for this one, so let's close it.


---

Comment by jdemeyer created at 2013-02-08 13:20:49

Resolution: worksforme
