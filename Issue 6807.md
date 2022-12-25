# Issue 6807: bug in blocks_and_cut_vertices() of a graph where a cut vertex can be listed more than once

archive/issues_006807.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @rlmill @jasongrout\n\nThere is another bug in blocks_and_cut_vertices() where cut vertices can appear more than once in the returned list of cut vertices.  Jason Grout pointed out this problem in ticket [#6632](http://trac.sagemath.org/sage_trac/ticket/6632#comment:5).\n\n\n```\nsage: graphs.StarGraph(3).blocks_and_cut_vertices()\n([[1, 0], [2, 0], [3, 0]], [0, 0, 0])\n```\n\n\nThe problem occurs because the list C of cut vertices should be treated as a set, not a list: membership should be tested before adding a vertex to the list.\n\nFollowing a suggestion of Jason's, I also changed the initialization of the parent array to None.\n\nPatch will be attached below.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6807\n\n",
    "created_at": "2009-08-22T21:30:28Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "bug in blocks_and_cut_vertices() of a graph where a cut vertex can be listed more than once",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6807",
    "user": "https://trac.sagemath.org/admin/accounts/users/hartke"
}
```
Assignee: @rlmill

CC:  @rlmill @jasongrout

There is another bug in blocks_and_cut_vertices() where cut vertices can appear more than once in the returned list of cut vertices.  Jason Grout pointed out this problem in ticket [#6632](http://trac.sagemath.org/sage_trac/ticket/6632#comment:5).


```
sage: graphs.StarGraph(3).blocks_and_cut_vertices()
([[1, 0], [2, 0], [3, 0]], [0, 0, 0])
```


The problem occurs because the list C of cut vertices should be treated as a set, not a list: membership should be tested before adding a vertex to the list.

Following a suggestion of Jason's, I also changed the initialization of the parent array to None.

Patch will be attached below.


Issue created by migration from https://trac.sagemath.org/ticket/6807





---

archive/issue_comments_055938.json:
```json
{
    "body": "Patch to fix bug in blocks_and_cut_vertices() in graph.py where cut vertices are repeated.",
    "created_at": "2009-08-22T21:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6807#issuecomment-55938",
    "user": "https://trac.sagemath.org/admin/accounts/users/hartke"
}
```

Patch to fix bug in blocks_and_cut_vertices() in graph.py where cut vertices are repeated.



---

archive/issue_comments_055939.json:
```json
{
    "body": "Attachment [blocks_and_cut_vertices-6807.patch](tarball://root/attachments/some-uuid/ticket6807/blocks_and_cut_vertices-6807.patch) by hartke created at 2009-08-22 21:36:24",
    "created_at": "2009-08-22T21:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6807#issuecomment-55939",
    "user": "https://trac.sagemath.org/admin/accounts/users/hartke"
}
```

Attachment [blocks_and_cut_vertices-6807.patch](tarball://root/attachments/some-uuid/ticket6807/blocks_and_cut_vertices-6807.patch) by hartke created at 2009-08-22 21:36:24



---

archive/issue_comments_055940.json:
```json
{
    "body": "Applies ok, fixes the bug... ;-)",
    "created_at": "2009-08-25T15:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6807#issuecomment-55940",
    "user": "https://github.com/nathanncohen"
}
```

Applies ok, fixes the bug... ;-)



---

archive/issue_events_007042.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-25T22:25:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6807",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6807#event-7042"
}
```



---

archive/issue_comments_055941.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-25T22:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6807#issuecomment-55941",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
