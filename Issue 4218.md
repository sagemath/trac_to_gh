# Issue 4218: Extensions of Finite Fields don't work well

archive/issues_004218.json:
```json
{
    "body": "Assignee: tbd\n\nThe following sage snippets show (some of) the problems.  First, we set\nthe stage:\n\n```\nsage: F1.<a> = GF(2^7)\nsage: P1.<x>=PolynomialRing(F1)\nsage: f=x^2+x+F1(1)\nsage: F2=F1.extension(f,'u')\nsage: F2\nUnivariate Quotient Polynomial Ring in u over Finite Field in a of size 2^7 with modulus u^2 + u + 1\nsage: a in F2\nTrue\n```\n\n\nFirst problem:\n\n```\nsage: for i in xrange(100):\n   ....:         r = F2.random_element()\n   ....:     if r != F2(0) and r != F2(1):\n   ....:             print \"Yoicks! r=%s\"%r\n   ....: \nsage: \n```\n\nNo output means that 100 random elements of F2 are either\n0 or 1, which seems somehow incorrect.\n\nThe next oddity is\n\n```\nsage: F1.order()\n128\nsage: F2.order()\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/SandBox/Justin/sb/sage-3.1.1/<ipython console> in <module>()\n\n/SandBox/Justin/sb/sage-3.1.1/ring.pyx in sage.rings.ring.Ring.order (sage/rings/ring.c:4108)()\n\nNotImplementedError: \n```\n\nShouldn't .order() work for extensions as well as those directly defined?\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4218\n\n",
    "created_at": "2008-09-29T20:21:44Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "Extensions of Finite Fields don't work well",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4218",
    "user": "justin"
}
```
Assignee: tbd

The following sage snippets show (some of) the problems.  First, we set
the stage:

```
sage: F1.<a> = GF(2^7)
sage: P1.<x>=PolynomialRing(F1)
sage: f=x^2+x+F1(1)
sage: F2=F1.extension(f,'u')
sage: F2
Univariate Quotient Polynomial Ring in u over Finite Field in a of size 2^7 with modulus u^2 + u + 1
sage: a in F2
True
```


First problem:

```
sage: for i in xrange(100):
   ....:         r = F2.random_element()
   ....:     if r != F2(0) and r != F2(1):
   ....:             print "Yoicks! r=%s"%r
   ....: 
sage: 
```

No output means that 100 random elements of F2 are either
0 or 1, which seems somehow incorrect.

The next oddity is

```
sage: F1.order()
128
sage: F2.order()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/SandBox/Justin/sb/sage-3.1.1/<ipython console> in <module>()

/SandBox/Justin/sb/sage-3.1.1/ring.pyx in sage.rings.ring.Ring.order (sage/rings/ring.c:4108)()

NotImplementedError: 
```

Shouldn't .order() work for extensions as well as those directly defined?



Issue created by migration from https://trac.sagemath.org/ticket/4218





---

archive/issue_comments_030654.json:
```json
{
    "body": "Justin,\n\nplease remember to assign a milestone to tickets you open :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-02T03:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4218#issuecomment-30654",
    "user": "mabshoff"
}
```

Justin,

please remember to assign a milestone to tickets you open :)

Cheers,

Michael



---

archive/issue_comments_030655.json:
```json
{
    "body": "Changing assignee from tbd to @aghitza.",
    "created_at": "2008-10-04T10:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4218#issuecomment-30655",
    "user": "@aghitza"
}
```

Changing assignee from tbd to @aghitza.



---

archive/issue_comments_030656.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-04T10:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4218#issuecomment-30656",
    "user": "@aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030657.json:
```json
{
    "body": "The attached patch resolves the issues reported above, by implementing methods random_element() and order() for quotients of polynomial rings.",
    "created_at": "2008-12-20T18:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4218#issuecomment-30657",
    "user": "@aghitza"
}
```

The attached patch resolves the issues reported above, by implementing methods random_element() and order() for quotients of polynomial rings.



---

archive/issue_comments_030658.json:
```json
{
    "body": "Attachment [trac_4218.patch](tarball://root/attachments/some-uuid/ticket4218/trac_4218.patch) by @JohnCremona created at 2008-12-21 18:08:33\n\nPositive review.  Patch applies cleanly to 3.2.2 and doctests in sage/rings/polynomial pass.\n\nI did notice while testing that this does not work:\n\n```\nsage: R.<x>=ZZ[]\nsage: S=ZZ.extension(x^3-2,'a')\nsage: S.order()\n---------------------------------------------------------------------------\nNotImplementedError    \n```\n\nand also that `S.random_element()` gives a random integer (I think).  Another ticket perhaps?",
    "created_at": "2008-12-21T18:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4218#issuecomment-30658",
    "user": "@JohnCremona"
}
```

Attachment [trac_4218.patch](tarball://root/attachments/some-uuid/ticket4218/trac_4218.patch) by @JohnCremona created at 2008-12-21 18:08:33

Positive review.  Patch applies cleanly to 3.2.2 and doctests in sage/rings/polynomial pass.

I did notice while testing that this does not work:

```
sage: R.<x>=ZZ[]
sage: S=ZZ.extension(x^3-2,'a')
sage: S.order()
---------------------------------------------------------------------------
NotImplementedError    
```

and also that `S.random_element()` gives a random integer (I think).  Another ticket perhaps?



---

archive/issue_comments_030659.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-21T22:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4218#issuecomment-30659",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030660.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-21T22:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4218#issuecomment-30660",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.3.alpha0
