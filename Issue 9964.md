# Issue 9964: Make SYMPOW not write to files under global Sage installations

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-09-21 22:23:39

Assignee: GeorgSWeber

CC:  cschwan fbissey lftabera

SYMPOW-related doctests can in

```
sage/lfunctions/sympow.py
sage/modular/abvar/abvar.py
sage/modular/hecke/submodule.py
sage/schemes/elliptic_curves/ell_rational_field.py
```

can fail if users who do not have write access under `SAGE_ROOT` runs these tests before a user who does have this access.

See [comment:ticket:9703:8 comments 8 and 9] at #9703 for background and a suggested solution.

This is the likely cause of the non-qepcad failures [reported by Luis Felipe Tabera on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/a56d4fbaad2dcce3).




---

Comment by jdemeyer created at 2012-09-27 08:37:49

This is fixed by #11920.


---

Comment by jdemeyer created at 2012-09-27 08:37:49

Resolution: duplicate
