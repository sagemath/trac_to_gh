# Issue 8235: fix another doctest in base.pyx

archive/issues_008235.json:
```json
{
    "body": "Assignee: @aghitza\n\nThis ticket is related to #7985. There's another doctest in base.pyx (on line 1308) that uses the output of texture_set(), which is inconsistent across machines since the order of Texture objects in a set is not well defined. This should be a trivial fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8235\n\n",
    "created_at": "2010-02-11T00:40:23Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "fix another doctest in base.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8235",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```
Assignee: @aghitza

This ticket is related to #7985. There's another doctest in base.pyx (on line 1308) that uses the output of texture_set(), which is inconsistent across machines since the order of Texture objects in a set is not well defined. This should be a trivial fix.

Issue created by migration from https://trac.sagemath.org/ticket/8235





---

archive/issue_comments_072622.json:
```json
{
    "body": "based on sage 4.3.1",
    "created_at": "2010-02-11T01:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72622",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

based on sage 4.3.1



---

archive/issue_comments_072623.json:
```json
{
    "body": "Attachment [trac_8235.patch](tarball://root/attachments/some-uuid/ticket8235/trac_8235.patch) by wcauchois created at 2010-02-11 01:10:51\n\nIts not terribly pretty, but this should fix it.",
    "created_at": "2010-02-11T01:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72623",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac_8235.patch](tarball://root/attachments/some-uuid/ticket8235/trac_8235.patch) by wcauchois created at 2010-02-11 01:10:51

Its not terribly pretty, but this should fix it.



---

archive/issue_comments_072624.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-11T01:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72624",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072625.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-02-11T10:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72625",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to minor.



---

archive/issue_comments_072626.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-11T10:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72626",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072627.json:
```json
{
    "body": "Changing component from algebra to graphics.",
    "created_at": "2010-02-11T10:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72627",
    "user": "https://github.com/qed777"
}
```

Changing component from algebra to graphics.



---

archive/issue_comments_072628.json:
```json
{
    "body": "Running `sage -t  plot/plot3d/base.pyx` 10 or so times in succession yields no failures.  Positive review.\n\nPlease remember to set / update the relevant ticket fields.\n\nThanks!",
    "created_at": "2010-02-11T10:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72628",
    "user": "https://github.com/qed777"
}
```

Running `sage -t  plot/plot3d/base.pyx` 10 or so times in succession yields no failures.  Positive review.

Please remember to set / update the relevant ticket fields.

Thanks!



---

archive/issue_comments_072629.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72629",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_008436.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-11T15:04:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8235#event-8436"
}
```
