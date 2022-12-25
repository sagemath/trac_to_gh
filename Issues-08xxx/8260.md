# Issue 8260: valuation of zero is wrong for Qq

archive/issues_008260.json:
```json
{
    "body": "Assignee: @roed314\n\nCC:  @roed314 @robertwb\n\nThis is ok:\n\n```\nsage: K = Qp(5)\nsage: x = K(0)\nsage: x.valuation()\n+Infinity\n```\n\nThis is bad:\n\n```\nsage: K.<a> = Qq(25)\nsage: x = K(0)\nsage: x.valuation()\n1073741823\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8260\n\n",
    "closed_at": "2010-03-03T14:47:14Z",
    "created_at": "2010-02-14T02:25:43Z",
    "labels": [
        "component: padics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "valuation of zero is wrong for Qq",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8260",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @roed314

CC:  @roed314 @robertwb

This is ok:

```
sage: K = Qp(5)
sage: x = K(0)
sage: x.valuation()
+Infinity
```

This is bad:

```
sage: K.<a> = Qq(25)
sage: x = K(0)
sage: x.valuation()
1073741823
```


Issue created by migration from https://trac.sagemath.org/ticket/8260





---

archive/issue_events_019776.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2010-02-21T03:40:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8260",
    "milestone": "sage-4.3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8260#event-19776"
}
```



---

archive/issue_comments_072982.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-21T03:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8260#issuecomment-72982",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072983.json:
```json
{
    "body": "Attachment [8260-Qq-valuation.patch](tarball://root/attachments/some-uuid/ticket8260/8260-Qq-valuation.patch) by @robertwb created at 2010-02-21 03:40:44\n\nThere were inconsistent definitions of maxordp.",
    "created_at": "2010-02-21T03:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8260#issuecomment-72983",
    "user": "https://github.com/robertwb"
}
```

Attachment [8260-Qq-valuation.patch](tarball://root/attachments/some-uuid/ticket8260/8260-Qq-valuation.patch) by @robertwb created at 2010-02-21 03:40:44

There were inconsistent definitions of maxordp.



---

archive/issue_comments_072984.json:
```json
{
    "body": "Yep, that should do it.  Doctests all pass.",
    "created_at": "2010-02-21T18:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8260#issuecomment-72984",
    "user": "https://github.com/roed314"
}
```

Yep, that should do it.  Doctests all pass.



---

archive/issue_comments_072985.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-21T18:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8260#issuecomment-72985",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019777.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-03T14:47:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8260",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8260#event-19777"
}
```



---

archive/issue_comments_072986.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8260#issuecomment-72986",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
