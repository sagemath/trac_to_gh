# Issue 5293: tab-completion menu creates two copies of the choice made

Issue created by migration from https://trac.sagemath.org/ticket/5293

Original creator: mhampton

Original creation time: 2009-02-17 12:57:36

Assignee: tbd

In sage-3.3.rc0 (presumable from some patch in an alpha release) tab-completion is somewhat broken in the notebook.  If you tab-complete and there is more than one possible completion, if you choose from the drop-down menu and press enter you get the entire command repeated, for example:

QQ. [press tab, get menu, choose absolute_degree and press enter]
QQ.absolute_degreeQQ.absolute_degree

This is currently effecting sagenb's rc0, and has been confirmed on several other installs.

I am not sure where to begin to track this down, or what patch caused it.


---

Comment by mhampton created at 2009-02-17 12:57:52

Changing assignee from tbd to boothby.


---

Comment by mhampton created at 2009-02-17 12:57:52

Changing keywords from "" to "tab completion".


---

Comment by mhampton created at 2009-02-17 12:57:52

Changing component from algebra to notebook.


---

Comment by mhampton created at 2009-02-17 20:39:06

Changing priority from major to critical.


---

Comment by mhampton created at 2009-02-17 22:39:08

This seems to be caused by #4440. I am working on a patch now.


---

Comment by jason created at 2009-02-17 23:06:17

I am just confirming that this is caused by #4440.  I found this with the (very cool) hg bisect command and then hand-tested before/after the patch was committed.


---

Comment by mabshoff created at 2009-02-17 23:08:19

Fixed by reverting #4440 for now.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-17 23:08:19

Resolution: fixed


---

Attachment


---

Comment by boothby created at 2009-02-19 20:39:45

Resolution changed from fixed to 


---

Comment by boothby created at 2009-02-19 20:39:45

Changing status from closed to reopened.


---

Comment by boothby created at 2009-02-19 20:44:51

patch depends on #4440


---

Comment by mhampton created at 2009-02-19 21:24:51

This appears to fix the side-effects from #4440.  Patch applies to rc0, which still had #4440 applied.


---

Comment by mabshoff created at 2009-02-20 07:24:02

Merged in Sage 3.3.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 07:24:02

Resolution: fixed
