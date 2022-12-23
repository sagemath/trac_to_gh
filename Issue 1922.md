# Issue 1922: change and update lprint

Issue created by migration from https://trac.sagemath.org/ticket/1922

Original creator: jason

Original creation time: 2008-01-25 08:03:08

Assignee: was

This is an update for lprint().

  * renamed to pretty_print_default()
  * _show_hook is now pretty_print()

Both functions are smarter now.

Someone (me?) should go through latex.py and clean it out.  There are lots of other functions like jsMath(), typeset(), etc. that all appear to do the same thing.


---

Comment by jason created at 2008-01-25 08:03:35

Changing component from algebraic geometry to notebook.


---

Comment by jason created at 2008-01-25 08:03:35

Changing assignee from was to boothby.


---

Attachment


---

Comment by was created at 2008-01-27 17:30:06

looks good.


---

Comment by mabshoff created at 2008-01-27 18:58:16

Resolution: fixed


---

Comment by mabshoff created at 2008-01-27 18:58:16

Merged in Sage 2.10.1.rc2
