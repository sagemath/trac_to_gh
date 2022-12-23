# Issue 7685: integer.pyx: factor docstring lies about output -- fix this

archive/issues_007685.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  kcrisman\n\nThe docstring for n.factor (for n a Sage integer) says it returns a list of pairs.  Actually it returns a Factorization (which derives from list, but prints differently, has arithmetic support, etc.).\n\nWe should also have an OUTPUT: block. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7685\n\n",
    "created_at": "2009-12-15T18:08:01Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "integer.pyx: factor docstring lies about output -- fix this",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7685",
    "user": "was"
}
```
Assignee: AlexGhitza

CC:  kcrisman

The docstring for n.factor (for n a Sage integer) says it returns a list of pairs.  Actually it returns a Factorization (which derives from list, but prints differently, has arithmetic support, etc.).

We should also have an OUTPUT: block. 

Issue created by migration from https://trac.sagemath.org/ticket/7685





---

archive/issue_comments_065953.json:
```json
{
    "body": "minor doc edits",
    "created_at": "2012-05-26T05:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65953",
    "user": "dsm"
}
```

minor doc edits



---

archive/issue_comments_065954.json:
```json
{
    "body": "Attachment\n\nMinor tweaks.",
    "created_at": "2012-05-26T05:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65954",
    "user": "dsm"
}
```

Attachment

Minor tweaks.



---

archive/issue_comments_065955.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-26T05:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65955",
    "user": "dsm"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065956.json:
```json
{
    "body": "LGTM!",
    "created_at": "2012-05-26T06:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65956",
    "user": "was"
}
```

LGTM!



---

archive/issue_comments_065957.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-26T06:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65957",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065958.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40.5\".",
    "created_at": "2012-05-26T06:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65958",
    "user": "was"
}
```

Changing keywords from "" to "sd40.5".



---

archive/issue_comments_065959.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-06-05T06:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7685#issuecomment-65959",
    "user": "jdemeyer"
}
```

Resolution: fixed
