# Issue 3290: Integrate ATLAS 3.8.1 Errate

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-23 20:29:59

Assignee: jkantor

From http://math-atlas.sourceforge.net/errata.html#JITNaN:


```
Complex GEMM sometimes accesses C when BETA=0
This happens when K is much larger than M and N, and is caused by a bug in special-case GEMM code. To fix, edit ATLAS/src/blas/gemm/ATL_cmmJITcp.c, and change lines 267 and 268 from:

   else  /* two or more dim < NB, requires generated cleanup */
      NBmm0 = NBmm1 = NBmmX = Mjoin(PATLU,pKBmm);

to:

   else { NBmm0 = NBmm1 = NBmmX = Mjoin(PATLU,pKBmm);
          if (SCALAR_IS_ZERO(beta)) Mjoin(PATL,gezero)(M, N, C, ldc); }
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-05-23 20:30:11

Changing assignee from jkantor to mabshoff.


---

Comment by mabshoff created at 2008-05-23 20:30:11

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-06-27 00:27:06

This ticket is fixed in the spkg at #3380

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-27 03:24:39

Since #3380 got a positive review by William I am also giving this ticket a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-27 03:24:53

Merged in Sage 3.0.4.alpha1


---

Comment by mabshoff created at 2008-06-27 03:24:53

Resolution: fixed
