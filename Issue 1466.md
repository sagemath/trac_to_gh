# Issue 1466: improve the "click to the left" aspect of the notebook

archive/issues_001466.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @qed777\n\n\n```\nAha!  Great!\n\nThis reminds we that when I started using the notebook interface, it\ntook me an embarrassingly long time to discover what was meant by the\nphrase\n'click to the left for traceback'.  I found this message confusing\nbecause there is nothing to the left to click on.  At first I thought\nthis was a strange way\nof saying `left-click'.  Eventually I worked it out by accident.  I\nsuggest a more verbose message along the lines of\n`for traceback, click in the blank area just to the left of this\nline'.  Or put something to click on, maybe along the lines of the\nbrackets in\nthe mathematica notebook, which has a hierarchical grouping mechanism\nwhereby groups of cells can be hidden or expanded together.\n(Of course maybe sage does too, and I just don't know about it!)\n\nCheers,\n\nPeter\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1466\n\n",
    "created_at": "2007-12-12T06:22:38Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "improve the \"click to the left\" aspect of the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1466",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @qed777


```
Aha!  Great!

This reminds we that when I started using the notebook interface, it
took me an embarrassingly long time to discover what was meant by the
phrase
'click to the left for traceback'.  I found this message confusing
because there is nothing to the left to click on.  At first I thought
this was a strange way
of saying `left-click'.  Eventually I worked it out by accident.  I
suggest a more verbose message along the lines of
`for traceback, click in the blank area just to the left of this
line'.  Or put something to click on, maybe along the lines of the
brackets in
the mathematica notebook, which has a hierarchical grouping mechanism
whereby groups of cells can be hidden or expanded together.
(Of course maybe sage does too, and I just don't know about it!)

Cheers,

Peter
```


Issue created by migration from https://trac.sagemath.org/ticket/1466





---

archive/issue_comments_009410.json:
```json
{
    "body": "Makes the traceback message: \"click to the left of this block for traceback\" instead.",
    "created_at": "2009-11-15T15:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1466#issuecomment-9410",
    "user": "https://github.com/TimDumol"
}
```

Makes the traceback message: "click to the left of this block for traceback" instead.



---

archive/issue_comments_009411.json:
```json
{
    "body": "Attachment [trac_1466-click-to-the-left-verbose.patch](tarball://root/attachments/some-uuid/ticket1466/trac_1466-click-to-the-left-verbose.patch) by @TimDumol created at 2009-11-15 15:41:57\n\nIn case anyone considers this confusing enough, this patch makes the error message slightly more verbose.",
    "created_at": "2009-11-15T15:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1466#issuecomment-9411",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_1466-click-to-the-left-verbose.patch](tarball://root/attachments/some-uuid/ticket1466/trac_1466-click-to-the-left-verbose.patch) by @TimDumol created at 2009-11-15 15:41:57

In case anyone considers this confusing enough, this patch makes the error message slightly more verbose.



---

archive/issue_comments_009412.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-15T15:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1466#issuecomment-9412",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_009413.json:
```json
{
    "body": "Seems to work as described and is a bit more clear to read. ~ Adam",
    "created_at": "2009-11-19T15:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1466#issuecomment-9413",
    "user": "https://github.com/maxthemouse"
}
```

Seems to work as described and is a bit more clear to read. ~ Adam



---

archive/issue_comments_009414.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-19T15:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1466#issuecomment-9414",
    "user": "https://github.com/maxthemouse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_009415.json:
```json
{
    "body": "merge into sagenb-0.4.4",
    "created_at": "2009-11-19T21:39:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1466#issuecomment-9415",
    "user": "https://github.com/williamstein"
}
```

merge into sagenb-0.4.4



---

archive/issue_comments_009416.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T21:39:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1466#issuecomment-9416",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_003734.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-11-19T21:39:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1466",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1466#event-3734"
}
```



---

archive/issue_events_003735.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-12-26T16:54:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1466",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1466#event-3735"
}
```
