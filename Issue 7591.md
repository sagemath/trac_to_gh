# Issue 7591: Boolean Polynomial Ring coercion broken

archive/issues_007591.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin\n\nThis is really bad\n\n\n```\nsage: B.<a,b,c> = BooleanPolynomialRing(order='lex')\nsage: P.<a,b,c> = BooleanPolynomialRing(order='degrevlex')\nsage: P(B('a')) # good\na\nsage: B(P('c')) # urgh!\na\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7591\n\n",
    "created_at": "2009-12-03T12:53:02Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Boolean Polynomial Ring coercion broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7591",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin

This is really bad


```
sage: B.<a,b,c> = BooleanPolynomialRing(order='lex')
sage: P.<a,b,c> = BooleanPolynomialRing(order='degrevlex')
sage: P(B('a')) # good
a
sage: B(P('c')) # urgh!
a
```


Issue created by migration from https://trac.sagemath.org/ticket/7591





---

archive/issue_comments_064605.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-04T15:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7591#issuecomment-64605",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064606.json:
```json
{
    "body": "The attached patch fixes the issue for me. Burcin, can I ask you to review this patch?",
    "created_at": "2009-12-04T15:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7591#issuecomment-64606",
    "user": "https://github.com/malb"
}
```

The attached patch fixes the issue for me. Burcin, can I ask you to review this patch?



---

archive/issue_comments_064607.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-06T17:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7591#issuecomment-64607",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064608.json:
```json
{
    "body": "Attachment [trac_7591.patch](tarball://root/attachments/some-uuid/ticket7591/trac_7591.patch) by @burcin created at 2009-12-06 17:39:02\n\nLooks good to me.",
    "created_at": "2009-12-06T17:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7591#issuecomment-64608",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7591.patch](tarball://root/attachments/some-uuid/ticket7591/trac_7591.patch) by @burcin created at 2009-12-06 17:39:02

Looks good to me.



---

archive/issue_comments_064609.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-07T08:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7591#issuecomment-64609",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
