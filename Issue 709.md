# Issue 709: Add doctests to ensure that  scipy and cvxopt build correctly on all platforms.

Issue created by migration from https://trac.sagemath.org/ticket/709

Original creator: jkantor

Original creation time: 2007-09-20 17:41:37

Assignee: jkantor

Scipy and cvxopt tend to appear to build correctly, but then raise exceptions when modules are imported (usually missing symbols). We need doctests so that this is detected when tests are run.


---

Attachment

The above patch adds a file that is doctested and tests importing modules from cvxopt and scipy that are known to have problems. This together with the fix for bug 700 should fix the cvxopt problem as well as detect future breakage which is good since cvxopt silently broke when we switched from gfortran to g95.


---

Comment by was created at 2007-09-21 02:12:52

Resolution: fixed


---

Comment by was created at 2007-09-21 02:23:56

Changing status from closed to reopened.


---

Comment by was created at 2007-09-21 02:23:56

I've included this but put a nodoctest in the file until trac #700 is resolved.


---

Comment by was created at 2007-09-21 02:23:56

Resolution changed from fixed to 


---

Comment by was created at 2007-10-20 19:57:23

Resolution: fixed
