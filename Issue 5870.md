# Issue 5870: Detect blas and atlas libraries for linbox on FreeBSD

archive/issues_005870.json:
```json
{
    "body": "Assignee: mabshoff\n\nspkg-install for linbox uses OS-specific code to detect and use the BLAS and Atlas libraries.  Add code to support FreeBSD.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5870\n\n",
    "created_at": "2009-04-23T07:12:05Z",
    "labels": [
        "porting: BSD",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Detect blas and atlas libraries for linbox on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5870",
    "user": "@peterjeremy"
}
```
Assignee: mabshoff

spkg-install for linbox uses OS-specific code to detect and use the BLAS and Atlas libraries.  Add code to support FreeBSD.

Issue created by migration from https://trac.sagemath.org/ticket/5870





---

archive/issue_comments_046364.json:
```json
{
    "body": "Attachment [linbox-1.1.6.patch](tarball://root/attachments/some-uuid/ticket5870/linbox-1.1.6.patch) by @peterjeremy created at 2009-04-23 07:12:14",
    "created_at": "2009-04-23T07:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5870#issuecomment-46364",
    "user": "@peterjeremy"
}
```

Attachment [linbox-1.1.6.patch](tarball://root/attachments/some-uuid/ticket5870/linbox-1.1.6.patch) by @peterjeremy created at 2009-04-23 07:12:14



---

archive/issue_comments_046365.json:
```json
{
    "body": "I will work on integrating this tomorrow.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T07:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5870#issuecomment-46365",
    "user": "mabshoff"
}
```

I will work on integrating this tomorrow.

Cheers,

Michael



---

archive/issue_comments_046366.json:
```json
{
    "body": "Looks good to me.\n\nAn spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/linbox-1.1.6.p0.spkg",
    "created_at": "2009-06-20T07:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5870#issuecomment-46366",
    "user": "@mwhansen"
}
```

Looks good to me.

An spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/linbox-1.1.6.p0.spkg



---

archive/issue_comments_046367.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-06-20T07:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5870#issuecomment-46367",
    "user": "@mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_046368.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T07:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5870#issuecomment-46368",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046369.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T22:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5870#issuecomment-46369",
    "user": "@rlmill"
}
```

Resolution: fixed
