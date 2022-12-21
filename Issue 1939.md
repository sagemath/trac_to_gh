# Issue 1939: [with patch] Fix OSX rpy import issues: DYLD_LIBRARY_PATH fix

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-26 13:45:33

Assignee: mabshoff

The latest r.spkg from 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc0/r-2.6.1.p13.spkg

needs the attached patch to properly import libR.dylib. `DYLD_LIBRARY_PATH` is properly set, but from some reason import fails. By adding the R's `lib` directory to `DY_LDLIBRARY_PATH` in `sage-env` the issue is resolved. 

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-01-26 13:49:46

Resolution: fixed


---

Comment by mabshoff created at 2008-01-26 13:49:46

Merged in Sage 2.10.1.rc0
