# Issue 7060: notebook -- templating patch introduces numerous bugs

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-29 03:13:33

Assignee: boothby

I realized that sage-4.1.2.alpha4 contains Tim Dumol's notebook patch, and many patches on top of that... but in separating the notebook off we found that that patch contains many errors which causes at least 6 serious bugs.  

Our options:

   * revert that patch and everything on top of it.

   * switch to the new separated notebook for sage-4.1.2.

This is unfortunate and is entirely my fault since I refereed this notebook templating code, and though I did try everything in the notebook, I clearly wasn't sufficiently careful.   Sorry people.


---

Comment by jason created at 2009-09-29 07:44:38

so what patch was this (i.e., ticket number)?


---

Comment by timdumol created at 2009-09-29 15:24:31

Replying to [comment:1 jason]:
> so what patch was this (i.e., ticket number)?

#6568. The template problems are being found, and hopefully we can backport the fixes to the old notebook, if we are not to switch to the new separated notebook.


---

Comment by was created at 2009-10-14 16:08:38

This is fixed by switching to the new notebook.


---

Comment by was created at 2009-10-14 16:08:38

Resolution: fixed
