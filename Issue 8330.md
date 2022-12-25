# Issue 8330: BipartiteGraph needs to hook delete_vertex() and delete_vertices()

archive/issues_008330.json:
```json
{
    "body": "Assignee: @rhinton\n\nCC:  @rlmill @jasongrout @nathanncohen\n\nKeywords: BipartiteGraph\n\nBipartiteGraph needs to hook delete_vertex() and delete_vertices().\n\n\n```\n```\n\n\nIt should also hook the add_vertex() and add_edge() (and similar) calls, but not sure of the right way to do this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8330\n\n",
    "created_at": "2010-02-22T21:23:20Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "BipartiteGraph needs to hook delete_vertex() and delete_vertices()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8330",
    "user": "https://github.com/rhinton"
}
```
Assignee: @rhinton

CC:  @rlmill @jasongrout @nathanncohen

Keywords: BipartiteGraph

BipartiteGraph needs to hook delete_vertex() and delete_vertices().


```
```


It should also hook the add_vertex() and add_edge() (and similar) calls, but not sure of the right way to do this.

Issue created by migration from https://trac.sagemath.org/ticket/8330





---

archive/issue_comments_074049.json:
```json
{
    "body": "When you say \"hook\", do you mean \"define\"?",
    "created_at": "2010-02-23T00:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74049",
    "user": "https://github.com/jasongrout"
}
```

When you say "hook", do you mean "define"?



---

archive/issue_comments_074050.json:
```json
{
    "body": "#1941 is relevant.",
    "created_at": "2010-02-23T01:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74050",
    "user": "https://github.com/rlmill"
}
```

#1941 is relevant.



---

archive/issue_comments_074051.json:
```json
{
    "body": "Yes, I do mean define these methods.  The proposed method definitions just call the corresponding method in Graph, then adjust the partition lists.  So it feels to me like a driver \"hook\" where you call the existing function but add a little extra functionality before or after.\n\nThe patch defines the needed methods including doctests that pass.",
    "created_at": "2010-02-23T02:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74051",
    "user": "https://github.com/rhinton"
}
```

Yes, I do mean define these methods.  The proposed method definitions just call the corresponding method in Graph, then adjust the partition lists.  So it feels to me like a driver "hook" where you call the existing function but add a little extra functionality before or after.

The patch defines the needed methods including doctests that pass.



---

archive/issue_comments_074052.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-23T02:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74052",
    "user": "https://github.com/rhinton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074053.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-24T17:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74053",
    "user": "https://github.com/rhinton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074054.json:
```json
{
    "body": "I just tested graph.py for another potential change, and found that a few doctests fail due to this patch.  Specifically, the tests create BipartiteGraphs (e.g. K23), and the Graph algorithm adds a temp vertex, then deletes it later.  But the new delete_vertex() raises an exception when it can't find the temp vertex in its left or right sets.\n\nSo we may need to fix add_vertex before this delete_vertex solution will work.  Or should we do a soft-fail (print a warning?) instead of raising an exception?",
    "created_at": "2010-02-24T17:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74054",
    "user": "https://github.com/rhinton"
}
```

I just tested graph.py for another potential change, and found that a few doctests fail due to this patch.  Specifically, the tests create BipartiteGraphs (e.g. K23), and the Graph algorithm adds a temp vertex, then deletes it later.  But the new delete_vertex() raises an exception when it can't find the temp vertex in its left or right sets.

So we may need to fix add_vertex before this delete_vertex solution will work.  Or should we do a soft-fail (print a warning?) instead of raising an exception?



---

archive/issue_comments_074055.json:
```json
{
    "body": "changing the ticket to handle add and delete methods for completeness",
    "created_at": "2010-03-02T02:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74055",
    "user": "https://github.com/rhinton"
}
```

changing the ticket to handle add and delete methods for completeness



---

archive/issue_comments_074056.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-03T01:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74056",
    "user": "https://github.com/rhinton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074057.json:
```json
{
    "body": "REQUIRES #8421. Implements add/delete vertex/vertices and to_undirected to fix a failing doctest elsewhere.",
    "created_at": "2010-03-05T02:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74057",
    "user": "https://github.com/rhinton"
}
```

REQUIRES #8421. Implements add/delete vertex/vertices and to_undirected to fix a failing doctest elsewhere.



---

archive/issue_comments_074058.json:
```json
{
    "body": "Attachment [trac_8330-bipartite-delete-vertex.patch](tarball://root/attachments/some-uuid/ticket8330/trac_8330-bipartite-delete-vertex.patch) by @nathanncohen created at 2010-04-01 12:30:24\n\nHello !!!\n\nNice patch, applies and does its job... I fixed one or two things... If you think they are ok, you can set this ticket to \"positive review\" :-)\n\nNathann",
    "created_at": "2010-04-01T12:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74058",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_8330-bipartite-delete-vertex.patch](tarball://root/attachments/some-uuid/ticket8330/trac_8330-bipartite-delete-vertex.patch) by @nathanncohen created at 2010-04-01 12:30:24

Hello !!!

Nice patch, applies and does its job... I fixed one or two things... If you think they are ok, you can set this ticket to "positive review" :-)

Nathann



---

archive/issue_comments_074059.json:
```json
{
    "body": "Attachment [trac_8330-smallfixes.patch](tarball://root/attachments/some-uuid/ticket8330/trac_8330-smallfixes.patch) by @nathanncohen created at 2010-04-15 14:25:50\n\nWell, it has been two weeks and I only fixed three lines, so let's say this ticket is positively reviewed ^^;\n\nNathann",
    "created_at": "2010-04-15T14:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74059",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_8330-smallfixes.patch](tarball://root/attachments/some-uuid/ticket8330/trac_8330-smallfixes.patch) by @nathanncohen created at 2010-04-15 14:25:50

Well, it has been two weeks and I only fixed three lines, so let's say this ticket is positively reviewed ^^;

Nathann



---

archive/issue_comments_074060.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-15T14:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74060",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074061.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74061",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_074062.json:
```json
{
    "body": "Merged into 4.4.alpha0:\n- trac_8330-bipartite-delete-vertex.patch\n- trac_8330-smallfixes.patch",
    "created_at": "2010-04-15T23:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8330#issuecomment-74062",
    "user": "https://github.com/jhpalmieri"
}
```

Merged into 4.4.alpha0:
- trac_8330-bipartite-delete-vertex.patch
- trac_8330-smallfixes.patch
