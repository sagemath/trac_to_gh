# Issue 6998: wrong error for powerseries sqrt

archive/issues_006998.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R.<x> = QQ[[]]\nsage: (x^10/2).sqrt()\nTraceback (click to the left for traceback)\n...\nValueError: power series does not have a square root since it has odd\nvaluation.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6998\n\n",
    "created_at": "2009-09-22T23:19:05Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "wrong error for powerseries sqrt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6998",
    "user": "robertwb"
}
```
Assignee: somebody


```
sage: R.<x> = QQ[[]]
sage: (x^10/2).sqrt()
Traceback (click to the left for traceback)
...
ValueError: power series does not have a square root since it has odd
valuation.
```


Issue created by migration from https://trac.sagemath.org/ticket/6998





---

archive/issue_comments_057869.json:
```json
{
    "body": "Changing component from basic arithmetic to algebra.",
    "created_at": "2009-09-22T23:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57869",
    "user": "robertwb"
}
```

Changing component from basic arithmetic to algebra.



---

archive/issue_comments_057870.json:
```json
{
    "body": "Changing assignee from somebody to tbd.",
    "created_at": "2009-09-22T23:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57870",
    "user": "robertwb"
}
```

Changing assignee from somebody to tbd.



---

archive/issue_comments_057871.json:
```json
{
    "body": "Changing assignee from tbd to mhansen.",
    "created_at": "2009-09-24T06:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57871",
    "user": "mhansen"
}
```

Changing assignee from tbd to mhansen.



---

archive/issue_comments_057872.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-24T06:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57872",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_057873.json:
```json
{
    "body": "Attachment [trac_6998.patch](tarball://root/attachments/some-uuid/ticket6998/trac_6998.patch) by mhansen created at 2009-09-24 06:12:15",
    "created_at": "2009-09-24T06:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57873",
    "user": "mhansen"
}
```

Attachment [trac_6998.patch](tarball://root/attachments/some-uuid/ticket6998/trac_6998.patch) by mhansen created at 2009-09-24 06:12:15



---

archive/issue_comments_057874.json:
```json
{
    "body": "The patch works as advertised so I give it a positive review. The doc also builds correctly.\n\nAdam",
    "created_at": "2009-10-06T08:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57874",
    "user": "awebb"
}
```

The patch works as advertised so I give it a positive review. The doc also builds correctly.

Adam



---

archive/issue_comments_057875.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T09:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57875",
    "user": "mhansen"
}
```

Resolution: fixed
