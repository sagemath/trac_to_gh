# Issue 6076: Allow to redefine the python symbol in the Notebook

Issue created by migration from https://trac.sagemath.org/ticket/6076

Original creator: certik

Original creation time: 2009-05-18 21:20:07

Assignee: boothby

CC:  was mhansen

The problem is that Sage notebook doesn't allow the user to redefine the "python" symbol. 

As a consequence,


```
from sympy import *
```


fails. We can of course fix this particular problem in sympy, but I think this is a bug that should be fixed in the notebook. See this thread for more info:

http://groups.google.com/group/sage-devel/browse_thread/thread/ed5db1f344ed6371/


---

Comment by timdumol created at 2009-11-30 08:49:24

Works for me now. Anyone mind checking if it's a problem, and close otherwise?


---

Comment by certik created at 2009-11-30 08:59:14

Resolution: fixed


---

Comment by certik created at 2009-11-30 08:59:14

I can confirm that this is now fixed on sagenb.org, so this ticket can be closed. Thanks for fixing it!

Ondrej
