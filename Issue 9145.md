# Issue 9145: Expand math symbols available in documentation, remove doc/common/macros.tex

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-06-05 04:03:42

Assignee: mvngu

CC:  jhpalmieri

See discussion at

http://groups.google.com/group/sage-devel/browse_thread/thread/d62ea229829048f7


---

Comment by rbeezer created at 2010-06-05 04:14:02

Changing status from new to needs_review.


---

Attachment

Patch removes doc/common/macros.tex, replaces amsfonts by amssymb in latex preamble string of doc/common/conf.py.

4.4.3.alpha3 HTMl and PDF documentation all build without halting when this patch is applied and a limited survey indicates they look good as well.


---

Comment by mvngu created at 2010-06-05 21:44:52

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-06-05 21:44:52

Without the patch, when building the PDF version of the reference manual for Sage 4.4.3, I got:

```
! Undefined control sequence.
l.217693 ...als}(\mathrm{pos}_{i+1})]_{1 \leqslant 
                                                   i \leqslant n}$
```

Note that the HTML version built OK. With the patch, the PDF version built successfully on these machines:

 * sage.math, Ubuntu 8.04.4 LTS, with latex and pdflatex
 * bsd.math, Mac OS X 10.6.3, with latex and pdflatex

But failed on these machines:

 * eno.skynet, Fedora 12, no latex or pdflatex
 * rh.math, Ubuntu 10.04 LTS, no latex or pdflatex
 * rosemary.math, Red Hat Enterprise Linux Server 5.5, with latex and pdflatex, but I got the following error when building the PDF version:
 {{{
! LaTeX Error: File `utf8x.def' not found.
 }}}
 This also happens without the patch. The issue is more likely due to the LaTeX installation on rosemary.math.

As for `doc/common/macros.tex`, that file was during the days when Sage's documentation followed how Python did it. Since switching over to Sphinx, we don't need that file any more.


---

Comment by mhansen created at 2010-06-06 00:44:00

Resolution: fixed
