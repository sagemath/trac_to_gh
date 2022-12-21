# Issue 6988: error building PDF version of reference manual on Sage 4.1.2.alpha2

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-09-22 16:52:09

Assignee: tba

As the subject says. I'm making this a blocker as it's critical to have both the HTML and PDF versions of every document in the standard documentation build without errors. We do distribute those documents separately from the source and binary tarballs.


---

Comment by jhpalmieri created at 2009-09-22 18:58:40

Changing assignee from tba to jhpalmieri.


---

Comment by jhpalmieri created at 2009-09-22 18:58:40

The issue is that in LaTeX, lists can only be nested four deep, and the file rings/ring.pyx had 6 levels of nesting.  The attached patch rephrases things so that there are only 4 levels of nesting again.


---

Comment by jhpalmieri created at 2009-09-22 18:58:40

Changing status from new to assigned.


---

Comment by mvngu created at 2009-09-22 19:24:40

Resolution: fixed


---

Attachment


---

Comment by mpatel created at 2009-09-22 20:11:06

I think #6885 is a duplicate.


---

Comment by mvngu created at 2009-09-27 09:29:37

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.
