# Issue 9478: LaTeX error for iterated polynomial rings

archive/issues_009478.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: latex\n\nI have just discovered the following:\n\n```\nsage: R1.<xi, x> = QQ[]\nsage: print latex(xi*x)\n\\xi x\nsage: R2.<a> = QQ[]\nsage: R3.<xi, x> = R2[]\nsage: print latex(xi*x)\n\\xix\n```\n\nNotice no space between variables on the last line. Of course, this gives an error.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9478\n\n",
    "created_at": "2010-07-12T01:45:07Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "LaTeX error for iterated polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9478",
    "user": "https://github.com/novoselt"
}
```
Assignee: @burcin

Keywords: latex

I have just discovered the following:

```
sage: R1.<xi, x> = QQ[]
sage: print latex(xi*x)
\xi x
sage: R2.<a> = QQ[]
sage: R3.<xi, x> = R2[]
sage: print latex(xi*x)
\xix
```

Notice no space between variables on the last line. Of course, this gives an error.

Issue created by migration from https://trac.sagemath.org/ticket/9478





---

archive/issue_comments_090838.json:
```json
{
    "body": "I am currently working \u00a0on a rewrite of the patch to\u00a0#8938.\u00a0\u00a0I will try to correct this at the same time.",
    "created_at": "2010-07-12T07:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90838",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

I am currently working  on a rewrite of the patch to #8938.  I will try to correct this at the same time.



---

archive/issue_comments_090839.json:
```json
{
    "body": "Changing component from symbolics to basic arithmetic.",
    "created_at": "2010-08-28T11:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90839",
    "user": "https://github.com/burcin"
}
```

Changing component from symbolics to basic arithmetic.



---

archive/issue_comments_090840.json:
```json
{
    "body": "Changing assignee from @burcin to @aghitza.",
    "created_at": "2010-08-28T11:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90840",
    "user": "https://github.com/burcin"
}
```

Changing assignee from @burcin to @aghitza.



---

archive/issue_comments_090841.json:
```json
{
    "body": "This doesn't belong in the symbolics component.",
    "created_at": "2010-08-28T11:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90841",
    "user": "https://github.com/burcin"
}
```

This doesn't belong in the symbolics component.



---

archive/issue_comments_090842.json:
```json
{
    "body": "This issue is still present in Sage-4.6.",
    "created_at": "2010-11-08T15:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90842",
    "user": "https://github.com/novoselt"
}
```

This issue is still present in Sage-4.6.



---

archive/issue_comments_090843.json:
```json
{
    "body": "Attachment [trac_9478_bug_in_LaTeXing_of_iterated_polynomials.patch](tarball://root/attachments/some-uuid/ticket9478/trac_9478_bug_in_LaTeXing_of_iterated_polynomials.patch) by @novoselt created at 2011-06-17 22:46:26",
    "created_at": "2011-06-17T22:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90843",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9478_bug_in_LaTeXing_of_iterated_polynomials.patch](tarball://root/attachments/some-uuid/ticket9478/trac_9478_bug_in_LaTeXing_of_iterated_polynomials.patch) by @novoselt created at 2011-06-17 22:46:26



---

archive/issue_comments_090844.json:
```json
{
    "body": "Changing keywords from \"latex\" to \"latex, sd31\".",
    "created_at": "2011-06-17T22:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90844",
    "user": "https://github.com/novoselt"
}
```

Changing keywords from "latex" to "latex, sd31".



---

archive/issue_comments_090845.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-17T23:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90845",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090846.json:
```json
{
    "body": "Changing keywords from \"latex, sd31\" to \"latex, sd31, beginner\".",
    "created_at": "2011-06-17T23:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90846",
    "user": "https://github.com/novoselt"
}
```

Changing keywords from "latex, sd31" to "latex, sd31, beginner".



---

archive/issue_comments_090847.json:
```json
{
    "body": "Looks fine, applies against 4.7, no doctest failures.",
    "created_at": "2011-06-18T13:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90847",
    "user": "https://github.com/kedlaya"
}
```

Looks fine, applies against 4.7, no doctest failures.



---

archive/issue_comments_090848.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-18T13:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90848",
    "user": "https://github.com/kedlaya"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090849.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-07-04T12:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90849",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009630.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-07-04T12:02:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9478#event-9630"
}
```
