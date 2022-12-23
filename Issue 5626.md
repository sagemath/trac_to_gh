# Issue 5626: when %latex goes bad in the notebook, it doesn't display the debug/error log anymore

Issue created by migration from https://trac.sagemath.org/ticket/5626

Original creator: was

Original creation time: 2009-03-29 01:40:00

Assignee: boothby

A user posted this:


```
Hi,

I try the following in my first cell in a new notebook with sage-3.4
and the latest Ubuntu 64bit os.

------------------------------------
%latex
Try this: $$x^2=-1$$.
------------------------------------
evaluate

An error occured.
Error latexing slide.

-------------------------------------
(new cell)
-------------------------------------

Thats all I get.  I don't get any other latex log output, and it
doesn't write any sage*.dvi files.  I've noticed in the sage-support
```


Then I responded to explicitly pass in the debug option and ...


```
On Sat, Mar 28, 2009 at 6:55 PM, J Elaych <> wrote:
>
>
>> What happens if you type this at the command line:
>>
>> sage: sage.misc.latex.Latex().eval('Try this: $$x^2=-1$$.',0,0,debug=True)
>>
>> William
>
> Awesome, thanks.   Latex wasn't finding 'fullpage.sty' so I installed
> 'dblatex' via
> Ubuntu, which in turn installed tons of latex packages, including ../
> preprint/fullpage.sty.
> I see that you have helped other people find fullpage.sty before, but
> the real
> help for me was the pointer to the sage.misc.latex.Latex().eval()
> command.
>
> Thanks again,

It's a bug that you didn't get a traceback in the first place.  It's possible thatthis bug was maybe introduced by John Palmieri in this patch:

http://hg.sagemath.org/sage-main/rev/b6c770bd40f8

But it could have also been introduced in a subsequent patch...



 -- William
```



---

Comment by acleone created at 2010-01-19 02:20:51

This seems to be fixed for me, can someone else test this?

To test - rename a necessary .sty file:

```
$ cd /usr/share/texmf-texlive/tex/latex/amsmath
$ sudo mv amsmath.sty amsmath.sty.BLAH
```


Then trying to execute:

```
%latex
Try this: $$x^2=-1$$.
```


Gives

```
An error occurred.
This is pdfTeXk, Version 3.141592-1.40.3 (Web2C 7.5.6) (format=latex
2009.12.24)  18 JAN 2010 18:08
entering extended mode
 %&-line parsing enabled.
**\nonstopmode \input{sage31.tex}
(./sage31.tex (/usr/share/texmf-texlive/tex/latex/base/article.cls
Document Class: article 2005/09/16 v1.4f Standard LaTeX document class
(/usr/share/texmf-texlive/tex/latex/base/size10.clo
File: size10.clo 2005/09/16 v1.4f Standard LaTeX file (size option)
)
\c@part=\count79
\c@section=\count80
\c@subsection=\count81
\c@subsubsection=\count82
\c@paragraph=\count83
\c@subparagraph=\count84
\c@figure=\count85
\c@table=\count86
\abovecaptionskip=\skip41
\belowcaptionskip=\skip42
\bibindent=\dimen102
)

! LaTeX Error: File `amsmath.sty' not found.

Type X to quit or <RETURN> to proceed,
or enter new name. (Default extension: sty)

Enter file name: 
! Emergency stop.
<read *> 
         
l.2 \usepackage
               {amssymb}^^M
*** (cannot \read from terminal in nonstop modes)

 
Here is how much of TeX's memory you used:
 200 strings out of 95087
 2124 string characters out of 1183277
 46102 words of memory out of 1500000
 3462 multiletter control sequences out of 10000+50000
 3640 words of font info for 14 fonts, out of 1200000 for 2000
 28 hyphenation exceptions out of 8191
 24i,0n,17p,186b,36s stack positions out of
5000i,500n,6000p,200000b,5000s
No pages of output.

None
```


Don't forget to rename amsmath.sty back after testing.


---

Comment by timdumol created at 2010-01-19 03:00:00

Resolution: duplicate
