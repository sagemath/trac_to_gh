# Issue 6022: [with patch, needs review] latex.py: if dvipng fails, use dvips and convert instead

archive/issues_006022.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nCC:  @rbeezer fidelbarrera\n\nOn systems where dvipng is installed: If in a %latex cell, dvipng fails to produce a good picture, you get basically nothing.  With this patch, this failure is detected, and dvips and convert are then used instead. The failure is detected by running dvipng with the '--picky' option; with this turned on, if dvipng produces any warnings or errors, no png file is produced.  The code then sees if there is a png file; if not, it runs dvips and convert.\n\nThis patch also fixes a long-standing complaint of William's: now when there is a problem in a %latex cell, the .log file is printed automatically, instead of just printing the message \"An error occurred.\"\n\nApply on top of the patch at #6012.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6022\n\n",
    "created_at": "2009-05-11T22:50:17Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] latex.py: if dvipng fails, use dvips and convert instead",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6022",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

CC:  @rbeezer fidelbarrera

On systems where dvipng is installed: If in a %latex cell, dvipng fails to produce a good picture, you get basically nothing.  With this patch, this failure is detected, and dvips and convert are then used instead. The failure is detected by running dvipng with the '--picky' option; with this turned on, if dvipng produces any warnings or errors, no png file is produced.  The code then sees if there is a png file; if not, it runs dvips and convert.

This patch also fixes a long-standing complaint of William's: now when there is a problem in a %latex cell, the .log file is printed automatically, instead of just printing the message "An error occurred."

Apply on top of the patch at #6012.


Issue created by migration from https://trac.sagemath.org/ticket/6022





---

archive/issue_comments_047871.json:
```json
{
    "body": "By the way: to test this,\n\n```\nlatex.extra_preamble('\\\\usepackage{tkz-graph}')\n```\nand (taken from [http://altermundus.com/pages/graph.html](http://altermundus.com/pages/graph.html)):\n\n```\n%latex\n\\begin{tikzpicture}[node distance   = 4 cm]\n     \\GraphInit[vstyle=Shade]\n     \\tikzset{LabelStyle/.style =   {draw,\n                                     fill  = yellow,\n                                     text  = red}}\n     \\Vertex{A}\n     \\EA(A){B}\n     \\EA(B){C}\n     \\tikzset{node distance   = 8 cm}% modifie la distance entre les nodes\n     \\NO(B){D}\n     \\Edge[label=1](B)(D)\n     \\tikzset{EdgeStyle/.append style = {bend left}}\n     \\Edge[label=4](A)(B)\n     \\Edge[label=5](B)(A)\n     \\Edge[label=6](B)(C)\n     \\Edge[label=7](C)(B)\n     \\Edge[label=2](A)(D)\n     \\Edge[label=3](D)(C)\n  \\end{tikzpicture}\n```\nBefore the patch, I just get a little black blob.  After the patch, I get a nice picture.  (This assume that you have the tkz-graph package installed, as well as the most recent version of pgf.)",
    "created_at": "2009-05-11T22:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6022#issuecomment-47871",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_comments_047872.json:
```json
{
    "body": "Here's a test that will work with a \"vanilla\" latex installation:\n\n```\n%latex\n\\begin{pspicture}(0,-4)(14,0)\n  \\psline{-}(0,0)(0,-4)\n  \\psline[linewidth=2pt]{-}(0,0)(1,-3)\n  \\qdisk(1,-3){3pt}\n  \\psarc{-}(0,0){0.6}{270}{292}\n  \\psline{->}(1,-3.3)(1,-4)\n  \\psline{->}(1.1,-2.7)(0.85,-1.95)\n  \\psline{-}(5,0)(5,-4)\n  \\psline[linewidth=2pt]{-}(5,0)(6,-3)\n  \\qdisk(6,-3){3pt}\n  \\psarc{-}(5,0){0.6}{270}{292}\n  \\psarc{-}(5,0){3.2}{270}{290}\n\\end{pspicture}\n```\nThat is, it won't work before applying that patch: I get no output from this.  With the patch, it produces a picture.",
    "created_at": "2009-05-12T00:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6022#issuecomment-47872",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_comments_047873.json:
```json
{
    "body": "Attachment [trac_6022.patch](tarball://root/attachments/some-uuid/ticket6022/trac_6022.patch) by @rbeezer created at 2009-05-12 05:02:25\n\nLooks real good - this greatly expands the possibilities for latex packages that can be employed, and the resulting possibilities for latex output.  Works as advertised - tested with various combinations of %latex, %pdflatex, missing dvipng, missing convert, and various types of input.  Passes tests on sage/misc/latex.py.\n\nApply after the patch at #6012.",
    "created_at": "2009-05-12T05:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6022#issuecomment-47873",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_6022.patch](tarball://root/attachments/some-uuid/ticket6022/trac_6022.patch) by @rbeezer created at 2009-05-12 05:02:25

Looks real good - this greatly expands the possibilities for latex packages that can be employed, and the resulting possibilities for latex output.  Works as advertised - tested with various combinations of %latex, %pdflatex, missing dvipng, missing convert, and various types of input.  Passes tests on sage/misc/latex.py.

Apply after the patch at #6012.



---

archive/issue_comments_047874.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-13T18:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6022#issuecomment-47874",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_014146.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-13T18:12:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6022",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6022#event-14146"
}
```



---

archive/issue_comments_047875.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-13T18:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6022#issuecomment-47875",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_events_014147.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-13T18:12:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6022",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6022#event-14147"
}
```
