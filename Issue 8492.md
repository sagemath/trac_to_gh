# Issue 8492: Sage 4.3.4.alpha1: docbuild warnings in HTML version of reference manual

archive/issues_008492.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  sage-combinat @nthiery @dwbump\n\nWith Sage 4.3.4.alpha1 and ticket #8457, building the HTML version of the standard documentation results in the following warnings:\n\n```\n/mnt/usb1/scratch/mvngu/release/sage-4.3.4.alpha1/local/lib/python2.6/site-packages/sage/categories/algebras_with_basis.py:docstring of sage.categories.algebras_with_basis.AlgebrasWithBasis.ParentMethods.product_on_basis:9: (ERROR/3) Unknown interpreted text role \"met\".\n<autodoc>:0: (ERROR/3) Unexpected indentation.\n/mnt/usb1/scratch/mvngu/release/sage-4.3.4.alpha1/local/lib/python2.6/site-packages/sage/categories/coxeter_groups.py:docstring of sage.categories.coxeter_groups.CoxeterGroups.ElementMethods.has_right_descent:5: (WARNING/2) Literal block expected; none found.\n/mnt/usb1/scratch/mvngu/release/sage-4.3.4.alpha1/local/lib/python2.6/site-packages/sage/categories/coxeter_groups.py:docstring of sage.categories.coxeter_groups.CoxeterGroups.ElementMethods.reduced_word_reverse_iterator:16: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.\n/mnt/usb1/scratch/mvngu/release/sage-4.3.4.alpha1/local/lib/python2.6/site-packages/sage/categories/coxeter_groups.py:docstring of sage.categories.coxeter_groups.CoxeterGroups.ParentMethods.simple_reflections:1: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.\n/mnt/usb1/scratch/mvngu/release/sage-4.3.4.alpha1/local/lib/python2.6/site-packages/sage/categories/modules_with_basis.py:docstring of sage.categories.modules_with_basis.ModulesWithBasis.ParentMethods.module_morphism:5: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.\n<autodoc>:0: (ERROR/3) Unexpected indentation.\n<autodoc>:0: (ERROR/3) Unexpected indentation.\n\n<SNIP>\n\nwriting output... [ 12%] sage/categories/coxeter_groups\nWARNING: display latex u'\\\\opi_i': latex exited with error:\n[stderr]\n\n[stdout]\nThis is pdfTeXk, Version 3.141592-1.40.3 (Web2C 7.5.6)\n %&-line parsing enabled.\nentering extended mode\n(./math.tex\nLaTeX2e <2005/12/01>\nBabel <v3.8h> and hyphenation patterns for english, usenglishmax, dumylang, noh\nyphenation, croatian, ukrainian, russian, bulgarian, czech, slovak, danish, dut\nch, finnish, basque, french, german, ngerman, ibycus, greek, monogreek, ancient\ngreek, hungarian, italian, latin, mongolian, norsk, icelandic, interlingua, tur\nkish, coptic, romanian, welsh, serbian, slovenian, estonian, esperanto, upperso\nrbian, indonesian, polish, portuguese, spanish, catalan, galician, swedish, loa\nded.\n(/usr/share/texmf-texlive/tex/latex/base/article.cls\nDocument Class: article 2005/09/16 v1.4f Standard LaTeX document class\n(/usr/share/texmf-texlive/tex/latex/base/size12.clo))\n(/usr/share/texmf-texlive/tex/latex/base/inputenc.sty\n(/usr/share/texmf-texlive/tex/latex/base/utf8.def\n(/usr/share/texmf-texlive/tex/latex/base/t1enc.dfu)\n(/usr/share/texmf-texlive/tex/latex/base/ot1enc.dfu)\n(/usr/share/texmf-texlive/tex/latex/base/omsenc.dfu)))\n(/usr/share/texmf-texlive/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texmf-texlive/tex/latex/amsmath/amstext.sty\n(/usr/share/texmf-texlive/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texmf-texlive/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texmf-texlive/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texmf-texlive/tex/latex/amscls/amsthm.sty)\n(/usr/share/texmf-texlive/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texmf-texlive/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texmf-texlive/tex/latex/tools/bm.sty) (./math.aux)\n(/usr/share/texmf-texlive/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texmf-texlive/tex/latex/amsfonts/umsb.fd)\n! Undefined control sequence.\n<recently read> \\opi \n                     \nl.29 $\\opi\n          _i$\n[1] (./math.aux) )\n(see the transcript file for additional information)\nOutput written on math.dvi (1 page, 208 bytes).\nTranscript written on math.log.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8492\n\n",
    "created_at": "2010-03-10T19:00:03Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Sage 4.3.4.alpha1: docbuild warnings in HTML version of reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8492",
    "user": "mvngu"
}
```
Assignee: mvngu

CC:  sage-combinat @nthiery @dwbump

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


Issue created by migration from https://trac.sagemath.org/ticket/8492





---

archive/issue_comments_076590.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T21:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8492#issuecomment-76590",
    "user": "@jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076591.json:
```json
{
    "body": "Here's a patch.  The patch fixes all but one of the issues.  One question: in the docstring for `apply_simple_projection` in `sage.categories.coxeter_groups.py`, I changed `\\opi` to `\\overline\\pi` -- this looked like the right change, given the other documentation.  But I would like some confirmation from someone (Nicolas? Dan?) familiar with that code.\n\nThe remaining issue: I don't know what's causing\n\n```\n<autodoc>:0: (ERROR/3) Unexpected indentation.\n<autodoc>:0: (ERROR/3) Unexpected indentation.\n<autodoc>:0: (ERROR/3) Unexpected indentation.\n```\n\nbut I'm trying to track it down.  A patch could go on another ticket -- no need to hold up this one.",
    "created_at": "2010-03-10T21:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8492#issuecomment-76591",
    "user": "@jhpalmieri"
}
```

Here's a patch.  The patch fixes all but one of the issues.  One question: in the docstring for `apply_simple_projection` in `sage.categories.coxeter_groups.py`, I changed `\opi` to `\overline\pi` -- this looked like the right change, given the other documentation.  But I would like some confirmation from someone (Nicolas? Dan?) familiar with that code.

The remaining issue: I don't know what's causing

```
<autodoc>:0: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.
```

but I'm trying to track it down.  A patch could go on another ticket -- no need to hold up this one.



---

archive/issue_comments_076592.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-11T00:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8492#issuecomment-76592",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076593.json:
```json
{
    "body": "Attachment [trac_8492-ref.patch](tarball://root/attachments/some-uuid/ticket8492/trac_8492-ref.patch) by mvngu created at 2010-03-11 00:43:11\n\nThe patch is OK by me. The remaining three warnings can be dealt with in another ticket.",
    "created_at": "2010-03-11T00:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8492#issuecomment-76593",
    "user": "mvngu"
}
```

Attachment [trac_8492-ref.patch](tarball://root/attachments/some-uuid/ticket8492/trac_8492-ref.patch) by mvngu created at 2010-03-11 00:43:11

The patch is OK by me. The remaining three warnings can be dealt with in another ticket.



---

archive/issue_comments_076594.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-12T04:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8492#issuecomment-76594",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_076595.json:
```json
{
    "body": "Replying to [comment:1 jhpalmieri]:\n\n> The remaining issue: I don't know what's causing\n\n```\n<autodoc>:0: (ERROR/3) Unexpected indentation.\n<autodoc>:0: (ERROR/3) Unexpected indentation.\n<autodoc>:0: (ERROR/3) Unexpected indentation.\n```\n\n> but I'm trying to track it down.  A patch could go on another ticket -- no need to hold up this one.\n\nSee #8511.",
    "created_at": "2010-03-12T23:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8492#issuecomment-76595",
    "user": "@jhpalmieri"
}
```

Replying to [comment:1 jhpalmieri]:

> The remaining issue: I don't know what's causing

```
<autodoc>:0: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.
```

> but I'm trying to track it down.  A patch could go on another ticket -- no need to hold up this one.

See #8511.
