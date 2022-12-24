# Issue 8235: fix another doctest in base.pyx

archive/issues_008235.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThis ticket is related to #7985. There's another doctest in base.pyx (on line 1308) that uses the output of texture_set(), which is inconsistent across machines since the order of Texture objects in a set is not well defined. This should be a trivial fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8235\n\n",
    "created_at": "2010-02-11T00:40:23Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "fix another doctest in base.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8235",
    "user": "wcauchois"
}
```
Assignee: AlexGhitza

This ticket is related to #7985. There's another doctest in base.pyx (on line 1308) that uses the output of texture_set(), which is inconsistent across machines since the order of Texture objects in a set is not well defined. This should be a trivial fix.

Issue created by migration from https://trac.sagemath.org/ticket/8235





---

archive/issue_comments_072744.json:
```json
{
    "body": "based on sage 4.3.1",
    "created_at": "2010-02-11T01:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72744",
    "user": "wcauchois"
}
```

based on sage 4.3.1



---

archive/issue_comments_072745.json:
```json
{
    "body": "Attachment [trac_8235.patch](tarball://root/attachments/some-uuid/ticket8235/trac_8235.patch) by wcauchois created at 2010-02-11 01:10:51\n\nIts not terribly pretty, but this should fix it.",
    "created_at": "2010-02-11T01:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72745",
    "user": "wcauchois"
}
```

Attachment [trac_8235.patch](tarball://root/attachments/some-uuid/ticket8235/trac_8235.patch) by wcauchois created at 2010-02-11 01:10:51

Its not terribly pretty, but this should fix it.



---

archive/issue_comments_072746.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-11T01:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72746",
    "user": "wcauchois"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072747.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-02-11T10:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72747",
    "user": "mpatel"
}
```

Changing priority from major to minor.



---

archive/issue_comments_072748.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-11T10:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72748",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072749.json:
```json
{
    "body": "Changing component from algebra to graphics.",
    "created_at": "2010-02-11T10:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72749",
    "user": "mpatel"
}
```

Changing component from algebra to graphics.



---

archive/issue_comments_072750.json:
```json
{
    "body": "Running `sage -t  plot/plot3d/base.pyx` 10 or so times in succession yields no failures.  Positive review.\n\nPlease remember to set / update the relevant ticket fields.\n\nThanks!",
    "created_at": "2010-02-11T10:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72750",
    "user": "mpatel"
}
```

Running `sage -t  plot/plot3d/base.pyx` 10 or so times in succession yields no failures.  Positive review.

Please remember to set / update the relevant ticket fields.

Thanks!



---

archive/issue_comments_072751.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8235#issuecomment-72751",
    "user": "mpatel"
}
```

Resolution: fixed
