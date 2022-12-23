# Issue 5029: Better diffs for trac

Issue created by migration from https://trac.sagemath.org/ticket/5029

Original creator: robertwb

Original creation time: 2009-01-19 20:17:13

Assignee: schilly

I got tired of not knowing what (new) file /dev/null is when reviewing tickets, or being able to see the hg comments, so I updated the hg plugin to show this info. I'm using this for trac.cython.org. 

This just needs to go into the plugin directory of this trac server, and then restart the trac server. Make sure the filename matches the python version (e.g. py2.4 or py2.5), just rename it if not. 


---

Attachment


---

Comment by schilly created at 2009-01-19 20:40:50

Changing assignee from schilly to mabshoff.


---

Comment by schilly created at 2009-01-19 20:40:50

`@`mabshoff: this is probably for you since you are managing the trac server.


---

Comment by schilly created at 2009-01-19 20:40:50

Changing type from defect to enhancement.


---

Comment by mhansen created at 2009-01-19 22:12:03

Also, the Trac 0.11 series has a diff viewer that shows this information.  Are we switching after SD12?


---

Comment by robertwb created at 2009-01-19 22:58:34

Oh, I didn't know that. However we do it, it would be really handy.


---

Comment by mhansen created at 2009-01-24 12:29:06

I installed this on the Trac server, but it doesn't seem to work.


---

Comment by was created at 2009-01-24 12:53:33

Resolution: fixed


---

Comment by mvngu created at 2009-01-26 08:58:56

> I got tired of not knowing what (new) file /dev/null is when reviewing tickets, or being able to see the hg comments,


Thanks, Robert, for raising this issue and have it fixed. With trac now able to display diff comments, it has made my life easier when it comes to crediting patch authors. Previously, I would need to download a patch in raw text format in order to see the patch author's name (and I'm bad at spelling people's names).
