# Issue 3318: improve 64 bit osx python 2.5.2 build

Issue created by migration from https://trac.sagemath.org/ticket/3318

Original creator: mabshoff

Original creation time: 2008-05-28 09:10:46

Assignee: mabshoff

There are are two issues that need to be fixed with the current python.spkg:

 * we need to pass OPT flags to configure since otherwise we end up missing "-m64"
 * Instead of "--enable-toolbox-glue=false" we need to use "--disable-toolbox-glue" to avoid building the Mac specific extensions that do not work in 64 bit mode anyway since there is no 64 bit Carbon
 * we need to slightly patch pymactoolbox.h so that twisted-8.0.1 work in 64 bit mode, see #3193

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-28 09:10:55

Changing status from new to assigned.


---

Attachment


---

Attachment


---

Attachment


---

Attachment

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/python-2.5.2.p1.spkg

contains the above fixes. It has been build tested with Linux and 32 & 64 bit OSX.

Currently the _ctypes.so extension is broken. Since the fix is complicated this will be another ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-28 13:19:39

Merged in Sage 3.0.3.alpha0


---

Comment by mabshoff created at 2008-05-28 13:19:39

Resolution: fixed
