# Issue 9006: Segfault evaluating large degree polynomials

archive/issues_009006.json:
```json
{
    "body": "Assignee: @aghitza\n\nsage: f = ZZ!['x'](1000000 * ![1])\nsage: f(1)\n/home/bosman/sage-4.4.2/local/bin/sage-sage: Zeile 206: 32438 Segmentation fault      sage-ipython \"$`@`\" -i\n\n\nIt might be in sage/rings/polynomial/polynomial_compiled.pyx: binary_pd has methods that use a recursive implementation, causing a stack overflow (but I don't have time now, so I'll try to look at it more carefully later).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9006\n\n",
    "created_at": "2010-05-21T12:12:03Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Segfault evaluating large degree polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9006",
    "user": "johanbosman"
}
```
Assignee: @aghitza

sage: f = ZZ!['x'](1000000 * ![1])
sage: f(1)
/home/bosman/sage-4.4.2/local/bin/sage-sage: Zeile 206: 32438 Segmentation fault      sage-ipython "$`@`" -i


It might be in sage/rings/polynomial/polynomial_compiled.pyx: binary_pd has methods that use a recursive implementation, causing a stack overflow (but I don't have time now, so I'll try to look at it more carefully later).

Issue created by migration from https://trac.sagemath.org/ticket/9006





---

archive/issue_comments_083309.json:
```json
{
    "body": "Attachment [trac_9006_polynomial_eval.patch](tarball://root/attachments/some-uuid/ticket9006/trac_9006_polynomial_eval.patch) by johanbosman created at 2010-05-24 15:58:02",
    "created_at": "2010-05-24T15:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9006#issuecomment-83309",
    "user": "johanbosman"
}
```

Attachment [trac_9006_polynomial_eval.patch](tarball://root/attachments/some-uuid/ticket9006/trac_9006_polynomial_eval.patch) by johanbosman created at 2010-05-24 15:58:02



---

archive/issue_comments_083310.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-24T16:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9006#issuecomment-83310",
    "user": "johanbosman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083311.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-06-05T00:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9006#issuecomment-83311",
    "user": "@aghitza"
}
```

Looks good.



---

archive/issue_comments_083312.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-05T00:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9006#issuecomment-83312",
    "user": "@aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083313.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9006#issuecomment-83313",
    "user": "@mwhansen"
}
```

Resolution: fixed
