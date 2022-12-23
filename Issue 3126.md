# Issue 3126: [with patch, needs review] Cython annotation has unicode errors (e.g. from the notebook)

Issue created by migration from https://trac.sagemath.org/ticket/3126

Original creator: robertwb

Original creation time: 2008-05-07 20:13:51

Assignee: mabshoff

CC:  jason

See for example http://sage.pastebin.com/m408b718c

cython-0.9.6.14.p1.spkg at http://sage.math.washington.edu/home/robertwb/cython/ has a one-line patch to resolve this issue, and is otherwise identical to the previous spkg distributed with 3.0.1. 


---

Comment by jason created at 2008-05-08 19:07:56

Works for me.  Thanks!


---

Comment by mabshoff created at 2008-05-08 21:36:20

Resolution: fixed


---

Comment by mabshoff created at 2008-05-08 21:36:20

Merged in Sage 3.0.2.alpha0
