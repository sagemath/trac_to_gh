# Issue 2680: Modular forms for Gamma1(N) have wrong Sturm bound

archive/issues_002680.json:
```json
{
    "body": "Assignee: craigcitro\n\nThere are several issues with modular forms for Gamma1. In particular, this breaks:\n\n\n```\nsage: ModularForms(Gamma1(22))._q_expansion_module()\n```\n\n\nIt's happening because the Sturm bound is getting calculated incorrectly (if you look at the code, it just looks at the level and takes the index of Gamma0 for that level, which is clearly wrong). This is probably an easy fix, but I don't want to do this hastily and make a mistake, so I'll look at it next week.\n\nI don't think we're going to produce any wrong answers right now -- I think there are just several places where we'll throw errors instead of producing answers.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2680\n\n",
    "created_at": "2008-03-26T23:00:25Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "Modular forms for Gamma1(N) have wrong Sturm bound",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2680",
    "user": "craigcitro"
}
```
Assignee: craigcitro

There are several issues with modular forms for Gamma1. In particular, this breaks:


```
sage: ModularForms(Gamma1(22))._q_expansion_module()
```


It's happening because the Sturm bound is getting calculated incorrectly (if you look at the code, it just looks at the level and takes the index of Gamma0 for that level, which is clearly wrong). This is probably an easy fix, but I don't want to do this hastily and make a mistake, so I'll look at it next week.

I don't think we're going to produce any wrong answers right now -- I think there are just several places where we'll throw errors instead of producing answers.

Issue created by migration from https://trac.sagemath.org/ticket/2680





---

archive/issue_comments_018428.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-26T23:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2680#issuecomment-18428",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018429.json:
```json
{
    "body": "Patch attached. The fix was what I described above, but apparently I was pessimistic about this breaking things -- I tried a handful of examples, and nothing seems broken. It also passes all doctests. If someone can find something I missed, let me know.",
    "created_at": "2008-04-06T06:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2680#issuecomment-18429",
    "user": "craigcitro"
}
```

Patch attached. The fix was what I described above, but apparently I was pessimistic about this breaking things -- I tried a handful of examples, and nothing seems broken. It also passes all doctests. If someone can find something I missed, let me know.



---

archive/issue_comments_018430.json:
```json
{
    "body": "Attachment [trac-2680.patch](tarball://root/attachments/some-uuid/ticket2680/trac-2680.patch) by robertwb created at 2008-04-06 06:56:37\n\nLooks good to me.",
    "created_at": "2008-04-06T06:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2680#issuecomment-18430",
    "user": "robertwb"
}
```

Attachment [trac-2680.patch](tarball://root/attachments/some-uuid/ticket2680/trac-2680.patch) by robertwb created at 2008-04-06 06:56:37

Looks good to me.



---

archive/issue_comments_018431.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T07:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2680#issuecomment-18431",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018432.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T07:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2680#issuecomment-18432",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2
