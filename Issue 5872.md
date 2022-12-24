# Issue 5872: [with patch, needs review] Explicitly pass -fPIC into ntl shared object build.

archive/issues_005872.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe ntl makefile appears to rely on compiler flags specified as a target dependency being passed to the compiler.  This fails on at least FreeBSD, resulting in an attempt to include non-PIC objects in a shared library.\n\nInstead, explicitly pass -fPIC to the sub-make used for the shared object build.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5872\n\n",
    "created_at": "2009-04-23T08:06:35Z",
    "labels": [
        "porting: BSD",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, needs review] Explicitly pass -fPIC into ntl shared object build.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5872",
    "user": "pjeremy"
}
```
Assignee: mabshoff

The ntl makefile appears to rely on compiler flags specified as a target dependency being passed to the compiler.  This fails on at least FreeBSD, resulting in an attempt to include non-PIC objects in a shared library.

Instead, explicitly pass -fPIC to the sub-make used for the shared object build.


Issue created by migration from https://trac.sagemath.org/ticket/5872





---

archive/issue_comments_046373.json:
```json
{
    "body": "Attachment [ntl-5.4.2.p6.patch](tarball://root/attachments/some-uuid/ticket5872/ntl-5.4.2.p6.patch) by mhansen created at 2009-06-20 07:13:30\n\nLooks good to me.\n\nThe spkg incorporating this patch can be found at http://sage.math.washington.edu/home/mhansen/ntl-5.4.2.p8.spkg",
    "created_at": "2009-06-20T07:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5872#issuecomment-46373",
    "user": "mhansen"
}
```

Attachment [ntl-5.4.2.p6.patch](tarball://root/attachments/some-uuid/ticket5872/ntl-5.4.2.p6.patch) by mhansen created at 2009-06-20 07:13:30

Looks good to me.

The spkg incorporating this patch can be found at http://sage.math.washington.edu/home/mhansen/ntl-5.4.2.p8.spkg



---

archive/issue_comments_046374.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T07:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5872#issuecomment-46374",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046375.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2009-06-20T07:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5872#issuecomment-46375",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_046376.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T22:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5872#issuecomment-46376",
    "user": "rlm"
}
```

Resolution: fixed
