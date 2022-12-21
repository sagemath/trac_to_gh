# Issue 7201: overflow: auto CSS on code cells

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-10-13 14:41:07

Assignee: boothby

CC:  was timdumol

Every now and then, the auto-expansion of code cells doesn't quite get all of the code, which leads to frustration because you can't see the last line or two of your code in a cell.  I think this has happened when the code on a line wraps to the next line maybe (I don't have an example of it happening right now).

Anyways, putting scroll bars on the code cells using the overflow attribute (so they're only there when they are needed) is an easy way to guard against errors in the auto-expansion code.


---

Comment by mpatel created at 2009-11-01 01:31:41

Potentially useful jQuery plug-ins:

 * [autoResize](http://james.padolsey.com/javascript/jquery-plugin-autoresize/).
 * [Elastic](http://www.unwrongest.com/projects/elastic/).
 * [Autogrow for jEditable](http://www.appelsiini.net/2008/4/autogrow-textarea-for-jeditable) or just [Autogrow](http://www.aclevercookie.com/facebook-like-auto-growing-textarea/)


---

Comment by mpatel created at 2009-11-19 21:20:15

Ticket #2902 is related.


---

Attachment


---

Comment by jason created at 2010-05-13 11:42:26

Patch is for the sagenb repository.


---

Comment by jason created at 2010-05-13 11:42:26

Changing status from new to needs_review.


---

Attachment

Edits the SASS source files too.


---

Comment by timdumol created at 2010-07-05 10:14:07

Looks ok to me. Here's a reviewer patch that edits the SASS source files as well. If the reviewer patch is alright, positive review.


---

Comment by jason created at 2010-09-28 21:05:24

Looks good to me.


---

Comment by jason created at 2010-09-28 21:05:24

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-09-28 21:13:06

Well, after using it for a bit---in FF 3.6 on OSX, every time I press enter in a cell, the cell momentarily flashes a scrollbar before auto-resizing.  This makes all of the text jump just a bit, which is very jarring.  So I'm going to put this ticket as needs work until that issue is taken care of.


---

Comment by jason created at 2010-09-28 21:13:06

Changing status from positive_review to needs_work.


---

Comment by kcrisman created at 2014-12-19 05:02:29

In addition, for some reason in the current notebook this breaks new cell creation by clicking.  Apparently - ?  I may have done something wrong.


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid
