# Issue 4853: Sage 3.2.2: numerical noise in sage/rings/number_field/number_field_morphisms.pyx

Issue created by migration from https://trac.sagemath.org/ticket/4853

Original creator: mabshoff

Original creation time: 2008-12-22 18:50:02

Assignee: mabshoff

This is cicero on SkyNet with gcc 4.3.2:

```
sage -t  "devel/sage/sage/rings/number_field/number_field_morphisms.pyx"
**********************************************************************
File "/home/mariah/sage/sage-3.2.2-x86-Linux-fc/devel/sage/sage/rings/number_field/number_field_morphisms.pyx",
line 44:
    sage: sigma_a = K.polynomial().change_ring(CC).roots()[1][0]; sigma_a
Expected:
    -0.629960524947436 + 1.09112363597172*I
Got:
    -0.629960524947437 + 1.09112363597172*I
**********************************************************************
File "/home/mariah/sage/sage-3.2.2-x86-Linux-fc/devel/sage/sage/rings/number_field/number_field_morphisms.pyx",
line 47:
    sage: g(a+1)
Expected:
    0.370039475052564 + 1.09112363597172*I
Got:
    0.370039475052563 + 1.09112363597172*I
**********************************************************************
```


Patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-22 22:24:22

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-22 22:24:22

Note the difference:

```
    -0.629960524947436 + 1.09112363597172*I
    -0.629960524947437 + 1.09112363597172*I
```

and

```
    0.370039475052564 + 1.09112363597172*I
    0.370039475052563 + 1.09112363597172*I
```


Cheers,

Michael


---

Attachment

+1 ± 0.000001


---

Comment by mabshoff created at 2008-12-23 23:19:24

Merged in Sage 3.2.3.alpha0


---

Comment by mabshoff created at 2008-12-23 23:19:24

Resolution: fixed
