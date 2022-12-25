# Issue 1089: [with patch] graphs: update subgraph to handle a list of edges

archive/issues_001089.json:
```json
{
    "body": "Assignee: @mwhansen\n\nKeywords: graphs\n\nHere is an update to the subgraph function to handle a list of edges.  If edges are not specified, then it reverts to the original functionality (returning an induced subgraph).\n\nI also fix a doctest that should have been complaining in transitive_reduction and make the doctests in min_spanning_tree make more sense.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1089\n\n",
    "created_at": "2007-11-03T20:48:47Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "[with patch] graphs: update subgraph to handle a list of edges",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1089",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @mwhansen

Keywords: graphs

Here is an update to the subgraph function to handle a list of edges.  If edges are not specified, then it reverts to the original functionality (returning an induced subgraph).

I also fix a doctest that should have been complaining in transitive_reduction and make the doctests in min_spanning_tree make more sense.

Issue created by migration from https://trac.sagemath.org/ticket/1089





---

archive/issue_comments_006573.json:
```json
{
    "body": "Attachment [subgraph-edges.patch](tarball://root/attachments/some-uuid/ticket1089/subgraph-edges.patch) by @rlmill created at 2007-11-03 23:29:50\n\nJason,\n\nPlease include a fresh patch that comes from a clean install of sage 2.8.11. The base version does not match. Also, the function subgraph(vertices) returns the induced subgraph with the given vertices and *all* edges from the original graph whose endpoints are in vertices. Perhaps the current function should be renamed induced_subgraph, and you could make a separate subgraph_from_edges() function. It also occurs to me that we don't yet have an is_subgraph fucntion...\n\nCheers,\n\nRobert M",
    "created_at": "2007-11-03T23:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1089#issuecomment-6573",
    "user": "https://github.com/rlmill"
}
```

Attachment [subgraph-edges.patch](tarball://root/attachments/some-uuid/ticket1089/subgraph-edges.patch) by @rlmill created at 2007-11-03 23:29:50

Jason,

Please include a fresh patch that comes from a clean install of sage 2.8.11. The base version does not match. Also, the function subgraph(vertices) returns the induced subgraph with the given vertices and *all* edges from the original graph whose endpoints are in vertices. Perhaps the current function should be renamed induced_subgraph, and you could make a separate subgraph_from_edges() function. It also occurs to me that we don't yet have an is_subgraph fucntion...

Cheers,

Robert M



---

archive/issue_events_002936.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-11-03T23:30:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1089#event-2936"
}
```



---

archive/issue_comments_006574.json:
```json
{
    "body": "Jason,\n\nI should have mentioned to apply the patches in #1088 to the clean version first, then patch on top of that.\n\nThanks, Robert M",
    "created_at": "2007-11-03T23:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1089#issuecomment-6574",
    "user": "https://github.com/rlmill"
}
```

Jason,

I should have mentioned to apply the patches in #1088 to the clean version first, then patch on top of that.

Thanks, Robert M



---

archive/issue_comments_006575.json:
```json
{
    "body": "Robert,\n\nYou're right, #1088 should be applied first.  This patch modifies a doctest in #1088 to be more sensible.  I was going to include the better doctest in #1088 to keep both patches more self-contained, but then the doctests wouldn't have passed after only applying #1088.  Did applying this patch after #1088 resolve the issue or would you still like me to rebase against 2.8.11?\n\nAs to the subgraph function: I think it's a reasonable idea to say that the subgraph function returns a graph that is the intersection of what is currently in the graph and the restrictions that you pass relating to vertices and edges (as represented by a list of \"allowable\" vertices and/or edges you pass the subgraph function).  If you pass just a restriction on the vertices to include in the subgraph, then there is no restriction on the edges and you get an induced subgraph.  If you pass a restriction on the edges, then you get a graph with the same vertices as the original graph, but with possibly fewer edges (that is what the added doctest tests).  If you pass a restriction on both the edges and vertices, then the returned graph only has vertices from the vertex set you passed and edges from the edge set you passed.  I don't think that we need to make several different functions for this feature.  But if you think it would be clearer to have several functions, let me know.\n\nOne of the things I'm trying to do here is consolidate functionality when it makes sense so that we don't end up having hundreds of different functions that people have to remember.  I guess the question here is whether it makes sense.\n\nAs for the is_subgraph function, I believe that that problem is quite a bit harder (in a technical sense) than the graph isomorphism problem, even if you restrict to induced subgraphs.  I suppose it would be fairly easy, though, to implement an is_induced_subgraph function by taking k-subsets of the vertices and asking if the induced subgraph is isomorphic to a given graph.\n\nA related feature request is for functions dealing with graph minors (constructing minors, asking if a graph is a minor of another, etc.).\n\nThanks for your comments and suggestions!",
    "created_at": "2007-11-04T03:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1089#issuecomment-6575",
    "user": "https://github.com/jasongrout"
}
```

Robert,

You're right, #1088 should be applied first.  This patch modifies a doctest in #1088 to be more sensible.  I was going to include the better doctest in #1088 to keep both patches more self-contained, but then the doctests wouldn't have passed after only applying #1088.  Did applying this patch after #1088 resolve the issue or would you still like me to rebase against 2.8.11?

As to the subgraph function: I think it's a reasonable idea to say that the subgraph function returns a graph that is the intersection of what is currently in the graph and the restrictions that you pass relating to vertices and edges (as represented by a list of "allowable" vertices and/or edges you pass the subgraph function).  If you pass just a restriction on the vertices to include in the subgraph, then there is no restriction on the edges and you get an induced subgraph.  If you pass a restriction on the edges, then you get a graph with the same vertices as the original graph, but with possibly fewer edges (that is what the added doctest tests).  If you pass a restriction on both the edges and vertices, then the returned graph only has vertices from the vertex set you passed and edges from the edge set you passed.  I don't think that we need to make several different functions for this feature.  But if you think it would be clearer to have several functions, let me know.

One of the things I'm trying to do here is consolidate functionality when it makes sense so that we don't end up having hundreds of different functions that people have to remember.  I guess the question here is whether it makes sense.

As for the is_subgraph function, I believe that that problem is quite a bit harder (in a technical sense) than the graph isomorphism problem, even if you restrict to induced subgraphs.  I suppose it would be fairly easy, though, to implement an is_induced_subgraph function by taking k-subsets of the vertices and asking if the induced subgraph is isomorphic to a given graph.

A related feature request is for functions dealing with graph minors (constructing minors, asking if a graph is a minor of another, etc.).

Thanks for your comments and suggestions!



---

archive/issue_comments_006576.json:
```json
{
    "body": "Jason,\n\nThe reason I was asking you to rebase is that I already patched up the doctests from 1088 (the second patch there). As far as patches go, you can do one of the following:\n\n1) Wait for sage-2.8.12 to be released, and do a patch on top of that.\n\n2) Apply *both* patches in ticket 1088 to a fresh 2.8.11, and do a patch on top of that.\n\nYou've convinced me that these functionalities should be in the same function. I was just thinking that the name \"subgraph\" was a little misleading for a function name. Under your interpretation, all of these would be induced subgraphs, so to speak. I don't know if induced_subgraph is better, since the first thing anyone would look for would be subgraph anyway, and it's shorter to type...\n\nIndeed, the subgraph isomorphism problem is NP-complete, but I was just talking about *is* subgraph, as a subset. Same vertices, same exact edges. I could see this being useful in some situations.",
    "created_at": "2007-11-06T19:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1089#issuecomment-6576",
    "user": "https://github.com/rlmill"
}
```

Jason,

The reason I was asking you to rebase is that I already patched up the doctests from 1088 (the second patch there). As far as patches go, you can do one of the following:

1) Wait for sage-2.8.12 to be released, and do a patch on top of that.

2) Apply *both* patches in ticket 1088 to a fresh 2.8.11, and do a patch on top of that.

You've convinced me that these functionalities should be in the same function. I was just thinking that the name "subgraph" was a little misleading for a function name. Under your interpretation, all of these would be induced subgraphs, so to speak. I don't know if induced_subgraph is better, since the first thing anyone would look for would be subgraph anyway, and it's shorter to type...

Indeed, the subgraph isomorphism problem is NP-complete, but I was just talking about *is* subgraph, as a subset. Same vertices, same exact edges. I could see this being useful in some situations.



---

archive/issue_comments_006577.json:
```json
{
    "body": "Attachment [subgraph_edges-updated.patch](tarball://root/attachments/some-uuid/ticket1089/subgraph_edges-updated.patch) by @jasongrout created at 2007-11-13 23:44:12\n\nCorrected bugs, rebased against 2.8.12, and put in more comprehensive doctests.",
    "created_at": "2007-11-13T23:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1089#issuecomment-6577",
    "user": "https://github.com/jasongrout"
}
```

Attachment [subgraph_edges-updated.patch](tarball://root/attachments/some-uuid/ticket1089/subgraph_edges-updated.patch) by @jasongrout created at 2007-11-13 23:44:12

Corrected bugs, rebased against 2.8.12, and put in more comprehensive doctests.



---

archive/issue_comments_006578.json:
```json
{
    "body": "The subgraph_edges-updated.patch should be applied instead of the subgraph_edges.patch.",
    "created_at": "2007-11-13T23:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1089#issuecomment-6578",
    "user": "https://github.com/jasongrout"
}
```

The subgraph_edges-updated.patch should be applied instead of the subgraph_edges.patch.



---

archive/issue_events_002937.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2007-11-13T23:45:19Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1089#event-2937"
}
```



---

archive/issue_events_002938.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2007-11-13T23:45:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1089#event-2938"
}
```



---

archive/issue_comments_006579.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2007-11-15T18:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1089#issuecomment-6579",
    "user": "https://github.com/rlmill"
}
```

Looks good to me.



---

archive/issue_events_002939.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-19T21:42:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1089#event-2939"
}
```



---

archive/issue_comments_006580.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-19T21:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1089#issuecomment-6580",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006581.json:
```json
{
    "body": "Merged in 2.8.13.alpha1.",
    "created_at": "2007-11-19T21:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1089#issuecomment-6581",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.13.alpha1.
