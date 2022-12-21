# Issue 652: .sage files destroy existing .py files

Issue created by migration from Trac.

Original creator: jvoight

Original creation time: 2007-09-14 04:24:51

Assignee: was

If files a.sage and a.py exist in a directory, then 

sage: load a.sage

destroys the file a.py and replaces it with an automatically generated file.  Either users should be warned of this "feature" or something else should be done.


---

Comment by mabshoff created at 2007-12-26 02:49:07

Changing priority from minor to blocker.


---

Comment by robertwb created at 2008-01-04 21:23:59

Is there any reason to put the .py files in the same directory? It would probably be less confusing to just put them in temp. If one wants to see them, one can use sage -preparse. 

I'm having trouble finding where exactly these files are getting written/used.


---

Comment by ncalexan created at 2008-01-19 21:35:04

Patch preparses .sage files to temporary .py files in a temp directory.


---

Attachment

DO NOT APPLY, THIS HAS TROUBLE WITH DIRECTORIES


---

Attachment


---

Comment by ncalexan created at 2008-01-23 02:53:53

Updated patch should work -- the issue was that 'load /abs/dir/tofile.sage' was borked.  Hopefully this works better.


---

Comment by cwitty created at 2008-01-27 01:30:31

I reproduced the problem with the previous code, and the patch does fix the problem; and the code looks good.


---

Comment by mabshoff created at 2008-01-27 01:40:15

Merged ncalexan-652-updated.patch in Sage 2.10.1.rc1


---

Comment by mabshoff created at 2008-01-27 01:40:15

Resolution: fixed
