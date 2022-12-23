# Issue 6719: Doctest failure with elliptic_eu (incomplete elliptic integral of the second kind) on Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/6719

Original creator: drkirkby

Original creation time: 2009-08-09 20:28:46

Assignee: tbd

This is a report of a test failure of elliptic_eu (0.5, 0.1), seen on Sage sage-4.1.1.rc0 with updated Maxima (5.19.0) and ecl (9.8.1)

I don't understand the maths of this, and don't even know how to independently verify this. But I'm just reporting it as a test failure. I don't even know if this should be 'algebra'. Please someone set the 'Component' to something else if this is inappropriate. 

File "/export/home/drkirkby/sage/sage-4.1.1.rc0/devel/sage/sage/functions/special.py", line 1259:
    sage: elliptic_eu (0.5, 0.1)
Expected:
    0.496054551287
Got:
    0.495848403419




---

Attachment

Patch produced from a modified file in CVS, retrived on August 10th 2009


---

Comment by drkirkby created at 2009-08-11 07:05:02

Juan Jose Garcia-Ripoll (Juanjo), the main developer of ECL has discovered a bug in ECL 9.8.1. On his advice, I took the CVS on August 10th 2009  and have updated just the one file. 

```
ecl-9.8.1/src/cmp/sysfun.lsp
```


This fixes the problem. 


As far as I am concerned, this, and trac #6716 (which effected elliptic_e) can now be closed. Doctest


```
sage -t  "devel/sage/sage/functions/special.py"
```


now passes. 

I will produce a revised ecl .spkg file, as per trac #6564


---

Comment by mvngu created at 2009-08-11 08:03:43

Closed as suggested by David Kirkby at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e4f409a99e668867) thread.


---

Comment by mvngu created at 2009-08-11 08:03:43

Resolution: invalid
