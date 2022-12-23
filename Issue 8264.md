# Issue 8264: swap_row does not work on modular matrices

archive/issues_008264.json:
```json
{
    "body": "Assignee: was\n\nFor some reason, swap_row does not work if the elements of the matrix are treated as integers modulo something. The code to reproduce the bug is the following:\n\n\n\n```\nA = matrix(ZZ, 2,[1,2,3,4])\nB = copy(A)\nB.swap_rows(0,1)\nprint B,'\\n'\nB.swap_columns(0,1) # So far so good\nprint B,'\\n'\nC = A.apply_map(lambda x:mod(x,8))\nC.swap_rows(0,1) # This line does not work\nprint C,'\\n'\nC.swap_columns(0,1) # But this one does\nprint C\n```\n\n\nThe bug reproduces every time on Mac OSX 10.6, SAGE version 4.3.1.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8264\n\n",
    "created_at": "2010-02-14T17:50:43Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "swap_row does not work on modular matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8264",
    "user": "janwil123"
}
```
Assignee: was

For some reason, swap_row does not work if the elements of the matrix are treated as integers modulo something. The code to reproduce the bug is the following:



```
A = matrix(ZZ, 2,[1,2,3,4])
B = copy(A)
B.swap_rows(0,1)
print B,'\n'
B.swap_columns(0,1) # So far so good
print B,'\n'
C = A.apply_map(lambda x:mod(x,8))
C.swap_rows(0,1) # This line does not work
print C,'\n'
C.swap_columns(0,1) # But this one does
print C
```


The bug reproduces every time on Mac OSX 10.6, SAGE version 4.3.1.

Issue created by migration from https://trac.sagemath.org/ticket/8264





---

archive/issue_comments_073157.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-03-05T23:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8264#issuecomment-73157",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_073158.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-05T23:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8264#issuecomment-73158",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073159.json:
```json
{
    "body": "The patch fix the ticket and add the good test.\n\nPositive review from me.",
    "created_at": "2010-03-06T10:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8264#issuecomment-73159",
    "user": "nborie"
}
```

The patch fix the ticket and add the good test.

Positive review from me.



---

archive/issue_comments_073160.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-06T10:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8264#issuecomment-73160",
    "user": "nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073161.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T23:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8264#issuecomment-73161",
    "user": "mhansen"
}
```

Resolution: fixed
