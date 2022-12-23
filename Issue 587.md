# Issue 587: bug in floating point complex number creation

Issue created by migration from https://trac.sagemath.org/ticket/587

Original creator: was

Original creation time: 2007-09-04 15:16:50

Assignee: somebody

This was found by Markus Fraczek:

```
sage: 1e8
100000000.000000
sage: 1e8*I
boom -- typeerror
```



---

Comment by mhansen created at 2007-09-04 19:11:04

Changing assignee from somebody to mhansen.


---

Comment by mhansen created at 2007-09-04 19:37:06

There problem was that SAGE doesn't like strings such as "1.0E+8*I" in symbolic_expression_from_maxima_string() , and the fix to replace all such occurrences of scientific notation with expanded notation (or at least on that doesn't involved pluses.

587.patch patches the calculus.py file.
587-2.patches adds the problem as a doctest


---

Comment by mhansen created at 2007-09-04 19:37:22

patch for calculus.py


---

Attachment

patch for constants.py


---

Comment by was created at 2007-09-04 21:51:29

fixed by mike hansen.


---

Comment by was created at 2007-09-04 21:51:29

Resolution: fixed
