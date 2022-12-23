# Issue 316: bug in modular symbols projection (probably really in linear algebra)

Issue created by migration from https://trac.sagemath.org/ticket/316

Original creator: was

Original creation time: 2007-03-11 05:26:38

Assignee: was



```
e = EllipticCurve('34a')
```



```
m = ModularSymbols(34); s = m.cuspidal_submodule()
```



```
d = s.decomposition(7)
```



```
d
///
[
Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 9 for Gamma_0(34) of weight 2 with sign 0 over Rational Field,
Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 9 for Gamma_0(34) of weight 2 with sign 0 over Rational Field
]
```



```
a = d[0]; a
///
Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 9 for Gamma_0(34) of weight 2 with sign 0 over Rational Field
```



```
pi = a.projection()
```



```
pi(m([0,oo]))
///
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```



---

Comment by was created at 2007-03-11 05:26:53

Changing status from new to assigned.


---

Comment by was created at 2007-08-18 21:16:39

This is totally fixed in sage-2.8.


---

Comment by was created at 2007-08-18 21:16:39

Resolution: fixed
