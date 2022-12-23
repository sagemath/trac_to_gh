# Issue 2172: sage -sdist loses debian build infrastructure

Issue created by migration from https://trac.sagemath.org/ticket/2172

Original creator: mabshoff

Original creation time: 2008-02-15 17:50:39

Assignee: tabbott

$SAGE_ROOT/devel/sage/spkg-dist currently does not copy the debian directory as well as `spkg-debian-maybe`. It is easily fixed in `spkg-dist`, patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-15 17:54:48

Changing assignee from tabbott to mabshoff.


---

Comment by mabshoff created at 2008-02-15 17:54:48

Changing status from new to assigned.


---

Attachment


---

Comment by ncalexan created at 2008-02-16 01:15:13

If you need to work with 2.10.1, do this:


```
[5:02pm] ncalexan: mabshoff: I have files missing in sage-2.10.1.  All related to debian.
[5:02pm] ncalexan: It means I can't apply that import patch.
[5:02pm] ncalexan: Any ideas?
[5:02pm] mabshoff: #2172
[5:03pm] mabshoff: I fixed it in my alpha1, but the files will only show up once I do another sdist.
[5:03pm] ncalexan: kk.
[5:03pm] mabshoff: But the plan is to do that "tonight" and use 2.10.2.alpha1 as basis fir BD10.
[5:03pm] mabshoff: "-sdist" is all magic and voodoo 
[5:04pm] mabshoff: Let's just say somebody ought to rewrite that POS properly down the road 
[5:04pm] ncalexan: So how do I use this for developing?  I can't commit anything right now.
[5:04pm] mabshoff: ok, let me post a tarball with the missing files then.
[5:05pm] ncalexan: Can I copy from my old tree?
[5:08pm] mabshoff: Nick: http://sage.math.washington.edu/home/mabshoff/missing-debian.tar.gz
[5:08pm] mabshoff: Move the files inside that dir into SAGE_ROOT/devel/sage
[5:08pm] mabshoff: The files aren't in any old tree.
```



---

Comment by ncalexan created at 2008-02-17 04:31:02

This needs to be applied.


---

Comment by mabshoff created at 2008-02-17 04:35:28

Resolution: fixed


---

Comment by mabshoff created at 2008-02-17 04:35:28

Merged in Sage 2.10.2.alpha1
