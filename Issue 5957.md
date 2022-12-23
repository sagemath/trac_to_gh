# Issue 5957: 3.4.2.rc0: Maxima related doctest failure in matrix/matrix_symbolic_dense.pyx

archive/issues_005957.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis happens with gcc 4.3.3 on iras and cicero:\n\n```\nsage -t -long \"devel/sage/sage/matrix/matrix_symbolic_dense.pyx\"\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.2.rc0/sage-3.4.2.rc0-ciero-gcc-4.3.3/\ndevel/sage/sage/matrix/matrix_symbolic_dense.pyx\", line 413:\n   sage: M.determinant()\nExpected:\n   4*x - 6\nGot:\n   determinant(sage513)\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5957\n\n",
    "created_at": "2009-05-01T13:34:36Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "3.4.2.rc0: Maxima related doctest failure in matrix/matrix_symbolic_dense.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5957",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This happens with gcc 4.3.3 on iras and cicero:

```
sage -t -long "devel/sage/sage/matrix/matrix_symbolic_dense.pyx"
**********************************************************************
File "/home/mabshoff/build-3.4.2.rc0/sage-3.4.2.rc0-ciero-gcc-4.3.3/
devel/sage/sage/matrix/matrix_symbolic_dense.pyx", line 413:
   sage: M.determinant()
Expected:
   4*x - 6
Got:
   determinant(sage513)
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/5957





---

archive/issue_comments_047159.json:
```json
{
    "body": "Maybe it is good to mention I had this failure already in sage-3.4.2.alpha0.\n\nBoth with Fedora 9 and 10, 32 bit.\n\ngcc version 4.3.0, resp. 4.3.2\n\nJaap",
    "created_at": "2009-05-03T22:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5957#issuecomment-47159",
    "user": "jsp"
}
```

Maybe it is good to mention I had this failure already in sage-3.4.2.alpha0.

Both with Fedora 9 and 10, 32 bit.

gcc version 4.3.0, resp. 4.3.2

Jaap



---

archive/issue_comments_047160.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-04T04:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5957#issuecomment-47160",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_047161.json:
```json
{
    "body": "This is William's patch, so I can review it :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T04:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5957#issuecomment-47161",
    "user": "mabshoff"
}
```

This is William's patch, so I can review it :)

Cheers,

Michael



---

archive/issue_comments_047162.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T05:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5957#issuecomment-47162",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_047163.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-04T05:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5957#issuecomment-47163",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047164.json:
```json
{
    "body": "Merged in Sage 3.4.2.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T05:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5957#issuecomment-47164",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.final.

Cheers,

Michael
