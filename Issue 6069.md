# Issue 6069: Blank notebook page when loading URL for published sheet that is AWOL

Issue created by migration from Trac.

Original creator: khorton

Original creation time: 2009-05-18 13:16:06

Assignee: somebody

CC:  acleone robert.marik

If someone attempts to access a URL for a published worksheet that no longer exists (perhaps because the URL changed when the worksheet went through a published to unpublished to published cycle), or the URL was mistyped, they get a blank page titled "Error | Sage Notebook", with no hint on what to do to resolve the problem.

If they are trying to access a published worksheet that cannot be found, it is probably useful to redirect to the page with the list of published worksheets, perhaps after showing an error message like "There is no worksheet currently available at this URL. You will be redirected to the <a href='URL of published worksheets index'>index of published worksheets</a> in 15 seconds."

This may be related to ticket 5988:

http://trac.sagemath.org/sage_trac/ticket/5988


---

Attachment

This says that "There is no published worksheet with name '%s'" instead.


---

Comment by timdumol created at 2010-01-18 19:54:19

I think the previous message "The user 'pub' has no worksheet '%s'" was a bit confusing, but it does work. Feel free to ignore the patch and close this.


---

Comment by timdumol created at 2010-01-18 19:54:19

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-20 03:10:45

Redirect to `pub/` after delay.  Apply only this patch.  sagenb repo.


---

Attachment

V2 is an attempt to set up redirection.  It should also ensure for `guest` users that the error page does not include the full top bar (Settings, Log, etc.).

Feel free to make changes.


---

Comment by mpatel created at 2010-01-25 04:45:02

V2 applies cleanly to #8051 + #7784 + #5712.


---

Comment by mpatel created at 2010-02-14 01:26:12

Better titles for non-Error pages.  Apply only this patch.


---

Attachment

V3 should

 * Fix #8234.
 * Use a title more appropriate than `Error` for certain non-Error pages (see the patch).
 * Make "Sign Out" redirect to "/" when `require_login=False`.  This is better than returning a page whose header refers to a user named "None" and has a broken "Home" link!


---

Comment by mpatel created at 2010-02-14 01:32:26

Changing priority from major to blocker.


---

Comment by timdumol created at 2010-03-12 01:58:37

Patel's changes look great. Anyone mind signing off mine?


---

Comment by mpatel created at 2010-03-12 18:26:11

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-23 04:41:38

(I'm not changing any notebook code in Sage 4.4.)


---

Comment by timdumol created at 2010-05-04 04:42:50

Resolution: fixed
