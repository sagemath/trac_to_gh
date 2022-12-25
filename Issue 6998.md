# Issue 6998: wrong error for powerseries sqrt

archive/issues_006998.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R.<x> = QQ[[]]\nsage: (x^10/2).sqrt()\nTraceback (click to the left for traceback)\n...\nValueError: power series does not have a square root since it has odd\nvaluation.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6998\n\n",
    "created_at": "2009-09-22T23:19:05Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "wrong error for powerseries sqrt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6998",
    "user": "https://github.com/robertwb"
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

archive/issue_comments_057761.json:
```json
{
    "body": "Changing component from basic arithmetic to algebra.",
    "created_at": "2009-09-22T23:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57761",
    "user": "https://github.com/robertwb"
}
```

Changing component from basic arithmetic to algebra.



---

archive/issue_comments_057762.json:
```json
{
    "body": "Changing assignee from somebody to tbd.",
    "created_at": "2009-09-22T23:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57762",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from somebody to tbd.



---

archive/issue_comments_057763.json:
```json
{
    "body": "Changing assignee from tbd to @mwhansen.",
    "created_at": "2009-09-24T06:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57763",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from tbd to @mwhansen.



---

archive/issue_comments_057764.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-24T06:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57764",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_057765.json:
```json
{
    "body": "Attachment [trac_6998.patch](tarball://root/attachments/some-uuid/ticket6998/trac_6998.patch) by @mwhansen created at 2009-09-24 06:12:15",
    "created_at": "2009-09-24T06:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57765",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6998.patch](tarball://root/attachments/some-uuid/ticket6998/trac_6998.patch) by @mwhansen created at 2009-09-24 06:12:15



---

archive/issue_comments_057766.json:
```json
{
    "body": "The patch works as advertised so I give it a positive review. The doc also builds correctly.\n\nAdam",
    "created_at": "2009-10-06T08:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57766",
    "user": "https://github.com/maxthemouse"
}
```

The patch works as advertised so I give it a positive review. The doc also builds correctly.

Adam



---

archive/issue_events_016423.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-15T09:35:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6998#event-16423"
}
```



---

archive/issue_comments_057767.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T09:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6998#issuecomment-57767",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
