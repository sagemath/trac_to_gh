# Issue 553: [with patch, positive review] calling of symbolic expressions is sometimes ridiculous

archive/issues_000553.json:
```json
{
    "body": "Assignee: @mwhansen\n\n```\n\nThe input should be\n\n       f = x^(1/9) + (2^(8/9) - 2^(1/9))*(x - 1) - x^(8/9)\n\nNote that * before (x-1).  That your input was accepted is an indication\nthat SAGE should be more restrictive with what it allows.  What's\nhappening is that (2^(8/9) - 2^(1/9)) is parsed as a symbolic expression (a\nconstant function), and then 2^(8/9) - 2^(1/9))(x - 1) is the value of that\nconstant function at x-1.  Yep, that this is allowed is ridiculous, and should\nbe changed (I've filed a bug report). \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/553\n\n",
    "closed_at": "2007-12-15T11:26:45Z",
    "created_at": "2007-09-01T17:22:55Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch, positive review] calling of symbolic expressions is sometimes ridiculous",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/553",
    "user": "https://github.com/williamstein"
}
```
Assignee: @mwhansen

```

The input should be

       f = x^(1/9) + (2^(8/9) - 2^(1/9))*(x - 1) - x^(8/9)

Note that * before (x-1).  That your input was accepted is an indication
that SAGE should be more restrictive with what it allows.  What's
happening is that (2^(8/9) - 2^(1/9)) is parsed as a symbolic expression (a
constant function), and then 2^(8/9) - 2^(1/9))(x - 1) is the value of that
constant function at x-1.  Yep, that this is allowed is ridiculous, and should
be changed (I've filed a bug report). 
```

Issue created by migration from https://trac.sagemath.org/ticket/553





---

archive/issue_comments_002839.json:
```json
{
    "body": "Attachment [553.patch](tarball://root/attachments/some-uuid/ticket553/553.patch) by @mwhansen created at 2007-09-06 22:49:40\n\nI attached a patch which throws an error when trying to substitute into a constant expression.\nIt can be overridden by passing a substitute=True parameter to __call__. \n\nAll doc tests pass with it.",
    "created_at": "2007-09-06T22:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2839",
    "user": "https://github.com/mwhansen"
}
```

Attachment [553.patch](tarball://root/attachments/some-uuid/ticket553/553.patch) by @mwhansen created at 2007-09-06 22:49:40

I attached a patch which throws an error when trying to substitute into a constant expression.
It can be overridden by passing a substitute=True parameter to __call__. 

All doc tests pass with it.



---

archive/issue_comments_002840.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-09-06T22:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2840",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_events_001467.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-07T04:14:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/553#event-1467"
}
```



---

archive/issue_comments_002841.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T04:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2841",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_002842.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-07T07:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2842",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_002843.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-07T07:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2843",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001468.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-07T07:21:31Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/553#event-1468"
}
```



---

archive/issue_comments_002844.json:
```json
{
    "body": "This patch doesn't fix the problem at all.   If you apply it the above example\ndoesn't raise an error.  In fact, it's a patch against named substitutions, which\nshould *always* be allowed.  So this was totally wrong.\n\nI'm worried actually that the expense of determining whether or not an expression\nis too costly.  The only reasonable fix is to completely ban calling \"non-callable\"\nsymbolic expressions without an explicit substitution.  doing this is a lot more\nwork though.",
    "created_at": "2007-09-07T07:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2844",
    "user": "https://github.com/williamstein"
}
```

This patch doesn't fix the problem at all.   If you apply it the above example
doesn't raise an error.  In fact, it's a patch against named substitutions, which
should *always* be allowed.  So this was totally wrong.

I'm worried actually that the expense of determining whether or not an expression
is too costly.  The only reasonable fix is to completely ban calling "non-callable"
symbolic expressions without an explicit substitution.  doing this is a lot more
work though.



---

archive/issue_comments_002845.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-09-07T07:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2845",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_001469.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-20T14:04:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/553#event-1469"
}
```



---

archive/issue_comments_002846.json:
```json
{
    "body": "I think the best way to go about doing this is to add a number_of_arguments() to SymbolicExpressions:\n\n```\nsage: sin.number_of_arguments()\n1\nsage: (sin+1).number_of_arguments()\n1\nsage: (sin+x).number_of_arguments()\n1\nsage: (sin+x+y).number_of_arguments()\n2\nsage: (2^(8/9)-2^(1/9)).number_of_arguments()\n0\n```",
    "created_at": "2007-12-05T21:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2846",
    "user": "https://github.com/mwhansen"
}
```

I think the best way to go about doing this is to add a number_of_arguments() to SymbolicExpressions:

```
sage: sin.number_of_arguments()
1
sage: (sin+1).number_of_arguments()
1
sage: (sin+x).number_of_arguments()
1
sage: (sin+x+y).number_of_arguments()
2
sage: (2^(8/9)-2^(1/9)).number_of_arguments()
0
```



---

archive/issue_comments_002847.json:
```json
{
    "body": "Attachment [533.patch](tarball://root/attachments/some-uuid/ticket553/533.patch) by @mwhansen created at 2007-12-06 10:55:08",
    "created_at": "2007-12-06T10:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2847",
    "user": "https://github.com/mwhansen"
}
```

Attachment [533.patch](tarball://root/attachments/some-uuid/ticket553/533.patch) by @mwhansen created at 2007-12-06 10:55:08



---

archive/issue_comments_002848.json:
```json
{
    "body": "I've put up a new patch.",
    "created_at": "2007-12-06T10:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2848",
    "user": "https://github.com/mwhansen"
}
```

I've put up a new patch.



---

archive/issue_comments_002849.json:
```json
{
    "body": "apply this patch and the one right above it.",
    "created_at": "2007-12-15T11:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2849",
    "user": "https://github.com/williamstein"
}
```

apply this patch and the one right above it.



---

archive/issue_comments_002850.json:
```json
{
    "body": "Attachment [trac-553-part2.patch](tarball://root/attachments/some-uuid/ticket553/trac-553-part2.patch) by @williamstein created at 2007-12-15 11:13:06",
    "created_at": "2007-12-15T11:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2850",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-553-part2.patch](tarball://root/attachments/some-uuid/ticket553/trac-553-part2.patch) by @williamstein created at 2007-12-15 11:13:06



---

archive/issue_comments_002851.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T11:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2851",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002852.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T11:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/553#issuecomment-2852",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_events_001470.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T11:26:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/553",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/553#event-1470"
}
```
