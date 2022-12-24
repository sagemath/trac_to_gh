# Issue 3419: [with patch, needs review] 100% coverage for sage.coding.binary_code

archive/issues_003419.json:
```json
{
    "body": "Assignee: rlm\n\n\n```\n$ ./sage -coverage devel/sage/sage/coding/binary_code.pyx\n----------------------------------------------------------------------\ndevel/sage/sage/coding/binary_code.pyx\nSCORE devel/sage/sage/coding/binary_code.pyx: 100% (41 of 41)\n\nPossibly wrong (function name doesn't occur in doctests):\n\t * int put_in_std_form(self)\n\n----------------------------------------------------------------------\n```\n\n\nThere seems to be a little bug in sage-coverage related to cpdef functions: the function name definitely occurs in the doctest. Has #1795 gone stale?!\n\nIssue created by migration from https://trac.sagemath.org/ticket/3419\n\n",
    "created_at": "2008-06-13T18:41:02Z",
    "labels": [
        "coding theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] 100% coverage for sage.coding.binary_code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3419",
    "user": "rlm"
}
```
Assignee: rlm


```
$ ./sage -coverage devel/sage/sage/coding/binary_code.pyx
----------------------------------------------------------------------
devel/sage/sage/coding/binary_code.pyx
SCORE devel/sage/sage/coding/binary_code.pyx: 100% (41 of 41)

Possibly wrong (function name doesn't occur in doctests):
	 * int put_in_std_form(self)

----------------------------------------------------------------------
```


There seems to be a little bug in sage-coverage related to cpdef functions: the function name definitely occurs in the doctest. Has #1795 gone stale?!

Issue created by migration from https://trac.sagemath.org/ticket/3419





---

archive/issue_comments_024067.json:
```json
{
    "body": "Attachment [trac3419-100_binary_code.patch](tarball://root/attachments/some-uuid/ticket3419/trac3419-100_binary_code.patch) by mabshoff created at 2008-06-13 18:47:06\n\nThe cpdef patch ought to get merged this week, I am not sure what the current merge status is.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-13T18:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3419#issuecomment-24067",
    "user": "mabshoff"
}
```

Attachment [trac3419-100_binary_code.patch](tarball://root/attachments/some-uuid/ticket3419/trac3419-100_binary_code.patch) by mabshoff created at 2008-06-13 18:47:06

The cpdef patch ought to get merged this week, I am not sure what the current merge status is.

Cheers,

Michael



---

archive/issue_comments_024068.json:
```json
{
    "body": "Patch looks good.",
    "created_at": "2008-06-15T19:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3419#issuecomment-24068",
    "user": "malb"
}
```

Patch looks good.



---

archive/issue_comments_024069.json:
```json
{
    "body": "Apply after #3471.",
    "created_at": "2008-06-22T20:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3419#issuecomment-24069",
    "user": "rlm"
}
```

Apply after #3471.



---

archive/issue_comments_024070.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T03:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3419#issuecomment-24070",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024071.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T03:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3419#issuecomment-24071",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha0
