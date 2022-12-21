# Issue 4099: Fix documentation for point2d, line2d, ...

Issue created by migration from Trac.

Original creator: anakha

Original creation time: 2008-09-11 02:41:34

Assignee: tba

Since #3853, the documentation for the *2d functions in plot/plot.py is outdated.  

It refers to things like point.options and line.reset which are gone and produce errors when you try to access them.

If I had the time I would do a patch for this, but I am currently swamped with other work.


---

Attachment

The patch just nukes all mention of .options and .reset.  So far as I can tell, this functionality is gone without replacement.  If there is now some other way to learn what these attributes used to tell you, then this patch should probably not be accepted, and the doc should be rewritten to explain the new functionality.


---

Comment by jwmerrill created at 2008-09-14 02:56:21

Changing assignee from tba to jwmerrill.


---

Comment by mhansen created at 2008-09-19 00:12:33

I think this is good for now.


---

Comment by mabshoff created at 2008-09-19 03:19:32

Merged in Sage 3.1.3.alpha0


---

Comment by mabshoff created at 2008-09-19 03:19:32

Resolution: fixed
