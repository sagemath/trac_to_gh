# Issue 6814: jordan_form transformation lack of precision sage 4.1.1

Issue created by migration from https://trac.sagemath.org/ticket/6814

Original creator: Henryk.Trappmann

Original creation time: 2009-08-23 12:45:16

Assignee: tbd

Keywords: jordan, precision, matrix, transformation

There is an example for a lack of precision exception in the doc of jordan_form

```
sage: b = matrix(ZZ,3,3,range(9))
sage: jf, p = b.jordan_form(RealField(15), transformation=True)
...
ValueError: cannot compute the transformation matrix due to lack of precision
```

But if one increases the precision to the maximum still the same error occurs

```
sage: b = matrix(ZZ,3,3,range(9))
sage: jf, p = b.jordan_form(RealField(16777216), transformation=True)
...
ValueError: cannot compute the transformation matrix due to lack of precision
```



---

Comment by AlexGhitza created at 2009-11-15 13:07:00

Changing component from algebra to linear algebra.


---

Comment by spancratz created at 2010-01-19 12:26:25

Resolution: invalid


---

Comment by spancratz created at 2010-01-19 12:26:25

The error messages come up because the code does not actually detect numerically instability.  Instead, it notices when it fails, and assumes the only possible reason for this could be numerical instability.  Instead, there's a bug in the actual code.

Thus, this ticket can be closed as being "invalid".
