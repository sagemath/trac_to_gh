# Issue 6930: [with patch, needs review] make 3d axes labels a little more precise

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-09-15 04:03:52

Assignee: was

CC:  was robertwb wcauchois

The frame labels on this plot look completely wrong, since they are only printed with 0 digits after the decimal.  The attached patch makes frames with small ranges print with one decimal after the decimal, which makes this plot look all right.


---

Attachment


---

Comment by mvngu created at 2009-09-23 23:03:10

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:53:02

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
