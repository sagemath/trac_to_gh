# Issue 1404: [with patch] bug in %latex feature in the notebook

Issue created by migration from https://trac.sagemath.org/ticket/1404

Original creator: was

Original creation time: 2007-12-05 18:13:06

Assignee: boothby

From F Clark:


```
A problem with latex processing in a notebook (otherwise a brilliant
feature):


Evaluating the input cell:

%latex

$y=\sin x$

% end of input

tries to process the TeX file:

\documentclass{article}\usepackage{fullpage}\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}\usepackage{graphicx}\usepackage{pstricks}
\pagestyle{empty}
\begin{document}

$y=\sin x$

% end of input\end{document}

but pdfTeX fails, because the \end{document} gets commented out.  The
reason is that  '\\end{document}' is tagged on to the end of the input
text rather than '\n\\end{document}'.

The following would seem to solve the problem:

diff -r 7110a20969c8 sage/misc/latex.py
--- a/sage/misc/latex.py        Mon Dec 03 22:27:57 2007 -0800
+++ b/sage/misc/latex.py        Tue Dec 04 22:11:15 2007 +0000
@@ -203,7 +203,7 @@ class Latex:
        if self.__slide:
            O.write('\n\n\\end{document}')
        else:
-            O.write('\\end{document}\n')
+            O.write('\n\\end{document}\n')

        O.close()
        if not debug:
```



---

Comment by mabshoff created at 2007-12-05 19:20:32

Hmm, since now both branches of the if case are identical except the additional newline couldn't we make collapse the if statement?

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2007-12-15 13:27:47

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 13:27:47

Merged in 2.9.rc0.
