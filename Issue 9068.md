# Issue 9068: remove redundant sgn function from quadratic_forms/extras

archive/issues_009068.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  kcrisman\n\nKeywords: sgn sign\n\nThere is a sgn() function defined in sage/quadratic_forms/extras.py which just duplicates the one in sage/functions/generalized.py, so I have removed it and adjusted imports accordingly.\n\nMay depend on #7828.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9068\n\n",
    "created_at": "2010-05-27T21:00:41Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "remove redundant sgn function from quadratic_forms/extras",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9068",
    "user": "cremona"
}
```
Assignee: AlexGhitza

CC:  kcrisman

Keywords: sgn sign

There is a sgn() function defined in sage/quadratic_forms/extras.py which just duplicates the one in sage/functions/generalized.py, so I have removed it and adjusted imports accordingly.

May depend on #7828.

Issue created by migration from https://trac.sagemath.org/ticket/9068





---

archive/issue_comments_084155.json:
```json
{
    "body": "Attachment [trac_9068-sgn.patch](tarball://root/attachments/some-uuid/ticket9068/trac_9068-sgn.patch) by cremona created at 2010-05-27 21:13:17\n\nApplies to 4.4.3.alpha0",
    "created_at": "2010-05-27T21:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9068#issuecomment-84155",
    "user": "cremona"
}
```

Attachment [trac_9068-sgn.patch](tarball://root/attachments/some-uuid/ticket9068/trac_9068-sgn.patch) by cremona created at 2010-05-27 21:13:17

Applies to 4.4.3.alpha0



---

archive/issue_comments_084156.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-27T21:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9068#issuecomment-84156",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084157.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-05T01:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9068#issuecomment-84157",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084158.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-06-05T01:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9068#issuecomment-84158",
    "user": "AlexGhitza"
}
```

Looks good.



---

archive/issue_comments_084159.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9068#issuecomment-84159",
    "user": "mhansen"
}
```

Resolution: fixed
