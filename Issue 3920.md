# Issue 3920: [with patch, needs review] FiniteFieldElement.vector/matrix -> _vector_/_matrix_

archive/issues_003920.json:
```json
{
    "body": "Assignee: was\n\nCC:  robertwb\n\nWhile reading the Developer's guide update at #3905 it occurred to me that `vector()`/`matrix()` methods are supposed to be called `_vector_`/`_matrix_()` methods so that `matrix(foo)` works. The attached patch changes those functions for finite field elements.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3920\n\n",
    "created_at": "2008-08-21T09:01:34Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] FiniteFieldElement.vector/matrix -> _vector_/_matrix_",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3920",
    "user": "malb"
}
```
Assignee: was

CC:  robertwb

While reading the Developer's guide update at #3905 it occurred to me that `vector()`/`matrix()` methods are supposed to be called `_vector_`/`_matrix_()` methods so that `matrix(foo)` works. The attached patch changes those functions for finite field elements.

Issue created by migration from https://trac.sagemath.org/ticket/3920





---

archive/issue_comments_028037.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-20T16:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3920#issuecomment-28037",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028038.json:
```json
{
    "body": "Changing assignee from was to malb.",
    "created_at": "2008-09-20T16:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3920#issuecomment-28038",
    "user": "malb"
}
```

Changing assignee from was to malb.



---

archive/issue_comments_028039.json:
```json
{
    "body": "Just a short comment: could you put back in the matrix() and vector() functions and add a deprecation warning for now?  That way code doesn't suddenly break.",
    "created_at": "2008-09-26T16:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3920#issuecomment-28039",
    "user": "jason"
}
```

Just a short comment: could you put back in the matrix() and vector() functions and add a deprecation warning for now?  That way code doesn't suddenly break.



---

archive/issue_comments_028040.json:
```json
{
    "body": "Attachment\n\nSince you use \"\\code\" in the docstring for vector and matrix, the docstrings need to start with r\"\"\" instead of \"\"\".  Patch attached.",
    "created_at": "2008-10-17T21:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3920#issuecomment-28040",
    "user": "jhpalmieri"
}
```

Attachment

Since you use "\code" in the docstring for vector and matrix, the docstrings need to start with r""" instead of """.  Patch attached.



---

archive/issue_comments_028041.json:
```json
{
    "body": "Attachment\n\napply after malb's patch",
    "created_at": "2008-10-17T21:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3920#issuecomment-28041",
    "user": "jhpalmieri"
}
```

Attachment

apply after malb's patch



---

archive/issue_comments_028042.json:
```json
{
    "body": "Otherwise, your patch looks good to me. Now I finally know of an example of the `_vector_` method -- I was looking for one when I was revising the Developer's guide...\n\nI've doctested the changed files with complete success. I'm currently running `sage -testall` to make sure nothing else is screwed up by this. I'll give it a tentative positive review now while I'm thinking about it, then change it one way or the other depending on how the testing works out.",
    "created_at": "2008-10-17T21:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3920#issuecomment-28042",
    "user": "jhpalmieri"
}
```

Otherwise, your patch looks good to me. Now I finally know of an example of the `_vector_` method -- I was looking for one when I was revising the Developer's guide...

I've doctested the changed files with complete success. I'm currently running `sage -testall` to make sure nothing else is screwed up by this. I'll give it a tentative positive review now while I'm thinking about it, then change it one way or the other depending on how the testing works out.



---

archive/issue_comments_028043.json:
```json
{
    "body": "All tests passed!",
    "created_at": "2008-10-17T22:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3920#issuecomment-28043",
    "user": "jhpalmieri"
}
```

All tests passed!



---

archive/issue_comments_028044.json:
```json
{
    "body": "Positive review on John's additional patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T10:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3920#issuecomment-28044",
    "user": "mabshoff"
}
```

Positive review on John's additional patch.

Cheers,

Michael



---

archive/issue_comments_028045.json:
```json
{
    "body": "Robert: This patch touches\n\n* sage/rings/finite_field_givaro.pyx\n* sage/rings/finite_field_ntl_gf2e.pyx\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T10:33:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3920#issuecomment-28045",
    "user": "mabshoff"
}
```

Robert: This patch touches

* sage/rings/finite_field_givaro.pyx
* sage/rings/finite_field_ntl_gf2e.pyx

Cheers,

Michael



---

archive/issue_comments_028046.json:
```json
{
    "body": "Merged both patches in Sage 3.2.alpha0",
    "created_at": "2008-10-18T11:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3920#issuecomment-28046",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.alpha0



---

archive/issue_comments_028047.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T11:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3920#issuecomment-28047",
    "user": "mabshoff"
}
```

Resolution: fixed
