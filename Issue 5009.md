# Issue 5009: elementary_divisors for integer matrices: fix doc string

archive/issues_005009.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: elementary divisor\n\nThe doc string for the `elementary_divisors` method in matrix_integer_dense.pyx says\n\n```\nThe elementary divisors are the invariants of the finite\nabelian group that is the cokernel of this matrix. \n```\n\nThe word \"cokernel\" needs to be expanded upon.  I think, from trial and error, that this is computing the cokernel of left multiplication by the matrix, and this needs to be **clearly stated**, especially given other left/right issues with matrices in Sage.  (See #1587, for example.)\n\nFurthermore, give at least one example where the matrix *isn't square* so we can see a bit more clearly on which side the matrix is acting, say a simple matrix like [[3, 0, 0], [0, 0, 0]].  Maybe even include both this and its transpose.\n\n(As an editorial comment, I find it really annoying that methods like this are for left multiplication, while methods like `restrict_codomain` are for right multiplication, so if I want to use them both, I have to take transposes way too many times.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5009\n\n",
    "created_at": "2009-01-18T06:32:17Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "elementary_divisors for integer matrices: fix doc string",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5009",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @williamstein

Keywords: elementary divisor

The doc string for the `elementary_divisors` method in matrix_integer_dense.pyx says

```
The elementary divisors are the invariants of the finite
abelian group that is the cokernel of this matrix. 
```

The word "cokernel" needs to be expanded upon.  I think, from trial and error, that this is computing the cokernel of left multiplication by the matrix, and this needs to be **clearly stated**, especially given other left/right issues with matrices in Sage.  (See #1587, for example.)

Furthermore, give at least one example where the matrix *isn't square* so we can see a bit more clearly on which side the matrix is acting, say a simple matrix like [[3, 0, 0], [0, 0, 0]].  Maybe even include both this and its transpose.

(As an editorial comment, I find it really annoying that methods like this are for left multiplication, while methods like `restrict_codomain` are for right multiplication, so if I want to use them both, I have to take transposes way too many times.)

Issue created by migration from https://trac.sagemath.org/ticket/5009





---

archive/issue_comments_038116.json:
```json
{
    "body": "Attachment [trac-5009.patch](tarball://root/attachments/some-uuid/ticket5009/trac-5009.patch) by @rlmill created at 2009-01-23 15:13:28",
    "created_at": "2009-01-23T15:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5009#issuecomment-38116",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac-5009.patch](tarball://root/attachments/some-uuid/ticket5009/trac-5009.patch) by @rlmill created at 2009-01-23 15:13:28



---

archive/issue_comments_038117.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-01-24T15:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5009#issuecomment-38117",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_038118.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T13:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5009#issuecomment-38118",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005253.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-28T13:03:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5009",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5009#event-5253"
}
```



---

archive/issue_comments_038119.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T13:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5009#issuecomment-38119",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael
