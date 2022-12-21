# Issue 6297: fix LaTeX formatting in sage/schemes/elliptic_curves/period_lattice.py

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-06-15 11:40:09

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



---

Attachment


---

Comment by ncalexan created at 2009-06-15 20:31:04

Fine by me.


---

Comment by craigcitro created at 2009-06-18 00:07:53

Resolution: fixed
