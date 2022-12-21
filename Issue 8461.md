# Issue 8461: Numerical noise in /sage/sage/plot/colors.py

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-06 22:23:54

Assignee: was

CC:  kcrisman robertwb wcauchois

Running Solaris 10 on a SPARC, I get some numerical noise on this. Since these are RGB values. 


```
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/plot/colors.py", line 660:
    sage: gold / pi + yellow * e
Expected:
    RGB color (0.51829585732141792, 0.49333037605210095, 0.0)
Got:
    RGB color (0.51829585732141814, 0.49333037605210117, 0.0)
**********************************************************************
```


The test makes use of 'e'. As has been shown on various other trac tickets (e.g. #8374, #8375), the value of 'e' returned by the SPARC processor is less accurate then the Intel/ADM chips. 

I'll attach a patch soon. 

Dave 




---

Comment by drkirkby created at 2010-03-06 23:03:08

This can be closed as a duplicate of #8462. It's better to do it this way, rather than close the later ticket, as that has a patch and more information attached. 

dave


---

Comment by mhansen created at 2010-03-06 23:14:41

Resolution: duplicate
