# Issue 5880: [with patch; needs review] notebook -- greatly reduce the number of actions that trigger taking a snapshot

Issue created by migration from https://trac.sagemath.org/ticket/5880

Original creator: was

Original creation time: 2009-04-23 20:31:10

Assignee: boothby

CC:  rbeezer

With the attached patch, you get snapshots when you click the save button, and that's about it (I hope). 

This patch simply deletes a bunch of calls to save_snapshot that were all over the place.   You'll still get snapshots, but not every time you blink. 


---

Attachment

I promised to try this patch, but I haven't yet installed into my production server. As it turns out, there is a big improvement in 3.4.1 wrt snapshots, which makes this issue less pressing wrt disk usage... I still think the semantics of snapshots are broken, and particularly they make "discard and quit" unusable, and "undo" a bit hard.

To clean up the snapshot directories in my production server, without removing old revisions in case somebody actually cares about them, I wrote a script to clean up repeated snapshots. The script is only good until you install 3.4.1, and its behaviour is to remove any snapshot which is identical to an earlier one. In effect, this retroactively imposes the new behaviour for snapshots...

To get an idea of the magnitude of the problem. Our notebook server has been in production for a little bit over a month. It has about 20 active users (most students on my sage course, so they actually use the notebook). Running the script deleted 479269 snapshots, keeping only 5908... In fact, I ran the script again after a few hours, and it deleted another 15k new snapshots or so... I've switched the notebook to 3.4.1, and it's not producing redundant snapshots anymore.


---

Attachment

Bash scripts to properly clean up redundant snapshots in the notebook produced by sage 3.4 and earlier.  This script removes every snapshot which is identical to a previous snapshot, giving statistics at the end. As of sage 3.4.1, redundant snapshots are no longer produced.


---

Comment by rbeezer created at 2009-04-26 20:30:31

This patch removes several unnecessary occurrences of `save_snapshot()` in the notebook.  The most significant is that autosave is disabled by inserting a `return`, so an explicit save is required.

As written the patch breaks several doctests.  It seems that in testing, new worksheets are created, but there is no save done under the change in the patch to the `__init__` method for a worksheet.  For example in the doctest for `__getstate___` the `_Worksheet__saved_by_info` key is not present post-patch, causing the doctest to fail.   One fix is to make an explicit call to `save_snapshot()` after each new creation of a test worksheet in a doctest.  Or, in the reviewer patch, I have just restored the `save_snapshot()` call to the `__init__` method for a worksheet since it (a) seems like not such a bad idea, and (b) isn't really a big contributor to the problem of excessive snapshots.

The change to `SendWorksheetToStop` in `twist.py` eliminates a save as part of the "stop" so the docstring needs an adjustment.  That minor change is in the reviewer patch as well.

This is a positive review, subject to fixing doctests, either with approval of the reviewer patch, or by further changes to problematic docstrings.


---

Attachment

> This is a positive review, subject to fixing doctests, either with approval of the reviewer patch, 
> or by further changes to problematic docstrings. 

Well, I applied your patch, which I like, and ran "make ptestlong" and it passes.  So positive review. 

Regarding credit, if anybody notices this, rbeezer should also get credit for this patch.


---

Comment by was created at 2009-04-27 13:20:00

Just an FYI.  I deleted all snapshots, then ran this patch on all the sagenb.org servers for about 5 days, after which there were 17925 snapshots.   That's a lot better than 15000/day, but with the "at most 30 snapshots" limit that #5895 introduces, this should be good.


---

Comment by mabshoff created at 2009-04-30 09:35:49

Resolution: fixed


---

Comment by mabshoff created at 2009-04-30 09:35:49

Merged both patches in Sage 3.4.2.rc0.

Cheers,

Michael
