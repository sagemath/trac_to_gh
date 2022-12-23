# Issue 503: 0^0 -- error or 1; and other exponentiation optimizations

Issue created by migration from https://trac.sagemath.org/ticket/503

Original creator: was

Original creation time: 2007-08-28 21:41:00

Assignee: boothby




---

Comment by was created at 2007-08-29 02:38:51

NOTE:  For polynomials x<sup>0</sup> should be 1 still.


---

Comment by boothby created at 2007-08-29 23:21:24

Changing status from new to assigned.


---

Comment by boothby created at 2007-08-29 23:21:24

*mostly* fixed by the patch:

[http://sage.math.washington.edu/home/boothby/my_patches/arith_2.8.3.hg](http://sage.math.washington.edu/home/boothby/my_patches/arith_2.8.3.hg)

the following files might still contain problems:

```
rings/integer.pyx
rings/rational.pyx

groups/abelian_gps/abelian_group_element.py
groups/abelian_gps/dual_abelian_group_element.py

rings/power_series_mpoly.pyx
rings/power_series_poly.pyx

schemes/generic/morphism.py

categories/morphism.pyx
categories/morphism.pyx

rings/padics/padic_extension_generic_element.py
rings/padics/padic_lazy_element.py
rings/padics/valuation.py
rings/padics/local_generic_element.pyx
rings/padics/padic_capped_absolute_element.pyx
rings/padics/padic_capped_relative_element.pyx
rings/padics/padic_fixed_mod_element.pyx
```



---

Comment by boothby created at 2007-09-07 01:12:09

Changing status from assigned to new.


---

Comment by boothby created at 2007-09-07 01:12:09

final patch (from me):

[http://sage.math.washington.edu/home/boothby/my_patches/arith503.hg](http://sage.math.washington.edu/home/boothby/my_patches/arith503.hg)

note:  the following files have no doctests, and are difficult to use -- hence have not been updated.  Once #610 is resolved, the pow methods there should be updated and this can be resolved.


```
rings/padics/padic_extension_generic_element.py
rings/padics/padic_lazy_element.py
rings/padics/valuation.py
rings/padics/local_generic_element.pyx
rings/padics/padic_capped_absolute_element.pyx
rings/padics/padic_capped_relative_element.pyx
rings/padics/padic_fixed_mod_element.pyx
```



---

Comment by boothby created at 2007-09-07 01:12:09

Changing assignee from boothby to roed.


---

Comment by boothby created at 2007-09-07 01:14:42

Changing assignee from roed to robertwb.


---

Attachment

Fixed remaining instances of __pow__


---

Comment by robertwb created at 2007-09-07 03:18:27

Changing status from new to assigned.


---

Comment by was created at 2007-09-07 04:08:04

Resolution: fixed
