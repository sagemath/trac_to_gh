# Issue 2524: update givaro.spkg to the 3.2.10.rc3 release

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-15 01:53:45

Assignee: mabshoff

The updated spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.4/alpha0/givaro-3.2.10.rc3.spkg

contains the following fixes:
 * update to upstream 3.2.10.rc3
 * add 64 bit OSX 10.5 support
 * remove all patches since they were integrated upstream
 * add spkg-check


---

Comment by mabshoff created at 2008-03-15 01:56:48

Note that you probably need to rebuild the linbox.spkg. #2525 is to upgrade linbox to the 1.1.5.rc3 linbox release.


---

Comment by mabshoff created at 2008-03-15 01:57:15

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-15 05:07:34

Once this ticket and #2525 are merged we can also close #454 and #520.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-15 06:40:55

Resolution: fixed


---

Comment by mabshoff created at 2008-03-15 06:40:55

Merged in Sage 2.10.4.alpha0
