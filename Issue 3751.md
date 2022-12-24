# Issue 3751: Type of output returned by QuadraticField(-1).class_number()

archive/issues_003751.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe output of the class_number() method for QuadraticFields is a Python integer. Would it be possible to change this so that it returned a Sage integer?\n\n\n```\nsage: K=QuadraticField(-1,'a')\nsage: K.class_number()\n1\nsage: type(K.class_number())\n<type 'int'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3751\n\n",
    "created_at": "2008-07-31T20:37:09Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "Type of output returned by QuadraticField(-1).class_number()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3751",
    "user": "ljpk"
}
```
Assignee: @williamstein

The output of the class_number() method for QuadraticFields is a Python integer. Would it be possible to change this so that it returned a Sage integer?


```
sage: K=QuadraticField(-1,'a')
sage: K.class_number()
1
sage: type(K.class_number())
<type 'int'>
```


Issue created by migration from https://trac.sagemath.org/ticket/3751





---

archive/issue_comments_026656.json:
```json
{
    "body": "Attachment [sage-trac3751.patch](tarball://root/attachments/some-uuid/ticket3751/sage-trac3751.patch) by @JohnCremona created at 2008-08-01 02:41:37\n\nThe patch fixes this.  Based on 3.0.6, and all tests in sage/rings/number_fields pass.",
    "created_at": "2008-08-01T02:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3751#issuecomment-26656",
    "user": "@JohnCremona"
}
```

Attachment [sage-trac3751.patch](tarball://root/attachments/some-uuid/ticket3751/sage-trac3751.patch) by @JohnCremona created at 2008-08-01 02:41:37

The patch fixes this.  Based on 3.0.6, and all tests in sage/rings/number_fields pass.



---

archive/issue_comments_026657.json:
```json
{
    "body": "Attachment [3751-ncalexan-class-number.patch](tarball://root/attachments/some-uuid/ticket3751/3751-ncalexan-class-number.patch) by @ncalexan created at 2008-08-10 19:02:08\n\nI added some tests, but this looks good.\n\nApply only 3751-ncalexan-class-number.patch.",
    "created_at": "2008-08-10T19:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3751#issuecomment-26657",
    "user": "@ncalexan"
}
```

Attachment [3751-ncalexan-class-number.patch](tarball://root/attachments/some-uuid/ticket3751/3751-ncalexan-class-number.patch) by @ncalexan created at 2008-08-10 19:02:08

I added some tests, but this looks good.

Apply only 3751-ncalexan-class-number.patch.



---

archive/issue_comments_026658.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-11T00:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3751#issuecomment-26658",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026659.json:
```json
{
    "body": "Merged 3751-ncalexan-class-number.patch in Sage 3.1.alpha1",
    "created_at": "2008-08-11T00:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3751#issuecomment-26659",
    "user": "mabshoff"
}
```

Merged 3751-ncalexan-class-number.patch in Sage 3.1.alpha1
