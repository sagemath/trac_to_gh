# Issue 5626: when %latex goes bad in the notebook, it doesn't display the debug/error log anymore

archive/issues_005626.json:
```json
{
    "body": "Assignee: boothby\n\nA user posted this:\n\n\n```\nHi,\n\nI try the following in my first cell in a new notebook with sage-3.4\nand the latest Ubuntu 64bit os.\n\n------------------------------------\n%latex\nTry this: $$x^2=-1$$.\n------------------------------------\nevaluate\n\nAn error occured.\nError latexing slide.\n\n-------------------------------------\n(new cell)\n-------------------------------------\n\nThats all I get.  I don't get any other latex log output, and it\ndoesn't write any sage*.dvi files.  I've noticed in the sage-support\n```\n\n\nThen I responded to explicitly pass in the debug option and ...\n\n\n```\nOn Sat, Mar 28, 2009 at 6:55 PM, J Elaych <> wrote:\n>\n>\n>> What happens if you type this at the command line:\n>>\n>> sage: sage.misc.latex.Latex().eval('Try this: $$x^2=-1$$.',0,0,debug=True)\n>>\n>> William\n>\n> Awesome, thanks.   Latex wasn't finding 'fullpage.sty' so I installed\n> 'dblatex' via\n> Ubuntu, which in turn installed tons of latex packages, including ../\n> preprint/fullpage.sty.\n> I see that you have helped other people find fullpage.sty before, but\n> the real\n> help for me was the pointer to the sage.misc.latex.Latex().eval()\n> command.\n>\n> Thanks again,\n\nIt's a bug that you didn't get a traceback in the first place.  It's possible thatthis bug was maybe introduced by John Palmieri in this patch:\n\nhttp://hg.sagemath.org/sage-main/rev/b6c770bd40f8\n\nBut it could have also been introduced in a subsequent patch...\n\n\n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5626\n\n",
    "created_at": "2009-03-29T01:40:00Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "when %latex goes bad in the notebook, it doesn't display the debug/error log anymore",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5626",
    "user": "https://github.com/williamstein"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/5626





---

archive/issue_comments_043844.json:
```json
{
    "body": "This seems to be fixed for me, can someone else test this?\n\nTo test - rename a necessary .sty file:\n\n```\n$ cd /usr/share/texmf-texlive/tex/latex/amsmath\n$ sudo mv amsmath.sty amsmath.sty.BLAH\n```\n\n\nThen trying to execute:\n\n```\n%latex\nTry this: $$x^2=-1$$.\n```\n\n\nGives\n\n```\nAn error occurred.\nThis is pdfTeXk, Version 3.141592-1.40.3 (Web2C 7.5.6) (format=latex\n2009.12.24)  18 JAN 2010 18:08\nentering extended mode\n %&-line parsing enabled.\n**\\nonstopmode \\input{sage31.tex}\n(./sage31.tex (/usr/share/texmf-texlive/tex/latex/base/article.cls\nDocument Class: article 2005/09/16 v1.4f Standard LaTeX document class\n(/usr/share/texmf-texlive/tex/latex/base/size10.clo\nFile: size10.clo 2005/09/16 v1.4f Standard LaTeX file (size option)\n)\n\\c@part=\\count79\n\\c@section=\\count80\n\\c@subsection=\\count81\n\\c@subsubsection=\\count82\n\\c@paragraph=\\count83\n\\c@subparagraph=\\count84\n\\c@figure=\\count85\n\\c@table=\\count86\n\\abovecaptionskip=\\skip41\n\\belowcaptionskip=\\skip42\n\\bibindent=\\dimen102\n)\n\n! LaTeX Error: File `amsmath.sty' not found.\n\nType X to quit or <RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n<read *> \n         \nl.2 \\usepackage\n               {amssymb}^^M\n*** (cannot \\read from terminal in nonstop modes)\n\n \nHere is how much of TeX's memory you used:\n 200 strings out of 95087\n 2124 string characters out of 1183277\n 46102 words of memory out of 1500000\n 3462 multiletter control sequences out of 10000+50000\n 3640 words of font info for 14 fonts, out of 1200000 for 2000\n 28 hyphenation exceptions out of 8191\n 24i,0n,17p,186b,36s stack positions out of\n5000i,500n,6000p,200000b,5000s\nNo pages of output.\n\nNone\n```\n\n\nDon't forget to rename amsmath.sty back after testing.",
    "created_at": "2010-01-19T02:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5626#issuecomment-43844",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

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

archive/issue_events_005867.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:00:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5626",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5626#event-5867"
}
```



---

archive/issue_comments_043845.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T03:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5626#issuecomment-43845",
    "user": "https://github.com/TimDumol"
}
```

Resolution: duplicate
