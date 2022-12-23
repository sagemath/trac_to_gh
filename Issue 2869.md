# Issue 2869: Cell sizing is broken

Issue created by migration from https://trac.sagemath.org/ticket/2869

Original creator: boothby

Original creation time: 2008-04-09 23:50:44

Assignee: boothby

Cells with funny input (i.e., long lines or long words) don't get sized nicely.  Worse, cells containing the character '<' are totally broken.


---

Attachment


---

Comment by was created at 2008-04-10 16:37:21

REFEREE REPORT:
  * Very good, simple, etc.  Excellent!

  * It's still very slow when the textarea gets full, esp. on Safari.  That's a separate issue though.


---

Comment by mabshoff created at 2008-04-10 16:46:02

Resolution: fixed


---

Comment by mabshoff created at 2008-04-10 16:46:02

Merged in Sage 3.0.alpha4


---

Attachment


---

Comment by boothby created at 2008-04-17 18:29:28

Patch was only partially applied to alpha4.  Posted rebase.


---

Comment by mabshoff created at 2008-04-17 18:32:23

Yeah, something went very, very wrong. Applied 2869-resizer_rebase-alpha5.patch - sorry boothby ;)

Cheers,

Michael
