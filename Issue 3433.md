# Issue 3433: notebook -- change it so worksheet text is *not* stored in the notebook/worksheet objects when pickling and unpickling

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-15 22:51:57

Assignee: boothby

This is a major efficiency problem with large notebooks.  The fix is to write custom worksheet __reduce__ and load methods that do not store the actual worksheet text in the object, but instead store it to disk and read it from disk.  That reading from disk should only happen when the worksheet is actually "activated", i.e., not when unpickling!


---

Comment by mabshoff created at 2008-07-31 02:47:26

Mhh, did William not fix this already when speeding up the notebook saving?

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-23 02:50:05

Changing type from defect to enhancement.


---

Comment by mhansen created at 2009-11-14 08:21:58

Resolution: invalid
