# Issue 2769: matplotlib produces invalid PDFs with axes=False

Issue created by migration from https://trac.sagemath.org/ticket/2769

Original creator: ddrake

Original creation time: 2008-04-02 06:31:26

Assignee: was

Keywords: pdf, plot, matplotlib, axes

When saving plots without axes, matplotlib produces invalid PDFs:


```
p = plot(x^2, x, 0, 1)
p.save('withaxes.pdf')
p.save('withoutaxes.pdf', axes=False)
```


the second file is not valid; if you use it in a LaTeX document, it makes the text shrink for the rest of the page -- see the attached PDF. If you try to convert withoutaxes.pdf to postscript using pdf2ps, you get:


```
drake@sansu5:~$ pdf2ps withoutaxes.pdf 
   **** Warning: File has imbalanced q/Q operators (too many q's)

   **** This file had errors that were repaired or ignored.
   **** The file was produced by: 
   **** >>>> matplotlib pdf backend <<<<
   **** Please notify the author of the software that produced this
   **** file that it does not conform to Adobe's published PDF
   **** specification.
```


This is probably a matplotlib problem, and I think it's [been noticed and fixed in the most recent version](http://www.nabble.com/Problem-with-matplotlib-and-pdflatex-td16210144.html).


---

Attachment


---

Comment by mhansen created at 2008-09-02 20:14:51

Resolution: fixed


---

Comment by mhansen created at 2008-09-02 20:14:51

This has been fixed by #3392.
