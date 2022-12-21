# Issue 5143: shift-enter should save and exit tinyMCE

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-01-30 23:11:30

Assignee: boothby

This would be more consistent with calculation cells.

References for developement:

It looks like we might be able to do this with the current key handler attaching an event to the tinymce instance that calls the triggerSave tinyMCE trigger: http://wiki.moxiecode.com/index.php/TinyMCE:Functions#tinyMCE.triggerSave

Also, see the bottom of the following page for a way to get tinyMCE to associate an event with a keypress:
http://tinymce.moxiecode.com/punbb/viewtopic.php?id=1321




---

Comment by jason created at 2009-01-30 23:25:51

See also: http://wiki.moxiecode.com/index.php/TinyMCE:API/tinymce.Editor/onKeyDown


---

Attachment


---

Comment by jason created at 2009-02-03 08:15:58

This patch also adds font formatting buttons that have been requested by several people.


---

Comment by jason created at 2009-02-03 08:16:14

Changing priority from major to critical.


---

Comment by jason created at 2009-02-03 09:25:05

Changing status from new to assigned.


---

Comment by jason created at 2009-02-03 09:25:05

Changing assignee from boothby to jason.


---

Comment by TimothyClemans created at 2009-02-04 01:04:31

Tested in FF3 & Safari on Mac.


---

Comment by mabshoff created at 2009-02-04 01:17:07

Merged in Sage 3.3.alpha5.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-04 01:17:07

Resolution: fixed
