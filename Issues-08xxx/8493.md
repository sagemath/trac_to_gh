# Issue 8493: Complex conjugation in Galois groups

archive/issues_008493.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @JohnCremona\n\nKeywords: Galois groups\n\nThe attached patch contains some simple code which will return the element of the Galois group of a number field corresponding to complex conjugation (at a specified complex place, or the \"default\" complex embedding where that exists).\n\nThe code also uses embeddings into QQbar, so I've moved QQbar over to the new coercion model (a simple case of renaming the ``__call__`` method to ``_element_constructor_``).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8493\n\n",
    "closed_at": "2010-04-19T05:13:40Z",
    "created_at": "2010-03-10T21:20:09Z",
    "labels": [
        "component: number fields",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Complex conjugation in Galois groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8493",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @loefflerd

CC:  @JohnCremona

Keywords: Galois groups

The attached patch contains some simple code which will return the element of the Galois group of a number field corresponding to complex conjugation (at a specified complex place, or the "default" complex embedding where that exists).

The code also uses embeddings into QQbar, so I've moved QQbar over to the new coercion model (a simple case of renaming the ``__call__`` method to ``_element_constructor_``).

Issue created by migration from https://trac.sagemath.org/ticket/8493





---

archive/issue_comments_076469.json:
```json
{
    "body": "Attachment [trac_8493-complex_conjugation.patch](tarball://root/attachments/some-uuid/ticket8493/trac_8493-complex_conjugation.patch) by @loefflerd created at 2010-03-10 21:22:31",
    "created_at": "2010-03-10T21:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76469",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8493-complex_conjugation.patch](tarball://root/attachments/some-uuid/ticket8493/trac_8493-complex_conjugation.patch) by @loefflerd created at 2010-03-10 21:22:31



---

archive/issue_comments_076470.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T23:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76470",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076471.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-13T14:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76471",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076472.json:
```json
{
    "body": "Looks good, applies fine to 4.3.4.alpha1, and all tests pass.",
    "created_at": "2010-03-13T14:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76472",
    "user": "https://github.com/JohnCremona"
}
```

Looks good, applies fine to 4.3.4.alpha1, and all tests pass.



---

archive/issue_comments_076473.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-17T04:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76473",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076474.json:
```json
{
    "body": "This doesn't apply cleanly; it apparently conflicts with a patch merged into Sage 4.4.alpha0.  Please rebase it against 4.4.alpha0 -- I don't think this will be too hard -- and we'll try hard to get this into 4.4.alpha1.",
    "created_at": "2010-04-17T04:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76474",
    "user": "https://github.com/jhpalmieri"
}
```

This doesn't apply cleanly; it apparently conflicts with a patch merged into Sage 4.4.alpha0.  Please rebase it against 4.4.alpha0 -- I don't think this will be too hard -- and we'll try hard to get this into 4.4.alpha1.



---

archive/issue_comments_076475.json:
```json
{
    "body": "Attachment [trac_8493-complex_conjugation.2.patch](tarball://root/attachments/some-uuid/ticket8493/trac_8493-complex_conjugation.2.patch) by @loefflerd created at 2010-04-17 09:55:07\n\nnow rebased against 4.4.alpha0",
    "created_at": "2010-04-17T09:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76475",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8493-complex_conjugation.2.patch](tarball://root/attachments/some-uuid/ticket8493/trac_8493-complex_conjugation.2.patch) by @loefflerd created at 2010-04-17 09:55:07

now rebased against 4.4.alpha0



---

archive/issue_comments_076476.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-17T09:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76476",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076477.json:
```json
{
    "body": "The new patch is actually functionally identical to the old one -- it's only one of the \"context\" marker lines that has changed, due to another patch changing import statements in `galois_group.py` -- so I'm taking the liberty of setting it straight back to \"positive_review\".\n\nDavid",
    "created_at": "2010-04-17T10:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76477",
    "user": "https://github.com/loefflerd"
}
```

The new patch is actually functionally identical to the old one -- it's only one of the "context" marker lines that has changed, due to another patch changing import statements in `galois_group.py` -- so I'm taking the liberty of setting it straight back to "positive_review".

David



---

archive/issue_comments_076478.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-17T10:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76478",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076479.json:
```json
{
    "body": "I am happy with this (as original reviewer).  I looked at the new patch, but have not tested it as I am still building 4.4.alpha0.",
    "created_at": "2010-04-17T11:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76479",
    "user": "https://github.com/JohnCremona"
}
```

I am happy with this (as original reviewer).  I looked at the new patch, but have not tested it as I am still building 4.4.alpha0.



---

archive/issue_comments_076480.json:
```json
{
    "body": "Replying to [comment:5 davidloeffler]:\n> I'm taking the liberty of setting it straight back to \"positive_review\".\n\n\nI think that's fine.  It applies cleanly to 4.4.alpha0; I'm checking doctests and will report if there are any problems.  Otherwise, it will get merged into 4.4.alpha1.",
    "created_at": "2010-04-17T18:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76480",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:5 davidloeffler]:
> I'm taking the liberty of setting it straight back to "positive_review".


I think that's fine.  It applies cleanly to 4.4.alpha0; I'm checking doctests and will report if there are any problems.  Otherwise, it will get merged into 4.4.alpha1.



---

archive/issue_events_020397.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-19T05:13:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8493#event-20397"
}
```



---

archive/issue_comments_076481.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76481",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_076482.json:
```json
{
    "body": "Merged \"trac_8493-complex_conjugation.2.patch\" into 4.4.alpha1",
    "created_at": "2010-04-19T05:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8493#issuecomment-76482",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8493-complex_conjugation.2.patch" into 4.4.alpha1
