# Issue 8107: Fewer unnecessary imports from `sage.server.*`

archive/issues_008107.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb @TimDumol\n\nThis should reduce startup time, according to `sage -startuptime`.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8107\n\n",
    "created_at": "2010-01-28T05:33:30Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Fewer unnecessary imports from `sage.server.*`",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8107",
    "user": "@qed777"
}
```
Assignee: @williamstein

CC:  @robertwb @TimDumol

This should reduce startup time, according to `sage -startuptime`.



Issue created by migration from https://trac.sagemath.org/ticket/8107





---

archive/issue_comments_071150.json:
```json
{
    "body": "Attachment [trac_8107-server_imports.patch](tarball://root/attachments/some-uuid/ticket8107/trac_8107-server_imports.patch) by @qed777 created at 2010-01-28 05:35:42\n\n*sage* repo.",
    "created_at": "2010-01-28T05:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71150",
    "user": "@qed777"
}
```

Attachment [trac_8107-server_imports.patch](tarball://root/attachments/some-uuid/ticket8107/trac_8107-server_imports.patch) by @qed777 created at 2010-01-28 05:35:42

*sage* repo.



---

archive/issue_comments_071151.json:
```json
{
    "body": "The *sage*-repository patch and #8102 together reduce the overall time for me from ~1.9 s to ~1.7 s.",
    "created_at": "2010-01-28T05:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71151",
    "user": "@qed777"
}
```

The *sage*-repository patch and #8102 together reduce the overall time for me from ~1.9 s to ~1.7 s.



---

archive/issue_comments_071152.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T05:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71152",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071153.json:
```json
{
    "body": "I'm sure we can do better with #7502...",
    "created_at": "2010-01-28T05:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71153",
    "user": "@qed777"
}
```

I'm sure we can do better with #7502...



---

archive/issue_comments_071154.json:
```json
{
    "body": "Awesome -- I was just being annoyed by precisely these imports last night.",
    "created_at": "2010-01-28T06:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71154",
    "user": "@williamstein"
}
```

Awesome -- I was just being annoyed by precisely these imports last night.



---

archive/issue_comments_071155.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T06:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71155",
    "user": "@williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071156.json:
```json
{
    "body": "A big +1 from me too. I'm curious about the comment \n\n\n```\n# We import the following two only for doctesting purposes\n```\n\n\nthough.",
    "created_at": "2010-01-28T09:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71156",
    "user": "@robertwb"
}
```

A big +1 from me too. I'm curious about the comment 


```
# We import the following two only for doctesting purposes
```


though.



---

archive/issue_comments_071157.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> A big +1 from me too. I'm curious about the comment \n\n```\n# We import the following two only for doctesting purposes\n```\n\nI'm not sure, but post-#7650, these imports should be unnecessary.  The patch above does not affect the results of `make ptestlong` on sage.math.",
    "created_at": "2010-01-30T05:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71157",
    "user": "@qed777"
}
```

Replying to [comment:4 robertwb]:
> A big +1 from me too. I'm curious about the comment 

```
# We import the following two only for doctesting purposes
```

I'm not sure, but post-#7650, these imports should be unnecessary.  The patch above does not affect the results of `make ptestlong` on sage.math.



---

archive/issue_comments_071158.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71158",
    "user": "mvngu"
}
```

Resolution: fixed
