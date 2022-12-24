# Issue 4435: %latex -- don't use \usepackage{fullpage}

archive/issues_004435.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\n\n\nOn Mon, Nov 3, 2008 at 7:57 PM, William Stein <wstein@gmail.com> wrote:\n>\n> On Mon, Nov 3, 2008 at 5:23 PM, Matthew J <matdjj@gmail.com> wrote:\n>>\n>> If anyone else comes across this problem and installing gs and\n>> imagemagick does not solve it, I also had to install tetex-extra.\n>>\n>>\n>> I realized when I was getting the error: fullpage.sty could not be\n>> found.\n>\n> Thanks.  Maybe we should get rid of dependence on fullpage.sty,\n> since probably there is an easy direct way to do about the same thing.\n>\n> William\n>\n\nThis should do something pretty close:\n\n%% margins\n\\oddsidemargin  0.0in\n\\evensidemargin 0.0in\n\\textwidth      6.45in\n\\topmargin  0.0in\n\\headheight 0.0in\n\\headsep    0.0in\n\\textheight 9.0in\n\n-cc\n- Hide quoted text -\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4435\n\n",
    "created_at": "2008-11-04T04:55:49Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "%latex -- don't use \\usepackage{fullpage}",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4435",
    "user": "was"
}
```
Assignee: cwitty


```


On Mon, Nov 3, 2008 at 7:57 PM, William Stein <wstein@gmail.com> wrote:
>
> On Mon, Nov 3, 2008 at 5:23 PM, Matthew J <matdjj@gmail.com> wrote:
>>
>> If anyone else comes across this problem and installing gs and
>> imagemagick does not solve it, I also had to install tetex-extra.
>>
>>
>> I realized when I was getting the error: fullpage.sty could not be
>> found.
>
> Thanks.  Maybe we should get rid of dependence on fullpage.sty,
> since probably there is an easy direct way to do about the same thing.
>
> William
>

This should do something pretty close:

%% margins
\oddsidemargin  0.0in
\evensidemargin 0.0in
\textwidth      6.45in
\topmargin  0.0in
\headheight 0.0in
\headsep    0.0in
\textheight 9.0in

-cc
- Hide quoted text -
```


Issue created by migration from https://trac.sagemath.org/ticket/4435





---

archive/issue_comments_032601.json:
```json
{
    "body": "Here's a patch.  (Does anyone use \"%slide\"?  The output is pretty ugly, seems to me.)",
    "created_at": "2009-03-22T22:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32601",
    "user": "jhpalmieri"
}
```

Here's a patch.  (Does anyone use "%slide"?  The output is pretty ugly, seems to me.)



---

archive/issue_comments_032602.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-22T22:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32602",
    "user": "jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032603.json:
```json
{
    "body": "Changing assignee from cwitty to jhpalmieri.",
    "created_at": "2009-03-22T22:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32603",
    "user": "jhpalmieri"
}
```

Changing assignee from cwitty to jhpalmieri.



---

archive/issue_comments_032604.json:
```json
{
    "body": "> Here's a patch. (Does anyone use \"%slide\"? The output is pretty ugly, seems to me.) \n\nI have -- it allows one to use anything in latex beamer (in theory), which is pretty (in theory).  I haven't used %slide in a long time though, since I just use TinyMCE now.",
    "created_at": "2009-03-29T16:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32604",
    "user": "was"
}
```

> Here's a patch. (Does anyone use "%slide"? The output is pretty ugly, seems to me.) 

I have -- it allows one to use anything in latex beamer (in theory), which is pretty (in theory).  I haven't used %slide in a long time though, since I just use TinyMCE now.



---

archive/issue_comments_032605.json:
```json
{
    "body": "Incidentally %slide takes a LONG time to tex any given slide on OS X... This has nothing to do with this patch (just an observation).",
    "created_at": "2009-03-29T16:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32605",
    "user": "was"
}
```

Incidentally %slide takes a LONG time to tex any given slide on OS X... This has nothing to do with this patch (just an observation).



---

archive/issue_comments_032606.json:
```json
{
    "body": "This patch causes doctest failures in the file it patches on sage.math! :)\n\n```\nsage -t -long \"devel/sage/sage/misc/latex.py\"               \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc0/devel/sage/sage/misc/latex.py\", line 368:\n    sage: _latex_file_(3, title=\"The number three\")\nExpected:\n    '\\\\documentclass{article}\\\\usepackage{fullpage}\\\\usepackage{amsmath}\n\\n\\\\usepackage{amssymb}\\n\\\\usepackage{amsfonts}\\\\usepackage{graphicx}\n\\\\usepackage{pstricks}\\\\pagestyle{empty}\\n\\n\\\\begin{document}\\n\\\\begin{center}\n{\\\\Large\\\\bf The number three}\\\\end{center}\\n\\\\vspace{40mm}\\\\[3\\\\]\\n\\\\end{document}'\nGot:\n    '\\\\documentclass{article}\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\n\\n\\\\usepackage{amsfonts}\\\\usepackage{graphicx}\\\\usepackage{pstricks}\\\\pagestyle{empty}\n\\n\\\\oddsidemargin 0.0in\\n\\\\evensidemargin 0.0in\\n\\\\textwidth 6.45in\\n\\\\topmargin \n0.0in\\n\\\\headheight 0.0in\\n\\\\headsep 0.0in\\n\\\\textheight 9.0in\\n\\n\\\\begin{document}\n\\n\\\\begin{center}{\\\\Large\\\\bf The number three}\\\\end{center}\\n\\\\vspace{40mm}\\\\[3\\\\]\n\\n\\\\end{document}'\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc0/devel/sage/sage/misc/latex.py\", line 370:\n    sage: _latex_file_([7, 8, 9], title=\"Why was six afraid of seven?\", sep='\\\\vfill\\\\hrule\\\\vfill')\nExpected:\n    '\\\\documentclass{article}\\\\usepackage{fullpage}\\\\usepackage{amsmath}\n\\n\\\\usepackage{amssymb}\\n\\\\usepackage{amsfonts}\\\\usepackage{graphicx}\n\\\\usepackage{pstricks}\\\\pagestyle{empty}\\n\\n\\\\begin{document}\\n\\\\begin{center}\n{\\\\Large\\\\bf Why was six afraid of seven?}\\\\end{center}\\n\\\\vspace{40mm}\\\\[7\\\\]\n\\n\\n\\\\vfill\\\\hrule\\\\vfill\\n\\n\\\\[8\\\\]\\n\\n\\\\vfill\\\\hrule\\\\vfill\\n\\n\\\\[\n\\\\]\\n\\\\end{document}'\nGot:\n    '\\\\documentclass{article}\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\n\\n\\\\usepackage{amsfonts}\\\\usepackage{graphicx}\\\\usepackage{pstricks}\\\\pagestyle{empty}\n\\n\\\\oddsidemargin 0.0in\\n\\\\evensidemargin 0.0in\\n\\\\textwidth 6.45in\\n\\\\topmargin \n0.0in\\n\\\\headheight 0.0in\\n\\\\headsep 0.0in\\n\\\\textheight 9.0in\\n\\n\\\\begin{document}\n\\n\\\\begin{center}{\\\\Large\\\\bf Why was six afraid of seven?}\\\\end{center}\n\\n\\\\vspace{40mm}\\\\[7\\\\]\\n\\n\\\\vfill\\\\hrule\\\\vfill\\n\\n\\\\[8\\\\]\\n\\n\\\\vfill\\\\hrule\\\\vfill\n\\n\\n\\\\[9\\\\]\\n\\\\end{document}'\n**********************************************************************\n1 items had failures:\n   2 of   5 in __main__.example_5\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.rc0/tmp/.doctest_latex.py\n\t [1.1 s]\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T08:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32606",
    "user": "mabshoff"
}
```

This patch causes doctest failures in the file it patches on sage.math! :)

```
sage -t -long "devel/sage/sage/misc/latex.py"               
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage/sage/misc/latex.py", line 368:
    sage: _latex_file_(3, title="The number three")
Expected:
    '\\documentclass{article}\\usepackage{fullpage}\\usepackage{amsmath}
\n\\usepackage{amssymb}\n\\usepackage{amsfonts}\\usepackage{graphicx}
\\usepackage{pstricks}\\pagestyle{empty}\n\n\\begin{document}\n\\begin{center}
{\\Large\\bf The number three}\\end{center}\n\\vspace{40mm}\\[3\\]\n\\end{document}'
Got:
    '\\documentclass{article}\\usepackage{amsmath}\n\\usepackage{amssymb}
\n\\usepackage{amsfonts}\\usepackage{graphicx}\\usepackage{pstricks}\\pagestyle{empty}
\n\\oddsidemargin 0.0in\n\\evensidemargin 0.0in\n\\textwidth 6.45in\n\\topmargin 
0.0in\n\\headheight 0.0in\n\\headsep 0.0in\n\\textheight 9.0in\n\n\\begin{document}
\n\\begin{center}{\\Large\\bf The number three}\\end{center}\n\\vspace{40mm}\\[3\\]
\n\\end{document}'
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage/sage/misc/latex.py", line 370:
    sage: _latex_file_([7, 8, 9], title="Why was six afraid of seven?", sep='\\vfill\\hrule\\vfill')
Expected:
    '\\documentclass{article}\\usepackage{fullpage}\\usepackage{amsmath}
\n\\usepackage{amssymb}\n\\usepackage{amsfonts}\\usepackage{graphicx}
\\usepackage{pstricks}\\pagestyle{empty}\n\n\\begin{document}\n\\begin{center}
{\\Large\\bf Why was six afraid of seven?}\\end{center}\n\\vspace{40mm}\\[7\\]
\n\n\\vfill\\hrule\\vfill\n\n\\[8\\]\n\n\\vfill\\hrule\\vfill\n\n\\[
\\]\n\\end{document}'
Got:
    '\\documentclass{article}\\usepackage{amsmath}\n\\usepackage{amssymb}
\n\\usepackage{amsfonts}\\usepackage{graphicx}\\usepackage{pstricks}\\pagestyle{empty}
\n\\oddsidemargin 0.0in\n\\evensidemargin 0.0in\n\\textwidth 6.45in\n\\topmargin 
0.0in\n\\headheight 0.0in\n\\headsep 0.0in\n\\textheight 9.0in\n\n\\begin{document}
\n\\begin{center}{\\Large\\bf Why was six afraid of seven?}\\end{center}
\n\\vspace{40mm}\\[7\\]\n\n\\vfill\\hrule\\vfill\n\n\\[8\\]\n\n\\vfill\\hrule\\vfill
\n\n\\[9\\]\n\\end{document}'
**********************************************************************
1 items had failures:
   2 of   5 in __main__.example_5
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.rc0/tmp/.doctest_latex.py
	 [1.1 s]
```


Cheers,

Michael



---

archive/issue_comments_032607.json:
```json
{
    "body": "Wait, so these things actually have to pass doctests?  :)\n\nHere's a new patch; the only change is to fix the doctests Michael pointed out.",
    "created_at": "2009-03-31T15:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32607",
    "user": "jhpalmieri"
}
```

Wait, so these things actually have to pass doctests?  :)

Here's a new patch; the only change is to fix the doctests Michael pointed out.



---

archive/issue_comments_032608.json:
```json
{
    "body": "It seems to not apply cleanly to 3.4.1.rc2. \n\n\n```\nwstein@sage:~/build/sage-3.4.1.rc2-ref2$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nhg_ssage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4435/4435.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4435/4435.patch\nLoading: [.]\ncd \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage\" && hg status\ncd \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage\" && hg status\ncd \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage\" && hg import   \"/scratch/wstein/sage/temp/sage.math.washington.edu/26219/tmp_1.patch\"\napplying /scratch/wstein/sage/temp/sage.math.washington.edu/26219/tmp_1.patch\npatching file sage/misc/latex.py\nHunk #3 FAILED at 365\n1 out of 3 hunks FAILED -- saving rejects to file sage/misc/latex.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2009-04-12T08:04:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32608",
    "user": "was"
}
```

It seems to not apply cleanly to 3.4.1.rc2. 


```
wstein@sage:~/build/sage-3.4.1.rc2-ref2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
hg_ssage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4435/4435.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4435/4435.patch
Loading: [.]
cd "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage" && hg status
cd "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage" && hg status
cd "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage" && hg import   "/scratch/wstein/sage/temp/sage.math.washington.edu/26219/tmp_1.patch"
applying /scratch/wstein/sage/temp/sage.math.washington.edu/26219/tmp_1.patch
patching file sage/misc/latex.py
Hunk #3 FAILED at 365
1 out of 3 hunks FAILED -- saving rejects to file sage/misc/latex.py.rej
abort: patch failed to apply
```




---

archive/issue_comments_032609.json:
```json
{
    "body": "Here's a rebased patch.",
    "created_at": "2009-04-12T15:40:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32609",
    "user": "jhpalmieri"
}
```

Here's a rebased patch.



---

archive/issue_comments_032610.json:
```json
{
    "body": "Attachment [4435.patch](tarball://root/attachments/some-uuid/ticket4435/4435.patch) by jhpalmieri created at 2009-04-24 19:30:58\n\nrebased against 3.4.2.alpha0",
    "created_at": "2009-04-24T19:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32610",
    "user": "jhpalmieri"
}
```

Attachment [4435.patch](tarball://root/attachments/some-uuid/ticket4435/4435.patch) by jhpalmieri created at 2009-04-24 19:30:58

rebased against 3.4.2.alpha0



---

archive/issue_comments_032611.json:
```json
{
    "body": "Does this actually need review?  The only changes since its positive review are fixes to make doctests pass; should the positive review still stand?",
    "created_at": "2009-04-24T20:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32611",
    "user": "jhpalmieri"
}
```

Does this actually need review?  The only changes since its positive review are fixes to make doctests pass; should the positive review still stand?



---

archive/issue_comments_032612.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> Does this actually need review?  The only changes since its positive review are fixes to make doctests pass; should the positive review still stand?\n\nIt can stand assuming the doctests pass, so if they do feel free to reinstate the positive review :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T21:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32612",
    "user": "mabshoff"
}
```

Replying to [comment:8 jhpalmieri]:
> Does this actually need review?  The only changes since its positive review are fixes to make doctests pass; should the positive review still stand?

It can stand assuming the doctests pass, so if they do feel free to reinstate the positive review :)

Cheers,

Michael



---

archive/issue_comments_032613.json:
```json
{
    "body": "Version rebased against 3.4.2.alpha0 passes all tests on sage.math.",
    "created_at": "2009-04-24T21:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32613",
    "user": "jhpalmieri"
}
```

Version rebased against 3.4.2.alpha0 passes all tests on sage.math.



---

archive/issue_comments_032614.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T03:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32614",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_032615.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T03:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4435#issuecomment-32615",
    "user": "mabshoff"
}
```

Resolution: fixed
