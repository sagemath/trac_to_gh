# Issue 5258: escape html strings with cgi.escape instead of custom (and lacking) regexp

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-02-13 19:06:54

Assignee: boothby

See http://groups.google.com/group/sage-devel/browse_thread/thread/3fd6f52b4b04108d for the discussion.



---

Attachment


---

Comment by was created at 2009-02-13 19:27:00

+1 and positive review!


---

Comment by jason created at 2009-02-13 23:08:21

Changing assignee from boothby to jason.


---

Comment by jason created at 2009-02-13 23:08:21

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-14 02:13:46

Merged in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 02:13:46

Resolution: fixed


---

Comment by was created at 2009-02-24 14:44:48

I blew it on this review -- there is a major major bug in this patch in that it uses escape in twist.py but does *not* import it!!  See #5358.


---

Comment by jason created at 2009-02-24 15:20:37

Well, I blew it even more by writing the error in the patch!
