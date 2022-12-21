# Issue 6844: Clean up spkg-install for readline

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-08-30 07:15:51

Assignee: tbd

The spkg-install for readline does a lot of silly things. 

 * It does a grep on /etc/SuSE-release even if the file does not exist. 
 * It adds  -m64 only on OS X if SAGE64 is set to 'yes'
 * It adds -m64 as a linker flag, even though no such linker flags exists on any linker I can find. 

It needs a cleanup. I'll do this. 

Dave 


---

Comment by mvngu created at 2009-09-17 22:12:08

Fixed by #6945.


---

Comment by mvngu created at 2009-09-17 22:12:08

Resolution: duplicate
