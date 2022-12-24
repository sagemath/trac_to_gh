# Issue 9534: add base method for permutation groups

archive/issues_009534.json:
```json
{
    "body": "Assignee: jasonbhill\n\nKeywords: base\n\nPatch to add a (working) base method for permutation groups.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9534\n\n",
    "created_at": "2010-07-17T23:33:27Z",
    "labels": [
        "group theory",
        "major",
        "enhancement"
    ],
    "title": "add base method for permutation groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9534",
    "user": "jasonbhill"
}
```
Assignee: jasonbhill

Keywords: base

Patch to add a (working) base method for permutation groups.

Issue created by migration from https://trac.sagemath.org/ticket/9534





---

archive/issue_comments_091826.json:
```json
{
    "body": "The existing base method returned \"Integer Ring\" for all permutation groups as it was inherited from ParentWithBase. This new base method uses GAP's base from stabilizer chain method to return an actual base, with an optional seed.\n\nThe patch was placed in the combinat queue as it depends on Mike Hansen's domain modifications.",
    "created_at": "2010-07-18T22:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91826",
    "user": "jasonbhill"
}
```

The existing base method returned "Integer Ring" for all permutation groups as it was inherited from ParentWithBase. This new base method uses GAP's base from stabilizer chain method to return an actual base, with an optional seed.

The patch was placed in the combinat queue as it depends on Mike Hansen's domain modifications.



---

archive/issue_comments_091827.json:
```json
{
    "body": "This is actually Jason's code, and it looks good to me.",
    "created_at": "2010-11-26T06:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91827",
    "user": "mhansen"
}
```

This is actually Jason's code, and it looks good to me.



---

archive/issue_comments_091828.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-26T06:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91828",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091829.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-26T06:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91829",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091830.json:
```json
{
    "body": "Attachment [trac_9534-permgroup_base.patch](tarball://root/attachments/some-uuid/ticket9534/trac_9534-permgroup_base.patch) by jdemeyer created at 2011-06-01 12:12:30",
    "created_at": "2011-06-01T12:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91830",
    "user": "jdemeyer"
}
```

Attachment [trac_9534-permgroup_base.patch](tarball://root/attachments/some-uuid/ticket9534/trac_9534-permgroup_base.patch) by jdemeyer created at 2011-06-01 12:12:30



---

archive/issue_comments_091831.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-07-22T12:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91831",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_091832.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-08-01T11:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91832",
    "user": "jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_091833.json:
```json
{
    "body": "Unmerged because of an issue with #10335.",
    "created_at": "2011-08-01T11:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91833",
    "user": "jdemeyer"
}
```

Unmerged because of an issue with #10335.



---

archive/issue_comments_091834.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-08-01T11:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91834",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_091835.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-01T11:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91835",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091836.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-01T11:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91836",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091837.json:
```json
{
    "body": "Does this now have to be rebased on (the rebased) #10335?\n\nIn case it does, one should set it to \"needs work\", otherwise the milestone should be changed to Sage 4.7.2 again.",
    "created_at": "2011-09-23T10:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91837",
    "user": "leif"
}
```

Does this now have to be rebased on (the rebased) #10335?

In case it does, one should set it to "needs work", otherwise the milestone should be changed to Sage 4.7.2 again.



---

archive/issue_comments_091838.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-10-07T19:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91838",
    "user": "jdemeyer"
}
```

Resolution: fixed
