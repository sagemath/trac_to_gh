# Issue 5863: [with patch, needs review] remove some files from sage/algebras

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-04-23 06:07:02

Assignee: jhpalmieri

Coverage of some files in algebras:

```
algebra_ideal.py: 0% (0 of 19)
algebra_ideal_element.py: 0% (0 of 1)
algebra_order.py: 0% (0 of 16)
algebra_order_element.py: 0% (0 of 13)
algebra_order_frac_ideal.py: 0% (0 of 17)
algebra_order_ideal.py: 0% (0 of 21)
algebra_order_ideal_element.py: 0% (0 of 1)
```

Furthermore, these don't seem to be used by any of the rest of the Sage code, so let's delete them.


---

Attachment


---

Comment by was created at 2009-04-23 06:32:11

If anybody wants these to be in Sage, they should revert this patch, then get the coverage to 100% and get everything up to how things work in Sage now (e.g., coercion model, etc.).  Right now they are used nowhere and have no tests.


---

Comment by mabshoff created at 2009-04-23 07:04:47

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-23 07:04:47

Resolution: fixed
