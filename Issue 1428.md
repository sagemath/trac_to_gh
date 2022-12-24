# Issue 1428: add SVD method to matrix_complex_double_dense

archive/issues_001428.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  dfdeshom@gmail.com\n\n\n```\nHallo!\n\nI tried to compute the SVD of a complex matrix (module\nmatrix.matrix_complex_double_dense), but I didn't found a function to\ndo so. However, real matrices (module matrix.matrix_real_double_dense)\nsupport it. Is there really no way to compute a complex SVD? If I\nremember correctly, at least the underlying library GSL supports\ncomplex SVDs... What would I have to do to integrate those functions\ninto Sage?\n\nSander\n```\n\n\nBasically all that needs to be done is to translate the real code over to the complex case.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1428\n\n",
    "created_at": "2007-12-08T14:53:32Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "add SVD method to matrix_complex_double_dense",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1428",
    "user": "@mwhansen"
}
```
Assignee: @williamstein

CC:  dfdeshom@gmail.com


```
Hallo!

I tried to compute the SVD of a complex matrix (module
matrix.matrix_complex_double_dense), but I didn't found a function to
do so. However, real matrices (module matrix.matrix_real_double_dense)
support it. Is there really no way to compute a complex SVD? If I
remember correctly, at least the underlying library GSL supports
complex SVDs... What would I have to do to integrate those functions
into Sage?

Sander
```


Basically all that needs to be done is to translate the real code over to the complex case.

Issue created by migration from https://trac.sagemath.org/ticket/1428





---

archive/issue_comments_009203.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-22T13:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1428#issuecomment-9203",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009204.json:
```json
{
    "body": "Attachment [1428.patch](tarball://root/attachments/some-uuid/ticket1428/1428.patch) by @mwhansen created at 2007-12-22 13:15:23",
    "created_at": "2007-12-22T13:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1428#issuecomment-9204",
    "user": "@mwhansen"
}
```

Attachment [1428.patch](tarball://root/attachments/some-uuid/ticket1428/1428.patch) by @mwhansen created at 2007-12-22 13:15:23



---

archive/issue_comments_009205.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-12-22T13:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1428#issuecomment-9205",
    "user": "@mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_009206.json:
```json
{
    "body": "The patch looks great. I would suggest making an option that would just return S, instead of the tuple (U,S,V') since people that use this method tend to care more about S than anything else.",
    "created_at": "2008-01-15T01:57:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1428#issuecomment-9206",
    "user": "@dfdeshom"
}
```

The patch looks great. I would suggest making an option that would just return S, instead of the tuple (U,S,V') since people that use this method tend to care more about S than anything else.



---

archive/issue_comments_009207.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T03:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1428#issuecomment-9207",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009208.json:
```json
{
    "body": "Merged in Sage 2.10.alpha3",
    "created_at": "2008-01-15T03:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1428#issuecomment-9208",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha3
