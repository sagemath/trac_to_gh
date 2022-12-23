# Issue 6022: [with patch, needs review] latex.py: if dvipng fails, use dvips and convert instead

Issue created by migration from https://trac.sagemath.org/ticket/6022

Original creator: jhpalmieri

Original creation time: 2009-05-11 22:50:17

Assignee: jhpalmieri

CC:  rbeezer fidelbarrera

On systems where dvipng is installed: If in a %latex cell, dvipng fails to produce a good picture, you get basically nothing.  With this patch, this failure is detected, and dvips and convert are then used instead. The failure is detected by running dvipng with the '--picky' option; with this turned on, if dvipng produces any warnings or errors, no png file is produced.  The code then sees if there is a png file; if not, it runs dvips and convert.

This patch also fixes a long-standing complaint of William's: now when there is a problem in a %latex cell, the .log file is printed automatically, instead of just printing the message "An error occurred."

Apply on top of the patch at #6012.



---

Comment by jhpalmieri created at 2009-05-11 22:54:16

By the way: to test this,

```
latex.extra_preamble('\\usepackage{tkz-graph}')
```

and (taken from [http://altermundus.com/pages/graph.html](http://altermundus.com/pages/graph.html)):

```
%latex
\begin{tikzpicture}[node distance   = 4 cm]
     \GraphInit[vstyle=Shade]
     \tikzset{LabelStyle/.style =   {draw,
                                     fill  = yellow,
                                     text  = red}}
     \Vertex{A}
     \EA(A){B}
     \EA(B){C}
     \tikzset{node distance   = 8 cm}% modifie la distance entre les nodes
     \NO(B){D}
     \Edge[label=1](B)(D)
     \tikzset{EdgeStyle/.append style = {bend left}}
     \Edge[label=4](A)(B)
     \Edge[label=5](B)(A)
     \Edge[label=6](B)(C)
     \Edge[label=7](C)(B)
     \Edge[label=2](A)(D)
     \Edge[label=3](D)(C)
  \end{tikzpicture}
```

Before the patch, I just get a little black blob.  After the patch, I get a nice picture.  (This assume that you have the tkz-graph package installed, as well as the most recent version of pgf.)


---

Comment by jhpalmieri created at 2009-05-12 00:35:09

Here's a test that will work with a "vanilla" latex installation:

```
%latex
\begin{pspicture}(0,-4)(14,0)
  \psline{-}(0,0)(0,-4)
  \psline[linewidth=2pt]{-}(0,0)(1,-3)
  \qdisk(1,-3){3pt}
  \psarc{-}(0,0){0.6}{270}{292}
  \psline{->}(1,-3.3)(1,-4)
  \psline{->}(1.1,-2.7)(0.85,-1.95)
  \psline{-}(5,0)(5,-4)
  \psline[linewidth=2pt]{-}(5,0)(6,-3)
  \qdisk(6,-3){3pt}
  \psarc{-}(5,0){0.6}{270}{292}
  \psarc{-}(5,0){3.2}{270}{290}
\end{pspicture}
```

That is, it won't work before applying that patch: I get no output from this.  With the patch, it produces a picture.


---

Attachment

Looks real good - this greatly expands the possibilities for latex packages that can be employed, and the resulting possibilities for latex output.  Works as advertised - tested with various combinations of %latex, %pdflatex, missing dvipng, missing convert, and various types of input.  Passes tests on sage/misc/latex.py.

Apply after the patch at #6012.


---

Comment by mabshoff created at 2009-05-13 18:12:51

Resolution: fixed


---

Comment by mabshoff created at 2009-05-13 18:12:51

Merged in Sage 4.0.alpha0.

Cheers,

Michael
