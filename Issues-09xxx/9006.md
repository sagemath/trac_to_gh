# Issue 9006: Segfault evaluating large degree polynomials (easy review)

archive/issues_009006.json:
```json
{
    "body": "Assignee: @aghitza\n\nsage: f = ZZ!['x'](1000000 * ![1])\nsage: f(1)\n/home/bosman/sage-4.4.2/local/bin/sage-sage: Zeile 206: 32438 Segmentation fault      sage-ipython \"$`@`\" -i\n\nIt is caused by sage/rings/polynomial/polynomial_compiled.pyx: generic_pd and derived classes create objects having large chains of dependencies.  They make the recursively implemented methods as well as the garbage collector run out of stack space.  I decided to simply use the 'naive' method for evaluating large degree polynomials.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9006\n\n",
    "closed_at": "2010-06-06T01:15:39Z",
    "created_at": "2010-05-21T12:12:03Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Segfault evaluating large degree polynomials (easy review)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9006",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```
Assignee: @aghitza

sage: f = ZZ!['x'](1000000 * ![1])
sage: f(1)
/home/bosman/sage-4.4.2/local/bin/sage-sage: Zeile 206: 32438 Segmentation fault      sage-ipython "$`@`" -i

It is caused by sage/rings/polynomial/polynomial_compiled.pyx: generic_pd and derived classes create objects having large chains of dependencies.  They make the recursively implemented methods as well as the garbage collector run out of stack space.  I decided to simply use the 'naive' method for evaluating large degree polynomials.

Issue created by migration from https://trac.sagemath.org/ticket/9006





---

archive/issue_comments_083173.json:
```json
{
    "body": "Attachment [trac_9006_polynomial_eval.patch](tarball://root/attachments/some-uuid/ticket9006/trac_9006_polynomial_eval.patch) by johanbosman created at 2010-05-24 15:58:02",
    "created_at": "2010-05-24T15:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9006#issuecomment-83173",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

Attachment [trac_9006_polynomial_eval.patch](tarball://root/attachments/some-uuid/ticket9006/trac_9006_polynomial_eval.patch) by johanbosman created at 2010-05-24 15:58:02



---

archive/issue_comments_083174.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-24T16:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9006#issuecomment-83174",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083175.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-06-05T00:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9006#issuecomment-83175",
    "user": "https://github.com/aghitza"
}
```

Looks good.



---

archive/issue_comments_083176.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-05T00:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9006#issuecomment-83176",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022038.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T01:15:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9006",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9006#event-22038"
}
```



---

archive/issue_comments_083177.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9006#issuecomment-83177",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
