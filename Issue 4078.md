# Issue 4078: [with patch, needs review] evaluate all has sometimes erratic behavior

archive/issues_004078.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n10:13 < mabshoff> And I have been slipping in FreeBSD fixes when no one was looking ;)\n10:16 < jason|log> okay, \"flaky\" == in one cell, I have a=[] and i=1, the next I have a.append(i).  \n                   Evaluate all sometimes gives me an error in the second cell and says that 'a' is not \n                   defined.\n10:16 < jason|log> I can't reproduce it on sage.math in the few minutes I tried.\n10:18 < jason|log> wstein: could the problem be the asynchronous requests to evaluate the cells?  One \n                   request gets ahead of another sometimes?\n10:19 < jason|log> (not in the sending, but in the server receiving the requests?)\n10:19 < wstein> Yes, that is possible.\n10:20 < wstein> The right fix would be to make a single \"evaluateall\" command that gets sent\n10:20 < wstein> to the notebook server.\n10:20 < wstein> Right now a stupid evaluate_all javascript function calls evaluate_cell on each cell.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4078\n\n",
    "created_at": "2008-09-08T13:52:56Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] evaluate all has sometimes erratic behavior",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4078",
    "user": "@mwhansen"
}
```
Assignee: boothby


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


Issue created by migration from https://trac.sagemath.org/ticket/4078





---

archive/issue_comments_029432.json:
```json
{
    "body": "Attachment [trac_4078.patch](tarball://root/attachments/some-uuid/ticket4078/trac_4078.patch) by @mwhansen created at 2008-09-08 17:30:23\n\nSee this thread: http://groups.google.com/group/sage-support/browse_thread/thread/2bb639b190728393/50bf3da4522eaa63?lnk=gst&q=%22evaluate+all%22#50bf3da4522eaa63",
    "created_at": "2008-09-08T17:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4078#issuecomment-29432",
    "user": "@mwhansen"
}
```

Attachment [trac_4078.patch](tarball://root/attachments/some-uuid/ticket4078/trac_4078.patch) by @mwhansen created at 2008-09-08 17:30:23

See this thread: http://groups.google.com/group/sage-support/browse_thread/thread/2bb639b190728393/50bf3da4522eaa63?lnk=gst&q=%22evaluate+all%22#50bf3da4522eaa63



---

archive/issue_comments_029433.json:
```json
{
    "body": "I strongly agree with this fix.",
    "created_at": "2008-09-09T01:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4078#issuecomment-29433",
    "user": "@williamstein"
}
```

I strongly agree with this fix.



---

archive/issue_comments_029434.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-09T02:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4078#issuecomment-29434",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_comments_029435.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-09T02:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4078#issuecomment-29435",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029436.json:
```json
{
    "body": "I don't like how this was done.  On a slow net connection, (or, if your wireless connection breaks) this can cause the entire browser (or browser window, or just the tab) to completely lock up.  *bad*",
    "created_at": "2008-09-09T20:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4078#issuecomment-29436",
    "user": "boothby"
}
```

I don't like how this was done.  On a slow net connection, (or, if your wireless connection breaks) this can cause the entire browser (or browser window, or just the tab) to completely lock up.  *bad*
