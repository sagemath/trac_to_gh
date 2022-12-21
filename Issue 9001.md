# Issue 9001: optional package database_cremona_ellcurve-20071019.p0.spkg causes test failure

Issue created by migration from Trac.

Original creator: mariah

Original creation time: 2010-05-20 20:37:26

Assignee: tbd


```
sage-4.4.2 with the optional package database_cremona_ellcurve-20071019.p0.spkg has the following test failure:


taurus% ./sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_point.py"
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_point.py"
**********************************************************************
File "/home/mariah/sage/sage-4.4.2-x86_64-Linux-nehalem-fc-test2/devel/sage/sage/schemes/elliptic_curves/ell_point.py", line 1729:
    sage: Q = E.isomorphism_to(ED.change_ring(K))(P); Q
Expected:
    (0 : -7/2*a - 1/2 : 1)
Got:
    (0 : 7/2*a - 1/2 : 1)
**********************************************************************
1 items had failures:
   1 of  67 in __main__.example_36
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mariah/.sage//tmp/.doctest_ell_point.py
         [32.7 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_point.py"
```



---

Attachment


---

Comment by cremona created at 2010-06-04 08:54:12

Changing status from new to needs_review.


---

Comment by cremona created at 2010-06-04 08:54:12

Dammit, I thought we had got rid of all of these,  If the ticket had been tagged as being in Elliptic Curves, I would have noticed this and fixed it 2 weeks ago, sorry.

Patch applies fine to 4.4.3.alpha3.  With no optional packages installed I tested the whole sage library (only 10 minutes with -tp 10!), and did it again after installing database_cremona_ellcurve-20071019.  Just to make sure there were not other examples of this lurking!  All pass.


---

Comment by cremona created at 2010-06-04 08:54:18

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-06-04 15:30:10

Resolution: fixed
