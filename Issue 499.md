# Issue 499: n() is undefined for rational numbers

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-28 17:45:59

Assignee: somebody

Reported by Ted Kosan in sage-support - see http://groups.google.com/group/sage-support/t/2a46ced7d28116eb


```
x = 1/2
x.n()

Exception (click to the left for traceback):
...
AttributeError: 'sage.rings.rational.Rational' object has no attribute 'n' 
```


Cheers,

Michael


---

Comment by was created at 2007-08-31 21:06:13

This is done, but it's capital N:

```
sage: x = 1/2
sage: x.N()
0.500000000000000
```



---

Comment by was created at 2007-08-31 21:06:13

Resolution: fixed
