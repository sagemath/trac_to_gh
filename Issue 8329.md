# Issue 8329: Missing copy() method in BipartiteGraph

archive/issues_008329.json:
```json
{
    "body": "Assignee: @rhinton\n\nCC:  @rlmill @jasongrout\n\nKeywords: BipartiteGraph\n\nBipartiteGraph is missing a copy() method.\n\n\n```\nsage: bg = BipartiteGraph(graphs.CycleGraph(4))\nsage: type(bg)\n<class 'sage.graphs.bipartite_graph.BipartiteGraph'>\nsage: bg2 = bg.copy()\nsage: type(bg2)\n<class 'sage.graphs.graph.Graph'>\n```\n\n\nThe result is not horrendous because the base Graph class has a copy() method.  But the result is unexpected: copy() a BipartiteGraph and you get a Graph?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8329\n\n",
    "created_at": "2010-02-22T19:51:40Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Missing copy() method in BipartiteGraph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8329",
    "user": "@rhinton"
}
```
Assignee: @rhinton

CC:  @rlmill @jasongrout

Keywords: BipartiteGraph

BipartiteGraph is missing a copy() method.


```
sage: bg = BipartiteGraph(graphs.CycleGraph(4))
sage: type(bg)
<class 'sage.graphs.bipartite_graph.BipartiteGraph'>
sage: bg2 = bg.copy()
sage: type(bg2)
<class 'sage.graphs.graph.Graph'>
```


The result is not horrendous because the base Graph class has a copy() method.  But the result is unexpected: copy() a BipartiteGraph and you get a Graph?


Issue created by migration from https://trac.sagemath.org/ticket/8329





---

archive/issue_comments_074146.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-22T20:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74146",
    "user": "@rhinton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074147.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-22T20:35:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74147",
    "user": "@rhinton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074148.json:
```json
{
    "body": "Oops, bug in doctest, the patch doesn't work at all.",
    "created_at": "2010-02-22T20:35:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74148",
    "user": "@rhinton"
}
```

Oops, bug in doctest, the patch doesn't work at all.



---

archive/issue_comments_074149.json:
```json
{
    "body": "New patch (replaced old) should work, including fixed doctest.",
    "created_at": "2010-02-22T20:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74149",
    "user": "@rhinton"
}
```

New patch (replaced old) should work, including fixed doctest.



---

archive/issue_comments_074150.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-22T20:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74150",
    "user": "@rhinton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074151.json:
```json
{
    "body": "This is item 9 on trac #1941.",
    "created_at": "2010-02-23T01:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74151",
    "user": "@rlmill"
}
```

This is item 9 on trac #1941.



---

archive/issue_comments_074152.json:
```json
{
    "body": "Right, I had forgotten about this.  Obviously I'm fixing methods as I need them.  I don't have time right now for the complete overhaul.  Is the piecemeal approach OK?  \n\nIncidentally, I think I have a decent approach for add_vertex.  I was planning on opening another ticket.... :-)",
    "created_at": "2010-02-23T01:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74152",
    "user": "@rhinton"
}
```

Right, I had forgotten about this.  Obviously I'm fixing methods as I need them.  I don't have time right now for the complete overhaul.  Is the piecemeal approach OK?  

Incidentally, I think I have a decent approach for add_vertex.  I was planning on opening another ticket.... :-)



---

archive/issue_comments_074153.json:
```json
{
    "body": "Replying to [comment:6 rhinton]:\n> Right, I had forgotten about this.  Obviously I'm fixing methods as I need them.  I don't have time right now for the complete overhaul.  Is the piecemeal approach OK?  \n\nI was just linking the tickets to each other. Adding edges to trac I guess... Any way you want to improve bipartite graphs I'll gladly review once I get the time, I just wanted to make sure you were aware of that ticket.\n\n> Incidentally, I think I have a decent approach for add_vertex.  I was planning on opening another ticket.... :-)\n\nGo for it!",
    "created_at": "2010-02-23T03:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74153",
    "user": "@rlmill"
}
```

Replying to [comment:6 rhinton]:
> Right, I had forgotten about this.  Obviously I'm fixing methods as I need them.  I don't have time right now for the complete overhaul.  Is the piecemeal approach OK?  

I was just linking the tickets to each other. Adding edges to trac I guess... Any way you want to improve bipartite graphs I'll gladly review once I get the time, I just wanted to make sure you were aware of that ticket.

> Incidentally, I think I have a decent approach for add_vertex.  I was planning on opening another ticket.... :-)

Go for it!



---

archive/issue_comments_074154.json:
```json
{
    "body": "Note for someone who is more knowledgeable: the new BipartiteGraph.copy() method doesn't try to do anything tricky with vertex associations, boundaries, positions, etc.  It just tries the Graph constructor.  I haven't figured out a way to copy() the Graph part and get out a BipartiteGraph instance.  This way works for me, but I'm not sure if it does all the special stuff that Graph.copy() does.",
    "created_at": "2010-02-24T01:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74154",
    "user": "@rhinton"
}
```

Note for someone who is more knowledgeable: the new BipartiteGraph.copy() method doesn't try to do anything tricky with vertex associations, boundaries, positions, etc.  It just tries the Graph constructor.  I haven't figured out a way to copy() the Graph part and get out a BipartiteGraph instance.  This way works for me, but I'm not sure if it does all the special stuff that Graph.copy() does.



---

archive/issue_comments_074155.json:
```json
{
    "body": "I get it ... adding edges. :-)\n\nReplying to [comment:7 rlm]:\n> Replying to [comment:6 rhinton]:\n> > Right, I had forgotten about this.  Obviously I'm fixing methods as I need them.  I don't have time right now for the complete overhaul.  Is the piecemeal approach OK?  \n> \n> I was just linking the tickets to each other. Adding edges to trac I guess... Any way you want to improve bipartite graphs I'll gladly review once I get the time, I just wanted to make sure you were aware of that ticket.",
    "created_at": "2010-02-24T21:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74155",
    "user": "@rhinton"
}
```

I get it ... adding edges. :-)

Replying to [comment:7 rlm]:
> Replying to [comment:6 rhinton]:
> > Right, I had forgotten about this.  Obviously I'm fixing methods as I need them.  I don't have time right now for the complete overhaul.  Is the piecemeal approach OK?  
> 
> I was just linking the tickets to each other. Adding edges to trac I guess... Any way you want to improve bipartite graphs I'll gladly review once I get the time, I just wanted to make sure you were aware of that ticket.



---

archive/issue_comments_074156.json:
```json
{
    "body": "Changing keywords from \"BipartiteGraph\" to \"BipartiteGraph, copy\".",
    "created_at": "2010-03-02T02:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74156",
    "user": "@rhinton"
}
```

Changing keywords from "BipartiteGraph" to "BipartiteGraph, copy".



---

archive/issue_comments_074157.json:
```json
{
    "body": "The new patch to GenericGraph.__copy__() always creates a new object of the same class as the original object -- no special case code for Graph, DiGraph, or BipartiteGraph.  Any future subclasses will work as well assuming they can handle the same initializer arguments (by passing them to the superclass initializer).",
    "created_at": "2010-03-02T02:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74157",
    "user": "@rhinton"
}
```

The new patch to GenericGraph.__copy__() always creates a new object of the same class as the original object -- no special case code for Graph, DiGraph, or BipartiteGraph.  Any future subclasses will work as well assuming they can handle the same initializer arguments (by passing them to the superclass initializer).



---

archive/issue_comments_074158.json:
```json
{
    "body": "This patch exposes a bug in another seldom used extension of the `Graph` class, `GraphBundle`.\n\n\n```\nFile \"/Users/rlmill/sage-4.3.3/devel/sage-main/sage/graphs/graph_bundle.py\", line 163:\n    sage: B.plot()\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/rlmill/sage-4.3.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/rlmill/sage-4.3.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/rlmill/sage-4.3.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[5]>\", line 1, in <module>\n        B.plot()###line 163:\n    sage: B.plot()\n      File \"/Users/rlmill/sage-4.3.3/local/lib/python/site-packages/sage/graphs/graph_bundle.py\", line 173, in plot\n        total_pos = generic_graph_pyx.spring_layout_fast(self, iterations=iters)\n      File \"generic_graph_pyx.pyx\", line 86, in sage.graphs.generic_graph_pyx.spring_layout_fast (sage/graphs/generic_graph_pyx.c:1361)\n      File \"/Users/rlmill/sage-4.3.3/local/lib/python/site-packages/sage/graphs/graph.py\", line 2061, in to_undirected\n        return copy(self)\n      File \"/Users/rlmill/sage-4.3.3/local/lib/python2.6/copy.py\", line 79, in copy\n        return copier(x)\n      File \"/Users/rlmill/sage-4.3.3/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 483, in __copy__\n        G = self.__class__(self, name=self.name(), pos=copy(self._pos), boundary=copy(self._boundary), implementation=implementation, sparse=sparse)\n      File \"/Users/rlmill/sage-4.3.3/local/lib/python/site-packages/sage/graphs/graph_bundle.py\", line 73, in __init__\n        if isinstance(args[0], (list, tuple)):\n    IndexError: tuple index out of range\n```\n",
    "created_at": "2010-03-02T02:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74158",
    "user": "@rlmill"
}
```

This patch exposes a bug in another seldom used extension of the `Graph` class, `GraphBundle`.


```
File "/Users/rlmill/sage-4.3.3/devel/sage-main/sage/graphs/graph_bundle.py", line 163:
    sage: B.plot()
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[5]>", line 1, in <module>
        B.plot()###line 163:
    sage: B.plot()
      File "/Users/rlmill/sage-4.3.3/local/lib/python/site-packages/sage/graphs/graph_bundle.py", line 173, in plot
        total_pos = generic_graph_pyx.spring_layout_fast(self, iterations=iters)
      File "generic_graph_pyx.pyx", line 86, in sage.graphs.generic_graph_pyx.spring_layout_fast (sage/graphs/generic_graph_pyx.c:1361)
      File "/Users/rlmill/sage-4.3.3/local/lib/python/site-packages/sage/graphs/graph.py", line 2061, in to_undirected
        return copy(self)
      File "/Users/rlmill/sage-4.3.3/local/lib/python2.6/copy.py", line 79, in copy
        return copier(x)
      File "/Users/rlmill/sage-4.3.3/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 483, in __copy__
        G = self.__class__(self, name=self.name(), pos=copy(self._pos), boundary=copy(self._boundary), implementation=implementation, sparse=sparse)
      File "/Users/rlmill/sage-4.3.3/local/lib/python/site-packages/sage/graphs/graph_bundle.py", line 73, in __init__
        if isinstance(args[0], (list, tuple)):
    IndexError: tuple index out of range
```




---

archive/issue_comments_074159.json:
```json
{
    "body": "I will offer the suggestion to disable the failing doctest, for discussion. I don't know of anyone who uses graph bundles in Sage. I've emailed Chris Godsil to see if he ever uses it.",
    "created_at": "2010-03-02T03:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74159",
    "user": "@rlmill"
}
```

I will offer the suggestion to disable the failing doctest, for discussion. I don't know of anyone who uses graph bundles in Sage. I've emailed Chris Godsil to see if he ever uses it.



---

archive/issue_comments_074160.json:
```json
{
    "body": "Sounds great to me.  The new patch disables the \"plot\" doctest that was failing and adds a \"known bugs\" warning to the beginning of the graph_bundle.py.",
    "created_at": "2010-03-02T16:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74160",
    "user": "@rhinton"
}
```

Sounds great to me.  The new patch disables the "plot" doctest that was failing and adds a "known bugs" warning to the beginning of the graph_bundle.py.



---

archive/issue_comments_074161.json:
```json
{
    "body": "Attachment [trac_8329-bipartite-graph-copy.patch](tarball://root/attachments/some-uuid/ticket8329/trac_8329-bipartite-graph-copy.patch) by @rhinton created at 2010-03-05 02:08:55\n\nmodifies copy() code in generic_graph.py and adds test to BipartiteGraph",
    "created_at": "2010-03-05T02:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74161",
    "user": "@rhinton"
}
```

Attachment [trac_8329-bipartite-graph-copy.patch](tarball://root/attachments/some-uuid/ticket8329/trac_8329-bipartite-graph-copy.patch) by @rhinton created at 2010-03-05 02:08:55

modifies copy() code in generic_graph.py and adds test to BipartiteGraph



---

archive/issue_comments_074162.json:
```json
{
    "body": "Anyone queasy about the `GraphBundle` doctest, Godsil tells me he has a student who is working on a bundle package, which I am assuming actually does something (unlike bundles in Sage). Look for this to appear in Sage at some point soon!",
    "created_at": "2010-03-06T22:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74162",
    "user": "@rlmill"
}
```

Anyone queasy about the `GraphBundle` doctest, Godsil tells me he has a student who is working on a bundle package, which I am assuming actually does something (unlike bundles in Sage). Look for this to appear in Sage at some point soon!



---

archive/issue_comments_074163.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-06T22:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74163",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074164.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-24T18:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74164",
    "user": "@rhinton"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_074165.json:
```json
{
    "body": "Found a failing doctest in combinat/posets/posets.py due to this change.  Additional patch coming soon.",
    "created_at": "2010-03-24T18:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74165",
    "user": "@rhinton"
}
```

Found a failing doctest in combinat/posets/posets.py due to this change.  Additional patch coming soon.



---

archive/issue_comments_074166.json:
```json
{
    "body": "Attachment [trac_8329-posets-repr.patch](tarball://root/attachments/some-uuid/ticket8329/trac_8329-posets-repr.patch) by @rhinton created at 2010-03-24 18:44:26\n\nApply both patches, order does not matter",
    "created_at": "2010-03-24T18:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74166",
    "user": "@rhinton"
}
```

Attachment [trac_8329-posets-repr.patch](tarball://root/attachments/some-uuid/ticket8329/trac_8329-posets-repr.patch) by @rhinton created at 2010-03-24 18:44:26

Apply both patches, order does not matter



---

archive/issue_comments_074167.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-24T18:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74167",
    "user": "@rhinton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074168.json:
```json
{
    "body": "New patch fixes posets doctest failure.  Apply both patches; order does not matter.",
    "created_at": "2010-03-24T18:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74168",
    "user": "@rhinton"
}
```

New patch fixes posets doctest failure.  Apply both patches; order does not matter.



---

archive/issue_comments_074169.json:
```json
{
    "body": "Good patch ! Applies fine, does its job.. :-)\n\nNathann",
    "created_at": "2010-04-01T11:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74169",
    "user": "@nathanncohen"
}
```

Good patch ! Applies fine, does its job.. :-)

Nathann



---

archive/issue_comments_074170.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-01T11:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74170",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074171.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n\n- trac_8329-bipartite-graph-copy.patch\n- trac_8329-posets-repr.patch",
    "created_at": "2010-04-15T20:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74171",
    "user": "@jhpalmieri"
}
```

Merged in 4.4.alpha0:

- trac_8329-bipartite-graph-copy.patch
- trac_8329-posets-repr.patch



---

archive/issue_comments_074172.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8329#issuecomment-74172",
    "user": "@jhpalmieri"
}
```

Resolution: fixed
