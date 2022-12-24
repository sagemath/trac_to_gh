# Issue 5001: kernels of integer matrices

archive/issues_005001.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: matrix, kernel\n\n\n```\nsage: id = matrix(ZZ, 2, 2, [[1, 0], [0, 1]]) \nsage: id.left_kernel()\nTraceback\n...\nTypeError: Argument K (= Integer Ring) must be a field.\n```\n\nOn the other hand, `id.right_kernel()` and `id.kernel()` both work, and `id.kernel()` actually computes the left kernel.  Note also that the documentation for both left_kernel and right_kernel says that the answer will be a vector space, not a module over the integers; this should be fixed, too.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5001\n\n",
    "created_at": "2009-01-17T16:36:51Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "kernels of integer matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5001",
    "user": "@jhpalmieri"
}
```
Assignee: @williamstein

Keywords: matrix, kernel


```
sage: id = matrix(ZZ, 2, 2, [[1, 0], [0, 1]]) 
sage: id.left_kernel()
Traceback
...
TypeError: Argument K (= Integer Ring) must be a field.
```

On the other hand, `id.right_kernel()` and `id.kernel()` both work, and `id.kernel()` actually computes the left kernel.  Note also that the documentation for both left_kernel and right_kernel says that the answer will be a vector space, not a module over the integers; this should be fixed, too.



Issue created by migration from https://trac.sagemath.org/ticket/5001





---

archive/issue_comments_038140.json:
```json
{
    "body": "Attachment [trac_5001.patch](tarball://root/attachments/some-uuid/ticket5001/trac_5001.patch) by @williamstein created at 2009-01-24 16:24:54",
    "created_at": "2009-01-24T16:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5001#issuecomment-38140",
    "user": "@williamstein"
}
```

Attachment [trac_5001.patch](tarball://root/attachments/some-uuid/ticket5001/trac_5001.patch) by @williamstein created at 2009-01-24 16:24:54



---

archive/issue_comments_038141.json:
```json
{
    "body": "Looks good, all tests passed. A few comments: the documentation still says \"vector space\" when computing the kernel of an integer matrix, but I can live with that.  Perhaps more seriously, if you don't apply patch #5089, then computing the kernel (or left_kernel or right_kernel) of a sparse integer matrix leads to a segmentation fault.  Does this need to be investigated further?",
    "created_at": "2009-01-24T17:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5001#issuecomment-38141",
    "user": "@jhpalmieri"
}
```

Looks good, all tests passed. A few comments: the documentation still says "vector space" when computing the kernel of an integer matrix, but I can live with that.  Perhaps more seriously, if you don't apply patch #5089, then computing the kernel (or left_kernel or right_kernel) of a sparse integer matrix leads to a segmentation fault.  Does this need to be investigated further?



---

archive/issue_comments_038142.json:
```json
{
    "body": "Since #5089 is being merged I am changing this to a positive review. The documentation issue about vector spaces vs. modules should be addressed via a followup ticket. \n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T17:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5001#issuecomment-38142",
    "user": "mabshoff"
}
```

Since #5089 is being merged I am changing this to a positive review. The documentation issue about vector spaces vs. modules should be addressed via a followup ticket. 

Cheers,

Michael



---

archive/issue_comments_038143.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T18:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5001#issuecomment-38143",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2

Cheers,

Michael



---

archive/issue_comments_038144.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T18:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5001#issuecomment-38144",
    "user": "mabshoff"
}
```

Resolution: fixed
