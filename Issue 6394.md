# Issue 6394: Fix fallout from removal of graph_isom in 4.1.alpha1

archive/issues_006394.json:
```json
{
    "body": "Assignee: @rlmill\n\nThese are the failing tests:\n\n```\n        sage -t  devel/sage-main/sage/databases/database.py # 20 doctests failed\n        sage -t  devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed\n        sage -t  devel/sage-main/sage/graphs/graph.py # 25 doctests failed\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6394\n\n",
    "created_at": "2009-06-24T11:56:39Z",
    "labels": [
        "component: graph theory",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Fix fallout from removal of graph_isom in 4.1.alpha1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6394",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

These are the failing tests:

```
        sage -t  devel/sage-main/sage/databases/database.py # 20 doctests failed
        sage -t  devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed
        sage -t  devel/sage-main/sage/graphs/graph.py # 25 doctests failed

```


Issue created by migration from https://trac.sagemath.org/ticket/6394





---

archive/issue_comments_051278.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2009-06-24T19:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6394#issuecomment-51278",
    "user": "https://github.com/rlmill"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_051279.json:
```json
{
    "body": "Attachment [trac_6394-graph_isom_fallout.patch](tarball://root/attachments/some-uuid/ticket6394/trac_6394-graph_isom_fallout.patch) by @rlmill created at 2009-06-24 19:26:57",
    "created_at": "2009-06-24T19:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6394#issuecomment-51279",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6394-graph_isom_fallout.patch](tarball://root/attachments/some-uuid/ticket6394/trac_6394-graph_isom_fallout.patch) by @rlmill created at 2009-06-24 19:26:57



---

archive/issue_comments_051280.json:
```json
{
    "body": "works for me",
    "created_at": "2009-06-25T17:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6394#issuecomment-51280",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

works for me



---

archive/issue_comments_051281.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-25T17:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6394#issuecomment-51281",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_015073.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-06-25T17:53:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6394",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6394#event-15073"
}
```
