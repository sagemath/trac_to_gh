# Issue 7597: segfault in libsingular

Issue created by migration from https://trac.sagemath.org/ticket/7597

Original creator: was

Original creation time: 2009-12-04 04:02:43

Assignee: malb

CC:  mjo


```
F2 = GF(2)
F.<x> = GF(2^8)
R4.<a,b> = PolynomialRing(F)
R.<u,v> = PolynomialRing(F2);
def foo(P, X):
    return (P(0,0).polynomial()[0])*X

def bar(X):
    P = a
    foo(P,X)
    return P(a,b)

bar(u)
```

BOOM!


```
Backtrace from sage 4.1.1, from Mandriva 2010.

Program received signal SIGSEGV, Segmentation fault.
0x00007feb8f08ad04 in naNormalize () from /usr/lib64/libsingular.so
Missing debug package(s), you should install: python-
debug-2.6.4-1mdv2010.0.x86_64
(gdb) bt
#0 0x00007feb8f08ad04 in naNormalize () from /usr/lib64/libsingular.so
#1 0x00007feb8f0b5931 in p_Normalize () from /usr/lib64/libsingular.so
#2 0x00007feb8f4806ed in ?? () from usr/lib64/python2.6/site-packages/
sage/rings/polynomial/multi_polynomial_libsingular.so
#3 0x00007feb8f4aa773 in ?? ()
from /usr/lib64/python2.6/site-packages/sage/rings/polynomial/
multi_polynomial_libsingular.so
#4 0x00007feba7829023 in PyObject_Call () from /usr/lib64/
libpython2.6.so.1.0
#5 0x00007feba78ba312 in PyEval_EvalFrameEx () from /usr/lib64/
libpython2.6.so.1.0
```



---

Attachment

Doctest from the test case.


---

Comment by mjo created at 2012-01-10 14:24:50

Changing status from new to needs_review.


---

Comment by mjo created at 2012-01-10 14:24:50

If my reproduction as a doctest is faithful, this has been fixed.


---

Comment by mhansen created at 2012-05-28 23:08:35

Changing keywords from "" to "sd40.5".


---

Comment by mhansen created at 2012-05-28 23:08:35

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2012-05-28 23:08:35

Looks good to me.


---

Comment by jdemeyer created at 2012-06-05 06:43:17

Resolution: fixed
