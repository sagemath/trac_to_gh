# Issue 8744: Improve add_edge in BipartiteGraph to make it independent from the current coloring

archive/issues_008744.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @rhinton brunellus\n\nThe current add_edge method in BipartiteGraph refuses to add an edge between two vertices belonging to the same set. This may seem perfectly fine, but when the two vertices are in distinct connected components, the graph may stay bipartite with a new edge even if the vertices are in the same partition :\n\n\n```\nsage: g = BipartiteGraph(2*graphs.GridGraph([4,4]))\nsage: g.add_edge(0,30)\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/usr/local/sage/devel/sage-bip/sage/graphs/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.pyc in add_edge(self, u, v, label)\n    690         # check for endpoints in different partitions\n    691         if self.left.issuperset((u,v)) or self.right.issuperset((u,v)):\n--> 692             raise RuntimeError('Edge vertices must lie in different partitions.')\n    693 \n    694         # add the edge\n\nRuntimeError: Edge vertices must lie in different partitions.\n```\n\n\nFrom the discussion on #8425 :\n\n//////\nTo be honest, I really would like to be able to deal with Bipartite Graphs without having to specify myself in which set my vertices are... What would you think of setting a vertex to \"left\" if the users does not specify left=True or right=True, and modify a bit add_edge ? This way, the edge could be added immediately if the two vertices at its ends are in different sets, and if they are not the colors could be changed whenever possible to fit the graph with a new edge ?\n\nActually, when a graph is bipartite and split in two sets, you can add an edge in exactly two situations :\n\n- The colors between the endpoints are different\n\n- The colors are the same, but the vertices belong to two different connected components\n\nSo two solutions :\n\n- Add an edge if the colors are different. If they are not, check that there is no path from one vertex to the other, and if it is the case reverse the coloring of one of the two components and add the edge\n\n- Fix a partition for any connected component, and maintain them updated.\n\nThe problem is that the first makes of add_edge a linear-time function. The second way keeps it to O(1), but we would have to update the list of connected components, even if it is not so hard. The truth is I do not know what is best for this class, and I'm eager to learn your advice on it. It is also possible to add a flag like \"allow_set_modifications\" if you want to keep the possibility to refuse an addition in somec ases... But anyway this should be mentionned in the docstrings :-) \n///////\n\nIf anybody working on the BipartiteGraph class is willing to give all this a try.... :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8744\n\n",
    "created_at": "2010-04-22T08:14:52Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "Improve add_edge in BipartiteGraph to make it independent from the current coloring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8744",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  @rhinton brunellus

The current add_edge method in BipartiteGraph refuses to add an edge between two vertices belonging to the same set. This may seem perfectly fine, but when the two vertices are in distinct connected components, the graph may stay bipartite with a new edge even if the vertices are in the same partition :


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


From the discussion on #8425 :

//////
To be honest, I really would like to be able to deal with Bipartite Graphs without having to specify myself in which set my vertices are... What would you think of setting a vertex to "left" if the users does not specify left=True or right=True, and modify a bit add_edge ? This way, the edge could be added immediately if the two vertices at its ends are in different sets, and if they are not the colors could be changed whenever possible to fit the graph with a new edge ?

Actually, when a graph is bipartite and split in two sets, you can add an edge in exactly two situations :

- The colors between the endpoints are different

- The colors are the same, but the vertices belong to two different connected components

So two solutions :

- Add an edge if the colors are different. If they are not, check that there is no path from one vertex to the other, and if it is the case reverse the coloring of one of the two components and add the edge

- Fix a partition for any connected component, and maintain them updated.

The problem is that the first makes of add_edge a linear-time function. The second way keeps it to O(1), but we would have to update the list of connected components, even if it is not so hard. The truth is I do not know what is best for this class, and I'm eager to learn your advice on it. It is also possible to add a flag like "allow_set_modifications" if you want to keep the possibility to refuse an addition in somec ases... But anyway this should be mentionned in the docstrings :-) 
///////

If anybody working on the BipartiteGraph class is willing to give all this a try.... :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8744





---

archive/issue_events_021248.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8744#event-21248"
}
```



---

archive/issue_events_021249.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8744#event-21249"
}
```



---

archive/issue_events_021250.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8744#event-21250"
}
```



---

archive/issue_events_021251.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8744#event-21251"
}
```



---

archive/issue_events_021252.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8744#event-21252"
}
```



---

archive/issue_events_021253.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8744#event-21253"
}
```



---

archive/issue_events_021254.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8744#event-21254"
}
```



---

archive/issue_comments_079868.json:
```json
{
    "body": "I just tested this out using the example in the description. It worked without any error message. So it's safe to say this has been fixed?",
    "created_at": "2022-03-11T16:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79868",
    "user": "https://github.com/enjeck"
}
```

I just tested this out using the example in the description. It worked without any error message. So it's safe to say this has been fixed?



---

archive/issue_comments_079869.json:
```json
{
    "body": "Not fully as this ticket raises the question of the addition of edges between vertices lying in different connected components.\n\nSo far, the order in which edges are added matters.\n\n```\nsage: g = BipartiteGraph()\nsage: g.add_edges([(0, 1), (1, 2), (2, 3)])\nsage: g = BipartiteGraph()\nsage: g.add_edges([(0, 1), (3, 2), (1, 2)])\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n<ipython-input-23-fa0c70b30e4b> in <module>\n----> 1 g.add_edges([(Integer(0), Integer(1)), (Integer(3), Integer(2)), (Integer(1), Integer(2))])\n\n~/sage/local/var/lib/sage/venv-python3.9/lib/python3.9/site-packages/sage/graphs/bipartite_graph.py in add_edges(self, edges, loops)\n    931             # check for endpoints in different partitions\n    932             if self.left.issuperset((u, v)) or self.right.issuperset((u, v)):\n--> 933                 raise RuntimeError(\"edge vertices must lie in different partitions\")\n    934 \n    935             # automatically decide partitions for the newly created vertices\n\nRuntimeError: edge vertices must lie in different partitions\n```\n\nI have no opinion on the best solution. Regular users of this class should clarify expected behavior.",
    "created_at": "2022-03-12T10:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79869",
    "user": "https://github.com/dcoudert"
}
```

Not fully as this ticket raises the question of the addition of edges between vertices lying in different connected components.

So far, the order in which edges are added matters.

```
sage: g = BipartiteGraph()
sage: g.add_edges([(0, 1), (1, 2), (2, 3)])
sage: g = BipartiteGraph()
sage: g.add_edges([(0, 1), (3, 2), (1, 2)])
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
<ipython-input-23-fa0c70b30e4b> in <module>
----> 1 g.add_edges([(Integer(0), Integer(1)), (Integer(3), Integer(2)), (Integer(1), Integer(2))])

~/sage/local/var/lib/sage/venv-python3.9/lib/python3.9/site-packages/sage/graphs/bipartite_graph.py in add_edges(self, edges, loops)
    931             # check for endpoints in different partitions
    932             if self.left.issuperset((u, v)) or self.right.issuperset((u, v)):
--> 933                 raise RuntimeError("edge vertices must lie in different partitions")
    934 
    935             # automatically decide partitions for the newly created vertices

RuntimeError: edge vertices must lie in different partitions
```

I have no opinion on the best solution. Regular users of this class should clarify expected behavior.



---

archive/issue_events_021255.json:
```json
{
    "actor": "https://github.com/dcoudert",
    "created_at": "2022-04-22T15:26:30Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8744#event-21255"
}
```



---

archive/issue_events_021256.json:
```json
{
    "actor": "https://github.com/dcoudert",
    "created_at": "2022-04-22T15:26:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "milestone": "sage-9.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8744#event-21256"
}
```



---

archive/issue_comments_079870.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2022-04-22T15:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79870",
    "user": "https://github.com/dcoudert"
}
```

Changing status from new to needs_info.



---

archive/issue_events_021257.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-09-19T18:58:47Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "milestone": "sage-9.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8744#event-21257"
}
```



---

archive/issue_events_021258.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-09-19T18:58:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "milestone": "sage-9.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8744#event-21258"
}
```



---

archive/issue_comments_079871.json:
```json
{
    "body": "Made a start on this ticket. Seeing as there is already an inherited .connected_components() method, that calculates them on the fly (rather than maintaining an invariant), I'm using that.",
    "created_at": "2022-11-17T16:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79871",
    "user": "https://github.com/Bruno-TT"
}
```

Made a start on this ticket. Seeing as there is already an inherited .connected_components() method, that calculates them on the fly (rather than maintaining an invariant), I'm using that.



---

archive/issue_comments_079872.json:
```json
{
    "body": "You should use `self.connected_component_containing_vertex(v, sort=False)`.\n\nFor coding style, prefer `old_left = frozenset(self.left)` with spaces around `=`.\n----\nNew commits:",
    "created_at": "2022-11-17T16:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79872",
    "user": "https://github.com/dcoudert"
}
```

You should use `self.connected_component_containing_vertex(v, sort=False)`.

For coding style, prefer `old_left = frozenset(self.left)` with spaces around `=`.
----
New commits:



---

archive/issue_comments_079873.json:
```json
{
    "body": "Replying to [comment:12 David Coudert]:\n> You should use `self.connected_component_containing_vertex(v, sort=False)`.\nGood spot, thanks!\n\n> For coding style, prefer `old_left = frozenset(self.left)` with spaces around `=`.\nThanks, will do this tomorrow.\n----\nNew commits:",
    "created_at": "2022-11-18T19:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79873",
    "user": "https://github.com/Bruno-TT"
}
```

Replying to [comment:12 David Coudert]:
> You should use `self.connected_component_containing_vertex(v, sort=False)`.
Good spot, thanks!

> For coding style, prefer `old_left = frozenset(self.left)` with spaces around `=`.
Thanks, will do this tomorrow.
----
New commits:



---

archive/issue_comments_079874.json:
```json
{
    "body": "`add_edge`:\n* you don't need to save current left/right\n* the warning is not necessary (we usually don't do that). The behavior of the method should be well documented. \n\nThere is something wrong in the proposed behavior for `add_edges`, and it's true that other `add_edges` methods in the graph module must also be corrected (in other tickets). The issue is that we modify the graph before raising an error. It would be much better to first check if it is possible to add all edges and then to actually add them and update the partition accordingly or raise an error without modifying the graph.",
    "created_at": "2022-11-19T08:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79874",
    "user": "https://github.com/dcoudert"
}
```

`add_edge`:
* you don't need to save current left/right
* the warning is not necessary (we usually don't do that). The behavior of the method should be well documented. 

There is something wrong in the proposed behavior for `add_edges`, and it's true that other `add_edges` methods in the graph module must also be corrected (in other tickets). The issue is that we modify the graph before raising an error. It would be much better to first check if it is possible to add all edges and then to actually add them and update the partition accordingly or raise an error without modifying the graph.



---

archive/issue_comments_079875.json:
```json
{
    "body": "Replying to [comment:14 David Coudert]:\n> `add_edge`:\n> * you don't need to save current left/right\nThanks, good spot - removed it.\n\n> * the warning is not necessary (we usually don't do that). The behavior of the method should be well documented. \nCool, I've removed the warning and updated the tests + documentation.\n\n> There is something wrong in the proposed behavior for `add_edges`, and it's true that other `add_edges` methods in the graph module must also be corrected (in other tickets). The issue is that we modify the graph before raising an error. It would be much better to first check if it is possible to add all edges and then to actually add them and update the partition accordingly or raise an error without modifying the graph.\nGood idea, I didn't think of that. I'll try and implement an algorithm now.",
    "created_at": "2022-11-22T14:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79875",
    "user": "https://github.com/Bruno-TT"
}
```

Replying to [comment:14 David Coudert]:
> `add_edge`:
> * you don't need to save current left/right
Thanks, good spot - removed it.

> * the warning is not necessary (we usually don't do that). The behavior of the method should be well documented. 
Cool, I've removed the warning and updated the tests + documentation.

> There is something wrong in the proposed behavior for `add_edges`, and it's true that other `add_edges` methods in the graph module must also be corrected (in other tickets). The issue is that we modify the graph before raising an error. It would be much better to first check if it is possible to add all edges and then to actually add them and update the partition accordingly or raise an error without modifying the graph.
Good idea, I didn't think of that. I'll try and implement an algorithm now.



---

archive/issue_comments_079876.json:
```json
{
    "body": "Update: I've implemented the algorithm to check whether adding a set of edges is possible\n----\nNew commits:",
    "created_at": "2022-11-24T17:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79876",
    "user": "https://github.com/Bruno-TT"
}
```

Update: I've implemented the algorithm to check whether adding a set of edges is possible
----
New commits:



---

archive/issue_comments_079877.json:
```json
{
    "body": "I moved the branch to public and pushed a review ticket (easier than explaining all the details). Let me know if you agree. \n----\nNew commits:",
    "created_at": "2022-11-26T15:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79877",
    "user": "https://github.com/dcoudert"
}
```

I moved the branch to public and pushed a review ticket (easier than explaining all the details). Let me know if you agree. 
----
New commits:



---

archive/issue_comments_079878.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2022-11-26T15:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79878",
    "user": "https://github.com/dcoudert"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_079879.json:
```json
{
    "body": "Why have you added the statement `# autopep8: off` ?",
    "created_at": "2022-11-26T15:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79879",
    "user": "https://github.com/dcoudert"
}
```

Why have you added the statement `# autopep8: off` ?



---

archive/issue_comments_079880.json:
```json
{
    "body": "Replying to [comment:17 David Coudert]:\n> I moved the branch to public and pushed a review ticket (easier than explaining all the details). Let me know if you agree. \nAssuming this is a typo and you mean review commit? If not then I can't find the ticket \n\n> ||[3dfe5fb](https://git.sagemath.org/sage.git/commit?id=3dfe5fbbf3f1d7cb8da10887e19e69abbb11bce0)||`trac #8744: review commit`||\n\nI don't quite understand why you've chosen to remove the\n\n\n```\nreturn set(left), set(right), vertex_in_left\n...\nself.left, self.right, vertex_in_left = b\n```\n\n\nand replace it with \n\n\n\n```\nreturn vertex_in_left\n...\n# If we get here, then we've found a valid bipartition.\n        # We update the bipartition\n        self.left.clear()\n        self.right.clear()\n        for v in vertex_in_left:\n            if vertex_in_left[v]:\n                self.left.add(v)\n            else:\n                self.right.add(v)\n```\n\n\nI understand that vertex_in_left contains all the info needed to reconstruct the sets, but surely it's more efficient to just return the set objects and replace the references inside the graph, rather than adding another loop to reconstruct them?\n\nOther than that, I like all the changes you made. It was a good idea having one edges_to_add list instead of us,vs,labels.",
    "created_at": "2022-12-10T14:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79880",
    "user": "https://github.com/Bruno-TT"
}
```

Replying to [comment:17 David Coudert]:
> I moved the branch to public and pushed a review ticket (easier than explaining all the details). Let me know if you agree. 
Assuming this is a typo and you mean review commit? If not then I can't find the ticket 

> ||[3dfe5fb](https://git.sagemath.org/sage.git/commit?id=3dfe5fbbf3f1d7cb8da10887e19e69abbb11bce0)||`trac #8744: review commit`||

I don't quite understand why you've chosen to remove the


```
return set(left), set(right), vertex_in_left
...
self.left, self.right, vertex_in_left = b
```


and replace it with 



```
return vertex_in_left
...
# If we get here, then we've found a valid bipartition.
        # We update the bipartition
        self.left.clear()
        self.right.clear()
        for v in vertex_in_left:
            if vertex_in_left[v]:
                self.left.add(v)
            else:
                self.right.add(v)
```


I understand that vertex_in_left contains all the info needed to reconstruct the sets, but surely it's more efficient to just return the set objects and replace the references inside the graph, rather than adding another loop to reconstruct them?

Other than that, I like all the changes you made. It was a good idea having one edges_to_add list instead of us,vs,labels.



---

archive/issue_comments_079881.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-12-10T16:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79881",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079882.json:
```json
{
    "body": "The reason for not returning `set(left), set(right), vertex_in_left` is simply that we don't maintain `left` and `right` anymore in `_check_bipartition_for_add_edges`. So we have to rebuild `left` and `right`.",
    "created_at": "2022-12-10T16:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8744#issuecomment-79882",
    "user": "https://github.com/dcoudert"
}
```

The reason for not returning `set(left), set(right), vertex_in_left` is simply that we don't maintain `left` and `right` anymore in `_check_bipartition_for_add_edges`. So we have to rebuild `left` and `right`.
