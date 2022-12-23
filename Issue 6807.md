# Issue 6807: bug in blocks_and_cut_vertices() of a graph where a cut vertex can be listed more than once

archive/issues_006807.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  rlm jason\n\nThere is another bug in blocks_and_cut_vertices() where cut vertices can appear more than once in the returned list of cut vertices.  Jason Grout pointed out this problem in ticket [#6632](http://trac.sagemath.org/sage_trac/ticket/6632#comment:5).\n\n\n```\nsage: graphs.StarGraph(3).blocks_and_cut_vertices()\n([[1, 0], [2, 0], [3, 0]], [0, 0, 0])\n```\n\n\nThe problem occurs because the list C of cut vertices should be treated as a set, not a list: membership should be tested before adding a vertex to the list.\n\nFollowing a suggestion of Jason's, I also changed the initialization of the parent array to None.\n\nPatch will be attached below.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6807\n\n",
    "created_at": "2009-08-22T21:30:28Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "bug in blocks_and_cut_vertices() of a graph where a cut vertex can be listed more than once",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6807",
    "user": "hartke"
}
```
Assignee: rlm

CC:  rlm jason

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

archive/issue_comments_056040.json:
```json
{
    "body": "Patch to fix bug in blocks_and_cut_vertices() in graph.py where cut vertices are repeated.",
    "created_at": "2009-08-22T21:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6807#issuecomment-56040",
    "user": "hartke"
}
```

Patch to fix bug in blocks_and_cut_vertices() in graph.py where cut vertices are repeated.



---

archive/issue_comments_056041.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-08-22T21:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6807#issuecomment-56041",
    "user": "hartke"
}
```

Attachment



---

archive/issue_comments_056042.json:
```json
{
    "body": "Applies ok, fixes the bug... ;-)",
    "created_at": "2009-08-25T15:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6807#issuecomment-56042",
    "user": "ncohen"
}
```

Applies ok, fixes the bug... ;-)



---

archive/issue_comments_056043.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-25T22:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6807#issuecomment-56043",
    "user": "mvngu"
}
```

Resolution: fixed
