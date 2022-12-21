# Issue 1923: Make an obvious checkbox or menu to switch on pretty printing in the notebook

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-01-25 08:15:33

Assignee: was

We ought to have a very obvious, easy-to-use switch to switch on or off pretty printing in the notebook.  This request is related to the updated work done in #1922 .

Something like a checkbox up by the menus would be great.


---

Comment by jason created at 2008-01-25 17:57:14

Changing assignee from was to boothby.


---

Comment by jason created at 2008-01-25 17:57:14

Changing component from algebraic geometry to notebook.


---

Comment by jason created at 2008-01-25 19:32:47

Apply this after the patch in #1922 (or change the executed command to "lprint()" in the sage.eval() )


---

Attachment


---

Comment by was created at 2008-01-27 17:29:00

I'm OK, with this temporarily, except I would like "[ ] Format output" replaced by "[ ] Typeset output".  Format output is too vague. 

I think the checkbox doesn't look like anything else in the interface.  But it is OK until something better is suggested.

Another issue is that typing pretty_print_default(True) doesn't change the state
of the checkbox.  This is something that will get reported as a bug, but again
I do not think it's a show stopper.  So I think this patch should be applied with the
phrase "Format output" replaced by "Typeset output".  

William


---

Attachment

Apply this instead of pretty-print-checkbox.patch


---

Comment by jason created at 2008-01-28 15:26:52

I've updated the patch to change Format output to Typeset output.

Dynamically updating the checkbox will require some way for the embedded sage session to communicate directly with the notebook or will require some command to be run after every evaluation (which seems bad).  This is linked to the much bigger issue (and momentum) of having interactive widgets in the notebook and I don't think the fix will be trivial.

I'm not sure if the state of the checkbox is actually saved with the notebook or how that works.  I'll be working on that soon.  Do I need for the setting to appear when the "text" version of the worksheet is shown?

I think this (updated) patch ought to go in as a start on full functionality (meaning saving the state and restoring the state when the worksheet is saved, putting the value in the text form of the worksheet, etc.).


---

Comment by was created at 2008-01-29 12:30:40

I think this should go into Sage as is.   More should be done at some point, but isn't needed now.  Already this is very useful (and I do use it now in fact!)


---

Comment by mabshoff created at 2008-01-29 12:38:20

Resolution: fixed


---

Comment by mabshoff created at 2008-01-29 12:38:20

Merged prettyprint-checkbox-updated.patch in Sage 2.10.1.rc3
