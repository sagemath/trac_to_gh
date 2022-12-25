# Issue 5099: rank for mod n sparse matrices is broken

archive/issues_005099.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: sparse, rank\n\nOn both sage.math (sage 3.2.3) and on my iMac (sage 3.3.alpha1), running\n\n```\nmatrix(GF(3), 0, 0, {}).rank()\n```\n\nis broken: sometimes I get 0, sometimes I get 1, sometimes I get `RuntimeError`. Same goes for \n\n```\nmatrix(GF(3), 0, 0, sparse=True).rank()\n```\n\nand \n\n```\nmatrix(GF(3), 0, 10, sparse=True).rank()\n```\n\nFor what it's worth, `matrix(GF(3), 10, 0, sparse=True).rank()` seems okay.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5099\n\n",
    "created_at": "2009-01-25T16:46:23Z",
    "labels": [
        "component: linear algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "rank for mod n sparse matrices is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5099",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @williamstein

Keywords: sparse, rank

On both sage.math (sage 3.2.3) and on my iMac (sage 3.3.alpha1), running

```
matrix(GF(3), 0, 0, {}).rank()
```

is broken: sometimes I get 0, sometimes I get 1, sometimes I get `RuntimeError`. Same goes for 

```
matrix(GF(3), 0, 0, sparse=True).rank()
```

and 

```
matrix(GF(3), 0, 10, sparse=True).rank()
```

For what it's worth, `matrix(GF(3), 10, 0, sparse=True).rank()` seems okay.



Issue created by migration from https://trac.sagemath.org/ticket/5099





---

archive/issue_comments_038846.json:
```json
{
    "body": "I Just discovered this problem, otherwise I would had taken care of it in #5256. This problem is very likely to occur for other kind of matrices. I suggest to expand `test_trivial_matrices_inverse` (from `sage.matrix.matrix_space`) which already tests `det`,`is_invertible` and `inverse` to also test the `rank` method. \n\nIf you need it, I can also investigate further...\n\nCheers,\n\nFlorent",
    "created_at": "2009-02-26T20:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5099#issuecomment-38846",
    "user": "https://github.com/hivert"
}
```

I Just discovered this problem, otherwise I would had taken care of it in #5256. This problem is very likely to occur for other kind of matrices. I suggest to expand `test_trivial_matrices_inverse` (from `sage.matrix.matrix_space`) which already tests `det`,`is_invertible` and `inverse` to also test the `rank` method. 

If you need it, I can also investigate further...

Cheers,

Florent



---

archive/issue_comments_038847.json:
```json
{
    "body": "Changing assignee from @williamstein to @hivert.",
    "created_at": "2009-02-26T21:33:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5099#issuecomment-38847",
    "user": "https://github.com/hivert"
}
```

Changing assignee from @williamstein to @hivert.



---

archive/issue_comments_038848.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-26T21:33:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5099#issuecomment-38848",
    "user": "https://github.com/hivert"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038849.json:
```json
{
    "body": "Attachment [matrix_fix_again-fh.patch](tarball://root/attachments/some-uuid/ticket5099/matrix_fix_again-fh.patch) by @hivert created at 2009-03-01 22:09:20\n\nPatch proposal",
    "created_at": "2009-03-01T22:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5099#issuecomment-38849",
    "user": "https://github.com/hivert"
}
```

Attachment [matrix_fix_again-fh.patch](tarball://root/attachments/some-uuid/ticket5099/matrix_fix_again-fh.patch) by @hivert created at 2009-03-01 22:09:20

Patch proposal



---

archive/issue_comments_038850.json:
```json
{
    "body": "The patch should solve the problem and check the rank methods for trivial matrices of other type. For Q[x,y] the rank is not implemented and can't be tested. I tested it as non implemented to ensure that it will be correctly tested if someone implement it. \n\nAuthor of the patch: Florent Hivert",
    "created_at": "2009-03-01T22:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5099#issuecomment-38850",
    "user": "https://github.com/hivert"
}
```

The patch should solve the problem and check the rank methods for trivial matrices of other type. For Q[x,y] the rank is not implemented and can't be tested. I tested it as non implemented to ensure that it will be correctly tested if someone implement it. 

Author of the patch: Florent Hivert



---

archive/issue_comments_038851.json:
```json
{
    "body": "This fixes my problem.  Positive review.",
    "created_at": "2009-03-03T19:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5099#issuecomment-38851",
    "user": "https://github.com/jhpalmieri"
}
```

This fixes my problem.  Positive review.



---

archive/issue_events_011776.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-05T00:45:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5099",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5099#event-11776"
}
```



---

archive/issue_comments_038852.json:
```json
{
    "body": "Merged in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-05T00:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5099#issuecomment-38852",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_events_011777.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-05T00:45:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5099",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5099#event-11777"
}
```



---

archive/issue_comments_038853.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-05T00:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5099#issuecomment-38853",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
