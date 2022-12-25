# Issue 3075: notebook -- add a "test" option

archive/issues_003075.json:
```json
{
    "body": "Assignee: boothby\n\nClick Action ---> Test and all cells will be evaluated and their output compared with the output last time.  Any time the output differs both outputs are shown with the bad one in RED.\n\nOr something like that...\n\nIssue created by migration from https://trac.sagemath.org/ticket/3075\n\n",
    "created_at": "2008-05-01T22:28:27Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- add a \"test\" option",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3075",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

Click Action ---> Test and all cells will be evaluated and their output compared with the output last time.  Any time the output differs both outputs are shown with the bad one in RED.

Or something like that...

Issue created by migration from https://trac.sagemath.org/ticket/3075





---

archive/issue_comments_021174.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-05-01T22:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3075#issuecomment-21174",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_021175.json:
```json
{
    "body": "\n```\n10:13 < mabshoff> And I have been slipping in FreeBSD fixes when no one was looking ;)\n10:16 < jason|log> okay, \"flaky\" == in one cell, I have a=[] and i=1, the next I have a.append(i).  \n                   Evaluate all sometimes gives me an error in the second cell and says that 'a' is not \n                   defined.\n10:16 < jason|log> I can't reproduce it on sage.math in the few minutes I tried.\n10:18 < jason|log> wstein: could the problem be the asynchronous requests to evaluate the cells?  One \n                   request gets ahead of another sometimes?\n10:19 < jason|log> (not in the sending, but in the server receiving the requests?)\n10:19 < wstein> Yes, that is possible.\n10:20 < wstein> The right fix would be to make a single \"evaluateall\" command that gets sent\n10:20 < wstein> to the notebook server.\n10:20 < wstein> Right now a stupid evaluate_all javascript function calls evaluate_cell on each cell.\n```\n",
    "created_at": "2008-05-02T17:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3075#issuecomment-21175",
    "user": "https://github.com/williamstein"
}
```


```
10:13 < mabshoff> And I have been slipping in FreeBSD fixes when no one was looking ;)
10:16 < jason|log> okay, "flaky" == in one cell, I have a=[] and i=1, the next I have a.append(i).  
                   Evaluate all sometimes gives me an error in the second cell and says that 'a' is not 
                   defined.
10:16 < jason|log> I can't reproduce it on sage.math in the few minutes I tried.
10:18 < jason|log> wstein: could the problem be the asynchronous requests to evaluate the cells?  One 
                   request gets ahead of another sometimes?
10:19 < jason|log> (not in the sending, but in the server receiving the requests?)
10:19 < wstein> Yes, that is possible.
10:20 < wstein> The right fix would be to make a single "evaluateall" command that gets sent
10:20 < wstein> to the notebook server.
10:20 < wstein> Right now a stupid evaluate_all javascript function calls evaluate_cell on each cell.
```




---

archive/issue_comments_021176.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-08T01:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3075#issuecomment-21176",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021177.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2008-09-08T01:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3075#issuecomment-21177",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_021178.json:
```json
{
    "body": "This patch fixes the problems with evaluate all.",
    "created_at": "2008-09-08T01:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3075#issuecomment-21178",
    "user": "https://github.com/mwhansen"
}
```

This patch fixes the problems with evaluate all.



---

archive/issue_comments_021179.json:
```json
{
    "body": "The patch by mhansen doesn't add a \"test\" option, so I think it should be on a different ticket.",
    "created_at": "2008-09-08T11:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3075#issuecomment-21179",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

The patch by mhansen doesn't add a "test" option, so I think it should be on a different ticket.



---

archive/issue_comments_021180.json:
```json
{
    "body": "I made #4078.\n\nDo we even really want this feature for the notebook?  I'd vote for marking this ticket as invalid.",
    "created_at": "2008-09-08T13:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3075#issuecomment-21180",
    "user": "https://github.com/mwhansen"
}
```

I made #4078.

Do we even really want this feature for the notebook?  I'd vote for marking this ticket as invalid.



---

archive/issue_comments_021181.json:
```json
{
    "body": "I don't want it.",
    "created_at": "2008-09-08T13:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3075#issuecomment-21181",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I don't want it.



---

archive/issue_events_006950.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-01-22T13:03:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3075",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3075#event-6950"
}
```



---

archive/issue_comments_021182.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-22T13:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3075#issuecomment-21182",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_006951.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-01-22T13:03:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3075",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3075#event-6951"
}
```
