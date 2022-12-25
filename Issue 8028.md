# Issue 8028: Improvements to element_wrapper

archive/issues_008028.json:
```json
{
    "body": "Assignee: sage-combinat\n\nKeywords: ElementWrapper, partial order\n\nImprovements to element_wrapper:\n\n- Don't define __cmp__ by default to not force a total order on subclasses\n- Define __lt__ to have elements incomparable by default\n- Provide alternative implementations as _cmp_by_value, _lt_by_value\n- Update accordingly:\n  - FiniteSemigroups().example\n- Misc polishing (copyright header, whitespace, ...)\n\nThis will be used by upcoming patches for crystals, ...\n\nIssue created by migration from https://trac.sagemath.org/ticket/8028\n\n",
    "created_at": "2010-01-21T17:08:34Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Improvements to element_wrapper",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8028",
    "user": "https://github.com/nthiery"
}
```
Assignee: sage-combinat

Keywords: ElementWrapper, partial order

Improvements to element_wrapper:

- Don't define __cmp__ by default to not force a total order on subclasses
- Define __lt__ to have elements incomparable by default
- Provide alternative implementations as _cmp_by_value, _lt_by_value
- Update accordingly:
  - FiniteSemigroups().example
- Misc polishing (copyright header, whitespace, ...)

This will be used by upcoming patches for crystals, ...

Issue created by migration from https://trac.sagemath.org/ticket/8028





---

archive/issue_comments_070003.json:
```json
{
    "body": "Attachment [trac_8028_element_wrapper-improvement-nt.patch](tarball://root/attachments/some-uuid/ticket8028/trac_8028_element_wrapper-improvement-nt.patch) by @nthiery created at 2010-01-21 17:13:25",
    "created_at": "2010-01-21T17:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8028#issuecomment-70003",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8028_element_wrapper-improvement-nt.patch](tarball://root/attachments/some-uuid/ticket8028/trac_8028_element_wrapper-improvement-nt.patch) by @nthiery created at 2010-01-21 17:13:25



---

archive/issue_comments_070004.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-21T17:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8028#issuecomment-70004",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070005.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-23T11:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8028#issuecomment-70005",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070006.json:
```json
{
    "body": "Everything ok !",
    "created_at": "2010-01-23T11:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8028#issuecomment-70006",
    "user": "https://github.com/hivert"
}
```

Everything ok !



---

archive/issue_events_008239.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-23T14:00:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8028",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8028#event-8239"
}
```



---

archive/issue_comments_070007.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T14:00:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8028#issuecomment-70007",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
