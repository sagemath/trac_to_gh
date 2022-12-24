# Issue 5144: [with patch, needs review] speed up right_nullity for matrices

archive/issues_005144.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason\n\nKeywords: right_nullity\n\nleft_nullity currently functions by computing the difference between self.nrows() and self.rank().\n\nright_nullity currently functions by calling left_nullity on the transpose of the matrix, and so it can be sped up if it instead computes self.ncols() - self.rank().  The attached patch does this.\n\nTo see the effect, try timing some things with\n\n```\nsage: m = random_matrix(ZZ, 50, x=2^16)\n```\n\nOn my machine, I get\n\n```\nsage: timeit('m.left_nullity()')\n625 loops, best of 3: 2.29 \u00b5s per loop\ntimeit('m.transpose()')\n125 loops, best of 3: 1.72 ms per loop\n```\n\nso the transpose operation is really slow.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5144\n\n",
    "created_at": "2009-01-31T01:13:24Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] speed up right_nullity for matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5144",
    "user": "jhpalmieri"
}
```
Assignee: was

CC:  jason

Keywords: right_nullity

left_nullity currently functions by computing the difference between self.nrows() and self.rank().

right_nullity currently functions by calling left_nullity on the transpose of the matrix, and so it can be sped up if it instead computes self.ncols() - self.rank().  The attached patch does this.

To see the effect, try timing some things with

```
sage: m = random_matrix(ZZ, 50, x=2^16)
```

On my machine, I get

```
sage: timeit('m.left_nullity()')
625 loops, best of 3: 2.29 µs per loop
timeit('m.transpose()')
125 loops, best of 3: 1.72 ms per loop
```

so the transpose operation is really slow.

Issue created by migration from https://trac.sagemath.org/ticket/5144





---

archive/issue_comments_039353.json:
```json
{
    "body": "Attachment [5144.patch](tarball://root/attachments/some-uuid/ticket5144/5144.patch) by jhpalmieri created at 2009-01-31 01:14:07",
    "created_at": "2009-01-31T01:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5144#issuecomment-39353",
    "user": "jhpalmieri"
}
```

Attachment [5144.patch](tarball://root/attachments/some-uuid/ticket5144/5144.patch) by jhpalmieri created at 2009-01-31 01:14:07



---

archive/issue_comments_039354.json:
```json
{
    "body": "Good catch!  The patch looks good and doctests pass in matrix2.pyx.  Positive review.",
    "created_at": "2009-02-06T18:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5144#issuecomment-39354",
    "user": "jason"
}
```

Good catch!  The patch looks good and doctests pass in matrix2.pyx.  Positive review.



---

archive/issue_comments_039355.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-06T22:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5144#issuecomment-39355",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039356.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T22:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5144#issuecomment-39356",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael
