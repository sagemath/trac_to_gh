# Issue 5066: [with patch, needs review] break out relative number fields into separate file

archive/issues_005066.json:
```json
{
    "body": "Assignee: was\n\nKeywords: relative number fields files\n\nThis has been some time coming, but let's separate relative number fields from generic/absolute number fields now, while I'm looking at them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5066\n\n",
    "created_at": "2009-01-23T08:59:32Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] break out relative number fields into separate file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5066",
    "user": "ncalexan"
}
```
Assignee: was

Keywords: relative number fields files

This has been some time coming, but let's separate relative number fields from generic/absolute number fields now, while I'm looking at them.

Issue created by migration from https://trac.sagemath.org/ticket/5066





---

archive/issue_comments_038592.json:
```json
{
    "body": "Attachment\n\nFails a doctest, to be addressed by patches to #1357 (which will depend on this)",
    "created_at": "2009-01-23T09:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5066#issuecomment-38592",
    "user": "ncalexan"
}
```

Attachment

Fails a doctest, to be addressed by patches to #1357 (which will depend on this)



---

archive/issue_comments_038593.json:
```json
{
    "body": "Looks good, assuming that the other patch you mentioned (which isn't #1357) gets in at the same time.  The only change that needs to be made is in sage.rings.polynomials.polynomial_quotient_ring_element, changing number_field to number_field_rel a couple places.",
    "created_at": "2009-01-24T09:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5066#issuecomment-38593",
    "user": "roed"
}
```

Looks good, assuming that the other patch you mentioned (which isn't #1357) gets in at the same time.  The only change that needs to be made is in sage.rings.polynomials.polynomial_quotient_ring_element, changing number_field to number_field_rel a couple places.



---

archive/issue_comments_038594.json:
```json
{
    "body": "Patch should be at #1367, sorry.  With #5066 and #1367, all doctests pass on sage.math.",
    "created_at": "2009-01-24T10:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5066#issuecomment-38594",
    "user": "ncalexan"
}
```

Patch should be at #1367, sorry.  With #5066 and #1367, all doctests pass on sage.math.



---

archive/issue_comments_038595.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T05:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5066#issuecomment-38595",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_038596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T05:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5066#issuecomment-38596",
    "user": "mabshoff"
}
```

Resolution: fixed
