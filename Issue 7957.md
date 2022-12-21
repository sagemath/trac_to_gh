# Issue 7957: problems with real_part function

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-01-16 18:49:00

Assignee: burcin

CC:  rossk

From the sage-devel thread:

http://groups.google.com/group/sage-devel/t/56519182d53e9cf8


```
On Tue, 5 Jan 2010 04:35:27 -0800 (PST)
Håkan Granath <hakan.granath`@`googlemail.com> wrote:

> Hi,
> 
> It seems computations in QQbar is sometimes much slower in Sage
> 4.3 than in the previous version. Here is an example (I am sorry
> if it is too convoluted):
> 
> v1 = sqrt(QQbar(3))
> v2 = QQbar(999/1000*I)
> v3 = (1 + v1)/2 + v2*(-3 - v1)/2
> v4 = (3 - v1)/2 + v2*(1 - v1)/2
> v5 = v3*(1/2) + v4*QQbar(500/999*I)
> v6 = v3*(1/2) + v4*QQbar(-500/999*I)
> v7 = -(v5/v6).conjugate() - QQbar(abs(v5))/v5/v6.conjugate()*QQbar(I)
> v8 = -(v5/v6).conjugate() + QQbar(abs(v5))/v5/v6.conjugate()*QQbar(I)
> v9 = abs(v8)
> v10 = abs(v7)
> v11 = (v7 - v8 + QQbar(v9*v9)*v7 - QQbar(v10*v10)*v8)/\
>       (v8.conjugate()*v7 - v7.conjugate()*v8)
> v12 = (v11*QQbar(I) - QQbar(-I)*v11.conjugate())/2/QQbar(I)
> v13 = abs(v12)
> v14 = QQbar(1 - sqrt(1 - 1/(v13*v13)))*v12
> time real(v14)
> 
> In Sage 4.3 I get the output:
> 
> Exception TypeError: TypeError('Unable to convert number to real
> interval.',) in 'sage.symbolic.pynac.py_is_real' ignored
> CPU times: user 67.94 s, sys: 0.30 s, total: 68.23 s
> Wall time: 68.68 s
> -0.5773508481209188?
> 
> In Sage 4.2.1 on the same computer I get the output:
> 
> CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
> Wall time: 0.00 s
> -0.5773508481209188?
```


This is fallout from #7490. See also #7916 for problems with `conjugate()`.


---

Attachment

add exception handling to sage/symbolic/pynac.pyx


---

Comment by burcin created at 2010-01-17 09:54:16

attachment:trac_7957-pynac_exceptions.patch adds exception handling to sage/symbolic/pynac.pyx to eliminate the "error ignored" message.

With a simple change in the pynac `numeric::real()` code, new timings are:

Before:


```
sage: %time real(v14)
CPU times: user 30.19 s, sys: 0.42 s, total: 30.61 s
Wall time: 30.96 s
-0.5773508481209188?
```


After:


```
sage: %time real(v14)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
-0.5773508481209188?
```


I'll make a new pynac package including this change available soon.


---

Comment by burcin created at 2010-01-17 09:54:16

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-01-18 02:14:15

Does [trac_7957-pynac_exceptions.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7957/trac_7957-pynac_exceptions.patch) depend on anything? I'm getting 3 hunk failures when applying this to Sage 4.3.1.rc0:

```
[mvngu`@`mod sage-main]$ pwd
/dev/shm/mvngu/sage-4.3.1.rc0-7957/devel/sage-main
[mvngu`@`mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7957/trac_7957-pynac_exceptions.patch
adding trac_7957-pynac_exceptions.patch to series file
[mvngu`@`mod sage-main]$ hg qpush
applying trac_7957-pynac_exceptions.patch
patching file sage/symbolic/pynac.pyx
Hunk #31 succeeded at 1538 with fuzz 2 (offset -33 lines).
Hunk #32 FAILED at 1603
Hunk #33 FAILED at 1637
Hunk #34 FAILED at 1668
3 out of 38 hunks FAILED -- saving rejects to file sage/symbolic/pynac.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7957-pynac_exceptions.patch
[mvngu`@`mod sage-main]$ cat sage/symbolic/pynac.pyx.rej
--- pynac.pyx
+++ pynac.pyx
`@``@` -1603,7 +1604,7 `@``@`
     """
     return py_li(x, n, parent)
 
-cdef public object py_psi(object x):
+cdef public object py_psi(object x) except +:
     """
     EXAMPLES::
 
`@``@` -1637,7 +1638,7 `@``@`
     """
     return py_psi(x)
 
-cdef public object py_psi2(object n, object x):
+cdef public object py_psi2(object n, object x) except +:
     """
     EXAMPLES::
 
`@``@` -1668,14 +1669,14 `@``@`
 ##################################################################
 # Not yet implemented
 ##################################################################
-cdef public object py_li2(object x):
+cdef public object py_li2(object x) except +:
     raise NotImplementedError
 
 ##################################################################
 # Constants
 ##################################################################
 
-cdef public GConstant py_get_constant(char* name):
+cdef public GConstant py_get_constant(char* name) except +:
     """
     Returns a constant given its name. This is called by
     constant::unarchive in constant.cpp in Pynac and is used for
```



---

Comment by burcin created at 2010-01-18 04:20:22

Sorry for the inconvenience. My patch queue contains all the fixes from yesterday. I forgot to check dependencies.

This depends on #6961. You can apply the patch there without waiting for the new pynac spkg. Only the `loads(dumps())` test with `psi2`, should fail.


---

Comment by kcrisman created at 2010-01-28 21:20:06

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-01-28 21:20:06

Fixes the error, and makes the same change throughout.  Positive review.


---

Comment by mvngu created at 2010-02-18 21:44:50

Resolution: fixed
