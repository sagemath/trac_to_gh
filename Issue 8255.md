# Issue 8255: update SageTeX spkg to 2.2.3.p0 to fix spkg-check script

Issue created by migration from https://trac.sagemath.org/ticket/8255

Original creator: ddrake

Original creation time: 2010-02-13 13:42:58

Assignee: tbd

The SageTeX spkg shipped in 4.3.2 has a slightly broken spkg-check: if LaTeX is present, but the tkz-berge.sty file isn't, the example file included with SageTeX cannot be typeset and spkg-check fails. Since I don't assume the user has LaTeX installed, I shouldn't assume that tkz-berge.sty is either.

There are also some documentation fixes, including notably an "egrep" which should be "egrep -v"!

Finally, the license for the documentation is now CC BY-SA; I've dropped the noncommercial clause.

The new spkg is version 2.2.3.p0 in http://sage.math.washington.edu/home/drake/code/sage/st/ . The last version of the spkg is available in the same place, for ease of reviewing.


---

Comment by ddrake created at 2010-02-13 13:43:26

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-02-15 06:25:34

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-02-15 06:25:34

Could you modify the file `spkg-check` to conform to the portability issues at #8255? For example, the following line in `spkg-check` is not recommended:

```
if [ "$(which latex)" -a "$(kpsewhich tkz-berge.sty)" ]
```



---

Comment by ddrake created at 2010-02-15 09:46:43

Replying to [comment:2 mvngu]:
> Could you modify the file `spkg-check` to conform to the portability issues at #8255?

I'm guessing you didn't mean to refer to _this_ ticket... :)


---

Comment by mvngu created at 2010-02-15 09:50:09

Replying to [comment:3 ddrake]:
> I'm guessing you didn't mean to refer to _this_ ticket... :)

Let's pretend I was referring to #7632 :-)


---

Comment by ddrake created at 2010-02-15 10:27:29

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2010-02-15 10:27:29

Thanks for the link. Ironically, I put in "-a" in an effort to be more portable...thanks for setting me straight. I've replaced the spkg with an updated one. Please review.


---

Comment by mvngu created at 2010-02-20 15:36:31

I had something like this in mind:

```diff
diff -r 2d39ee3a7530 -r e739e330a66a spkg-check
--- a/spkg-check
+++ b/spkg-check
@@ -29,8 +29,7 @@
     fi
 }
 
-if [ "$(which latex)" && "$(kpsewhich tkz-berge.sty)" ]
-then
+if [ "$(which latex)" ] && [ "$(kpsewhich tkz-berge.sty)" ]; then
     cd src
 
     typeset example.tex
```

It would be good if the ticket number is referenced in the hg log.


---

Comment by ddrake created at 2010-02-21 06:38:21

Okay, fixed. New version reflects your suggestions.

BTW, how did you get that diff in your comment?


---

Comment by mvngu created at 2010-02-21 08:36:01

Replying to [comment:7 ddrake]:
> BTW, how did you get that diff in your comment? 

See the [Wiki Processors](http://trac.sagemath.org/sage_trac/wiki/WikiProcessors) section.


---

Comment by jhpalmieri created at 2010-03-01 23:19:29

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-03-01 23:19:29

spkg-check tests whether latex is present, and then it actually runs pdflatex.  I suppose that anyone who has latex will have pdflatex also, but I think this should be fixed anyway: if latex is not found, sage-check exits gracefully, but in the unlikely event that latex is found but pdflatex isn't, then I get

```
Running the test suite.
./spkg-check: line 10: pdflatex: command not found
Error typesetting example.tex! To fully test SageTeX, make sure
LaTeX can find sagetex.sty, and that TikZ (version 2.00
or newer), tkz-berge.sty and tkz-graph.sty is installed.
*************************************
Error testing package ** sagetex-2.2.3.p0 **
*************************************
```

Can we run latex instead of pdflatex?  Otherwise, change "which latex" to "which pdflatex", and maybe change the error message from "LaTeX isn't installed" to "PDFLaTeX isn't installed"?

Also, something is wrong with the shell script on Solaris but I don't know what.  If I log into t2.math.washington.edu and try installing with SAGE_CHECK equal to 1, then I get the bad error message even though latex is not found.  Maybe this is because on many systems, 'which latex' produces nothing if latex isn't found, but on t2, 'which latex' does this:

$ which latex                                          
no latex in /usr/local/gcc-4.4.1-sun-linker/bin /usr/local/bin2 /usr/bin /usr/ccs/bin /usr/local/bin /usr/sfw/bin /bin /usr/sbin


---

Comment by ddrake created at 2010-03-02 00:15:30

Replying to [comment:9 jhpalmieri]:
> spkg-check tests whether latex is present, and then it actually runs pdflatex.  I suppose that anyone who has latex will have pdflatex also, but I think this should be fixed anyway:

In TeXLive (and teTeX), "latex" and "pdflatex" are just symlinks to pdftex (or pdfetex), so it seems really unlikely that someone would have "latex" but not "pdflatex". But your idea is correct; I'll change it.

By the way, is that a real example? Do you have a system with latex but not pdflatex? I'm curious to know about it.

> Also, something is wrong with the shell script on Solaris but I don't know what.  If I log into t2.math.washington.edu and try installing with SAGE_CHECK equal to 1, then I get the bad error message even though latex is not found.  Maybe this is because on many systems, 'which latex' produces nothing if latex isn't found, but on t2, 'which latex' does this:
> 
> $ which latex                                          
> no latex in /usr/local/gcc-4.4.1-sun-linker/bin /usr/local/bin2 /usr/bin /usr/ccs/bin /usr/local/bin /usr/sfw/bin /bin /usr/sbin

This is a more serious problem. I'll look into it. Hopefully it gives a useful return code or something.


---

Comment by jhpalmieri created at 2010-03-02 00:49:14

Replying to [comment:10 ddrake]:
> By the way, is that a real example? Do you have a system with latex but not pdflatex? I'm curious to know about it.

It was a contrived example: I renamed pdflatex temporarily but kept latex around.


---

Comment by ddrake created at 2010-03-02 02:07:38

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2010-03-02 02:07:38

New spkg up for review at http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.2.3.p0.spkg.

The spkg-check script now simply tries running latex and kpsewhich, and checks the return code to see if it worked. I think this is more portable, as returning 0 for success is pretty standard. It also uses "latex" throughout, and doesn't use "pdflatex".


---

Comment by jhpalmieri created at 2010-03-02 02:41:55

Looks good to me.  It works on systems on which latex and/or tkz-berge.sty is not installed.  I also created a bug in the file example.tex and rebuilt the spkg, and indeed, it didn't pass tests.

Tested on sage.math, a Mac running OS X 10.6, and t2.math.


---

Comment by jhpalmieri created at 2010-03-02 02:41:55

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-03 15:05:58

Resolution: fixed


---

Comment by mvngu created at 2010-03-03 15:05:58

Merged [sagetex-2.2.3.p0.spkg](http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.2.3.p0.spkg) in the standard spkg repository.
