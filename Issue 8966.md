# Issue 8966: Polynomial reduce causes segmentation fault

archive/issues_008966.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @malb polybori\n\n\n```\neno% ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: R=BooleanPolynomialRing(20,'x','lex')\nsage: a=R.random_element()\nsage: a.reduce([None,None])\n| Sage Version 4.4.1, Release Date: 2010-05-02                       |\n| Type notebook() for the GUI, and license() for information.        |\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in Sage.\nThis probably occured because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n\neno%\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8966\n\n",
    "created_at": "2010-05-14T18:18:46Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Polynomial reduce causes segmentation fault",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8966",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```
Assignee: @aghitza

CC:  @malb polybori


```
eno% ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R=BooleanPolynomialRing(20,'x','lex')
sage: a=R.random_element()
sage: a.reduce([None,None])
| Sage Version 4.4.1, Release Date: 2010-05-02                       |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------

eno%
```


Issue created by migration from https://trac.sagemath.org/ticket/8966





---

archive/issue_comments_082500.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2010-06-04T11:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8966#issuecomment-82500",
    "user": "https://github.com/burcin"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_082501.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-04T11:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8966#issuecomment-82501",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082502.json:
```json
{
    "body": "This was a simple input checking problem in our interface to polybori. I would have expected Cython not to accept `None` as a `BooleanPolynomial` though.",
    "created_at": "2010-06-04T11:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8966#issuecomment-82502",
    "user": "https://github.com/burcin"
}
```

This was a simple input checking problem in our interface to polybori. I would have expected Cython not to accept `None` as a `BooleanPolynomial` though.



---

archive/issue_comments_082503.json:
```json
{
    "body": "Patch looks good, doctests pass.",
    "created_at": "2010-06-04T12:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8966#issuecomment-82503",
    "user": "https://github.com/malb"
}
```

Patch looks good, doctests pass.



---

archive/issue_comments_082504.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-04T12:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8966#issuecomment-82504",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082505.json:
```json
{
    "body": "Attachment [trac_8966-pbori_reduce.patch](tarball://root/attachments/some-uuid/ticket8966/trac_8966-pbori_reduce.patch) by @williamstein created at 2010-06-04 14:59:04",
    "created_at": "2010-06-04T14:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8966#issuecomment-82505",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8966-pbori_reduce.patch](tarball://root/attachments/some-uuid/ticket8966/trac_8966-pbori_reduce.patch) by @williamstein created at 2010-06-04 14:59:04



---

archive/issue_comments_082506.json:
```json
{
    "body": "Looks good.  Note I changed it from ValueError to TypeError, since it is really a TypeError, and that's what Cython should raise.",
    "created_at": "2010-06-04T14:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8966#issuecomment-82506",
    "user": "https://github.com/williamstein"
}
```

Looks good.  Note I changed it from ValueError to TypeError, since it is really a TypeError, and that's what Cython should raise.



---

archive/issue_comments_082507.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T00:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8966#issuecomment-82507",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_009116.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T00:59:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8966",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8966#event-9116"
}
```
