# Issue 6260: sage -startuptime is totally broken in sage-4.0.1

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-11 15:31:33

Assignee: cwitty

subject says it all.  This has something to do with hitting new code because of factoring out dsage.


---

Attachment


---

Comment by mhansen created at 2009-06-11 18:06:01

Looks good to me.  The old version wouldn't work when importing any module that used absolute imports (whose import signature is different than the old import signature.


---

Comment by ncalexan created at 2009-06-13 22:54:33

Resolution: fixed
