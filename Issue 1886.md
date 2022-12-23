# Issue 1886: [with patch - actually tuning tarball] add atlas pretuning for AMD Athlon MP processors

Issue created by migration from https://trac.sagemath.org/ticket/1886

Original creator: was

Original creation time: 2008-01-22 04:45:44

Assignee: was

So that building ATLAS on AMD Athlon doesn't take FIVE HOURS, I've recorded the tuning information and attached it to this ticket. 


---

Attachment

I followed the directions here:
   http://math-atlas.sourceforge.net/devel/atlas_devel/atlas_devel.html#SECTION00070000000000000000

In particular, I did:

```
   1. sage -f -m atlas-3.8.p7
   2. cd spkg/build/atlas-3.8.p7
   3. cd ATLAS-build/ARCHS
   4. make ArchNew
   5. make tarfile
```



---

Comment by mabshoff created at 2008-02-02 09:12:33

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-02-02 09:12:33

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-02 09:12:33

Look at #1547 for an spkg with the tuning information added.


---

Comment by mabshoff created at 2008-02-02 09:58:59

Merged in Sage 2.10.1.rc5


---

Comment by mabshoff created at 2008-02-02 09:58:59

Resolution: fixed
