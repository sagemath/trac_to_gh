# Issue 5955: Sage 3.4.2.rc0: Set stacksize for clisp.spkg to 32kb

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-05-01 06:39:31

Assignee: mabshoff

Various boxen have too little stacksapce, i.e. FC 10 and RHEL 10 for example use 10k. This makes clisp blow up during the build, so raise the limit to 32k on linux in general.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-01 06:39:49

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-05-04 05:16:45

The spkg at 

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/final/clisp-2.47.p1.spkg

fixes the problem.

Cheers,

Michael


---

Comment by roed created at 2009-05-04 09:08:05

I installed the spkg, rebuilt maxima.  Sage starts fine, and maxima works.


---

Comment by mabshoff created at 2009-05-04 09:16:02

Merged in sage 3.4.2.final.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-04 09:16:02

Resolution: fixed
