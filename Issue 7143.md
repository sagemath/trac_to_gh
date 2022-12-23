# Issue 7143: We must check if the version of 'make' found is gnu 'make'

Issue created by migration from https://trac.sagemath.org/ticket/7143

Original creator: drkirkby

Original creation time: 2009-10-06 17:08:29

Assignee: tbd

Sage needs GNU make (at least I know neither Sun's 'make' in Solaris or HP's make in HP-UX are not suitable), so we need to check that 'make' is in fact gnu 'make', and not some other version of make. 

On HP-UX there does not appear to be a version of GNU make on the system. With Solaris, there  is a version called 'gmake' at /usr/sfw/bin/gmake. 

One way or another, we need to make sure that the 'make' that Sage finds is the GNU version. 


---

Comment by mhansen created at 2009-11-20 06:21:39

Fixed by #7352


---

Comment by mhansen created at 2009-11-20 06:21:39

Resolution: fixed
