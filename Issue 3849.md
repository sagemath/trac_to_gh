# Issue 3849: notebook -- Internal Server Error given when input to File upload or Data attachment is invalid

Issue created by migration from https://trac.sagemath.org/ticket/3849

Original creator: TimothyClemans

Original creation time: 2008-08-14 12:54:59

Assignee: boothby

(1) In Google Docs if one fills in both "Browse your computer ..." and "Or enter the url of a ...", the server just deals with the first input box. The Notebook instead deals with the second. Do what Google does.

(2) Google uses JavaScript alert boxes to report errors. The Notebook just gives a "Internal Server Error." The Notebook should do inline error reporting just as is done on the Registration page.


---

Comment by TimothyClemans created at 2008-08-14 12:55:18

Changing status from new to assigned.


---

Comment by TimothyClemans created at 2008-08-14 12:55:18

Changing assignee from boothby to TimothyClemans.


---

Comment by TimothyClemans created at 2008-08-14 12:59:36

Error reporting does exist for file extension errors. However, it is not inline.


---

Attachment


---

Comment by TimothyClemans created at 2008-08-14 13:32:03

Took care of (1) and also now clicking "Upload Worksheet" when form blank no longer displays "Internal Server Error."


---

Attachment

Forget about this code.  This is an important error though.

The attached patch sagenb_3849-part1.patch I think completely fixes all such problems for uploading a *worksheet*, but doesn't do anything about Data-->Upload or attach file.

I'm making Data -->Upload or attach a file a new ticket: #7495


---

Comment by was created at 2009-11-20 00:36:37

Changing status from needs_work to needs_review.


---

Attachment


---

Attachment

Version 2.  Added backlink.  Apply only this patch to the sagenb repo.


---

Comment by mpatel created at 2009-11-20 07:33:48

Version 2:

 * Adds a link back to the upload page.
 * `sage-support` --> `sage-support group`.

My review, to the extent it counts, is positive.


---

Comment by timdumol created at 2009-12-06 07:48:36

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2009-12-06 07:48:36

Replying to [comment:7 mpatel]:
> [...]
> My review, to the extent it counts, is positive.

I'm giving this a positive review. Everything works fine.


---

Comment by was created at 2009-12-08 05:29:34

Resolution: fixed


---

Comment by was created at 2009-12-08 05:29:34

merged into sage-4.3
