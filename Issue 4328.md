# Issue 4328: bug in roots

archive/issues_004328.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.4, Release Date: 2008-10-16                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: R=PolynomialRing(ZZ, x)\nsage: f=R(x^4+1)\nsage: f.roots(GF(2))\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n...\nValueError: factorization of 0 not defined\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4328\n\n",
    "created_at": "2008-10-20T11:39:21Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "bug in roots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4328",
    "user": "zimmerma"
}
```
Assignee: somebody


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: R=PolynomialRing(ZZ, x)
sage: f=R(x^4+1)
sage: f.roots(GF(2))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: factorization of 0 not defined
```


Issue created by migration from https://trac.sagemath.org/ticket/4328





---

archive/issue_comments_031747.json:
```json
{
    "body": "I should have said it works with vanilla 3.1.4, thus it is most likely related to the recent patches for\nGF(2)[x] I have applied to my 3.1.4 version.",
    "created_at": "2008-10-20T11:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4328#issuecomment-31747",
    "user": "zimmerma"
}
```

I should have said it works with vanilla 3.1.4, thus it is most likely related to the recent patches for
GF(2)[x] I have applied to my 3.1.4 version.



---

archive/issue_comments_031748.json:
```json
{
    "body": "It works with my current 3.2.alpha0 merge tree:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.4, Release Date: 2008-10-16                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: R=PolynomialRing(ZZ, x)\nsage: sage: f=R(x^4+1)\nsage: sage: f.roots(GF(2))\n[(1, 4)]\n```\n\nI suspect the root cause could be #4302.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-20T12:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4328#issuecomment-31748",
    "user": "mabshoff"
}
```

It works with my current 3.2.alpha0 merge tree:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: R=PolynomialRing(ZZ, x)
sage: sage: f=R(x^4+1)
sage: sage: f.roots(GF(2))
[(1, 4)]
```

I suspect the root cause could be #4302.

Cheers,

Michael



---

archive/issue_comments_031749.json:
```json
{
    "body": "worksforme:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: test\nsage: R=PolynomialRing(ZZ, x)\nsage: f=R(x^4+1)\nsage: f.roots(GF(2))\n[(1, 4)]\n| SAGE Version 3.1.3, Release Date: 2008-10-14                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: P.<x> = PolynomialRing(GF(2))\nsage: type(x) # check whether the patch is applied\n<type 'sage.rings.polynomial.polynomial_gf2x.Polynomial_GF2X'>\n```\n\n\nNote that I updates #4302 recently.",
    "created_at": "2008-10-20T13:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4328#issuecomment-31749",
    "user": "malb"
}
```

worksforme:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: test
sage: R=PolynomialRing(ZZ, x)
sage: f=R(x^4+1)
sage: f.roots(GF(2))
[(1, 4)]
| SAGE Version 3.1.3, Release Date: 2008-10-14                       |
| Type notebook() for the GUI, and license() for information.        |
sage: P.<x> = PolynomialRing(GF(2))
sage: type(x) # check whether the patch is applied
<type 'sage.rings.polynomial.polynomial_gf2x.Polynomial_GF2X'>
```


Note that I updates #4302 recently.



---

archive/issue_comments_031750.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2008-10-20T13:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4328#issuecomment-31750",
    "user": "malb"
}
```

Resolution: worksforme
