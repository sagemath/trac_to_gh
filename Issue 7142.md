# Issue 7142: We must check if the version of 'tar' found is gnu tar

Issue created by migration from https://trac.sagemath.org/ticket/7142

Original creator: drkirkby

Original creation time: 2009-10-06 17:03:53

Assignee: tbd

Sage needs GNU tar (at least I know the Sun tar is not suitable), so we need to check that 'tar' is in fact gnu tar, and not some other version of tar. 

On HP-UX there does not appear to be a version of GNU tar on the system. With Solaris, there  is a version called 'gtar' at /usr/sfw/bin/gtar. 

One way or another, we need to make sure that the tar that Sage files is the GNU version. 


---

Comment by drkirkby created at 2009-11-02 13:49:08

Possibly a better solution would be to write tar files in a more portable format. It would appear the GNU tar developers are going to change to a POSIX format for the default format of GNU tar, rather than their current 'gnu' format. See

[http://groups.google.com/group/sage-devel/browse_thread/thread/c1d1f27d455e3c72#](http://groups.google.com/group/sage-devel/browse_thread/thread/c1d1f27d455e3c72#)

However, at this point in time, I'm not aware of whether that will solve the problem. It may be on some platforms the 'tar' program is just not suitable and so insisting on the use of GNU tar will be necessary.


---

Comment by mhansen created at 2009-11-20 06:21:15

Resolution: fixed


---

Comment by mhansen created at 2009-11-20 06:21:15

Fixed by #7352
