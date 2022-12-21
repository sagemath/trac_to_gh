# Issue 2141: Access to file list on notebook.

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-02-11 20:43:28

Assignee: boothby

Currently the Notebook produces a list of files it doesn't know how to handle at the bottom of cell output. Sometimes it would be useful to be able to grab the files that are rendered as well (e.g. see  http://groups.google.com/group/sage-newbie/browse_thread/thread/859e20cc33a29930 )


---

Comment by was created at 2008-02-12 05:33:17

It would be very nice if somebody could actually propose what this would look like?  It could be annoying if every image has a big link next to it...


---

Comment by robertwb created at 2008-02-12 05:39:50

I would imagine a link at the very bottom that says "File list..." and links to the cell (where twisted will give a nice directory browser). Perhaps some files could trigger this, and others not (for example, it's easy to drag/grab an image, but something like jmol is a bit harder. I agree we don't want something super intrusive.


---

Comment by malb created at 2009-01-22 23:07:54

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2014-12-10 20:44:20

See https://github.com/sagemath/sagenb/issues/297


---

Comment by kcrisman created at 2014-12-10 20:44:20

Changing priority from major to minor.


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid
