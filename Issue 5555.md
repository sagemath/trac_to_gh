# Issue 5555: [with patch, not ready for review] make some TeX macros available to docstrings

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-03-17 23:38:59

Assignee: jhpalmieri

With the attached patch, you should be able to use \ZZ, \CC, \RR, and \QQ in docstrings and have them typeset correctly in the html, live html, latex, and pdf versions of the documentation.  To add new macros, edit the file '$SAGE_ROOT/devel/sage/doc/common/sage-macros.tex'.  (I considered just using the existing file 'macros.tex' in the same directory, but decided it was too bloated.)

The point here is to be able to write docstrings which are readable from interactive help in Sage and which also get typeset correctly in the reference manual; this was discussed on [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/74e6bcf5ef716d1c), and people seemed to agree that a docstring like 

```
This computes the integral homology `H_d(X, \ZZ)` of `X` in dimension `d`. 
```

was better than

```
This computes the integral homology `H_d(X, \mathbb{Z})` of `X` in dimension `d`. 
```

especially since the \ZZ gets turned into ZZ when pre-parsed for interactive help.  

This point should be kept in mind if anyone wants to add new macros: the name should be short and unambiguous, and there should be a good reason for using it instead of plain LaTeX.  (This was maybe what I meant when I said that macros.tex was too bloated.)

Having said all of that, I would be happy to add some more macros now.  What else should be added?  Once we seem to have made some sort of decision about that, I'll update the patch and mark this ticket as "needs review".


---

Comment by jhpalmieri created at 2009-03-19 19:01:56

Now I need help.  'new-macros.patch' doesn't work, and I don't know why.  When I run it, I get the error message

```
% sage -docbuild reference html
sphinx-build -b html -d /Applications/sage/devel/sage/doc/output/doctrees/en/reference   .  /Applications/sage/devel/sage/doc/output/html/en/reference
Exception occurred:
  File "<string>", line 1, in <module>
NameError: name 'sage' is not defined
The full traceback has been saved in /var/folders/JV/JVYCpshdHd4FFoThuUgD8k+++TI/-Tmp-/sphinx-err-l-jOy1.log, if you want to report the issue to the author.
Please also report this if it was a user error, so that a better error message can be provided next time.
```

This is coming from the line

```
defn += eval('str(latex(' + module + "." + name + args + '))') + '}'
```

which, for example, doesn't seem to like doing this:

```
eval('str(latex(sage.rings.all.ZZ))')
```

(A few lines earlier, `from sage.misc.latex import latex` seems to be perfectly acceptable.)

When I run sage and "attach conf.py", then the function `produce_latex_macro` works just fine.  I'm probably making some stupid Python mistake.  Can anyone help?


---

Comment by jhpalmieri created at 2009-03-19 19:55:11

Ignore my previous remark.  This is now ready for review.

To add new macros, edit these lines in conf.py:

```
sage_macros = [("ZZ", "sage.rings.all"),
               ("RR", "sage.rings.all"),
               ("CC", "sage.rings.all"),
               ("QQ", "sage.rings.all"),
               ("QQbar", "sage.rings.all"),
               ("GF", "sage.rings.all", 17),
               ]
```

The file has comments explaining what to do...


---

Comment by mhansen created at 2009-03-19 21:13:03

We really should/need to make it so all of this plays well with jsMath: http://www.math.union.edu/~dpvc/jsMath/authors/macros.html


---

Comment by jhpalmieri created at 2009-03-20 01:55:58

Replying to [comment:3 mhansen]:
> We really should/need to make it so all of this plays well with jsMath: 
> http://www.math.union.edu/~dpvc/jsMath/authors/macros.html

Okay, how about this patch?


---

Comment by jhpalmieri created at 2009-03-20 02:02:10

(I clicked 'submit' too early.  Here's a longer reply.)

Replying to [comment:3 mhansen]:
> We really should/need to make it so all of this plays well with jsMath: 
> http://www.math.union.edu/~dpvc/jsMath/authors/macros.html

Okay, how about this patch?  This seems to allow use of the imported macros in the notebook (e.g. by shift-clicking between cells and adding "test: $\ZZ$") and in the live versions of the reference manual and the tutorial. Does that definitely mean that it's working well with jsMath?  I'm not sure how to test this...


---

Comment by jhpalmieri created at 2009-03-20 02:43:57

By the way, #5568 should be trivial to review and is somewhat related to this one.


---

Comment by malb created at 2009-03-23 10:06:24

Am I right that $\GF(2^n)$ won't work, from the patch it looks like it?


---

Comment by jhpalmieri created at 2009-03-24 05:09:21

Replying to [comment:7 malb]:
> Am I right that `$\GF(2^n)$` won't work, from the patch it looks like it?

If you put ``\GF{2^n}`` in a docstring (note the curly braces, not parentheses), then this will appear as `"GF{2^n}"` in a docstring, and it will be typeset as `"\mathbf{F}_{2^n}"` in the reference manual.  In general, given ``\GF{blah}``, then `blah` is not modified: it appears as is in both the docstring and the LaTeX which produces reference manual. It can be a complicated LaTeX expression, for example, and it should work fine.

You can test this by applying the patch and then putting `\GF{2<sup>{3</sup>n}}` somewhere in the tutorial, for example, and then type "sage -docbuild tutorial html" (or "pdf" instead of "html") to check the output, or "sage -docbuild tutorial latex" to check the LaTeX source code.  

Is that good enough, or were you hoping for something else?


---

Comment by jhpalmieri created at 2009-03-24 05:12:45

> If you put ``\GF{2^n}`` in a docstring 

Of course, you need to be careful about single vs. double backslashes.  This should probably be ``\\GF{2^n}`` ...


---

Comment by malb created at 2009-03-24 10:21:38

Replying to [comment:8 jhpalmieri]:
> Is that good enough, or were you hoping for something else?

All good, sorry I didn't understand the patch properly. Thanks for explaining!


---

Comment by jhpalmieri created at 2009-03-24 20:18:55

Here's an additional patch; apply on top of the other one.  This allows use of these macros interactively; for example, in the notebook you could do

```
%latex
$\ZZ$
```

and it will be typeset correctly.


---

Attachment

(don't use, obsolete)


---

Attachment

(don't use, obsolete)


---

Attachment

(don't use, obsolete)


---

Comment by jhpalmieri created at 2009-03-24 20:21:37

apply this one first


---

Attachment

(Is there a way to delete attachments?)


---

Comment by mabshoff created at 2009-04-06 22:19:07

Hmm, this patch was not on my radar at all. Given the patch at #5700 which patch here is the current one to apply and review?

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-04-06 22:59:44

This one may have been posted during the Great Trac Email Blackout.

As I've tried to indicate at #5700, that patch is temporary.  This one is supposed to be permanent.  Applying this one will make #5700 unnecessary.  If you think this patch might get in some time soon, then maybe we should ignore #5700?


---

Comment by mabshoff created at 2009-04-06 23:08:24

Ok, looking at the patches again I think it is obvious that we need to review

 * new-macros-with-jsmath.patch
 * 5555-second.patch

only and can ignore the others as indicated. I am actually for merging and reviewing this one instead of merging #5700 now as a stopgap, so reassigned without any guarantee which one will go in.

Cheers,

Michael


---

Comment by ddrake created at 2009-04-10 04:15:45

I'm looking over this, and the code seems good, but I can't find any examples of it doing anything in the html documentation. Am I missing something, or building the documentation wrong? I'm using --jsmath, which works in the notebook, but when I click the Help link at the top, it's not typesetting anything.


---

Comment by jhpalmieri created at 2009-04-10 04:52:24

This patch doesn't actually add any examples in the documentation.  However, there are examples, recently added in Sage, which use these macros:

  * in sage/algebras/quatalg/quaternion_algebra.py, the functions `ideal`, `left_ideal` and `right_ideal` all use \ZZ, 

  * in sage/rings/polynomial/polynomial_element.pyx, `is_primitive` uses \GF{-},

  * in sage/schemes/elliptic_curves/ell_rational_field.py, `modular_symbol` uses \QQ.

So right now, those docstrings don't appear correctly in the html version of the reference manual, and they actually produce errors in the pdf version.  If you apply the patches here, those issues should be fixed.

Also as I said earlier:

> You can test this by applying the patch and then putting `"\GF{q}"` somewhere in the tutorial, for example, and then type  "sage -docbuild tutorial html" (or "pdf" instead of "html") to check the output, or "sage -docbuild tutorial latex" to check the LaTeX source code.

Does this answer your question?


---

Comment by ddrake created at 2009-04-10 09:10:51

Replying to [comment:17 jhpalmieri]:
> Does this answer your question?

Yes, pretty much. I think most of my problems involve my own lack of knowledge about building the documentation, and the problems we still have with building it. But I got the tutorial to correctly show the macros in html, pdf, and text form.

I've reviewed the patches "new-macros-with-jsmath.patch" and "5555-second.patch" and they are very nice. Works as advertised, good code, all doctests pass: positive review.


---

Comment by mabshoff created at 2009-04-10 21:45:07

Did someone not run doctests? :)


```
sage -t -long "devel/sage/sage/misc/latex.py"               
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/misc/latex.py", line 371:
    sage: _latex_file_(3, title="The number three")
Expected:
    '\\documentclass{article}\\usepackage{fullpage}\\usepackage{amsmath}
\n\\usepackage{amssymb}\n\\usepackage{amsfonts}\\usepackage{graphicx}
\\usepackage{pstricks}\\pagestyle{empty}\n\n\\begin{document}\n\\begin{center}
{\\Large\\bf The number three}\\end{center}\n\\vspace{40mm}\\[3\\]\n\\end{document}'
Got:
    '\\documentclass{article}\\usepackage{fullpage}\\usepackage{amsmath}
\n\\usepackage{amssymb}\n\\usepackage{amsfonts}\\usepackage{graphicx}
\\usepackage{pstricks}\\pagestyle{empty}\n\n\n\\newcommand{\\ZZ}{\\mathbf{Z}}
\n\\newcommand{\\RR}{\\mathbf{R}}\n\\newcommand{\\CC}{\\mathbf{C}}\n\\newcommand{\\QQ}
{\\mathbf{Q}}\n\\newcommand{\\QQbar}{\\overline{\\mathbf{Q}}}\n\\newcommand{\\GF}
[1]{\\mathbf{F}_{#1}}\n\\newcommand{\\Zp}[1]{\\mathbf{Z}_{#1}}\n\\newcommand{\\Qp}
[1]{\\mathbf{Q}_{#1}}\n\\newcommand{\\Zmod}[1]{\\mathbf{Z}/#1\\mathbf{Z}}
\n\\newcommand{\\CDF}{\\text{Complex Double Field}}\n\\newcommand{\\CIF}{\\mathbf{C}}
\n\\newcommand{\\CLF}{\\mathbf{C}}\n\\newcommand{\\RDF}{\\mathbf{R}}
\n\\newcommand{\\RIF}{\\I \\R}\n\\newcommand{\\RLF}{\\mathbf{R}}\n\\newcommand{\\RQDF}
{\\mathbf{R}}\n\\newcommand{\\CFF}{\\mathbf{CFF}}\n\n\\begin{document}\n\\begin{center}
{\\Large\\bf The number three}\\end{center}\n\\vspace{40mm}\\[3\\]\n\\end{document}'
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/misc/latex.py", line 373:
    sage: _latex_file_([7, 8, 9], title="Why was six afraid of seven?", sep='\\vfill\\hrule\\vfill')
Expected:
    '\\documentclass{article}\\usepackage{fullpage}\\usepackage{amsmath}
\n\\usepackage{amssymb}\n\\usepackage{amsfonts}\\usepackage{graphicx}
\\usepackage{pstricks}\\pagestyle{empty}\n\n\\begin{document}\n\\begin{center}
{\\Large\\bf Why was six afraid of seven?}\\end{center}\n\\vspace{40mm}\\[7\\]
\n\n\\vfill\\hrule\\vfill\n\n\\[8\\]\n\n\\vfill\\hrule\\vfill\n\n\\[9
\\]\n\\end{document}'
Got:
    '\\documentclass{article}\\usepackage{fullpage}\\usepackage{amsmath}
\n\\usepackage{amssymb}\n\\usepackage{amsfonts}\\usepackage{graphicx}
\\usepackage{pstricks}\\pagestyle{empty}\n\n\n\\newcommand{\\ZZ}{\\mathbf{Z}}
\n\\newcommand{\\RR}{\\mathbf{R}}\n\\newcommand{\\CC}{\\mathbf{C}}\n\\newcommand{\\QQ}
{\\mathbf{Q}}\n\\newcommand{\\QQbar}{\\overline{\\mathbf{Q}}}\n\\newcommand{\\GF}
[1]{\\mathbf{F}_{#1}}\n\\newcommand{\\Zp}[1]{\\mathbf{Z}_{#1}}\n\\newcommand{\\Qp}
[1]{\\mathbf{Q}_{#1}}\n\\newcommand{\\Zmod}[1]{\\mathbf{Z}/#1\\mathbf{Z}}
\n\\newcommand{\\CDF}{\\text{Complex Double Field}}\n\\newcommand{\\CIF}{\\mathbf{C}}
\n\\newcommand{\\CLF}{\\mathbf{C}}\n\\newcommand{\\RDF}{\\mathbf{R}}
\n\\newcommand{\\RIF}{\\I \\R}\n\\newcommand{\\RLF}{\\mathbf{R}}\n\\newcommand{\\RQDF}
{\\mathbf{R}}\n\\newcommand{\\CFF}{\\mathbf{CFF}}\n\n\\begin{document}\n\\begin{center}
{\\Large\\bf Why was six afraid of seven?}\\end{center}\n\\vspace{40mm}\\[7\\]
\n\n\\vfill\\hrule\\vfill\n\n\\[8\\]\n\n\\vfill\\hrule\\vfill\n\n\\[9
\\]\n\\end{document}'
**********************************************************************
```

Once this obvious failure is fixed feel free to reinstate the positive review.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-04-10 22:55:10

apply this one second


---

Attachment

Okay, here's a new patch with revised doctests.


---

Comment by mabshoff created at 2009-04-11 00:19:08

Resolution: fixed


---

Comment by mabshoff created at 2009-04-11 00:19:08

Merged  new-macros-with-jsmath.patch and 5555-second.patch in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by ddrake created at 2009-04-11 02:49:12

Replying to [comment:19 mabshoff]:
> Did someone not run doctests? :)

That's weird...I doctested the whole tree and everything worked. I'm glad to see it was fixed and merged, though.
