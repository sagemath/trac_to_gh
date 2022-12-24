# Issue 7374: wrong docstring for is_isomorphic() in permgroup.py

archive/issues_007374.json:
```json
{
    "body": "Assignee: joyner\n\nThe docstring for `is_isomorphic()` for permutation groups claims \"If mode=\"verbose\" then an isomorphism is printed.\"\n\nHowever, that's not the case.  This is probably just left over from a previous version of the method.  In any case, the attached trivial patch removes this from the docstring.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7374\n\n",
    "created_at": "2009-11-02T06:18:33Z",
    "labels": [
        "group theory",
        "trivial",
        "bug"
    ],
    "title": "wrong docstring for is_isomorphic() in permgroup.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7374",
    "user": "AlexGhitza"
}
```
Assignee: joyner

The docstring for `is_isomorphic()` for permutation groups claims "If mode="verbose" then an isomorphism is printed."

However, that's not the case.  This is probably just left over from a previous version of the method.  In any case, the attached trivial patch removes this from the docstring.

Issue created by migration from https://trac.sagemath.org/ticket/7374





---

archive/issue_comments_061776.json:
```json
{
    "body": "Attachment [trac_7374.patch](tarball://root/attachments/some-uuid/ticket7374/trac_7374.patch) by AlexGhitza created at 2009-11-02 06:20:31",
    "created_at": "2009-11-02T06:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7374#issuecomment-61776",
    "user": "AlexGhitza"
}
```

Attachment [trac_7374.patch](tarball://root/attachments/some-uuid/ticket7374/trac_7374.patch) by AlexGhitza created at 2009-11-02 06:20:31



---

archive/issue_comments_061777.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-02T06:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7374#issuecomment-61777",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061778.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-03T15:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7374#issuecomment-61778",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_061779.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-03T15:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7374#issuecomment-61779",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061780.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-04T14:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7374#issuecomment-61780",
    "user": "mhansen"
}
```

Resolution: fixed
