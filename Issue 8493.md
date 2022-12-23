# Issue 8493: Complex conjugation in Galois groups

archive/issues_008493.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  cremona\n\nKeywords: Galois groups\n\nThe attached patch contains some simple code which will return the element of the Galois group of a number field corresponding to complex conjugation (at a specified complex place, or the \"default\" complex embedding where that exists).\n\nThe code also uses embeddings into QQbar, so I've moved QQbar over to the new coercion model (a simple case of renaming the ``__call__`` method to ``_element_constructor_``).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8493\n\n",
    "created_at": "2010-03-10T21:20:09Z",
    "labels": [
        "number fields",
        "minor",
        "enhancement"
    ],
    "title": "Complex conjugation in Galois groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8493",
    "user": "davidloeffler"
}
```
Assignee: davidloeffler

CC:  cremona

Keywords: Galois groups

The attached patch contains some simple code which will return the element of the Galois group of a number field corresponding to complex conjugation (at a specified complex place, or the "default" complex embedding where that exists).

The code also uses embeddings into QQbar, so I've moved QQbar over to the new coercion model (a simple case of renaming the ``__call__`` method to ``_element_constructor_``).

Issue created by migration from https://trac.sagemath.org/ticket/8493





---

archive/issue_comments_076596.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-03-10T21:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76596",
    "user": "davidloeffler"
}
```

Attachment



---

archive/issue_comments_076597.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T23:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76597",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076598.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-13T14:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76598",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076599.json:
```json
{
    "body": "Looks good, applies fine to 4.3.4.alpha1, and all tests pass.",
    "created_at": "2010-03-13T14:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76599",
    "user": "cremona"
}
```

Looks good, applies fine to 4.3.4.alpha1, and all tests pass.



---

archive/issue_comments_076600.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-17T04:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76600",
    "user": "jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076601.json:
```json
{
    "body": "This doesn't apply cleanly; it apparently conflicts with a patch merged into Sage 4.4.alpha0.  Please rebase it against 4.4.alpha0 -- I don't think this will be too hard -- and we'll try hard to get this into 4.4.alpha1.",
    "created_at": "2010-04-17T04:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76601",
    "user": "jhpalmieri"
}
```

This doesn't apply cleanly; it apparently conflicts with a patch merged into Sage 4.4.alpha0.  Please rebase it against 4.4.alpha0 -- I don't think this will be too hard -- and we'll try hard to get this into 4.4.alpha1.



---

archive/issue_comments_076602.json:
```json
{
    "body": "Attachment\n\nnow rebased against 4.4.alpha0",
    "created_at": "2010-04-17T09:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76602",
    "user": "davidloeffler"
}
```

Attachment

now rebased against 4.4.alpha0



---

archive/issue_comments_076603.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-17T09:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76603",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076604.json:
```json
{
    "body": "The new patch is actually functionally identical to the old one -- it's only one of the \"context\" marker lines that has changed, due to another patch changing import statements in `galois_group.py` -- so I'm taking the liberty of setting it straight back to \"positive_review\".\n\nDavid",
    "created_at": "2010-04-17T10:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76604",
    "user": "davidloeffler"
}
```

The new patch is actually functionally identical to the old one -- it's only one of the "context" marker lines that has changed, due to another patch changing import statements in `galois_group.py` -- so I'm taking the liberty of setting it straight back to "positive_review".

David



---

archive/issue_comments_076605.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-17T10:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76605",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076606.json:
```json
{
    "body": "I am happy with this (as original reviewer).  I looked at the new patch, but have not tested it as I am still building 4.4.alpha0.",
    "created_at": "2010-04-17T11:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76606",
    "user": "cremona"
}
```

I am happy with this (as original reviewer).  I looked at the new patch, but have not tested it as I am still building 4.4.alpha0.



---

archive/issue_comments_076607.json:
```json
{
    "body": "Replying to [comment:5 davidloeffler]:\n> I'm taking the liberty of setting it straight back to \"positive_review\".\n\nI think that's fine.  It applies cleanly to 4.4.alpha0; I'm checking doctests and will report if there are any problems.  Otherwise, it will get merged into 4.4.alpha1.",
    "created_at": "2010-04-17T18:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76607",
    "user": "jhpalmieri"
}
```

Replying to [comment:5 davidloeffler]:
> I'm taking the liberty of setting it straight back to "positive_review".

I think that's fine.  It applies cleanly to 4.4.alpha0; I'm checking doctests and will report if there are any problems.  Otherwise, it will get merged into 4.4.alpha1.



---

archive/issue_comments_076608.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76608",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_076609.json:
```json
{
    "body": "Merged \"trac_8493-complex_conjugation.2.patch\" into 4.4.alpha1",
    "created_at": "2010-04-19T05:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76609",
    "user": "jhpalmieri"
}
```

Merged "trac_8493-complex_conjugation.2.patch" into 4.4.alpha1
