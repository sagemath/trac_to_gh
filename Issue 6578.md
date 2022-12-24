# Issue 6578: fast subgraphs by building the graph instead of deleting things

archive/issues_006578.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @rlmill\n\nCurrently, to create a subgraph, Sage copies the graph and then deletes everything not specified.  This is very slow if you just want a small part of a large graph.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6578\n\n",
    "created_at": "2009-07-21T11:08:27Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "fast subgraphs by building the graph instead of deleting things",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6578",
    "user": "@jasongrout"
}
```
Assignee: @rlmill

CC:  @rlmill

Currently, to create a subgraph, Sage copies the graph and then deletes everything not specified.  This is very slow if you just want a small part of a large graph.

Issue created by migration from https://trac.sagemath.org/ticket/6578





---

archive/issue_comments_053698.json:
```json
{
    "body": "This patch refactors the subgraph code into two functions, and then tries to intelligently choose between building the graph from scratch and deleting vertices and edges from a copy of the graph.",
    "created_at": "2009-07-21T11:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6578#issuecomment-53698",
    "user": "@jasongrout"
}
```

This patch refactors the subgraph code into two functions, and then tries to intelligently choose between building the graph from scratch and deleting vertices and edges from a copy of the graph.



---

archive/issue_comments_053699.json:
```json
{
    "body": "Attachment [trac-6578-subgraph-refactoring.patch](tarball://root/attachments/some-uuid/ticket6578/trac-6578-subgraph-refactoring.patch) by @jasongrout created at 2009-07-21 11:41:40\n\nTiming comparison:\n\n\n```\nsage: g=graphs.PathGraph(100000)                     \nsage: %time g.subgraph(range(20), algorithm='add')   \nCPU times: user 0.61 s, sys: 0.01 s, total: 0.62 s\nWall time: 0.68 s\nSubgraph of (Path Graph): Graph on 20 vertices\nsage: %time g.subgraph(range(20), algorithm='delete') # the old algorithm\nCPU times: user 3.96 s, sys: 0.04 s, total: 4.00 s\nWall time: 4.15 s\nSubgraph of (Path Graph): Graph on 20 vertices\n```\n",
    "created_at": "2009-07-21T11:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6578#issuecomment-53699",
    "user": "@jasongrout"
}
```

Attachment [trac-6578-subgraph-refactoring.patch](tarball://root/attachments/some-uuid/ticket6578/trac-6578-subgraph-refactoring.patch) by @jasongrout created at 2009-07-21 11:41:40

Timing comparison:


```
sage: g=graphs.PathGraph(100000)                     
sage: %time g.subgraph(range(20), algorithm='add')   
CPU times: user 0.61 s, sys: 0.01 s, total: 0.62 s
Wall time: 0.68 s
Subgraph of (Path Graph): Graph on 20 vertices
sage: %time g.subgraph(range(20), algorithm='delete') # the old algorithm
CPU times: user 3.96 s, sys: 0.04 s, total: 4.00 s
Wall time: 4.15 s
Subgraph of (Path Graph): Graph on 20 vertices
```




---

archive/issue_comments_053700.json:
```json
{
    "body": "Jason,\n\nDo you have any examples where `delete` is actually faster than `add`? I ask because what this does is add every edge, and then delete a bunch of them. I doubt it's ever faster.",
    "created_at": "2009-07-21T21:08:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6578#issuecomment-53700",
    "user": "@rlmill"
}
```

Jason,

Do you have any examples where `delete` is actually faster than `add`? I ask because what this does is add every edge, and then delete a bunch of them. I doubt it's ever faster.



---

archive/issue_comments_053701.json:
```json
{
    "body": "Most of the time delete is faster than add; that's why I set the factor so that if we want more than 5% of the vertices, it does delete.\n\nI think delete copies the graph, which doesn't *add* every edge, but probably just copies the edge dictionary, which should be *way* faster.\n\nThe tests I was taking my data from was doing\n\n\n```\nsage: g=graphs.PathGraph(1000)\n```\n\n\nand then doing `g.subgraph(range(i)` using each of the algorithms.  The breakeven point seemed to be between 50 and 100.  I also did this with the complete graph, and got similar results.",
    "created_at": "2009-07-22T02:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6578#issuecomment-53701",
    "user": "@jasongrout"
}
```

Most of the time delete is faster than add; that's why I set the factor so that if we want more than 5% of the vertices, it does delete.

I think delete copies the graph, which doesn't *add* every edge, but probably just copies the edge dictionary, which should be *way* faster.

The tests I was taking my data from was doing


```
sage: g=graphs.PathGraph(1000)
```


and then doing `g.subgraph(range(i)` using each of the algorithms.  The breakeven point seemed to be between 50 and 100.  I also did this with the complete graph, and got similar results.



---

archive/issue_comments_053702.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> I think delete copies the graph, which doesn't *add* every edge, but probably just copies the edge dictionary, which should be *way* faster.\n\nWhat is this opinion based on? If it's not an inplace subgraph then it creates a copy, which calls networkx_graph, which calls NX's copy, which has the following lines:\n\n```\n        for e in self.edges_iter():\n            H.add_edge(e)\n```\n\n\nSo we're definitely not using the adjacency dictionary there. The crossover between add and delete you observed above is most likely due to overhead from the fact that calling Sage's add_edge is using several layers of Python functions.\n\nI expect this to change drastically once the graph backends are optimized. This may be a while in the future, but you should keep this in mind for when that does eventually happen. In general, this patch is an improvement, since it provides both options, but thinking in terms of optimization at this stage is going to result in wasted effort, since the floor is about to drop out from underneath any current timings.\n\nAnyway, everything looks good here (especially, applies to 4.1.1.alpha0 and passes tests), so let's go ahead and merge it!",
    "created_at": "2009-07-22T02:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6578#issuecomment-53702",
    "user": "@rlmill"
}
```

Replying to [comment:4 jason]:
> I think delete copies the graph, which doesn't *add* every edge, but probably just copies the edge dictionary, which should be *way* faster.

What is this opinion based on? If it's not an inplace subgraph then it creates a copy, which calls networkx_graph, which calls NX's copy, which has the following lines:

```
        for e in self.edges_iter():
            H.add_edge(e)
```


So we're definitely not using the adjacency dictionary there. The crossover between add and delete you observed above is most likely due to overhead from the fact that calling Sage's add_edge is using several layers of Python functions.

I expect this to change drastically once the graph backends are optimized. This may be a while in the future, but you should keep this in mind for when that does eventually happen. In general, this patch is an improvement, since it provides both options, but thinking in terms of optimization at this stage is going to result in wasted effort, since the floor is about to drop out from underneath any current timings.

Anyway, everything looks good here (especially, applies to 4.1.1.alpha0 and passes tests), so let's go ahead and merge it!



---

archive/issue_comments_053703.json:
```json
{
    "body": "The opinion was based on thinking of the most logical way to implement it (hence the \"I think\") :).  Thanks for looking into the code.\n\nI'm dreaming of the day that this optimization and choice is obsolete!  It would be *so* nice!",
    "created_at": "2009-07-22T06:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6578#issuecomment-53703",
    "user": "@jasongrout"
}
```

The opinion was based on thinking of the most logical way to implement it (hence the "I think") :).  Thanks for looking into the code.

I'm dreaming of the day that this optimization and choice is obsolete!  It would be *so* nice!



---

archive/issue_comments_053704.json:
```json
{
    "body": "referee patch",
    "created_at": "2009-07-23T05:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6578#issuecomment-53704",
    "user": "mvngu"
}
```

referee patch



---

archive/issue_comments_053705.json:
```json
{
    "body": "Attachment [trac_6578-referee.patch](tarball://root/attachments/some-uuid/ticket6578/trac_6578-referee.patch) by mvngu created at 2009-07-23 05:24:40\n\nThe patch `trac_6578-referee.patch` adds a missing double colon \"::\". It also deletes two sets of redundant double colons.",
    "created_at": "2009-07-23T05:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6578#issuecomment-53705",
    "user": "mvngu"
}
```

Attachment [trac_6578-referee.patch](tarball://root/attachments/some-uuid/ticket6578/trac_6578-referee.patch) by mvngu created at 2009-07-23 05:24:40

The patch `trac_6578-referee.patch` adds a missing double colon "::". It also deletes two sets of redundant double colons.



---

archive/issue_comments_053706.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T05:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6578#issuecomment-53706",
    "user": "mvngu"
}
```

Resolution: fixed
