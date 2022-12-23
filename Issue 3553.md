# Issue 3553: Update eclib to eclib-20080310.p4.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3553

Original creator: mabshoff

Original creation time: 2008-07-05 20:42:22

Assignee: cremona

There's a newly patched version here:

http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20080310.p4.spkg

John Cremona removed some unused LiDiA code since it no longer builds. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-05 21:40:04

Changing keywords from "" to "editor_mabshoff".


---

Comment by mabshoff created at 2008-07-05 22:07:29

The spkg was based on eclib-20080310.p3.spkg without my fixes to SPKG.txt and the current spkg also did not have a changelog in SPKG.txt. I added back the changes for p3 and also wrote a new entry for p4. In addition the hg repo in src had uncommitted changes:

```
eclib-20080310.p4/src$ hg status
M procs/gf.h
M procs/interface.h
M procs/marith.cc
M procs/marith.h
M procs/mptest.cc
M procs/mptest.out
```

I checked those in in John's name. Builds fine for me.

John: the updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha2/eclib-20080310.p4.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-05 22:12:03

Resolution: fixed


---

Comment by mabshoff created at 2008-07-05 22:12:03

Merged in Sage 3.0.4.alpha2
