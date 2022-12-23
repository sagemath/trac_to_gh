# Issue 3581: The new pbuild pyhon files are not copied on sdist

Issue created by migration from https://trac.sagemath.org/ticket/3581

Original creator: mabshoff

Original creation time: 2008-07-07 06:33:59

Assignee: mabshoff


```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.alpha2/spkg/standard/sage-3.0.4.alpha2$ hg status
! build.py
! clib.py
! sagebuild.py
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-07-07 06:34:07

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-07-07 22:13:21

Positive revivew, but we should then also remove the three offending files from MANIFEST.in. I am doing an sdist with the patch applied to make 100% sure it works.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-07 22:32:22

I can now confirm this actually works:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.foo/spkg/standard$ tar xjf sage-3.0.4.foo.spkg 
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.foo/spkg/standard$ cd sage-3.0.4.foo
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.foo/spkg/standard/sage-3.0.4.foo$ hg status
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.foo/spkg/standard/sage-3.0.4.foo$ 
```

sage-3.0.4.foo is the sdisted 3.0.4.a2 with the patch applied :)

Cheers,

Michael


---

Comment by was created at 2008-07-07 22:33:13

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 23:02:23

Merged in Sage 3.0.4.rc0
