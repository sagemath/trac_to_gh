# Issue 850: graphs: create graph by specifying vertices and a function giving adjacencies

archive/issues_000850.json:
```json
{
    "body": "Assignee: was\n\nKeywords: graphs\n\nIt would be very useful to be able to create a graph by giving a list of vertices and a function which specified the adjacencies.  See the doc examples in the patch for several examples.\n\nIssue created by migration from https://trac.sagemath.org/ticket/850\n\n",
    "created_at": "2007-10-11T15:33:15Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "graphs: create graph by specifying vertices and a function giving adjacencies",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/850",
    "user": "jason"
}
```
Assignee: was

Keywords: graphs

It would be very useful to be able to create a graph by giving a list of vertices and a function which specified the adjacencies.  See the doc examples in the patch for several examples.

Issue created by migration from https://trac.sagemath.org/ticket/850





---

archive/issue_comments_005254.json:
```json
{
    "body": "Attachment [function-init.patch](tarball://root/attachments/some-uuid/ticket850/function-init.patch) by jason created at 2007-10-11 15:34:01",
    "created_at": "2007-10-11T15:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/850#issuecomment-5254",
    "user": "jason"
}
```

Attachment [function-init.patch](tarball://root/attachments/some-uuid/ticket850/function-init.patch) by jason created at 2007-10-11 15:34:01



---

archive/issue_comments_005255.json:
```json
{
    "body": "I just noticed that the comment in the DiGraph __init__ function should be changed from: \n\n                # Pass XGraph a dict of lists describing the adjacencies\nto\n                # Pass XDiGraph a dict of lists describing the adjacencies\n\nSorry.",
    "created_at": "2007-10-11T15:37:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/850#issuecomment-5255",
    "user": "jason"
}
```

I just noticed that the comment in the DiGraph __init__ function should be changed from: 

                # Pass XGraph a dict of lists describing the adjacencies
to
                # Pass XDiGraph a dict of lists describing the adjacencies

Sorry.



---

archive/issue_comments_005256.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/850#issuecomment-5256",
    "user": "was"
}
```

Resolution: fixed
