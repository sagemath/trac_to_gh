# Issue 7877: matrix indexing should be explained in the manual

archive/issues_007877.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  rbeezer mvngu\n\nA lot of the great stuff in the docstrings for the matrix __getitem__ and __setitem__ functions should be in the reference manual somewhere, maybe http://sagemath.org/doc/reference/sage/matrix/docs.html.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7877\n\n",
    "created_at": "2010-01-09T17:51:19Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "matrix indexing should be explained in the manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7877",
    "user": "jason"
}
```
Assignee: mvngu

CC:  rbeezer mvngu

A lot of the great stuff in the docstrings for the matrix __getitem__ and __setitem__ functions should be in the reference manual somewhere, maybe http://sagemath.org/doc/reference/sage/matrix/docs.html.

Issue created by migration from https://trac.sagemath.org/ticket/7877





---

archive/issue_comments_068435.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T07:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68435",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068436.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-20T07:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68436",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_068437.json:
```json
{
    "body": "Depends on #8008, but otherwise, excellent!",
    "created_at": "2010-01-20T09:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68437",
    "user": "robertwb"
}
```

Depends on #8008, but otherwise, excellent!



---

archive/issue_comments_068438.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T09:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68438",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068439.json:
```json
{
    "body": "Attachment\n\napply on top of previous",
    "created_at": "2010-01-20T09:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68439",
    "user": "mvngu"
}
```

Attachment

apply on top of previous



---

archive/issue_comments_068440.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-20T09:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68440",
    "user": "mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_068441.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T09:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68441",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068442.json:
```json
{
    "body": "Here's a typo in the patch:\n\n```\n96\tGet the second column of M:: \n97\t         \n98\t    sage: M[1:,0] \n99\t    [ 1] \n100\t    [ 1] \n101\t    [-1]\n```\n\nThe code should be:\n\n```\nsage: M[:,1]\n[-2]\n[ 8]\n[ 1]\n[ 2]\n```\n\nI have attached patch for this, which needs some review. Otherwise the whole ticket looks good.",
    "created_at": "2010-01-20T09:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68442",
    "user": "mvngu"
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

archive/issue_comments_068443.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-20T10:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68443",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_068444.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T10:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68444",
    "user": "jason"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068445.json:
```json
{
    "body": "positive review for Minh's patch; I attached the same patch for the __getitem__ docstring in matrix0.pyx.",
    "created_at": "2010-01-20T10:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68445",
    "user": "jason"
}
```

positive review for Minh's patch; I attached the same patch for the __getitem__ docstring in matrix0.pyx.



---

archive/issue_comments_068446.json:
```json
{
    "body": "(apply trac-7877-doc-error.patch on top of all previous patches)",
    "created_at": "2010-01-20T10:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68446",
    "user": "jason"
}
```

(apply trac-7877-doc-error.patch on top of all previous patches)



---

archive/issue_comments_068447.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68447",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_068448.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac-7877-doc-matrix-indexing.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac-7877-doc-matrix-indexing.patch)\n2. [trac_7877-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac_7877-reviewer.patch)\n3. [trac-7877-doc-error.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac-7877-doc-error.patch)\n\nJason: You should put a sensible commit message in your patch, together with the ticket number.",
    "created_at": "2010-03-02T21:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7877#issuecomment-68448",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac-7877-doc-matrix-indexing.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac-7877-doc-matrix-indexing.patch)
2. [trac_7877-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac_7877-reviewer.patch)
3. [trac-7877-doc-error.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7877/trac-7877-doc-error.patch)

Jason: You should put a sensible commit message in your patch, together with the ticket number.
