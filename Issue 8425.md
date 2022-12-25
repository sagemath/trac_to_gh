# Issue 8425: BipartiteGraph add_edge allows bipartite property to be violated.

archive/issues_008425.json:
```json
{
    "body": "Assignee: @rhinton\n\nCC:  @rlmill @jasongrout @nathanncohen\n\nKeywords: BipartiteGraph, add_edge\n\nadd_edge() needs to be overridden in BipartiteGraph in order to preserve the bipartite property of the graph.\n\n```\nsage: # non-bipartite graphs are rejected by the constructor\nsage: BipartiteGraph(Graph({0:[1,2], 1:[2]}))\nTraceback (most recent call last)\n...\nTypeError: Input graph is not bipartite!\n\nsage: # but the same graph can be constructed edge-by-edge without raising an error\nsage: bg = BipartiteGraph()\nsage: bg.add_vertices([0,1,2], left=[True,False,True])\nsage: bg.add_edges([(0,1), (1,2)])  # good so far\nsage: bg.add_edge(2,0)  # should raise exception!\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8425\n\n",
    "created_at": "2010-03-03T01:35:07Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "BipartiteGraph add_edge allows bipartite property to be violated.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8425",
    "user": "https://github.com/rhinton"
}
```
Assignee: @rhinton

CC:  @rlmill @jasongrout @nathanncohen

Keywords: BipartiteGraph, add_edge

add_edge() needs to be overridden in BipartiteGraph in order to preserve the bipartite property of the graph.

```
sage: # non-bipartite graphs are rejected by the constructor
sage: BipartiteGraph(Graph({0:[1,2], 1:[2]}))
Traceback (most recent call last)
...
TypeError: Input graph is not bipartite!

sage: # but the same graph can be constructed edge-by-edge without raising an error
sage: bg = BipartiteGraph()
sage: bg.add_vertices([0,1,2], left=[True,False,True])
sage: bg.add_edges([(0,1), (1,2)])  # good so far
sage: bg.add_edge(2,0)  # should raise exception!
```


Issue created by migration from https://trac.sagemath.org/ticket/8425





---

archive/issue_comments_075402.json:
```json
{
    "body": "One of the \"core\" routines to overload from #1941.",
    "created_at": "2010-03-03T01:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75402",
    "user": "https://github.com/rhinton"
}
```

One of the "core" routines to overload from #1941.



---

archive/issue_comments_075403.json:
```json
{
    "body": "Patch applied after other patches in this order:\n\napplying trac_8331-bipartite-dict-initializer.patch\napplying trac_8329-bipartite-graph-copy.patch\napplying trac_8421-bipartite-partition-sets.patch\napplying trac_8330-bipartite-delete-vertex.patch\napplying trac_8425-bipartite-add-edge.patch\n\nTheir functionality is more-or-less mutually exclusive, but they all add functions to about the same place in bipartite_graph.py.",
    "created_at": "2010-03-04T22:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75403",
    "user": "https://github.com/rhinton"
}
```

Patch applied after other patches in this order:

applying trac_8331-bipartite-dict-initializer.patch
applying trac_8329-bipartite-graph-copy.patch
applying trac_8421-bipartite-partition-sets.patch
applying trac_8330-bipartite-delete-vertex.patch
applying trac_8425-bipartite-add-edge.patch

Their functionality is more-or-less mutually exclusive, but they all add functions to about the same place in bipartite_graph.py.



---

archive/issue_comments_075404.json:
```json
{
    "body": "Attachment [trac_8425-bipartite-add-edge.patch](tarball://root/attachments/some-uuid/ticket8425/trac_8425-bipartite-add-edge.patch) by @rhinton created at 2010-03-05 02:04:36\n\napply after #8331, #8329, and #8421",
    "created_at": "2010-03-05T02:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75404",
    "user": "https://github.com/rhinton"
}
```

Attachment [trac_8425-bipartite-add-edge.patch](tarball://root/attachments/some-uuid/ticket8425/trac_8425-bipartite-add-edge.patch) by @rhinton created at 2010-03-05 02:04:36

apply after #8331, #8329, and #8421



---

archive/issue_comments_075405.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-05T02:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75405",
    "user": "https://github.com/rhinton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075406.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-06T22:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75406",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075407.json:
```json
{
    "body": "Hunk failures applying to Sage-4.3.4.alpha0 + #8329 + #8421. Please rebase.",
    "created_at": "2010-03-06T22:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75407",
    "user": "https://github.com/rlmill"
}
```

Hunk failures applying to Sage-4.3.4.alpha0 + #8329 + #8421. Please rebase.



---

archive/issue_comments_075408.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-24T18:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75408",
    "user": "https://github.com/rhinton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075409.json:
```json
{
    "body": "Sorry for the delay and mixup.\n\nREQUIRES: #8421 + #8329 + #8330\n\nI don't know how to change the \"patch\" section above to reflect this....",
    "created_at": "2010-03-24T18:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75409",
    "user": "https://github.com/rhinton"
}
```

Sorry for the delay and mixup.

REQUIRES: #8421 + #8329 + #8330

I don't know how to change the "patch" section above to reflect this....



---

archive/issue_comments_075410.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-01T13:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75410",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075411.json:
```json
{
    "body": "Hello !!!\n\nI have to admit I do not really like this one :-/\n\nI seldom work on this BipartiteGraph class, and I understand you usally know which are your left and right sets, but I have to admit I would not want to see an error raised when I am building a valid bipartite graph, without taking care of the sets myself. For example :\n\n\n```\nsage: g = BipartiteGraph(2*graphs.GridGraph([4,4]))\nsage: g.add_edge(0,30)\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/usr/local/sage/devel/sage-bip/sage/graphs/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.pyc in add_edge(self, u, v, label)\n    690         # check for endpoints in different partitions\n    691         if self.left.issuperset((u,v)) or self.right.issuperset((u,v)):\n--> 692             raise RuntimeError('Edge vertices must lie in different partitions.')\n    693 \n    694         # add the edge\n\nRuntimeError: Edge vertices must lie in different partitions.\n```\n\n\nAnd to be honest, I really would like to be able to deal with Bipartite Graphs without having to specify myself in which set my vertices are... What would you think of setting a vertex to \"left\" if the users does not specify left=True or right=True, and modify a bit add_edge ? This way, the edge could be added immediately if the two vertices at its ends are in different sets, and if they are not the colors could be changed whenever possible to fit the graph with a new edge ?\n\nActually, when a graph is bipartite and split in two sets, you can add an edge in exactly two situations : \n\n- The colors between the endpoints are different\n\n- The colors are the same, but the vertices belong to two different connected components\n\nSo two solutions : \n\n- Add an edge if the colors are different. If they are not, check that there is no path from one vertex to the other, and if it is the case reverse the coloring of one of the two components and add the edge\n\n- Fix a partition for any connected component, and maintain them updated. \n\n\nThe problem is that the first makes of add_edge a linear-time function. The second way keeps it to O(1), but we would have to update the list of connected components, even if it is not so hard. The truth is I do not know what is best for this class, and I'm eager to learn your advice on it. It is also possible to add a flag like \"allow_set_modifications\" if you want to keep the possibility to refuse an addition in somec ases... But anyway this should be mentionned in the docstrings :-)\n\nNathann",
    "created_at": "2010-04-01T13:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75411",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!!

I have to admit I do not really like this one :-/

I seldom work on this BipartiteGraph class, and I understand you usally know which are your left and right sets, but I have to admit I would not want to see an error raised when I am building a valid bipartite graph, without taking care of the sets myself. For example :


```
sage: g = BipartiteGraph(2*graphs.GridGraph([4,4]))
sage: g.add_edge(0,30)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/usr/local/sage/devel/sage-bip/sage/graphs/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.pyc in add_edge(self, u, v, label)
    690         # check for endpoints in different partitions
    691         if self.left.issuperset((u,v)) or self.right.issuperset((u,v)):
--> 692             raise RuntimeError('Edge vertices must lie in different partitions.')
    693 
    694         # add the edge

RuntimeError: Edge vertices must lie in different partitions.
```


And to be honest, I really would like to be able to deal with Bipartite Graphs without having to specify myself in which set my vertices are... What would you think of setting a vertex to "left" if the users does not specify left=True or right=True, and modify a bit add_edge ? This way, the edge could be added immediately if the two vertices at its ends are in different sets, and if they are not the colors could be changed whenever possible to fit the graph with a new edge ?

Actually, when a graph is bipartite and split in two sets, you can add an edge in exactly two situations : 

- The colors between the endpoints are different

- The colors are the same, but the vertices belong to two different connected components

So two solutions : 

- Add an edge if the colors are different. If they are not, check that there is no path from one vertex to the other, and if it is the case reverse the coloring of one of the two components and add the edge

- Fix a partition for any connected component, and maintain them updated. 


The problem is that the first makes of add_edge a linear-time function. The second way keeps it to O(1), but we would have to update the list of connected components, even if it is not so hard. The truth is I do not know what is best for this class, and I'm eager to learn your advice on it. It is also possible to add a flag like "allow_set_modifications" if you want to keep the possibility to refuse an addition in somec ases... But anyway this should be mentionned in the docstrings :-)

Nathann



---

archive/issue_comments_075412.json:
```json
{
    "body": "Thanks for helping!  Sorry for the slow response: apparently trac decided to stop sending me email notifications.\n\nYour suggestions are good.  They would make BipartiteGraph much easier to work with.  Not that the current approach is invalid -- some people might take offense if their left/right sets started changing without permission.  Of course, we can always add a keyword flag to prevent set modification and essentially keep the current behavior.\n\nMy selfish suggestion is to allow this patch to go through because it fixes an important deficiency in BipartiteGraph.  Right now BG is broken.  This patch fixes it, although it doesn't handle the left/right sets automatically.  I would love to see an additional ticket to add this convenience.  (I'm happy to review it!)  In particular, this handling would make the left/right keywords for add_vertex optional and obviate some of the dirty tricks I played during BipartiteGraph initialization.\n\nThe docstring test shows that an exception is raised.  Would you like me to add verbiage above saying that it is an error for the two endpoints to be in the same partition?",
    "created_at": "2010-04-22T01:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75412",
    "user": "https://github.com/rhinton"
}
```

Thanks for helping!  Sorry for the slow response: apparently trac decided to stop sending me email notifications.

Your suggestions are good.  They would make BipartiteGraph much easier to work with.  Not that the current approach is invalid -- some people might take offense if their left/right sets started changing without permission.  Of course, we can always add a keyword flag to prevent set modification and essentially keep the current behavior.

My selfish suggestion is to allow this patch to go through because it fixes an important deficiency in BipartiteGraph.  Right now BG is broken.  This patch fixes it, although it doesn't handle the left/right sets automatically.  I would love to see an additional ticket to add this convenience.  (I'm happy to review it!)  In particular, this handling would make the left/right keywords for add_vertex optional and obviate some of the dirty tricks I played during BipartiteGraph initialization.

The docstring test shows that an exception is raised.  Would you like me to add verbiage above saying that it is an error for the two endpoints to be in the same partition?



---

archive/issue_comments_075413.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-22T08:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75413",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075414.json:
```json
{
    "body": "> The docstring test shows that an exception is raised.  Would you like me to add verbiage above saying that it is an error for the two endpoints to be in the same partition?\n\nWell, it is already the case, as the Exception raised is \"RuntimeError: Edge vertices must lie in different partitions\". Well, I can understand you would like to have a *functional* BipartiteGraph as soon as possible, so I'm giving this ticket a positive review !\n\nThe tests pass, the documentation is fine, and it clearly is a necessary fix :-)\n\nNathann",
    "created_at": "2010-04-22T08:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75414",
    "user": "https://github.com/nathanncohen"
}
```

> The docstring test shows that an exception is raised.  Would you like me to add verbiage above saying that it is an error for the two endpoints to be in the same partition?

Well, it is already the case, as the Exception raised is "RuntimeError: Edge vertices must lie in different partitions". Well, I can understand you would like to have a *functional* BipartiteGraph as soon as possible, so I'm giving this ticket a positive review !

The tests pass, the documentation is fine, and it clearly is a necessary fix :-)

Nathann



---

archive/issue_comments_075415.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-22T08:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75415",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075416.json:
```json
{
    "body": "See #8744 for the previous comments :-)\n\nNathann",
    "created_at": "2010-04-22T08:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75416",
    "user": "https://github.com/nathanncohen"
}
```

See #8744 for the previous comments :-)

Nathann



---

archive/issue_comments_075417.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8425#issuecomment-75417",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
