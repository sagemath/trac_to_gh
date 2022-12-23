# Issue 4210: [with spkg, needs review] Remove some deprecation warnings from numpy-1.2.spkg

Issue created by migration from https://trac.sagemath.org/ticket/4210

Original creator: mabshoff

Original creation time: 2008-09-27 22:18:16

Assignee: mabshoff

#4205 depends on the new scipy-0.7svn.spkg and some other tickets which will not go into Sage 3.1.3. To still be able to update to numpy 1.2 we need to quiet some deprecation warnings in numpy itself for now. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/numpy-1.2.0.p0.spkg

introduces a couple work arounds for now that should be reverted once #3391, #3498 and #4005 go in.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-27 22:18:24

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-27 22:25:56

Looks good to me.


---

Comment by mabshoff created at 2008-09-27 22:30:44

Merged in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-27 22:30:44

Resolution: fixed
