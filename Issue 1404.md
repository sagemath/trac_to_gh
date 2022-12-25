# Issue 1404: [with patch] bug in %latex feature in the notebook

archive/issues_001404.json:
```json
{
    "body": "Assignee: boothby\n\nFrom F Clark:\n\n\n```\nA problem with latex processing in a notebook (otherwise a brilliant\nfeature):\n\n\nEvaluating the input cell:\n\n%latex\n\n$y=\\sin x$\n\n% end of input\n\ntries to process the TeX file:\n\n\\documentclass{article}\\usepackage{fullpage}\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{amsfonts}\\usepackage{graphicx}\\usepackage{pstricks}\n\\pagestyle{empty}\n\\begin{document}\n\n$y=\\sin x$\n\n% end of input\\end{document}\n\nbut pdfTeX fails, because the \\end{document} gets commented out.  The\nreason is that  '\\\\end{document}' is tagged on to the end of the input\ntext rather than '\\n\\\\end{document}'.\n\nThe following would seem to solve the problem:\n\ndiff -r 7110a20969c8 sage/misc/latex.py\n--- a/sage/misc/latex.py        Mon Dec 03 22:27:57 2007 -0800\n+++ b/sage/misc/latex.py        Tue Dec 04 22:11:15 2007 +0000\n@@ -203,7 +203,7 @@ class Latex:\n        if self.__slide:\n            O.write('\\n\\n\\\\end{document}')\n        else:\n-            O.write('\\\\end{document}\\n')\n+            O.write('\\n\\\\end{document}\\n')\n\n        O.close()\n        if not debug:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1404\n\n",
    "created_at": "2007-12-05T18:13:06Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch] bug in %latex feature in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1404",
    "user": "https://github.com/williamstein"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/1404





---

archive/issue_comments_009040.json:
```json
{
    "body": "Hmm, since now both branches of the if case are identical except the additional newline couldn't we make collapse the if statement?\n\nCheers,\n\nMichael",
    "created_at": "2007-12-05T19:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1404#issuecomment-9040",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, since now both branches of the if case are identical except the additional newline couldn't we make collapse the if statement?

Cheers,

Michael



---

archive/issue_comments_009041.json:
```json
{
    "body": "Attachment [trac-1404.patch](tarball://root/attachments/some-uuid/ticket1404/trac-1404.patch) by @williamstein created at 2007-12-15 13:09:08",
    "created_at": "2007-12-15T13:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1404#issuecomment-9041",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1404.patch](tarball://root/attachments/some-uuid/ticket1404/trac-1404.patch) by @williamstein created at 2007-12-15 13:09:08



---

archive/issue_events_001552.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-15T13:27:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1404",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1404#event-1552"
}
```



---

archive/issue_comments_009042.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T13:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1404#issuecomment-9042",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009043.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T13:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1404#issuecomment-9043",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.
