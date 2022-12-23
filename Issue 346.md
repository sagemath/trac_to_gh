# Issue 346: Notebook input cell focus

Issue created by migration from https://trac.sagemath.org/ticket/346

Original creator: nbruin

Original creation time: 2007-04-03 21:04:31

Assignee: boothby

In Firefox 1.5 (which is still what ships standard with, say Redhat), the following happens:
If I select text by dragging in a cell that currently does not have input focus, then the cell that did have focus loses it, but the cell in which I select the text does not gain focus.

The result is that the usual reflex for deleting the selection (press backspace) doesn't get sent to the cell but to the browser window, where it means the back button!

If I first put the cell in focus and then select the text, things work as expected, so there is a work-around. However, it does involve unlearning a reflex that works almost everywhere else. The penalty, getting sent to the previously visited page, is also a rather shocking experience.

I understand that this behaviour might be out of the control of sage, but it would be nice if you could work around it.





---

Comment by nbruin created at 2007-04-05 00:51:50

Changing priority from minor to major.


---

Comment by nbruin created at 2007-04-05 00:51:50

Upgraded to major. I'm running into this problem all the time and since other programs reinforce the behaviour, the habit does not go away. I think it's enough for me to abandon using the notebook.


---

Comment by was created at 2007-08-19 02:08:19

This isn't a bug but a feature request.


---

Comment by was created at 2007-08-19 02:08:19

Changing type from defect to enhancement.


---

Comment by boothby created at 2008-03-17 04:48:58

Resolution: invalid


---

Comment by boothby created at 2008-03-17 04:48:58

This hasn't been an issue since we removed syntax hilighting.
