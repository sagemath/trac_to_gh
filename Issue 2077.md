# Issue 2077: matrix.column(i) should throw error when i is larger than the number of columns in the matrix (minus 1).

archive/issues_002077.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: a=matrix([[1,2],[3,4]])\nsage: a.column(0)\n(1, 3)\nsage: a.column(1)\n(2, 4)\nsage: a.column(3)\n(2, 4)\nsage: a.column(2)\n(1, 3)\n```\n\n\nThe documentation for a.column says that it behaves like list indexing when given a negative index.  We should probably also act like list indexing for positive indices that are too big and throw an error:\n\n\n```\nsage: l=range(3); l\n[0, 1, 2]\nsage: l[3]\n---------------------------------------------------------------------------\n<type 'exceptions.IndexError'>            Traceback (most recent call last)\n\n/home/grout/downloads/cython-callback/<ipython console> in <module>()\n\n<type 'exceptions.IndexError'>: list index out of range\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2077\n\n",
    "created_at": "2008-02-06T23:29:16Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "matrix.column(i) should throw error when i is larger than the number of columns in the matrix (minus 1).",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2077",
    "user": "@jasongrout"
}
```
Assignee: @williamstein


```
sage: a=matrix([[1,2],[3,4]])
sage: a.column(0)
(1, 3)
sage: a.column(1)
(2, 4)
sage: a.column(3)
(2, 4)
sage: a.column(2)
(1, 3)
```


The documentation for a.column says that it behaves like list indexing when given a negative index.  We should probably also act like list indexing for positive indices that are too big and throw an error:


```
sage: l=range(3); l
[0, 1, 2]
sage: l[3]
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/home/grout/downloads/cython-callback/<ipython console> in <module>()

<type 'exceptions.IndexError'>: list index out of range
```



Issue created by migration from https://trac.sagemath.org/ticket/2077





---

archive/issue_comments_013443.json:
```json
{
    "body": "Attachment [matrix-column-wrapping.patch](tarball://root/attachments/some-uuid/ticket2077/matrix-column-wrapping.patch) by @jasongrout created at 2008-02-07 02:31:31",
    "created_at": "2008-02-07T02:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2077#issuecomment-13443",
    "user": "@jasongrout"
}
```

Attachment [matrix-column-wrapping.patch](tarball://root/attachments/some-uuid/ticket2077/matrix-column-wrapping.patch) by @jasongrout created at 2008-02-07 02:31:31



---

archive/issue_comments_013444.json:
```json
{
    "body": "Attachment [matrix-column-wrapping.2.patch](tarball://root/attachments/some-uuid/ticket2077/matrix-column-wrapping.2.patch) by @jasongrout created at 2008-02-07 02:33:55\n\nApply the .2.patch (which corrects a minor typo).",
    "created_at": "2008-02-07T02:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2077#issuecomment-13444",
    "user": "@jasongrout"
}
```

Attachment [matrix-column-wrapping.2.patch](tarball://root/attachments/some-uuid/ticket2077/matrix-column-wrapping.2.patch) by @jasongrout created at 2008-02-07 02:33:55

Apply the .2.patch (which corrects a minor typo).



---

archive/issue_comments_013445.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-02-07T08:16:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2077#issuecomment-13445",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_013446.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-07T10:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2077#issuecomment-13446",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013447.json:
```json
{
    "body": "Merged matrix-column-wrapping.2.patch in Sage 2.10.2.alpha2",
    "created_at": "2008-02-07T10:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2077#issuecomment-13447",
    "user": "mabshoff"
}
```

Merged matrix-column-wrapping.2.patch in Sage 2.10.2.alpha2
