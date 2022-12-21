# Issue 5757: [with patch, needs review] change nodoctest directive

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-04-11 17:47:59

Assignee: jhpalmieri

Without this patch, if the string 'nodoctest' is anywhere in the file, then the file is not doctested.  This changes it to only look at for 'nodoctest' in the first 50 characters of the file.

(This is a patch to the 'scripts' repository.)


---

Attachment


---

Comment by mabshoff created at 2009-04-13 01:57:07

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 01:57:07

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
