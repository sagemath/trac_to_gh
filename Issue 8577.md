# Issue 8577: Fix ETuple.eadd_p

archive/issues_008577.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  mjo\n\nThis should return `True` not `False` (reported by\nMichael Bachtold)\n\n\n```python\nsage: from sage.rings.polynomial.polydict import ETuple\nsage: ETuple([0,1]).eadd_p(1, 0)==ETuple([1,1])\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8577\n\n",
    "created_at": "2010-03-22T11:51:35Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "Fix ETuple.eadd_p",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8577",
    "user": "malb"
}
```
Assignee: AlexGhitza

CC:  mjo

This should return `True` not `False` (reported by
Michael Bachtold)


```python
sage: from sage.rings.polynomial.polydict import ETuple
sage: ETuple([0,1]).eadd_p(1, 0)==ETuple([1,1])
```



Issue created by migration from https://trac.sagemath.org/ticket/8577





---

archive/issue_comments_077687.json:
```json
{
    "body": "Attachment [etuple_eadd_fix.patch](tarball://root/attachments/some-uuid/ticket8577/etuple_eadd_fix.patch) by mjo created at 2012-01-16 03:16:56",
    "created_at": "2012-01-16T03:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8577#issuecomment-77687",
    "user": "mjo"
}
```

Attachment [etuple_eadd_fix.patch](tarball://root/attachments/some-uuid/ticket8577/etuple_eadd_fix.patch) by mjo created at 2012-01-16 03:16:56



---

archive/issue_comments_077688.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-16T03:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8577#issuecomment-77688",
    "user": "mjo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077689.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-28T21:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8577#issuecomment-77689",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077690.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2012-03-28T21:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8577#issuecomment-77690",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_077691.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-04-19T06:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8577#issuecomment-77691",
    "user": "jdemeyer"
}
```

Resolution: fixed
