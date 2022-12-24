# Issue 8210: Problem in Displaying Graphs

archive/issues_008210.json:
```json
{
    "body": "Assignee: rlm\n\nKeywords: Graph\n\nFor example,\n\nk=graphs.CompleteGraph(6)\nshow(k)\n\nShows K6 but the vertices are partially chopped off.\n\nA work around would be \nshow(k, axes_pad=.1)\n\nBut I hope this can be fixed once and for all.\nThere are some discussion about this problem in SAGE Support.\nhttp://groups.google.com/group/sage-support/browse_thread/thread/85a797a886a6446f/4d58090a4c868200#4d58090a4c868200\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8210\n\n",
    "created_at": "2010-02-08T05:14:09Z",
    "labels": [
        "graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Problem in Displaying Graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8210",
    "user": "pong"
}
```
Assignee: rlm

Keywords: Graph

For example,

k=graphs.CompleteGraph(6)
show(k)

Shows K6 but the vertices are partially chopped off.

A work around would be 
show(k, axes_pad=.1)

But I hope this can be fixed once and for all.
There are some discussion about this problem in SAGE Support.
http://groups.google.com/group/sage-support/browse_thread/thread/85a797a886a6446f/4d58090a4c868200#4d58090a4c868200


Issue created by migration from https://trac.sagemath.org/ticket/8210





---

archive/issue_comments_072409.json:
```json
{
    "body": "This is a dup of #7299, and has been fixed in 4.3.2.",
    "created_at": "2010-02-09T15:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8210#issuecomment-72409",
    "user": "jason"
}
```

This is a dup of #7299, and has been fixed in 4.3.2.



---

archive/issue_comments_072410.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-02-09T15:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8210#issuecomment-72410",
    "user": "jason"
}
```

Resolution: duplicate
