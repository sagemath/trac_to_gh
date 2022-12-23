# Issue 1421: [with patch] finer control in ECM interface

Issue created by migration from https://trac.sagemath.org/ticket/1421

Original creator: zimmerma

Original creation time: 2007-12-07 19:34:29

Assignee: was

I have added a new method "one_curve" (maybe a better name can be found) to run exactly one
curve (either ECM or P-1 or P+1). Also added examples for find_factor() method.


---

Attachment


---

Comment by was created at 2007-12-15 10:18:37

code looks good -- if it passes tests, put it in.


---

Comment by craigcitro created at 2007-12-18 01:45:18

Fixed one line in the original patch -- it creates a string to return as the error message, and then accidentally returns something other than that string (which I'm assuming wasn't the intended behavior).


---

Attachment


---

Comment by rlm created at 2007-12-18 02:12:38

Resolution: fixed


---

Comment by rlm created at 2007-12-18 02:12:38

Merged in 2.9.1.alpha1
