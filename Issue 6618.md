# Issue 6618: Follow up on #6591: make tightpage work even in the notebook

archive/issues_006618.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat @rbeezer fidelbarrera @jhpalmieri @fchapoton\n\nKeywords: view, pdflatex, tightpage, tikz\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6618\n\n",
    "created_at": "2009-07-25T14:52:25Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Follow up on #6591: make tightpage work even in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6618",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat @rbeezer fidelbarrera @jhpalmieri @fchapoton

Keywords: view, pdflatex, tightpage, tikz



Issue created by migration from https://trac.sagemath.org/ticket/6618





---

archive/issue_comments_054123.json:
```json
{
    "body": "Can you clarify what you want to do here?  The pictures produced by \"view\" in the notebook already look cropped to me.  Try this example:\n\n```\nfrom sage.misc.latex import latex_examples\nlatex.add_to_preamble(\"\\\\usepackage{tkz-graph}\")\nlatex.add_to_jsmath_avoid_list(\"tikzpicture\")\nview(latex_examples.graph())\n```\n",
    "created_at": "2009-07-25T20:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54123",
    "user": "https://github.com/jhpalmieri"
}
```

Can you clarify what you want to do here?  The pictures produced by "view" in the notebook already look cropped to me.  Try this example:

```
from sage.misc.latex import latex_examples
latex.add_to_preamble("\\usepackage{tkz-graph}")
latex.add_to_jsmath_avoid_list("tikzpicture")
view(latex_examples.graph())
```




---

archive/issue_comments_054124.json:
```json
{
    "body": "Replying to [comment:1 jhpalmieri]:\n> Can you clarify what you want to do here?  The pictures produced by \"view\" in the notebook already look cropped to me.  Try this example:\n> {{{\n> from sage.misc.latex import latex_examples\n> latex.add_to_preamble(\"\\\\usepackage{tkz-graph}\")\n> latex.add_to_jsmath_avoid_list(\"tikzpicture\")\n> view(latex_examples.graph())\n> }}}\n\nThe point is that tightpage crops if the picture is small, but also does *not* crop to the page size if the picture is big.\nIn other words, it really sets the page size to be the size of the picture.\n\nI have a apparently working patch. I still need to test it further and document it this time :-)",
    "created_at": "2009-07-25T20:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54124",
    "user": "https://github.com/nthiery"
}
```

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

archive/issue_comments_054125.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-25T20:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54125",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_054126.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-20T09:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54126",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054127.json:
```json
{
    "body": "Feedback welcome: Anne seems to have an issue with it (see http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/c46b8a2fcbb5875a).\n\nAlso, the notebook seems to crop the resulting image.",
    "created_at": "2010-02-20T09:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54127",
    "user": "https://github.com/nthiery"
}
```

Feedback welcome: Anne seems to have an issue with it (see http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/c46b8a2fcbb5875a).

Also, the notebook seems to crop the resulting image.



---

archive/issue_comments_054128.json:
```json
{
    "body": "> Also, the notebook seems to crop the resulting image.\n\nOnly when pdflatex=False; for details, see the doctests of view. Maybe tightpage should impose pdflatex=True.",
    "created_at": "2010-02-20T10:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54128",
    "user": "https://github.com/nthiery"
}
```

> Also, the notebook seems to crop the resulting image.

Only when pdflatex=False; for details, see the doctests of view. Maybe tightpage should impose pdflatex=True.



---

archive/issue_comments_054129.json:
```json
{
    "body": "I think that tightpage should impose pdflatex = True, because producing badly cropped images is bad.  One other comment (for now -- I may have more later): in line 1264\n\n```diff\n \t1261\t    if tightpage: \n \t1262\t        title = '' \n \t1263\t        extra_preamble += '\\\\usepackage[tightpage,active]{preview}\\\\PreviewEnvironment{page}' \n \t1264\t        math_left  = '\\\\begin{page}$\\displaystyle' \n \t1265\t        math_right = '$\\\\end{page}' \n```\n\nadd a space after \"displaystyle\".  On my computer:\n\n```\nsage: CB = CrystalOfLetters(['B',2]) \nsage: latex(CB)\ndot2tex not available.  Install after running 'sage -sh'\ndot2tex not available.  Install after running 'sage -sh'\nNone\n```\n\nSince `latex(CB)` returns `None`, then when I try \n\n```\nsage: view(CB, tightpage = True)\n```\n\nit forms a latex document containing\n\n```\n\\begin{page}$\\displaystyleNone$\\end{page}\n```\n\nThis leads to an error.  A space after \"displaystyle\" would fix this.",
    "created_at": "2010-02-20T17:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54129",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_comments_054130.json:
```json
{
    "body": "Two more comments, and otherwise I think this looks okay: first, it needs to be rebased against 4.3.3 (alpha0 or later), because of #8219.  Second, the issue with the cropped images seems to be the fault of \"convert\": if you create a dvi file using tightpage, say by using \"debug=True\" in the view command and cutting and pasting the latex, and then if you run dvips on it, then run \n\n```\nconvert -density 150x150 -trim test.ps test.png\n```\n\nit's badly cropped.  The postscript file is actually okay: if you run ps2pdf on it, the pdf file looks good.  So maybe it's a bug in \"convert\"?\n\nFor a future ticket: should we consider changing the default so that pdflatex is True rather than False?",
    "created_at": "2010-02-20T21:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54130",
    "user": "https://github.com/jhpalmieri"
}
```

Two more comments, and otherwise I think this looks okay: first, it needs to be rebased against 4.3.3 (alpha0 or later), because of #8219.  Second, the issue with the cropped images seems to be the fault of "convert": if you create a dvi file using tightpage, say by using "debug=True" in the view command and cutting and pasting the latex, and then if you run dvips on it, then run 

```
convert -density 150x150 -trim test.ps test.png
```

it's badly cropped.  The postscript file is actually okay: if you run ps2pdf on it, the pdf file looks good.  So maybe it's a bug in "convert"?

For a future ticket: should we consider changing the default so that pdflatex is True rather than False?



---

archive/issue_comments_054131.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-20T21:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54131",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_054132.json:
```json
{
    "body": "Attachment [trac_6618_view_viewer_tightpage-followup-nt.patch](tarball://root/attachments/some-uuid/ticket6618/trac_6618_view_viewer_tightpage-followup-nt.patch) by @mwhansen created at 2012-08-04 04:24:49\n\nI've rebased this patch and made it so that engine is set to 'pdflatex' if tightpage=True is enabled.",
    "created_at": "2012-08-04T04:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54132",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6618_view_viewer_tightpage-followup-nt.patch](tarball://root/attachments/some-uuid/ticket6618/trac_6618_view_viewer_tightpage-followup-nt.patch) by @mwhansen created at 2012-08-04 04:24:49

I've rebased this patch and made it so that engine is set to 'pdflatex' if tightpage=True is enabled.



---

archive/issue_comments_054133.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-04T04:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54133",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054134.json:
```json
{
    "body": "On my OS X machine, running doctests opens up an external viewer for PDF files. Also, doctests fail because I don't have dot2tex installed (this is easy to fix). For the external viewer issue, maybe we should just rip out these doctests:\n\n```diff\ndiff --git a/sage/misc/latex.py b/sage/misc/latex.py\n--- a/sage/misc/latex.py\n+++ b/sage/misc/latex.py\n@@ -2048,17 +2048,6 @@ def view(objects, title='SAGE', debug=Fa\n         <html><span class=\"math\">\\newcommand{\\Bold}[1]{\\mathbf{#1}}x 2</span></html>\n         sage: sage.misc.latex.EMBEDDED_MODE = False\n \n-        sage: CB = CrystalOfLetters(['B',5])\n-        sage: view(CB, tightpage = True, viewer = \"pdf\")\n-\n-        sage: CB = CrystalOfLetters(['B',5])\n-        sage: view(CB, tightpage = True, pdflatex = True)\n-\n-        sage: g = sage.categories.category.category_graph() # long time\n-        sage: g.set_latex_options(format = \"dot2tex\")       # long time\n-        sage: view(g, tightpage=True, pdflatex = True)      # long time\n-\n-\n     TESTS::\n \n         sage: from sage.misc.latex import _run_latex_, _latex_file_\n```\n\nOther suggestions?\n\nI also still some cropping issues in the notebook, say with this code:\n\n```\ng = graphs.BidiakisCube()\nlatex.add_to_jsmath_avoid_list('tikz')\nview(g, tightpage=True)\n```\n\nBut maybe that's not a big deal.",
    "created_at": "2012-08-20T18:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54134",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_comments_054135.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-01-03T20:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54135",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_054136.json:
```json
{
    "body": "Changing component from interfaces to notebook.",
    "created_at": "2015-06-23T13:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54136",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from interfaces to notebook.



---

archive/issue_comments_054137.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54137",
    "user": "https://github.com/mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_054138.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54138",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054139.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-25T09:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54139",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054140.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-15T15:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6618#issuecomment-54140",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
