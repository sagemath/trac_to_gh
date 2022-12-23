# Issue 4558: please update to sympy-0.6.3.spkg

Issue created by migration from https://trac.sagemath.org/ticket/4558

Original creator: certik

Original creation time: 2008-11-20 00:21:33

Assignee: burcin

The spkg is here:

http://sage.math.washington.edu/home/ondrej/spkg/sympy-0.6.3.spkg

and also apply the attached patch, that fixes one failing test in test_sympy.py.

The Sage tests are still running, I'll report if all pass.


---

Attachment

Ok, all tests pass:

http://sage.math.washington.edu/home/ondrej/sympy-0.6.3-sage-tests.log


---

Comment by mabshoff created at 2008-11-23 00:49:42

Ondrej,

in the future make sure to use the sympy.spkg from the tree, not the one you build last time since the one in tree contains various cleanups from the review. Next time you do not use the latest upstream the review on my end will be an automatic "needs work" since I am tired of forward porting fixes I have done over and over again.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-23 00:57:27

Positive review on the spkg and the patch - I have some cleanups in 

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/alpha0/sympy-0.6.3.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-23 00:58:22

Merged in Sage 3.2.1.alpha0


---

Comment by mabshoff created at 2008-11-23 00:58:22

Resolution: fixed
