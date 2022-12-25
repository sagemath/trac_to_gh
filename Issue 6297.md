# Issue 6297: fix LaTeX formatting in sage/schemes/elliptic_curves/period_lattice.py

archive/issues_006297.json:
```json
{
    "body": "Assignee: tba\n\nWhile building the reference manual of Sage 4.0.2.rc0, I noticed the following LaTeX error:\n\n```\nsage/schemes/elliptic_curves/period_lattice WARNING: display latex u'\\\\signa(P)': latex exited with error:\n[stderr]\n\n[stdout]\nThis is pdfTeXk, Version 3.141592-1.40.3 (Web2C 7.5.6)\n %&-line parsing enabled.\nentering extended mode\n(./math.tex\nLaTeX2e <2005/12/01>\nBabel <v3.8h> and hyphenation patterns for english, usenglishmax, dumylang, noh\nyphenation, croatian, ukrainian, russian, bulgarian, czech, slovak, danish, dut\nch, finnish, basque, french, german, ngerman, ibycus, greek, monogreek, ancient\ngreek, hungarian, italian, latin, mongolian, norsk, icelandic, interlingua, tur\nkish, coptic, romanian, welsh, serbian, slovenian, estonian, esperanto, upperso\nrbian, indonesian, polish, portuguese, spanish, catalan, galician, swedish, loa\nded.\n(/usr/share/texmf-texlive/tex/latex/base/article.cls\nDocument Class: article 2005/09/16 v1.4f Standard LaTeX document class\n(/usr/share/texmf-texlive/tex/latex/base/size12.clo))\n(/usr/share/texmf-texlive/tex/latex/base/inputenc.sty\n(/usr/share/texmf-texlive/tex/latex/base/utf8.def\n(/usr/share/texmf-texlive/tex/latex/base/t1enc.dfu)\n(/usr/share/texmf-texlive/tex/latex/base/ot1enc.dfu)\n(/usr/share/texmf-texlive/tex/latex/base/omsenc.dfu)))\n(/usr/share/texmf-texlive/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texmf-texlive/tex/latex/amsmath/amstext.sty\n(/usr/share/texmf-texlive/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texmf-texlive/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texmf-texlive/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texmf-texlive/tex/latex/amscls/amsthm.sty)\n(/usr/share/texmf-texlive/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texmf-texlive/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texmf-texlive/tex/latex/tools/bm.sty)\nNo file math.aux.\n(/usr/share/texmf-texlive/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texmf-texlive/tex/latex/amsfonts/umsb.fd)\n! Undefined control sequence.\n<recently read> \\signa \n                       \nl.30 $\\signa\n            (P)$\n[1] (./math.aux) )\n(see the transcript file for additional information)\nOutput written on math.dvi (1 page, 256 bytes).\nTranscript written on math.log.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6297\n\n",
    "created_at": "2009-06-15T11:40:09Z",
    "labels": [
        "component: documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "fix LaTeX formatting in sage/schemes/elliptic_curves/period_lattice.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6297",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

While building the reference manual of Sage 4.0.2.rc0, I noticed the following LaTeX error:

```
sage/schemes/elliptic_curves/period_lattice WARNING: display latex u'\\signa(P)': latex exited with error:
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
(/usr/share/texmf-texlive/tex/latex/tools/bm.sty)
No file math.aux.
(/usr/share/texmf-texlive/tex/latex/amsfonts/umsa.fd)
(/usr/share/texmf-texlive/tex/latex/amsfonts/umsb.fd)
! Undefined control sequence.
<recently read> \signa 
                       
l.30 $\signa
            (P)$
[1] (./math.aux) )
(see the transcript file for additional information)
Output written on math.dvi (1 page, 256 bytes).
Transcript written on math.log.
```


Issue created by migration from https://trac.sagemath.org/ticket/6297





---

archive/issue_comments_050151.json:
```json
{
    "body": "Attachment [trac_6297.patch](tarball://root/attachments/some-uuid/ticket6297/trac_6297.patch) by mvngu created at 2009-06-15 11:41:49",
    "created_at": "2009-06-15T11:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6297#issuecomment-50151",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6297.patch](tarball://root/attachments/some-uuid/ticket6297/trac_6297.patch) by mvngu created at 2009-06-15 11:41:49



---

archive/issue_comments_050152.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2009-06-15T20:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6297#issuecomment-50152",
    "user": "https://github.com/ncalexan"
}
```

Fine by me.



---

archive/issue_comments_050153.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-18T00:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6297#issuecomment-50153",
    "user": "https://github.com/craigcitro"
}
```

Resolution: fixed
