# Issue 7474: [with patch, needs review]Expose some more functionality of fmz_poly

archive/issues_007474.json:
```json
{
    "body": "Assignee: mraum\n\nKeywords: flint, fmpz_poly, integers\n\nThis makes the FLINT wrapper in sage.libs.flint.fmpz_poly handle big integers correctly and exposes shifts and derivatives.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7474\n\n",
    "created_at": "2009-11-16T17:15:41Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review]Expose some more functionality of fmz_poly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7474",
    "user": "mraum"
}
```
Assignee: mraum

Keywords: flint, fmpz_poly, integers

This makes the FLINT wrapper in sage.libs.flint.fmpz_poly handle big integers correctly and exposes shifts and derivatives.

Issue created by migration from https://trac.sagemath.org/ticket/7474





---

archive/issue_comments_062990.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-16T17:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62990",
    "user": "mraum"
}
```

Attachment



---

archive/issue_comments_062991.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-17T07:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62991",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_062992.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-17T07:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62992",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062993.json:
```json
{
    "body": "Actually, the derivative of 1 + 2*x + 6*x^2 should be [2, 12] and not [4, 18].  With this change the tests pass.",
    "created_at": "2009-11-17T07:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62993",
    "user": "mhansen"
}
```

Actually, the derivative of 1 + 2*x + 6*x^2 should be [2, 12] and not [4, 18].  With this change the tests pass.



---

archive/issue_comments_062994.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T07:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62994",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062995.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T07:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62995",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_062996.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-17T07:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62996",
    "user": "mhansen"
}
```

Attachment
