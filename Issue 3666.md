# Issue 3666: pari(infinity) looks like it works, but it doesn't

archive/issues_003666.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis looks like `pari(infinity)` works:\n\n```\nsage: pari(infinity)\nInfinity\n```\n\n\nbut it's actually just creating a Pari variable named Infinity.\n\n```\nsage: (pari(infinity)-1)^2\nInfinity^2 - 2*Infinity + 1\n```\n\n\nWe should make pari(infinity) raise an exception, instead.  (As far as I can tell, Pari has no built-in notion of infinity, so we can't actually make it work.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3666\n\n",
    "created_at": "2008-07-16T05:12:04Z",
    "labels": [
        "packages",
        "major",
        "bug"
    ],
    "title": "pari(infinity) looks like it works, but it doesn't",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3666",
    "user": "cwitty"
}
```
Assignee: mabshoff

This looks like `pari(infinity)` works:

```
sage: pari(infinity)
Infinity
```


but it's actually just creating a Pari variable named Infinity.

```
sage: (pari(infinity)-1)^2
Infinity^2 - 2*Infinity + 1
```


We should make pari(infinity) raise an exception, instead.  (As far as I can tell, Pari has no built-in notion of infinity, so we can't actually make it work.)

Issue created by migration from https://trac.sagemath.org/ticket/3666





---

archive/issue_comments_025912.json:
```json
{
    "body": "Changing component from packages to interfaces.",
    "created_at": "2009-10-24T12:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3666#issuecomment-25912",
    "user": "AlexGhitza"
}
```

Changing component from packages to interfaces.



---

archive/issue_comments_025913.json:
```json
{
    "body": "See attached patch.",
    "created_at": "2009-10-24T12:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3666#issuecomment-25913",
    "user": "AlexGhitza"
}
```

See attached patch.



---

archive/issue_comments_025914.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-24T12:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3666#issuecomment-25914",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_025915.json:
```json
{
    "body": "Attachment [trac_3666.patch](tarball://root/attachments/some-uuid/ticket3666/trac_3666.patch) by AlexGhitza created at 2009-10-24 12:22:33",
    "created_at": "2009-10-24T12:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3666#issuecomment-25915",
    "user": "AlexGhitza"
}
```

Attachment [trac_3666.patch](tarball://root/attachments/some-uuid/ticket3666/trac_3666.patch) by AlexGhitza created at 2009-10-24 12:22:33



---

archive/issue_comments_025916.json:
```json
{
    "body": "Seems like Pari actually has INFINITY as a user-settable constant, which we probably would not want to make our oo equal to.  So nice patch and docs.\n\nIt's a little annoying that pari(maxima(inf)) still 'works', but Sage is only supposed to be the go-between, not to check that one doesn't do silly things with strings, so that's okay.  Positive review.",
    "created_at": "2009-10-29T18:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3666#issuecomment-25916",
    "user": "kcrisman"
}
```

Seems like Pari actually has INFINITY as a user-settable constant, which we probably would not want to make our oo equal to.  So nice patch and docs.

It's a little annoying that pari(maxima(inf)) still 'works', but Sage is only supposed to be the go-between, not to check that one doesn't do silly things with strings, so that's okay.  Positive review.



---

archive/issue_comments_025917.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-29T18:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3666#issuecomment-25917",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025918.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T05:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3666#issuecomment-25918",
    "user": "mhansen"
}
```

Resolution: fixed
