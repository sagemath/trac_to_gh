# Issue 3380: Fix large performance regression in ATLAS 3.8.0 and 3.8.1

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-06-06 23:05:43

Assignee: mabshoff


```
There is a performance bug that causes a fairly large performance drop on
all architectures.  This bug is present in both ATLAS 3.8.0 and 3.8.1.
The explanation and fix is available at:
   http://math-atlas.sourceforge.net/errata.html#JITcpBug

Regards,
Clint
```



---

Comment by mabshoff created at 2008-06-06 23:05:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-06-06 23:07:41

The errata says specifically:

```
Bad GEMM call causes performance drop for all architectures
A piece of duplicated code causes a special-case code to be used 
for all GEMM problems, which reduces performance on all architectures 
and almost all problems. To fix, comment out (or delete) lines 191-194 
of ATLAS/src/blas/gemm/ATL_gemmXX.c, which read:

         {
            mm2 = mm1;
            mm1 = Mjoin(PATL,mmJITcp);
         }

(notice these 4 lines are a duplicate of the for lines above. 
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-06-27 00:28:33

The new spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha1/atlas-3.8.1.p2.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-27 03:24:04

Merged in Sage 3.0.4.alpha1


---

Comment by mabshoff created at 2008-06-27 03:24:04

Resolution: fixed
