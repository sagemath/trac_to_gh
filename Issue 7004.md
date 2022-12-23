# Issue 7004: [with patch] Refactor the graph layout code, and add interface with graphviz for acyclic layout

Issue created by migration from https://trac.sagemath.org/ticket/7004

Original creator: nthiery

Original creation time: 2009-09-24 22:02:49

Assignee: nthiery

CC:  sage-combinat ncohen rlm

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


---

Comment by nthiery created at 2009-09-24 22:04:05

Changing status from new to assigned.


---

Comment by nthiery created at 2010-02-09 23:28:29

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-02-11 00:22:59

Cc me


---

Comment by rlm created at 2010-02-11 04:20:31

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

Comment by rlm created at 2010-02-11 05:37:41

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

Comment by nthiery created at 2010-02-11 10:51:00

Ooops, sorry Robert for the wasted time, I completely forgot to upload the latest version on trac yesterday night. I also screwed up in my example which too small. Please try instead:

```
G = posets.IntegerPartitions(5).hasse_diagram()
```


```
G = DiGraph({1:(2,3), 2:[4], 3:[4]})
```


Looking again at those pictures, it feels like the nodes of same height do not repulse each other, or at least not as much as in the pure spring layout.


---

Comment by nthiery created at 2010-02-11 14:46:32

See discussion on http://groups.google.com/group/sage-devel/browse_thread/thread/c46b8a2fcbb5875a


---

Comment by rlm created at 2010-02-11 15:44:13

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

Comment by hivert created at 2010-02-13 10:52:10

Hi there,

Compiling the doc in our queue if found a missing `r"""` in an `"""`, which prevented the doc to compile. I just pushed a trivial patch in our queue under the name 

```
    trac_7004-graphviz-doc-fix.patch
```

Nicolas: please upload or fold in yours at will.


---

Comment by hivert created at 2010-02-13 11:00:35

Sorry for replying to myself... Reading the doc I noticed the following: Nicolas you probably want to add yourself in the list of authors to the file `graph_latex.py` and probably some other files as well. Please seize the opportunity to fold my patch.


---

Comment by nthiery created at 2010-02-13 15:13:26

The uploaded patch folds in Florent's doc fix, adds me as author as he suggested, and adds a couple comments here and there.


---

Comment by vdelecroix created at 2010-02-27 22:43:37

It's not clear from the graph documentation that we can use latex for the output. It could be clearer to have a link in the docstring of the plot method or in the one of the object (Graph or DiGraph) itself.

An important option that I did not find

   * be able to modifiate the layout

It could be nice to have pointers in the documentation:

   * more documentation for the method .set_latex_options()... at least a list of options (or is it available somewhere else)
   * have a view(G, ...) example somewhere in the docstring of the object or in the set_latex_options one.


---

Comment by vdelecroix created at 2010-02-27 22:43:37

Changing status from needs_review to needs_work.


---

Comment by vdelecroix created at 2010-02-28 11:07:41

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

Comment by nthiery created at 2010-03-08 09:29:41

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

Comment by nthiery created at 2010-04-17 21:53:42

Calling view on a graph with dot2tex format can be a bit slow. But see #8707 for making it 5 times faster :-)


---

Attachment

Apply only this patch that fold all others


---

Comment by vdelecroix created at 2010-04-27 21:58:39

All test pass, documentation builds without warning and we get beautiful graphs!


---

Comment by vdelecroix created at 2010-04-27 21:58:39

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2010-04-27 22:09:40

Changing status from needs_review to positive_review.


---

Attachment

Apply only this one


---

Comment by nthiery created at 2010-04-28 10:08:14

Hi!

I made a micro fix in dot2tex_utils.py: the (assert_) have_dot2tex methods are now tested
with # optional rather than random. This is slightly stronger, and otherwise the assert_have_dot2tex method was failing when dot2tex was not installed. All test still pass,
so I leave the positive review, but please Vincent double check.

I also made micro changes in the patch header.


---

Comment by vdelecroix created at 2010-04-28 11:14:11

Tests still pass and doc still builds. It's OK for me.


---

Comment by was created at 2010-04-29 05:38:01

Resolution: fixed
