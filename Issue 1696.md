# Issue 1696: osx 10.4 2.9.2 instructions don't work.

Issue created by migration from https://trac.sagemath.org/ticket/1696

Original creator: jkantor

Original creation time: 2008-01-05 23:48:32

Assignee: cwitty

I tried the 2.9.2 dmg for osx 10.4. There were two major issue

1. Graphically dragging and dropping the sage folder didn't work. about halfway through the copy 
   failed with the message 

(You cannot copy "singular" to the destination because its name is the 
same as the name of an item on the destination except for the case of 
some characters) 

2. From the command line I was able to do 

cp -R -P /Volumes/sage-2.9.2-OSX10.4-intel-i386-Darwin/sage . 

This worked modulo a missing libintl (see 1695).

If you only do cp -r, every symbolic link breaks.


---

Comment by mabshoff created at 2008-02-15 23:31:53

What is the current status? I think the problems have been resolved, but can somebody confirm?

Cheers,

Michael


---

Comment by was created at 2008-02-16 06:11:07

This can be closed.  The issue is that my osx 10.4 intel build machine had a case-sensitive filesystem.  This is now a non-issue because that machine no longer exists (more precisely it was upgraded to 10.5; it's not my machine).  

William


---

Comment by was created at 2008-02-16 06:11:07

Resolution: wontfix
