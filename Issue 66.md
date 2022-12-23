# Issue 66: notebook -- should be able export (=print) to latex/pdf/dvi

archive/issues_000066.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  robert.marik kcrisman kini\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/66\n\n",
    "created_at": "2006-09-17T21:48:12Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "title": "notebook -- should be able export (=print) to latex/pdf/dvi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/66",
    "user": "was"
}
```
Assignee: somebody

CC:  robert.marik kcrisman kini



Issue created by migration from https://trac.sagemath.org/ticket/66





---

archive/issue_comments_000339.json:
```json
{
    "body": "\n```\nOn 9/21/07, gani <bganapathi@earthlink.net> wrote:\n> Since I really wanted a nice print out of my worksheets with Latex\n> with all the fancy math intact, I decided to write a simple sed file\n> which works pretty well for me. It can be modified to handle any user-\n> specific html tags. The color of input/output boxes are currently blue/\n> red but can be also changed, along with the width of the box\n> surrounding the text (try framesep=3mm instead of 5mm for example).\n> However, it does involve going through a 3-step process.\n\nThat's actually a pretty good idea for a temporary workaround.  Thanks!\nCould you please resend the sed file as an attachment or post it somewhere\nonline, since it gets mangled by email?\n\n> 1. copy code from \"edit worksheet\" tab in your current worksheet into\n> file, say, worksheet_code.\n> 2. run \"sed -f file_with_sed_cmds worksheet_code > output.tex\" (see\n> below for contents in file_with_sed_cmds)\n> 3. Latex the resulting file output.tex. You can change the title, name\n> in \\title,  \\author command before this step.\n> \n> Let me know if this worked for you. Now if there is a way someone\n> could include it to automate the process from within Sage, it would be\n> great!\n\nYes, this could be easily automated (by those who know how)\nfrom within Sage by modifying some code that's part of the \nnotebook server. \n\n\n> \n> thanks!\n> \n> gani --\n> \n> ***file_with_sed_cmds******************** (copy from below - make sure\n> you start with the 1i\\\\\\document....)\n> \n> *************************************************************************************************************\n> 1i\\\\\\documentclass[letterpaper]{report} \\n \\\\usepackage[pdftex]\n> {graphicx,color} \\n \\\\usepackage[left=2cm,right=1cm,top=2cm,bottom=2cm]\n> {geometry} \\\\usepackage{fancyvrb} \\n \\\\begin{document} \\n \\\\title{Your\n> document title here} \\n \\\\author {Your name here} \\n \\\\maketitle \\n\n> \n> $a\\\\\\end{document} \\n\n> \n> s?<p>?\\\\newline ?ig\n> s?</p>??ig\n> s?<ol>?\\\\begin{itemize}?ig\n> s?</ol>?\\\\end{itemize}?ig\n> s?<li>?\\\\item?ig\n> s?^{{{?\\\\begin{Verbatim}[formatcom=\\\\color{blue}, frame = single,\n> framesep=5mm]?ig\n> s?\\}}}?\\\\end{Verbatim}?ig\n> s?<b>?\\\\bfseries ?ig\n> s?</b>?\\\\normalfont?ig\n> s?<i>?\\\\itshape ?ig\n> s?</i>?\\\\normalfont?ig\n> s?^///?\\\\end{Verbatim} \\n \\\\begin{Verbatim}[formatcom = \\\\color{red},\n> frame = single, framesep=5mm]?ig\n> s?<pre>??ig\n> s?</pre>??ig\n> s?<img src=\"?\\\\begin{figure}[!h] \\n \\\\begin{center} \\n \\\n> \\includegraphics[scale=0.5]{?ig\n> s?<img src = \"?\\\\begin{figure}[!h] \\n \\\\begin{center} \\n \\\n> \\includegraphics[scale=0.5]{?ig\n> s?\">?\\}\\n \\\\end{center} \\n \\\\end{figure}?ig\n> \n> \n> --~--~---------~--~----~------------~-------~--~----~\n> To post to this group, send email to sage-support@googlegroups.com\n> To unsubscribe from this group, send email to sage-support-unsubscribe@googlegroups.com\n> For more options, visit this group at http://groups.google.com/group/sage-support\n> URLs: http://sage.math.washington.edu/sage/ and http://sage.scipy.org/sage/\n> -~----------~----~----~----~------~----~------~--~---\n> \n> \n\n\n-- \nWilliam Stein\nAssociate Professor of Mathematics\nUniversity of Washington\nhttp://wstein.org\n\n```\n",
    "created_at": "2007-09-21T19:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-339",
    "user": "was"
}
```


```
On 9/21/07, gani <bganapathi@earthlink.net> wrote:
> Since I really wanted a nice print out of my worksheets with Latex
> with all the fancy math intact, I decided to write a simple sed file
> which works pretty well for me. It can be modified to handle any user-
> specific html tags. The color of input/output boxes are currently blue/
> red but can be also changed, along with the width of the box
> surrounding the text (try framesep=3mm instead of 5mm for example).
> However, it does involve going through a 3-step process.

That's actually a pretty good idea for a temporary workaround.  Thanks!
Could you please resend the sed file as an attachment or post it somewhere
online, since it gets mangled by email?

> 1. copy code from "edit worksheet" tab in your current worksheet into
> file, say, worksheet_code.
> 2. run "sed -f file_with_sed_cmds worksheet_code > output.tex" (see
> below for contents in file_with_sed_cmds)
> 3. Latex the resulting file output.tex. You can change the title, name
> in \title,  \author command before this step.
> 
> Let me know if this worked for you. Now if there is a way someone
> could include it to automate the process from within Sage, it would be
> great!

Yes, this could be easily automated (by those who know how)
from within Sage by modifying some code that's part of the 
notebook server. 


> 
> thanks!
> 
> gani --
> 
> ***file_with_sed_cmds******************** (copy from below - make sure
> you start with the 1i\\\document....)
> 
> *************************************************************************************************************
> 1i\\\documentclass[letterpaper]{report} \n \\usepackage[pdftex]
> {graphicx,color} \n \\usepackage[left=2cm,right=1cm,top=2cm,bottom=2cm]
> {geometry} \\usepackage{fancyvrb} \n \\begin{document} \n \\title{Your
> document title here} \n \\author {Your name here} \n \\maketitle \n
> 
> $a\\\end{document} \n
> 
> s?<p>?\\newline ?ig
> s?</p>??ig
> s?<ol>?\\begin{itemize}?ig
> s?</ol>?\\end{itemize}?ig
> s?<li>?\\item?ig
> s?^{{{?\\begin{Verbatim}[formatcom=\\color{blue}, frame = single,
> framesep=5mm]?ig
> s?\}}}?\\end{Verbatim}?ig
> s?<b>?\\bfseries ?ig
> s?</b>?\\normalfont?ig
> s?<i>?\\itshape ?ig
> s?</i>?\\normalfont?ig
> s?^///?\\end{Verbatim} \n \\begin{Verbatim}[formatcom = \\color{red},
> frame = single, framesep=5mm]?ig
> s?<pre>??ig
> s?</pre>??ig
> s?<img src="?\\begin{figure}[!h] \n \\begin{center} \n \
> \includegraphics[scale=0.5]{?ig
> s?<img src = "?\\begin{figure}[!h] \n \\begin{center} \n \
> \includegraphics[scale=0.5]{?ig
> s?">?\}\n \\end{center} \n \\end{figure}?ig
> 
> 
> --~--~---------~--~----~------------~-------~--~----~
> To post to this group, send email to sage-support@googlegroups.com
> To unsubscribe from this group, send email to sage-support-unsubscribe@googlegroups.com
> For more options, visit this group at http://groups.google.com/group/sage-support
> URLs: http://sage.math.washington.edu/sage/ and http://sage.scipy.org/sage/
> -~----------~----~----~----~------~----~------~--~---
> 
> 


-- 
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org

```




---

archive/issue_comments_000340.json:
```json
{
    "body": "Attachment\n\nthis is a sed file to do something useful.",
    "created_at": "2007-09-23T17:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-340",
    "user": "was"
}
```

Attachment

this is a sed file to do something useful.



---

archive/issue_comments_000341.json:
```json
{
    "body": "Changing component from basic arithmetic to notebook.",
    "created_at": "2008-01-27T05:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-341",
    "user": "AlexGhitza"
}
```

Changing component from basic arithmetic to notebook.



---

archive/issue_comments_000342.json:
```json
{
    "body": "Changing assignee from somebody to boothby.",
    "created_at": "2008-01-27T05:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-342",
    "user": "AlexGhitza"
}
```

Changing assignee from somebody to boothby.



---

archive/issue_comments_000343.json:
```json
{
    "body": "A C program to do conversion from HTML to LaTeX is available: \n[http://www.iwriteiam.nl/html2tex.html](http://www.iwriteiam.nl/html2tex.html). \n\nIt's available under the GPL. Also on that web page is a link to a Perl program that is supposed to be better. I'm not certain about the license of the Perl program.",
    "created_at": "2008-11-27T11:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-343",
    "user": "tjlahey"
}
```

A C program to do conversion from HTML to LaTeX is available: 
[http://www.iwriteiam.nl/html2tex.html](http://www.iwriteiam.nl/html2tex.html). 

It's available under the GPL. Also on that web page is a link to a Perl program that is supposed to be better. I'm not certain about the license of the Perl program.



---

archive/issue_comments_000344.json:
```json
{
    "body": "Look at the comment here at #2628.",
    "created_at": "2009-01-22T09:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-344",
    "user": "mhansen"
}
```

Look at the comment here at #2628.



---

archive/issue_comments_000345.json:
```json
{
    "body": "See also the sws2tex converter - http://bitbucket.org/whuss/sws2tex\n\nThe demo is at http://user.mendelu.cz/marik/sage/conversion.pdf",
    "created_at": "2010-08-24T20:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-345",
    "user": "robert.marik"
}
```

See also the sws2tex converter - http://bitbucket.org/whuss/sws2tex

The demo is at http://user.mendelu.cz/marik/sage/conversion.pdf



---

archive/issue_comments_000346.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2013-01-29T20:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-346",
    "user": "kcrisman"
}
```

Changing priority from minor to major.



---

archive/issue_comments_000347.json:
```json
{
    "body": "In principle, this is possible using one of TWO methods.\n* [sws2tex](https://bitbucket.org/whuss/sws2tex), which should probably just be merged into sage or sagenb eventually, plus latex\n* `sage -sws2rst` along with `sphinx-quickstart`, `sphinx-build`, and finally `make pdf`\nOne would have to automate these things and throw very good error messages in the event latex was not available, as it is only a recommended Sage dependency.   `sws2rst` has the advantage of keeping (2d) graphics, `sws2tex` the advantage of fewer steps.\n\nAlso, of course, it is possible to get a non-latex pdf and has been for a long, long time, but just by \"print\"ing the page, though this is surprisingly useful in informal contexts.",
    "created_at": "2014-11-20T13:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-347",
    "user": "kcrisman"
}
```

In principle, this is possible using one of TWO methods.
* [sws2tex](https://bitbucket.org/whuss/sws2tex), which should probably just be merged into sage or sagenb eventually, plus latex
* `sage -sws2rst` along with `sphinx-quickstart`, `sphinx-build`, and finally `make pdf`
One would have to automate these things and throw very good error messages in the event latex was not available, as it is only a recommended Sage dependency.   `sws2rst` has the advantage of keeping (2d) graphics, `sws2tex` the advantage of fewer steps.

Also, of course, it is possible to get a non-latex pdf and has been for a long, long time, but just by "print"ing the page, though this is surprisingly useful in informal contexts.



---

archive/issue_comments_000348.json:
```json
{
    "body": "See #17473 for sws2tex.",
    "created_at": "2014-12-09T02:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-348",
    "user": "kcrisman"
}
```

See #17473 for sws2tex.



---

archive/issue_comments_000349.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-04-04T18:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-349",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_000350.json:
```json
{
    "body": "Let us now close this, as the legacy sagenb is being phased out.",
    "created_at": "2018-04-04T18:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-350",
    "user": "chapoton"
}
```

Let us now close this, as the legacy sagenb is being phased out.



---

archive/issue_comments_000351.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-04-04T18:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-351",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_000352.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-352",
    "user": "vdelecroix"
}
```

closing positively reviewed duplicates



---

archive/issue_comments_000353.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/66",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/66#issuecomment-353",
    "user": "vdelecroix"
}
```

Resolution: wontfix
