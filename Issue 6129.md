# Issue 6129: Ammend docstring in ode.pyx

Issue created by migration from Trac.

Original creator: adavid

Original creation time: 2009-05-26 02:15:06

Assignee: somebody

Keywords: ode docstring


```
# HG changeset patch
# User Anthony David <adavid`@`adavid.com.au>
# Date 1243305447 -36000
# Node ID 894f488ddccd3411fdd0736b455f27e2d8272099
# Parent  958178a11b9e809788f1eda0cc29107c456a1bbe
ammend EXAMPLE comment in sage/gsl/ode.pyx to match doctest function g_1

diff -r 958178a11b9e -r 894f488ddccd sage/gsl/ode.pyx
--- a/sage/gsl/ode.pyx	Mon May 25 00:46:38 2009 +1000
+++ b/sage/gsl/ode.pyx	Tue May 26 12:37:27 2009 +1000
`@``@` -213,7 +213,7 `@``@`
 
          Lets try a system
 
-         y_0'=y_2*y_3
+         y_0'=y_1*y_2
          y_1'=-y_0*y_2
          y_2'=-.51*y_0*y_1
```



---

Comment by mhansen created at 2009-05-28 07:22:01

Looks good to me.


---

Attachment


---

Comment by mhansen created at 2009-05-28 07:31:58

Merged trac_6129.patch in 4.0.rc1.


---

Comment by mhansen created at 2009-05-28 07:31:58

Resolution: fixed
