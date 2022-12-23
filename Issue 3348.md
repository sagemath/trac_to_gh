# Issue 3348: Coercion problem: creating vectors from a mix of python and symbolic types

Issue created by migration from https://trac.sagemath.org/ticket/3348

Original creator: dunfield

Original creation time: 2008-06-01 20:22:01

Assignee: robertwb

In the following (isomorphic) cases, the first entry is floored

```
sage: vector(eval("[0.78, 1, 1 + 2.38 * I]"))
(0, 1, 2.38000000000000*I + 1)
sage: vector([float(5.52), int(1), 1.3*x])
(5, 1, 1.30000000000000*x)
```

Note: the order of the types here seems to have to be (float, int, symbolic ring) for this to occur.  If one uses proper Sage types, the problem goes away:

```
vector(sage_eval("[0.78, 1, 1 + 2.38 * I]"))
(0.780000000000000, 1.00000000000000, 2.38000000000000*I + 1)
```






---

Comment by mhansen created at 2009-06-04 22:55:41

Resolution: invalid


---

Comment by mhansen created at 2009-06-04 22:55:41

This has been fixed in the switch to Pynac symbolics:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: vector(eval("[0.78, 1, 1 + 2.38 * I]"))
(0.78, 1.0, 1.00000000000000 + 2.38000000000000*I)
sage: _.parent()
Vector space of dimension 3 over Symbolic Ring
sage: sage: vector([float(5.52), int(1), 1.3*x])
(5.52, 1.0, 1.30000000000000*x)
sage: _.parent()
Vector space of dimension 3 over Symbolic Ring
sage: vector(sage_eval("[0.78, 1, 1 + 2.38 * I]"))
(0.780000000000000, 1.00000000000000, 1.00000000000000 + 2.38000000000000*I)
sage: _.parent()
Vector space of dimension 3 over Symbolic Ring
```

