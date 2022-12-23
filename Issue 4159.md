# Issue 4159: sage -bdist fails on osx 10.5 ppc with libpng errors

Issue created by migration from https://trac.sagemath.org/ticket/4159

Original creator: was

Original creation time: 2008-09-20 15:47:42

Assignee: mabshoff

With sage-3.1.2 if you try to do sage -bdist it fails with weird libpng linking errors
and missing symbols.  This is when it tries to make a dmg. 

For the 3.1.2 binary, I'm just using tar for now until this is fixed.  The fix will
probably be to unset some dynamic library paths right before running the commands
in the sage-bdist script that create the dmg. 


---

Comment by mabshoff created at 2008-09-20 20:31:30

What are the errors? Is this on varro?

Cheers,

Michael


---

Comment by was created at 2008-09-21 13:52:37

It turns out that this happens on *all* OS X machines, both 10.5 and 10.4 on both ppc and intel.  Basically "sage -bdist" is completely broken in sage-3.1.2 on OS X.


---

Comment by was created at 2008-09-21 13:52:37

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-09-21 17:57:41

Yeah, I agree that the fix will be to unset DYLD_LIBRARY_PATH right before actually calling hdiutil in sage-bdist. Very odd that a command line utility pulls in libpng symbols. Oh well.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-30 17:43:16

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-30 17:43:16

Patch coming up.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-10-12 23:31:26

Looks good to me.


---

Comment by mabshoff created at 2008-10-12 23:39:40

Resolution: fixed


---

Comment by mabshoff created at 2008-10-12 23:39:40

Merged in Sage 3.1.3.rc0
