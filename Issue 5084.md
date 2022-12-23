# Issue 5084: speed regression in number of partitons

Issue created by migration from https://trac.sagemath.org/ticket/5084

Original creator: robertwb

Original creation time: 2009-01-24 03:07:31

Assignee: tbd

CC:  sage-combinat




---

Comment by robertwb created at 2009-01-24 03:14:38

Changing assignee from tbd to mhansen.


---

Comment by robertwb created at 2009-01-24 03:14:38

Changing component from algebra to combinatorics.


---

Comment by robertwb created at 2009-01-24 03:14:38

This is due to #3762. It might be nice to either (1) detect whether or not quaddouble is available (e.g. if it's on the system or an optional installed spkg) and turn on the macro to use it (2) make the mpfr version faster. Some timings


```
%cython
#clang c++

from sage.libs.mpfr cimport *
from sage.rings.real_rqdf cimport *

def test_mpfr(N, bits=212):
    cdef mpfr_t a, b
    mpfr_init2(a, bits)
    mpfr_init2(b, bits)
    mpfr_random(a)
    mpfr_random(b)
    cdef int i
    for i from 0 <= i < N:
        mpfr_add(a, a, b, GMP_RNDN)
        mpfr_mul(a, a, b, GMP_RNDN)
    mpfr_clear(a)
    mpfr_clear(b)

def test_qd(N):
    cdef double a[4]
    cdef double b[4]
    cdef int i
    c_qd_rand(a)
    c_qd_rand(b)
    for i from 0 <= i < N:
        c_qd_add(a, a, b)
        c_qd_mul(a, a, b)
```


and 


```
sage: time test_mpfr(10^6, 212)
CPU time: 0.34 s,  Wall time: 0.35 s
sage: time test_mpfr(10^6, 150)
CPU time: 0.22 s,  Wall time: 0.23 s
sage: time test_qd(10^6)
CPU time: 0.25 s,  Wall time: 0.26 s
```


(OS X 32-bit)

So there might be hope. Also, the constants calculated up front are used to full (1000s of bits) precision throughout, which can slow things down in some cases.


---

Comment by mabshoff created at 2009-01-24 03:20:34

Quaddouble is fundamentally broken and numerically unstable. With the current settings in the partition_cc code out of the first 500 integers the number of partitions 250 or those are *wrong*, i.e. this problem happens even in the trivial case. There is no way to fix this AFAIK since the correct rounding mode is set on Solaris and any use of quaddouble should be discouraged since it plainly sucks.

Cheers,

Michael


---

Comment by tscrim created at 2013-02-26 15:55:08

Changing status from new to needs_review.


---

Comment by tscrim created at 2013-02-26 15:55:08

I believe this is no longer an issue, however I have nothing to really compare it to.


---

Comment by ncohen created at 2013-03-24 20:35:26

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2013-03-24 20:35:26

4 years ago.... `-_-`

If you want to close it you should set it to positive_review, though.

Nathann


---

Comment by jdemeyer created at 2013-03-29 18:58:05

Resolution: invalid
