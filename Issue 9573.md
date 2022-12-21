# Issue 9573: Error building the PDF reference manual

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-22 04:52:45

Assignee: mvngu

CC:  novoselt vbraun davidloeffler

Building the PDF reference manual for the forthcoming Sage 4.5.2.alpha0 on sage.math, I get

```
[4610] [4611]
Underfull \hbox (badness 10000) in paragraph at lines 373276--373277

[4612] [4613] [4614] [4615] [4616] [4617] [4618]
(/usr/share/texmf-texlive/tex/latex/ucs/data/uni-4.def)
! Undefined control sequence.
\u-default-1065 #1->\CYRSHCH

l.373945 ...`@`PYGaB["]`@`PYGaB[Щ`@`_45]`@`PYGaB["]`@`rb[])

?
```

The problem _may_ be in `schemes/generic/toric_variety.py` (cf. #8988).


---

Comment by mpatel created at 2010-07-22 04:54:24

[Here](http://sage.math.washington.edu/home/mpatel/trac/9573/reference.log) is the full pdflatex log.


---

Comment by novoselt created at 2010-07-22 04:59:48

Changing assignee from mvngu to novoselt.


---

Comment by novoselt created at 2010-07-22 04:59:48

I'll fix this. It is a cool non-alphanumeric symbol "Щ" that cannot be used as a variable name...


---

Comment by mpatel created at 2010-07-22 05:01:14

Out of curiosity: Does it help to replace `r"""` with `ur"""` for the relevant docstring?


---

Attachment

Replying to [comment:3 mpatel]:
> Out of curiosity: Does it help to replace `r"""` with `ur"""` for the relevant docstring?

I don't know, but I think using "`@`" here as an example of an unacceptable character is more robust and appropriate.

I apologize for the caused problem.


---

Comment by novoselt created at 2010-07-22 05:25:39

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-07-22 05:51:14

No need to apologize!


---

Comment by novoselt created at 2010-07-22 06:08:05

I am still getting an error, although a different one. I am not sure if it is related since I didn't have a pdf version before. Working...


---

Comment by novoselt created at 2010-07-22 06:08:05

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-07-22 07:00:46

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-07-22 07:00:46

OK, looks like a false alarm. I have done the following:

 * Removed doc/output in a sage-4.5.1 installation.
 * Built PDF-documentation without any patches applied.
 * Applied all merged toric patches and the patch on this ticket.
 * Build PDF-documentation again. Is seems to be OK in the sense that I got back to the shell prompt, there is a big PDF file in output, and I can see the modified example there just fine.

Please test it with 4.5.2.alpha0.


---

Comment by jhpalmieri created at 2010-07-23 00:24:20

Looks good to me.  PDF builds successfully, output looks fine.


---

Comment by jhpalmieri created at 2010-07-23 00:24:20

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-23 02:22:44

Resolution: fixed
