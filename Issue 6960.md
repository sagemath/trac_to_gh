# Issue 6960: silly inconsistency in pari versus magma interface

archive/issues_006960.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: a = pari('393')\nsage: a.python()\n393\nsage: a = magma('393')\nsage: a.sage()\n393     \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6960\n\n",
    "created_at": "2009-09-19T06:13:32Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "silly inconsistency in pari versus magma interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6960",
    "user": "was"
}
```
Assignee: was


```
sage: a = pari('393')
sage: a.python()
393
sage: a = magma('393')
sage: a.sage()
393     
```


Issue created by migration from https://trac.sagemath.org/ticket/6960





---

archive/issue_comments_057571.json:
```json
{
    "body": "Attachment [trac_6960.patch](tarball://root/attachments/some-uuid/ticket6960/trac_6960.patch) by was created at 2010-01-18 13:26:32",
    "created_at": "2010-01-18T13:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6960#issuecomment-57571",
    "user": "was"
}
```

Attachment [trac_6960.patch](tarball://root/attachments/some-uuid/ticket6960/trac_6960.patch) by was created at 2010-01-18 13:26:32



---

archive/issue_comments_057572.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T06:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6960#issuecomment-57572",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057573.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T06:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6960#issuecomment-57573",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057574.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T06:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6960#issuecomment-57574",
    "user": "rlm"
}
```

Resolution: fixed
