# Issue 8669: interrupting download in sage-spkg should delete the spkg file

archive/issues_008669.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  leif\n\nIf you run `sage-spkg PKG_NAME` and hit ctrl-c during downloading, you end up with a partial spkg file.  Then if you run `sage-spkg PKG_NAME` again, it just opens up that file and then crashes because the file is incomplete.\n\nThe attached patch attempts to fix this.  It seems to work, deleting the partially downloaded file, but for reasons I don't understand, it's not printing any of the accompanying messages.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8669\n\n",
    "created_at": "2010-04-10T18:56:51Z",
    "labels": [
        "packages: optional",
        "minor",
        "bug"
    ],
    "title": "interrupting download in sage-spkg should delete the spkg file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8669",
    "user": "jhpalmieri"
}
```
Assignee: tbd

CC:  leif

If you run `sage-spkg PKG_NAME` and hit ctrl-c during downloading, you end up with a partial spkg file.  Then if you run `sage-spkg PKG_NAME` again, it just opens up that file and then crashes because the file is incomplete.

The attached patch attempts to fix this.  It seems to work, deleting the partially downloaded file, but for reasons I don't understand, it's not printing any of the accompanying messages.


Issue created by migration from https://trac.sagemath.org/ticket/8669





---

archive/issue_comments_078877.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-10T18:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78877",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078878.json:
```json
{
    "body": "I'm marking this as \"needs review\", but if anyone can fix the printing problem mentioned in the summary, that would be great.",
    "created_at": "2010-04-10T18:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78878",
    "user": "jhpalmieri"
}
```

I'm marking this as "needs review", but if anyone can fix the printing problem mentioned in the summary, that would be great.



---

archive/issue_comments_078879.json:
```json
{
    "body": "The reason for the \"non-printing\" is simple:\n\nIn `local/bin/sage-sage`, the output of `sage-spkg` is piped to `tee`, which is run from the same subshell and so gets the same signal.\n\n(`sage-spkg` *does* print the messages, but `tee` *does not* \"wait\" for the *post-*`Ctrl-C` output.)",
    "created_at": "2010-04-10T20:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78879",
    "user": "leif"
}
```

The reason for the "non-printing" is simple:

In `local/bin/sage-sage`, the output of `sage-spkg` is piped to `tee`, which is run from the same subshell and so gets the same signal.

(`sage-spkg` *does* print the messages, but `tee` *does not* "wait" for the *post-*`Ctrl-C` output.)



---

archive/issue_comments_078880.json:
```json
{
    "body": "Replying to [comment:2 leif]:\n> The reason for the \"non-printing\" is simple:\n> \n> In `local/bin/sage-sage`, the output of `sage-spkg` is piped to `tee`, which is run from the same subshell and so gets the same signal.\n\nAny ideas how to fix this?  I tried using \"pipestatus\" from #8306, but it doesn't seem to help: when I hit ctrl-C, it prints \n\n```\n[..^Cclose failed in file object destructor:\nError in sys.excepthook:\n\nOriginal exception was:\n```\n",
    "created_at": "2010-04-10T22:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78880",
    "user": "jhpalmieri"
}
```

Replying to [comment:2 leif]:
> The reason for the "non-printing" is simple:
> 
> In `local/bin/sage-sage`, the output of `sage-spkg` is piped to `tee`, which is run from the same subshell and so gets the same signal.

Any ideas how to fix this?  I tried using "pipestatus" from #8306, but it doesn't seem to help: when I hit ctrl-C, it prints 

```
[..^Cclose failed in file object destructor:
Error in sys.excepthook:

Original exception was:
```




---

archive/issue_comments_078881.json:
```json
{
    "body": "Okay, here's a new patch without any printing problems.",
    "created_at": "2010-04-10T23:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78881",
    "user": "jhpalmieri"
}
```

Okay, here's a new patch without any printing problems.



---

archive/issue_comments_078882.json:
```json
{
    "body": "scripts repo",
    "created_at": "2010-04-10T23:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78882",
    "user": "jhpalmieri"
}
```

scripts repo



---

archive/issue_comments_078883.json:
```json
{
    "body": "Attachment [trac_8669-download.2.patch](tarball://root/attachments/some-uuid/ticket8669/trac_8669-download.2.patch) by jhpalmieri created at 2010-04-10 23:46:55\n\nscripts repo",
    "created_at": "2010-04-10T23:46:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78883",
    "user": "jhpalmieri"
}
```

Attachment [trac_8669-download.2.patch](tarball://root/attachments/some-uuid/ticket8669/trac_8669-download.2.patch) by jhpalmieri created at 2010-04-10 23:46:55

scripts repo



---

archive/issue_comments_078884.json:
```json
{
    "body": "Attachment [trac_8669-download.patch](tarball://root/attachments/some-uuid/ticket8669/trac_8669-download.patch) by jhpalmieri created at 2010-04-10 23:47:11\n\nscripts repo (same as other patch)",
    "created_at": "2010-04-10T23:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78884",
    "user": "jhpalmieri"
}
```

Attachment [trac_8669-download.patch](tarball://root/attachments/some-uuid/ticket8669/trac_8669-download.patch) by jhpalmieri created at 2010-04-10 23:47:11

scripts repo (same as other patch)



---

archive/issue_comments_078885.json:
```json
{
    "body": "Attachment [trac_8669-download.3.patch](tarball://root/attachments/some-uuid/ticket8669/trac_8669-download.3.patch) by jhpalmieri created at 2010-04-10 23:47:47\n\nTo the release manager: please delete all but \"trac_8669-download.patch\".",
    "created_at": "2010-04-10T23:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78885",
    "user": "jhpalmieri"
}
```

Attachment [trac_8669-download.3.patch](tarball://root/attachments/some-uuid/ticket8669/trac_8669-download.3.patch) by jhpalmieri created at 2010-04-10 23:47:47

To the release manager: please delete all but "trac_8669-download.patch".



---

archive/issue_comments_078886.json:
```json
{
    "body": "Works as advertised. Positive review.",
    "created_at": "2010-04-18T08:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78886",
    "user": "timdumol"
}
```

Works as advertised. Positive review.



---

archive/issue_comments_078887.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-18T08:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78887",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078888.json:
```json
{
    "body": "Merged \"trac_8669-download.patch\" into 4.4.alpha1.",
    "created_at": "2010-04-19T05:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78888",
    "user": "jhpalmieri"
}
```

Merged "trac_8669-download.patch" into 4.4.alpha1.



---

archive/issue_comments_078889.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8669#issuecomment-78889",
    "user": "jhpalmieri"
}
```

Resolution: fixed
