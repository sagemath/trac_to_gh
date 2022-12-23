# Issue 2688: Kuratowski subgraph isolator for planarity checking

archive/issues_002688.json:
```json
{
    "body": "Assignee: rlm\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2688\n\n",
    "created_at": "2008-03-27T20:54:59Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Kuratowski subgraph isolator for planarity checking",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2688",
    "user": "rlm"
}
```
Assignee: rlm



Issue created by migration from https://trac.sagemath.org/ticket/2688





---

archive/issue_comments_018506.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-29T05:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2688#issuecomment-18506",
    "user": "ekirkman"
}
```

Attachment



---

archive/issue_comments_018507.json:
```json
{
    "body": "Passes all tests after applying cleanly to 2.11.alpha1. I'll give it a try on alpha2 once it finishes building.",
    "created_at": "2008-03-29T17:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2688#issuecomment-18507",
    "user": "rlm"
}
```

Passes all tests after applying cleanly to 2.11.alpha1. I'll give it a try on alpha2 once it finishes building.



---

archive/issue_comments_018508.json:
```json
{
    "body": "Well, against my 2.11.rc0 build I got the following doctest failure:\n\n```\nsage -t  devel/sage-main/sage/graphs/graph.py\n**********************************************************************\nFile \"graph.py\", line 1695:\n    sage: cube.is_circular_planar()\nExpected:\n    False\nGot:\n    (False, Graph on 9 vertices)\n**********************************************************************\n```\n\nIt seems easy enough to fix. Care to update the patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T18:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2688#issuecomment-18508",
    "user": "mabshoff"
}
```

Well, against my 2.11.rc0 build I got the following doctest failure:

```
sage -t  devel/sage-main/sage/graphs/graph.py
**********************************************************************
File "graph.py", line 1695:
    sage: cube.is_circular_planar()
Expected:
    False
Got:
    (False, Graph on 9 vertices)
**********************************************************************
```

It seems easy enough to fix. Care to update the patch?

Cheers,

Michael



---

archive/issue_comments_018509.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-29T20:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2688#issuecomment-18509",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_018510.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T21:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2688#issuecomment-18510",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018511.json:
```json
{
    "body": "Merged 2688-kuratowski-isolator.patch and 2688-fix.patch in Sage 2.11.rc0",
    "created_at": "2008-03-29T21:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2688#issuecomment-18511",
    "user": "mabshoff"
}
```

Merged 2688-kuratowski-isolator.patch and 2688-fix.patch in Sage 2.11.rc0
