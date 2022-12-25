# Issue 7877: matrix indexing should be explained in the manual

archive/issues_007877.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @rbeezer mvngu\n\nA lot of the great stuff in the docstrings for the matrix __getitem__ and __setitem__ functions should be in the reference manual somewhere, maybe http://sagemath.org/doc/reference/sage/matrix/docs.html.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7877\n\n",
    "created_at": "2010-01-09T17:51:19Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "matrix indexing should be explained in the manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7877",
    "user": "https://github.com/jasongrout"
}
```
Assignee: mvngu

CC:  @rbeezer mvngu

A lot of the great stuff in the docstrings for the matrix __getitem__ and __setitem__ functions should be in the reference manual somewhere, maybe http://sagemath.org/doc/reference/sage/matrix/docs.html.

Issue created by migration from https://trac.sagemath.org/ticket/7877





---

archive/issue_comments_068317.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T07:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68317",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068318.json:
```json
{
    "body": "Attachment [trac-7877-doc-matrix-indexing.patch](tarball://root/attachments/some-uuid/ticket7877/trac-7877-doc-matrix-indexing.patch) by @jasongrout created at 2010-01-20 07:05:49",
    "created_at": "2010-01-20T07:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68318",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7877-doc-matrix-indexing.patch](tarball://root/attachments/some-uuid/ticket7877/trac-7877-doc-matrix-indexing.patch) by @jasongrout created at 2010-01-20 07:05:49



---

archive/issue_comments_068319.json:
```json
{
    "body": "Depends on #8008, but otherwise, excellent!",
    "created_at": "2010-01-20T09:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68319",
    "user": "https://github.com/robertwb"
}
```

Depends on #8008, but otherwise, excellent!



---

archive/issue_comments_068320.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T09:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68320",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068321.json:
```json
{
    "body": "Attachment [trac_7877-reviewer.patch](tarball://root/attachments/some-uuid/ticket7877/trac_7877-reviewer.patch) by mvngu created at 2010-01-20 09:51:11\n\napply on top of previous",
    "created_at": "2010-01-20T09:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68321",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7877-reviewer.patch](tarball://root/attachments/some-uuid/ticket7877/trac_7877-reviewer.patch) by mvngu created at 2010-01-20 09:51:11

apply on top of previous



---

archive/issue_comments_068322.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-20T09:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68322",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_068323.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T09:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68323",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068324.json:
```json
{
    "body": "Here's a typo in the patch:\n\n```\n96\tGet the second column of M:: \n97\t         \n98\t    sage: M[1:,0] \n99\t    [ 1] \n100\t    [ 1] \n101\t    [-1]\n```\n\nThe code should be:\n\n```\nsage: M[:,1]\n[-2]\n[ 8]\n[ 1]\n[ 2]\n```\n\nI have attached patch for this, which needs some review. Otherwise the whole ticket looks good.",
    "created_at": "2010-01-20T09:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68324",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Here's a typo in the patch:

```
96	Get the second column of M:: 
97	         
98	    sage: M[1:,0] 
99	    [ 1] 
100	    [ 1] 
101	    [-1]
```

The code should be:

```
sage: M[:,1]
[-2]
[ 8]
[ 1]
[ 2]
```

I have attached patch for this, which needs some review. Otherwise the whole ticket looks good.



---

archive/issue_comments_068325.json:
```json
{
    "body": "Attachment [trac-7877-doc-error.patch](tarball://root/attachments/some-uuid/ticket7877/trac-7877-doc-error.patch) by @jasongrout created at 2010-01-20 10:11:48",
    "created_at": "2010-01-20T10:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68325",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7877-doc-error.patch](tarball://root/attachments/some-uuid/ticket7877/trac-7877-doc-error.patch) by @jasongrout created at 2010-01-20 10:11:48



---

archive/issue_comments_068326.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T10:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68326",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068327.json:
```json
{
    "body": "positive review for Minh's patch; I attached the same patch for the __getitem__ docstring in matrix0.pyx.",
    "created_at": "2010-01-20T10:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68327",
    "user": "https://github.com/jasongrout"
}
```

positive review for Minh's patch; I attached the same patch for the __getitem__ docstring in matrix0.pyx.



---

archive/issue_comments_068328.json:
```json
{
    "body": "(apply trac-7877-doc-error.patch on top of all previous patches)",
    "created_at": "2010-01-20T10:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68328",
    "user": "https://github.com/jasongrout"
}
```

(apply trac-7877-doc-error.patch on top of all previous patches)



---

archive/issue_comments_068329.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68329",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_008092.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T21:59:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7877#event-8092"
}
```



---

archive/issue_comments_068330.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac-7877-doc-matrix-indexing.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac-7877-doc-matrix-indexing.patch)\n2. [trac_7877-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac_7877-reviewer.patch)\n3. [trac-7877-doc-error.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac-7877-doc-error.patch)\n\nJason: You should put a sensible commit message in your patch, together with the ticket number.",
    "created_at": "2010-03-02T21:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68330",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac-7877-doc-matrix-indexing.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac-7877-doc-matrix-indexing.patch)
2. [trac_7877-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac_7877-reviewer.patch)
3. [trac-7877-doc-error.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac-7877-doc-error.patch)

Jason: You should put a sensible commit message in your patch, together with the ticket number.
