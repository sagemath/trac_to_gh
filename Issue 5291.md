# Issue 5291: notebook - Do not save snapshots if nothing has changed

Issue created by migration from https://trac.sagemath.org/ticket/5291

Original creator: mabshoff

Original creation time: 2009-02-17 03:44:45

Assignee: boothby

CC:  timothy.clemans@gmail.com jason-sage@creativetrax.com

This problem has come up over and over again. Per default Sage saves a snapshot every 3 minutes regardless if anything has changed or not. This can add up to a *lot* of identical snapshots if a computation is left running a long time. And that in turn causes people with quotas to run out of space as reported in 

http://groups.google.com/group/sage-devel/browse_thread/thread/8544666b8b18660c#

I am making this a critical issue against 3.3.

Cheers,

Michael


---

Attachment


---

Comment by TimothyClemans created at 2009-02-17 22:04:55

I tested it by setting the auto save interval to 10 seconds and clicking undo to see the revisions. Each revision was different.


---

Comment by jason created at 2009-02-17 23:10:14

I'm not sure that this fixes the problem.  Isn't saving to worksheet.txt and saving a snapshot two different things?  If so, then I imagine there will be a time when things are saved to worksheet.txt, and then a snapshot should happen, but wouldn't under this code.


---

Comment by TimothyClemans created at 2009-02-17 23:19:29

save calls save_snapshot which updates worksheet.txt


---

Comment by was created at 2009-02-18 00:50:19

> save calls save_snapshot which updates worksheet.txt 

yep.  Snapshotting *only* ever writes a copy of worksheet.txt. 

REVIEW:

  * positive review -- but it is not an efficient approach.  

See Trac #5300 which will be about doing the same thing more efficiently.


---

Comment by mabshoff created at 2009-02-18 00:58:09

Merged in Sage 3.3.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-18 00:58:09

Resolution: fixed


---

Comment by rbeezer created at 2009-03-09 04:00:34

Replying to [comment:7 mabshoff]:

It appears to me that this code only gets called if (1) there is a worksheet edit, and (2) the time since the last save exceeds the per-user autosave_interval.  If so, checking for a change is always true.  See #5459 for more.


---

Comment by kcrisman created at 2014-09-18 17:07:16

Was this even ever merged?  https://github.com/sagemath/sagenb/blob/master/sagenb/notebook/worksheet.py does not have this diff, and I have a version of Sage from 2010 hanging around that does not have it either.  Maybe it was unmerged at some unspecified point...

(Also note that the function in question also has `return` as its first line.)
