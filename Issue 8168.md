# Issue 8168: Keyword option to keep reset() from detaching all attached files

archive/issues_008168.json:
```json
{
    "body": "Assignee: tbd\n\nWith this option, one can put `reset(attached=False)` at the top of an attached file.  This resets the global variables and interfaces but not the list of attached files.  Otherwise, the file detaches itself.\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/7a43d2944dc35674#).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8168\n\n",
    "created_at": "2010-02-03T09:58:21Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "Keyword option to keep reset() from detaching all attached files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8168",
    "user": "@qed777"
}
```
Assignee: tbd

With this option, one can put `reset(attached=False)` at the top of an attached file.  This resets the global variables and interfaces but not the list of attached files.  Otherwise, the file detaches itself.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/7a43d2944dc35674#).

Issue created by migration from https://trac.sagemath.org/ticket/8168





---

archive/issue_comments_071868.json:
```json
{
    "body": "Add keyword option `attached=True` to `reset`.  sage repo.",
    "created_at": "2010-02-03T10:00:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71868",
    "user": "@qed777"
}
```

Add keyword option `attached=True` to `reset`.  sage repo.



---

archive/issue_comments_071869.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T10:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71869",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071870.json:
```json
{
    "body": "Attachment [trac_8168-attached_reset.patch](tarball://root/attachments/some-uuid/ticket8168/trac_8168-attached_reset.patch) by @qed777 created at 2010-02-03 10:05:54",
    "created_at": "2010-02-03T10:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71870",
    "user": "@qed777"
}
```

Attachment [trac_8168-attached_reset.patch](tarball://root/attachments/some-uuid/ticket8168/trac_8168-attached_reset.patch) by @qed777 created at 2010-02-03 10:05:54



---

archive/issue_comments_071871.json:
```json
{
    "body": "V2 makes the `attached=False` the default.",
    "created_at": "2010-02-03T10:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71871",
    "user": "@qed777"
}
```

V2 makes the `attached=False` the default.



---

archive/issue_comments_071872.json:
```json
{
    "body": "Same as previous, except with default `attached=False`.  Apply just one patch.",
    "created_at": "2010-02-03T10:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71872",
    "user": "@qed777"
}
```

Same as previous, except with default `attached=False`.  Apply just one patch.



---

archive/issue_comments_071873.json:
```json
{
    "body": "Attachment [trac_8168-attached_reset.2.patch](tarball://root/attachments/some-uuid/ticket8168/trac_8168-attached_reset.2.patch) by @qed777 created at 2010-02-03 10:39:46\n\nNote: With V2, attaching a file that contains `reset(attached=True)` does not immediately detach the file.  This happens because `sage.misc.preparser.load` `exec`s the file *before* updating the attached files dictionary.",
    "created_at": "2010-02-03T10:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71873",
    "user": "@qed777"
}
```

Attachment [trac_8168-attached_reset.2.patch](tarball://root/attachments/some-uuid/ticket8168/trac_8168-attached_reset.2.patch) by @qed777 created at 2010-02-03 10:39:46

Note: With V2, attaching a file that contains `reset(attached=True)` does not immediately detach the file.  This happens because `sage.misc.preparser.load` `exec`s the file *before* updating the attached files dictionary.



---

archive/issue_comments_071874.json:
```json
{
    "body": "V2 rebased for #378.  Apply only this patch.",
    "created_at": "2010-02-16T21:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71874",
    "user": "@qed777"
}
```

V2 rebased for #378.  Apply only this patch.



---

archive/issue_comments_071875.json:
```json
{
    "body": "Attachment [trac_8168-attached_reset.3.patch](tarball://root/attachments/some-uuid/ticket8168/trac_8168-attached_reset.3.patch) by @qed777 created at 2010-02-16 21:58:16\n\nV3 is V2 rebased for #378.",
    "created_at": "2010-02-16T21:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71875",
    "user": "@qed777"
}
```

Attachment [trac_8168-attached_reset.3.patch](tarball://root/attachments/some-uuid/ticket8168/trac_8168-attached_reset.3.patch) by @qed777 created at 2010-02-16 21:58:16

V3 is V2 rebased for #378.



---

archive/issue_comments_071876.json:
```json
{
    "body": "Note to potential reviewers:  V2 of the patch should apply cleanly to 4.4.4.alpha1.  V3 is based on #378, but that ticket needs work.",
    "created_at": "2010-06-23T01:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71876",
    "user": "@qed777"
}
```

Note to potential reviewers:  V2 of the patch should apply cleanly to 4.4.4.alpha1.  V3 is based on #378, but that ticket needs work.



---

archive/issue_comments_071877.json:
```json
{
    "body": "Attachment [trac_8168-attached_reset.4.patch](tarball://root/attachments/some-uuid/ticket8168/trac_8168-attached_reset.4.patch) by @mwhansen created at 2011-12-18 10:19:11",
    "created_at": "2011-12-18T10:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71877",
    "user": "@mwhansen"
}
```

Attachment [trac_8168-attached_reset.4.patch](tarball://root/attachments/some-uuid/ticket8168/trac_8168-attached_reset.4.patch) by @mwhansen created at 2011-12-18 10:19:11



---

archive/issue_comments_071878.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-18T10:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71878",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071879.json:
```json
{
    "body": "I rebased this and think it looks okay.  Apply only  trac_8168-attached_reset.4.patch.",
    "created_at": "2011-12-18T10:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71879",
    "user": "@mwhansen"
}
```

I rebased this and think it looks okay.  Apply only  trac_8168-attached_reset.4.patch.



---

archive/issue_comments_071880.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-12-22T13:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8168#issuecomment-71880",
    "user": "@jdemeyer"
}
```

Resolution: fixed
