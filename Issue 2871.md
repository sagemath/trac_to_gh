# Issue 2871: matrix: M[range(2,-1,-1),:] returns junk

archive/issues_002871.json:
```json
{
    "body": "Assignee: dfdeshom\n\nIn the following example, A should be \"upside down\", but it's not\n\n```\nsage: A = random_matrix(ZZ,3); A\n\n[ 1  3 -1]\n[ 4 -3 -1]\n[-1  0 -1]\n\nsage: A[range(2,-1,-1),:]\n\n[ 1  3 -1]\n[ 4 -3 -1]\n[-1  0 -1]\n\n```\n\n\nThe problem is with `set()`, which doesn't preserve order.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2871\n\n",
    "created_at": "2008-04-10T18:13:17Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "matrix: M[range(2,-1,-1),:] returns junk",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2871",
    "user": "dfdeshom"
}
```
Assignee: dfdeshom

In the following example, A should be "upside down", but it's not

```
sage: A = random_matrix(ZZ,3); A

[ 1  3 -1]
[ 4 -3 -1]
[-1  0 -1]

sage: A[range(2,-1,-1),:]

[ 1  3 -1]
[ 4 -3 -1]
[-1  0 -1]

```


The problem is with `set()`, which doesn't preserve order.

Issue created by migration from https://trac.sagemath.org/ticket/2871





---

archive/issue_comments_019702.json:
```json
{
    "body": "Attachment\n\nThe code and doctests look good, and doctests pass in sage/matrix in Sage 2.11.  Unfortunately, applying the patch to Sage 3.0 alpha 2 (the latest I have at the moment) gives a rejected hunk.",
    "created_at": "2008-04-12T04:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2871#issuecomment-19702",
    "user": "cwitty"
}
```

Attachment

The code and doctests look good, and doctests pass in sage/matrix in Sage 2.11.  Unfortunately, applying the patch to Sage 3.0 alpha 2 (the latest I have at the moment) gives a rejected hunk.



---

archive/issue_comments_019703.json:
```json
{
    "body": "patch against alpha2",
    "created_at": "2008-04-12T04:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2871#issuecomment-19703",
    "user": "dfdeshom"
}
```

patch against alpha2



---

archive/issue_comments_019704.json:
```json
{
    "body": "Attachment\n\nWith the revised 2871-alpha2.patch, the patch applies and doctests pass in sage/matrix for sage 3.0 alpha2.\n\nDidier, thanks for making the changes I requested on IRC!\n\nLooks good, please apply.",
    "created_at": "2008-04-12T05:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2871#issuecomment-19704",
    "user": "cwitty"
}
```

Attachment

With the revised 2871-alpha2.patch, the patch applies and doctests pass in sage/matrix for sage 3.0 alpha2.

Didier, thanks for making the changes I requested on IRC!

Looks good, please apply.



---

archive/issue_comments_019705.json:
```json
{
    "body": "Merged 2871-alpha2.patch in Sage 3.0.alpha4",
    "created_at": "2008-04-12T10:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2871#issuecomment-19705",
    "user": "mabshoff"
}
```

Merged 2871-alpha2.patch in Sage 3.0.alpha4



---

archive/issue_comments_019706.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T10:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2871#issuecomment-19706",
    "user": "mabshoff"
}
```

Resolution: fixed
