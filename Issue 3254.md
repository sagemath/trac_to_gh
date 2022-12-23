# Issue 3254: [with patch, needs review] improvements and doctests for CachedFunction

Issue created by migration from https://trac.sagemath.org/ticket/3254

Original creator: mhansen

Original creation time: 2008-05-19 00:49:38

Assignee: cwitty

CachedFunction now works with class methods.


---

Attachment

Very cool, I want this. Is `CachedFunction` the right name though? Shouldn't it be `cached_function`? I think there is a different style convention for the persistent and the cached functions which is a bummer. This is not a blocker for merging this code though, since it wasn't introduced by this patch.


---

Comment by mabshoff created at 2008-06-04 20:54:04

Merged in Sage 3.0.3.alpha1


---

Comment by mabshoff created at 2008-06-04 20:54:04

Resolution: fixed
