# Issue 150: if foo is a pyrex function then foo?? should give the source code

Issue created by migration from https://trac.sagemath.org/ticket/150

Original creator: was

Original creation time: 2006-10-25 09:09:22

Assignee: was




---

Comment by was created at 2006-10-25 09:10:52

OK, I created this just to mark it off. 

I solved this by adding a new option to Pyrex that embeds the source location
in the generated Pyrex code.  I think modified IPython slightly, and finally
wrote a new display of source hook that uses the embeded Pyrex info.

It works!

For SAGE-1.4.2


---

Comment by was created at 2006-10-25 09:10:52

Resolution: fixed
