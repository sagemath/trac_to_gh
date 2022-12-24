# Issue 2349: homogenize does different things in different contexts

archive/issues_002349.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @ncalexan\n\nKeywords: polynomial multi multivariate homogenize\n\nHere are some examples:\n\n\n```\nsage: x = Zmod(3)['x'].gen(); x.homogenize('y')\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/ncalexan/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute 'homogenize'\nsage: x, y = Zmod(3)['x', 'y'].gens(); (x + x^2).homogenize(y)\nx^2 + x*y\nsage: x, y = Zmod(3)['x', 'y'].gens(); (x + x^2).homogenize(y).parent()\nMultivariate Polynomial Ring in x, y, y over Ring of integers modulo 3\nsage: x, y = GF(3)['x', 'y'].gens(); (x + x^2).homogenize(y)\nx^2 + x*y\nsage: x, y = GF(3)['x', 'y'].gens(); (x + x^2).homogenize(y).parent()\nMultivariate Polynomial Ring in x, y over Finite Field of size 3\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2349\n\n",
    "created_at": "2008-02-28T21:54:09Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "homogenize does different things in different contexts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2349",
    "user": "@ncalexan"
}
```
Assignee: @malb

CC:  @ncalexan

Keywords: polynomial multi multivariate homogenize

Here are some examples:


```
sage: x = Zmod(3)['x'].gen(); x.homogenize('y')
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute 'homogenize'
sage: x, y = Zmod(3)['x', 'y'].gens(); (x + x^2).homogenize(y)
x^2 + x*y
sage: x, y = Zmod(3)['x', 'y'].gens(); (x + x^2).homogenize(y).parent()
Multivariate Polynomial Ring in x, y, y over Ring of integers modulo 3
sage: x, y = GF(3)['x', 'y'].gens(); (x + x^2).homogenize(y)
x^2 + x*y
sage: x, y = GF(3)['x', 'y'].gens(); (x + x^2).homogenize(y).parent()
Multivariate Polynomial Ring in x, y over Finite Field of size 3
```



Issue created by migration from https://trac.sagemath.org/ticket/2349





---

archive/issue_comments_015778.json:
```json
{
    "body": "Attachment [trac_2349.patch](tarball://root/attachments/some-uuid/ticket2349/trac_2349.patch) by @malb created at 2008-02-29 01:44:26",
    "created_at": "2008-02-29T01:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2349#issuecomment-15778",
    "user": "@malb"
}
```

Attachment [trac_2349.patch](tarball://root/attachments/some-uuid/ticket2349/trac_2349.patch) by @malb created at 2008-02-29 01:44:26



---

archive/issue_comments_015779.json:
```json
{
    "body": "The attached patch unifies homogenize for the multivariate polynomials, but not the univariate yet.",
    "created_at": "2008-02-29T01:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2349#issuecomment-15779",
    "user": "@malb"
}
```

The attached patch unifies homogenize for the multivariate polynomials, but not the univariate yet.



---

archive/issue_comments_015780.json:
```json
{
    "body": "This patch fixes the code I was writing :)  It only applies to the multivariate case, see ticket #2352 for the univariate case.\n\nDoctests are good.  I say apply.",
    "created_at": "2008-02-29T18:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2349#issuecomment-15780",
    "user": "@ncalexan"
}
```

This patch fixes the code I was writing :)  It only applies to the multivariate case, see ticket #2352 for the univariate case.

Doctests are good.  I say apply.



---

archive/issue_comments_015781.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-02T20:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2349#issuecomment-15781",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015782.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc1",
    "created_at": "2008-03-02T20:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2349#issuecomment-15782",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc1
