# Issue 8536: Change SAGE" to "Sage" in output

archive/issues_008536.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jhpalmieri\n\nWhen quitting we see\n\n```\nExiting SAGE (CPU time 0m0.04s, Wall time 0m0.63s).\n```\n\nand there are several other places where \"SAGE\" is output instead of \"Sage\".\n\nThe patch changes these.  I tested the whole library: no doctests needed changing at all.  But maybe there are other issues which I did not think of.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8536\n\n",
    "created_at": "2010-03-14T18:01:19Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Change SAGE\" to \"Sage\" in output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8536",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

CC:  @jhpalmieri

When quitting we see

```
Exiting SAGE (CPU time 0m0.04s, Wall time 0m0.63s).
```

and there are several other places where "SAGE" is output instead of "Sage".

The patch changes these.  I tested the whole library: no doctests needed changing at all.  But maybe there are other issues which I did not think of.

Issue created by migration from https://trac.sagemath.org/ticket/8536





---

archive/issue_comments_077023.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-14T18:03:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77023",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077024.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-25T05:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77024",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077025.json:
```json
{
    "body": "This looks good, although I did find some other instances of SAGE in output: `c_lib/src/interrupt.c` near the end of the file has a bunch of SAGEs; see line 138 to the end. With those changes, I'll give this a positive review.",
    "created_at": "2010-03-25T05:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77025",
    "user": "https://github.com/dandrake"
}
```

This looks good, although I did find some other instances of SAGE in output: `c_lib/src/interrupt.c` near the end of the file has a bunch of SAGEs; see line 138 to the end. With those changes, I'll give this a positive review.



---

archive/issue_comments_077026.json:
```json
{
    "body": "applies to 4.3.5",
    "created_at": "2010-04-01T09:23:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77026",
    "user": "https://github.com/JohnCremona"
}
```

applies to 4.3.5



---

archive/issue_comments_077027.json:
```json
{
    "body": "Attachment [trac_8536-SAGE.patch](tarball://root/attachments/some-uuid/ticket8536/trac_8536-SAGE.patch) by @JohnCremona created at 2010-04-01 09:26:58\n\nI don't know how to change the file c_lib/src/interrupt.c safely since it is not included in the cloning system.  Can you either tell me how to do that, or do it yourself?\n\nMeanwhile I have added to the patch to deal with file misc/sagedoc.py so that the latex control sequences \\sage and \\SAGE (and also \\Sage) convert to 'Sage' instead of 'SAGE'.  I am not too sure of the reperucssions of this (it will surely change a lot o the documentation, but not affect doctests), so I am cc-ing jpalmieri and hope that he will comment.\n\nI testing the whole sage library and all tests passed.",
    "created_at": "2010-04-01T09:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77027",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8536-SAGE.patch](tarball://root/attachments/some-uuid/ticket8536/trac_8536-SAGE.patch) by @JohnCremona created at 2010-04-01 09:26:58

I don't know how to change the file c_lib/src/interrupt.c safely since it is not included in the cloning system.  Can you either tell me how to do that, or do it yourself?

Meanwhile I have added to the patch to deal with file misc/sagedoc.py so that the latex control sequences \sage and \SAGE (and also \Sage) convert to 'Sage' instead of 'SAGE'.  I am not too sure of the reperucssions of this (it will surely change a lot o the documentation, but not affect doctests), so I am cc-ing jpalmieri and hope that he will comment.

I testing the whole sage library and all tests passed.



---

archive/issue_comments_077028.json:
```json
{
    "body": "Replying to [comment:3 cremona]:\n> I don't know how to change the file c_lib/src/interrupt.c safely since it is not included in the cloning system.  Can you either tell me how to do that, or do it yourself?\n\nI believe that directory is in the same Mercurial repo that the main Sage library is in -- it looks like interrupt.c was last changed by revision 9552:470b9bd4c96e (try \"hg annotate\" on that file). If you are using queues, you should be able to just make the change and do \"hg qref\". That worked for me.\n\nI'm running doctests now; it's not finished, but I would be surprised if anything fails.",
    "created_at": "2010-04-01T12:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77028",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:3 cremona]:
> I don't know how to change the file c_lib/src/interrupt.c safely since it is not included in the cloning system.  Can you either tell me how to do that, or do it yourself?

I believe that directory is in the same Mercurial repo that the main Sage library is in -- it looks like interrupt.c was last changed by revision 9552:470b9bd4c96e (try "hg annotate" on that file). If you are using queues, you should be able to just make the change and do "hg qref". That worked for me.

I'm running doctests now; it's not finished, but I would be surprised if anything fails.



---

archive/issue_comments_077029.json:
```json
{
    "body": "same as previous + c_lib/src/interrupt.c edits",
    "created_at": "2010-04-01T13:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77029",
    "user": "https://github.com/JohnCremona"
}
```

same as previous + c_lib/src/interrupt.c edits



---

archive/issue_comments_077030.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-01T13:24:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77030",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077031.json:
```json
{
    "body": "Attachment [trac_8536-SAGE.2.patch](tarball://root/attachments/some-uuid/ticket8536/trac_8536-SAGE.2.patch) by @JohnCremona created at 2010-04-01 13:24:57\n\nYou are right.  I updated the patch to include that file, and reinstated \"needs review\".",
    "created_at": "2010-04-01T13:24:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77031",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8536-SAGE.2.patch](tarball://root/attachments/some-uuid/ticket8536/trac_8536-SAGE.2.patch) by @JohnCremona created at 2010-04-01 13:24:57

You are right.  I updated the patch to include that file, and reinstated "needs review".



---

archive/issue_comments_077032.json:
```json
{
    "body": "Everything looks good, and all tests pass. Positive review -- although if John Palmieri finds something fishy with the sagedoc.py, he should revert that. I find it very unlikely that there's any problem, though.",
    "created_at": "2010-04-02T01:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77032",
    "user": "https://github.com/dandrake"
}
```

Everything looks good, and all tests pass. Positive review -- although if John Palmieri finds something fishy with the sagedoc.py, he should revert that. I find it very unlikely that there's any problem, though.



---

archive/issue_comments_077033.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-02T01:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77033",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077034.json:
```json
{
    "body": "The changes to sagedoc.py look okay to me.",
    "created_at": "2010-04-02T05:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77034",
    "user": "https://github.com/jhpalmieri"
}
```

The changes to sagedoc.py look okay to me.



---

archive/issue_comments_077035.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> The changes to sagedoc.py look okay to me.\n\nThanks, and sorry for the typo.  John",
    "created_at": "2010-04-02T09:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77035",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:8 jhpalmieri]:
> The changes to sagedoc.py look okay to me.

Thanks, and sorry for the typo.  John



---

archive/issue_comments_077036.json:
```json
{
    "body": "Merged \"trac_8536-SAGE.2.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-16T18:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77036",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8536-SAGE.2.patch" in 4.4.alpha0.



---

archive/issue_events_008715.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-16T18:40:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8536#event-8715"
}
```



---

archive/issue_comments_077037.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8536#issuecomment-77037",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
