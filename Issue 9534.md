# Issue 9534: add base method for permutation groups

archive/issues_009534.json:
```json
{
    "body": "Assignee: jasonbhill\n\nKeywords: base\n\nPatch to add a (working) base method for permutation groups.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9534\n\n",
    "created_at": "2010-07-17T23:33:27Z",
    "labels": [
        "component: group theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "add base method for permutation groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9534",
    "user": "https://trac.sagemath.org/admin/accounts/users/jasonbhill"
}
```
Assignee: jasonbhill

Keywords: base

Patch to add a (working) base method for permutation groups.

Issue created by migration from https://trac.sagemath.org/ticket/9534





---

archive/issue_comments_091672.json:
```json
{
    "body": "The existing base method returned \"Integer Ring\" for all permutation groups as it was inherited from ParentWithBase. This new base method uses GAP's base from stabilizer chain method to return an actual base, with an optional seed.\n\nThe patch was placed in the combinat queue as it depends on Mike Hansen's domain modifications.",
    "created_at": "2010-07-18T22:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91672",
    "user": "https://trac.sagemath.org/admin/accounts/users/jasonbhill"
}
```

The existing base method returned "Integer Ring" for all permutation groups as it was inherited from ParentWithBase. This new base method uses GAP's base from stabilizer chain method to return an actual base, with an optional seed.

The patch was placed in the combinat queue as it depends on Mike Hansen's domain modifications.



---

archive/issue_comments_091673.json:
```json
{
    "body": "This is actually Jason's code, and it looks good to me.",
    "created_at": "2010-11-26T06:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91673",
    "user": "https://github.com/mwhansen"
}
```

This is actually Jason's code, and it looks good to me.



---

archive/issue_comments_091674.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-26T06:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91674",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091675.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-26T06:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91675",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091676.json:
```json
{
    "body": "Attachment [trac_9534-permgroup_base.patch](tarball://root/attachments/some-uuid/ticket9534/trac_9534-permgroup_base.patch) by @jdemeyer created at 2011-06-01 12:12:30",
    "created_at": "2011-06-01T12:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91676",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_9534-permgroup_base.patch](tarball://root/attachments/some-uuid/ticket9534/trac_9534-permgroup_base.patch) by @jdemeyer created at 2011-06-01 12:12:30



---

archive/issue_events_009682.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-07-22T12:49:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9534#event-9682"
}
```



---

archive/issue_comments_091677.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-07-22T12:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91677",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_091678.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-08-01T11:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91678",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_091679.json:
```json
{
    "body": "Unmerged because of an issue with #10335.",
    "created_at": "2011-08-01T11:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91679",
    "user": "https://github.com/jdemeyer"
}
```

Unmerged because of an issue with #10335.



---

archive/issue_comments_091680.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-08-01T11:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91680",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_events_009683.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-08-01T11:37:36Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9534#event-9683"
}
```



---

archive/issue_comments_091681.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-01T11:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91681",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091682.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-01T11:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91682",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091683.json:
```json
{
    "body": "Does this now have to be rebased on (the rebased) #10335?\n\nIn case it does, one should set it to \"needs work\", otherwise the milestone should be changed to Sage 4.7.2 again.",
    "created_at": "2011-09-23T10:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91683",
    "user": "https://github.com/nexttime"
}
```

Does this now have to be rebased on (the rebased) #10335?

In case it does, one should set it to "needs work", otherwise the milestone should be changed to Sage 4.7.2 again.



---

archive/issue_events_009684.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-10-07T19:11:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9534#event-9684"
}
```



---

archive/issue_comments_091684.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-10-07T19:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9534#issuecomment-91684",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
