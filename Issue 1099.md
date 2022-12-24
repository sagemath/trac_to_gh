# Issue 1099: graphs: consolidating delete functionality

archive/issues_001099.json:
```json
{
    "body": "Assignee: mhansen\n\nKeywords: graphs\n\nCurrently there are four different functions to delete things from a graph: delete_edge, delete_edges, delete_vertex, and delete_vertices.  How about we consolidate these into one function, \"delete\", that looks like this:\n\ndelete(vertices=list_of_vertices, edges=list_of_edges) deletes the vertices specified, then the edges specified.\n\nSo:\n\n* delete_vertex(v) == delete(vertices=[v])\n\n* delete_vertices(list) == delete(vertices=list)\n\n* delete_edge(e) == delete(edges=[e])\n\n* delete_edges(list) == delete(edges=list)\n\n* deleting vertices and edges is accomplished by passing both parameters in.\n\nThis idea may be completely irrational, but I thought I'd throw it out in an effort to consolidate functions and make the interface simpler to remember.  What do you think?\n\n(I'm ignoring delete_multiedge here, though we could probably include that in as an option to delete).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1099\n\n",
    "created_at": "2007-11-04T03:30:51Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "graphs: consolidating delete functionality",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1099",
    "user": "jason"
}
```
Assignee: mhansen

Keywords: graphs

Currently there are four different functions to delete things from a graph: delete_edge, delete_edges, delete_vertex, and delete_vertices.  How about we consolidate these into one function, "delete", that looks like this:

delete(vertices=list_of_vertices, edges=list_of_edges) deletes the vertices specified, then the edges specified.

So:

* delete_vertex(v) == delete(vertices=[v])

* delete_vertices(list) == delete(vertices=list)

* delete_edge(e) == delete(edges=[e])

* delete_edges(list) == delete(edges=list)

* deleting vertices and edges is accomplished by passing both parameters in.

This idea may be completely irrational, but I thought I'd throw it out in an effort to consolidate functions and make the interface simpler to remember.  What do you think?

(I'm ignoring delete_multiedge here, though we could probably include that in as an option to delete).


Issue created by migration from https://trac.sagemath.org/ticket/1099





---

archive/issue_comments_006641.json:
```json
{
    "body": "Changing assignee from mhansen to rlm.",
    "created_at": "2007-12-17T15:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6641",
    "user": "rlm"
}
```

Changing assignee from mhansen to rlm.



---

archive/issue_comments_006642.json:
```json
{
    "body": "Changing component from combinatorics to graph theory.",
    "created_at": "2007-12-17T15:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6642",
    "user": "rlm"
}
```

Changing component from combinatorics to graph theory.



---

archive/issue_comments_006643.json:
```json
{
    "body": "Changing keywords from \"graphs\" to \"\".",
    "created_at": "2007-12-17T15:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6643",
    "user": "rlm"
}
```

Changing keywords from "graphs" to "".



---

archive/issue_comments_006644.json:
```json
{
    "body": "Attachment [delete.patch](tarball://root/attachments/some-uuid/ticket1099/delete.patch) by rlm created at 2008-01-27 03:11:02\n\nDefines the delete function, but does not remove any other functions",
    "created_at": "2008-01-27T03:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6644",
    "user": "rlm"
}
```

Attachment [delete.patch](tarball://root/attachments/some-uuid/ticket1099/delete.patch) by rlm created at 2008-01-27 03:11:02

Defines the delete function, but does not remove any other functions



---

archive/issue_comments_006645.json:
```json
{
    "body": "We still need to figure out what to do with delete_multiedge (perhaps just keep it). Also, is there any loss of functionality going from the other functions to this one?",
    "created_at": "2008-01-27T03:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6645",
    "user": "rlm"
}
```

We still need to figure out what to do with delete_multiedge (perhaps just keep it). Also, is there any loss of functionality going from the other functions to this one?



---

archive/issue_comments_006646.json:
```json
{
    "body": "Also note the somewhat arbitrary choice to support delete(edges=e) and delete(vertices=v) for vertex v and edge e. Should this stay?",
    "created_at": "2008-01-27T03:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6646",
    "user": "rlm"
}
```

Also note the somewhat arbitrary choice to support delete(edges=e) and delete(vertices=v) for vertex v and edge e. Should this stay?



---

archive/issue_comments_006647.json:
```json
{
    "body": "I support removing all other delete methods -- tab completion on a graph produces a formidable list, and having a bunch of redundant functions adds to the clutter.  That said, there are some strange things about this patch that I could do without:\n\n\n```\nG.delete(1)       #deletes a node\nG.delete(1,2)     #deletes an edge\nG.delete(1,2,3)   #deletes three nodes\nG.delete(1,2,3,4) #deletes four nodes\n```\n\n\none of these is not like the other... maybe you could balance it out, so if they pass in an even number of arguments, it removes the edges between successive pairs; odd number of arguments deletes nodes?",
    "created_at": "2008-01-28T15:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6647",
    "user": "boothby"
}
```

I support removing all other delete methods -- tab completion on a graph produces a formidable list, and having a bunch of redundant functions adds to the clutter.  That said, there are some strange things about this patch that I could do without:


```
G.delete(1)       #deletes a node
G.delete(1,2)     #deletes an edge
G.delete(1,2,3)   #deletes three nodes
G.delete(1,2,3,4) #deletes four nodes
```


one of these is not like the other... maybe you could balance it out, so if they pass in an even number of arguments, it removes the edges between successive pairs; odd number of arguments deletes nodes?



---

archive/issue_comments_006648.json:
```json
{
    "body": "I propose the following:\n\n1. Add an option, `multiple_edges`, to `delete()`, which is a boolean. If True, for every edge given, it deletes all edges on those vertices.\n2. Make it so that `delete(arg)` deletes vertex `arg`, or fails silently if it is not there. Make it so that `delete(arg1, arg2)` deletes the edge `(arg1, arg2)` if it is there, or fails silently if it is not there. Due to edges being 3-tuples (two vertices and a label), also make it so that `delete(arg1, arg2, arg3)` deletes the edge `(arg1, arg2, arg3)` if it is there, or fails silently if it is not.\n3. Make it so that calling `delete` with more than 3 arguments is not supported.\n4. Make it so that only iterable containers can be passed in for `delete(vertices=[v])` and `delete(edges=[e])`, so that `delete(edges=e)` and `delete(vertices=v)` is also not supported.",
    "created_at": "2008-01-28T17:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6648",
    "user": "rlm"
}
```

I propose the following:

1. Add an option, `multiple_edges`, to `delete()`, which is a boolean. If True, for every edge given, it deletes all edges on those vertices.
2. Make it so that `delete(arg)` deletes vertex `arg`, or fails silently if it is not there. Make it so that `delete(arg1, arg2)` deletes the edge `(arg1, arg2)` if it is there, or fails silently if it is not there. Due to edges being 3-tuples (two vertices and a label), also make it so that `delete(arg1, arg2, arg3)` deletes the edge `(arg1, arg2, arg3)` if it is there, or fails silently if it is not.
3. Make it so that calling `delete` with more than 3 arguments is not supported.
4. Make it so that only iterable containers can be passed in for `delete(vertices=[v])` and `delete(edges=[e])`, so that `delete(edges=e)` and `delete(vertices=v)` is also not supported.



---

archive/issue_comments_006649.json:
```json
{
    "body": "Attachment [delete-2.patch](tarball://root/attachments/some-uuid/ticket1099/delete-2.patch) by rlm created at 2008-01-28 19:08:56\n\nOn top of delete.patch",
    "created_at": "2008-01-28T19:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6649",
    "user": "rlm"
}
```

Attachment [delete-2.patch](tarball://root/attachments/some-uuid/ticket1099/delete-2.patch) by rlm created at 2008-01-28 19:08:56

On top of delete.patch



---

archive/issue_comments_006650.json:
```json
{
    "body": "Attachment [delete-3.patch](tarball://root/attachments/some-uuid/ticket1099/delete-3.patch) by rlm created at 2008-01-28 19:09:34\n\nOn top of delete-2.patch",
    "created_at": "2008-01-28T19:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6650",
    "user": "rlm"
}
```

Attachment [delete-3.patch](tarball://root/attachments/some-uuid/ticket1099/delete-3.patch) by rlm created at 2008-01-28 19:09:34

On top of delete-2.patch



---

archive/issue_comments_006651.json:
```json
{
    "body": "Attachment [delete-4.patch](tarball://root/attachments/some-uuid/ticket1099/delete-4.patch) by jason created at 2008-01-28 20:59:36\n\non top of delete-3.patch",
    "created_at": "2008-01-28T20:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6651",
    "user": "jason"
}
```

Attachment [delete-4.patch](tarball://root/attachments/some-uuid/ticket1099/delete-4.patch) by jason created at 2008-01-28 20:59:36

on top of delete-3.patch



---

archive/issue_comments_006652.json:
```json
{
    "body": "delete-4.patch should be applied on top of delete-3.patch.  It adds the following:\n\n1. extends the syntax so that delete((u,v)) or delete((u,v,label)) deletes an edge; this is so that we can do something like for e in g.edges(): g.delete(e)\n\n2. enhances the doctests for delete and also adds a doctest in another function that should have shown errors from the change we've made.\n\n3. Fix the errors from calling the old functions.  Robert, can you specifically look at the change in graph_generators?",
    "created_at": "2008-01-28T21:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6652",
    "user": "jason"
}
```

delete-4.patch should be applied on top of delete-3.patch.  It adds the following:

1. extends the syntax so that delete((u,v)) or delete((u,v,label)) deletes an edge; this is so that we can do something like for e in g.edges(): g.delete(e)

2. enhances the doctests for delete and also adds a doctest in another function that should have shown errors from the change we've made.

3. Fix the errors from calling the old functions.  Robert, can you specifically look at the change in graph_generators?



---

archive/issue_comments_006653.json:
```json
{
    "body": "I've run out of time today to work on this, but rlm and I agree that we should consolidate to two functions: delete_vertices and delete_edges, with a single non-list argument deleting a single vertex or edge.\n\nThat patch should be much simpler and should make much more sense in the long run.",
    "created_at": "2008-01-28T21:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6653",
    "user": "jason"
}
```

I've run out of time today to work on this, but rlm and I agree that we should consolidate to two functions: delete_vertices and delete_edges, with a single non-list argument deleting a single vertex or edge.

That patch should be much simpler and should make much more sense in the long run.



---

archive/issue_comments_006654.json:
```json
{
    "body": "> with a single non-list argument deleting a single vertex or edge.\n\nTo clarify, if there is only one argument, and it is either a list or of type types.GeneratorType...",
    "created_at": "2008-01-29T00:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6654",
    "user": "rlm"
}
```

> with a single non-list argument deleting a single vertex or edge.

To clarify, if there is only one argument, and it is either a list or of type types.GeneratorType...



---

archive/issue_comments_006655.json:
```json
{
    "body": "What is the status of this ticket? I am afraid this code has/will bitrot.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-08T15:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6655",
    "user": "mabshoff"
}
```

What is the status of this ticket? I am afraid this code has/will bitrot.

Cheers,

Michael



---

archive/issue_comments_006656.json:
```json
{
    "body": "None of the patches for this ticket are or ever were quite ready. I also have to say that I still disagree with the ticket in general. It is much simpler to specify what you are deleting (especially if you happen to do a lot of actual coding with graphs, like me!).",
    "created_at": "2008-04-09T13:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6656",
    "user": "rlm"
}
```

None of the patches for this ticket are or ever were quite ready. I also have to say that I still disagree with the ticket in general. It is much simpler to specify what you are deleting (especially if you happen to do a lot of actual coding with graphs, like me!).



---

archive/issue_comments_006657.json:
```json
{
    "body": "Jason,\n\nwhat is the status of this work? It this something you are working on? Did those patches rot in the meantime?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-13T02:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6657",
    "user": "mabshoff"
}
```

Jason,

what is the status of this work? It this something you are working on? Did those patches rot in the meantime?

Cheers,

Michael



---

archive/issue_comments_006658.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-08-30T21:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1099#issuecomment-6658",
    "user": "rlm"
}
```

Resolution: wontfix
