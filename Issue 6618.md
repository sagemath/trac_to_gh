# Issue 6618: Follow up on #6591: make tightpage work even in the notebook

Issue created by migration from https://trac.sagemath.org/ticket/6618

Original creator: nthiery

Original creation time: 2009-07-25 14:52:25

Assignee: nthiery

CC:  sage-combinat rbeezer fidelbarrera jhpalmieri chapoton

Keywords: view, pdflatex, tightpage, tikz




---

Comment by jhpalmieri created at 2009-07-25 20:13:21

Can you clarify what you want to do here?  The pictures produced by "view" in the notebook already look cropped to me.  Try this example:

```
from sage.misc.latex import latex_examples
latex.add_to_preamble("\\usepackage{tkz-graph}")
latex.add_to_jsmath_avoid_list("tikzpicture")
view(latex_examples.graph())
```



---

Comment by nthiery created at 2009-07-25 20:31:34

Replying to [comment:1 jhpalmieri]:
> Can you clarify what you want to do here?  The pictures produced by "view" in the notebook already look cropped to me.  Try this example:
> {{{
> from sage.misc.latex import latex_examples
> latex.add_to_preamble("\\usepackage{tkz-graph}")
> latex.add_to_jsmath_avoid_list("tikzpicture")
> view(latex_examples.graph())
> }}}

The point is that tightpage crops if the picture is small, but also does *not* crop to the page size if the picture is big.
In other words, it really sets the page size to be the size of the picture.

I have a apparently working patch. I still need to test it further and document it this time :-)


---

Comment by nthiery created at 2009-07-25 20:31:45

Changing status from new to assigned.


---

Comment by nthiery created at 2010-02-20 09:55:54

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-02-20 09:55:54

Feedback welcome: Anne seems to have an issue with it (see http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/c46b8a2fcbb5875a).

Also, the notebook seems to crop the resulting image.


---

Comment by nthiery created at 2010-02-20 10:11:35

> Also, the notebook seems to crop the resulting image.

Only when pdflatex=False; for details, see the doctests of view. Maybe tightpage should impose pdflatex=True.


---

Comment by jhpalmieri created at 2010-02-20 17:00:44

I think that tightpage should impose pdflatex = True, because producing badly cropped images is bad.  One other comment (for now -- I may have more later): in line 1264

```diff
 	1261	    if tightpage: 
 	1262	        title = '' 
 	1263	        extra_preamble += '\\usepackage[tightpage,active]{preview}\\PreviewEnvironment{page}' 
 	1264	        math_left  = '\\begin{page}$\displaystyle' 
 	1265	        math_right = '$\\end{page}' 
```

add a space after "displaystyle".  On my computer:

```
sage: CB = CrystalOfLetters(['B',2]) 
sage: latex(CB)
dot2tex not available.  Install after running 'sage -sh'
dot2tex not available.  Install after running 'sage -sh'
None
```

Since `latex(CB)` returns `None`, then when I try 

```
sage: view(CB, tightpage = True)
```

it forms a latex document containing

```
\begin{page}$\displaystyleNone$\end{page}
```

This leads to an error.  A space after "displaystyle" would fix this.


---

Comment by jhpalmieri created at 2010-02-20 21:00:01

Two more comments, and otherwise I think this looks okay: first, it needs to be rebased against 4.3.3 (alpha0 or later), because of #8219.  Second, the issue with the cropped images seems to be the fault of "convert": if you create a dvi file using tightpage, say by using "debug=True" in the view command and cutting and pasting the latex, and then if you run dvips on it, then run 

```
convert -density 150x150 -trim test.ps test.png
```

it's badly cropped.  The postscript file is actually okay: if you run ps2pdf on it, the pdf file looks good.  So maybe it's a bug in "convert"?

For a future ticket: should we consider changing the default so that pdflatex is True rather than False?


---

Comment by jhpalmieri created at 2010-02-20 21:00:01

Changing status from needs_review to needs_work.


---

Attachment

I've rebased this patch and made it so that engine is set to 'pdflatex' if tightpage=True is enabled.


---

Comment by mhansen created at 2012-08-04 04:24:49

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2012-08-20 18:37:11

On my OS X machine, running doctests opens up an external viewer for PDF files. Also, doctests fail because I don't have dot2tex installed (this is easy to fix). For the external viewer issue, maybe we should just rip out these doctests:

```diff
diff --git a/sage/misc/latex.py b/sage/misc/latex.py
--- a/sage/misc/latex.py
+++ b/sage/misc/latex.py
@@ -2048,17 +2048,6 @@ def view(objects, title='SAGE', debug=Fa
         <html><span class="math">\newcommand{\Bold}[1]{\mathbf{#1}}x 2</span></html>
         sage: sage.misc.latex.EMBEDDED_MODE = False
 
-        sage: CB = CrystalOfLetters(['B',5])
-        sage: view(CB, tightpage = True, viewer = "pdf")
-
-        sage: CB = CrystalOfLetters(['B',5])
-        sage: view(CB, tightpage = True, pdflatex = True)
-
-        sage: g = sage.categories.category.category_graph() # long time
-        sage: g.set_latex_options(format = "dot2tex")       # long time
-        sage: view(g, tightpage=True, pdflatex = True)      # long time
-
-
     TESTS::
 
         sage: from sage.misc.latex import _run_latex_, _latex_file_
```

Other suggestions?

I also still some cropping issues in the notebook, say with this code:

```
g = graphs.BidiakisCube()
latex.add_to_jsmath_avoid_list('tikz')
view(g, tightpage=True)
```

But maybe that's not a big deal.


---

Comment by kcrisman created at 2013-01-03 20:04:01

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2015-06-23 13:50:00

Changing component from interfaces to notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2020-08-25 09:25:46

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-09-15 15:58:55

Resolution: invalid
