# Issue 3373: ZZ division gives wrong sym_parent [new symbolics]

archive/issues_003373.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nFor x a ZZ variable, 1/x claims to be an integer:\n\n```\nsage: var('x', ZZ)\nx\nsage: (1/x).sym_parent()\nInteger Ring\n```\n\n\nBut in Sage, integer division always gives a rational:\n\n```\nsage: parent(1/1)\nRational Field\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3373\n\n",
    "created_at": "2008-06-05T20:07:17Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "title": "ZZ division gives wrong sym_parent [new symbolics]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3373",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @garyfurnish

For x a ZZ variable, 1/x claims to be an integer:

```
sage: var('x', ZZ)
x
sage: (1/x).sym_parent()
Integer Ring
```


But in Sage, integer division always gives a rational:

```
sage: parent(1/1)
Rational Field
```


Issue created by migration from https://trac.sagemath.org/ticket/3373





---

archive/issue_comments_023547.json:
```json
{
    "body": "Fixed in sage-symbolics rev #10235",
    "created_at": "2008-07-18T09:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3373#issuecomment-23547",
    "user": "https://github.com/garyfurnish"
}
```

Fixed in sage-symbolics rev #10235



---

archive/issue_comments_023548.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-18T09:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3373#issuecomment-23548",
    "user": "https://github.com/garyfurnish"
}
```

Resolution: fixed



---

archive/issue_comments_023549.json:
```json
{
    "body": "Milestone sage-symbolics deleted",
    "created_at": "2008-08-23T08:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3373#issuecomment-23549",
    "user": "https://github.com/williamstein"
}
```

Milestone sage-symbolics deleted
