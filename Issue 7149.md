# Issue 7149: [with patch, needs review] tutorial: delete the graph theory section

archive/issues_007149.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/b0d82d01bc1f123?tvc=2):\n\n```\nAs of version 4.1.2.alpha2, the Sage tutorial has a section containing \na guided tour of graph theory in Sage.  In principle, this is a good \nidea, but the execution is severely flawed: about 2/3 of the tour \nfocuses on the methods \"g.max_matching()\", \"g.edge_coloring()\", and \n\"g.vertex_coloring()\".  There are no such methods in Sage.  (The \nrelevant doctests were never executed because of the issue discussed \nat trac ticket #6572.)  Since the tutorial ought to be one of the \nfirst pieces of documentation people use, this situation is \ndisastrous. \n\nI suggest that before we release 4.1.2, we delete this part of the \ntutorial until the file is fixed.  (Alternatively, we could delete 2/3 \nof the file, but that might make it a bit short on substance.) \n```\nSee #6572 for some related issues.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7149\n\n",
    "created_at": "2009-10-08T00:54:23Z",
    "labels": [
        "component: documentation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] tutorial: delete the graph theory section",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7149",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/b0d82d01bc1f123?tvc=2):

```
As of version 4.1.2.alpha2, the Sage tutorial has a section containing 
a guided tour of graph theory in Sage.  In principle, this is a good 
idea, but the execution is severely flawed: about 2/3 of the tour 
focuses on the methods "g.max_matching()", "g.edge_coloring()", and 
"g.vertex_coloring()".  There are no such methods in Sage.  (The 
relevant doctests were never executed because of the issue discussed 
at trac ticket #6572.)  Since the tutorial ought to be one of the 
first pieces of documentation people use, this situation is 
disastrous. 

I suggest that before we release 4.1.2, we delete this part of the 
tutorial until the file is fixed.  (Alternatively, we could delete 2/3 
of the file, but that might make it a bit short on substance.) 
```
See #6572 for some related issues.


Issue created by migration from https://trac.sagemath.org/ticket/7149





---

archive/issue_comments_059125.json:
```json
{
    "body": "Attachment [trac_7149-delete-graphtheory.patch](tarball://root/attachments/some-uuid/ticket7149/trac_7149-delete-graphtheory.patch) by @williamstein created at 2009-10-08 01:05:41\n\nthanks for noticing this!\n\nmerged in 4.2.1.rc1",
    "created_at": "2009-10-08T01:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7149#issuecomment-59125",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7149-delete-graphtheory.patch](tarball://root/attachments/some-uuid/ticket7149/trac_7149-delete-graphtheory.patch) by @williamstein created at 2009-10-08 01:05:41

thanks for noticing this!

merged in 4.2.1.rc1



---

archive/issue_events_016901.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-08T01:05:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7149",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7149#event-16901"
}
```



---

archive/issue_comments_059126.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-08T01:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7149#issuecomment-59126",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_059127.json:
```json
{
    "body": "This was from #6774.  I gave it a positive review, pending the merging of the tickets with the necessary functionality, since I did not have those tickets merged in my tree yet.  Minh merged it after the doctests passed (I guess assuming that the functions had been merged then), so it does look like it was a problem of the doctests not actually being run (manually or otherwise!).\n\nThanks for catching this; sorry for the bother!\n\nWe should probably reopen #6774 now, for when the functionality is merged into Sage.",
    "created_at": "2009-10-08T02:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7149#issuecomment-59127",
    "user": "https://github.com/jasongrout"
}
```

This was from #6774.  I gave it a positive review, pending the merging of the tickets with the necessary functionality, since I did not have those tickets merged in my tree yet.  Minh merged it after the doctests passed (I guess assuming that the functions had been merged then), so it does look like it was a problem of the doctests not actually being run (manually or otherwise!).

Thanks for catching this; sorry for the bother!

We should probably reopen #6774 now, for when the functionality is merged into Sage.



---

archive/issue_comments_059128.json:
```json
{
    "body": "We can reopen #6774 or open a new ticket -- I'm not sure which is better.  In any case, we should make sure that the most recent version of the graph theory tour is included (combining at least #6774 and #6952 -- are there any other relevant tickets?).",
    "created_at": "2009-10-08T02:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7149#issuecomment-59128",
    "user": "https://github.com/jhpalmieri"
}
```

We can reopen #6774 or open a new ticket -- I'm not sure which is better.  In any case, we should make sure that the most recent version of the graph theory tour is included (combining at least #6774 and #6952 -- are there any other relevant tickets?).



---

archive/issue_events_016902.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-19T06:10:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7149",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7149#event-16902"
}
```
