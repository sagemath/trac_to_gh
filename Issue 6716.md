# Issue 6716: elliptic_e(0.5, 0.1) test failure on Solaris SPARC (error about 0.04%)

Issue created by migration from https://trac.sagemath.org/ticket/6716

Original creator: drkirkby

Original creation time: 2009-08-09 17:38:16

Assignee: tbd

Here's a failure observed on a sun4u machine with Sage Version 4.1.1.rc0, Release Date: 2009-07-29, but with updates to some packages including ECL 9.8.1 (#6564) and Maxima 5.19.1



```
sage -t  "devel/sage/sage/functions/special.py"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1.rc0/devel/sage/sage/functions/special.py", line 1208:
    sage: elliptic_e(0.5, 0.1)
Expected:
    0.498011394499
Got:
    0.497801100392
**********************************************************************

```



The result is similar to that expected, but not identical. I tried this in Mathematica 7.0 too, but using 1/2 instead of 0.5, and 1/10 instead of 0.1. Then asked for the result with 50 digits of precision. 


```

In[4]:= N[EllipticE[1/2,1/10],50]

Out[4]= 0.49801139449883153311546104061744810584963105068054
```



I know it would be unwise to trust Mathematica fully, but the Mathematica result does agree much more closely with what the doctest is expecting than it does the answer on Solaris. The difference between the answer from Mathematica and that from Sage on Solaris is -0.000210294 or around 0.04%. 




---

Comment by drkirkby created at 2009-08-10 07:12:19

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2009-08-10 07:12:19

Just to add a few more comments.

 * The issue is also seen with elliptic_eu (#6716), where 0.496054551287 was expected, but 0.495848403419 was returned. 
 * While both elliptic_e(0.5,0.1) and elliptic_eu(0.5,0.1) both return numbers close to 0.5, the expected values are *not* the same. 
 * Others using x86 hardware on both linux and Windows are not seeing this issue with either elliptic_eu or elliptic_e. 
 * This is not a newish sun4v machine, but an older sun4u machine. So libraries are probably better debugged. (An issue recently with the memset function call is only seen on the newer hardware due to a bug in the Solaris library). 
 * If one makes no attempt in Mathematica to use extended precision, the results are still the same, though returned with less digits of course. This rather suggests this is not a broken library on Solaris, as otherwise Mathematica would probably get the result incorrect too when it uses the library. Of course, with black-box closed source software, one never really knows what's going on inside).


```
In[1]:= EllipticE[0.5,0.1]
Out[1]= 0.498011
```



Dave


---

Comment by drkirkby created at 2009-08-10 07:14:42

I'm changing the component from 'algebra' to 'solaris', as this seems to be specific to Solaris.


---

Comment by drkirkby created at 2009-08-10 07:14:42

Changing component from algebra to solaris.


---

Comment by drkirkby created at 2009-08-11 07:11:26

Juanjo, the main developer of ECL has discovered a bug in ECL 9.8.1, which was effecting both elliptic_e and elliptic_eu. A patch, which corrects both this and #6719 can be found on #6719 


As far as I am concerned, this, and trac #6719 (which effected elliptic_eu) can now be closed. Doctest


```
sage -t  "devel/sage/sage/functions/special.py"
```


now passes. 

I will produce a revised ecl .spkg file, as per trac #6564


---

Comment by drkirkby created at 2009-08-11 07:11:26

Changing component from solaris to algebra.


---

Comment by mvngu created at 2009-08-11 08:02:18

Closed as suggested by David Kirkby at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e4f409a99e668867) thread.


---

Comment by mvngu created at 2009-08-11 08:02:18

Resolution: invalid
