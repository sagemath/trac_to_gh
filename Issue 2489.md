# Issue 2489: symmetric crashes when giving a skew partition to kostka_tab

archive/issues_002489.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\n\n```\n\nsymmetrica.kostka_tab([[2,2],[1]],[2,1])\n\nevaluating this expression leads to the error message:\n\nException exceptions.TypeError: 'an integer is required' in\n'sage.libs.symmetrica.symmetrica._op_integer' ignored\nException exceptions.TypeError: 'an integer is required' in\n'sage.libs.symmetrica.symmetrica._op_integer' ignored\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2489\n\n",
    "created_at": "2008-03-12T11:01:42Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "symmetric crashes when giving a skew partition to kostka_tab",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2489",
    "user": "@mwhansen"
}
```
Assignee: @mwhansen

CC:  sage-combinat


```

symmetrica.kostka_tab([[2,2],[1]],[2,1])

evaluating this expression leads to the error message:

Exception exceptions.TypeError: 'an integer is required' in
'sage.libs.symmetrica.symmetrica._op_integer' ignored
Exception exceptions.TypeError: 'an integer is required' in
'sage.libs.symmetrica.symmetrica._op_integer' ignored
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


Issue created by migration from https://trac.sagemath.org/ticket/2489





---

archive/issue_comments_016871.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-12T11:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2489#issuecomment-16871",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016872.json:
```json
{
    "body": "Attachment [2489.patch](tarball://root/attachments/some-uuid/ticket2489/2489.patch) by @mwhansen created at 2008-03-12 11:20:53",
    "created_at": "2008-03-12T11:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2489#issuecomment-16872",
    "user": "@mwhansen"
}
```

Attachment [2489.patch](tarball://root/attachments/some-uuid/ticket2489/2489.patch) by @mwhansen created at 2008-03-12 11:20:53



---

archive/issue_comments_016873.json:
```json
{
    "body": "Successfully installs, no more error, code looks good.",
    "created_at": "2008-03-14T19:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2489#issuecomment-16873",
    "user": "@saliola"
}
```

Successfully installs, no more error, code looks good.



---

archive/issue_comments_016874.json:
```json
{
    "body": "Attachment [2489.2.patch](tarball://root/attachments/some-uuid/ticket2489/2489.2.patch) by @mwhansen created at 2008-03-14 20:32:16",
    "created_at": "2008-03-14T20:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2489#issuecomment-16874",
    "user": "@mwhansen"
}
```

Attachment [2489.2.patch](tarball://root/attachments/some-uuid/ticket2489/2489.2.patch) by @mwhansen created at 2008-03-14 20:32:16



---

archive/issue_comments_016875.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T20:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2489#issuecomment-16875",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016876.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T20:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2489#issuecomment-16876",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
