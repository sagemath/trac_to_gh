# Issue 7871: Mis-specified background color for interacts

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-01-08 09:28:36

Assignee: was

CC:  kcrisman timdumol

IE 7/8 use a bluish background color for `interact` tables, instead of white.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/d3feb880dcecfcb6#).


---

Attachment

Fix CSS color.  sagenb repo.


---

Comment by mpatel created at 2010-01-08 09:35:53

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-08 09:35:53

The patch is minimal, but it seems to work for me in IE8 on Windows XP.  I'll clean up and move `interact` CSS directives to the main stylesheet in a separate ticket.


---

Comment by kcrisman created at 2010-01-08 15:31:01

Still looks good on FF3.5, Safari 4, and Chrome on a Mac.  At least, I think I changed it - unfortunately, this HTML doesn't show up in View->Source, and I'm not sure where to look for it - what is the relevant CSS file name in the rendered worksheet directory?  Probably someone should check on FF on Windows and Linux, but the one-character change seems fine.


---

Comment by mpatel created at 2010-01-08 16:08:51

The markup is inserted dynamically.  To view live changes in Safari / Chrome, evaluate an `interact` cell, right-click on the output, and select "Inspect Element."  This should open the "Web Inspector" / "Developer Tools," which should also be available under some menu (the location and name depend on the browser, OS, etc.).  Anyway, try browsing to the cell under "Elements" (an instantaneous tree-like representation of the page).

Opera and IE8 have similar, built-in tools.  For Firefox, I suggest installing the [Firebug extension](http://getfirebug.com/).


---

Comment by kcrisman created at 2010-01-08 16:50:19

Great, I just needed to check that I actually HAD made the change for real and not just in some file deep in the site-packages directory.   So positive review, modulo someone other than the author of the patch testing it on IE.


---

Comment by kcrisman created at 2010-01-11 20:48:25

Finally got to test it on IE 7 - great catch!


---

Comment by kcrisman created at 2010-01-11 20:48:25

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-01-12 21:01:24

merged into sagenb-0.5.


---

Comment by was created at 2010-01-12 21:01:24

Resolution: fixed
