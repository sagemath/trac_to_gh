# Issue 6143: Upgrade tinyMCE to 3.2.4.1

Issue created by migration from https://trac.sagemath.org/ticket/6143

Original creator: jason

Original creation time: 2009-05-28 04:56:22

Assignee: mabshoff

CC:  rlm boothby tclemans was robertwb mhampton

An spkg is up at http://sage.math.washington.edu/home/jason/tinyMCE-3.2.4.1.spkg

The new version has lots and lots of bugfixes, including lots of fixes for Safari.  It also has a greatly improved paste-from-word functionality.


---

Comment by mpatel created at 2009-07-17 01:55:52

I downloaded the new package and installed it via `sage -i`.  TinyMCE seems to work for me just as it did previously, in Cr3, FF3.5, and O9 on Linux and Cr2, FF3.5, IE8, S4, and O9 on Windows XP.   However, I can't test the new spkg in any Mac OS browsers or with Word.  I did have success with the 'paste-from-Word' feature --- from OpenOffice.org Writer v3.0.1 on Linux.  In particular, I was able to "paste," through the dialog, tables and variously-formatted text.

The package contents conform to the [guidelines](http://wiki.sagemath.org/SPKG_Audit).

Pending a confirmation that it works properly on Macs, particularly in Safari, I give the new spkg a positive review.

For what it's worth, the patch at #6459 still works for me after the upgrade.


---

Comment by jason created at 2009-07-18 23:38:18

I'm CCing people that I know have macs or have worked on the notebook.  Can someone please check this spkg out on a mac?


---

Comment by jason created at 2009-07-30 09:47:51

CCing one more person that I know has a mac, in hopes that someone will review this ticket (i.e., apply the spkg and check to make sure tinymce works in Safari.)


---

Comment by mhampton created at 2009-07-30 14:30:54

Seems to work fine on my mac, with Safari and Firefox.  Based on the previous review I think I can change this to a positive review.


---

Comment by mvngu created at 2009-08-03 02:19:52

Resolution: fixed
