# Issue 5914: default edge color is *invisible*

archive/issues_005914.json:
```json
{
    "body": "Assignee: @rlmill\n\nIf you do\n\nsage: G = graphs.CompleteGraph(5)\nsage: G.show(edge_colors={'red':(0,1)})\n\nwhat you get is one red edge...\n\nThe default color should be black.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5914\n\n",
    "created_at": "2009-04-27T19:06:21Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "default edge color is *invisible*",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5914",
    "user": "@rlmill"
}
```
Assignee: @rlmill

If you do

sage: G = graphs.CompleteGraph(5)
sage: G.show(edge_colors={'red':(0,1)})

what you get is one red edge...

The default color should be black.

Issue created by migration from https://trac.sagemath.org/ticket/5914





---

archive/issue_comments_046747.json:
```json
{
    "body": "vertex_colors might also suffer from the same problem...",
    "created_at": "2009-04-27T19:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5914#issuecomment-46747",
    "user": "@jasongrout"
}
```

vertex_colors might also suffer from the same problem...



---

archive/issue_comments_046748.json:
```json
{
    "body": "Attachment [trac_5914.patch](tarball://root/attachments/some-uuid/ticket5914/trac_5914.patch) by @williamstein created at 2009-04-28 14:00:57\n\nQuick remark: If you do \n\n```\nsage: G = graphs.CompleteGraph(5)\nsage: G.show(edge_colors={'red':(0,1)})\n```\n\nas you put in the ticket description, you get an error.  The proper input is:\n\n```\nsage: G = graphs.CompleteGraph(5)\nsage: G.show(edge_colors={'red':[(0,1)]})\n```\n\n\nThis patch works fine.",
    "created_at": "2009-04-28T14:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5914#issuecomment-46748",
    "user": "@williamstein"
}
```

Attachment [trac_5914.patch](tarball://root/attachments/some-uuid/ticket5914/trac_5914.patch) by @williamstein created at 2009-04-28 14:00:57

Quick remark: If you do 

```
sage: G = graphs.CompleteGraph(5)
sage: G.show(edge_colors={'red':(0,1)})
```

as you put in the ticket description, you get an error.  The proper input is:

```
sage: G = graphs.CompleteGraph(5)
sage: G.show(edge_colors={'red':[(0,1)]})
```


This patch works fine.



---

archive/issue_comments_046749.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T02:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5914#issuecomment-46749",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046750.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T02:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5914#issuecomment-46750",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael
