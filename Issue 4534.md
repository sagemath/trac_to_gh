# Issue 4534: Stupid error in odd_part

archive/issues_004534.json:
```json
{
    "body": "Assignee: @craigcitro\n\nI introduced an error in `odd_part` while working on #4443; the attached patch is the obvious fix, along with a doctest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4534\n\n",
    "created_at": "2008-11-16T13:00:42Z",
    "labels": [
        "component: basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Stupid error in odd_part",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4534",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

I introduced an error in `odd_part` while working on #4443; the attached patch is the obvious fix, along with a doctest.

Issue created by migration from https://trac.sagemath.org/ticket/4534





---

archive/issue_comments_033715.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-16T13:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4534#issuecomment-33715",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033716.json:
```json
{
    "body": "Attachment [trac-4534.patch](tarball://root/attachments/some-uuid/ticket4534/trac-4534.patch) by @craigcitro created at 2008-11-16 13:01:26",
    "created_at": "2008-11-16T13:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4534#issuecomment-33716",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4534.patch](tarball://root/attachments/some-uuid/ticket4534/trac-4534.patch) by @craigcitro created at 2008-11-16 13:01:26



---

archive/issue_comments_033717.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-11-16T13:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4534#issuecomment-33717",
    "user": "https://github.com/mwhansen"
}
```

Looks good.



---

archive/issue_comments_033718.json:
```json
{
    "body": "Wouldn't it be much faster to divide out by the valuation at 2?",
    "created_at": "2008-11-17T18:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4534#issuecomment-33718",
    "user": "https://github.com/robertwb"
}
```

Wouldn't it be much faster to divide out by the valuation at 2?



---

archive/issue_comments_033719.json:
```json
{
    "body": "Good point. I know I timed it when I wrote it (though I obviously didn't look at the output carefully) -- of course, since the broken version doesn't do much work, it's faster. Correcting it slows it way down. \n\nPatch coming right up.",
    "created_at": "2008-11-17T18:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4534#issuecomment-33719",
    "user": "https://github.com/craigcitro"
}
```

Good point. I know I timed it when I wrote it (though I obviously didn't look at the output carefully) -- of course, since the broken version doesn't do much work, it's faster. Correcting it slows it way down. 

Patch coming right up.



---

archive/issue_comments_033720.json:
```json
{
    "body": "Attachment [trac-4534-v2.patch](tarball://root/attachments/some-uuid/ticket4534/trac-4534-v2.patch) by @craigcitro created at 2008-11-17 20:43:52\n\nNew patch, which should be much better. Unfortunately, it touches `integer.pxd`, so it takes a while to rebuild.",
    "created_at": "2008-11-17T20:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4534#issuecomment-33720",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4534-v2.patch](tarball://root/attachments/some-uuid/ticket4534/trac-4534-v2.patch) by @craigcitro created at 2008-11-17 20:43:52

New patch, which should be much better. Unfortunately, it touches `integer.pxd`, so it takes a while to rebuild.



---

archive/issue_comments_033721.json:
```json
{
    "body": "Applied trac-4534-v2.patch\n\nRun ./sage -b and did a make check\n\nAll tests passed except the known issue with combinat/species/library.py\n\nSo I give this ticket a positive review.\n\nJaap",
    "created_at": "2008-11-18T15:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4534#issuecomment-33721",
    "user": "https://github.com/jaapspies"
}
```

Applied trac-4534-v2.patch

Run ./sage -b and did a make check

All tests passed except the known issue with combinat/species/library.py

So I give this ticket a positive review.

Jaap



---

archive/issue_events_004780.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-18T19:39:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4534",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4534#event-4780"
}
```



---

archive/issue_comments_033722.json:
```json
{
    "body": "Merged trac-4534-v2.patch in Sage 3.2.rc2",
    "created_at": "2008-11-18T19:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4534#issuecomment-33722",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac-4534-v2.patch in Sage 3.2.rc2



---

archive/issue_comments_033723.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-18T19:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4534#issuecomment-33723",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
