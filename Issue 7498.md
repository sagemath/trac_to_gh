# Issue 7498: Do *not* import matplotlib at sage startup.

archive/issues_007498.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein\n\nDespite the warning\n\n```\n## IMPORTANT: Do *not* import matplotlib at module scope.  It takes a\n## surprisingly long time to initialize itself.  It's better if it is\n## imported in functions, so it only gets started if it is actually\n## going to be used.\n```\n\nit's gotten back in there again. There should be a test. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7498\n\n",
    "created_at": "2009-11-20T06:34:07Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Do *not* import matplotlib at sage startup.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7498",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

CC:  @williamstein

Despite the warning

```
## IMPORTANT: Do *not* import matplotlib at module scope.  It takes a
## surprisingly long time to initialize itself.  It's better if it is
## imported in functions, so it only gets started if it is actually
## going to be used.
```

it's gotten back in there again. There should be a test. 

Issue created by migration from https://trac.sagemath.org/ticket/7498





---

archive/issue_comments_063276.json:
```json
{
    "body": "Attachment [7498-no-matplotlib.patch](tarball://root/attachments/some-uuid/ticket7498/7498-no-matplotlib.patch) by @robertwb created at 2009-11-20 06:40:45",
    "created_at": "2009-11-20T06:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63276",
    "user": "https://github.com/robertwb"
}
```

Attachment [7498-no-matplotlib.patch](tarball://root/attachments/some-uuid/ticket7498/7498-no-matplotlib.patch) by @robertwb created at 2009-11-20 06:40:45



---

archive/issue_comments_063277.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-20T06:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63277",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063278.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-20T12:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63278",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063279.json:
```json
{
    "body": "This patch is weird.  It has a 3-liner that does what this ticket is about, but then it also has a bunch of other complicated unrelated code.  Hmm?",
    "created_at": "2009-11-20T12:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63279",
    "user": "https://github.com/williamstein"
}
```

This patch is weird.  It has a 3-liner that does what this ticket is about, but then it also has a bunch of other complicated unrelated code.  Hmm?



---

archive/issue_comments_063280.json:
```json
{
    "body": "The diff is odd, try looking at before and after. There's a class that extends a class from matplotlib, which I moved to inside a function body so I didn't have to import it on startup.",
    "created_at": "2009-11-20T17:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63280",
    "user": "https://github.com/robertwb"
}
```

The diff is odd, try looking at before and after. There's a class that extends a class from matplotlib, which I moved to inside a function body so I didn't have to import it on startup.



---

archive/issue_comments_063281.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-20T18:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63281",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063282.json:
```json
{
    "body": "Attachment [trac_7498-review.patch](tarball://root/attachments/some-uuid/ticket7498/trac_7498-review.patch) by @mwhansen created at 2009-12-01 09:01:26\n\nRobert's changes look good, but it looks like we also need to make some changes in plot_field3d.py.\n\nI've attached a patch for that.",
    "created_at": "2009-12-01T09:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63282",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7498-review.patch](tarball://root/attachments/some-uuid/ticket7498/trac_7498-review.patch) by @mwhansen created at 2009-12-01 09:01:26

Robert's changes look good, but it looks like we also need to make some changes in plot_field3d.py.

I've attached a patch for that.



---

archive/issue_comments_063283.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-01T09:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63283",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063284.json:
```json
{
    "body": "Patch trac_7498-review.patch is ok => Positive review.",
    "created_at": "2009-12-01T09:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63284",
    "user": "https://github.com/hivert"
}
```

Patch trac_7498-review.patch is ok => Positive review.



---

archive/issue_events_017769.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-01T09:24:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7498#event-17769"
}
```



---

archive/issue_comments_063285.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-01T09:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63285",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
