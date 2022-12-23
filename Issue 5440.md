# Issue 5440: Failure to restart %magma in notebook.

Issue created by migration from https://trac.sagemath.org/ticket/5440

Original creator: kohel

Original creation time: 2009-03-05 16:26:39

Assignee: boothby

In the notebook, if one does:

  %magma 
  quit;

then

  %magma
  1+1

one gets an error (the terminated magma process 
apparently does not get restarted).

It works fine in the shell.


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets
