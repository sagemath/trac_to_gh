# Issue 9068: remove redundant sgn function from quadratic_forms/extras

archive/issues_009068.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @kcrisman\n\nKeywords: sgn sign\n\nThere is a sgn() function defined in sage/quadratic_forms/extras.py which just duplicates the one in sage/functions/generalized.py, so I have removed it and adjusted imports accordingly.\n\nMay depend on #7828.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9068\n\n",
    "created_at": "2010-05-27T21:00:41Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "remove redundant sgn function from quadratic_forms/extras",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9068",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @aghitza

CC:  @kcrisman

Keywords: sgn sign

There is a sgn() function defined in sage/quadratic_forms/extras.py which just duplicates the one in sage/functions/generalized.py, so I have removed it and adjusted imports accordingly.

May depend on #7828.

Issue created by migration from https://trac.sagemath.org/ticket/9068





---

archive/issue_comments_084019.json:
```json
{
    "body": "Attachment [trac_9068-sgn.patch](tarball://root/attachments/some-uuid/ticket9068/trac_9068-sgn.patch) by @JohnCremona created at 2010-05-27 21:13:17\n\nApplies to 4.4.3.alpha0",
    "created_at": "2010-05-27T21:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9068#issuecomment-84019",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_9068-sgn.patch](tarball://root/attachments/some-uuid/ticket9068/trac_9068-sgn.patch) by @JohnCremona created at 2010-05-27 21:13:17

Applies to 4.4.3.alpha0



---

archive/issue_comments_084020.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-27T21:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9068#issuecomment-84020",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084021.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-05T01:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9068#issuecomment-84021",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022222.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2010-06-05T01:32:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9068",
    "milestone": "sage-4.4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9068#event-22222"
}
```



---

archive/issue_comments_084022.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-06-05T01:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9068#issuecomment-84022",
    "user": "https://github.com/aghitza"
}
```

Looks good.



---

archive/issue_events_022223.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T01:16:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9068",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9068#event-22223"
}
```



---

archive/issue_comments_084023.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9068#issuecomment-84023",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
