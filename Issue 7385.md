# Issue 7385: renaming "Untitled" published pages

Issue created by migration from https://trac.sagemath.org/ticket/7385

Original creator: jason

Original creation time: 2009-11-03 20:59:04

Assignee: boothby

When I go to this published page:

http://www.sagenb.org/home/pub/924/

It asks me about renaming the page, presumably because it's titled "Untitled".

Of course, this is silly; it's not my page, and it's a static published page anyway.


---

Comment by timdumol created at 2009-11-04 11:20:28

This makes the check only occur in non-published pages.


---

Comment by timdumol created at 2009-11-04 11:22:17

Changing status from new to needs_review.


---

Attachment

This patch should fix your problem. This depends on #7309 and #7310.


---

Comment by mpatel created at 2009-11-04 12:02:10

The patch looks good to and works for me.


---

Comment by mpatel created at 2009-11-04 12:02:10

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-11 22:15:20

merged into sagenb-0.4.2 (sage-4.2.1)


---

Comment by was created at 2009-11-11 22:15:20

Resolution: fixed
