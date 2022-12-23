# Issue 4435: %latex -- don't use \usepackage{fullpage}

Issue created by migration from https://trac.sagemath.org/ticket/4435

Original creator: was

Original creation time: 2008-11-04 04:55:49

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



---

Comment by jhpalmieri created at 2009-03-22 22:41:37

Here's a patch.  (Does anyone use "%slide"?  The output is pretty ugly, seems to me.)


---

Comment by jhpalmieri created at 2009-03-22 22:41:37

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-03-22 22:41:37

Changing assignee from cwitty to jhpalmieri.


---

Comment by was created at 2009-03-29 16:38:32

> Here's a patch. (Does anyone use "%slide"? The output is pretty ugly, seems to me.) 

I have -- it allows one to use anything in latex beamer (in theory), which is pretty (in theory).  I haven't used %slide in a long time though, since I just use TinyMCE now.


---

Comment by was created at 2009-03-29 16:50:35

Incidentally %slide takes a LONG time to tex any given slide on OS X... This has nothing to do with this patch (just an observation).


---

Comment by mabshoff created at 2009-03-31 08:03:41

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

Comment by jhpalmieri created at 2009-03-31 15:49:02

Wait, so these things actually have to pass doctests?  :)

Here's a new patch; the only change is to fix the doctests Michael pointed out.


---

Comment by was created at 2009-04-12 08:04:51

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

Comment by jhpalmieri created at 2009-04-12 15:40:28

Here's a rebased patch.


---

Attachment

rebased against 3.4.2.alpha0


---

Comment by jhpalmieri created at 2009-04-24 20:54:38

Does this actually need review?  The only changes since its positive review are fixes to make doctests pass; should the positive review still stand?


---

Comment by mabshoff created at 2009-04-24 21:08:30

Replying to [comment:8 jhpalmieri]:
> Does this actually need review?  The only changes since its positive review are fixes to make doctests pass; should the positive review still stand?

It can stand assuming the doctests pass, so if they do feel free to reinstate the positive review :)

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-04-24 21:15:06

Version rebased against 3.4.2.alpha0 passes all tests on sage.math.


---

Comment by mabshoff created at 2009-04-30 03:59:17

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 03:59:17

Resolution: fixed
