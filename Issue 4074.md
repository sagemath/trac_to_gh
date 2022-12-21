# Issue 4074: [with spkg, needs review] the notebook is totally broken in secure mode with the new twisted spkg

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-09-07 20:05:37

Assignee: mabshoff

This is because in the previous spkg the patches were applied directly to src/ rather than going through the standard patches/ mechanism.

The new spkg can be found here: http://sage.math.washington.edu/home/mhansen/twisted-8.1.0.p1.spkg


---

Comment by mhansen created at 2008-09-07 20:06:23

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-07 20:06:23

Thanks to exarkun on #twisted (irc.freenode.net) for helping me track this down.


---

Comment by mhansen created at 2008-09-07 20:06:23

Changing assignee from mabshoff to mhansen.


---

Comment by mabshoff created at 2008-09-07 22:58:52

I fixed two small issues:

 * remove old `._*` crap from OSX - they must have been in the original spkg
 * added diffs for the changed files to the patches directory

Positive review. The new spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc1/twisted-8.1.0.p1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-07 22:59:09

Merged in Sage 3.1.2.rc1


---

Comment by mabshoff created at 2008-09-07 22:59:23

Resolution: fixed


---

Comment by mabshoff created at 2008-09-07 22:59:23

Merged in Sage 3.1.2.rc1
