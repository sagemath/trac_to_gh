# Issue 2386: copy and pasting matrices doesn't work

Issue created by migration from https://trac.sagemath.org/ticket/2386

Original creator: jason

Original creation time: 2008-03-04 16:21:12

Assignee: mabshoff

We should be able to somehow get a printout of a matrix that is suitable for pasting into an input cell.

I think that is what repr is supposed to do.  Currently, repr is the same as str, which seems like a bug considering the python convention.


---

Comment by was created at 2008-03-04 17:19:18

> I think that is what repr is supposed to do. Currently,
> repr is the same as str, which seems like a bug considering the python convention.

SAGE blatantly and *systematically* does not follow that Python convention.

I am happy if we implement systematically a method _input_form_  (say -- after Mathematica's well chosen named InputForm) for objects which returns -- if possible (sometimes it isn't!) -- an expression that sage_evals to that object.  

Discuss!


---

Comment by jason created at 2008-03-04 20:46:41

This would be part of #2387.


---

Comment by jason created at 2008-03-04 20:46:41

Resolution: duplicate
