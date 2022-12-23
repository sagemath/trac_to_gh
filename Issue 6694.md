# Issue 6694: [with patch, needs review] Live reference manual worksheets

Issue created by migration from https://trac.sagemath.org/ticket/6694

Original creator: mpatel

Original creation time: 2009-08-09 06:07:47

Assignee: boothby

CC:  jhpalmieri

Sage generates live "docbrowser" worksheets for the tutorial, developer's guide, and constructions guide, but not for the reference manual.


---

Attachment


---

Comment by mpatel created at 2009-08-09 06:25:37

I've attached a first take.  I haven't tested it extensively, but it seems to work for several pages at different depths in the reference manual's hierarchy.

Should we change the green background color for Sage output?  Perhaps we can insert a CSS directive after `default.css` in `twist.py` (see lines 194+).

Actually, the patch is not specific to the manual, so we should be able to add other complex documents, including textbooks, specialized tutorials, etc.


---

Attachment

Handle nonexistent pages better.  Apply only this patch.


---

Comment by mpatel created at 2009-08-09 18:02:36

The new version does not throw an exception for, e.g., `http://localhost:8000/doc/live/reference/foo.html`.


---

Attachment

Style tweaks.  Apply before or after "live_ref_manual" patch.


---

Comment by mpatel created at 2009-08-09 19:56:33

Feel free to edit the optional CSS patch.


---

Comment by mpatel created at 2009-09-21 03:12:01

Replying to [comment:4 mpatel]:
> Feel free to edit the optional CSS patch.
Or ignore it altogether!


---

Comment by mhampton created at 2009-09-22 16:39:50

This seems to work great, and I would give it a positive review except that I just saw William Stein comment that in his notebook refactoring he is switching all path joining to use os.path.join.  In this patch, there are lines:

path = self.docpath + '/' + '/'.join(segments) 

and

path = self.docpath + '/' + '/'.join(segments[ind:])

that should be changed to use os.path.join().


---

Comment by mpatel created at 2009-09-23 00:37:04

Normalize real paths. Apply only this patch.


---

Attachment

Use os.path.join(). Apply only this patch.


---

Attachment

Please try [attachment:trac_6694-live_ref_manual_v3.2.patch v3.2].


---

Comment by mhampton created at 2009-09-23 14:15:48

Great, thanks for the quick change.  That should make it a little easier to merge this into William's notebook rewrite.


---

Comment by mpatel created at 2009-09-23 14:20:35

Replying to [comment:9 mhampton]:
> Great, thanks for the quick change.  That should make it a little easier to merge this into William's notebook rewrite.
No problem.  To really tax a browser, try "evaluating all" cells in a long section of the manual.


---

Comment by mvngu created at 2009-09-24 09:46:32

Merged `trac_6694-live_ref_manual_v3.2.patch`.


---

Comment by mvngu created at 2009-09-24 09:46:32

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:18:20

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
