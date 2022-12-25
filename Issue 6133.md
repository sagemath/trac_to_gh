# Issue 6133: [with patch, needs review] remove pbuild files in devel/sage

archive/issues_006133.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @mwhansen\n\nThree pbuild files still live in `devel/sage`, but are clearly out of date and need to be removed. The patch just removes all three.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6133\n\n",
    "created_at": "2009-05-26T18:31:22Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] remove pbuild files in devel/sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6133",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

CC:  @mwhansen

Three pbuild files still live in `devel/sage`, but are clearly out of date and need to be removed. The patch just removes all three.

Issue created by migration from https://trac.sagemath.org/ticket/6133





---

archive/issue_comments_048892.json:
```json
{
    "body": "New patch -- cleans up `MANIFEST.in`, too.",
    "created_at": "2009-05-26T23:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6133#issuecomment-48892",
    "user": "https://github.com/craigcitro"
}
```

New patch -- cleans up `MANIFEST.in`, too.



---

archive/issue_comments_048893.json:
```json
{
    "body": "No hurry, so this should go in 4.0.1.  But I also read it, and it's a positive review.",
    "created_at": "2009-05-28T07:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6133#issuecomment-48893",
    "user": "https://github.com/williamstein"
}
```

No hurry, so this should go in 4.0.1.  But I also read it, and it's a positive review.



---

archive/issue_comments_048894.json:
```json
{
    "body": "I get these failures when applying:\n\n\n```\napplying trac-6133.patch\nunable to find 'build.py' for patching\n1 out of 1 hunks FAILED -- saving rejects to file build.py.rej\nunable to find 'clib.py' for patching\n1 out of 1 hunks FAILED -- saving rejects to file clib.py.rej\nunable to find 'sagebuild.py' for patching\n1 out of 1 hunks FAILED -- saving rejects to file sagebuild.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh trac-6133.patch\n\n```\n",
    "created_at": "2009-05-28T07:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6133#issuecomment-48894",
    "user": "https://github.com/mwhansen"
}
```

I get these failures when applying:


```
applying trac-6133.patch
unable to find 'build.py' for patching
1 out of 1 hunks FAILED -- saving rejects to file build.py.rej
unable to find 'clib.py' for patching
1 out of 1 hunks FAILED -- saving rejects to file clib.py.rej
unable to find 'sagebuild.py' for patching
1 out of 1 hunks FAILED -- saving rejects to file sagebuild.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac-6133.patch

```




---

archive/issue_comments_048895.json:
```json
{
    "body": "Attachment [trac-6133.patch](tarball://root/attachments/some-uuid/ticket6133/trac-6133.patch) by @craigcitro created at 2009-05-28 08:26:32",
    "created_at": "2009-05-28T08:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6133#issuecomment-48895",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-6133.patch](tarball://root/attachments/some-uuid/ticket6133/trac-6133.patch) by @craigcitro created at 2009-05-28 08:26:32



---

archive/issue_comments_048896.json:
```json
{
    "body": "I was stupid -- the patch file had two copies of the same patch appended to one another. This works.",
    "created_at": "2009-05-28T08:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6133#issuecomment-48896",
    "user": "https://github.com/craigcitro"
}
```

I was stupid -- the patch file had two copies of the same patch appended to one another. This works.



---

archive/issue_comments_048897.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-28T19:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6133#issuecomment-48897",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_048898.json:
```json
{
    "body": "The new patch works.\n\nMerged in 4.0.rc2.",
    "created_at": "2009-05-28T19:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6133#issuecomment-48898",
    "user": "https://github.com/mwhansen"
}
```

The new patch works.

Merged in 4.0.rc2.
