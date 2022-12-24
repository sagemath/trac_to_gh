# Issue 4439: Sage 3.2.a2: make three doctests from #788 random again

archive/issues_004439.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe following tests should be made random again:\n\n```\n(make #random again)\nsage -t  devel/sage/sage/matrix/matrix_complex_double_dense.pyx\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/matrix_complex_double_dense.py\", line 899:\n    sage: U*S*V.transpose()\nExpected:\n    [...e-1...                1.0]\n    [               2.0                3.0]\n    [               4.0                5.0]\nGot:\n    [  0 1.0]\n    [2.0 3.0]\n    [4.0 5.0]\n**********************************************************************\n\n(make random again)\nsage -t  devel/sage/sage/matrix/matrix_real_double_dense.pyx\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/matrix_real_double_dense.py\", line 786:\n    sage: U*S*V.transpose()\nExpected:\n    [...e-1...               1.0               2.0]\n    [              3.0               4.0               5.0]\nGot:\n    [0.0 1.0 2.0]\n    [3.0 4.0 5.0]\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/matrix_real_double_dense.py\", line 794:\n    sage: U*S*V.transpose()\nExpected:\n    [...e-1...                1.0]\n    [               2.0                3.0]\n    [               4.0                5.0]\nGot:\n    [0.0 1.0]\n    [2.0 3.0]\n    [4.0 5.0]\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4439\n\n",
    "created_at": "2008-11-04T13:57:11Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 3.2.a2: make three doctests from #788 random again",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4439",
    "user": "mabshoff"
}
```
Assignee: mabshoff

The following tests should be made random again:

```
(make #random again)
sage -t  devel/sage/sage/matrix/matrix_complex_double_dense.pyx
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/matrix_complex_double_dense.py", line 899:
    sage: U*S*V.transpose()
Expected:
    [...e-1...                1.0]
    [               2.0                3.0]
    [               4.0                5.0]
Got:
    [  0 1.0]
    [2.0 3.0]
    [4.0 5.0]
**********************************************************************

(make random again)
sage -t  devel/sage/sage/matrix/matrix_real_double_dense.pyx
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/matrix_real_double_dense.py", line 786:
    sage: U*S*V.transpose()
Expected:
    [...e-1...               1.0               2.0]
    [              3.0               4.0               5.0]
Got:
    [0.0 1.0 2.0]
    [3.0 4.0 5.0]
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-menas/tmp/matrix_real_double_dense.py", line 794:
    sage: U*S*V.transpose()
Expected:
    [...e-1...                1.0]
    [               2.0                3.0]
    [               4.0                5.0]
Got:
    [0.0 1.0]
    [2.0 3.0]
    [4.0 5.0]
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4439





---

archive/issue_comments_032633.json:
```json
{
    "body": "Attachment [trac_4439.patch](tarball://root/attachments/some-uuid/ticket4439/trac_4439.patch) by craigcitro created at 2008-11-05 22:39:04\n\nLooks good.",
    "created_at": "2008-11-05T22:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4439#issuecomment-32633",
    "user": "craigcitro"
}
```

Attachment [trac_4439.patch](tarball://root/attachments/some-uuid/ticket4439/trac_4439.patch) by craigcitro created at 2008-11-05 22:39:04

Looks good.



---

archive/issue_comments_032634.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-05T23:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4439#issuecomment-32634",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha3



---

archive/issue_comments_032635.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-05T23:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4439#issuecomment-32635",
    "user": "mabshoff"
}
```

Resolution: fixed
