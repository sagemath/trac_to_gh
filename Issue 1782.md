# Issue 1782: doctests for multi_polynomial_ideal.py not reproducible

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-01-15 18:55:47

Assignee: malb

Keywords: test doctest multi polynomial ideal reporducible

In multi_polynomial_ideal.py, the doctests for

 * complete_primary_decomposition
 * groebner_basis
 * primary_decomposition

work under `sage -t` but do not work from the `sage:` prompt.  Presumably there is some singular initialization that is not being reproduced at the prompt?


---

Comment by ncalexan created at 2008-01-15 18:56:06

Changing keywords from "test doctest multi polynomial ideal reporducible" to "test doctest multi polynomial ideal reproducible".


---

Comment by malb created at 2008-01-23 21:29:54

This should be fixed since we compute reduced Gröbner bases by default.


---

Comment by malb created at 2008-03-28 11:41:21

Nick, as you reported the bug: I claim this is fixed. Could you check?


---

Comment by malb created at 2008-04-01 12:16:46

This issue is resolved, I just checked and I can reproduce all doctests. Someone not me please close this ticket :-)


---

Comment by mabshoff created at 2008-04-01 12:23:38

Resolution: fixed


---

Comment by mabshoff created at 2008-04-01 12:23:38

Your wish is my command ;)
