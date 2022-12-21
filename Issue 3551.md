# Issue 3551: magma_version command

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2008-07-05 11:39:11

Assignee: tba

The magma_version command is not documented; I would suggest that it say "this command returns a tuple of the form ((int,int,int),str) giving the version numbers, and it depends on having magma installed".

It also actually calls magma (to ask it its version number, I think). Would it be worth storing the version information in a file somewhere to aviod having to start a magma session?


---

Comment by mhansen created at 2008-07-05 23:16:18

You can't store it in a file since the Magma version on any given system could be different.

That being said, lots of functions in sage/interfaces/ need to be documented.


---

Comment by was created at 2008-07-07 00:16:00

> It also actually calls magma (to ask it its version number, I think). Would it be worth storing the 
> version information in a file somewhere to aviod having to start a magma session? 

Also, it would suddenly give a wrong answer as soon as one changes their magma version, which presumably happens a lot. 

William


---

Comment by was created at 2008-07-07 00:16:14

Changing type from defect to enhancement.


---

Comment by was created at 2008-10-23 16:34:39

This was now closed by some other magma documentation patch that is in 3.1.4.


---

Comment by was created at 2008-10-23 16:34:39

Resolution: fixed
