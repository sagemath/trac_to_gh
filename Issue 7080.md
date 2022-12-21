# Issue 7080: include new separated sage notebook in Sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-30 08:44:26

Assignee: boothby

First we will just include this in a way that still technically allows one to use the old notebook.  In a future version of sage we'll remove support for the old version of the notebook.  

Note that the new notebook spkg includes jmol and jquery in it's sagenb/data directory (it's distutils package data).   But we'll do things in two phases:

  (1) include new notebook, but leave all the old stuff there, which is redundant but safe,

  (2) delete old stuff in a future version of sage

This ticket has an spkg and a patch to the core Sage library (to change the notebook(...) command).

  * http://sage.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.2.spkg

  * the patches are attached as patches. 




---

Attachment


---

Comment by was created at 2009-10-14 16:11:31

Resolution: fixed
