# Issue 3881: [with patch, needs review] Quiet three MPolynomialRing deprecation warnings

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-16 21:20:17

Assignee: mabshoff

Currently we have:

```
sage -t -long devel/sage/sage/rings/fraction_field_element.py
/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/.doctest_fraction_field_element.py:1: DeprecationWarning: MPolynomialRing is deprecated, use PolynomialRing instead!
  # -*- coding: utf-8 -*-


sage -t -long devel/sage/sage/modules/free_quadratic_module.py
/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/.doctest_free_quadratic_module.py:1: DeprecationWarning: MPolynomialRing is deprecated, use PolynomialRing instead!
  # -*- coding: utf-8 -*-
/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/.doctest_free_quadratic_module.py:1: DeprecationWarning: MPolynomialRing is deprecated, use PolynomialRing instead!
  # -*- coding: utf-8 -*-
```

The attached patch fixes that.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-08-16 21:49:37

Merged in Sage 3.1.final


---

Comment by mabshoff created at 2008-08-16 21:49:37

Resolution: fixed
