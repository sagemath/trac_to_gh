# Issue 7004: [with patch] Refactor the graph layout code, and add interface with graphviz for acyclic layout

archive/issues_007004.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat @nathanncohen @rlmill\n\nKeywords: graph layout, graphviz, acyclic\n\nExperimental patch on:  http://combinat.sagemath.org/hgwebdir.cgi/patches/file/tip/graphviz-nt.patch\n\nFrom the patch description:\n\n- Refactors the graph layout code, with:\n\n  - A new main graph.layout() method, to be called by plot, latex, ...\n  - Many layout methods, like graph._layout_circular()\n  - Extends the graphviz_string method (latex labels)\n  - Define a new layout method ._layout_acyclic() implemented by\n    calling dot2tex and graphviz\n  - Implement an alternative implementation of latex for graphs\n    by delegating all the work to dot2tex (GraphLatex.dot2tex_picture)\n  - Slightly simplifies the handling of default values for graph.latex_options\n\n- Makes some fixes to the poset code:\n  - __repr__ -> _repr_\n  - _latex_ by calling latex on the internal element\n\nTODO:\n\n- Add an optional default_layout method that subclasses could\n  override (like for the Petersen graph, ...). This would be better\n  for them than to systematically construct the layout at\n  construction time.\n\n- Refactor the remaining layout functions (planar, ...) as above\n\n- Double check all the logic to make sure it is backward compatible\n\n- A lot of code is doing things very similar to dot2tex. Maybe things\n  could be merged.\n\n- Finish to doctest everything\n\n- Implement the different options for both latex constructions\n\n- Add appropriate # optional comments\n\n- Make dot2tex.spkg into an optional sage package\n\nIssue created by migration from https://trac.sagemath.org/ticket/7004\n\n",
    "created_at": "2009-09-24T22:02:49Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "[with patch] Refactor the graph layout code, and add interface with graphviz for acyclic layout",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7004",
    "user": "@nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat @nathanncohen @rlmill

Keywords: graph layout, graphviz, acyclic

Experimental patch on:  http://combinat.sagemath.org/hgwebdir.cgi/patches/file/tip/graphviz-nt.patch

From the patch description:

- Refactors the graph layout code, with:

  - A new main graph.layout() method, to be called by plot, latex, ...
  - Many layout methods, like graph._layout_circular()
  - Extends the graphviz_string method (latex labels)
  - Define a new layout method ._layout_acyclic() implemented by
    calling dot2tex and graphviz
  - Implement an alternative implementation of latex for graphs
    by delegating all the work to dot2tex (GraphLatex.dot2tex_picture)
  - Slightly simplifies the handling of default values for graph.latex_options

- Makes some fixes to the poset code:
  - __repr__ -> _repr_
  - _latex_ by calling latex on the internal element

TODO:

- Add an optional default_layout method that subclasses could
  override (like for the Petersen graph, ...). This would be better
  for them than to systematically construct the layout at
  construction time.

- Refactor the remaining layout functions (planar, ...) as above

- Double check all the logic to make sure it is backward compatible

- A lot of code is doing things very similar to dot2tex. Maybe things
  could be merged.

- Finish to doctest everything

- Implement the different options for both latex constructions

- Add appropriate # optional comments

- Make dot2tex.spkg into an optional sage package

Issue created by migration from https://trac.sagemath.org/ticket/7004





---

archive/issue_comments_057908.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-24T22:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57908",
    "user": "@nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_057909.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-09T23:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57909",
    "user": "@nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057910.json:
```json
{
    "body": "Cc me",
    "created_at": "2010-02-11T00:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57910",
    "user": "@nathanncohen"
}
```

Cc me



---

archive/issue_comments_057911.json:
```json
{
    "body": "I tried reproducing this:\n\n```\nG = posets.IntegerPartitions(3).hasse_diagram() \nG.plot(layout=\"acyclic_dummy\", spring = True)\n```\n\n\nBut I got:\n\n```\nAttributeError                            Traceback (most recent call last)\n\n/Users/rlmill/sage-4.3.2/devel/sage-main/<ipython console> in <module>()\n\n/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)\n    136                 options['__original_opts'] = kwds\n    137             options.update(kwds)\n--> 138             return func(*args, **options)\n    139 \n    140         \n\n/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/generic_graph.pyc in plot(self, **options)\n   9137         \"\"\"\n   9138         from sage.graphs.graph_plot import GraphPlot\n-> 9139         return GraphPlot(graph=self, options=options).plot()\n   9140 \n   9141     def show(self, **kwds):\n\n/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/graph_plot.pyc in __init__(self, graph, options)\n     83         self._graph = graph\n     84         self._options = options\n---> 85         self.set_pos()\n     86         self._arcs = self._graph.has_multiple_edges(to_undirected=True)\n     87         self._loops = self._graph.has_loops()\n\n/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/graph_plot.pyc in set_pos(self)\n    183                 self._pos = pos\n    184 \n--> 185         if not self._pos:\n    186             self._pos = generic_graph_pyx.spring_layout_fast(self._graph, iterations=self._options['iterations'], height=(self._options['heights'] is not None))\n    187             \n\nAttributeError: 'GraphPlot' object has no attribute '_pos'\n```\n\n\nLooks like the first if of `set_pos` needs an `else` clause. But this wasn't the problem you indicated.",
    "created_at": "2010-02-11T04:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57911",
    "user": "@rlmill"
}
```

I tried reproducing this:

```
G = posets.IntegerPartitions(3).hasse_diagram() 
G.plot(layout="acyclic_dummy", spring = True)
```


But I got:

```
AttributeError                            Traceback (most recent call last)

/Users/rlmill/sage-4.3.2/devel/sage-main/<ipython console> in <module>()

/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)
    136                 options['__original_opts'] = kwds
    137             options.update(kwds)
--> 138             return func(*args, **options)
    139 
    140         

/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/generic_graph.pyc in plot(self, **options)
   9137         """
   9138         from sage.graphs.graph_plot import GraphPlot
-> 9139         return GraphPlot(graph=self, options=options).plot()
   9140 
   9141     def show(self, **kwds):

/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/graph_plot.pyc in __init__(self, graph, options)
     83         self._graph = graph
     84         self._options = options
---> 85         self.set_pos()
     86         self._arcs = self._graph.has_multiple_edges(to_undirected=True)
     87         self._loops = self._graph.has_loops()

/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/graph_plot.pyc in set_pos(self)
    183                 self._pos = pos
    184 
--> 185         if not self._pos:
    186             self._pos = generic_graph_pyx.spring_layout_fast(self._graph, iterations=self._options['iterations'], height=(self._options['heights'] is not None))
    187             

AttributeError: 'GraphPlot' object has no attribute '_pos'
```


Looks like the first if of `set_pos` needs an `else` clause. But this wasn't the problem you indicated.



---

archive/issue_comments_057912.json:
```json
{
    "body": "I tried this again, and now I am getting a different (!) error:\n\n```\nAttributeError                            Traceback (most recent call last)\n\n/Users/rlmill/sage-4.3.2/devel/sage-main/<ipython console> in <module>()\n\n/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)\n    136                 options['__original_opts'] = kwds\n    137             options.update(kwds)\n--> 138             return func(*args, **options)\n    139 \n    140         \n\n/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/generic_graph.pyc in plot(self, **options)\n   9596         \"\"\"\n   9597         from sage.graphs.graph_plot import GraphPlot\n-> 9598         return GraphPlot(graph=self, options=options).plot()\n   9599 \n   9600     def show(self, **kwds):\n\n/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/graph_plot.pyc in __init__(self, graph, options)\n     91         self._graph = graph\n     92         self._options = options\n---> 93         self.set_pos()\n     94         self._arcs = self._graph.has_multiple_edges(to_undirected=True)\n     95         self._loops = self._graph.has_loops()\n\n/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/graph_plot.pyc in set_pos(self)\n    137             sage: t.plot(heights={0:[0], 1:[4,5,1], 2:[2], 3:[3,6]})\n    138         \"\"\"\n--> 139         self._pos = self._graph.layout(**self._options)\n    140 \n    141     def set_vertices(self, **vertex_options):\n\n/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/generic_graph.pyc in layout(self, layout, pos, dim, save_pos, **options)\n   8952 \n   8953         if hasattr(self, \"layout_%s\"%layout):\n-> 8954             pos = getattr(self, \"layout_%s\"%layout)(dim = dim, **options)\n   8955         elif layout is not None:\n   8956             raise ValueError, \"unknown layout algorithm: %s\"%layout\n\n/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/digraph.pyc in layout_acyclic_dummy(self, heights, **options)\n   1482             levels = [sorted(z) for z in levels]\n   1483             heights = dict([[i, levels[i]] for i in range(len(levels))])\n-> 1484         return self.layout_graded(heights = heights, **options)\n   1485 \n   1486     def level_sets(self):\n\nAttributeError: 'DiGraph' object has no attribute 'layout_graded'\n```\n\n\nI'm baffled.",
    "created_at": "2010-02-11T05:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57912",
    "user": "@rlmill"
}
```

I tried this again, and now I am getting a different (!) error:

```
AttributeError                            Traceback (most recent call last)

/Users/rlmill/sage-4.3.2/devel/sage-main/<ipython console> in <module>()

/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)
    136                 options['__original_opts'] = kwds
    137             options.update(kwds)
--> 138             return func(*args, **options)
    139 
    140         

/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/generic_graph.pyc in plot(self, **options)
   9596         """
   9597         from sage.graphs.graph_plot import GraphPlot
-> 9598         return GraphPlot(graph=self, options=options).plot()
   9599 
   9600     def show(self, **kwds):

/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/graph_plot.pyc in __init__(self, graph, options)
     91         self._graph = graph
     92         self._options = options
---> 93         self.set_pos()
     94         self._arcs = self._graph.has_multiple_edges(to_undirected=True)
     95         self._loops = self._graph.has_loops()

/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/graph_plot.pyc in set_pos(self)
    137             sage: t.plot(heights={0:[0], 1:[4,5,1], 2:[2], 3:[3,6]})
    138         """
--> 139         self._pos = self._graph.layout(**self._options)
    140 
    141     def set_vertices(self, **vertex_options):

/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/generic_graph.pyc in layout(self, layout, pos, dim, save_pos, **options)
   8952 
   8953         if hasattr(self, "layout_%s"%layout):
-> 8954             pos = getattr(self, "layout_%s"%layout)(dim = dim, **options)
   8955         elif layout is not None:
   8956             raise ValueError, "unknown layout algorithm: %s"%layout

/Users/rlmill/sage-4.3.2/local/lib/python2.6/site-packages/sage/graphs/digraph.pyc in layout_acyclic_dummy(self, heights, **options)
   1482             levels = [sorted(z) for z in levels]
   1483             heights = dict([[i, levels[i]] for i in range(len(levels))])
-> 1484         return self.layout_graded(heights = heights, **options)
   1485 
   1486     def level_sets(self):

AttributeError: 'DiGraph' object has no attribute 'layout_graded'
```


I'm baffled.



---

archive/issue_comments_057913.json:
```json
{
    "body": "Ooops, sorry Robert for the wasted time, I completely forgot to upload the latest version on trac yesterday night. I also screwed up in my example which too small. Please try instead:\n\n```\nG = posets.IntegerPartitions(5).hasse_diagram()\n```\n\n\n```\nG = DiGraph({1:(2,3), 2:[4], 3:[4]})\n```\n\n\nLooking again at those pictures, it feels like the nodes of same height do not repulse each other, or at least not as much as in the pure spring layout.",
    "created_at": "2010-02-11T10:51:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57913",
    "user": "@nthiery"
}
```

Ooops, sorry Robert for the wasted time, I completely forgot to upload the latest version on trac yesterday night. I also screwed up in my example which too small. Please try instead:

```
G = posets.IntegerPartitions(5).hasse_diagram()
```


```
G = DiGraph({1:(2,3), 2:[4], 3:[4]})
```


Looking again at those pictures, it feels like the nodes of same height do not repulse each other, or at least not as much as in the pure spring layout.



---

archive/issue_comments_057914.json:
```json
{
    "body": "See discussion on http://groups.google.com/group/sage-devel/browse_thread/thread/c46b8a2fcbb5875a",
    "created_at": "2010-02-11T14:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57914",
    "user": "@nthiery"
}
```

See discussion on http://groups.google.com/group/sage-devel/browse_thread/thread/c46b8a2fcbb5875a



---

archive/issue_comments_057915.json:
```json
{
    "body": "All graphs used to plot as square plots, whether you wanted them to or not. This would stretch any plot into a square, so if the relative distances were larger in one dimension than in the other, this would not show in the plot.\n\nThe following adjustment seems to improve the situation a bit, but I'm really not sure what the \"right\" fix is here.\n\n\n```\n--- a/sage/graphs/generic_graph.py\tThu Feb 11 15:36:58 2010 +0100\n+++ b/sage/graphs/generic_graph.py\tThu Feb 11 07:39:46 2010 -0800\n@@ -9058,6 +9058,8 @@\n             # We restore back the original height.\n             for x in self.vertices():\n                 newpos[x][dim-1] = pos[x][dim-1]\n+                for i in range(dim-1):\n+                    newpos[x][i] *= 10\n             pos = newpos\n         return pos\n```\n",
    "created_at": "2010-02-11T15:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57915",
    "user": "@rlmill"
}
```

All graphs used to plot as square plots, whether you wanted them to or not. This would stretch any plot into a square, so if the relative distances were larger in one dimension than in the other, this would not show in the plot.

The following adjustment seems to improve the situation a bit, but I'm really not sure what the "right" fix is here.


```
--- a/sage/graphs/generic_graph.py	Thu Feb 11 15:36:58 2010 +0100
+++ b/sage/graphs/generic_graph.py	Thu Feb 11 07:39:46 2010 -0800
@@ -9058,6 +9058,8 @@
             # We restore back the original height.
             for x in self.vertices():
                 newpos[x][dim-1] = pos[x][dim-1]
+                for i in range(dim-1):
+                    newpos[x][i] *= 10
             pos = newpos
         return pos
```




---

archive/issue_comments_057916.json:
```json
{
    "body": "Hi there,\n\nCompiling the doc in our queue if found a missing `r\"\"\"` in an `\"\"\"`, which prevented the doc to compile. I just pushed a trivial patch in our queue under the name \n\n```\n    trac_7004-graphviz-doc-fix.patch\n```\n\nNicolas: please upload or fold in yours at will.",
    "created_at": "2010-02-13T10:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57916",
    "user": "@hivert"
}
```

Hi there,

Compiling the doc in our queue if found a missing `r"""` in an `"""`, which prevented the doc to compile. I just pushed a trivial patch in our queue under the name 

```
    trac_7004-graphviz-doc-fix.patch
```

Nicolas: please upload or fold in yours at will.



---

archive/issue_comments_057917.json:
```json
{
    "body": "Sorry for replying to myself... Reading the doc I noticed the following: Nicolas you probably want to add yourself in the list of authors to the file `graph_latex.py` and probably some other files as well. Please seize the opportunity to fold my patch.",
    "created_at": "2010-02-13T11:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57917",
    "user": "@hivert"
}
```

Sorry for replying to myself... Reading the doc I noticed the following: Nicolas you probably want to add yourself in the list of authors to the file `graph_latex.py` and probably some other files as well. Please seize the opportunity to fold my patch.



---

archive/issue_comments_057918.json:
```json
{
    "body": "The uploaded patch folds in Florent's doc fix, adds me as author as he suggested, and adds a couple comments here and there.",
    "created_at": "2010-02-13T15:13:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57918",
    "user": "@nthiery"
}
```

The uploaded patch folds in Florent's doc fix, adds me as author as he suggested, and adds a couple comments here and there.



---

archive/issue_comments_057919.json:
```json
{
    "body": "It's not clear from the graph documentation that we can use latex for the output. It could be clearer to have a link in the docstring of the plot method or in the one of the object (Graph or DiGraph) itself.\n\nAn important option that I did not find\n\n* be able to modifiate the layout\n\nIt could be nice to have pointers in the documentation:\n\n* more documentation for the method .set_latex_options()... at least a list of options (or is it available somewhere else)\n* have a view(G, ...) example somewhere in the docstring of the object or in the set_latex_options one.",
    "created_at": "2010-02-27T22:43:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57919",
    "user": "@videlec"
}
```

It's not clear from the graph documentation that we can use latex for the output. It could be clearer to have a link in the docstring of the plot method or in the one of the object (Graph or DiGraph) itself.

An important option that I did not find

* be able to modifiate the layout

It could be nice to have pointers in the documentation:

* more documentation for the method .set_latex_options()... at least a list of options (or is it available somewhere else)
* have a view(G, ...) example somewhere in the docstring of the object or in the set_latex_options one.



---

archive/issue_comments_057920.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-27T22:43:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57920",
    "user": "@videlec"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057921.json:
```json
{
    "body": "> It's not clear from the graph documentation that we can use latex for the output. It could be clearer to have a link in the docstring of the plot method or in the one of the object (Graph or DiGraph) itself.\n\nThe documentation is quite clear and complete but in an \"hidden\" file: sage.graphs.graph_latex\n\nThe refactorization of the code is really good, I will just talk about the graphviz, string and latex possibilities. Perhaps for other tickets...\n\n1) __graph to text conversion__\n\nThere is different standards format for string representations of graph objects. At least two or three\n* graphml (http://graphml.graphdrawing.org) which uses XML\n* dot (http://www.graphviz.org) which was created by graphviz\n* xdot which is can be considered as an extension of dot with non standard options\n\nFrom now, there exists a method graphviz_string. Could we prefer a dot_string ? and in the same manner think about a graphml_string ?\nThe main problem with those two names is that there does not start with the same prefix... and we get a contradiction with the use of the tab completion. As the refactorization for layout is perhaps we can consider string_dot and string_gml ? and string(format='dot') string(format='gml')\n\n2) __latex generation__\n\nThere is a intersection between the two format of GraphLatex (which is written in the description). dot2tex is able to produce a lot of different format...\n\nCouldn't we prefer in the GraphLatex file some different methods\n\n* picture_tikz\n* picture_pstricks\n* which can also be used from picture(format='tikz') picture(format='pstricks')\n\nand have an option inside picture_tikz to consider whether we use dot2tex or we use the actual code ?\n\n3) __latency__\n\nIt took one second to execute in a console\n\n\n```\nneato -Txdot my_graph.dot | dot2tex -ftikz | pdflatex\n```\n\n\nAnd almost one minute for\n\n```\nsage: G = MyGraph()\nsage: G.set_latex_options(format='dot2tex')\nsage: view(G)\n```\n\n\nDo you have an idea where the time is lost ?\n\n4) __graph editor__\n\nThere is a java program which can be used to interact with graphviz: http://www.dynagraph.org/\nThe program is made of two things dynagraph and grappa. It could be really nice to have an applet inside the notebook to use it directly as graph_editor works !!\n\nIt is available under the Common Public License",
    "created_at": "2010-02-28T11:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57921",
    "user": "@videlec"
}
```

> It's not clear from the graph documentation that we can use latex for the output. It could be clearer to have a link in the docstring of the plot method or in the one of the object (Graph or DiGraph) itself.

The documentation is quite clear and complete but in an "hidden" file: sage.graphs.graph_latex

The refactorization of the code is really good, I will just talk about the graphviz, string and latex possibilities. Perhaps for other tickets...

1) __graph to text conversion__

There is different standards format for string representations of graph objects. At least two or three
* graphml (http://graphml.graphdrawing.org) which uses XML
* dot (http://www.graphviz.org) which was created by graphviz
* xdot which is can be considered as an extension of dot with non standard options

From now, there exists a method graphviz_string. Could we prefer a dot_string ? and in the same manner think about a graphml_string ?
The main problem with those two names is that there does not start with the same prefix... and we get a contradiction with the use of the tab completion. As the refactorization for layout is perhaps we can consider string_dot and string_gml ? and string(format='dot') string(format='gml')

2) __latex generation__

There is a intersection between the two format of GraphLatex (which is written in the description). dot2tex is able to produce a lot of different format...

Couldn't we prefer in the GraphLatex file some different methods

* picture_tikz
* picture_pstricks
* which can also be used from picture(format='tikz') picture(format='pstricks')

and have an option inside picture_tikz to consider whether we use dot2tex or we use the actual code ?

3) __latency__

It took one second to execute in a console


```
neato -Txdot my_graph.dot | dot2tex -ftikz | pdflatex
```


And almost one minute for

```
sage: G = MyGraph()
sage: G.set_latex_options(format='dot2tex')
sage: view(G)
```


Do you have an idea where the time is lost ?

4) __graph editor__

There is a java program which can be used to interact with graphviz: http://www.dynagraph.org/
The program is made of two things dynagraph and grappa. It could be really nice to have an applet inside the notebook to use it directly as graph_editor works !!

It is available under the Common Public License



---

archive/issue_comments_057922.json:
```json
{
    "body": "Replying to [comment:21 vdelecroix]:\n> > It's not clear from the graph documentation that we can use latex for the output. It could be clearer to have a link in the docstring of the plot method or in the one of the object (Graph or DiGraph) itself.\n> The documentation is quite clear and complete but in an \"hidden\" file: sage.graphs.graph_latex\n\n+1 on adding appropriate links.\n\n> The refactorization of the code is really good, \n\n:-)\n\n> I will just talk about the graphviz, string and latex possibilities. Perhaps for other tickets...\n\n> 1) __graph to text conversion__\n> \n> There is different standards format for string representations of graph objects. At least two or three\n>   * graphml (http://graphml.graphdrawing.org) which uses XML\n>   * dot (http://www.graphviz.org) which was created by graphviz\n>   * xdot which is can be considered as an extension of dot with non standard options\n>\n> From now, there exists a method graphviz_string. Could we prefer a\n> dot_string ? and in the same manner think about a graphml_string ?\n\nYup. Note that there already exists methods graph6_string\nsparse6_string, and so on.\n\n> The main problem with those two names is that there does not start\n> with the same prefix... and we get a contradiction with the use of\n> the tab completion. As the refactorization for layout is perhaps we\n> can consider string_dot and string_gml ? and string(format='dot')\n> string(format='gml')\n\nThe ..._string convention is followed consistently; so it might be a\nbit late to change it. On the other hand, it could be nice indeed to\nhave a string(format='...') method\n\n\n> 2) __latex generation__\n> \n> There is a intersection between the two format of GraphLatex (which is written in the description). dot2tex is able to produce a lot of different format...\n> \n> Couldn't we prefer in the GraphLatex file some different methods\n> \n>   * picture_tikz\n>   * picture_pstricks\n>   * which can also be used from picture(format='tikz') picture(format='pstricks')\n> \n> and have an option inside picture_tikz to consider whether we use dot2tex or we use the actual code ?\n\nI see all those methods as internal (actually, maybe they should start\nwith _), while the main entry point for the user is the latex method.\nWith this in mind, each picture_* method should concentrate on a\nspecific task (creating a tikz picture manually / creating a picture\nby calling dot2tex), whereas all the dispatching job should go in the\nlatex method.\n\nI would not mind if the latex method would take extra arguments (as a\nshortcut to calling set_latex_options).\n\n> 3) __latency__\n> \n> It took one second to execute in a console\n> \n> {{{\n> neato -Txdot my_graph.dot | dot2tex -ftikz | pdflatex\n> }}}\n> \n> And almost one minute for\n> {{{\n> sage: G = MyGraph()\n> sage: G.set_latex_options(format='dot2tex')\n> sage: view(G)\n> }}}\n> \n> Do you have an idea where the time is lost ?\n\nAh, interesting! On extra thing that dot2tex does it to run latex on\neach node to get the dimension of its bounding box. In principle, this\nis done in one swoop for all nodes, so that should not be that bad. So\nwe should check whether it is dot2tex or the interface to dot2tex\nwhich is to be blamed. Could you give me your example and/or run the\ndot2tex script on it?\n\n> 4) __graph editor__\n> \n> There is a java program which can be used to interact with graphviz: http://www.dynagraph.org/\n> The program is made of two things dynagraph and grappa. It could be really nice to have an applet inside the notebook to use it directly as graph_editor works !!\n> \n> It is available under the Common Public License\n\n+1 definitely!\n\nIt does not seem to have been very active recently though.\n\nCheers,",
    "created_at": "2010-03-08T09:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57922",
    "user": "@nthiery"
}
```

Replying to [comment:21 vdelecroix]:
> > It's not clear from the graph documentation that we can use latex for the output. It could be clearer to have a link in the docstring of the plot method or in the one of the object (Graph or DiGraph) itself.
> The documentation is quite clear and complete but in an "hidden" file: sage.graphs.graph_latex

+1 on adding appropriate links.

> The refactorization of the code is really good, 

:-)

> I will just talk about the graphviz, string and latex possibilities. Perhaps for other tickets...

> 1) __graph to text conversion__
> 
> There is different standards format for string representations of graph objects. At least two or three
>   * graphml (http://graphml.graphdrawing.org) which uses XML
>   * dot (http://www.graphviz.org) which was created by graphviz
>   * xdot which is can be considered as an extension of dot with non standard options
>
> From now, there exists a method graphviz_string. Could we prefer a
> dot_string ? and in the same manner think about a graphml_string ?

Yup. Note that there already exists methods graph6_string
sparse6_string, and so on.

> The main problem with those two names is that there does not start
> with the same prefix... and we get a contradiction with the use of
> the tab completion. As the refactorization for layout is perhaps we
> can consider string_dot and string_gml ? and string(format='dot')
> string(format='gml')

The ..._string convention is followed consistently; so it might be a
bit late to change it. On the other hand, it could be nice indeed to
have a string(format='...') method


> 2) __latex generation__
> 
> There is a intersection between the two format of GraphLatex (which is written in the description). dot2tex is able to produce a lot of different format...
> 
> Couldn't we prefer in the GraphLatex file some different methods
> 
>   * picture_tikz
>   * picture_pstricks
>   * which can also be used from picture(format='tikz') picture(format='pstricks')
> 
> and have an option inside picture_tikz to consider whether we use dot2tex or we use the actual code ?

I see all those methods as internal (actually, maybe they should start
with _), while the main entry point for the user is the latex method.
With this in mind, each picture_* method should concentrate on a
specific task (creating a tikz picture manually / creating a picture
by calling dot2tex), whereas all the dispatching job should go in the
latex method.

I would not mind if the latex method would take extra arguments (as a
shortcut to calling set_latex_options).

> 3) __latency__
> 
> It took one second to execute in a console
> 
> {{{
> neato -Txdot my_graph.dot | dot2tex -ftikz | pdflatex
> }}}
> 
> And almost one minute for
> {{{
> sage: G = MyGraph()
> sage: G.set_latex_options(format='dot2tex')
> sage: view(G)
> }}}
> 
> Do you have an idea where the time is lost ?

Ah, interesting! On extra thing that dot2tex does it to run latex on
each node to get the dimension of its bounding box. In principle, this
is done in one swoop for all nodes, so that should not be that bad. So
we should check whether it is dot2tex or the interface to dot2tex
which is to be blamed. Could you give me your example and/or run the
dot2tex script on it?

> 4) __graph editor__
> 
> There is a java program which can be used to interact with graphviz: http://www.dynagraph.org/
> The program is made of two things dynagraph and grappa. It could be really nice to have an applet inside the notebook to use it directly as graph_editor works !!
> 
> It is available under the Common Public License

+1 definitely!

It does not seem to have been very active recently though.

Cheers,



---

archive/issue_comments_057923.json:
```json
{
    "body": "Calling view on a graph with dot2tex format can be a bit slow. But see #8707 for making it 5 times faster :-)",
    "created_at": "2010-04-17T21:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57923",
    "user": "@nthiery"
}
```

Calling view on a graph with dot2tex format can be a bit slow. But see #8707 for making it 5 times faster :-)



---

archive/issue_comments_057924.json:
```json
{
    "body": "Attachment [trac_7004-graphviz.patch](tarball://root/attachments/some-uuid/ticket7004/trac_7004-graphviz.patch) by @videlec created at 2010-04-27 21:56:20\n\nApply only this patch that fold all others",
    "created_at": "2010-04-27T21:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57924",
    "user": "@videlec"
}
```

Attachment [trac_7004-graphviz.patch](tarball://root/attachments/some-uuid/ticket7004/trac_7004-graphviz.patch) by @videlec created at 2010-04-27 21:56:20

Apply only this patch that fold all others



---

archive/issue_comments_057925.json:
```json
{
    "body": "All test pass, documentation builds without warning and we get beautiful graphs!",
    "created_at": "2010-04-27T21:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57925",
    "user": "@videlec"
}
```

All test pass, documentation builds without warning and we get beautiful graphs!



---

archive/issue_comments_057926.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-27T21:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57926",
    "user": "@videlec"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057927.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-27T22:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57927",
    "user": "@videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057928.json:
```json
{
    "body": "Attachment [trac_7004-graphviz-nt.patch](tarball://root/attachments/some-uuid/ticket7004/trac_7004-graphviz-nt.patch) by @nthiery created at 2010-04-28 10:05:16\n\nApply only this one",
    "created_at": "2010-04-28T10:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57928",
    "user": "@nthiery"
}
```

Attachment [trac_7004-graphviz-nt.patch](tarball://root/attachments/some-uuid/ticket7004/trac_7004-graphviz-nt.patch) by @nthiery created at 2010-04-28 10:05:16

Apply only this one



---

archive/issue_comments_057929.json:
```json
{
    "body": "Hi!\n\nI made a micro fix in dot2tex_utils.py: the (assert_) have_dot2tex methods are now tested\nwith # optional rather than random. This is slightly stronger, and otherwise the assert_have_dot2tex method was failing when dot2tex was not installed. All test still pass,\nso I leave the positive review, but please Vincent double check.\n\nI also made micro changes in the patch header.",
    "created_at": "2010-04-28T10:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57929",
    "user": "@nthiery"
}
```

Hi!

I made a micro fix in dot2tex_utils.py: the (assert_) have_dot2tex methods are now tested
with # optional rather than random. This is slightly stronger, and otherwise the assert_have_dot2tex method was failing when dot2tex was not installed. All test still pass,
so I leave the positive review, but please Vincent double check.

I also made micro changes in the patch header.



---

archive/issue_comments_057930.json:
```json
{
    "body": "Tests still pass and doc still builds. It's OK for me.",
    "created_at": "2010-04-28T11:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57930",
    "user": "@videlec"
}
```

Tests still pass and doc still builds. It's OK for me.



---

archive/issue_comments_057931.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7004#issuecomment-57931",
    "user": "@williamstein"
}
```

Resolution: fixed
