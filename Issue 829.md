# Issue 829: edit() always puts the editor into the background

Issue created by migration from https://trac.sagemath.org/ticket/829

Original creator: justin

Original creation time: 2007-10-05 05:57:41

Assignee: was

The new edit() command in SAGE forces the chosen editor into the background.  I'm not sure of the ramifications, but I have a change to the command that does the following: if DISPLAY is set in the user's environment, the assumption is that the editor will work with X (the window system).  Since the default 'emacs' in Mac OS X does not work with X, the result is that edit() terminates prematurely, complaining that standard output is not a tty.

My fix is to retain the current behavior only if DISPLAY is set.  Otherwise, the editor command is invoked as a "foreground" task, not a background task.



---

Comment by justin created at 2007-10-05 05:58:56

Resolution: invalid


---

Comment by justin created at 2007-10-05 05:58:56

FIddle.  Somehow, I submitted it twice.  Somehow, I submitted it twice.


---

Comment by mabshoff created at 2007-10-05 22:41:19

Resolution changed from invalid to 


---

Comment by mabshoff created at 2007-10-05 22:41:19

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-10-05 22:41:39

Resolution: invalid
