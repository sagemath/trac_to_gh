# Issue 850: graphs: create graph by specifying vertices and a function giving adjacencies

Issue created by migration from https://trac.sagemath.org/ticket/850

Original creator: jason

Original creation time: 2007-10-11 15:33:15

Assignee: was

Keywords: graphs

It would be very useful to be able to create a graph by giving a list of vertices and a function which specified the adjacencies.  See the doc examples in the patch for several examples.


---

Attachment


---

Comment by jason created at 2007-10-11 15:37:42

I just noticed that the comment in the DiGraph __init__ function should be changed from: 

                # Pass XGraph a dict of lists describing the adjacencies
to
                # Pass XDiGraph a dict of lists describing the adjacencies

Sorry.


---

Comment by was created at 2007-10-13 07:25:44

Resolution: fixed
