# Issue 4820: Type inconsistency in rational points on elliptic curves

archive/issues_004820.json:
```json
{
    "body": "Assignee: was\n\nKeywords: elliptic curves\n\nPoints on elliptic curves over Q which are not [0:1:0] have their last coordinate =1 but sometimes this is an int (not even an Integer) which breaks some code:\n\n\n```\nsage: E=EllipticCurve('37a1')\nsage: [type(c) for c in E(0)]\n\n[<type 'sage.rings.rational.Rational'>,\n <type 'sage.rings.rational.Rational'>,\n <type 'sage.rings.rational.Rational'>]\nsage: [type(c) for c in E.gen(0)]\n\n[<type 'sage.rings.rational.Rational'>,\n <type 'sage.rings.rational.Rational'>,\n <type 'sage.rings.rational.Rational'>]\nsage: [type(c) for c in 2*E.gen(0)]\n\n[<type 'sage.rings.rational.Rational'>,\n <type 'sage.rings.rational.Rational'>,\n <type 'int'>]\n```\n\nI am tracking this down and will post a patch soon.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4820\n\n",
    "created_at": "2008-12-17T11:55:08Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "Type inconsistency in rational points on elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4820",
    "user": "cremona"
}
```
Assignee: was

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

archive/issue_comments_036542.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-17T15:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36542",
    "user": "cremona"
}
```

Attachment



---

archive/issue_comments_036543.json:
```json
{
    "body": "Looks fine by me.  I checked that (0 : 1 : 0) over a non-standard ring had the correct types.",
    "created_at": "2009-01-21T22:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36543",
    "user": "ncalexan"
}
```

Looks fine by me.  I checked that (0 : 1 : 0) over a non-standard ring had the correct types.



---

archive/issue_comments_036544.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T10:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36544",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1

Cheers,

Michael



---

archive/issue_comments_036545.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2009-01-23T10:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36545",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_036546.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T10:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36546",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036547.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-01-23T10:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36547",
    "user": "mabshoff"
}
```

Changing status from assigned to new.



---

archive/issue_comments_036548.json:
```json
{
    "body": "Changing assignee from mabshoff to was.",
    "created_at": "2009-01-23T10:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36548",
    "user": "mabshoff"
}
```

Changing assignee from mabshoff to was.



---

archive/issue_comments_036549.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T10:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36549",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036550.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T10:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4820#issuecomment-36550",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1

Cheers,

Michael
