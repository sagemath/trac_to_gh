# Issue 8367: element_class of Subsets is broken

archive/issues_008367.json:
```json
{
    "body": "Assignee: giraudo\n\nKeywords: Subsets element_class\n\nelement_class of Subsets is broken\n\n```\nsage: s = Subsets(Set([1]))\nsage: e = s.first()\nsage: isinstance(e, s.element_class)\nFalse\n```\n\n\nNote: this should be caught by setting good categories \n\n```\nsage: s.category()\nCategory of objects\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8367\n\n",
    "created_at": "2010-02-25T17:39:41Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "element_class of Subsets is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8367",
    "user": "https://trac.sagemath.org/admin/accounts/users/giraudo"
}
```
Assignee: giraudo

Keywords: Subsets element_class

element_class of Subsets is broken

```
sage: s = Subsets(Set([1]))
sage: e = s.first()
sage: isinstance(e, s.element_class)
False
```


Note: this should be caught by setting good categories 

```
sage: s.category()
Category of objects
```


Issue created by migration from https://trac.sagemath.org/ticket/8367





---

archive/issue_comments_074668.json:
```json
{
    "body": "Attachment [trac_8367_subsets_element_class_fix-sg.patch](tarball://root/attachments/some-uuid/ticket8367/trac_8367_subsets_element_class_fix-sg.patch) by giraudo created at 2010-02-25 18:21:55",
    "created_at": "2010-02-25T18:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8367#issuecomment-74668",
    "user": "https://trac.sagemath.org/admin/accounts/users/giraudo"
}
```

Attachment [trac_8367_subsets_element_class_fix-sg.patch](tarball://root/attachments/some-uuid/ticket8367/trac_8367_subsets_element_class_fix-sg.patch) by giraudo created at 2010-02-25 18:21:55



---

archive/issue_comments_074669.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-25T18:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8367#issuecomment-74669",
    "user": "https://trac.sagemath.org/admin/accounts/users/giraudo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074670.json:
```json
{
    "body": "Replying to [comment:1 giraudo]:\n\nHi Samuele,\n\nI think you made a mistake in opening new ticket #8396 for this problem. This ticket should be closed as duplicate.",
    "created_at": "2010-03-01T16:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8367#issuecomment-74670",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:1 giraudo]:

Hi Samuele,

I think you made a mistake in opening new ticket #8396 for this problem. This ticket should be closed as duplicate.



---

archive/issue_comments_074671.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-03-01T16:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8367#issuecomment-74671",
    "user": "https://github.com/hivert"
}
```

Resolution: duplicate



---

archive/issue_events_008555.json:
```json
{
    "actor": "https://github.com/hivert",
    "created_at": "2010-03-01T16:39:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8367",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8367#event-8555"
}
```
