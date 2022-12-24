# Issue 5198: apply_map skips zeroes in sparse vectors and matrices

archive/issues_005198.json:
```json
{
    "body": "Assignee: was\n\nConsider:\n\n```\nsage: vector(ZZ, range(3)).apply_map(lambda x: x+1)\n(1, 2, 3)\nsage: vector(ZZ, range(3), sparse=True).apply_map(lambda x: x+1)\n(0, 2, 3)\n```\n\n\nand\n\n\n```\nsage: matrix(ZZ, range(3)).apply_map(lambda x: x+1)\n[1 2 3]\nsage: matrix(ZZ, range(3), sparse=True).apply_map(lambda x: x+1)\n[0 2 3]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5198\n\n",
    "created_at": "2009-02-07T00:39:36Z",
    "labels": [
        "linear algebra",
        "blocker",
        "bug"
    ],
    "title": "apply_map skips zeroes in sparse vectors and matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5198",
    "user": "cwitty"
}
```
Assignee: was

Consider:

```
sage: vector(ZZ, range(3)).apply_map(lambda x: x+1)
(1, 2, 3)
sage: vector(ZZ, range(3), sparse=True).apply_map(lambda x: x+1)
(0, 2, 3)
```


and


```
sage: matrix(ZZ, range(3)).apply_map(lambda x: x+1)
[1 2 3]
sage: matrix(ZZ, range(3), sparse=True).apply_map(lambda x: x+1)
[0 2 3]
```



Issue created by migration from https://trac.sagemath.org/ticket/5198





---

archive/issue_comments_039836.json:
```json
{
    "body": "Attachment [trac5198_apply_map_sparse.patch](tarball://root/attachments/some-uuid/ticket5198/trac5198_apply_map_sparse.patch) by cwitty created at 2009-02-07 04:49:38\n\nThe attached patch fixes the problem, and adds a sparse=True/False argument to apply_map that may be useful if you know that the result will have a different sparsity than the input.\n\nI also fixed a bug along the way: apply_map didn't preserve subdivisions for sparse matrices.  Sorry, reviewer, whoever you are.",
    "created_at": "2009-02-07T04:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5198#issuecomment-39836",
    "user": "cwitty"
}
```

Attachment [trac5198_apply_map_sparse.patch](tarball://root/attachments/some-uuid/ticket5198/trac5198_apply_map_sparse.patch) by cwitty created at 2009-02-07 04:49:38

The attached patch fixes the problem, and adds a sparse=True/False argument to apply_map that may be useful if you know that the result will have a different sparsity than the input.

I also fixed a bug along the way: apply_map didn't preserve subdivisions for sparse matrices.  Sorry, reviewer, whoever you are.



---

archive/issue_comments_039837.json:
```json
{
    "body": "Ouch...that is a pretty bad bug. \n\nThe patch fixes the above issues and works well for me (including the subdivisions fix).",
    "created_at": "2009-02-07T09:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5198#issuecomment-39837",
    "user": "robertwb"
}
```

Ouch...that is a pretty bad bug. 

The patch fixes the above issues and works well for me (including the subdivisions fix).



---

archive/issue_comments_039838.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-08T01:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5198#issuecomment-39838",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039839.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T01:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5198#issuecomment-39839",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael
