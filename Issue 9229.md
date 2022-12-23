# Issue 9229: Bring doctests for databases/cremona.py up to 100% (from  42% (17 of 40) )

Issue created by migration from https://trac.sagemath.org/ticket/9229

Original creator: cremona

Original creation time: 2010-06-12 13:43:32

Assignee: cremona


```

devel/sage-main/sage/databases/cremona.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE devel/sage-main/sage/databases/cremona.py: 42% (17 of 40)

Missing documentation:
* _init(self, ftpdata):
* __repr__(self):
* CremonaDatabase():


Missing doctests:
* rebuild(data_tgz, largest_conductor, decompress=True):
* __init__(self, read_only=True):
* __iter__(self):
* __getitem__(self, N):
* __repr__(self):
* allbsd(self, N):
* allcurves(self, N):
* allgens(self, N):
* degphi(self, N):
* elliptic_curve_from_ainvs(self, N, ainvs):
* elliptic_curve(self, label):
* iter(self, conductors):
* isogeny_classes(self, conductor):
* isogeny_class(self, label):
* list(self, conductors):
* _init_allcurves(self, ftpdata, largest_conductor=0):
* _init_degphi(self, ftpdata, largest_conductor=0):
* _init_allbsd(self, ftpdata, largest_conductor=0):
* _init_allgens(self, ftpdata, largest_conductor=0):
* __init__(self, read_only=True):
```




---

Comment by cremona created at 2010-06-12 18:42:22

Changing priority from major to minor.


---

Comment by cremona created at 2010-06-12 18:42:22

This is a duplicate of #9223 and should be deleted.


---

Comment by drkirkby created at 2010-06-12 21:12:49

Resolution: duplicate
