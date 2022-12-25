# Issue 3680: NumberFieldFractionalIdeal should not be a subclass of Ideal_generic

archive/issues_003680.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  alexghitza @pjbruin\n\nWhy is `NumberFieldFractionalIdeal` a subclass of `Ideal_generic`?\n\nA fractional ideal is **not** an ideal.\n\nThis makes about as much as sense as having `Rational` be a subclass of `Integer`.\n\nThis has been discussed before:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/0b01d58d8c3565c2/c081ba96b5fed6eb?#c081ba96b5fed6eb\n\nAnd it came up again recently in #1367.\n\nThere seem to be serious design issues with the whole algebraic number theory setup in Sage which make it very frustrating to do any serious work on things like #1367.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3680\n\n",
    "created_at": "2008-07-19T13:36:55Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "NumberFieldFractionalIdeal should not be a subclass of Ideal_generic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3680",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: tbd

CC:  alexghitza @pjbruin

Why is `NumberFieldFractionalIdeal` a subclass of `Ideal_generic`?

A fractional ideal is **not** an ideal.

This makes about as much as sense as having `Rational` be a subclass of `Integer`.

This has been discussed before:

http://groups.google.com/group/sage-devel/browse_thread/thread/0b01d58d8c3565c2/c081ba96b5fed6eb?#c081ba96b5fed6eb

And it came up again recently in #1367.

There seem to be serious design issues with the whole algebraic number theory setup in Sage which make it very frustrating to do any serious work on things like #1367.


Issue created by migration from https://trac.sagemath.org/ticket/3680





---

archive/issue_comments_026008.json:
```json
{
    "body": "Changing component from algebra to number theory.",
    "created_at": "2009-01-28T22:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3680#issuecomment-26008",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to number theory.



---

archive/issue_comments_026009.json:
```json
{
    "body": "Changing assignee from tbd to @williamstein.",
    "created_at": "2009-01-28T22:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3680#issuecomment-26009",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from tbd to @williamstein.



---

archive/issue_comments_026010.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T20:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3680#issuecomment-26010",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_026011.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T20:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3680#issuecomment-26011",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.
