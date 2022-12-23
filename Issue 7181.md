# Issue 7181: We must ensure we have GNU make, not HP-UX or Solaris 'make'

Issue created by migration from https://trac.sagemath.org/ticket/7181

Original creator: drkirkby

Original creation time: 2009-10-10 09:30:33

Assignee: tbd

Keywords: HP-UX Solaris make

Although I noticed this issue on HP-UX, I know it affects Solaris too. The 'make' program certainly can not be Sun's on Solaris, and while it looks like a minor mod would allow the 'make' on HP-UX to work, it seems sensible we just check for GNU make.


---

Comment by mhansen created at 2009-11-20 06:22:10

Resolution: fixed


---

Comment by mhansen created at 2009-11-20 06:22:10

Fixed by #7352
