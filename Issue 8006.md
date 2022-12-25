# Issue 8006: Identation syntax errors fail silently

archive/issues_008006.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @TimDumol @fchapoton\n\nSee #6729\n\nThis fails silently\n\n```\nCELL 1:\n u = 2\n  u = 3\nCELL 2:\nprint u # = 2\n```\n\nThis should fail with an `IdentationError`, as it does in `%python`:\n\n```\nCELL 1:\n u = 2\n  u = 3\n# generates IdentationError\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8006\n\n",
    "created_at": "2010-01-20T01:52:43Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Identation syntax errors fail silently",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8006",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```
Assignee: @williamstein

CC:  @TimDumol @fchapoton

See #6729

This fails silently

```
CELL 1:
 u = 2
  u = 3
CELL 2:
print u # = 2
```

This should fail with an `IdentationError`, as it does in `%python`:

```
CELL 1:
 u = 2
  u = 3
# generates IdentationError
```

Issue created by migration from https://trac.sagemath.org/ticket/8006





---

archive/issue_comments_069839.json:
```json
{
    "body": "This is likely related to https://github.com/sagemath/sagenb/issues/288 as well, though it seems to be slightly different.",
    "created_at": "2014-12-09T19:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8006#issuecomment-69839",
    "user": "https://github.com/kcrisman"
}
```

This is likely related to https://github.com/sagemath/sagenb/issues/288 as well, though it seems to be slightly different.



---

archive/issue_comments_069840.json:
```json
{
    "body": "See https://github.com/sagemath/sagenb/issues/289",
    "created_at": "2014-12-09T19:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8006#issuecomment-69840",
    "user": "https://github.com/kcrisman"
}
```

See https://github.com/sagemath/sagenb/issues/289



---

archive/issue_comments_069841.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8006#issuecomment-69841",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069842.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8006#issuecomment-69842",
    "user": "https://github.com/mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_events_019184.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-08-18T00:36:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8006",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8006#event-19184"
}
```



---

archive/issue_comments_069843.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-25T09:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8006#issuecomment-69843",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069844.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-29T15:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8006#issuecomment-69844",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_019185.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-08-29T15:27:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8006",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8006#event-19185"
}
```
