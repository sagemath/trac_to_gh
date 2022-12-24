# Issue 7498: Do *not* import matplotlib at sage startup.

archive/issues_007498.json:
```json
{
    "body": "Assignee: was\n\nCC:  was\n\nDespite the warning\n\n\n```\n## IMPORTANT: Do *not* import matplotlib at module scope.  It takes a\n## surprisingly long time to initialize itself.  It's better if it is\n## imported in functions, so it only gets started if it is actually\n## going to be used.\n```\n\n\nit's gotten back in there again. There should be a test. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7498\n\n",
    "created_at": "2009-11-20T06:34:07Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "Do *not* import matplotlib at sage startup.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7498",
    "user": "robertwb"
}
```
Assignee: was

CC:  was

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

archive/issue_comments_063391.json:
```json
{
    "body": "Attachment [7498-no-matplotlib.patch](tarball://root/attachments/some-uuid/ticket7498/7498-no-matplotlib.patch) by robertwb created at 2009-11-20 06:40:45",
    "created_at": "2009-11-20T06:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63391",
    "user": "robertwb"
}
```

Attachment [7498-no-matplotlib.patch](tarball://root/attachments/some-uuid/ticket7498/7498-no-matplotlib.patch) by robertwb created at 2009-11-20 06:40:45



---

archive/issue_comments_063392.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-20T06:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63392",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063393.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-20T12:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63393",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063394.json:
```json
{
    "body": "This patch is weird.  It has a 3-liner that does what this ticket is about, but then it also has a bunch of other complicated unrelated code.  Hmm?",
    "created_at": "2009-11-20T12:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63394",
    "user": "was"
}
```

This patch is weird.  It has a 3-liner that does what this ticket is about, but then it also has a bunch of other complicated unrelated code.  Hmm?



---

archive/issue_comments_063395.json:
```json
{
    "body": "The diff is odd, try looking at before and after. There's a class that extends a class from matplotlib, which I moved to inside a function body so I didn't have to import it on startup.",
    "created_at": "2009-11-20T17:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63395",
    "user": "robertwb"
}
```

The diff is odd, try looking at before and after. There's a class that extends a class from matplotlib, which I moved to inside a function body so I didn't have to import it on startup.



---

archive/issue_comments_063396.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-20T18:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63396",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063397.json:
```json
{
    "body": "Attachment [trac_7498-review.patch](tarball://root/attachments/some-uuid/ticket7498/trac_7498-review.patch) by mhansen created at 2009-12-01 09:01:26\n\nRobert's changes look good, but it looks like we also need to make some changes in plot_field3d.py.\n\nI've attached a patch for that.",
    "created_at": "2009-12-01T09:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63397",
    "user": "mhansen"
}
```

Attachment [trac_7498-review.patch](tarball://root/attachments/some-uuid/ticket7498/trac_7498-review.patch) by mhansen created at 2009-12-01 09:01:26

Robert's changes look good, but it looks like we also need to make some changes in plot_field3d.py.

I've attached a patch for that.



---

archive/issue_comments_063398.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-01T09:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63398",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063399.json:
```json
{
    "body": "Patch trac_7498-review.patch is ok => Positive review.",
    "created_at": "2009-12-01T09:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63399",
    "user": "hivert"
}
```

Patch trac_7498-review.patch is ok => Positive review.



---

archive/issue_comments_063400.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-01T09:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7498#issuecomment-63400",
    "user": "mhansen"
}
```

Resolution: fixed
