# Issue 9257: remove misc/darcs.py in Sage 5.0

archive/issues_009257.json:
```json
{
    "body": "Assignee: mvngu\n\nFrom [sage-devel](https://groups.google.com/group/sage-devel/browse_thread/thread/971ea3ce256eed20):\n\n```\nThe file misc/darcs.py was meant to serve as an interface to the Darcs\nsource code version control system, back in the old days before Sage\nswitched to using Mercurial. With the upcoming Sage 5.0 milestone, I\nthink that module can be removed from the Sage library. I believe its\nremoval would result in very minimal (next to zero?) hassle regarding\nissues of backward compatibility. If I understand the Mercurial log of\nthe Sage library correctly, Sage hasn't been using Darcs for over 2\nyears now, or even since February 2006. \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9257\n\n",
    "closed_at": "2010-07-21T10:10:38Z",
    "created_at": "2010-06-18T05:58:15Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "remove misc/darcs.py in Sage 5.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9257",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

From [sage-devel](https://groups.google.com/group/sage-devel/browse_thread/thread/971ea3ce256eed20):

```
The file misc/darcs.py was meant to serve as an interface to the Darcs
source code version control system, back in the old days before Sage
switched to using Mercurial. With the upcoming Sage 5.0 milestone, I
think that module can be removed from the Sage library. I believe its
removal would result in very minimal (next to zero?) hassle regarding
issues of backward compatibility. If I understand the Mercurial log of
the Sage library correctly, Sage hasn't been using Darcs for over 2
years now, or even since February 2006. 
```

Issue created by migration from https://trac.sagemath.org/ticket/9257





---

archive/issue_comments_086973.json:
```json
{
    "body": "Attachment [9257-remove-darcs.patch](tarball://root/attachments/some-uuid/ticket9257/9257-remove-darcs.patch) by @robertwb created at 2010-06-21 21:36:15",
    "created_at": "2010-06-21T21:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-86973",
    "user": "https://github.com/robertwb"
}
```

Attachment [9257-remove-darcs.patch](tarball://root/attachments/some-uuid/ticket9257/9257-remove-darcs.patch) by @robertwb created at 2010-06-21 21:36:15



---

archive/issue_comments_086974.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-21T21:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-86974",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086975.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-22T17:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-86975",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086976.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-06-22T17:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-86976",
    "user": "https://github.com/rlmill"
}
```

Looks good to me.



---

archive/issue_events_022800.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-21T10:10:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9257#event-22800"
}
```



---

archive/issue_comments_086977.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T10:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-86977",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_022801.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-21T10:10:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "milestone": "sage-4.5.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9257#event-22801"
}
```



---

archive/issue_comments_086978.json:
```json
{
    "body": "Followup; apparently we *still* have remnants of darcs.  See #13122.",
    "created_at": "2012-06-16T03:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-86978",
    "user": "https://github.com/kcrisman"
}
```

Followup; apparently we *still* have remnants of darcs.  See #13122.



---

archive/issue_comments_086979.json:
```json
{
    "body": "As a historical note, the original thread referenced here was off by about a year and a half on when Sage 5.0 would be released... ah, expectations.",
    "created_at": "2012-06-16T03:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-86979",
    "user": "https://github.com/kcrisman"
}
```

As a historical note, the original thread referenced here was off by about a year and a half on when Sage 5.0 would be released... ah, expectations.
