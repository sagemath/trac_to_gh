# Issue 2799: matrix's __getitem__ doesn't respect slice object's step attribute

archive/issues_002799.json:
```json
{
    "body": "Assignee: dfdeshom\n\nEx: ` A[:,0:4:2]` should return the 0th and 2nd column of A, if possible:\n\n\n```\nage: A = matrix(ZZ,3,4, [3, 2, -5, 0, 1, -1, 1, -4, 1, 0, 1, -3]); A\n[ 3  2 -5  0]\n[ 1 -1  1 -4]\n[ 1  0  1 -3]\n\nsage: A[:,0:4:2]\n[ 3  2 -5  0]\n[ 1 -1  1 -4]\n[ 1  0  1 -3]\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2799\n\n",
    "created_at": "2008-04-04T19:09:31Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "matrix's __getitem__ doesn't respect slice object's step attribute",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2799",
    "user": "dfdeshom"
}
```
Assignee: dfdeshom

Ex: ` A[:,0:4:2]` should return the 0th and 2nd column of A, if possible:


```
age: A = matrix(ZZ,3,4, [3, 2, -5, 0, 1, -1, 1, -4, 1, 0, 1, -3]); A
[ 3  2 -5  0]
[ 1 -1  1 -4]
[ 1  0  1 -3]

sage: A[:,0:4:2]
[ 3  2 -5  0]
[ 1 -1  1 -4]
[ 1  0  1 -3]

```


Issue created by migration from https://trac.sagemath.org/ticket/2799





---

archive/issue_comments_019218.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-04T22:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2799#issuecomment-19218",
    "user": "dfdeshom"
}
```

Attachment



---

archive/issue_comments_019219.json:
```json
{
    "body": "I've added a patch which should allow people to do more flexible things such as \n`A[2:-1:-1,3:1:-1] `.",
    "created_at": "2008-04-04T22:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2799#issuecomment-19219",
    "user": "dfdeshom"
}
```

I've added a patch which should allow people to do more flexible things such as 
`A[2:-1:-1,3:1:-1] `.



---

archive/issue_comments_019220.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-05T10:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2799#issuecomment-19220",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_019221.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-05T16:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2799#issuecomment-19221",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019222.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-05T16:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2799#issuecomment-19222",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2
