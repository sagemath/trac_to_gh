# Issue 5016: bump ecmgmp, make libecm extension depend on local/include/ecm.h

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-18 16:58:00

Assignee: mabshoff

As the above states. Note that this is required to force a rebuild due to the MPIR update from #4966.

Spkg and patch coming up shortly.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-18 16:58:36

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-19 10:54:30

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/ecm-6.2.1.p0.spkg

There are no functional changes. The patch to make it depend on the ecm header is already in Sage.

Cheers,

Michael


---

Comment by mhansen created at 2009-01-19 10:56:34

Looks fine.


---

Comment by mabshoff created at 2009-01-19 11:10:23

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 11:10:23

Merged in Sage 3.3.alpha0
