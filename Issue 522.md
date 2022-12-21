# Issue 522: singular build issues on a mac

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2007-08-29 22:33:08

Assignee: craigcitro

Keywords: singular

On my G4, singular won't start at all (and interestingly, sage -singular silently fails). The problem is a simple one: in the build scripts, $SAGE_ROOT/local/bin/Singular gets created with a command that uses "tail -1" ... this is now considered "obselete" usage on a mac, where tail -1 fails and tells you to use "tail -n 1" instead. 

A bundle with the fix is attached, and also at the address below:

http://sage.math.washington.edu/home/citro/patches/tail_fix.hg

Note: if tail -1 gets used in any other build scripts, we need to fix that.


---

Comment by craigcitro created at 2007-08-29 22:43:40

Actually, at William's request, I've uploaded the whole singular spkg. It's here:

http://sage.math.washington.edu/home/citro/patches/singular-3-0-3-20070829.p1.spkg

I think that should be good to go. Let me know if anyone runs into trouble.


---

Comment by craigcitro created at 2007-08-29 22:43:40

Changing status from new to assigned.


---

Comment by was created at 2007-08-29 23:55:20

Resolution: fixed
