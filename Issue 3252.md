# Issue 3252: add kbase functionality to libsingular

archive/issues_003252.json:
```json
{
    "body": "Assignee: @williamstein\n\nimplemented a cython wrapper for singular's kbase command. This is significantly faster than doing singular.kbase() because it doesn't have the pexpect overhead. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3252\n\n",
    "created_at": "2008-05-18T03:35:33Z",
    "labels": [
        "algebraic geometry",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "add kbase functionality to libsingular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3252",
    "user": "@yqiang"
}
```
Assignee: @williamstein

implemented a cython wrapper for singular's kbase command. This is significantly faster than doing singular.kbase() because it doesn't have the pexpect overhead. 

Issue created by migration from https://trac.sagemath.org/ticket/3252





---

archive/issue_comments_022495.json:
```json
{
    "body": "Attachment [libsingular_kbase.patch](tarball://root/attachments/some-uuid/ticket3252/libsingular_kbase.patch) by @yqiang created at 2008-05-18 03:35:48",
    "created_at": "2008-05-18T03:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3252#issuecomment-22495",
    "user": "@yqiang"
}
```

Attachment [libsingular_kbase.patch](tarball://root/attachments/some-uuid/ticket3252/libsingular_kbase.patch) by @yqiang created at 2008-05-18 03:35:48



---

archive/issue_comments_022496.json:
```json
{
    "body": "The patch looks good, applies cleanly and does as advertised. However, two new functions are introduced without doctests. Though they are only wrappers every new function must have a doctest these days.",
    "created_at": "2008-05-18T14:35:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3252#issuecomment-22496",
    "user": "@malb"
}
```

The patch looks good, applies cleanly and does as advertised. However, two new functions are introduced without doctests. Though they are only wrappers every new function must have a doctest these days.



---

archive/issue_comments_022497.json:
```json
{
    "body": "Attachment [libsingular_kbase_doctest.patch](tarball://root/attachments/some-uuid/ticket3252/libsingular_kbase_doctest.patch) by @yqiang created at 2008-05-18 15:12:45\n\nadd doctests as requested by reviewer",
    "created_at": "2008-05-18T15:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3252#issuecomment-22497",
    "user": "@yqiang"
}
```

Attachment [libsingular_kbase_doctest.patch](tarball://root/attachments/some-uuid/ticket3252/libsingular_kbase_doctest.patch) by @yqiang created at 2008-05-18 15:12:45

add doctests as requested by reviewer



---

archive/issue_comments_022498.json:
```json
{
    "body": "Attached a patch which doctests the 2 functions mentioned. Apply after the first patch.",
    "created_at": "2008-05-18T15:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3252#issuecomment-22498",
    "user": "@yqiang"
}
```

Attached a patch which doctests the 2 functions mentioned. Apply after the first patch.



---

archive/issue_comments_022499.json:
```json
{
    "body": "Great! and even greater: We know have a new libSingular developer :-)",
    "created_at": "2008-05-18T15:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3252#issuecomment-22499",
    "user": "@malb"
}
```

Great! and even greater: We know have a new libSingular developer :-)



---

archive/issue_comments_022500.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-18T16:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3252#issuecomment-22500",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022501.json:
```json
{
    "body": "Merged both patches in Sage 3.0.2.alpha1",
    "created_at": "2008-05-18T16:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3252#issuecomment-22501",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.0.2.alpha1
