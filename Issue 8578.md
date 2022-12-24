# Issue 8578: method int_repr only works for small finite fields

archive/issues_008578.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f41d594281e843d9):\n\n```\nFor a finite field of, say 2^6 elements, an object representing an\nelement of such a field has a method called int_repr() that returns\nthe object's integer representation. However, if we are dealing with,\nsay GF(7^100), an object representing an element of such a field\ndoesn't have a corresponding int_repr() method. The report below\nincludes such a method, which is meant to work for a finite field of\nany order.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8578\n\n",
    "created_at": "2010-03-22T12:00:54Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "method int_repr only works for small finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8578",
    "user": "mvngu"
}
```
Assignee: AlexGhitza

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f41d594281e843d9):

```
For a finite field of, say 2^6 elements, an object representing an
element of such a field has a method called int_repr() that returns
the object's integer representation. However, if we are dealing with,
say GF(7^100), an object representing an element of such a field
doesn't have a corresponding int_repr() method. The report below
includes such a method, which is meant to work for a finite field of
any order.
```


Issue created by migration from https://trac.sagemath.org/ticket/8578





---

archive/issue_comments_077692.json:
```json
{
    "body": "Apparently this is still an issue, see [this stack overflow question](http://stackoverflow.com/questions/36391931/how-do-i-get-the-int-representation-of-a-big-field-in-sage).",
    "created_at": "2016-04-04T14:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8578#issuecomment-77692",
    "user": "kcrisman"
}
```

Apparently this is still an issue, see [this stack overflow question](http://stackoverflow.com/questions/36391931/how-do-i-get-the-int-representation-of-a-big-field-in-sage).



---

archive/issue_comments_077693.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-04-05T01:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8578#issuecomment-77693",
    "user": "@DaveWitteMorris"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077694.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2021-04-05T01:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8578#issuecomment-77694",
    "user": "@DaveWitteMorris"
}
```

Changing priority from major to minor.



---

archive/issue_comments_077695.json:
```json
{
    "body": "Duplicate of #31605.",
    "created_at": "2021-04-05T01:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8578#issuecomment-77695",
    "user": "@DaveWitteMorris"
}
```

Duplicate of #31605.



---

archive/issue_comments_077696.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-04-11T23:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8578#issuecomment-77696",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077697.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-06-24T20:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8578#issuecomment-77697",
    "user": "mkoeppe"
}
```

Resolution: invalid
