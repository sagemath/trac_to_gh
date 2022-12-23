# Issue 8460: doctest failure sagenb-0.7.5.1-py2.6.egg/sagenb/misc/sageinspect.py

Issue created by migration from https://trac.sagemath.org/ticket/8460

Original creator: drkirkby

Original creation time: 2010-03-06 22:13:05

Assignee: was

I get this failure on Solaris 10, on SPARC using a modified version of the 4.3.4.alpha0 sources. (All modifications were necessary to get Sage to build). 


```
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/misc/sageinspect.py", line 562:
    sage: sage_getsourcelines(matrix, True)[1]
Expected:
    33
Got:
    34
**********************************************************************
```



I'm guessing a bit about the category for his. I'll this if I have chosen the wrong category. 


---

Comment by mpatel created at 2010-03-09 06:41:20

This happens to be part of #8430 and the fix from #8324 is part of #8435.


---

Comment by mpatel created at 2010-03-09 06:41:20

Resolution: fixed
