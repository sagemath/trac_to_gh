# Issue 3219: spkg -- upgrad to gmp-4.2.2 while we wait for MPIR

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-16 14:11:45

Assignee: mabshoff

The upgraded spkg is here:

http://sage.math.washington.edu/home/was/cygwin/gmp-4.2.2.spkg

This is needed for both the OS X 64-bit port and Cygwin ports. 


---

Comment by mhansen created at 2008-05-17 08:54:42

This spkg built fine for me under cygwin! :-)

Also, isn't there an LGPLv3 issue with gmp-4.2.2?


---

Comment by mabshoff created at 2008-05-23 02:01:19

There is an LGPL V3 issue, but we are willing to live with that until MPIR is ready. This spkg has been merged. So I am closing this.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-23 02:01:19

Resolution: fixed


---

Comment by mabshoff created at 2008-05-23 02:02:47

For the record: Merged in Sage 3.0.2.rc0 

Cheers,

Michael
