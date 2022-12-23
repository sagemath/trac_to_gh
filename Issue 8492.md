# Issue 8492: Sage 4.3.4.alpha1: docbuild warnings in HTML version of reference manual

Issue created by migration from https://trac.sagemath.org/ticket/8492

Original creator: mvngu

Original creation time: 2010-03-10 19:00:03

Assignee: mvngu

CC:  sage-combinat nthiery bump

With Sage 4.3.4.alpha1 and ticket #8457, building the HTML version of the standard documentation results in the following warnings:

```
/mnt/usb1/scratch/mvngu/release/sage-4.3.4.alpha1/local/lib/python2.6/site-packages/sage/categories/algebras_with_basis.py:docstring of sage.categories.algebras_with_basis.AlgebrasWithBasis.ParentMethods.product_on_basis:9: (ERROR/3) Unknown interpreted text role "met".
<autodoc>:0: (ERROR/3) Unexpected indentation.
/mnt/usb1/scratch/mvngu/release/sage-4.3.4.alpha1/local/lib/python2.6/site-packages/sage/categories/coxeter_groups.py:docstring of sage.categories.coxeter_groups.CoxeterGroups.ElementMethods.has_right_descent:5: (WARNING/2) Literal block expected; none found.
/mnt/usb1/scratch/mvngu/release/sage-4.3.4.alpha1/local/lib/python2.6/site-packages/sage/categories/coxeter_groups.py:docstring of sage.categories.coxeter_groups.CoxeterGroups.ElementMethods.reduced_word_reverse_iterator:16: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.
/mnt/usb1/scratch/mvngu/release/sage-4.3.4.alpha1/local/lib/python2.6/site-packages/sage/categories/coxeter_groups.py:docstring of sage.categories.coxeter_groups.CoxeterGroups.ParentMethods.simple_reflections:1: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.
/mnt/usb1/scratch/mvngu/release/sage-4.3.4.alpha1/local/lib/python2.6/site-packages/sage/categories/modules_with_basis.py:docstring of sage.categories.modules_with_basis.ModulesWithBasis.ParentMethods.module_morphism:5: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.
<autodoc>:0: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.

<SNIP>

writing output... [ 12%] sage/categories/coxeter_groups
WARNING: display latex u'\\opi_i': latex exited with error:
[stderr]

[stdout]
This is pdfTeXk, Version 3.141592-1.40.3 (Web2C 7.5.6)
 %&-line parsing enabled.
entering extended mode
(./math.tex
LaTeX2e <2005/12/01>
Babel <v3.8h> and hyphenation patterns for english, usenglishmax, dumylang, noh
yphenation, croatian, ukrainian, russian, bulgarian, czech, slovak, danish, dut
ch, finnish, basque, french, german, ngerman, ibycus, greek, monogreek, ancient
greek, hungarian, italian, latin, mongolian, norsk, icelandic, interlingua, tur
kish, coptic, romanian, welsh, serbian, slovenian, estonian, esperanto, upperso
rbian, indonesian, polish, portuguese, spanish, catalan, galician, swedish, loa
ded.
(/usr/share/texmf-texlive/tex/latex/base/article.cls
Document Class: article 2005/09/16 v1.4f Standard LaTeX document class
(/usr/share/texmf-texlive/tex/latex/base/size12.clo))
(/usr/share/texmf-texlive/tex/latex/base/inputenc.sty
(/usr/share/texmf-texlive/tex/latex/base/utf8.def
(/usr/share/texmf-texlive/tex/latex/base/t1enc.dfu)
(/usr/share/texmf-texlive/tex/latex/base/ot1enc.dfu)
(/usr/share/texmf-texlive/tex/latex/base/omsenc.dfu)))
(/usr/share/texmf-texlive/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texmf-texlive/tex/latex/amsmath/amstext.sty
(/usr/share/texmf-texlive/tex/latex/amsmath/amsgen.sty))
(/usr/share/texmf-texlive/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texmf-texlive/tex/latex/amsmath/amsopn.sty))
(/usr/share/texmf-texlive/tex/latex/amscls/amsthm.sty)
(/usr/share/texmf-texlive/tex/latex/amsfonts/amssymb.sty
(/usr/share/texmf-texlive/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texmf-texlive/tex/latex/tools/bm.sty) (./math.aux)
(/usr/share/texmf-texlive/tex/latex/amsfonts/umsa.fd)
(/usr/share/texmf-texlive/tex/latex/amsfonts/umsb.fd)
! Undefined control sequence.
<recently read> \opi 
                     
l.29 $\opi
          _i$
[1] (./math.aux) )
(see the transcript file for additional information)
Output written on math.dvi (1 page, 208 bytes).
Transcript written on math.log.
```



---

Comment by jhpalmieri created at 2010-03-10 21:02:04

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-03-10 21:02:04

Here's a patch.  The patch fixes all but one of the issues.  One question: in the docstring for `apply_simple_projection` in `sage.categories.coxeter_groups.py`, I changed `\opi` to `\overline\pi` -- this looked like the right change, given the other documentation.  But I would like some confirmation from someone (Nicolas? Dan?) familiar with that code.

The remaining issue: I don't know what's causing

```
<autodoc>:0: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.
```

but I'm trying to track it down.  A patch could go on another ticket -- no need to hold up this one.


---

Comment by mvngu created at 2010-03-11 00:43:11

Changing status from needs_review to positive_review.


---

Attachment

The patch is OK by me. The remaining three warnings can be dealt with in another ticket.


---

Comment by mvngu created at 2010-03-12 04:51:13

Resolution: fixed


---

Comment by jhpalmieri created at 2010-03-12 23:39:38

Replying to [comment:1 jhpalmieri]:

> The remaining issue: I don't know what's causing

```
<autodoc>:0: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.
```

> but I'm trying to track it down.  A patch could go on another ticket -- no need to hold up this one.

See #8511.
