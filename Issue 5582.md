# Issue 5582: Coercion from float to QQ is missing

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2009-03-21 20:00:18

Assignee: robertwb

CC:  jbandlow


```
	sage: a = float(1.0)
 	sage: QQ(a)
 	TypeError: Unable to coerce 1.0 (<type 'float'>) to Rational
```

Note that the following works:

```
 	sage: a = float(1.0)
 	sage: QQ(RR(a))
 	1
```


> Yes, this conversion is missing. It should be easy to implement.
> 
> - Robert



---

Attachment


---

Comment by jbandlow created at 2009-03-22 16:04:59

Applies cleanly to my sage 3.4, solves the problem and has a doctest.  Positive review. Thanks very much for this, Robert!


---

Comment by mabshoff created at 2009-03-23 21:01:14

This patch causes the following failure for me:

```
sage -t -long "devel/sage/sage/rings/rational.pyx"          
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/rings/rational.pyx", line 1510:
    sage: float(1.2)**(1/2)
Expected:
    1.0954451150103321
Got:
    sqrt(6)/sqrt(5)
**********************************************************************
```


Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2009-05-19 20:01:40

Looks good to me.  Apply both patches.


---

Comment by mabshoff created at 2009-05-21 01:05:13

These apply with quite some offset, so let's hope for the best:

```
mabshoff`@`sage:/scratch/mabshoff/sage-4.0.rc0/devel/sage$ patch -p1 < trac_5582-float-QQ.patch
patching file sage/rings/rational.pyx
Hunk #1 succeeded at 65 (offset 4 lines).
Hunk #2 succeeded at 298 (offset 135 lines).
Hunk #3 succeeded at 492 (offset 151 lines).
mabshoff`@`sage:/scratch/mabshoff/sage-4.0.rc0/devel/sage$ patch -p1 < trac_5582-QQfloat2.patch 
patching file sage/rings/rational.pyx
Hunk #1 succeeded at 1816 (offset 191 lines).
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-05-21 01:27:33

Merged both patches into Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-21 01:27:33

Resolution: fixed
