# Issue 4820: Type inconsistency in rational points on elliptic curves

archive/issues_004820.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: elliptic curves\n\nPoints on elliptic curves over Q which are not [0:1:0] have their last coordinate =1 but sometimes this is an int (not even an Integer) which breaks some code:\n\n\n```\nsage: E=EllipticCurve('37a1')\nsage: [type(c) for c in E(0)]\n\n[<type 'sage.rings.rational.Rational'>,\n <type 'sage.rings.rational.Rational'>,\n <type 'sage.rings.rational.Rational'>]\nsage: [type(c) for c in E.gen(0)]\n\n[<type 'sage.rings.rational.Rational'>,\n <type 'sage.rings.rational.Rational'>,\n <type 'sage.rings.rational.Rational'>]\nsage: [type(c) for c in 2*E.gen(0)]\n\n[<type 'sage.rings.rational.Rational'>,\n <type 'sage.rings.rational.Rational'>,\n <type 'int'>]\n```\n\nI am tracking this down and will post a patch soon.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4820\n\n",
    "created_at": "2008-12-17T11:55:08Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Type inconsistency in rational points on elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4820",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

Keywords: elliptic curves

Points on elliptic curves over Q which are not [0:1:0] have their last coordinate =1 but sometimes this is an int (not even an Integer) which breaks some code:


```
sage: E=EllipticCurve('37a1')
sage: [type(c) for c in E(0)]

[<type 'sage.rings.rational.Rational'>,
 <type 'sage.rings.rational.Rational'>,
 <type 'sage.rings.rational.Rational'>]
sage: [type(c) for c in E.gen(0)]

[<type 'sage.rings.rational.Rational'>,
 <type 'sage.rings.rational.Rational'>,
 <type 'sage.rings.rational.Rational'>]
sage: [type(c) for c in 2*E.gen(0)]

[<type 'sage.rings.rational.Rational'>,
 <type 'sage.rings.rational.Rational'>,
 <type 'int'>]
```

I am tracking this down and will post a patch soon.


Issue created by migration from https://trac.sagemath.org/ticket/4820





---

archive/issue_comments_036470.json:
```json
{
    "body": "Attachment [trac-4820.patch](tarball://root/attachments/some-uuid/ticket4820/trac-4820.patch) by @JohnCremona created at 2008-12-17 15:39:35",
    "created_at": "2008-12-17T15:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36470",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac-4820.patch](tarball://root/attachments/some-uuid/ticket4820/trac-4820.patch) by @JohnCremona created at 2008-12-17 15:39:35



---

archive/issue_comments_036471.json:
```json
{
    "body": "Looks fine by me.  I checked that (0 : 1 : 0) over a non-standard ring had the correct types.",
    "created_at": "2009-01-21T22:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36471",
    "user": "https://github.com/ncalexan"
}
```

Looks fine by me.  I checked that (0 : 1 : 0) over a non-standard ring had the correct types.



---

archive/issue_comments_036472.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T10:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36472",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1

Cheers,

Michael



---

archive/issue_comments_036473.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2009-01-23T10:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36473",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_036474.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T10:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36474",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036475.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-01-23T10:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36475",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from assigned to new.



---

archive/issue_comments_036476.json:
```json
{
    "body": "Changing assignee from mabshoff to @williamstein.",
    "created_at": "2009-01-23T10:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36476",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from mabshoff to @williamstein.



---

archive/issue_comments_036477.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T10:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36477",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036478.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T10:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36478",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1

Cheers,

Michael



---

archive/issue_events_005064.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T10:28:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4820#event-5064"
}
```
