# Issue 2947: [with patch; needs review] block_matrix([]) fails

archive/issues_002947.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhile debugging #2946 on IRC, Jason found that `block_matrix()` doesn't properly handle an empty list.\n\nThe attached patch makes `block_matrix([])` return a 0x0 matrix over ZZ. If nrows and ncols are also specified, and subdivide isn't false, this 0x0 matrix will be further subdivided into nrows x ncols 0x0 matrices. This subdivision might be overkill, but it's probably the most consistent return value. Other opinions are welcome, of course.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2947\n\n",
    "created_at": "2008-04-17T22:19:05Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; needs review] block_matrix([]) fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2947",
    "user": "@wjp"
}
```
Assignee: @williamstein

While debugging #2946 on IRC, Jason found that `block_matrix()` doesn't properly handle an empty list.

The attached patch makes `block_matrix([])` return a 0x0 matrix over ZZ. If nrows and ncols are also specified, and subdivide isn't false, this 0x0 matrix will be further subdivided into nrows x ncols 0x0 matrices. This subdivision might be overkill, but it's probably the most consistent return value. Other opinions are welcome, of course.

Issue created by migration from https://trac.sagemath.org/ticket/2947





---

archive/issue_comments_020324.json:
```json
{
    "body": "Attachment [block_matrix_empty.patch](tarball://root/attachments/some-uuid/ticket2947/block_matrix_empty.patch) by @wjp created at 2008-04-17 22:19:15",
    "created_at": "2008-04-17T22:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2947#issuecomment-20324",
    "user": "@wjp"
}
```

Attachment [block_matrix_empty.patch](tarball://root/attachments/some-uuid/ticket2947/block_matrix_empty.patch) by @wjp created at 2008-04-17 22:19:15



---

archive/issue_comments_020325.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-18T03:24:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2947#issuecomment-20325",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_020326.json:
```json
{
    "body": "There are rejection problems [with or without #2946 applied]:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha6/devel/sage$ patch -p1 < trac_2947_block_matrix_empty.patch\npatching file sage/matrix/constructor.py\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha6/devel/sage$ patch -p1 < trac_2946_noninvertible_jordan_form.patch\npatching file sage/matrix/matrix2.pyx\nHunk #1 succeeded at 3591 (offset 59 lines).\nHunk #2 FAILED at 3601.\nHunk #3 FAILED at 3630.\n2 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej\n(reverse-i-search)`rm': patch -p1 < trac_2946_noninvertible_jordan_form.patch\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-04-18T06:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2947#issuecomment-20326",
    "user": "mabshoff"
}
```

There are rejection problems [with or without #2946 applied]:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha6/devel/sage$ patch -p1 < trac_2947_block_matrix_empty.patch
patching file sage/matrix/constructor.py
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha6/devel/sage$ patch -p1 < trac_2946_noninvertible_jordan_form.patch
patching file sage/matrix/matrix2.pyx
Hunk #1 succeeded at 3591 (offset 59 lines).
Hunk #2 FAILED at 3601.
Hunk #3 FAILED at 3630.
2 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej
(reverse-i-search)`rm': patch -p1 < trac_2946_noninvertible_jordan_form.patch
```


Cheers,

Michael



---

archive/issue_comments_020327.json:
```json
{
    "body": "Disregard the last comment, it should have been on the #2947 ticket. My bad.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-18T06:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2947#issuecomment-20327",
    "user": "mabshoff"
}
```

Disregard the last comment, it should have been on the #2947 ticket. My bad.

Cheers,

Michael



---

archive/issue_comments_020328.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-18T06:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2947#issuecomment-20328",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020329.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-18T06:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2947#issuecomment-20329",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha6
