# Issue 108: inconsistent return type for binomial function

Issue created by migration from https://trac.sagemath.org/ticket/108

Original creator: dmharvey

Original creation time: 2006-10-03 18:03:57

Assignee: somebody


```
sage: R = Integers(125)
sage: type(binomial(R(4), 2))
 <type 'integer_mod_pyx.IntegerMod_int'>
sage: type(binomial(R(4), 1))
 <type 'integer_mod_pyx.IntegerMod_int'>
sage: type(binomial(R(4), 0))
 <type 'rational.Rational'>
```


The type/parent should always match that of the first argument. (Or I suppose it could lie in the fraction field. But the above behaviour is a bit confusing.)



---

Comment by was created at 2006-10-05 08:15:00

Resolution: fixed


---

Comment by was created at 2006-10-05 08:15:00

Fixed trac Ticket #108: inconsistent return type for binomial function

This badness no longer happens:

```
  sage: R = Integers(125)
  sage: type(binomial(R(4), 2))
  <type 'integer_mod_pyx.IntegerMod_int'>
  sage: type(binomial(R(4), 0))
  <type 'rational.Rational'>
```

