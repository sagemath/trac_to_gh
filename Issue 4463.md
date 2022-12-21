# Issue 4463: modular/abvar/homspace.py doctests are long

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-11-07 17:08:32

Assignee: mabshoff

CC:  was

Keywords: abvar, homspace, long

The doctests in modular/abvar/homspace.py timeout on my PPC mac, so something in there takes long enough that it should get the "# long time" comment.


---

Comment by mabshoff created at 2008-11-16 08:59:34

This ought to get fixed in Sage 3.2.

Cheers,

Michael


---

Attachment


---

Comment by craigcitro created at 2008-11-23 11:14:32

Changing priority from minor to major.


---

Comment by craigcitro created at 2008-11-23 11:14:32

Changing assignee from mabshoff to craigcitro.


---

Comment by craigcitro created at 2008-11-23 11:14:32

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-11-23 11:14:32

Some speedups for computation of endomorphism rings of modular abelian varieties. This patch just makes one or two easy changes; much work remains. However, it gives a noticeable speedup (at least on my machine): testing `sage/modular/abvar/homspace.py` drops from ~150s to ~100s. This should at least stop the timeouts people keep running into.


---

Comment by craigcitro created at 2008-11-23 11:14:32

Changing component from doctest to modular forms.


---

Comment by craigcitro created at 2008-11-23 11:17:00

For the record, the two optimizations in the above patch:

 * for computing endomorphism ring generators for a one dimensional abelian variety, simply return the answer, and 
 * if we're intersecting a space of modular symbols with `ZZ^n`, simply take the appropriate submodule instead of doing any linear algebra.


---

Comment by mabshoff created at 2008-11-23 11:18:12

Well, initially this was all about making some doctests "#long time", but speeding things up is obviously better :)

Cheers,

Michael


---

Comment by was created at 2008-11-23 21:59:06

Works and seems sensible.  Makes the test take half the time on one of my test machines.


---

Comment by mabshoff created at 2008-11-23 23:44:55

There is one doctest failure issue here:

```
sage -t -long devel/sage/sage/modules/free_module.py        
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/modules/free_module.py", line 1164:
    sage: K = S.integral_structure(); K
Expected:
    Free module of degree 19 and rank 8 over Integer Ring
    Echelon basis matrix:
    [ 0  1  0  0 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
    ...
Got:
    Free module of degree 19 and rank 8 over Integer Ring
    User basis matrix:
    [ 0  1  0  0 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
    [ 0  0  1  0 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0  1  0  0  0 -1  0  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0  0  1  0  0  0 -1  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0  0  0  1  0 -1  0  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0  0  0  0  1  0 -1  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0  0  0  0  0  0  0  1  0 -1  0  0  0 -1  1]
    [ 0  0  0  0  0  0  0  0  0  0  0  0  1  0 -1  0  0  1 -1]
**********************************************************************
```

Changing this is simple, but I would like to know if the experts think this change is justified.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-23 23:53:14

Craig mentioned in IRC that some more work needs to be done here.

Cheers,

Michael


---

Attachment

Added a new patch that fixes the doctest failure. It was just a question of calling the free module constructor appropriately; this version is even ever so slightly faster than before.


---

Comment by mabshoff created at 2008-11-24 19:35:37

Merged both patches in Sage 3.2.1.alpha1


---

Comment by mabshoff created at 2008-11-24 19:35:37

Resolution: fixed
