# Issue 5459: Notebook and worksheet autosave intervals, excessive snapshots

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-03-09 03:54:45

Assignee: somebody

CC:  chapoton

Keywords: notebook worksheet autosave snapshots

There is a notebook configuration item indexed by 'save_interval'.  This can be set at the sage command line by instantiating a notebook object (call it "nb") and issuing commands like 
`nb.conf()['save_interval'] = int(3600)`   This value seems to be used by server/notebook/twist.py to make backup copies of nb.sobj.  It seems to make a snapshot of a worksheet as a side-effect, without any check if the snapshot is different from previous snapshots.  This is speculation, since I could not decipher what triggers twist.py to check and do such a save.  Also, experimentally, I see that it happens "automatically", even if the worksheets and notebook are left untouched.

There is also a per-user 'autosave_interval'  This can be accessed through code like `nb.user("admin")['autosave_interval']` and can also be set from the drop-down box in the "Settings" area of the notebook (to be 1,3,5,7,9 minutes only).  The use of this seems a bit odd.  Any edit (but only edits) in the worksheet triggers a possible snapshot save.  First, the time since the last save is checked against the user autosave_interval.  If not enough time has elapsed, it exits, otherwise it continues towards a snapshot save.  It then checks to see if the worksheet has changed.  But it must have changed, since only edits trigger the routine.  Then it writes a snapshot.

So in summary, a new snapshot every period given by 'save_interval' which is not obviously user-configurable.  No check on if the snapshot is different.  Every edit triggers a possible snapshot, it happens only if time exceeds user's autosave_interval, which can be set by the user to limited number of values.

This may be an imperfect understanding of the situation, but I think it is confusing for a user and potentially filling up disk space and/or degrading performance.  So there's some room for improvement in how this works.



---

Comment by kcrisman created at 2014-09-18 02:28:09

Upstream https://github.com/sagemath/sagenb/issues/233

There has been a lot of change and this is more or less disabled.  But still very worth fixing.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by dimpase created at 2020-08-25 09:30:33

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-25 15:43:05

Resolution: invalid
