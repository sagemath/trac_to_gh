# Issue 7597: segfault in libsingular

archive/issues_007597.json:
```json
{
    "body": "Assignee: malb\n\nCC:  mjo\n\n\n```\nF2 = GF(2)\nF.<x> = GF(2^8)\nR4.<a,b> = PolynomialRing(F)\nR.<u,v> = PolynomialRing(F2);\ndef foo(P, X):\n    return (P(0,0).polynomial()[0])*X\n\ndef bar(X):\n    P = a\n    foo(P,X)\n    return P(a,b)\n\nbar(u)\n```\n\nBOOM!\n\n\n```\nBacktrace from sage 4.1.1, from Mandriva 2010.\n\nProgram received signal SIGSEGV, Segmentation fault.\n0x00007feb8f08ad04 in naNormalize () from /usr/lib64/libsingular.so\nMissing debug package(s), you should install: python-\ndebug-2.6.4-1mdv2010.0.x86_64\n(gdb) bt\n#0 0x00007feb8f08ad04 in naNormalize () from /usr/lib64/libsingular.so\n#1 0x00007feb8f0b5931 in p_Normalize () from /usr/lib64/libsingular.so\n#2 0x00007feb8f4806ed in ?? () from usr/lib64/python2.6/site-packages/\nsage/rings/polynomial/multi_polynomial_libsingular.so\n#3 0x00007feb8f4aa773 in ?? ()\nfrom /usr/lib64/python2.6/site-packages/sage/rings/polynomial/\nmulti_polynomial_libsingular.so\n#4 0x00007feba7829023 in PyObject_Call () from /usr/lib64/\nlibpython2.6.so.1.0\n#5 0x00007feba78ba312 in PyEval_EvalFrameEx () from /usr/lib64/\nlibpython2.6.so.1.0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7597\n\n",
    "created_at": "2009-12-04T04:02:43Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "segfault in libsingular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7597",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/7597





---

archive/issue_comments_064801.json:
```json
{
    "body": "Attachment [sage-trac_7597.patch](tarball://root/attachments/some-uuid/ticket7597/sage-trac_7597.patch) by mjo created at 2012-01-10 14:22:47\n\nDoctest from the test case.",
    "created_at": "2012-01-10T14:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7597#issuecomment-64801",
    "user": "mjo"
}
```

Attachment [sage-trac_7597.patch](tarball://root/attachments/some-uuid/ticket7597/sage-trac_7597.patch) by mjo created at 2012-01-10 14:22:47

Doctest from the test case.



---

archive/issue_comments_064802.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-10T14:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7597#issuecomment-64802",
    "user": "mjo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064803.json:
```json
{
    "body": "If my reproduction as a doctest is faithful, this has been fixed.",
    "created_at": "2012-01-10T14:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7597#issuecomment-64803",
    "user": "mjo"
}
```

If my reproduction as a doctest is faithful, this has been fixed.



---

archive/issue_comments_064804.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40.5\".",
    "created_at": "2012-05-28T23:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7597#issuecomment-64804",
    "user": "mhansen"
}
```

Changing keywords from "" to "sd40.5".



---

archive/issue_comments_064805.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-28T23:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7597#issuecomment-64805",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064806.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2012-05-28T23:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7597#issuecomment-64806",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_064807.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-06-05T06:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7597#issuecomment-64807",
    "user": "jdemeyer"
}
```

Resolution: fixed
