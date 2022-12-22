# Issue 5975: Implement latex output for (combinatorial) graphs

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-05-04 05:36:18

Assignee: rlm

CC:  jhpalmieri ekirkman

For a graph  g  the command latex(g)  has not been implemented.  The tkz-graph package provides latex commands for drawing graphs in a variety of ways.  So rather than outputting a graphic image, this command would output latex commands that could be incorporated into latex documents.

This originated in this [thread](http://groups.google.com/group/sage-devel/browse_thread/thread/834be3b28bd7919f) on sage-devel.  The tkz-graph package is described [here](http://altermundus.com/pages/graph.html) and more can be found [here](http://graphtheoryinlatex.blogspot.com/).


---

Comment by rbeezer created at 2009-05-04 05:48:14

Changing assignee from rlm to rbeezer.


---

Comment by rbeezer created at 2009-05-05 05:47:29

latex-test-1.patch is just that, a test.  Code by Fidel Barrera-Cruz, which I've got working in this patch.  Strictly experimental for discussion purposes.  The session


```
g = graphs.PetersenGraph()
latex(g)
```


produces


```
\begin{tikzpicture}
\GraphInit[vstyle=Dijkstra]

\SetVertexNoLabel
\SetVertexMath   

\Vertex[x=2.5cm,y=4.7553cm]{a0}
\Vertex[x=0.0cm,y=2.9389cm]{a1}
\Vertex[x=0.9549cm,y=0.0cm]{a2}
\Vertex[x=4.0451cm,y=0.0cm]{a3}
\Vertex[x=5.0cm,y=2.9389cm]{a4}
\Vertex[x=2.5cm,y=3.441cm]{a5} 
\Vertex[x=1.25cm,y=2.5328cm]{a6}
\Vertex[x=1.7275cm,y=1.0633cm]{a7}
\Vertex[x=3.2725cm,y=1.0633cm]{a8}
\Vertex[x=3.75cm,y=2.5328cm]{a9}

\AssignVertexLabel{a}{10}{
$0$,
$1$,
$2$,
$3$,
$4$,
$5$,
$6$,
$7$,
$8$,
$9$
}

\Edge(a0)(a1)
\Edge(a0)(a4)
\Edge(a0)(a5)
\Edge(a1)(a2)
\Edge(a1)(a6)
\Edge(a2)(a3)
\Edge(a2)(a7)
\Edge(a3)(a4)
\Edge(a3)(a8)
\Edge(a4)(a9)
\Edge(a5)(a7)
\Edge(a5)(a8)
\Edge(a6)(a8)
\Edge(a6)(a9)
\Edge(a7)(a9)

\end{tikzpicture}
```


which when run through Latex produces the attached PDF.


---

Attachment


---

Attachment


---

Comment by fidelbarrera created at 2009-05-08 01:11:44

Second test to latex graphs. Includes more options than first test.


---

Attachment

Replying to [comment:2 rbeezer]:
> latex-test-1.patch is just that, a test.  Code by Fidel Barrera-Cruz, which I've got working in this patch.  Strictly experimental for discussion purposes.  The session
> 
> {{{
> g = graphs.PetersenGraph()
> latex(g)
> }}}
> 
> produces
> 
> {{{
> \begin{tikzpicture}
> \GraphInit[vstyle=Dijkstra]
> 
> \SetVertexNoLabel
> \SetVertexMath   
> 
> \Vertex[x=2.5cm,y=4.7553cm]{a0}
> \Vertex[x=0.0cm,y=2.9389cm]{a1}
> \Vertex[x=0.9549cm,y=0.0cm]{a2}
> \Vertex[x=4.0451cm,y=0.0cm]{a3}
> \Vertex[x=5.0cm,y=2.9389cm]{a4}
> \Vertex[x=2.5cm,y=3.441cm]{a5} 
> \Vertex[x=1.25cm,y=2.5328cm]{a6}
> \Vertex[x=1.7275cm,y=1.0633cm]{a7}
> \Vertex[x=3.2725cm,y=1.0633cm]{a8}
> \Vertex[x=3.75cm,y=2.5328cm]{a9}
> 
> \AssignVertexLabel{a}{10}{
> $0$,
> $1$,
> $2$,
> $3$,
> $4$,
> $5$,
> $6$,
> $7$,
> $8$,
> $9$
> }
> 
> \Edge(a0)(a1)
> \Edge(a0)(a4)
> \Edge(a0)(a5)
> \Edge(a1)(a2)
> \Edge(a1)(a6)
> \Edge(a2)(a3)
> \Edge(a2)(a7)
> \Edge(a3)(a4)
> \Edge(a3)(a8)
> \Edge(a4)(a9)
> \Edge(a5)(a7)
> \Edge(a5)(a8)
> \Edge(a6)(a8)
> \Edge(a6)(a9)
> \Edge(a7)(a9)
> 
> \end{tikzpicture}
> }}}
> 
> which when run through Latex produces the attached PDF.
This new test version supports colors in vertices, labels and vertices. One can also choose among the different styles offered by tkz-graph, 'Art', 'Shade', 'Welsh', 'Classic', etc. A sample session:


```
G=graphs.PetersenGraph()
latex(G)
```

This should give:


```
\begin{tikzpicture}
%
\definecolor{col_a0}{rgb}{1.0,1.0,1.0}
\definecolor{col_a1}{rgb}{1.0,1.0,1.0}
\definecolor{col_a2}{rgb}{1.0,1.0,1.0}
\definecolor{col_a3}{rgb}{1.0,1.0,1.0}
\definecolor{col_a4}{rgb}{1.0,1.0,1.0}
\definecolor{col_a5}{rgb}{1.0,1.0,1.0}
\definecolor{col_a6}{rgb}{1.0,1.0,1.0}
\definecolor{col_a7}{rgb}{1.0,1.0,1.0}
\definecolor{col_a8}{rgb}{1.0,1.0,1.0}
\definecolor{col_a9}{rgb}{1.0,1.0,1.0}
%
%
\definecolor{col_lab_a0}{rgb}{0.0,0.0,0.0}
\definecolor{col_lab_a1}{rgb}{0.0,0.0,0.0}
\definecolor{col_lab_a2}{rgb}{0.0,0.0,0.0}
\definecolor{col_lab_a3}{rgb}{0.0,0.0,0.0}
\definecolor{col_lab_a4}{rgb}{0.0,0.0,0.0}
\definecolor{col_lab_a5}{rgb}{0.0,0.0,0.0}
\definecolor{col_lab_a6}{rgb}{0.0,0.0,0.0}
\definecolor{col_lab_a7}{rgb}{0.0,0.0,0.0}
\definecolor{col_lab_a8}{rgb}{0.0,0.0,0.0}
\definecolor{col_lab_a9}{rgb}{0.0,0.0,0.0}
%
%
\definecolor{col_a0-a1}{rgb}{0.0,0.0,0.0}
\definecolor{col_a0-a4}{rgb}{0.0,0.0,0.0}
\definecolor{col_a0-a5}{rgb}{0.0,0.0,0.0}
\definecolor{col_a1-a2}{rgb}{0.0,0.0,0.0}
\definecolor{col_a1-a6}{rgb}{0.0,0.0,0.0}
\definecolor{col_a2-a3}{rgb}{0.0,0.0,0.0}
\definecolor{col_a2-a7}{rgb}{0.0,0.0,0.0}
\definecolor{col_a3-a4}{rgb}{0.0,0.0,0.0}
\definecolor{col_a3-a8}{rgb}{0.0,0.0,0.0}
\definecolor{col_a4-a9}{rgb}{0.0,0.0,0.0}
\definecolor{col_a5-a7}{rgb}{0.0,0.0,0.0}
\definecolor{col_a5-a8}{rgb}{0.0,0.0,0.0}
\definecolor{col_a6-a8}{rgb}{0.0,0.0,0.0}
\definecolor{col_a6-a9}{rgb}{0.0,0.0,0.0}
\definecolor{col_a7-a9}{rgb}{0.0,0.0,0.0}
%
%
\GraphInit[vstyle=Normal]
%
\SetVertexMath
%
\SetVertexNoLabel
%
\renewcommand*{\VertexLightFillColor}{col_a0}
\Vertex[x=2.5cm,y=4.7553cm]{a0}
\renewcommand*{\VertexLightFillColor}{col_a1}
\Vertex[x=0.0cm,y=2.9389cm]{a1}
\renewcommand*{\VertexLightFillColor}{col_a2}
\Vertex[x=0.9549cm,y=0.0cm]{a2}
\renewcommand*{\VertexLightFillColor}{col_a3}
\Vertex[x=4.0451cm,y=0.0cm]{a3}
\renewcommand*{\VertexLightFillColor}{col_a4}
\Vertex[x=5.0cm,y=2.9389cm]{a4}
\renewcommand*{\VertexLightFillColor}{col_a5}
\Vertex[x=2.5cm,y=3.441cm]{a5}
\renewcommand*{\VertexLightFillColor}{col_a6}
\Vertex[x=1.25cm,y=2.5328cm]{a6}
\renewcommand*{\VertexLightFillColor}{col_a7}
\Vertex[x=1.7275cm,y=1.0633cm]{a7}
\renewcommand*{\VertexLightFillColor}{col_a8}
\Vertex[x=3.2725cm,y=1.0633cm]{a8}
\renewcommand*{\VertexLightFillColor}{col_a9}
\Vertex[x=3.75cm,y=2.5328cm]{a9}
%
%
\AssignVertexLabel{a}{10}{
\color{col_lab_a0}{$0$},
\color{col_lab_a1}{$1$},
\color{col_lab_a2}{$2$},
\color{col_lab_a3}{$3$},
\color{col_lab_a4}{$4$},
\color{col_lab_a5}{$5$},
\color{col_lab_a6}{$6$},
\color{col_lab_a7}{$7$},
\color{col_lab_a8}{$8$},
\color{col_lab_a9}{$9$}
}
%
%
\renewcommand*{\EdgeColor}{col_a0-a1}
\Edge(a0)(a1)
\renewcommand*{\EdgeColor}{col_a0-a4}
\Edge(a0)(a4)
\renewcommand*{\EdgeColor}{col_a0-a5}
\Edge(a0)(a5)
\renewcommand*{\EdgeColor}{col_a1-a2}
\Edge(a1)(a2)
\renewcommand*{\EdgeColor}{col_a1-a6}
\Edge(a1)(a6)
\renewcommand*{\EdgeColor}{col_a2-a3}
\Edge(a2)(a3)
\renewcommand*{\EdgeColor}{col_a2-a7}
\Edge(a2)(a7)
\renewcommand*{\EdgeColor}{col_a3-a4}
\Edge(a3)(a4)
\renewcommand*{\EdgeColor}{col_a3-a8}
\Edge(a3)(a8)
\renewcommand*{\EdgeColor}{col_a4-a9}
\Edge(a4)(a9)
\renewcommand*{\EdgeColor}{col_a5-a7}
\Edge(a5)(a7)
\renewcommand*{\EdgeColor}{col_a5-a8}
\Edge(a5)(a8)
\renewcommand*{\EdgeColor}{col_a6-a8}
\Edge(a6)(a8)
\renewcommand*{\EdgeColor}{col_a6-a9}
\Edge(a6)(a9)
\renewcommand*{\EdgeColor}{col_a7-a9}
\Edge(a7)(a9)
%
%
\end{tikzpicture}
```

which should still produce the same output as in sage-petersen.pdf when processed by LaTeX.

The '%' were added to avoid doctest errors.


---

Comment by mabshoff created at 2009-05-08 01:32:12

Please use proper identifiers. If this is not ready for review change the summary.

Cheers,

Michael


---

Comment by rbeezer created at 2009-05-08 03:25:58

latex-test-2.patch  has what looks like a few stray unicode characters in the docstring where "vertex_color" is explained.  Those could be edited in a final patch.


---

Comment by rbeezer created at 2009-05-20 15:08:00

Created a new `GraphLatex` object to hold and manipulate options for customizing the latex output of a graph (which was not implemented before).

To test

1.  Make sure your TeX installation has the tkz-graph and tkz-berge packages along with an up-to-date pgf package.

2.  For a graph `g`, `latex(g)` will build a string you can cut/paste into a document.

3.  At the sage command line, `view(g, pdflatex=True)` will create and display a PDF.


The purpose of this patch is to get the infrastructure working, so only one option is implemented.  A wider range of options should follow in a subsequent patch.  Also, see #6089 for details about making this fit into the broader Sage-LaTeX integration.

Apply only the `trac_5975_graph_latex.patch`.  Joint work of Rob Beezer and Fidel Barrera, with assistance from Emily Kirkman.


---

Attachment

Self-contained, don't apply earlier patches.


---

Comment by rbeezer created at 2009-05-20 17:30:06

Scaling code needs work when the layout is horizontal or vertical.  These layouts cause zero dimensions to result in denominators of scaling factors.

fidel.barrera reports two good test cases

`graphs.CompleteBipartiteGraph(0,10)`

`graphs.PathGraph(7)`



---

Comment by rbeezer created at 2009-05-20 22:10:28

Scaling code needed some attention.  One slip with `xfactor` and `yfactor` confused.  Layouts with exactly zero horizontal or vertical ranges are migrated to the midline of the bounding box.  A doctest was added to test the horizontal case.  Apply `trac_5975_graph_latex_scale.patch` on top of the previous patch.


---

Comment by rbeezer created at 2009-05-20 22:11:19

Apply on top of previous


---

Attachment

A doctest failure after applying the above two patches on (roughly) 4.0.rc1


```
sage -t  "devel/sage-main/sage/graphs/graph.py"             
**********************************************************************
File "/home/jason/download/sage-sage-4.0.alpha0.5/devel/sage-main/sage/graphs/graph.py", line 615:
    sage: print g._latex_()
Expected:
    \begin{tikzpicture}
    %
    \definecolor{col_a0}{rgb}{1.0,1.0,1.0}
    \definecolor{col_a1}{rgb}{1.0,1.0,1.0}
    %
    %
    \definecolor{col_lab_a0}{rgb}{0.0,0.0,0.0}
    \definecolor{col_lab_a1}{rgb}{0.0,0.0,0.0}
    %
    %
    \definecolor{col_a0-a1}{rgb}{0.0,0.0,0.0}
    %
    %
    \GraphInit[vstyle=Normal]
    %
    \SetVertexMath
    %
    \SetVertexNoLabel
    %
    \renewcommand*{\VertexLightFillColor}{col_a0}
    \Vertex[x=5.0cm,y=5.0cm]{a0}
    \renewcommand*{\VertexLightFillColor}{col_a1}
    \Vertex[x=0.0cm,y=0.0cm]{a1}
    %
    %
    \AssignVertexLabel{a}{2}{
    \color{col_lab_a0}{$0$},
    \color{col_lab_a1}{$1$}
    }
    %
    %
    \renewcommand*{\EdgeColor}{col_a0-a1}
    \Edge(a0)(a1)
    %
    %
    \end{tikzpicture}
Got:
    Warning: tkz-graph.sty is required.
    Warning: tkz-berge.sty is required.
    \begin{tikzpicture}
    %
    \definecolor{col_a0}{rgb}{1.0,1.0,1.0}
    \definecolor{col_a1}{rgb}{1.0,1.0,1.0}
    %
    %
    \definecolor{col_lab_a0}{rgb}{0.0,0.0,0.0}
    \definecolor{col_lab_a1}{rgb}{0.0,0.0,0.0}
    %
    %
    \definecolor{col_a0-a1}{rgb}{0.0,0.0,0.0}
    %
    %
    \GraphInit[vstyle=Normal]
    %
    \SetVertexMath
    %
    \SetVertexNoLabel
    %
    \renewcommand*{\VertexLightFillColor}{col_a0}
    \Vertex[x=5.0cm,y=5.0cm]{a0}
    \renewcommand*{\VertexLightFillColor}{col_a1}
    \Vertex[x=0.0cm,y=0.0cm]{a1}
    %
    %
    \AssignVertexLabel{a}{2}{
    \color{col_lab_a0}{$0$},
    \color{col_lab_a1}{$1$}
    }
    %
    %
    \renewcommand*{\EdgeColor}{col_a0-a1}
    \Edge(a0)(a1)
    %
    %
    \end{tikzpicture}
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_11
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/jason/download/sage-sage-4.0.alpha0.5/tmp/.doctest_graph.py
	 [148.9 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main/sage/graphs/graph.py"
Total time for all tests: 148.9 seconds
```



---

Comment by jason created at 2009-05-30 04:57:07

I also got similar multiple failures in graph_latex.py.


---

Comment by jason created at 2009-05-30 05:28:47

From a high-level review:

This is fantastic and very, very cool!  rbeezer says he is going to make another pass through things (so I'm changing it to needs work).  After installing the tkz-berge.sty and tkz-graph.sty files into my local tex installation, I could do:


```
sage: G=graphs.PetersenGraph()
sage: view(G, pdflatex=True)
```


and the tikz graph popped up.  This will be really cool when combined with sagetex.

When I just did `view(G)`, a dvi popped up, which did not contain the graph.

I am posting a small referee patch touching the docs on a function or two.


---

Comment by jason created at 2009-05-30 05:31:28

apply on top of previous patches


---

Attachment

Apply only this patch


---

Comment by rbeezer created at 2009-06-02 05:41:38

Consolidated patch attached, including three previous patches, plus better docstrings and a few more required additions that should have been present when adding a new class.


---

Comment by rbeezer created at 2009-06-03 00:24:42

The docstrings here need a bit more work.  Shortly.

Rob


---

Attachment

Apply on top of previous patch


---

Comment by rbeezer created at 2009-06-03 06:26:33

Promised improvements to documentation included in latest patch.  Apply the two most recent patches.


---

Comment by rbeezer created at 2009-06-04 04:15:52

Working through #6089 I've stumbled on one problem.  In `tkz_picture()` the necessary `\usepackage`'s are added on the presumption that they are not present.  However this happens too late, I believe.  The general latex code has probably already built a preamble, so these commands will only surface on the *second* attempt to view the graph (this is indeed what seems to happens experimentally).  And I don't think these two (large) packages should be routinely included always.  So they could be added "by hand" before a view, making the automatic addition pointless.  I can't think of a place where it would be appropriate to add them in before a request to be viewed.  Since the `GraphLatex` object is not always instantiated until needed, it's constructor could even be too late.


---

Attachment

Apply just this patch.


---

Comment by rbeezer created at 2009-06-06 22:53:04

Version 3 is a consolidated patch, bases on 4.0.1.  Should be all ready to go now.

Automatic addition of the correct LaTeX packages has been removed since I can't see where to get them in *before* a preamble is being built.


---

Attachment

aply on top of trac_5975_graph_latex_3.patch


---

Comment by jhpalmieri created at 2009-06-09 03:00:46

I think this is almost ready to go.  I'm attaching a patch with a bunch of trivial fixes (changing "EXAMPLE::" to "EXAMPLES::" lots of places, for instance), one medium fix (since methods beginning with underscore are not included in the reference manual, I moved the docstring from the init method for `GraphLatex` to the class itself), and one more major fix: why not add to the LaTeX preamble when the graph itself is initialized?  My patch does this, but it's easy enough to take out if you think it's a bad idea.  I don't think that adding those two packages will slow any latex process down that much, so I think it's okay.  Oh, and I forgot to add the appropriate strings to avoid_jsmath_..., and this should be done in the same place (this should have no impact on speed).  This last change would make this ticket depend on #6089, but because of your positive review, that shouldn't be a big deal.

Other comments: if have_tkz_graph returns false, then should tkz_picture return an error, or return a string which tells the user why they're not getting a nice picture?  That's what the docstring says, more or less, but that's not what actually happens, I think.  The docstring should not say anything about strings being added to the latex_preamble, by the way.

The following doesn't do anything.  Should it?

```
sage: g = graphs.CompleteBipartiteGraph(1,3)
sage: g.latex_options(tkz_style = 'Art')  
```


In the following, the nodes are overlapping, and it doesn't look good.  It looks like there is room to space them out more:

```
sage: g = graphs.CompleteBipartiteGraph(1,15)
sage: view(g)
```


Finally, I found the documentation not as helpful as it could be, partly because it was scattered around.  I think one solution is to add stuff about "view(g)" and "latex(g)" (etc.) to the "Visualization" section at the top of graph.py.  You might include information about how to test (in Sage) whether your system has tkz-graph and tkz-berge installed, where to get them if they're not installed, and maybe brief descriptions, or at least a list, of the available tkz_styles.  When more options get added, they can go here, too.  You could also expand the documentation in graph_latex.py, either at the top of the file or for the class `GraphLatex`, with some more examples and then a pointer to the Visualization section.  You could also put a "See also" in the docstring for plot and other related methods.


---

Comment by rbeezer created at 2009-06-11 06:23:27

Replying to [comment:18 jhpalmieri]:

Some answers.

1.  Even if the right tkz-graph packages are not present on a system, then I'd still like the user to be able to get out a proper string.  I often use Sage as a sort of Latex assistant - build an object `obj` and run `latex(obj)` and cut/paste the string into a document.  So a warning should be useful, but an error would be too severe I feel.  You ought to be able to get legitimate Latex snippets from Sage, even if you have no tex on your system.  But if you are asking for a rendering in `view()` or the notebook, then errors and warnings are in order.

2.  Yes, I think the documentation is out-of-sync with the above, since I pulled some warnings at the last minute.  I'll fix that.

3.  The code snippet 
>

``` 
sage: g = graphs.CompleteBipartiteGraph(1,3)
sage: g.latex_options(tkz_style = 'Art')  
```


should have no immediate ovious effect or output.  But `latex(g)` should differ if run before and after these commands - afterwards it should have the tkz-graph commands to use the pre-built "Art" style, rather than the default "Normal" style.

4.
> In the following, the nodes are overlapping, and it doesn't look good.  It looks like there is room to space them out more:

```
sage: g = graphs.CompleteBipartiteGraph(1,15)
sage: view(g)
```


Eventually the user will have control over vertex sizes, bounding boxes, and vertex locations.  The intent of this patch is to get the infrastructure right for changing options, then many, more localized changes, will open up more control.  So I think this can slide for now, but this sort of control should be first on the list of changes.



5.
> Finally, I found the documentation not as helpful as it could be, partly because it was scattered around.

Great suggestions.  I'll spruce up the documentation when its not so late in the evening sometime tomorrow night and get up a patch with that, plus other suggestions.

Thanks,
Rob


---

Comment by jhpalmieri created at 2009-06-11 14:52:29

Replying to [comment:19 rbeezer]:
> Replying to [comment:18 jhpalmieri]:
> 
3.  
> The code snippet 
> >

``` 
sage: g = graphs.CompleteBipartiteGraph(1,3)
sage: g.latex_options(tkz_style = 'Art')  
```

> 
> should have no immediate ovious effect or output.  But `latex(g)` should differ if run before and after these commands - afterwards it should have the tkz-graph commands to use the pre-built "Art" style, rather than the default "Normal" style.

I think at the moment it doesn't do this: it only changes the options if the options are None.  `g.set_latex_options()` behaves as it should, but either `g.latex_options()` should behave the same way, or it should not accept any arguments.  The documentation suggests the second choice.


---

Attachment

Information only for reviewer


---

Attachment

Apply only this patch


---

Comment by rbeezer created at 2009-06-12 19:52:12

Hi John,

1.  The initialization of a `GenericGraph` has the necessary `\usepackage` as you included in your patch and I added the jsmath-avoidance string based on the `tikzpicture` latex environment.  This only happens if the right packages are actually installed, so a user's preamble won't get fouled with missing packages.

2.  After several approaches, I finally created a `check_tkz_graph` method.  This acts as a one-time check and warning on a user's environment.  It is called from the routine that actually builds the latex string (`tkz_picture`).  So if a user never tries to render a graph, they never hear about it.  And when they do try, they get a one-time warning if the packages are missing.  This makes doctesting easier - before testing a latex string, we call `check_tkz_graph` as a "random" doctest and possibly warnings are emitted, but are ignored.  Then we actually build the string and it will be free of error messages for comparison to the expected output.  Consequently, `have_tkz_graph` no longer emits messages, just reports the presence of the packages.  This scheme should scale to other packages that might be employed to draw graphs.

3.  `have_tkz_graph` is now a module level function, as it should be, alongside the new `check_tkz_graph`.

4.  I didn't study your original question very carefully about `GenericGraph.latex_options()`.  No, it wasn't really designed to accept options, but the `kwds` argument was needed to make the `@`options decorator work.  I wasn't very happy with `@`options, since it appeared twice, requiring two (identical) edits to keep the defaults in sync.  So, I've removed the decorators and now default options are set in the `GraphLatex` initialization where they need only be edited once.  And so `latex_options()` will no longer accept any arguments.

5.  Documentation:
    (a)  "Visualization" section for graphs has a short blurb and points to the `sage.graphs.graph_latex` module for details.

    (b)  Module level documentation in sage.graphs.graph_latex is meant to be a fairly comprehensive introduction.  I was asked not to pile too much stuff into `sage/graphs/graph.py` since it is so big already, which mostly explains why I've put it here.

    (c)  Authoritative documentation for the actual options is being kept in the docstring for `GraphLatex.set_option()`, which is were options actually get set.  We only have one option right now, but there will be more.  Necessarily some of these will need to refer to the approximately 100-page manual for tkz-graph.

    (d)  I've added pointers to the module documentation from the `plot()` and `plot3d()` methods for graphs.


Delta patch should help you *see* where latest changes are - it begins after your reviewer patch to my version 3.  I wouldn't trust this delta patch as something to apply on an old branch, please do any testing based on the self-contained version 4, which needs to be applied on top of #6089.

Thanks,
Rob


---

Comment by jhpalmieri created at 2009-06-12 21:07:00

Looks good.  I'm attaching a referee's patch with trivial fixes. Now, if I don't have tkz-graph and/or tkz-berge installed, running `view(g)` produces a warning and then a dvi file with gibberish (if from the command-line) or an error about an unknown environment tikzpicture (in the notebook).  I don't think this is terrible since the warning is printed, but should latex do anything at all in this case, or do something more innocuous?  I'm willing to leave it as is, and then if you want, you can change it in a future revision.

If my little patch is okay, change to a positive review.


---

Comment by jhpalmieri created at 2009-06-12 21:07:38

apply on top of trac_5975_graph_latex_4.patch


---

Attachment

Hi John,

Thanks for the quick review and the improvements.  Fixes in reviewer patch are very welcome.

I've given a lot of thought about how best to react to "missing" parts of a user's environment.  As you've seen, it makes doctesting difficult.  So at the moment, I'm content with the one-time warning and whatever goes boom after that.  ;-)   It did make it easier in my mind to separate a check/warning from an existence test, even though they are very similar.

Two things I did think about though.  `\typeout` in TeX will insert text into the log and/or at the console.  So a message just before a potential problem could happen this way.  Another approach would be to put some TeX comments right before a potential problem.  These might locate information close to where folks might investigate, especially in a %latex_debug cell.  But hopefully thorough documentation and a warning will get folks on track.  I'll add some more protections if they come to me, but I'm ready to cut this one loose.

Minh:  ping me if there isn't a graphic example here for the release tour.  ;-)

Release manager: Apply #6089, revision 4 patch, then latest reviewer patch.  Thanks.


---

Comment by jason created at 2009-06-13 14:15:42

Can I make one small suggestion?

This line:

```
check_tkz_graph()  # random - depends on TeX installation 
```

ought to be

```
check_tkz_graph()  # optional - depends on the TeX installation containing <whatever tex files you need>
```


We really don't like #random doctests if we can help it, and this doctest is really testing the existence of an optional program.  I guess one argument against this is that it is not testing the installation of an optional spkg.

Since we have at least one other spkg installing .sty files (sagetex), maybe (in a different ticket) we could have a small spkg that installs the needed .sty files for this into the sage local tex tree.


---

Comment by rbeezer created at 2009-06-13 21:36:29

Hi Jason,

The purpose of the line in question is not really a doctest of the existence of the packages.

The function `check_tkz_graph()` will emit a warning *once* per session, if needed, and then be silent.  In order to doctest the latex output, I need to be sure that the warning doesn't get mixed in.  So I call this function in the doctest, which *may* produce a warning.  Then the latex output will be "pure."

So I need to be certain this line runs, and I don't want to test its (variable) output.  If it is tagged "optional" will it always be run in testing, no matter what?

In any event, if there is a change here, I'll make it as part of some other revision, so I don't want this to hold up getting this merged.

Rob

Replying to [comment:24 jason]:
> Can I make one small suggestion?
> 
> This line:
> {{{
> check_tkz_graph()  # random - depends on TeX installation 
> }}}
> ought to be
> {{{
> check_tkz_graph()  # optional - depends on the TeX installation containing <whatever tex files you need>
> }}}
> 
> We really don't like #random doctests if we can help it, and this doctest is really testing the existence of an optional program.  I guess one argument against this is that it is not testing the installation of an optional spkg.
> 
> Since we have at least one other spkg installing .sty files (sagetex), maybe (in a different ticket) we could have a small spkg that installs the needed .sty files for this into the sage local tex tree.


---

Comment by jason created at 2009-06-13 21:50:39

Replying to [comment:25 rbeezer]:
> Hi Jason,
> 
> The purpose of the line in question is not really a doctest of the existence of the packages.
> 
> The function `check_tkz_graph()` will emit a warning *once* per session, if needed, and then be silent.  In order to doctest the latex output, I need to be sure that the warning doesn't get mixed in.  So I call this function in the doctest, which *may* produce a warning.  Then the latex output will be "pure."
> 
> So I need to be certain this line runs, and I don't want to test its (variable) output.  If it is tagged "optional" will it always be run in testing, no matter what?


ah, good point.  If it's tagged optional, it won't always run.

I retract my comment.

The right way to do something like this is to disable the warnings for that module before the doctest.  But that's probably the subject of another ticket, as I don't have time to make the patch now, and I'd rather not hold this up any more.


---

Comment by ncalexan created at 2009-06-13 22:33:07

Resolution: fixed


---

Comment by was created at 2009-06-14 10:23:17

> ah, good point. If it's tagged optional, it won't always run.

More precisely, it will never ever run, except in the exceedingly rare case anybody every runs any optional doctests (which is basically never).


---

Comment by rbeezer created at 2009-06-15 04:50:38

Sample output for release tour


---

Attachment

Minh,

For the release tour.

See PNG screenshot of PDF output.  Complete code required to get the PDF:


```
g = graphs.PetersenGraph()
g.set_latex_options(tkz_style='Art')
view(g, pdflatex=True)
```


Mostly this patch puts in place the infrastructure to make many of the features of the the tkz-graph latex package available.  Only one option (tkz_style) is actually implemented at the moment - more will follow.
