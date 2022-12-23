# Issue 2376: [with patch, needs review] Sage 2.10.3.rc1: various doctest failure in abvar

Issue created by migration from https://trac.sagemath.org/ticket/2376

Original creator: mabshoff

Original creation time: 2008-03-03 16:54:38

Assignee: failure

We have various doctest failures in

```
sage -t -long devel/sage-main/sage/modular/abvar/abvar.py
sage -t -long devel/sage-main/sage/modular/abvar/finite_subgroup.py
sage -t -long devel/sage-main/sage/modular/abvar/torsion_subgroup.py
```


The attached patch fixes those.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-03 16:54:43

Changing assignee from failure to mabshoff.


---

Comment by mabshoff created at 2008-03-03 16:54:43

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2008-03-03 17:06:08

Looks great!


---

Comment by mabshoff created at 2008-03-03 17:21:20

Resolution: fixed


---

Comment by mabshoff created at 2008-03-03 17:21:20

Merged in Sage 2.10.3.rc1


---

Attachment

I just attached another trivial, "obviously" correct doctest fix related to trac-2245-lseries.patch to this ticket. It has already been merged, but feel free to review it.

Cheers,

Michael
