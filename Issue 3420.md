# Issue 3420: Failure in markov_multifractal (random?)

Issue created by migration from https://trac.sagemath.org/ticket/3420

Original creator: jsp

Original creation time: 2008-06-13 18:55:59

Assignee: was

On Fedora 9:


```
sage -t  devel/sage/sage/finance/markov_multifractal.py     **********************************************************************
File "/home/jaap/downloads/sage-3.0.3.alpha2/tmp/markov_multifractal.py", line 56:
    sage: msm.__cmp__(3)
Expected:
    -1
Got:
    1
**********************************************************************
1 items had failures:

```




---

Comment by mabshoff created at 2008-06-13 22:45:07

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-06-13 22:45:07

Changing assignee from was to mabshoff.


---

Comment by was created at 2008-06-13 22:47:03

positive review


---

Comment by mabshoff created at 2008-06-15 19:05:07

Merged in Sage 3.0.3.rc0


---

Comment by mabshoff created at 2008-06-15 19:05:07

Resolution: fixed
