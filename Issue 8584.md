# Issue 8584: implement latex'ing of Dirichlet characters

archive/issues_008584.json:
```json
{
    "body": "Assignee: craigcitro\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8584\n\n",
    "created_at": "2010-03-23T07:11:27Z",
    "labels": [
        "modular forms",
        "minor",
        "enhancement"
    ],
    "title": "implement latex'ing of Dirichlet characters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8584",
    "user": "was"
}
```
Assignee: craigcitro



Issue created by migration from https://trac.sagemath.org/ticket/8584





---

archive/issue_comments_077738.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-23T07:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77738",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077739.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-23T16:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77739",
    "user": "craigcitro"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077740.json:
```json
{
    "body": "Attachment\n\nLooks good, though I still agree with David Loeffler's complaint from another ticket that the print representation for Dirichlet characters isn't great. If we decide to change it, that means we need to remember to change this function, too (since it directly calls `values_on_gens`).",
    "created_at": "2010-03-23T16:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77740",
    "user": "craigcitro"
}
```

Attachment

Looks good, though I still agree with David Loeffler's complaint from another ticket that the print representation for Dirichlet characters isn't great. If we decide to change it, that means we need to remember to change this function, too (since it directly calls `values_on_gens`).



---

archive/issue_comments_077741.json:
```json
{
    "body": "> I still agree. .. print representation for Dirichlet characters isn't great. \n\nI don't agree.  I really like the print representation of Dirichlet characters.",
    "created_at": "2010-04-02T13:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77741",
    "user": "was"
}
```

> I still agree. .. print representation for Dirichlet characters isn't great. 

I don't agree.  I really like the print representation of Dirichlet characters.



---

archive/issue_comments_077742.json:
```json
{
    "body": "I'm putting this back on \"needs work\" because it conflicts with #8133, and there seems to be a consensus on sage-nt that #8133 should go in.\n\nDavid",
    "created_at": "2010-04-05T13:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77742",
    "user": "davidloeffler"
}
```

I'm putting this back on "needs work" because it conflicts with #8133, and there seems to be a consensus on sage-nt that #8133 should go in.

David



---

archive/issue_comments_077743.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-05T13:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77743",
    "user": "davidloeffler"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_077744.json:
```json
{
    "body": "replaces previous patch, apply after #8133",
    "created_at": "2010-04-05T13:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77744",
    "user": "davidloeffler"
}
```

replaces previous patch, apply after #8133



---

archive/issue_comments_077745.json:
```json
{
    "body": "Attachment\n\nHere's a new patch which produces output similar to the new `_repr_` but with the zeta's and mapsto arrows latexified.",
    "created_at": "2010-04-05T13:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77745",
    "user": "davidloeffler"
}
```

Attachment

Here's a new patch which produces output similar to the new `_repr_` but with the zeta's and mapsto arrows latexified.



---

archive/issue_comments_077746.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-05T13:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77746",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077747.json:
```json
{
    "body": "all tests pass on the new patch applied after #8133. Thanks.",
    "created_at": "2010-04-08T13:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77747",
    "user": "wuthrich"
}
```

all tests pass on the new patch applied after #8133. Thanks.



---

archive/issue_comments_077748.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-08T13:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77748",
    "user": "wuthrich"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077749.json:
```json
{
    "body": "Merged \"trac_8584_new.patch\" into 4.4.alpha0.",
    "created_at": "2010-04-15T23:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77749",
    "user": "jhpalmieri"
}
```

Merged "trac_8584_new.patch" into 4.4.alpha0.



---

archive/issue_comments_077750.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8584#issuecomment-77750",
    "user": "jhpalmieri"
}
```

Resolution: fixed
