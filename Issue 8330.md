# Issue 8330: BipartiteGraph needs to hook delete_vertex() and delete_vertices()

archive/issues_008330.json:
```json
{
    "body": "Assignee: rhinton\n\nCC:  rlm jason ncohen\n\nKeywords: BipartiteGraph\n\nBipartiteGraph needs to hook delete_vertex() and delete_vertices().\n\n\n```\n```\n\n\nIt should also hook the add_vertex() and add_edge() (and similar) calls, but not sure of the right way to do this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8330\n\n",
    "created_at": "2010-02-22T21:23:20Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "BipartiteGraph needs to hook delete_vertex() and delete_vertices()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8330",
    "user": "rhinton"
}
```
Assignee: rhinton

CC:  rlm jason ncohen

Keywords: BipartiteGraph

BipartiteGraph needs to hook delete_vertex() and delete_vertices().


```
```


It should also hook the add_vertex() and add_edge() (and similar) calls, but not sure of the right way to do this.

Issue created by migration from https://trac.sagemath.org/ticket/8330





---

archive/issue_comments_074173.json:
```json
{
    "body": "When you say \"hook\", do you mean \"define\"?",
    "created_at": "2010-02-23T00:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74173",
    "user": "jason"
}
```

When you say "hook", do you mean "define"?



---

archive/issue_comments_074174.json:
```json
{
    "body": "#1941 is relevant.",
    "created_at": "2010-02-23T01:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74174",
    "user": "rlm"
}
```

#1941 is relevant.



---

archive/issue_comments_074175.json:
```json
{
    "body": "Yes, I do mean define these methods.  The proposed method definitions just call the corresponding method in Graph, then adjust the partition lists.  So it feels to me like a driver \"hook\" where you call the existing function but add a little extra functionality before or after.\n\nThe patch defines the needed methods including doctests that pass.",
    "created_at": "2010-02-23T02:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74175",
    "user": "rhinton"
}
```

Yes, I do mean define these methods.  The proposed method definitions just call the corresponding method in Graph, then adjust the partition lists.  So it feels to me like a driver "hook" where you call the existing function but add a little extra functionality before or after.

The patch defines the needed methods including doctests that pass.



---

archive/issue_comments_074176.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-23T02:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74176",
    "user": "rhinton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074177.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-24T17:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74177",
    "user": "rhinton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074178.json:
```json
{
    "body": "I just tested graph.py for another potential change, and found that a few doctests fail due to this patch.  Specifically, the tests create BipartiteGraphs (e.g. K23), and the Graph algorithm adds a temp vertex, then deletes it later.  But the new delete_vertex() raises an exception when it can't find the temp vertex in its left or right sets.\n\nSo we may need to fix add_vertex before this delete_vertex solution will work.  Or should we do a soft-fail (print a warning?) instead of raising an exception?",
    "created_at": "2010-02-24T17:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74178",
    "user": "rhinton"
}
```

I just tested graph.py for another potential change, and found that a few doctests fail due to this patch.  Specifically, the tests create BipartiteGraphs (e.g. K23), and the Graph algorithm adds a temp vertex, then deletes it later.  But the new delete_vertex() raises an exception when it can't find the temp vertex in its left or right sets.

So we may need to fix add_vertex before this delete_vertex solution will work.  Or should we do a soft-fail (print a warning?) instead of raising an exception?



---

archive/issue_comments_074179.json:
```json
{
    "body": "changing the ticket to handle add and delete methods for completeness",
    "created_at": "2010-03-02T02:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74179",
    "user": "rhinton"
}
```

changing the ticket to handle add and delete methods for completeness



---

archive/issue_comments_074180.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-03T01:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74180",
    "user": "rhinton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074181.json:
```json
{
    "body": "REQUIRES #8421. Implements add/delete vertex/vertices and to_undirected to fix a failing doctest elsewhere.",
    "created_at": "2010-03-05T02:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74181",
    "user": "rhinton"
}
```

REQUIRES #8421. Implements add/delete vertex/vertices and to_undirected to fix a failing doctest elsewhere.



---

archive/issue_comments_074182.json:
```json
{
    "body": "Attachment [trac_8330-bipartite-delete-vertex.patch](tarball://root/attachments/some-uuid/ticket8330/trac_8330-bipartite-delete-vertex.patch) by ncohen created at 2010-04-01 12:30:24\n\nHello !!!\n\nNice patch, applies and does its job... I fixed one or two things... If you think they are ok, you can set this ticket to \"positive review\" :-)\n\nNathann",
    "created_at": "2010-04-01T12:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74182",
    "user": "ncohen"
}
```

Attachment [trac_8330-bipartite-delete-vertex.patch](tarball://root/attachments/some-uuid/ticket8330/trac_8330-bipartite-delete-vertex.patch) by ncohen created at 2010-04-01 12:30:24

Hello !!!

Nice patch, applies and does its job... I fixed one or two things... If you think they are ok, you can set this ticket to "positive review" :-)

Nathann



---

archive/issue_comments_074183.json:
```json
{
    "body": "Attachment [trac_8330-smallfixes.patch](tarball://root/attachments/some-uuid/ticket8330/trac_8330-smallfixes.patch) by ncohen created at 2010-04-15 14:25:50\n\nWell, it has been two weeks and I only fixed three lines, so let's say this ticket is positively reviewed ^^;\n\nNathann",
    "created_at": "2010-04-15T14:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74183",
    "user": "ncohen"
}
```

Attachment [trac_8330-smallfixes.patch](tarball://root/attachments/some-uuid/ticket8330/trac_8330-smallfixes.patch) by ncohen created at 2010-04-15 14:25:50

Well, it has been two weeks and I only fixed three lines, so let's say this ticket is positively reviewed ^^;

Nathann



---

archive/issue_comments_074184.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-15T14:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74184",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074185.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74185",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_074186.json:
```json
{
    "body": "Merged into 4.4.alpha0:\n- trac_8330-bipartite-delete-vertex.patch\n- trac_8330-smallfixes.patch",
    "created_at": "2010-04-15T23:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74186",
    "user": "jhpalmieri"
}
```

Merged into 4.4.alpha0:
- trac_8330-bipartite-delete-vertex.patch
- trac_8330-smallfixes.patch
