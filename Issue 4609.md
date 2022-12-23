# Issue 4609: Sage 3.2.1.a1: Make two optional magma doctests also depend on database_gap

Issue created by migration from https://trac.sagemath.org/ticket/4609

Original creator: mabshoff

Original creation time: 2008-11-25 00:34:27

Assignee: was

When running -only_optional=magma without the database_gap.spkg installed we see two failures:

```
sage -t -only-optional=magma -long devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/number_field.py", line 2455:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(algorithm='magma')   # optional - magma
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
**********************************************************************
```

and

```
sage -t -only-optional=magma -long devel/sage/sage/rings/polynomial/polynomial_element_generic.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/rings/polynomial/polynomial_element_generic.py", line 742:
    sage: f.galois_group(algorithm='magma')     # optional - magma
Expected:
    Transitive group number 5 of degree 4
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
    Transitive group number 5 of degree 4
**********************************************************************
```


The fix should be obvious :)

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-11-25 11:03:16

Positive review - exactly the fix I suggested.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-25 11:17:52

Merged in Sage 3.2.1.alpha1.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-25 11:17:52

Resolution: fixed
