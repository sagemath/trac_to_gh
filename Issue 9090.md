# Issue 9090: Interactive matrix_viewer(...)

Issue created by migration from https://trac.sagemath.org/ticket/9090

Original creator: acleone

Original creation time: 2010-05-29 22:52:27

Assignee: acleone

CC:  acleone

Adds an interactive matrix viewer to the notebook.

Requires: #8758


---

Comment by jdemeyer created at 2017-07-04 13:56:37

What is an "interactive matrix viewer"?


---

Comment by kcrisman created at 2017-07-05 15:20:44

My guess is that this might be something that allows easy input of a matrix, as with the `graph_editor`?  That would certainly be useful (in TeXShop I use something analogous all the time to relieve the tedium of typing in LaTeX matrices).  Don't know for sure, though.


---

Comment by jdemeyer created at 2017-07-05 15:56:43

Well, we have `input_grid` (both in SageNB and Jupyter) which can do this. The only potential caveat is that the size is fixed: you need to specify the number of rows and columns in advance.


---

Comment by kcrisman created at 2017-07-05 16:46:18

In interacts, yes? Maybe this was originally opened to allow this outside of interacts ... honestly I don't know, but your caveat sounds like a reasonable goal for this ticket.


---

Comment by jdemeyer created at 2017-07-06 09:55:22

Right... the thing with Jupyter widgets is that one can use the widgets without interacts. Essentially ``@`interact` is built up from widgets, for example setting up the auto-evaluation when a widget changes.

With SageNB on the other hand, controls (the SageNB term for widgets) cannot live by themselves. They require ``@`interact` to be used.
