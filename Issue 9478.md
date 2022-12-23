# Issue 9478: LaTeX error for iterated polynomial rings

archive/issues_009478.json:
```json
{
    "body": "Assignee: burcin\n\nKeywords: latex\n\nI have just discovered the following:\n\n```\nsage: R1.<xi, x> = QQ[]\nsage: print latex(xi*x)\n\\xi x\nsage: R2.<a> = QQ[]\nsage: R3.<xi, x> = R2[]\nsage: print latex(xi*x)\n\\xix\n```\n\nNotice no space between variables on the last line. Of course, this gives an error.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9478\n\n",
    "created_at": "2010-07-12T01:45:07Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "LaTeX error for iterated polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9478",
    "user": "novoselt"
}
```
Assignee: burcin

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

archive/issue_comments_090990.json:
```json
{
    "body": "I am currently working \u00a0on a rewrite of the patch to\u00a0#8938.\u00a0\u00a0I will try to correct this at the same time.",
    "created_at": "2010-07-12T07:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90990",
    "user": "fwclarke"
}
```

I am currently working  on a rewrite of the patch to #8938.  I will try to correct this at the same time.



---

archive/issue_comments_090991.json:
```json
{
    "body": "Changing component from symbolics to basic arithmetic.",
    "created_at": "2010-08-28T11:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90991",
    "user": "burcin"
}
```

Changing component from symbolics to basic arithmetic.



---

archive/issue_comments_090992.json:
```json
{
    "body": "Changing assignee from burcin to AlexGhitza.",
    "created_at": "2010-08-28T11:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90992",
    "user": "burcin"
}
```

Changing assignee from burcin to AlexGhitza.



---

archive/issue_comments_090993.json:
```json
{
    "body": "This doesn't belong in the symbolics component.",
    "created_at": "2010-08-28T11:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90993",
    "user": "burcin"
}
```

This doesn't belong in the symbolics component.



---

archive/issue_comments_090994.json:
```json
{
    "body": "This issue is still present in Sage-4.6.",
    "created_at": "2010-11-08T15:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90994",
    "user": "novoselt"
}
```

This issue is still present in Sage-4.6.



---

archive/issue_comments_090995.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-06-17T22:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90995",
    "user": "novoselt"
}
```

Attachment



---

archive/issue_comments_090996.json:
```json
{
    "body": "Changing keywords from \"latex\" to \"latex, sd31\".",
    "created_at": "2011-06-17T22:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90996",
    "user": "novoselt"
}
```

Changing keywords from "latex" to "latex, sd31".



---

archive/issue_comments_090997.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-17T23:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90997",
    "user": "novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090998.json:
```json
{
    "body": "Changing keywords from \"latex, sd31\" to \"latex, sd31, beginner\".",
    "created_at": "2011-06-17T23:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90998",
    "user": "novoselt"
}
```

Changing keywords from "latex, sd31" to "latex, sd31, beginner".



---

archive/issue_comments_090999.json:
```json
{
    "body": "Looks fine, applies against 4.7, no doctest failures.",
    "created_at": "2011-06-18T13:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-90999",
    "user": "kedlaya"
}
```

Looks fine, applies against 4.7, no doctest failures.



---

archive/issue_comments_091000.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-18T13:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-91000",
    "user": "kedlaya"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091001.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-07-04T12:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9478#issuecomment-91001",
    "user": "jdemeyer"
}
```

Resolution: fixed
