# Issue 7455: SageNB - Searching on Log page does not work.

archive/issues_007455.json:
```json
{
    "body": "Assignee: @aghitza\n\nSearching for anything on the Log page does not work due to missing javascript libraries.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7455\n\n",
    "created_at": "2009-11-13T20:28:26Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "SageNB - Searching on Log page does not work.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7455",
    "user": "https://github.com/TimDumol"
}
```
Assignee: @aghitza

Searching for anything on the Log page does not work due to missing javascript libraries.

Issue created by migration from https://trac.sagemath.org/ticket/7455





---

archive/issue_comments_062672.json:
```json
{
    "body": "Changing component from algebra to notebook.",
    "created_at": "2009-11-13T22:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62672",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to notebook.



---

archive/issue_events_017682.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2009-11-13T22:20:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7455#event-17682"
}
```



---

archive/issue_comments_062673.json:
```json
{
    "body": "Changing assignee from @aghitza to boothby.",
    "created_at": "2009-11-13T22:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62673",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @aghitza to boothby.



---

archive/issue_comments_062674.json:
```json
{
    "body": "Attachment [trac_7455-searching-on-log-page.patch](tarball://root/attachments/some-uuid/ticket7455/trac_7455-searching-on-log-page.patch) by @TimDumol created at 2009-11-13 23:31:29\n\nThis remvoes the search bar from the history page and updates the tests to reflect that.",
    "created_at": "2009-11-13T23:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62674",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7455-searching-on-log-page.patch](tarball://root/attachments/some-uuid/ticket7455/trac_7455-searching-on-log-page.patch) by @TimDumol created at 2009-11-13 23:31:29

This remvoes the search bar from the history page and updates the tests to reflect that.



---

archive/issue_comments_062675.json:
```json
{
    "body": "The problem is apparently a bit harder to fix. It requires a few changes to the js libraries. For now, this patch is a temporary fix.",
    "created_at": "2009-11-13T23:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62675",
    "user": "https://github.com/TimDumol"
}
```

The problem is apparently a bit harder to fix. It requires a few changes to the js libraries. For now, this patch is a temporary fix.



---

archive/issue_comments_062676.json:
```json
{
    "body": "I have thought over this, and it seems to me that it makes more sense to keep the search box only in the worksheet list pages (Home and Published). If there are no objections, then the previous patch removing the search box should be the one included.",
    "created_at": "2009-11-15T02:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62676",
    "user": "https://github.com/TimDumol"
}
```

I have thought over this, and it seems to me that it makes more sense to keep the search box only in the worksheet list pages (Home and Published). If there are no objections, then the previous patch removing the search box should be the one included.



---

archive/issue_comments_062677.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-15T02:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62677",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062678.json:
```json
{
    "body": "I agree with this patch.  It would of course be better to just get rid of the whole top bar, and make all the cells be properly styled, etc.   But this current patch is very simple at and at least fixes this bug.  Positive review.",
    "created_at": "2009-12-08T21:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62678",
    "user": "https://github.com/williamstein"
}
```

I agree with this patch.  It would of course be better to just get rid of the whole top bar, and make all the cells be properly styled, etc.   But this current patch is very simple at and at least fixes this bug.  Positive review.



---

archive/issue_comments_062679.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T21:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62679",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062680.json:
```json
{
    "body": "merged in sagenb-0.4.6",
    "created_at": "2009-12-09T06:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62680",
    "user": "https://github.com/williamstein"
}
```

merged in sagenb-0.4.6



---

archive/issue_comments_062681.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T06:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7455#issuecomment-62681",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_017683.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-09T06:32:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7455",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7455#event-17683"
}
```
