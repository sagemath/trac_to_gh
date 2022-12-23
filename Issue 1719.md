# Issue 1719: problems building documentation

archive/issues_001719.json:
```json
{
    "body": "Assignee: tba\n\n\n```\nI've managed to solve the problem: The package\ntexlive-cyrillic (in Debian/Ubuntu) is needed to build the Sage\ndocumentation.\n\nPablo\n\nEl Tuesday 01 January 2008 21:25:35 Pablo De Napoli escribi\u00f3:\n- Show quoted text -\n> When building Sage documentation\n> (make in devel/doc), I've got a strange message\n> (I quote below the output)\n>\n> <output>\n>\n> TEXINPUTS=/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/commontex\n>: python\n> /media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/tools/mkhowto\n> --html --about html/stdabout.dat --iconserver ../icons --favicon\n> ../icons/pyfav.png --address \"See <i><a href=\\\"about.html\\\">About this\n> document...</a></i> for information on suggesting changes.\" --up-link\n> ../index.html --up-title \"SAGE Documentation Index\" --global-module-index\n> \"../modindex.html\" --dvips-safe --dir html/ref ref/ref.tex\n> +++\n> TEXINPUTS=/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/ref:/medi\n>a/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/commontex:/media/hda2/pab\n>lo.new_home/sage/sage-2.9/devel/doc-main/paper-letter:/media/hda2/pablo.new_\n>home/sage/sage-2.9/devel/doc-main/texinputs: +++ latex ref\n> *** Session transcript and error messages are\n> in\n> /media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/html/ref/ref.how.\n> *** Exited with status 1.\n> The relevant lines from the transcript are:\n> ------------------------------------------------------------------------\n> +++ latex ref\n> This is pdfTeXk, Version 3.141592-1.40.3 (Web2C 7.5.6)\n>  %&-line parsing enabled.\n> entering extended mode\n> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/ref/ref.tex\n> LaTeX2e <2005/12/01>\n> Babel <v3.8h> and hyphenation patterns for english, usenglishmax, dumylang,\n> noh\n> yphenation, spanish, catalan, galician, spanish, catalan, galician, loaded.\n> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/texinputs/manual.c\n>ls Document Class: manual 1998/03/03 Document class (Python manual)\n> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/texinputs/pypaper.\n>sty)\n>\n> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/texinputs/fancybox\n>.sty Style option: `fancybox' v1.3 <2000/09/19> (tvz)\n> ) (/usr/share/texmf-texlive/tex/latex/base/report.cls\n> Document Class: report 2005/09/16 v1.4f Standard LaTeX document class\n> (/usr/share/texmf-texlive/tex/latex/base/size12.clo))\n> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/texinputs/fancyhdr\n>.sty )\n> Using fancier footers than usual.\n>\n> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/texinputs/fncychap\n>.sty )\n> Using fancy chapter headings.\n> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/texinputs/python.s\n>ty (/usr/share/texmf-texlive/tex/latex/tools/longtable.sty)\n> (/usr/share/texmf-texlive/tex/latex/tools/verbatim.sty)\n> (/usr/share/texmf-texlive/tex/latex/graphics/color.sty\n> (/etc/texmf/tex/latex/config/color.cfg)\n> (/usr/share/texmf-texlive/tex/latex/graphics/dvips.def)\n> (/usr/share/texmf-texlive/tex/latex/graphics/dvipsnam.def))))\n> (/usr/share/texmf-texlive/tex/latex/base/textcomp.sty\n> (/usr/share/texmf-texlive/tex/latex/base/ts1enc.def))\n> (/usr/share/texmf-texlive/tex/latex/amsmath/amsmath.sty\n> For additional information on amsmath, use the `?' option.\n> (/usr/share/texmf-texlive/tex/latex/amsmath/amstext.sty\n> (/usr/share/texmf-texlive/tex/latex/amsmath/amsgen.sty))\n> (/usr/share/texmf-texlive/tex/latex/amsmath/amsbsy.sty)\n> (/usr/share/texmf-texlive/tex/latex/amsmath/amsopn.sty))\n> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/commontex/macros.t\n>ex (/usr/share/texmf-texlive/tex/latex/tools/xspace.sty))\n> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/commontex/boilerpl\n>ate. tex\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1719\n\n",
    "created_at": "2008-01-08T08:22:53Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "problems building documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1719",
    "user": "was"
}
```
Assignee: tba


```
I've managed to solve the problem: The package
texlive-cyrillic (in Debian/Ubuntu) is needed to build the Sage
documentation.

Pablo

El Tuesday 01 January 2008 21:25:35 Pablo De Napoli escribió:
- Show quoted text -
> When building Sage documentation
> (make in devel/doc), I've got a strange message
> (I quote below the output)
>
> <output>
>
> TEXINPUTS=/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/commontex
>: python
> /media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/tools/mkhowto
> --html --about html/stdabout.dat --iconserver ../icons --favicon
> ../icons/pyfav.png --address "See <i><a href=\"about.html\">About this
> document...</a></i> for information on suggesting changes." --up-link
> ../index.html --up-title "SAGE Documentation Index" --global-module-index
> "../modindex.html" --dvips-safe --dir html/ref ref/ref.tex
> +++
> TEXINPUTS=/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/ref:/medi
>a/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/commontex:/media/hda2/pab
>lo.new_home/sage/sage-2.9/devel/doc-main/paper-letter:/media/hda2/pablo.new_
>home/sage/sage-2.9/devel/doc-main/texinputs: +++ latex ref
> *** Session transcript and error messages are
> in
> /media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/html/ref/ref.how.
> *** Exited with status 1.
> The relevant lines from the transcript are:
> ------------------------------------------------------------------------
> +++ latex ref
> This is pdfTeXk, Version 3.141592-1.40.3 (Web2C 7.5.6)
>  %&-line parsing enabled.
> entering extended mode
> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/ref/ref.tex
> LaTeX2e <2005/12/01>
> Babel <v3.8h> and hyphenation patterns for english, usenglishmax, dumylang,
> noh
> yphenation, spanish, catalan, galician, spanish, catalan, galician, loaded.
> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/texinputs/manual.c
>ls Document Class: manual 1998/03/03 Document class (Python manual)
> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/texinputs/pypaper.
>sty)
>
> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/texinputs/fancybox
>.sty Style option: `fancybox' v1.3 <2000/09/19> (tvz)
> ) (/usr/share/texmf-texlive/tex/latex/base/report.cls
> Document Class: report 2005/09/16 v1.4f Standard LaTeX document class
> (/usr/share/texmf-texlive/tex/latex/base/size12.clo))
> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/texinputs/fancyhdr
>.sty )
> Using fancier footers than usual.
>
> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/texinputs/fncychap
>.sty )
> Using fancy chapter headings.
> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/texinputs/python.s
>ty (/usr/share/texmf-texlive/tex/latex/tools/longtable.sty)
> (/usr/share/texmf-texlive/tex/latex/tools/verbatim.sty)
> (/usr/share/texmf-texlive/tex/latex/graphics/color.sty
> (/etc/texmf/tex/latex/config/color.cfg)
> (/usr/share/texmf-texlive/tex/latex/graphics/dvips.def)
> (/usr/share/texmf-texlive/tex/latex/graphics/dvipsnam.def))))
> (/usr/share/texmf-texlive/tex/latex/base/textcomp.sty
> (/usr/share/texmf-texlive/tex/latex/base/ts1enc.def))
> (/usr/share/texmf-texlive/tex/latex/amsmath/amsmath.sty
> For additional information on amsmath, use the `?' option.
> (/usr/share/texmf-texlive/tex/latex/amsmath/amstext.sty
> (/usr/share/texmf-texlive/tex/latex/amsmath/amsgen.sty))
> (/usr/share/texmf-texlive/tex/latex/amsmath/amsbsy.sty)
> (/usr/share/texmf-texlive/tex/latex/amsmath/amsopn.sty))
> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/commontex/macros.t
>ex (/usr/share/texmf-texlive/tex/latex/tools/xspace.sty))
> (/media/hda2/pablo.new_home/sage/sage-2.9/devel/doc-main/commontex/boilerpl
>ate. tex

```


Issue created by migration from https://trac.sagemath.org/ticket/1719





---

archive/issue_comments_010894.json:
```json
{
    "body": "Oh, the solution should probably just to add this to a README.txt file\netc. under hte devel/doc directory.  Trivial to do..",
    "created_at": "2008-01-08T08:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1719#issuecomment-10894",
    "user": "was"
}
```

Oh, the solution should probably just to add this to a README.txt file
etc. under hte devel/doc directory.  Trivial to do..



---

archive/issue_comments_010895.json:
```json
{
    "body": "Apply to the doc repository",
    "created_at": "2008-08-13T14:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1719#issuecomment-10895",
    "user": "jason"
}
```

Apply to the doc repository



---

archive/issue_comments_010896.json:
```json
{
    "body": "Attachment\n\nBoy, that was easy.  Adding the appropriate package took care of at least this error for me on Ubuntu Hardy.",
    "created_at": "2008-08-13T14:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1719#issuecomment-10896",
    "user": "jason"
}
```

Attachment

Boy, that was easy.  Adding the appropriate package took care of at least this error for me on Ubuntu Hardy.



---

archive/issue_comments_010897.json:
```json
{
    "body": "Looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-15T06:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1719#issuecomment-10897",
    "user": "mabshoff"
}
```

Looks good to me.

Cheers,

Michael



---

archive/issue_comments_010898.json:
```json
{
    "body": "Merged in Sage 3.1.rc0",
    "created_at": "2008-08-15T06:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1719#issuecomment-10898",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.rc0



---

archive/issue_comments_010899.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-15T06:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1719#issuecomment-10899",
    "user": "mabshoff"
}
```

Resolution: fixed
