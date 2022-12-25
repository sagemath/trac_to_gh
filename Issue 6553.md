# Issue 6553: fast slicing of sparse matrices

archive/issues_006553.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @rbeezer\n\nExtracting a slice from a sparse matrix is insanely slow, as the code effectively treats the matrix as a dense matrix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6553\n\n",
    "created_at": "2009-07-18T12:46:30Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "fast slicing of sparse matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6553",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @rbeezer

Extracting a slice from a sparse matrix is insanely slow, as the code effectively treats the matrix as a dense matrix.

Issue created by migration from https://trac.sagemath.org/ticket/6553





---

archive/issue_comments_053340.json:
```json
{
    "body": "Before, I waited for several minutes before giving up.\n\nAFTER:\n\n```\nsage: A=random_matrix(ZZ,100000,density=.00005,sparse=True)                  \nsage: %time A[50000:,:50000]                                                 \nCPU times: user 0.43 s, sys: 0.01 s, total: 0.44 s\nWall time: 0.47 s\n50000 x 50000 sparse matrix over Integer Ring\n```\n\n\nAlso:\n\nBEFORE:\n\n```\nsage: A=random_matrix(ZZ,10000,density=.00005,sparse=True)     \nsage: %time A[5000:,:5000]                                     \nCPU times: user 8.32 s, sys: 0.02 s, total: 8.34 s\nWall time: 8.69 s\n5000 x 5000 sparse matrix over Integer Ring\n```\n\nAFTER:\n\n```\nsage: A=random_matrix(ZZ,10000,density=.00005,sparse=True)\nsage: %time A[5000:,:5000]                                \nCPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s\nWall time: 0.08 s\n5000 x 5000 sparse matrix over Integer Ring\n```",
    "created_at": "2009-07-18T13:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6553#issuecomment-53340",
    "user": "https://github.com/jasongrout"
}
```

Before, I waited for several minutes before giving up.

AFTER:

```
sage: A=random_matrix(ZZ,100000,density=.00005,sparse=True)                  
sage: %time A[50000:,:50000]                                                 
CPU times: user 0.43 s, sys: 0.01 s, total: 0.44 s
Wall time: 0.47 s
50000 x 50000 sparse matrix over Integer Ring
```


Also:

BEFORE:

```
sage: A=random_matrix(ZZ,10000,density=.00005,sparse=True)     
sage: %time A[5000:,:5000]                                     
CPU times: user 8.32 s, sys: 0.02 s, total: 8.34 s
Wall time: 8.69 s
5000 x 5000 sparse matrix over Integer Ring
```

AFTER:

```
sage: A=random_matrix(ZZ,10000,density=.00005,sparse=True)
sage: %time A[5000:,:5000]                                
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.08 s
5000 x 5000 sparse matrix over Integer Ring
```



---

archive/issue_comments_053341.json:
```json
{
    "body": "Nicely done.  Three comments before giving this a positive review.\n\n1.  The last test behaves differently for me, and the result seems \"more correct\" according to the density specified.  This is on 4.1.rc1 (which is the newest upgrade I could muster).\n\n```\n    sage: len(B.nonzero_positions())\nExpected:\n    14047\nGot:\n    100550\n```\n\n2.  Lists of non-integers (admittedly silly) fails silently and incorrectly.  It would appear that no entry of the new matrix gets set properly, so the result is the zero matrix of the correct size.\n\n```\nsage: A = random_matrix(ZZ, 20, 20, x=10, sparse=True)\nsage: len(A.nonzero_positions())\n353\nsage: A.matrix_from_rows_and_columns([1.1, 2.1, 3.1, 4.1], [5.1, 6.1, 7.1, 8.1])\n\n[0 0 0 0]\n[0 0 0 0]\n[0 0 0 0]\n[0 0 0 0]\n```\n\n3.  I'd think the doctests would be improved if there were tests for \n\n(a) the condition in (2)\n\n(b) the case of non-list input (raising the `TypeError` as implemented)",
    "created_at": "2009-07-20T02:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6553#issuecomment-53341",
    "user": "https://github.com/rbeezer"
}
```

Nicely done.  Three comments before giving this a positive review.

1.  The last test behaves differently for me, and the result seems "more correct" according to the density specified.  This is on 4.1.rc1 (which is the newest upgrade I could muster).

```
    sage: len(B.nonzero_positions())
Expected:
    14047
Got:
    100550
```

2.  Lists of non-integers (admittedly silly) fails silently and incorrectly.  It would appear that no entry of the new matrix gets set properly, so the result is the zero matrix of the correct size.

```
sage: A = random_matrix(ZZ, 20, 20, x=10, sparse=True)
sage: len(A.nonzero_positions())
353
sage: A.matrix_from_rows_and_columns([1.1, 2.1, 3.1, 4.1], [5.1, 6.1, 7.1, 8.1])

[0 0 0 0]
[0 0 0 0]
[0 0 0 0]
[0 0 0 0]
```

3.  I'd think the doctests would be improved if there were tests for 

(a) the condition in (2)

(b) the case of non-list input (raising the `TypeError` as implemented)



---

archive/issue_comments_053342.json:
```json
{
    "body": "Thanks for reviewing these so quickly!\n\n1. Are you on a 64-bit system (maybe you are getting a different random matrix)?  That doctest quite definitely passes for me.  I agree that your answer seems more correct, though.\n\n2.  The error is in the sparse matrix indexing function, not in this function.  I've opened up #6569 to address this issue, with a relevant example.  I don't think that should hold back this code.\n\n3. The condition in (2) should be tested in #6569.  I've updated the patch to include a doctest for (b).",
    "created_at": "2009-07-20T14:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6553#issuecomment-53342",
    "user": "https://github.com/jasongrout"
}
```

Thanks for reviewing these so quickly!

1. Are you on a 64-bit system (maybe you are getting a different random matrix)?  That doctest quite definitely passes for me.  I agree that your answer seems more correct, though.

2.  The error is in the sparse matrix indexing function, not in this function.  I've opened up #6569 to address this issue, with a relevant example.  I don't think that should hold back this code.

3. The condition in (2) should be tested in #6569.  I've updated the patch to include a doctest for (b).



---

archive/issue_comments_053343.json:
```json
{
    "body": "Also, the problem (1) above might be related to #3436.",
    "created_at": "2009-07-20T14:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6553#issuecomment-53343",
    "user": "https://github.com/jasongrout"
}
```

Also, the problem (1) above might be related to #3436.



---

archive/issue_comments_053344.json:
```json
{
    "body": "Yes, I'm testing on a 64-bit system.  What do you want to do with this doctest?  \n\nI think that is all that needs to be addressed now, since you are right that the non-integer index and density behavior belong elsewhere.\n\nSolve one problem and expose two more?  ;-)\n\nRob",
    "created_at": "2009-07-20T18:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6553#issuecomment-53344",
    "user": "https://github.com/rbeezer"
}
```

Yes, I'm testing on a 64-bit system.  What do you want to do with this doctest?  

I think that is all that needs to be addressed now, since you are right that the non-integer index and density behavior belong elsewhere.

Solve one problem and expose two more?  ;-)

Rob



---

archive/issue_comments_053345.json:
```json
{
    "body": "Attachment [trac-6553-slicing-sparse-matrices.patch](tarball://root/attachments/some-uuid/ticket6553/trac-6553-slicing-sparse-matrices.patch) by @jasongrout created at 2009-07-21 06:50:33\n\nI've updated the patch again with both of our outputs.  It should pass your doctests now too.  Can you review it again?\n\nThanks!",
    "created_at": "2009-07-21T06:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6553#issuecomment-53345",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-6553-slicing-sparse-matrices.patch](tarball://root/attachments/some-uuid/ticket6553/trac-6553-slicing-sparse-matrices.patch) by @jasongrout created at 2009-07-21 06:50:33

I've updated the patch again with both of our outputs.  It should pass your doctests now too.  Can you review it again?

Thanks!



---

archive/issue_comments_053346.json:
```json
{
    "body": "The fix on the one doctest works.  Passes tests for all of sage/matrix/*\n\nPositive review.\n\nPS The discrepancy here, and as illustrated in #3436, is troubling.",
    "created_at": "2009-07-22T00:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6553#issuecomment-53346",
    "user": "https://github.com/rbeezer"
}
```

The fix on the one doctest works.  Passes tests for all of sage/matrix/*

Positive review.

PS The discrepancy here, and as illustrated in #3436, is troubling.



---

archive/issue_comments_053347.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T04:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6553#issuecomment-53347",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015463.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-23T04:57:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6553",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6553#event-15463"
}
```
