# Issue 7320: search_src and friends are case-sensitive

archive/issues_007320.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nCC:  mvngu\n\nThe functions `search_src`, `search_def`, and `search_src` are case-sensitive and have been for a while.  The documentation says that they're not.  This patch changes the documentation to reflect this, and adds one doctest to verify it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7320\n\n",
    "created_at": "2009-10-27T05:15:26Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "search_src and friends are case-sensitive",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7320",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

CC:  mvngu

The functions `search_src`, `search_def`, and `search_src` are case-sensitive and have been for a while.  The documentation says that they're not.  This patch changes the documentation to reflect this, and adds one doctest to verify it.

Issue created by migration from https://trac.sagemath.org/ticket/7320





---

archive/issue_comments_061053.json:
```json
{
    "body": "Attachment [trac_7320-case-sensitive.patch](tarball://root/attachments/some-uuid/ticket7320/trac_7320-case-sensitive.patch) by @jhpalmieri created at 2009-10-27 05:15:54",
    "created_at": "2009-10-27T05:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7320#issuecomment-61053",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_7320-case-sensitive.patch](tarball://root/attachments/some-uuid/ticket7320/trac_7320-case-sensitive.patch) by @jhpalmieri created at 2009-10-27 05:15:54



---

archive/issue_comments_061054.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-27T05:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7320#issuecomment-61054",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061055.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-29T18:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7320#issuecomment-61055",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061056.json:
```json
{
    "body": "Just out of curiosity, is it possible to change the behavior?  Obviously that would be a different ticket.  That could be useful (or not).  Maybe a function that is, and another one that isn't...\n\nThe new patch is just making the notation for \"case-sensitive\" uniformly with hyphen, which seemed to be the majority of references in the doc; however, usage in general seems quite variable.  One word for the adjective seems right, though.  Maybe mvngu will have a comment, so I'm cc:ing him on this.\n\nI also added a little to the doctests to make sure we're really doctesting the right thing and compare the two possibilities.",
    "created_at": "2009-10-29T18:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7320#issuecomment-61056",
    "user": "https://github.com/kcrisman"
}
```

Just out of curiosity, is it possible to change the behavior?  Obviously that would be a different ticket.  That could be useful (or not).  Maybe a function that is, and another one that isn't...

The new patch is just making the notation for "case-sensitive" uniformly with hyphen, which seemed to be the majority of references in the doc; however, usage in general seems quite variable.  One word for the adjective seems right, though.  Maybe mvngu will have a comment, so I'm cc:ing him on this.

I also added a little to the doctests to make sure we're really doctesting the right thing and compare the two possibilities.



---

archive/issue_comments_061057.json:
```json
{
    "body": "Fixes a few things, adds doctest - use this",
    "created_at": "2009-10-29T18:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7320#issuecomment-61057",
    "user": "https://github.com/kcrisman"
}
```

Fixes a few things, adds doctest - use this



---

archive/issue_comments_061058.json:
```json
{
    "body": "Attachment [trac_7320-case-sensitive.2.patch](tarball://root/attachments/some-uuid/ticket7320/trac_7320-case-sensitive.2.patch) by @jhpalmieri created at 2009-10-29 19:01:50\n\nReplying to [comment:2 kcrisman]:\n> Just out of curiosity, is it possible to change the behavior?  Obviously that would be a different ticket.  That could be useful (or not).  Maybe a function that is, and another one that isn't...\n\n\nI think so: I think we can add a flag to the regular expression search to make it case-insensitive.  We could add a flag (like `ignore_case=False`) to the search functions so people could toggle this.  Of course, I haven't actually tried this, but the documentation for regular expression searches in Python suggests that it should be possible...",
    "created_at": "2009-10-29T19:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7320#issuecomment-61058",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_7320-case-sensitive.2.patch](tarball://root/attachments/some-uuid/ticket7320/trac_7320-case-sensitive.2.patch) by @jhpalmieri created at 2009-10-29 19:01:50

Replying to [comment:2 kcrisman]:
> Just out of curiosity, is it possible to change the behavior?  Obviously that would be a different ticket.  That could be useful (or not).  Maybe a function that is, and another one that isn't...


I think so: I think we can add a flag to the regular expression search to make it case-insensitive.  We could add a flag (like `ignore_case=False`) to the search functions so people could toggle this.  Of course, I haven't actually tried this, but the documentation for regular expression searches in Python suggests that it should be possible...



---

archive/issue_comments_061059.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> Maybe mvngu will have a comment, so I'm cc:ing him on this.\n\n\nSometimes I want to search the source with case-sensitivity on. For example, I might be interested in knowing if the source has anything with the word \"Euler\" in it. As function and method names are lower-case, case-sensitivity search might not return the name of a function/method like \"euler_phi\". However, if the documentation for \"euler_phi\" has something like \"Euler phi function\" or \"Euler totient function\", then case-sensitivity search would pick up \"Euler\". Sometimes I want to do a case-insensitivity search. In that case (pun not intended), I would expect that both \"euler_phi\" and \"Euler\" be returned by the search. At the end of the day, one can make case-insensitivity search as default, but should also give people the option to do case-sensitivity search. My 2-cent.",
    "created_at": "2009-10-30T04:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7320#issuecomment-61059",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:2 kcrisman]:
> Maybe mvngu will have a comment, so I'm cc:ing him on this.


Sometimes I want to search the source with case-sensitivity on. For example, I might be interested in knowing if the source has anything with the word "Euler" in it. As function and method names are lower-case, case-sensitivity search might not return the name of a function/method like "euler_phi". However, if the documentation for "euler_phi" has something like "Euler phi function" or "Euler totient function", then case-sensitivity search would pick up "Euler". Sometimes I want to do a case-insensitivity search. In that case (pun not intended), I would expect that both "euler_phi" and "Euler" be returned by the search. At the end of the day, one can make case-insensitivity search as default, but should also give people the option to do case-sensitivity search. My 2-cent.



---

archive/issue_events_017338.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-31T15:50:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7320",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7320#event-17338"
}
```



---

archive/issue_comments_061060.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T15:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7320#issuecomment-61060",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
