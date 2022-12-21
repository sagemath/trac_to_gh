# Issue 2245: abvar -- increase the doctest coverage to 100%

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-21 07:31:34

Assignee: was

The doctest coverage for devel/sage/sage/modular/abvar is as follows:

```
teragon:abvar was$ sage -coverage .
abvar.py: 62% (20 of 32)
abvar_ambient_jacobian.py: 28% (2 of 7)
abvar_modsym_factor.py: 60% (3 of 5)
abvar_newform.py: 0% (0 of 1)
constructor.py: 100% (3 of 3)
cuspidal_subgroup.py: 16% (1 of 6)
finite_subgroup.py: 12% (4 of 33)
hecke_operator.py: 66% (4 of 6)
homology.py: 57% (16 of 28)
homspace.py: 0% (0 of 2)
lseries.py: 0% (0 of 6)
morphism.py: 0% (0 of 2)
torsion_point.py: 0% (0 of 2)
torsion_subgroup.py: 37% (3 of 8)

Overall weighted coverage score:  39.4%
Total number of functions:  141
```


The goal of this ticket is to change that to 100%.

This is in preparation for substantial work to move
the modular abelian varieties package forward in preparation
for lots of enhancements to it that are coming up. 


---

Comment by was created at 2008-02-25 05:45:14

After:

```
teragon:abvar was$ sage -coverage .
abvar.py: 100% (38 of 38)
abvar_ambient_jacobian.py: 100% (8 of 8)
abvar_modsym_factor.py: 100% (7 of 7)
abvar_newform.py: 100% (3 of 3)
constructor.py: 100% (3 of 3)
cuspidal_subgroup.py: 100% (6 of 6)
finite_subgroup.py: 100% (33 of 33)
hecke_operator.py: 100% (6 of 6)
homology.py: 100% (30 of 30)
homspace.py: 100% (2 of 2)
lseries.py: 100% (11 of 11)
morphism.py: 100% (1 of 1)
torsion_subgroup.py: 100% (8 of 8)

Overall weighted coverage score:  100.0%
Total number of functions:  156
```



---

Attachment

this is the whole thing flattened and rebased against sage-2.10.3.alpha0


---

Comment by craigcitro created at 2008-03-03 06:14:49

Looks great. I went through and edited a few things here and there, mostly correcting typos and over-long lines. 

There's one thing that still bothers me, though: given a modular abelian variety `A`, one uses `A.lseries()` and `A.padic_lseries(5)` to get the complex and p-adic L-series, which is totally reasonable. However, for an elliptic curve `E`, it's `E.Lseries()` and `E.padic_lseries(5)` -- I don't like that one of the four is uppercase, while the other three are lowercase. I think we should make everything consistent, and I personally prefer lowercase. If someone else (e.g. William) agrees, I'll go ahead and make another patch to correct that.


---

Attachment

minor typo corrections; apply after william's patch above


---

Comment by was created at 2008-03-03 07:00:34

Good job fixing up my patch.  I just looked over your touch ups.  Very nice.


---

Attachment

apply this third


---

Comment by craigcitro created at 2008-03-03 07:27:58

Added a patch to change `Lseries` to `lseries` throughout Sage. Apply after the above patches.


---

Comment by mabshoff created at 2008-03-03 12:56:23

Merged all three patches in Sage 2.10.3.rc1


---

Comment by mabshoff created at 2008-03-03 12:56:23

Resolution: fixed
