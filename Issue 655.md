# Issue 655: Wrap LinBox's Sparse Matrix Echelonizer over Finite Fields

archive/issues_000655.json:
```json
{
    "body": "Assignee: @williamstein\n\nApparently, LinBox can compute echelon forms for sparse matrices over finite fields. And it seems to be faster than what we have now:\n\nSAGE:\n\n```\nsage: A = random_matrix(GF(127),10000,10000,density=0.0002,sparse=True)\nsage: time A.echelonize()\nCPU times: user 99.64 s, sys: 0.22 s, total: 99.85 s\n```\n\n\nLinBox:\n\n```\nmatrix size :10000x10000\ndensity = 0.0002\nsize before = 19981\nGaussian elimination (no reordering)...done (9.08057 s)\nDONE\nsize after = 0 # Bug\n```\n\n\nI was told that `SparseMatrixBase::NoReordering` works but `InPlaceLinearPivoting` crashes.\n\nAlso, it claims to support GF(q) which is very very slow in SAGE right now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/655\n\n",
    "created_at": "2007-09-14T09:22:40Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "Wrap LinBox's Sparse Matrix Echelonizer over Finite Fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/655",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

Apparently, LinBox can compute echelon forms for sparse matrices over finite fields. And it seems to be faster than what we have now:

SAGE:

```
sage: A = random_matrix(GF(127),10000,10000,density=0.0002,sparse=True)
sage: time A.echelonize()
CPU times: user 99.64 s, sys: 0.22 s, total: 99.85 s
```


LinBox:

```
matrix size :10000x10000
density = 0.0002
size before = 19981
Gaussian elimination (no reordering)...done (9.08057 s)
DONE
size after = 0 # Bug
```


I was told that `SparseMatrixBase::NoReordering` works but `InPlaceLinearPivoting` crashes.

Also, it claims to support GF(q) which is very very slow in SAGE right now.

Issue created by migration from https://trac.sagemath.org/ticket/655





---

archive/issue_comments_003392.json:
```json
{
    "body": "Actually, the above is not a bug but the size actually is zero after application of the Gaussian elimination. LinBox clears rows it doesn't need anymore to save memory.\n\nAlso, `InPlaceLinearPivoting` does not crash if called correctly and is often faster than `NoReordering`.",
    "created_at": "2007-09-15T14:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/655#issuecomment-3392",
    "user": "https://github.com/malb"
}
```

Actually, the above is not a bug but the size actually is zero after application of the Gaussian elimination. LinBox clears rows it doesn't need anymore to save memory.

Also, `InPlaceLinearPivoting` does not crash if called correctly and is often faster than `NoReordering`.



---

archive/issue_comments_003393.json:
```json
{
    "body": "Attachment [sparsegfp.patch](tarball://root/attachments/some-uuid/ticket655/sparsegfp.patch) by @malb created at 2007-09-15 14:28:13",
    "created_at": "2007-09-15T14:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/655#issuecomment-3393",
    "user": "https://github.com/malb"
}
```

Attachment [sparsegfp.patch](tarball://root/attachments/some-uuid/ticket655/sparsegfp.patch) by @malb created at 2007-09-15 14:28:13



---

archive/issue_comments_003394.json:
```json
{
    "body": "`sparsegfp.patch` requires http://sage.math.washington.edu/home/malb/pkgs/linbox-20070915.spkg and exposes some of LinBox's functionality for sparse matrices over GF(p) to SAGE. More to come.",
    "created_at": "2007-09-15T14:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/655#issuecomment-3394",
    "user": "https://github.com/malb"
}
```

`sparsegfp.patch` requires http://sage.math.washington.edu/home/malb/pkgs/linbox-20070915.spkg and exposes some of LinBox's functionality for sparse matrices over GF(p) to SAGE. More to come.



---

archive/issue_comments_003395.json:
```json
{
    "body": "Attachment [sparsegfq-solve.patch](tarball://root/attachments/some-uuid/ticket655/sparsegfq-solve.patch) by @malb created at 2007-09-15 21:26:25",
    "created_at": "2007-09-15T21:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/655#issuecomment-3395",
    "user": "https://github.com/malb"
}
```

Attachment [sparsegfq-solve.patch](tarball://root/attachments/some-uuid/ticket655/sparsegfq-solve.patch) by @malb created at 2007-09-15 21:26:25



---

archive/issue_comments_003396.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T00:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/655#issuecomment-3396",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000721.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-09-21T00:08:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/655",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/655#event-721"
}
```
