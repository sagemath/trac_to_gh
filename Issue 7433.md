# Issue 7433: notebook: changing title of worksheet changes title of corresponding published worksheet

Issue created by migration from https://trac.sagemath.org/ticket/7433

Original creator: was

Original creation time: 2009-11-11 22:14:15

Assignee: boothby

CC:  was mpatel

This is a really weird bug. 

1. Create a worksheet W and publish it to make a published worksheet P.  Do *not* check "Automatically re-publish when changes are made". 

2. Change the title of W and something in the body of W.  Notice that in the list of published worksheets the title of P doesn't change.  However, click on P in that list, and notice that the title *does* change at the top of the worksheet.  The body doesn't change, fortunately. 


---

Attachment

Fixes template bug.


---

Comment by timdumol created at 2009-11-14 13:16:56

The problem was with a template bug referencing the original worksheet's title instead of the published worksheet's title. Patch up. I'll add the tests later (or whoever else wants to)


---

Attachment

Fixes template bug and adds Selenium tests.


---

Comment by timdumol created at 2009-11-14 16:49:23

Alright, tests and template fix up.


---

Comment by timdumol created at 2009-11-14 16:49:23

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2009-12-08 20:55:16

This works fine for me and fixes the problem. 

I haven't verified that the selenium tests work, since I can't run Selenium yet on my OS X computer. 

Note that the patch needed to be rebased for me, so I've posted a rebased patch.


---

Comment by was created at 2009-12-08 20:55:16

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-09 01:07:13

merged into sagenb-0.4.6


---

Comment by was created at 2009-12-09 01:07:13

Resolution: fixed
