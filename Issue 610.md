# Issue 610: padics have no doctests

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2007-09-07 01:09:01

Assignee: roed

All files in the rings/padics directory need doctests.


---

Comment by mabshoff created at 2007-12-24 09:15:11

While it isn't 0% any more it certainly isn't close to 100% yet.

```
./sage -coverageall devel/sage-main/sage/rings/padics
Overall weighted coverage score:  11.3%
Total number of functions:  796
./sage -coverageall devel/sage-main/sage/rings/polynomial/padics
[snip]
Overall weighted coverage score:  42.4%
Total number of functions:  47
./sage -coverageall devel/sage-main/sage/matrix/padics
[snip]
Overall weighted coverage score:  0.0%
Total number of functions:  4

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-17 01:03:53

Things are improving. With 2.10.4 final I get:

```
sage-2.10.4.final$ ./sage -coverageall devel/sage/sage/rings/padics/
capped_absolute_generic.py: 0% (0 of 1)
capped_relative_generic.py: 0% (0 of 1)
eisenstein_extension_generic.py: 0% (0 of 18)
factory.py: 13% (3 of 22)
fixed_mod_generic.py: 0% (0 of 1)
lazy_generic.py: 0% (0 of 3)
local_generic_element.pyx: 70% (7 of 10)
local_generic.py: 27% (10 of 37)
misc.py: 0% (0 of 2)
padic_base_generic_element.pyx: 0% (0 of 1)
padic_base_generic.py: 0% (0 of 5)
padic_capped_absolute_element.pyx: 84% (22 of 26)
padic_capped_relative_element.pyx: 48% (16 of 33)
padic_ext_element.pyx: 0% (0 of 1)
padic_extension_generic.py: 0% (0 of 20)
padic_extension_leaves.py: 0% (0 of 8)
padic_field_capped_relative.py: 20% (1 of 5)
padic_field_generic.py: 0% (0 of 14)
padic_field_lazy.py: 11% (2 of 17)
padic_fixed_mod_element.pyx: 42% (12 of 28)
padic_generic_element.pyx: 31% (10 of 32)
padic_generic.py: 42% (14 of 33)
padic_lazy_element.py: 0% (1 of 110)
padic_lazy_field_generic.py: 0% (0 of 1)
padic_lazy_generic.py: 0% (0 of 2)
padic_lazy_ring_generic.py: 0% (0 of 1)
padic_printing.pyx: 33% (7 of 21)
padic_ring_base_generic.py: 0% (0 of 3)
padic_ring_capped_absolute.py: 0% (0 of 5)
padic_ring_capped_relative.py: 0% (0 of 5)
padic_ring_fixed_mod.py: 0% (0 of 5)
padic_ring_generic.py: 0% (0 of 6)
padic_ring_lazy.py: 7% (1 of 13)
padic_ZZ_pX_CA_element.pyx: 72% (21 of 29)
padic_ZZ_pX_CR_element.pyx: 70% (22 of 31)
padic_ZZ_pX_element.pyx: 40% (2 of 5)
padic_ZZ_pX_FM_element.pyx: 74% (23 of 31)
pow_computer_ext.pyx: 77% (21 of 27)
pow_computer.pyx: 93% (14 of 15)
rigid_functions.pyx: 0% (0 of 37)
unramified_extension_generic.py: 0% (0 of 20)
valuation.py: 0% (0 of 114)

Overall weighted coverage score:  25.8%
Total number of functions:  799
```

and

```
sage-2.10.4.final$ ./sage -coverageall devel/sage-main/sage/rings/polynomial/padics/
polynomial_padic_capped_relative_dense.py: 42% (19 of 45)
polynomial_padic_flat.py: 25% (1 of 4)

Overall weighted coverage score:  40.6%
Total number of functions:  49
```


Cheers,

Michael


---

Comment by craigcitro created at 2009-01-15 00:23:12

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2009-01-15 00:34:33

Replying to [comment:4 craigcitro]:

> type changed from defect to enhancement.

Well, given the fact that the padics code was merged at SD 7 under the assumption that someone would write more doctests I could see this being a defect given the amount of time elapsed since then :)

Cheers,

Michael


---

Comment by was created at 2009-01-15 03:03:58

We changed this since the "defects" in trac should be actual bugs.  This will be helpful, e.g., next week at Sage Days 12 -- fix many bugs in Sage.  There are at least 600 (or so) *open* "defects" in trac right now.


---

Comment by kcrisman created at 2009-04-30 00:50:08

Is this now a duplicate of the behemoth work at #5778?


---

Comment by roed created at 2009-04-30 00:55:34

yes.  This is subsumed by #5778.


---

Comment by mabshoff created at 2009-04-30 00:56:23

Resolution: duplicate


---

Comment by mabshoff created at 2009-04-30 00:56:23

Replying to [comment:7 kcrisman]:
> Is this now a duplicate of the behemoth work at #5778?

Yes, David opened a new ticket, so nuke this as a dupe.

Cheers,

Michael
