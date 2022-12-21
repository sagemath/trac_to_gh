# Issue 1288: misformating of some of the reference manual in live version; also out of date

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-27 14:09:36

Assignee: tba

See below.  I suspect that the best solution is to remove this stuff about "sage -advanced" from the reference manual entirely, since it is always going to get out of date, hence be misleading.  It's much better to just described how "sage -advanced" works, and suggest that the user try it out, then improve the output of "sage -advanced". 



```
Reading 2.3 of the Reference Manual from the Notebook interface, I find that this "live" version has turned the lines:

\item
\verb+-advanced+ Lists additional options:

\begin{verbatim}
$ sage -advanced
in devel/doc-main/ref/options.tex into

<li><code>-advanced</code> Lists additional options:

<p>
<div class="verbatim"><pre><span class="math"> sage -advanced

in localhost:8000/doc/live/ref/node7.html , which, of course, completely wrecks the formatting.  There seems to be no problem with the pre-built  devel/doc-main/html/ref/node7.html , where latex2html has correctly turned the TeX into

<LI><code>-advanced</code> Lists additional options:

<P>
<div class="verbatim"><pre>
$ sage -advanced


Moreover, the list of options given in options.tex is considerably different from those currently produced by sage -advanced .


Mac OS X 10.4.11
Sage 2.8.14

-- 

Francis Clarke
```



---

Comment by mhansen created at 2007-12-06 21:15:10

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-06 21:15:10

Changing assignee from tba to mhansen.


---

Attachment


---

Comment by mabshoff created at 2007-12-09 10:39:11

Looks good to me. Initially I was confused about this since it seemed to only remove content until I read William's comments.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-09 10:40:17

Resolution: fixed


---

Comment by mabshoff created at 2007-12-09 10:40:17

Merged in 2.9.alpha2.
