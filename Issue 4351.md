# Issue 4351: bugs in abelian variety homspace computation

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-23 19:34:51

Assignee: craigcitro

Please see #4346 first and apply the patch there.

After applying this patch and doctesting all sage, there are a bunch of failures in the modular abelian varieties code:

```
	sage -t  devel/sage-main/sage/modular/abvar/abvar_ambient_jacobian.py # 3 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/abvar_newform.py # 3 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/morphism.py # 3 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/homspace.py # 34 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/abvar.py # 11 doctests failed
```


These are because of bugs in that code exposed by doing proper bounds checking.


---

Comment by was created at 2008-10-23 20:27:34

This is a red herring.  It is fixed by #4350, and there were never any bugs suggested by this ticket.


---

Comment by was created at 2008-10-23 20:27:34

Resolution: invalid
