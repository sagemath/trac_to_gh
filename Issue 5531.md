# Issue 5531: [with patch, needs review] Quaternion algebra docstring formatting needs small fixes

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-03-16 17:44:59

Assignee: davidloeffler

In a vanilla copy of 3.4, I get complaints from sage -docbuild because some of the docstrings in sage/algebras/quaternion_algebra.py are wrongly formatted. 


```
WARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra.py:docstring of sage.algebras.quaternion_algebra.unpickle_QuaternionAlgebra_v0:4: (WARNING/2) Inline emphasis start-string without end-string.
WARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_abstract.conjugate:13: (WARNING/2) Inline literal start-string without end-string.
WARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_generic:3: (WARNING/2) Literal block expected; none found.
WARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_rational_field:4: (WARNING/2) Literal block expected; none found.
WARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.unpickle_QuaternionAlgebraElement_generic_v0:2: (WARNING/2) Inline emphasis start-string without end-string.
WARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.unpickle_QuaternionAlgebraElement_generic_v0:2: (WARNING/2) Inline emphasis start-string without end-string.
```


This patch fixes that.


---

Comment by davidloeffler created at 2009-03-16 17:53:03

Changing status from new to assigned.


---

Attachment


---

Comment by mvngu created at 2009-03-17 03:44:44

REFEREE REPORT



The patch *quaternion_docstring_fix.patch* applied OK against Sage 3.4, doctests passed even with the `-long` option, and the reference manual builds fine. Positive review for the Sphinx formatting issues that the patch fixes.



However, while reviewing the patch I noticed some other formatting issues. But these are addressed in ticket #5541.


---

Comment by mabshoff created at 2009-03-20 21:50:57

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-20 21:50:57

Resolution: fixed
