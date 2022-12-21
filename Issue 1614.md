# Issue 1614: cleanup setup.py in sage.spkg

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-28 17:02:27

Assignee: mabshoff

CC:  craigcitro

We have a lot of extensions directly listed in the `ext_modules section`. Move those out and also sort the `ext_modules list`


---

Comment by robertwb created at 2008-01-04 22:31:18

Is there any reason to not list extensions directly in the ext_modules list? This seems far simpler and less error prone. If anything needs to change, I'd move all of them there.


---

Comment by mabshoff created at 2008-01-04 22:36:45

Well, as it it just seems very inconsistent. We can move it either way, it should just be consistent. I have a Cygwin build patch for setup.py that should be applied before anybody else touches setup.py with some major reorg patch. The is needed because the order of libraries matters on Cygwin. That patch is one of the first patches that I plan to merge for 2.10 as I am reluctant to merge it now for 2.9.2.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-13 16:32:39

This issue has been fixed via #4480 by Craig Citro.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-13 16:32:39

Resolution: fixed
