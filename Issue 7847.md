# Issue 7847: Emptying the trash in Firefox 3.5.6 displays a "Forbidden  No referer found. Forbidden." page

archive/issues_007847.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein @TimDumol @jhpalmieri @jasongrout\n\nThis is also a problem in IE8 on Windows XP.\n\nThis is a follow-up to #5100.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7847\n\n",
    "created_at": "2010-01-05T03:41:39Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Emptying the trash in Firefox 3.5.6 displays a \"Forbidden  No referer found. Forbidden.\" page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7847",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @williamstein @TimDumol @jhpalmieri @jasongrout

This is also a problem in IE8 on Windows XP.

This is a follow-up to #5100.

Issue created by migration from https://trac.sagemath.org/ticket/7847





---

archive/issue_comments_067853.json:
```json
{
    "body": "Attachment [trac_7847-empty_trash_ie_ff.patch](tarball://root/attachments/some-uuid/ticket7847/trac_7847-empty_trash_ie_ff.patch) by @qed777 created at 2010-01-05 03:57:59\n\n\"No referer\" workaround.  sagenb repo.",
    "created_at": "2010-01-05T03:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67853",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7847-empty_trash_ie_ff.patch](tarball://root/attachments/some-uuid/ticket7847/trac_7847-empty_trash_ie_ff.patch) by @qed777 created at 2010-01-05 03:57:59

"No referer" workaround.  sagenb repo.



---

archive/issue_comments_067854.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-05T04:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67854",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067855.json:
```json
{
    "body": "The patch works for me and should not affect browsers that do include the referer.  I don't know if we can use just the workaround for all browsers.",
    "created_at": "2010-01-05T04:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67855",
    "user": "https://github.com/qed777"
}
```

The patch works for me and should not affect browsers that do include the referer.  I don't know if we can use just the workaround for all browsers.



---

archive/issue_events_018760.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-01-05T04:02:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "milestone": "sage-4.3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7847#event-18760"
}
```



---

archive/issue_comments_067856.json:
```json
{
    "body": "Makes Worksheet_emptytrash accept only POST requests, and adds the requisite form.",
    "created_at": "2010-01-17T19:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67856",
    "user": "https://github.com/TimDumol"
}
```

Makes Worksheet_emptytrash accept only POST requests, and adds the requisite form.



---

archive/issue_comments_067857.json:
```json
{
    "body": "Attachment [trac_7847-empty-trash-no-referer.patch](tarball://root/attachments/some-uuid/ticket7847/trac_7847-empty-trash-no-referer.patch) by @TimDumol created at 2010-01-17 19:13:27\n\nGood job fixing the problem, but unfortunately your patch means anyone can cause you to empty your trash.\n\nThe reason for the HTTP-Referer check was actually security. Without it, anyone could have sent you a link to http://localhost:8000/emptytrash (or http://sagenb.org/emptytrash) and empty one's trash. This was clearly the wrong approach though.\n\nThis new patch accepts only POST requests, which should be much more secure.",
    "created_at": "2010-01-17T19:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67857",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7847-empty-trash-no-referer.patch](tarball://root/attachments/some-uuid/ticket7847/trac_7847-empty-trash-no-referer.patch) by @TimDumol created at 2010-01-17 19:13:27

Good job fixing the problem, but unfortunately your patch means anyone can cause you to empty your trash.

The reason for the HTTP-Referer check was actually security. Without it, anyone could have sent you a link to http://localhost:8000/emptytrash (or http://sagenb.org/emptytrash) and empty one's trash. This was clearly the wrong approach though.

This new patch accepts only POST requests, which should be much more secure.



---

archive/issue_comments_067858.json:
```json
{
    "body": "Great catch.  That's definitely the way to go.  I've checked that this works in multiple browsers on Linux and Windows XP.\n\nTo the release manager: Apply only [attachment:trac_7847-empty-trash-no-referer.patch]",
    "created_at": "2010-01-18T05:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67858",
    "user": "https://github.com/qed777"
}
```

Great catch.  That's definitely the way to go.  I've checked that this works in multiple browsers on Linux and Windows XP.

To the release manager: Apply only [attachment:trac_7847-empty-trash-no-referer.patch]



---

archive/issue_comments_067859.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T05:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67859",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_018761.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:31:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7847#event-18761"
}
```



---

archive/issue_comments_067860.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67860",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed
