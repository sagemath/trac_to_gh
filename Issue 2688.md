# Issue 2688: Kuratowski subgraph isolator for planarity checking

archive/issues_002688.json:
```json
{
    "body": "Assignee: @rlmill\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2688\n\n",
    "created_at": "2008-03-27T20:54:59Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "Kuratowski subgraph isolator for planarity checking",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2688",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill



Issue created by migration from https://trac.sagemath.org/ticket/2688





---

archive/issue_comments_018467.json:
```json
{
    "body": "Attachment [2688-kuratowski-isolator.patch](tarball://root/attachments/some-uuid/ticket2688/2688-kuratowski-isolator.patch) by ekirkman created at 2008-03-29 05:56:29",
    "created_at": "2008-03-29T05:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2688#issuecomment-18467",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

Attachment [2688-kuratowski-isolator.patch](tarball://root/attachments/some-uuid/ticket2688/2688-kuratowski-isolator.patch) by ekirkman created at 2008-03-29 05:56:29



---

archive/issue_comments_018468.json:
```json
{
    "body": "Passes all tests after applying cleanly to 2.11.alpha1. I'll give it a try on alpha2 once it finishes building.",
    "created_at": "2008-03-29T17:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2688#issuecomment-18468",
    "user": "https://github.com/rlmill"
}
```

Passes all tests after applying cleanly to 2.11.alpha1. I'll give it a try on alpha2 once it finishes building.



---

archive/issue_comments_018469.json:
```json
{
    "body": "Well, against my 2.11.rc0 build I got the following doctest failure:\n\n```\nsage -t  devel/sage-main/sage/graphs/graph.py\n**********************************************************************\nFile \"graph.py\", line 1695:\n    sage: cube.is_circular_planar()\nExpected:\n    False\nGot:\n    (False, Graph on 9 vertices)\n**********************************************************************\n```\nIt seems easy enough to fix. Care to update the patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T18:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2688#issuecomment-18469",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_018470.json:
```json
{
    "body": "Attachment [2688-fix.patch](tarball://root/attachments/some-uuid/ticket2688/2688-fix.patch) by @rlmill created at 2008-03-29 20:45:35",
    "created_at": "2008-03-29T20:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2688#issuecomment-18470",
    "user": "https://github.com/rlmill"
}
```

Attachment [2688-fix.patch](tarball://root/attachments/some-uuid/ticket2688/2688-fix.patch) by @rlmill created at 2008-03-29 20:45:35



---

archive/issue_comments_018471.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T21:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2688#issuecomment-18471",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018472.json:
```json
{
    "body": "Merged 2688-kuratowski-isolator.patch and 2688-fix.patch in Sage 2.11.rc0",
    "created_at": "2008-03-29T21:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2688#issuecomment-18472",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2688-kuratowski-isolator.patch and 2688-fix.patch in Sage 2.11.rc0



---

archive/issue_events_006274.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-29T21:54:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2688",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2688#event-6274"
}
```
