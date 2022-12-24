# Issue 4947: worksheets with interact cells auto-launch

archive/issues_004947.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  timothyclemans\n\nKeywords: notebook, interact\n\nNote: this is NOT a duplicate of #4363.\n\nSince 3.2.2 (possibly 3.2.1?), worksheets which contain `@`interact cells auto-launch when the notebook is started.  This is an extremely serious problem for notebooks with many such worksheets.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4947\n\n",
    "created_at": "2009-01-07T03:42:39Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "worksheets with interact cells auto-launch",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4947",
    "user": "mhampton"
}
```
Assignee: boothby

CC:  timothyclemans

Keywords: notebook, interact

Note: this is NOT a duplicate of #4363.

Since 3.2.2 (possibly 3.2.1?), worksheets which contain `@`interact cells auto-launch when the notebook is started.  This is an extremely serious problem for notebooks with many such worksheets.

Issue created by migration from https://trac.sagemath.org/ticket/4947





---

archive/issue_comments_037549.json:
```json
{
    "body": "> Note: this is NOT a duplicate of #4363.\n\n> Since 3.2.2 (possibly 3.2.1?), worksheets which contain `@`interact\n> cells auto-launch when the notebook is started. This is an extremely \n> serious problem for notebooks with many such worksheets. \n\nAre you sure???   This would be so wrong/horrible, that I would think I would have noticed.  Also, I can't imagine how this is possible; from my understanding of the notebook code, this is highly unlikely to happen.   Finally, I tried creating a worksheet with an interact cell on my laptop with sage-3.2.3 then restarting the sage notebook server, and that worksheet was *not* running.  In only started running when I clicked to open the worksheet.\n\nCan you please check that you didn't just get confused?  Thanks.",
    "created_at": "2009-01-07T15:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4947#issuecomment-37549",
    "user": "was"
}
```

> Note: this is NOT a duplicate of #4363.

> Since 3.2.2 (possibly 3.2.1?), worksheets which contain `@`interact
> cells auto-launch when the notebook is started. This is an extremely 
> serious problem for notebooks with many such worksheets. 

Are you sure???   This would be so wrong/horrible, that I would think I would have noticed.  Also, I can't imagine how this is possible; from my understanding of the notebook code, this is highly unlikely to happen.   Finally, I tried creating a worksheet with an interact cell on my laptop with sage-3.2.3 then restarting the sage notebook server, and that worksheet was *not* running.  In only started running when I clicked to open the worksheet.

Can you please check that you didn't just get confused?  Thanks.



---

archive/issue_comments_037550.json:
```json
{
    "body": "I just checked on the public sagenb.org, and *did* observe this behavior.  So it does happen systematically on some installs.  This is obviously a terrible bug.",
    "created_at": "2009-01-07T17:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4947#issuecomment-37550",
    "user": "was"
}
```

I just checked on the public sagenb.org, and *did* observe this behavior.  So it does happen systematically on some installs.  This is obviously a terrible bug.



---

archive/issue_comments_037551.json:
```json
{
    "body": "This happened to me, but I cannot replicate it on 3.2.1 - only 3.2.2.  I hope that helps track it down.",
    "created_at": "2009-01-07T22:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4947#issuecomment-37551",
    "user": "kcrisman"
}
```

This happened to me, but I cannot replicate it on 3.2.1 - only 3.2.2.  I hope that helps track it down.



---

archive/issue_comments_037552.json:
```json
{
    "body": "After a non-expert look at all changesets for 3.2.2, the only one that really stuck out was #3950 - not that there was anything immediately obvious in it that would cause this behavior, but it seemed to be the only nontrivial change to the notebook.  There were a few others that touched it, though all (including this one) seemed to be mostly on the listing of worksheets or html, not starting processes!",
    "created_at": "2009-01-15T16:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4947#issuecomment-37552",
    "user": "kcrisman"
}
```

After a non-expert look at all changesets for 3.2.2, the only one that really stuck out was #3950 - not that there was anything immediately obvious in it that would cause this behavior, but it seemed to be the only nontrivial change to the notebook.  There were a few others that touched it, though all (including this one) seemed to be mostly on the listing of worksheets or html, not starting processes!



---

archive/issue_comments_037553.json:
```json
{
    "body": "Is it possible that #3950 could have opened each worksheet, and when doing that, #4363 kicks in and starts running things?\n\nTimothyClemans, can you look at this and see if #3950 caused the problem?",
    "created_at": "2009-01-16T17:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4947#issuecomment-37553",
    "user": "jason"
}
```

Is it possible that #3950 could have opened each worksheet, and when doing that, #4363 kicks in and starts running things?

TimothyClemans, can you look at this and see if #3950 caused the problem?



---

archive/issue_comments_037554.json:
```json
{
    "body": "I can verify this behavior on 3.2.3 (ubuntu 8.10 x86_64) and wanted to also verify that the worksheets are indeed running and have `@`interact cells",
    "created_at": "2009-01-17T07:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4947#issuecomment-37554",
    "user": "ghtdak"
}
```

I can verify this behavior on 3.2.3 (ubuntu 8.10 x86_64) and wanted to also verify that the worksheets are indeed running and have `@`interact cells



---

archive/issue_comments_037555.json:
```json
{
    "body": "This is fixed by #4363.",
    "created_at": "2009-01-19T04:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4947#issuecomment-37555",
    "user": "mhansen"
}
```

This is fixed by #4363.



---

archive/issue_comments_037556.json:
```json
{
    "body": "Fixed in Sage 3.3.alpha0 by merging #4363.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T06:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4947#issuecomment-37556",
    "user": "mabshoff"
}
```

Fixed in Sage 3.3.alpha0 by merging #4363.

Cheers,

Michael



---

archive/issue_comments_037557.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T06:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4947#issuecomment-37557",
    "user": "mabshoff"
}
```

Resolution: fixed
