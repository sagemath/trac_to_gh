# Issue 7382: MonskyWashnitzer segfault

Issue created by migration from Trac.

Original creator: jen

Original creation time: 2009-11-03 17:59:21

Assignee: robertwb

CC:  jen minz jpflori

So I don't actually *need* matrix_of_frobenius_hyperelliptic of a curve over an extension field, but I inadvertently passed it in during a computation and caused a segfault. It would be nice for this to work (coercion?), since the curve is defined over QQ anyway.


```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x^3-10*x+9)
sage: K = Qp(3,5)
sage: J.<a> = K.extension(x^30-3)
sage: HJ = H.change_ring(J)
sage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw
sage: M_frob, forms = mw.matrix_of_frobenius_hyperelliptic(HJ)


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```



---

Comment by jdemeyer created at 2014-12-12 11:39:17

Changing component from number theory to algebraic geometry.


---

Comment by edgarcosta created at 2018-04-25 17:49:12

I cannot recreate this error anymore. (most likely it has been fixed indirectly)

Jen, could you double check?

Thanks!


---

Comment by chapoton created at 2018-04-26 09:13:05

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2018-05-01 12:34:39

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates
