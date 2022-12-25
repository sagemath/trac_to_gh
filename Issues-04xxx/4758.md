# Issue 4758: [with patch, positive review] eigenvalues of matrices over CDF is embarassingly frickin' slow!!!!!!!!!!!! (at least 100 times too slow!)

archive/issues_004758.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @jasongrout\n\nBelow we compute the eigenvalues of a 100x100 random matrix over CDF in two ways.  Notices that the second way is 117 times faster than the first.  This is bad. \n\n```\nsage: a = random_matrix(CDF, 100)\nsage: time v = a.eigenvalues()\nCPU times: user 9.32 s, sys: 0.05 s, total: 9.37 s\nWall time: 9.56 s\nsage: a = random_matrix(CDF, 100)\nsage: time w = a.left_eigenvectors()[0]\nCPU times: user 0.08 s, sys: 0.00 s, total: 0.08 s\nWall time: 0.08 s\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4758\n\n",
    "closed_at": "2008-12-13T09:05:50Z",
    "created_at": "2008-12-11T05:21:06Z",
    "labels": [
        "component: linear algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch, positive review] eigenvalues of matrices over CDF is embarassingly frickin' slow!!!!!!!!!!!! (at least 100 times too slow!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4758",
    "user": "https://github.com/williamstein"
}
```
Assignee: @mwhansen

CC:  @jasongrout

Below we compute the eigenvalues of a 100x100 random matrix over CDF in two ways.  Notices that the second way is 117 times faster than the first.  This is bad. 

```
sage: a = random_matrix(CDF, 100)
sage: time v = a.eigenvalues()
CPU times: user 9.32 s, sys: 0.05 s, total: 9.37 s
Wall time: 9.56 s
sage: a = random_matrix(CDF, 100)
sage: time w = a.left_eigenvectors()[0]
CPU times: user 0.08 s, sys: 0.00 s, total: 0.08 s
Wall time: 0.08 s


Issue created by migration from https://trac.sagemath.org/ticket/4758





---

archive/issue_comments_035983.json:
```json
{
    "body": "This is the culprit since all of the specialized methods were removed:\n\nhttp://www.sagemath.org/hg/sage-main/diff/9550477ef46a/sage/matrix/matrix_complex_double_dense.pyx",
    "created_at": "2008-12-11T06:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35983",
    "user": "https://github.com/mwhansen"
}
```

This is the culprit since all of the specialized methods were removed:

http://www.sagemath.org/hg/sage-main/diff/9550477ef46a/sage/matrix/matrix_complex_double_dense.pyx



---

archive/issue_comments_035984.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-12-11T06:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35984",
    "user": "https://github.com/mwhansen"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_035985.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-11T07:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35985",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035986.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-12-11T07:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35986",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_035987.json:
```json
{
    "body": "Sorry, I didn't see that the specialized methods were moved to matrix_double_dense.pyx.\n\nI've attached a patch to fix this which just uses scipy.linalg.eigvals.\n\n```\nsage: sage: a = random_matrix(CDF, 100)\nsage: sage: time v = a.eigenvalues()\nCPU times: user 0.40 s, sys: 0.05 s, total: 0.45 s\nWall time: 0.47 s\nsage: %time w = a.left_eigenvectors()\nCPU times: user 0.51 s, sys: 0.00 s, total: 0.51 s\nWall time: 0.65 s\n```",
    "created_at": "2008-12-11T07:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35987",
    "user": "https://github.com/mwhansen"
}
```

Sorry, I didn't see that the specialized methods were moved to matrix_double_dense.pyx.

I've attached a patch to fix this which just uses scipy.linalg.eigvals.

```
sage: sage: a = random_matrix(CDF, 100)
sage: sage: time v = a.eigenvalues()
CPU times: user 0.40 s, sys: 0.05 s, total: 0.45 s
Wall time: 0.47 s
sage: %time w = a.left_eigenvectors()
CPU times: user 0.51 s, sys: 0.00 s, total: 0.51 s
Wall time: 0.65 s
```



---

archive/issue_comments_035988.json:
```json
{
    "body": "Where is the patch? :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T08:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35988",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Where is the patch? :)

Cheers,

Michael



---

archive/issue_comments_035989.json:
```json
{
    "body": "Attachment [trac_4758.patch](tarball://root/attachments/some-uuid/ticket4758/trac_4758.patch) by @mwhansen created at 2008-12-11 08:19:56",
    "created_at": "2008-12-11T08:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35989",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4758.patch](tarball://root/attachments/some-uuid/ticket4758/trac_4758.patch) by @mwhansen created at 2008-12-11 08:19:56



---

archive/issue_comments_035990.json:
```json
{
    "body": "Thanks.  Also, in matrix2.pyx, the eigenvalues command caches its result; we may want to add that here.  The code looks good; I can't test it right away.\n\nNote that there was not a special method for eigenvalues in the previous matrix_complex_double_dense.pyx, so the switch to a numpy backend was not the actual culprit.\n\nI'll be able to test this patch in the next day or two.",
    "created_at": "2008-12-11T08:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35990",
    "user": "https://github.com/jasongrout"
}
```

Thanks.  Also, in matrix2.pyx, the eigenvalues command caches its result; we may want to add that here.  The code looks good; I can't test it right away.

Note that there was not a special method for eigenvalues in the previous matrix_complex_double_dense.pyx, so the switch to a numpy backend was not the actual culprit.

I'll be able to test this patch in the next day or two.



---

archive/issue_comments_035991.json:
```json
{
    "body": "Also, there should probably be a test illustrating that the eigenvalues returned from an RDF matrix are CDF numbers.",
    "created_at": "2008-12-11T10:37:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35991",
    "user": "https://github.com/jasongrout"
}
```

Also, there should probably be a test illustrating that the eigenvalues returned from an RDF matrix are CDF numbers.



---

archive/issue_comments_035992.json:
```json
{
    "body": "Attachment [trac_4758_review.patch](tarball://root/attachments/some-uuid/ticket4758/trac_4758_review.patch) by @jasongrout created at 2008-12-12 21:04:53\n\napply on top of previous patches",
    "created_at": "2008-12-12T21:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35992",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_4758_review.patch](tarball://root/attachments/some-uuid/ticket4758/trac_4758_review.patch) by @jasongrout created at 2008-12-12 21:04:53

apply on top of previous patches



---

archive/issue_comments_035993.json:
```json
{
    "body": "Positive review.  I added a few more doctests in the review patch.  Doctests pass in the file.  If caching becomes an issue, we can add it later.",
    "created_at": "2008-12-12T21:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35993",
    "user": "https://github.com/jasongrout"
}
```

Positive review.  I added a few more doctests in the review patch.  Doctests pass in the file.  If caching becomes an issue, we can add it later.



---

archive/issue_comments_035994.json:
```json
{
    "body": "And one more time, this was a NotImplementedError, not a WasHereButThenDeletedError error :).",
    "created_at": "2008-12-12T21:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35994",
    "user": "https://github.com/jasongrout"
}
```

And one more time, this was a NotImplementedError, not a WasHereButThenDeletedError error :).



---

archive/issue_comments_035995.json:
```json
{
    "body": "Merged both patches in Sage 3.2.2.alpha2",
    "created_at": "2008-12-13T09:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35995",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.2.alpha2



---

archive/issue_events_010881.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-13T09:05:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4758#event-10881"
}
```



---

archive/issue_comments_035996.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-13T09:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4758#issuecomment-35996",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
