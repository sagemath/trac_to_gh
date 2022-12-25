# Issue 4196: write a new coercion section for the developer's/programmer's guide

archive/issues_004196.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: coercion, documentation\n\nThe coercion section of the developer's guide is completely out of date and needs to be rewritten.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4196\n\n",
    "created_at": "2008-09-25T21:58:29Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "write a new coercion section for the developer's/programmer's guide",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4196",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: somebody

Keywords: coercion, documentation

The coercion section of the developer's guide is completely out of date and needs to be rewritten.



Issue created by migration from https://trac.sagemath.org/ticket/4196





---

archive/issue_comments_030392.json:
```json
{
    "body": "See also #4272.",
    "created_at": "2008-10-13T17:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4196#issuecomment-30392",
    "user": "https://github.com/jhpalmieri"
}
```

See also #4272.



---

archive/issue_comments_030393.json:
```json
{
    "body": "See also Robert Bradshaw's coercion docs on the [Sage wiki](http://wiki.sagemath.org/coercion).",
    "created_at": "2009-02-14T21:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4196#issuecomment-30393",
    "user": "https://github.com/jhpalmieri"
}
```

See also Robert Bradshaw's coercion docs on the [Sage wiki](http://wiki.sagemath.org/coercion).



---

archive/issue_comments_030394.json:
```json
{
    "body": "Changing assignee from somebody to @jhpalmieri.",
    "created_at": "2009-06-17T22:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4196#issuecomment-30394",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from somebody to @jhpalmieri.



---

archive/issue_comments_030395.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-17T22:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4196#issuecomment-30395",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030396.json:
```json
{
    "body": "Attachment [trac_4196.patch](tarball://root/attachments/some-uuid/ticket4196/trac_4196.patch) by @jhpalmieri created at 2009-06-17 22:03:27\n\nHere's a patch.  This basically just refers to the coercion section in the reference manual, added in #5454.",
    "created_at": "2009-06-17T22:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4196#issuecomment-30396",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4196.patch](tarball://root/attachments/some-uuid/ticket4196/trac_4196.patch) by @jhpalmieri created at 2009-06-17 22:03:27

Here's a patch.  This basically just refers to the coercion section in the reference manual, added in #5454.



---

archive/issue_comments_030397.json:
```json
{
    "body": "rebased against Sage 4.0.2",
    "created_at": "2009-06-19T23:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4196#issuecomment-30397",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

rebased against Sage 4.0.2



---

archive/issue_comments_030398.json:
```json
{
    "body": "Attachment [trac_4196.2.patch](tarball://root/attachments/some-uuid/ticket4196/trac_4196.2.patch) by mvngu created at 2009-06-19 23:10:20\n\nWhen applying the patch `trac_4196.patch` against Sage 4.0.2, I received one hunk failure:\n\n```\nsage: hg_sage.apply(\"http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4196/trac_4196.patch\")\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4196/trac_4196.patch\nLoading: [..]\ncd \"/scratch/mvngu/sage-4.0.2/devel/sage\" && hg status\ncd \"/scratch/mvngu/sage-4.0.2/devel/sage\" && hg status\ncd \"/scratch/mvngu/sage-4.0.2/devel/sage\" && hg import   \"/home/mvngu/.sage/temp/sage.math.washington.edu/5611/tmp_1.patch\"\napplying /home/mvngu/.sage/temp/sage.math.washington.edu/5611/tmp_1.patch\npatching file doc/en/reference/coercion.rst\nHunk #3 FAILED at 244\n1 out of 3 hunks FAILED -- saving rejects to file doc/en/reference/coercion.rst.rej\nabort: patch failed to apply\n```\n\nThe patch `trac_4196.2.patch` is a rebase against Sage 4.0.2. It turns out that the cause of the failure was line 248 in the first patch. So the only difference between `trac_4196.patch` and `trac_4196.2.patch` is that in `trac_4196.2.patch` I left out line 248 in the original patch. Apart from the rebase, positive review.",
    "created_at": "2009-06-19T23:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4196#issuecomment-30398",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_4196.2.patch](tarball://root/attachments/some-uuid/ticket4196/trac_4196.2.patch) by mvngu created at 2009-06-19 23:10:20

When applying the patch `trac_4196.patch` against Sage 4.0.2, I received one hunk failure:

```
sage: hg_sage.apply("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4196/trac_4196.patch")
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4196/trac_4196.patch
Loading: [..]
cd "/scratch/mvngu/sage-4.0.2/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.0.2/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.0.2/devel/sage" && hg import   "/home/mvngu/.sage/temp/sage.math.washington.edu/5611/tmp_1.patch"
applying /home/mvngu/.sage/temp/sage.math.washington.edu/5611/tmp_1.patch
patching file doc/en/reference/coercion.rst
Hunk #3 FAILED at 244
1 out of 3 hunks FAILED -- saving rejects to file doc/en/reference/coercion.rst.rej
abort: patch failed to apply
```

The patch `trac_4196.2.patch` is a rebase against Sage 4.0.2. It turns out that the cause of the failure was line 248 in the first patch. So the only difference between `trac_4196.patch` and `trac_4196.2.patch` is that in `trac_4196.2.patch` I left out line 248 in the original patch. Apart from the rebase, positive review.



---

archive/issue_comments_030399.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T09:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4196#issuecomment-30399",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_009515.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-06-24T09:48:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4196",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4196#event-9515"
}
```



---

archive/issue_comments_030400.json:
```json
{
    "body": "Yes, you beat me to it, but positive review from me too.",
    "created_at": "2009-06-25T10:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4196#issuecomment-30400",
    "user": "https://github.com/robertwb"
}
```

Yes, you beat me to it, but positive review from me too.
