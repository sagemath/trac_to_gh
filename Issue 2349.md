# Issue 2349: homogenize does different things in different contexts

archive/issues_002349.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @ncalexan\n\nKeywords: polynomial multi multivariate homogenize\n\nHere are some examples:\n\n```\nsage: x = Zmod(3)['x'].gen(); x.homogenize('y')\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/ncalexan/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute 'homogenize'\nsage: x, y = Zmod(3)['x', 'y'].gens(); (x + x^2).homogenize(y)\nx^2 + x*y\nsage: x, y = Zmod(3)['x', 'y'].gens(); (x + x^2).homogenize(y).parent()\nMultivariate Polynomial Ring in x, y, y over Ring of integers modulo 3\nsage: x, y = GF(3)['x', 'y'].gens(); (x + x^2).homogenize(y)\nx^2 + x*y\nsage: x, y = GF(3)['x', 'y'].gens(); (x + x^2).homogenize(y).parent()\nMultivariate Polynomial Ring in x, y over Finite Field of size 3\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2349\n\n",
    "created_at": "2008-02-28T21:54:09Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "homogenize does different things in different contexts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2349",
    "user": "https://github.com/ncalexan"
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

archive/issue_comments_015743.json:
```json
{
    "body": "Attachment [trac_2349.patch](tarball://root/attachments/some-uuid/ticket2349/trac_2349.patch) by @malb created at 2008-02-29 01:44:26",
    "created_at": "2008-02-29T01:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2349#issuecomment-15743",
    "user": "https://github.com/malb"
}
```

Attachment [trac_2349.patch](tarball://root/attachments/some-uuid/ticket2349/trac_2349.patch) by @malb created at 2008-02-29 01:44:26



---

archive/issue_comments_015744.json:
```json
{
    "body": "The attached patch unifies homogenize for the multivariate polynomials, but not the univariate yet.",
    "created_at": "2008-02-29T01:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2349#issuecomment-15744",
    "user": "https://github.com/malb"
}
```

The attached patch unifies homogenize for the multivariate polynomials, but not the univariate yet.



---

archive/issue_comments_015745.json:
```json
{
    "body": "This patch fixes the code I was writing :)  It only applies to the multivariate case, see ticket #2352 for the univariate case.\n\nDoctests are good.  I say apply.",
    "created_at": "2008-02-29T18:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2349#issuecomment-15745",
    "user": "https://github.com/ncalexan"
}
```

This patch fixes the code I was writing :)  It only applies to the multivariate case, see ticket #2352 for the univariate case.

Doctests are good.  I say apply.



---

archive/issue_comments_015746.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-02T20:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2349#issuecomment-15746",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015747.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc1",
    "created_at": "2008-03-02T20:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2349#issuecomment-15747",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc1



---

archive/issue_events_005538.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-02T20:54:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2349",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2349#event-5538"
}
```



---

archive/issue_events_005539.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-03-03T01:50:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2349",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2349#event-5539"
}
```
