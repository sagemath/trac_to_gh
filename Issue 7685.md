# Issue 7685: integer.pyx: factor docstring lies about output -- fix this

archive/issues_007685.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @kcrisman\n\nThe docstring for n.factor (for n a Sage integer) says it returns a list of pairs.  Actually it returns a Factorization (which derives from list, but prints differently, has arithmetic support, etc.).\n\nWe should also have an OUTPUT: block. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7685\n\n",
    "created_at": "2009-12-15T18:08:01Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.1",
    "title": "integer.pyx: factor docstring lies about output -- fix this",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7685",
    "user": "https://github.com/williamstein"
}
```
Assignee: @aghitza

CC:  @kcrisman

The docstring for n.factor (for n a Sage integer) says it returns a list of pairs.  Actually it returns a Factorization (which derives from list, but prints differently, has arithmetic support, etc.).

We should also have an OUTPUT: block. 

Issue created by migration from https://trac.sagemath.org/ticket/7685





---

archive/issue_comments_065837.json:
```json
{
    "body": "minor doc edits",
    "created_at": "2012-05-26T05:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65837",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

minor doc edits



---

archive/issue_comments_065838.json:
```json
{
    "body": "Attachment [trac_7685_improve_integer_factor_doc.patch](tarball://root/attachments/some-uuid/ticket7685/trac_7685_improve_integer_factor_doc.patch) by dsm created at 2012-05-26 05:10:07\n\nMinor tweaks.",
    "created_at": "2012-05-26T05:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65838",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Attachment [trac_7685_improve_integer_factor_doc.patch](tarball://root/attachments/some-uuid/ticket7685/trac_7685_improve_integer_factor_doc.patch) by dsm created at 2012-05-26 05:10:07

Minor tweaks.



---

archive/issue_comments_065839.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-26T05:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65839",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065840.json:
```json
{
    "body": "LGTM!",
    "created_at": "2012-05-26T06:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65840",
    "user": "https://github.com/williamstein"
}
```

LGTM!



---

archive/issue_comments_065841.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-26T06:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65841",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065842.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40.5\".",
    "created_at": "2012-05-26T06:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65842",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "sd40.5".



---

archive/issue_comments_065843.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-06-05T06:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65843",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
