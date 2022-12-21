# Issue 8328: clisp rather than ecl mentioned on web page.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-02-22 19:20:49

Assignee: mvngu

http://www.sagemath.org/doc/tutorial/interfaces.html
says:

"Maxima is included with Sage, as is clisp (a version of the Lisp language)."

Clearly this is wrong. 

It would be worth going over the web site with a recursive grep, to see if there are any other mentions of clisp or Vmware, as I believe there are a few points where VMware is mentioned, despite the fact there is a shift to VirtualBox. 

Dave 


---

Attachment

based on Sage 4.3.3


---

Comment by mvngu created at 2010-02-26 02:20:21

The patch [trac_8328-tutorial.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8328/trac_8328-tutorial.patch) only fixes that one issue reported in the ticket description. I did a recursive grep over all `.rst` files in the following documentation, looking for occurrences of "clisp" and "VMware", and other variations in spelling:

 * A Tour of Sage
 * Bordeaux 2008 lecture
 * Constructions Document
 * Developer's Guide
 * Installation Guide
 * Numerical Guide
 * Tutorial

And I only found the occurrences as fixed in the patch.


---

Comment by mvngu created at 2010-02-26 02:20:21

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-02-26 02:26:31

I thought I'd seen VMware somewhere - it might have been on the Wiki. 

Anyway, that looks good to me.


---

Comment by drkirkby created at 2010-02-26 02:26:31

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-02 22:06:42

Resolution: fixed
