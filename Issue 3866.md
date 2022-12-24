# Issue 3866: Create a 2d locator interact widget

archive/issues_003866.json:
```json
{
    "body": "Assignee: @itolkov\n\nThis is a *very* *extremely* rough-cut of a 2d locator widget.  All the docstrings are blatantly wrong and the code is full of ugly things.  But it works, sort of.  It's a starting point for someone to finish.\n\nAn example:\n\n\n```\n@interact\ndef _(pos=locator(3)):\n    print pos\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3866\n\n",
    "created_at": "2008-08-15T03:46:33Z",
    "labels": [
        "interact",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Create a 2d locator interact widget",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3866",
    "user": "@jasongrout"
}
```
Assignee: @itolkov

This is a *very* *extremely* rough-cut of a 2d locator widget.  All the docstrings are blatantly wrong and the code is full of ugly things.  But it works, sort of.  It's a starting point for someone to finish.

An example:


```
@interact
def _(pos=locator(3)):
    print pos
```



Issue created by migration from https://trac.sagemath.org/ticket/3866





---

archive/issue_comments_027557.json:
```json
{
    "body": "Attachment [locator.patch](tarball://root/attachments/some-uuid/ticket3866/locator.patch) by @jasongrout created at 2008-08-15 03:48:16",
    "created_at": "2008-08-15T03:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27557",
    "user": "@jasongrout"
}
```

Attachment [locator.patch](tarball://root/attachments/some-uuid/ticket3866/locator.patch) by @jasongrout created at 2008-08-15 03:48:16



---

archive/issue_comments_027558.json:
```json
{
    "body": "Hi Jason,\n\ndoes this patch need a review?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-15T05:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27558",
    "user": "mabshoff"
}
```

Hi Jason,

does this patch need a review?

Cheers,

Michael



---

archive/issue_comments_027559.json:
```json
{
    "body": "No, not yet; definitely not yet.  I'm embarrassed to post the patch as it was; I only posted it because I was more embarrassed by almost losing the patch (I just barely found it).",
    "created_at": "2008-08-15T07:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27559",
    "user": "@jasongrout"
}
```

No, not yet; definitely not yet.  I'm embarrassed to post the patch as it was; I only posted it because I was more embarrassed by almost losing the patch (I just barely found it).



---

archive/issue_comments_027560.json:
```json
{
    "body": "I am thinking of giving this to a student of mine for an independent study project.  To avoid duplication of effort I would appreciate being informed of any independent effort on it.\n\nThanks,\nMarshall Hampton",
    "created_at": "2008-12-30T18:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27560",
    "user": "mhampton"
}
```

I am thinking of giving this to a student of mine for an independent study project.  To avoid duplication of effort I would appreciate being informed of any independent effort on it.

Thanks,
Marshall Hampton



---

archive/issue_comments_027561.json:
```json
{
    "body": "Attachment [trac_3866_4.0.1_rebase.patch](tarball://root/attachments/some-uuid/ticket3866/trac_3866_4.0.1_rebase.patch) by mhampton created at 2009-06-11 23:01:08\n\nrebase against 4.0.1, along with some very minor cleanup",
    "created_at": "2009-06-11T23:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27561",
    "user": "mhampton"
}
```

Attachment [trac_3866_4.0.1_rebase.patch](tarball://root/attachments/some-uuid/ticket3866/trac_3866_4.0.1_rebase.patch) by mhampton created at 2009-06-11 23:01:08

rebase against 4.0.1, along with some very minor cleanup



---

archive/issue_comments_027562.json:
```json
{
    "body": "It looks like my student didn't get very far, unfortunately.  I will attempt to improve this further, but I am attaching a rebased (and slightly cleaned-up) patch in case other people want to move ahead faster.",
    "created_at": "2009-06-11T23:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27562",
    "user": "mhampton"
}
```

It looks like my student didn't get very far, unfortunately.  I will attempt to improve this further, but I am attaching a rebased (and slightly cleaned-up) patch in case other people want to move ahead faster.



---

archive/issue_comments_027563.json:
```json
{
    "body": "There is a bounty for a feature like this:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/4b52ee22e227370d/a5347db58d549c71?lnk=gst&q=locator#a5347db58d549c71",
    "created_at": "2010-08-13T04:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27563",
    "user": "@jasongrout"
}
```

There is a bounty for a feature like this:

http://groups.google.com/group/sage-devel/browse_thread/thread/4b52ee22e227370d/a5347db58d549c71?lnk=gst&q=locator#a5347db58d549c71



---

archive/issue_comments_027564.json:
```json
{
    "body": "Given that the legacy-notebook is no longer maintained or developed, let us close that old ticket.",
    "created_at": "2018-04-30T08:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27564",
    "user": "@fchapoton"
}
```

Given that the legacy-notebook is no longer maintained or developed, let us close that old ticket.



---

archive/issue_comments_027565.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2018-04-30T08:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27565",
    "user": "@fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_027566.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-05-01T12:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27566",
    "user": "@videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_027567.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27567",
    "user": "@videlec"
}
```

closing positively reviewed duplicates



---

archive/issue_comments_027568.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27568",
    "user": "@videlec"
}
```

Resolution: wontfix
