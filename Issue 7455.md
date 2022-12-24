# Issue 7455: SageNB - Searching on Log page does not work.

archive/issues_007455.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nSearching for anything on the Log page does not work due to missing javascript libraries.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7455\n\n",
    "created_at": "2009-11-13T20:28:26Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "SageNB - Searching on Log page does not work.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7455",
    "user": "timdumol"
}
```
Assignee: AlexGhitza

Searching for anything on the Log page does not work due to missing javascript libraries.

Issue created by migration from https://trac.sagemath.org/ticket/7455





---

archive/issue_comments_062787.json:
```json
{
    "body": "Changing component from algebra to notebook.",
    "created_at": "2009-11-13T22:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62787",
    "user": "AlexGhitza"
}
```

Changing component from algebra to notebook.



---

archive/issue_comments_062788.json:
```json
{
    "body": "Changing assignee from AlexGhitza to boothby.",
    "created_at": "2009-11-13T22:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62788",
    "user": "AlexGhitza"
}
```

Changing assignee from AlexGhitza to boothby.



---

archive/issue_comments_062789.json:
```json
{
    "body": "Attachment [trac_7455-searching-on-log-page.patch](tarball://root/attachments/some-uuid/ticket7455/trac_7455-searching-on-log-page.patch) by timdumol created at 2009-11-13 23:31:29\n\nThis remvoes the search bar from the history page and updates the tests to reflect that.",
    "created_at": "2009-11-13T23:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62789",
    "user": "timdumol"
}
```

Attachment [trac_7455-searching-on-log-page.patch](tarball://root/attachments/some-uuid/ticket7455/trac_7455-searching-on-log-page.patch) by timdumol created at 2009-11-13 23:31:29

This remvoes the search bar from the history page and updates the tests to reflect that.



---

archive/issue_comments_062790.json:
```json
{
    "body": "The problem is apparently a bit harder to fix. It requires a few changes to the js libraries. For now, this patch is a temporary fix.",
    "created_at": "2009-11-13T23:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62790",
    "user": "timdumol"
}
```

The problem is apparently a bit harder to fix. It requires a few changes to the js libraries. For now, this patch is a temporary fix.



---

archive/issue_comments_062791.json:
```json
{
    "body": "I have thought over this, and it seems to me that it makes more sense to keep the search box only in the worksheet list pages (Home and Published). If there are no objections, then the previous patch removing the search box should be the one included.",
    "created_at": "2009-11-15T02:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62791",
    "user": "timdumol"
}
```

I have thought over this, and it seems to me that it makes more sense to keep the search box only in the worksheet list pages (Home and Published). If there are no objections, then the previous patch removing the search box should be the one included.



---

archive/issue_comments_062792.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-15T02:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62792",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062793.json:
```json
{
    "body": "I agree with this patch.  It would of course be better to just get rid of the whole top bar, and make all the cells be properly styled, etc.   But this current patch is very simple at and at least fixes this bug.  Positive review.",
    "created_at": "2009-12-08T21:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62793",
    "user": "was"
}
```

I agree with this patch.  It would of course be better to just get rid of the whole top bar, and make all the cells be properly styled, etc.   But this current patch is very simple at and at least fixes this bug.  Positive review.



---

archive/issue_comments_062794.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T21:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62794",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062795.json:
```json
{
    "body": "merged in sagenb-0.4.6",
    "created_at": "2009-12-09T06:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62795",
    "user": "was"
}
```

merged in sagenb-0.4.6



---

archive/issue_comments_062796.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T06:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62796",
    "user": "was"
}
```

Resolution: fixed
