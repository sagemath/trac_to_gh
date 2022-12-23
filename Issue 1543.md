# Issue 1543: rpy build fails if "tail -1" doesn't work

archive/issues_001543.json:
```json
{
    "body": "Assignee: craigcitro\n\nAgain, the title says it all -- on some systems (like mine), tail -1 produces an error (since this is supposedly \"deprecated\" behavior), recommending that the user use tail -n 1 instead. rpy fails after that; fixing this, everything works fine. I've added one more file to the patches/ directory, and one more line to the spkg-install (namely, copying that file over). \n\nIssue created by migration from https://trac.sagemath.org/ticket/1543\n\n",
    "created_at": "2007-12-17T02:56:50Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "title": "rpy build fails if \"tail -1\" doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1543",
    "user": "craigcitro"
}
```
Assignee: craigcitro

Again, the title says it all -- on some systems (like mine), tail -1 produces an error (since this is supposedly "deprecated" behavior), recommending that the user use tail -n 1 instead. rpy fails after that; fixing this, everything works fine. I've added one more file to the patches/ directory, and one more line to the spkg-install (namely, copying that file over). 

Issue created by migration from https://trac.sagemath.org/ticket/1543





---

archive/issue_comments_009853.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-17T02:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1543#issuecomment-9853",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_009854.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-17T02:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1543#issuecomment-9854",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009855.json:
```json
{
    "body": "Attachment\n\nAs mabshoff pointed out, this spkg name should probably get updated, since changes were made, and so I've added rpy-1.0.1.p0.spkg ... I'm also putting up a new patch for 1542, which will know about this new filename. (It has to appear in the r spkg-install, so these two should be handled simultaneously.)",
    "created_at": "2007-12-17T04:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1543#issuecomment-9855",
    "user": "craigcitro"
}
```

Attachment

As mabshoff pointed out, this spkg name should probably get updated, since changes were made, and so I've added rpy-1.0.1.p0.spkg ... I'm also putting up a new patch for 1542, which will know about this new filename. (It has to appear in the r spkg-install, so these two should be handled simultaneously.)



---

archive/issue_comments_009856.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-18T02:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1543#issuecomment-9856",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_009857.json:
```json
{
    "body": "Merged in 2.9.1.alpha1",
    "created_at": "2007-12-18T02:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1543#issuecomment-9857",
    "user": "rlm"
}
```

Merged in 2.9.1.alpha1
