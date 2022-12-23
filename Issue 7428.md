# Issue 7428: worksheets listed on published list only after they are republished, but not after initial publication

Issue created by migration from https://trac.sagemath.org/ticket/7428

Original creator: jason

Original creation time: 2009-11-11 07:31:12

Assignee: boothby

CC:  was

When I try to publish a worksheet, it does not initially show up in the list of published worksheets.  To reproduce, on sagenb.org:

1. Create a new worksheet
2. Click the Publish tab
3. Click "Yes"
4. Click the "Published" link at the very top right to look at the list of published worksheets.

The worksheet you just published should be up at the top of this list, but it's not.  This is the bug.
5. Navigate back to your worksheet
6. Click the publish tab again
7. Click "Re-publish worksheet"
8. Again click "Published" to go to the list of published worksheets

Now your worksheet is listed at the top of this list.


---

Comment by mpatel created at 2009-11-12 04:00:34

The problem appears to be the "Last Edited" field.


---

Attachment

Update "Last Edited" field for newly published worksheets.  Apply to sagenb repo.


---

Attachment

Added Selenium test.  Apply only this patch to sagenb repo.


---

Comment by mpatel created at 2009-11-12 14:00:49

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-11-12 14:01:50

Feel free to bump the milestone back to 4.3.


---

Comment by timdumol created at 2009-11-13 19:46:36

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2009-11-13 19:46:36

Patch and test work. Positive review.


---

Comment by was created at 2009-12-08 05:39:25

Resolution: fixed
