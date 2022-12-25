# Issue 5389: Creating a  updated workspace with -tp is racy

archive/issues_005389.json:
```json
{
    "body": "Assignee: mabshoff\n\nSee a comment on #5366. When one does doctest Sage with -tp and GAP has been updated, but Sage not started the creation of the workspace is racy since many processes will try to update it at the same time.\n\nStarting up Sage once at the start of -tp via \"sage -c\" ought to fix the problem.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5389\n\n",
    "created_at": "2009-02-26T23:33:09Z",
    "labels": [
        "component: doctest coverage",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Creating a  updated workspace with -tp is racy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5389",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

See a comment on #5366. When one does doctest Sage with -tp and GAP has been updated, but Sage not started the creation of the workspace is racy since many processes will try to update it at the same time.

Starting up Sage once at the start of -tp via "sage -c" ought to fix the problem.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5389





---

archive/issue_comments_041426.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-26T23:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5389#issuecomment-41426",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041427.json:
```json
{
    "body": "I believe that since `sage-starts` is now executed at the beginning of parallel testing, this has already been fixed.",
    "created_at": "2011-01-11T01:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5389#issuecomment-41427",
    "user": "https://github.com/wjp"
}
```

I believe that since `sage-starts` is now executed at the beginning of parallel testing, this has already been fixed.



---

archive/issue_comments_041428.json:
```json
{
    "body": "Replying to [comment:2 wjp]:\n> I believe that since `sage-starts` is now executed at the beginning of parallel testing, this has already been fixed.\n\nI agree.",
    "created_at": "2011-01-11T06:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5389#issuecomment-41428",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:2 wjp]:
> I believe that since `sage-starts` is now executed at the beginning of parallel testing, this has already been fixed.

I agree.



---

archive/issue_comments_041429.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2011-01-11T06:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5389#issuecomment-41429",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
