# Issue 1547: Add pre-tuned settings for ATLAS for certain CPUs

Issue created by migration from https://trac.sagemath.org/ticket/1547

Original creator: mabshoff

Original creation time: 2007-12-17 04:11:09

Assignee: mabshoff

William says:

```
Michael,

Can we add new machines to the ATLAS database of pre-tuned machines?
I ask, because my Thinkpad laptop -- a Pentium M, is taking literally
several *hours* to build ATLAS, which sucks.

William
```


I will look into this. I am also afraid that compiling ATLAS on PPC/Linux for example will be a rather long, painful experience, so we ought to get on top of this and submit profiles of those CPUs that are missing upstream.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-15 20:04:06

See

http://math-atlas.sourceforge.net/devel/atlas_devel/atlas_devel.html#SECTION00070000000000000000

for details.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 09:10:44

There is an atlas.spkg with tuning information for Pentium M and Athlon MP added at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc5/atlas-3.8.p11.spkg

See also #1886.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 09:58:49

Resolution: fixed


---

Comment by mabshoff created at 2008-02-02 09:58:49

Merged in Sage 2.10.1.rc5
