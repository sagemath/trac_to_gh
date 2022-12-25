# Issue 850: graphs: create graph by specifying vertices and a function giving adjacencies

archive/issues_000850.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: graphs\n\nIt would be very useful to be able to create a graph by giving a list of vertices and a function which specified the adjacencies.  See the doc examples in the patch for several examples.\n\nIssue created by migration from https://trac.sagemath.org/ticket/850\n\n",
    "created_at": "2007-10-11T15:33:15Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "graphs: create graph by specifying vertices and a function giving adjacencies",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/850",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Keywords: graphs

It would be very useful to be able to create a graph by giving a list of vertices and a function which specified the adjacencies.  See the doc examples in the patch for several examples.

Issue created by migration from https://trac.sagemath.org/ticket/850





---

archive/issue_comments_005238.json:
```json
{
    "body": "Attachment [function-init.patch](tarball://root/attachments/some-uuid/ticket850/function-init.patch) by @jasongrout created at 2007-10-11 15:34:01",
    "created_at": "2007-10-11T15:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/850#issuecomment-5238",
    "user": "https://github.com/jasongrout"
}
```

Attachment [function-init.patch](tarball://root/attachments/some-uuid/ticket850/function-init.patch) by @jasongrout created at 2007-10-11 15:34:01



---

archive/issue_comments_005239.json:
```json
{
    "body": "I just noticed that the comment in the DiGraph __init__ function should be changed from: \n\n                # Pass XGraph a dict of lists describing the adjacencies\nto\n                # Pass XDiGraph a dict of lists describing the adjacencies\n\nSorry.",
    "created_at": "2007-10-11T15:37:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/850#issuecomment-5239",
    "user": "https://github.com/jasongrout"
}
```

I just noticed that the comment in the DiGraph __init__ function should be changed from: 

                # Pass XGraph a dict of lists describing the adjacencies
to
                # Pass XDiGraph a dict of lists describing the adjacencies

Sorry.



---

archive/issue_events_002391.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-13T07:25:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/850",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/850#event-2391"
}
```



---

archive/issue_comments_005240.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/850#issuecomment-5240",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
