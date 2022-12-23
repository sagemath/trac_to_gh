# Issue 8494: docstring f or digits() should mention its inverse

archive/issues_008494.json:
```json
{
    "body": "Assignee: mvngu\n\nOne can use the `digits()` method to go from an integer to a list of digits, but it would be nice if the docstring explained how to do the inverse:\n\n```\nZ(x.digits(base), base)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8494\n\n",
    "created_at": "2010-03-11T05:40:42Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "docstring f or digits() should mention its inverse",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8494",
    "user": "ddrake"
}
```
Assignee: mvngu

One can use the `digits()` method to go from an integer to a list of digits, but it would be nice if the docstring explained how to do the inverse:

```
Z(x.digits(base), base)
```


Issue created by migration from https://trac.sagemath.org/ticket/8494





---

archive/issue_comments_076610.json:
```json
{
    "body": "I took the liberty of fixing up some of the ReST formatting, and also removed a comment that says \"s = 2003^100300000\" crashes Sage, because it doesn't anymore. (On my machine, at any rate.)",
    "created_at": "2010-03-11T07:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8494#issuecomment-76610",
    "user": "ddrake"
}
```

I took the liberty of fixing up some of the ReST formatting, and also removed a comment that says "s = 2003^100300000" crashes Sage, because it doesn't anymore. (On my machine, at any rate.)



---

archive/issue_comments_076611.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-11T07:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8494#issuecomment-76611",
    "user": "ddrake"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076612.json:
```json
{
    "body": "Attachment\n\nAdded a bit about `balanced_sum`; note that Sphinx won't do the hyperlink properly until we add `sage.misc.misc_c` to the reference manual.",
    "created_at": "2010-03-12T02:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8494#issuecomment-76612",
    "user": "ddrake"
}
```

Attachment

Added a bit about `balanced_sum`; note that Sphinx won't do the hyperlink properly until we add `sage.misc.misc_c` to the reference manual.



---

archive/issue_comments_076613.json:
```json
{
    "body": "Looks good to go into Sage 4.3.4.rc0.",
    "created_at": "2010-03-12T05:58:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8494#issuecomment-76613",
    "user": "mvngu"
}
```

Looks good to go into Sage 4.3.4.rc0.



---

archive/issue_comments_076614.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-12T05:58:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8494#issuecomment-76614",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076615.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-14T08:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8494#issuecomment-76615",
    "user": "mvngu"
}
```

Resolution: fixed
