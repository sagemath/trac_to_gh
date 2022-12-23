# Issue 5978: Can't construct the quotient of an univariate polynomial ring by it's zero ideal

archive/issues_005978.json:
```json
{
    "body": "Assignee: tbd\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5978\n\n",
    "created_at": "2009-05-04T08:10:39Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "title": "Can't construct the quotient of an univariate polynomial ring by it's zero ideal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5978",
    "user": "jmbr"
}
```
Assignee: tbd



Issue created by migration from https://trac.sagemath.org/ticket/5978





---

archive/issue_comments_047479.json:
```json
{
    "body": "Do **not** attach the error message, but post it verbatim into the ticket.\n\nAlso **always** assign a milestone.",
    "created_at": "2009-05-04T08:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5978#issuecomment-47479",
    "user": "mabshoff"
}
```

Do **not** attach the error message, but post it verbatim into the ticket.

Also **always** assign a milestone.



---

archive/issue_comments_047480.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-11-18T07:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5978#issuecomment-47480",
    "user": "tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_047481.json:
```json
{
    "body": "Fixed by making the quotient by a zero ideal return the original ring.\n\n```\nsage: ZZ.quotient(ZZ.zero_ideal()) is ZZ\nTrue\nsage: R = QQ['x']\nsage: R.quotient(R.zero_ideal()) is R\nTrue\n```\n",
    "created_at": "2012-11-18T07:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5978#issuecomment-47481",
    "user": "tscrim"
}
```

Fixed by making the quotient by a zero ideal return the original ring.

```
sage: ZZ.quotient(ZZ.zero_ideal()) is ZZ
True
sage: R = QQ['x']
sage: R.quotient(R.zero_ideal()) is R
True
```




---

archive/issue_comments_047482.json:
```json
{
    "body": "Fixed this for `quotient_by_principal_ideal()` method in polynomial ring as well.\n\nFor patchbot:\n\nApply: trac_5978-quotient_zero_ideal-ts.2.patch",
    "created_at": "2012-11-18T07:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5978#issuecomment-47482",
    "user": "tscrim"
}
```

Fixed this for `quotient_by_principal_ideal()` method in polynomial ring as well.

For patchbot:

Apply: trac_5978-quotient_zero_ideal-ts.2.patch



---

archive/issue_comments_047483.json:
```json
{
    "body": "Fixed other doctests.\n\nFor patchbot:\n\nApply: trac_5978-quotient_zero_ideal-ts.patch",
    "created_at": "2012-11-18T19:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5978#issuecomment-47483",
    "user": "tscrim"
}
```

Fixed other doctests.

For patchbot:

Apply: trac_5978-quotient_zero_ideal-ts.patch



---

archive/issue_comments_047484.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-20T18:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5978#issuecomment-47484",
    "user": "lftabera"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047485.json:
```json
{
    "body": "the patch looks good to me. I have made also further tests. Positive review.\n\nApply: trac_5978-quotient_zero_ideal-ts.patch",
    "created_at": "2013-02-20T18:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5978#issuecomment-47485",
    "user": "lftabera"
}
```

the patch looks good to me. I have made also further tests. Positive review.

Apply: trac_5978-quotient_zero_ideal-ts.patch



---

archive/issue_comments_047486.json:
```json
{
    "body": "Thank you for the review.\n\nTravis",
    "created_at": "2013-02-20T18:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5978#issuecomment-47486",
    "user": "tscrim"
}
```

Thank you for the review.

Travis



---

archive/issue_comments_047487.json:
```json
{
    "body": "Attachment\n\nRebased to sage-5.8.beta0.",
    "created_at": "2013-02-21T10:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5978#issuecomment-47487",
    "user": "jdemeyer"
}
```

Attachment

Rebased to sage-5.8.beta0.



---

archive/issue_comments_047488.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-02-22T19:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5978#issuecomment-47488",
    "user": "jdemeyer"
}
```

Resolution: fixed
