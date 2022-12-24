# Issue 7847: Emptying the trash in Firefox 3.5.6 displays a "Forbidden  No referer found. Forbidden." page

archive/issues_007847.json:
```json
{
    "body": "Assignee: was\n\nCC:  was timdumol jhpalmieri jason\n\nThis is also a problem in IE8 on Windows XP.\n\nThis is a follow-up to #5100.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7847\n\n",
    "created_at": "2010-01-05T03:41:39Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Emptying the trash in Firefox 3.5.6 displays a \"Forbidden  No referer found. Forbidden.\" page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7847",
    "user": "mpatel"
}
```
Assignee: was

CC:  was timdumol jhpalmieri jason

This is also a problem in IE8 on Windows XP.

This is a follow-up to #5100.

Issue created by migration from https://trac.sagemath.org/ticket/7847





---

archive/issue_comments_067970.json:
```json
{
    "body": "Attachment [trac_7847-empty_trash_ie_ff.patch](tarball://root/attachments/some-uuid/ticket7847/trac_7847-empty_trash_ie_ff.patch) by mpatel created at 2010-01-05 03:57:59\n\n\"No referer\" workaround.  sagenb repo.",
    "created_at": "2010-01-05T03:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67970",
    "user": "mpatel"
}
```

Attachment [trac_7847-empty_trash_ie_ff.patch](tarball://root/attachments/some-uuid/ticket7847/trac_7847-empty_trash_ie_ff.patch) by mpatel created at 2010-01-05 03:57:59

"No referer" workaround.  sagenb repo.



---

archive/issue_comments_067971.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-05T04:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67971",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067972.json:
```json
{
    "body": "The patch works for me and should not affect browsers that do include the referer.  I don't know if we can use just the workaround for all browsers.",
    "created_at": "2010-01-05T04:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67972",
    "user": "mpatel"
}
```

The patch works for me and should not affect browsers that do include the referer.  I don't know if we can use just the workaround for all browsers.



---

archive/issue_comments_067973.json:
```json
{
    "body": "Makes Worksheet_emptytrash accept only POST requests, and adds the requisite form.",
    "created_at": "2010-01-17T19:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67973",
    "user": "timdumol"
}
```

Makes Worksheet_emptytrash accept only POST requests, and adds the requisite form.



---

archive/issue_comments_067974.json:
```json
{
    "body": "Attachment [trac_7847-empty-trash-no-referer.patch](tarball://root/attachments/some-uuid/ticket7847/trac_7847-empty-trash-no-referer.patch) by timdumol created at 2010-01-17 19:13:27\n\nGood job fixing the problem, but unfortunately your patch means anyone can cause you to empty your trash.\n\nThe reason for the HTTP-Referer check was actually security. Without it, anyone could have sent you a link to http://localhost:8000/emptytrash (or http://sagenb.org/emptytrash) and empty one's trash. This was clearly the wrong approach though.\n\nThis new patch accepts only POST requests, which should be much more secure.",
    "created_at": "2010-01-17T19:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67974",
    "user": "timdumol"
}
```

Attachment [trac_7847-empty-trash-no-referer.patch](tarball://root/attachments/some-uuid/ticket7847/trac_7847-empty-trash-no-referer.patch) by timdumol created at 2010-01-17 19:13:27

Good job fixing the problem, but unfortunately your patch means anyone can cause you to empty your trash.

The reason for the HTTP-Referer check was actually security. Without it, anyone could have sent you a link to http://localhost:8000/emptytrash (or http://sagenb.org/emptytrash) and empty one's trash. This was clearly the wrong approach though.

This new patch accepts only POST requests, which should be much more secure.



---

archive/issue_comments_067975.json:
```json
{
    "body": "Great catch.  That's definitely the way to go.  I've checked that this works in multiple browsers on Linux and Windows XP.\n\nTo the release manager: Apply only [attachment:trac_7847-empty-trash-no-referer.patch]",
    "created_at": "2010-01-18T05:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67975",
    "user": "mpatel"
}
```

Great catch.  That's definitely the way to go.  I've checked that this works in multiple browsers on Linux and Windows XP.

To the release manager: Apply only [attachment:trac_7847-empty-trash-no-referer.patch]



---

archive/issue_comments_067976.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T05:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67976",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067977.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7847#issuecomment-67977",
    "user": "timdumol"
}
```

Resolution: fixed
