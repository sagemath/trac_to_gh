# Issue 4434: [with patch; needs review] hgmerge massively broken on os x

Issue created by migration from https://trac.sagemath.org/ticket/4434

Original creator: was

Original creation time: 2008-11-04 04:41:23

Assignee: mabshoff

When doing a graphical 3-way merge under OS X, hgmerge is missing so one gets infinite loops or errors.  This is a major problem.

The spkg here:

http://sage.math.washington.edu/home/was/patches/mercurial-1.01.p2.spkg

does the following:

 * Added custom hgmerge script for OS X. For some reason no script at all was 
   copied over, which lead to (1) hg merge silently failing painfully for most
   users, and (2) for users that run install_scripts, they would get a fork
   bomb, since hgmerge would call sage -hgmerge which would call hgmerge 
   ad infintum.




---

Comment by mabshoff created at 2008-11-04 13:34:34

Spkg looks good, but I checked in all outstanding changes.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-04 13:34:54

Resolution: fixed


---

Comment by mabshoff created at 2008-11-04 13:34:54

Merged in Sage 3.2.alpha3


---

Comment by kini created at 2011-04-04 16:45:24

#11120 reverses this patch. Your comments would be greatly appreciated!
