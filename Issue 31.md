# Issue 31: modular forms -- missing q_eigenform functionality

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:27:20

Assignee: somebody

*q_eigenform on old factors doesn't work:


```
sage: M = ModularSymbols(63,2,sign=1).cuspidal_subspace()
sage: M[2].q_eigenform()
Traceback (most recent call last):
    M[2].q_eigenform()
...
AttributeError: 'ModularSymbolsAmbient_wt2_g0' object has no attribute 'subspace_generated_by_images'
```



---

Comment by was created at 2007-01-13 02:04:50

Resolution: fixed


---

Comment by was created at 2007-01-13 02:04:50

Fixed -- or rather, now there is the *correct* error message:

```

sage: M = ModularSymbols(63,2,sign=1).cuspidal_subspace()
sage: M[2].q_eigenform()
Traceback (most recent call last):
...
ArithmeticError: self must be simple.


```

