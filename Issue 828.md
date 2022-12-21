# Issue 828: edit() always puts the editor into the background

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2007-10-05 05:56:32

Assignee: was

The new edit() command in SAGE forces the chosen editor into the background.  I'm not sure of the ramifications, but I have a change to the command that does the following: if DISPLAY is set in the user's environment, the assumption is that the editor will work with X (the window system).  Since the default 'emacs' in Mac OS X does not work with X, the result is that edit() terminates prematurely, complaining that standard output is not a tty.

My fix is to retain the current behavior only if DISPLAY is set.  Otherwise, the editor command is invoked as a "foreground" task, not a background task.



---

Comment by justin created at 2007-10-05 05:57:01

Patch file fixing an edit() problem


---

Attachment

I don't think the DISPLAY variable is a good indication. Even when DISPLAY is set, if the editor is vi then running it in the background is a bad idea.
I would propose:
 * if a full template is supplied, then take it as the user gives it
 * if you're trying to guess from the "EDITOR" variable, you'll have to look up
how to pass a line number anyway. For each of these editors you know whether an & makes sense, and this is independent of the &


---

Comment by nbruin created at 2007-10-05 07:44:22

sorry. Why can't I edit my comments? I meant "independent of the value of EDITOR".


---

Comment by was created at 2007-10-13 07:33:16

Resolution: invalid


---

Comment by was created at 2007-10-13 07:33:16

I don't think this is needed -- it was only need for the old version...
