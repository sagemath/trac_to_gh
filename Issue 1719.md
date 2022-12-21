# Issue 1719: problems building documentation

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-08 08:22:53

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



---

Comment by was created at 2008-01-08 08:23:43

Oh, the solution should probably just to add this to a README.txt file
etc. under hte devel/doc directory.  Trivial to do..


---

Comment by jason created at 2008-08-13 14:55:33

Apply to the doc repository


---

Attachment

Boy, that was easy.  Adding the appropriate package took care of at least this error for me on Ubuntu Hardy.


---

Comment by mabshoff created at 2008-08-15 06:42:54

Looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-15 06:47:47

Merged in Sage 3.1.rc0


---

Comment by mabshoff created at 2008-08-15 06:47:47

Resolution: fixed
