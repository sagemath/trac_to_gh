# Issue 2310: [with patch; needs review] bug attaching files in files that are attached

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-26 04:15:27

Assignee: cwitty

I found this bug when testing #1964.  To replicate, create a file a.sage and put 

```
attach b.sage
```

in it.  This fails, but {{{attach "b.sage"} works.  This was a problem before this patch, so it is NOT the fault of this patch.  


---

Attachment

This likely depends on #1964.


---

Comment by was created at 2008-02-26 04:35:23

NOTE: This could likely be done better after #1964 is done by using the method split_file_names(line): in interpreter.py?


---

Comment by was created at 2008-02-26 04:39:12

Regarding my comment about split_file_names -- yes it could be done that way, but split_file_names is a VERY complicated function whereas _strip_quotes which is included in this patch is very simple and easy to use/understand. So I'm not convinced by my previous suggestion.


---

Comment by mhansen created at 2008-03-05 00:40:30

Works for me in 2.10.3.rc1


---

Comment by mabshoff created at 2008-03-05 05:33:19

Resolution: fixed


---

Comment by mabshoff created at 2008-03-05 05:33:19

Merged in Sage 2.10.3.rc2
