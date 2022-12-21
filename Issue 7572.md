# Issue 7572: Memleak in GLPK interface

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-12-01 15:53:33

Assignee: tbd

CC:  ncohen

The GLPK interface `sage_malloc`s various arrays and never frees them. Also the interface uses Python keywords as variable names.


---

Comment by malb created at 2009-12-01 15:54:16

Changing status from new to needs_review.


---

Attachment

The attached patch is for the GLPK SPKG.


---

Comment by ncohen created at 2009-12-01 16:09:12

Thank you for your help !!! just one question though : on which version of GLPK is your patch based ? The new version of GLPK is available in #7268 and still waiting for review... Could we merge your changes in ? :-)

I had no idea that "id" was a python keyword... And thank you for noticing this memory leak !

Nathann


---

Comment by ncohen created at 2009-12-01 16:09:12

Changing status from needs_review to needs_info.


---

Comment by malb created at 2009-12-01 16:11:24

Replying to [comment:2 ncohen]:
> Thank you for your help !!! just one question though : on which version of GLPK is your patch based ? The new version of GLPK is available in #7268 and still waiting for review... Could we merge your changes in ? :-)

Sure, I'll take a look at #7268.
 
> I had no idea that "id" was a python keyword... And thank you for noticing this memory leak !
 
Me neither, but Emacs noticed it :) I think there's still a memleak there, you `new glp_ioct` but never `delete` it. However, I couldn't find anything on `glp_ioct` anywhere.


---

Comment by ncohen created at 2009-12-01 16:13:23

This could be deleted as part of the whole GLPK version of the LP syste, though... But it could be good to take a look at it, indeed :-)

Nathann


---

Comment by malb created at 2009-12-01 17:05:10

This is now fixed in #7268


---

Comment by malb created at 2009-12-01 17:05:10

Resolution: duplicate
