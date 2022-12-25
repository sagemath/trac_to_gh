# Issue 8107: Fewer unnecessary imports from `sage.server.*`

archive/issues_008107.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb @TimDumol\n\nThis should reduce startup time, according to `sage -startuptime`.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8107\n\n",
    "created_at": "2010-01-28T05:33:30Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Fewer unnecessary imports from `sage.server.*`",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8107",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @robertwb @TimDumol

This should reduce startup time, according to `sage -startuptime`.



Issue created by migration from https://trac.sagemath.org/ticket/8107





---

archive/issue_comments_071029.json:
```json
{
    "body": "Attachment [trac_8107-server_imports.patch](tarball://root/attachments/some-uuid/ticket8107/trac_8107-server_imports.patch) by @qed777 created at 2010-01-28 05:35:42\n\n*sage* repo.",
    "created_at": "2010-01-28T05:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71029",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8107-server_imports.patch](tarball://root/attachments/some-uuid/ticket8107/trac_8107-server_imports.patch) by @qed777 created at 2010-01-28 05:35:42

*sage* repo.



---

archive/issue_comments_071030.json:
```json
{
    "body": "The *sage*-repository patch and #8102 together reduce the overall time for me from ~1.9 s to ~1.7 s.",
    "created_at": "2010-01-28T05:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71030",
    "user": "https://github.com/qed777"
}
```

The *sage*-repository patch and #8102 together reduce the overall time for me from ~1.9 s to ~1.7 s.



---

archive/issue_comments_071031.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T05:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71031",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071032.json:
```json
{
    "body": "I'm sure we can do better with #7502...",
    "created_at": "2010-01-28T05:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71032",
    "user": "https://github.com/qed777"
}
```

I'm sure we can do better with #7502...



---

archive/issue_comments_071033.json:
```json
{
    "body": "Awesome -- I was just being annoyed by precisely these imports last night.",
    "created_at": "2010-01-28T06:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71033",
    "user": "https://github.com/williamstein"
}
```

Awesome -- I was just being annoyed by precisely these imports last night.



---

archive/issue_comments_071034.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T06:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71034",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071035.json:
```json
{
    "body": "A big +1 from me too. I'm curious about the comment \n\n\n```\n# We import the following two only for doctesting purposes\n```\n\n\nthough.",
    "created_at": "2010-01-28T09:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71035",
    "user": "https://github.com/robertwb"
}
```

A big +1 from me too. I'm curious about the comment 


```
# We import the following two only for doctesting purposes
```


though.



---

archive/issue_comments_071036.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> A big +1 from me too. I'm curious about the comment \n\n```\n# We import the following two only for doctesting purposes\n```\n\nI'm not sure, but post-#7650, these imports should be unnecessary.  The patch above does not affect the results of `make ptestlong` on sage.math.",
    "created_at": "2010-01-30T05:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71036",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:4 robertwb]:
> A big +1 from me too. I'm curious about the comment 

```
# We import the following two only for doctesting purposes
```

I'm not sure, but post-#7650, these imports should be unnecessary.  The patch above does not affect the results of `make ptestlong` on sage.math.



---

archive/issue_events_008314.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-30T23:52:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8107#event-8314"
}
```



---

archive/issue_comments_071037.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8107#issuecomment-71037",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
