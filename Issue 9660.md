# Issue 9660: Obtaining the string representation of a number field ideal takes too long

Issue created by migration from https://trac.sagemath.org/ticket/9660

Original creator: jdemeyer

Original creation time: 2010-08-01 15:52:53

Assignee: davidloeffler

In order to obtain the string representation of an NumberFieldFractionalIdeal, the class group of the number field is computed to determine whether or not the ideal is principal.  This can take a very long time.  For example, the following is essentially immediate:

```
sage: K.<zeta> = CyclotomicField(23)
sage: F = K.ideal(2).factor()
```

But now, doing

```
sage: F
```

takes a very long time.


---

Comment by mvngu created at 2010-09-10 12:27:13

Resolution: invalid
