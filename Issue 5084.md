# Issue 5084: speed regression in number of partitons

archive/issues_005084.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  sage-combinat\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5084\n\n",
    "created_at": "2009-01-24T03:07:31Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "speed regression in number of partitons",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5084",
    "user": "@robertwb"
}
```
Assignee: tbd

CC:  sage-combinat



Issue created by migration from https://trac.sagemath.org/ticket/5084





---

archive/issue_comments_038746.json:
```json
{
    "body": "Changing assignee from tbd to @mwhansen.",
    "created_at": "2009-01-24T03:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5084#issuecomment-38746",
    "user": "@robertwb"
}
```

Changing assignee from tbd to @mwhansen.



---

archive/issue_comments_038747.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2009-01-24T03:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5084#issuecomment-38747",
    "user": "@robertwb"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_038748.json:
```json
{
    "body": "This is due to #3762. It might be nice to either (1) detect whether or not quaddouble is available (e.g. if it's on the system or an optional installed spkg) and turn on the macro to use it (2) make the mpfr version faster. Some timings\n\n\n```\n%cython\n#clang c++\n\nfrom sage.libs.mpfr cimport *\nfrom sage.rings.real_rqdf cimport *\n\ndef test_mpfr(N, bits=212):\n    cdef mpfr_t a, b\n    mpfr_init2(a, bits)\n    mpfr_init2(b, bits)\n    mpfr_random(a)\n    mpfr_random(b)\n    cdef int i\n    for i from 0 <= i < N:\n        mpfr_add(a, a, b, GMP_RNDN)\n        mpfr_mul(a, a, b, GMP_RNDN)\n    mpfr_clear(a)\n    mpfr_clear(b)\n\ndef test_qd(N):\n    cdef double a[4]\n    cdef double b[4]\n    cdef int i\n    c_qd_rand(a)\n    c_qd_rand(b)\n    for i from 0 <= i < N:\n        c_qd_add(a, a, b)\n        c_qd_mul(a, a, b)\n```\n\n\nand \n\n\n```\nsage: time test_mpfr(10^6, 212)\nCPU time: 0.34 s,  Wall time: 0.35 s\nsage: time test_mpfr(10^6, 150)\nCPU time: 0.22 s,  Wall time: 0.23 s\nsage: time test_qd(10^6)\nCPU time: 0.25 s,  Wall time: 0.26 s\n```\n\n\n(OS X 32-bit)\n\nSo there might be hope. Also, the constants calculated up front are used to full (1000s of bits) precision throughout, which can slow things down in some cases.",
    "created_at": "2009-01-24T03:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5084#issuecomment-38748",
    "user": "@robertwb"
}
```

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

archive/issue_comments_038749.json:
```json
{
    "body": "Quaddouble is fundamentally broken and numerically unstable. With the current settings in the partition_cc code out of the first 500 integers the number of partitions 250 or those are *wrong*, i.e. this problem happens even in the trivial case. There is no way to fix this AFAIK since the correct rounding mode is set on Solaris and any use of quaddouble should be discouraged since it plainly sucks.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T03:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5084#issuecomment-38749",
    "user": "mabshoff"
}
```

Quaddouble is fundamentally broken and numerically unstable. With the current settings in the partition_cc code out of the first 500 integers the number of partitions 250 or those are *wrong*, i.e. this problem happens even in the trivial case. There is no way to fix this AFAIK since the correct rounding mode is set on Solaris and any use of quaddouble should be discouraged since it plainly sucks.

Cheers,

Michael



---

archive/issue_comments_038750.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-26T15:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5084#issuecomment-38750",
    "user": "@tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_038751.json:
```json
{
    "body": "I believe this is no longer an issue, however I have nothing to really compare it to.",
    "created_at": "2013-02-26T15:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5084#issuecomment-38751",
    "user": "@tscrim"
}
```

I believe this is no longer an issue, however I have nothing to really compare it to.



---

archive/issue_comments_038752.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-24T20:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5084#issuecomment-38752",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_038753.json:
```json
{
    "body": "4 years ago.... `-_-`\n\nIf you want to close it you should set it to positive_review, though.\n\nNathann",
    "created_at": "2013-03-24T20:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5084#issuecomment-38753",
    "user": "@nathanncohen"
}
```

4 years ago.... `-_-`

If you want to close it you should set it to positive_review, though.

Nathann



---

archive/issue_comments_038754.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-03-29T18:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5084#issuecomment-38754",
    "user": "@jdemeyer"
}
```

Resolution: invalid
