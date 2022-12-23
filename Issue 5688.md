# Issue 5688: update to sympy 0.6.4

Issue created by migration from https://trac.sagemath.org/ticket/5688

Original creator: certik

Original creation time: 2009-04-05 08:13:22

Assignee: burcin

The spkg package is at:

http://sympy.googlecode.com/files/sympy-0.6.4.spkg

All calculus tests run fine, I am now testing the whole sage. When it's done, I'll append the log.


---

Comment by certik created at 2009-04-05 08:20:59

Unfortunately, the tests hung. It may be that they hung on my machine even before uploading the new sympy. I used sage 3.4.1.alpha0.

So this should be investigated.


---

Comment by certik created at 2009-04-05 08:58:47

Ignore the sympy_test.2.log, I don't know how to delete it.


sympy_test.log now contains the testsuite including the timeout failures.


---

Comment by mabshoff created at 2009-04-05 09:07:18

Do not attach logs to trac - copy and paste the failures into a comment. I have deleted both logs.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 04:28:09

Please mark ticket with spkg properly do people are aware that there is something to review. I will do so in the short term and hopefully get this spkg merged.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 04:55:17

Spkg is clean, doctests pass. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 04:55:31

Resolution: fixed


---

Comment by mabshoff created at 2009-04-06 04:55:31

Merged in Sage 3.4.1.rc1.

Cheers,

Michael
