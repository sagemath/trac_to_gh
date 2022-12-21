# Issue 66: notebook -- should be able export (=print) to latex/pdf/dvi

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-17 21:48:12

Assignee: somebody

CC:  robert.marik kcrisman kini




---

Comment by was created at 2007-09-21 19:01:25


```
On 9/21/07, gani <bganapathi`@`earthlink.net> wrote:
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
> To post to this group, send email to sage-support`@`googlegroups.com
> To unsubscribe from this group, send email to sage-support-unsubscribe`@`googlegroups.com
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

Attachment

this is a sed file to do something useful.


---

Comment by AlexGhitza created at 2008-01-27 05:06:34

Changing component from basic arithmetic to notebook.


---

Comment by AlexGhitza created at 2008-01-27 05:06:34

Changing assignee from somebody to boothby.


---

Comment by tjlahey created at 2008-11-27 11:44:01

A C program to do conversion from HTML to LaTeX is available: 
[http://www.iwriteiam.nl/html2tex.html](http://www.iwriteiam.nl/html2tex.html). 

It's available under the GPL. Also on that web page is a link to a Perl program that is supposed to be better. I'm not certain about the license of the Perl program.


---

Comment by mhansen created at 2009-01-22 09:36:59

Look at the comment here at #2628.


---

Comment by robert.marik created at 2010-08-24 20:33:00

See also the sws2tex converter - http://bitbucket.org/whuss/sws2tex

The demo is at http://user.mendelu.cz/marik/sage/conversion.pdf


---

Comment by kcrisman created at 2013-01-29 20:22:15

Changing priority from minor to major.


---

Comment by kcrisman created at 2014-11-20 13:36:35

In principle, this is possible using one of TWO methods.
 * [sws2tex](https://bitbucket.org/whuss/sws2tex), which should probably just be merged into sage or sagenb eventually, plus latex
 * `sage -sws2rst` along with `sphinx-quickstart`, `sphinx-build`, and finally `make pdf`
One would have to automate these things and throw very good error messages in the event latex was not available, as it is only a recommended Sage dependency.   `sws2rst` has the advantage of keeping (2d) graphics, `sws2tex` the advantage of fewer steps.

Also, of course, it is possible to get a non-latex pdf and has been for a long, long time, but just by "print"ing the page, though this is surprisingly useful in informal contexts.


---

Comment by kcrisman created at 2014-12-09 02:28:06

See #17473 for sws2tex.


---

Comment by chapoton created at 2018-04-04 18:10:11

Changing status from new to needs_review.


---

Comment by chapoton created at 2018-04-04 18:10:11

Let us now close this, as the legacy sagenb is being phased out.


---

Comment by chapoton created at 2018-04-04 18:11:10

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix
