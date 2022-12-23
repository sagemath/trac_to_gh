# Issue 8683: add randstate to the reference manual

Issue created by migration from https://trac.sagemath.org/ticket/8683

Original creator: mvngu

Original creation time: 2010-04-13 23:44:34

Assignee: mvngu

CC:  rhinton jason jhpalmieri

As the subject says. See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/277c49764bb2aea) thread for the request and some background information.


---

Comment by mvngu created at 2010-04-13 23:46:12

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-04-14 01:51:47

reviewer patch


---

Attachment

I have attached a reviewer patch that includes the following changes:

 * Some stylistic clean-ups.
 * Get rid of trailing white spaces.
 * Put in some headings to make the organization of the module clear when you're skimming the reference manual.
 * Some cross-referencing within the Sage library.

John's patch is OK by me. If my reviewer patch is OK, then the whole ticket gets a positive review.


---

Comment by jhpalmieri created at 2010-04-14 17:33:51

Thanks for cleaning up my patch.  I don't know what you have against semicolons, but otherwise your reviewer patch is fine. :)


---

Comment by jhpalmieri created at 2010-04-14 17:33:51

Changing status from needs_review to positive_review.


---

Attachment

(just changing the commit message on the patch)


---

Comment by jhpalmieri created at 2010-04-16 18:57:38

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-16 18:57:38

Merged in 4.4.alpha0:
 - trac_8683-randstate.2.patch
 - trac_8683-reviewer.patch
