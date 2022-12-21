# Issue 305: weird pickling bug in padics

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-03-03 14:57:19

Assignee: somebody


```
sage: K = pAdicField(5)
sage: x = K(0)
sage: y = loads(dumps(x))
sage: x.parent().print_prec()
 Infinity
sage: y.parent().print_prec()
 <class 'sage.rings.padic_field.pAdicField_generic'>
```




---

Comment by dmharvey created at 2007-03-03 15:09:53

Two more examples of weirdness:

```
sage: K = pAdicField(5)
sage: x = K(0)
sage: x.prec()
 Infinity
sage: y = loads(dumps(x))
sage: y.prec()
 <class 'sage.rings.padic_field.pAdicField_generic'>
```


and


```
sage: K = pAdicField(5)
sage: x = K(42)
sage: x.prec()
 Infinity
sage: y = loads(dumps(x))
sage: y.prec()
 '_pAdicField_generic__p'
```



---

Comment by was created at 2007-03-06 22:22:57

This is fixed by David Roe's new p-adics in SAGE-2.3.


---

Comment by was created at 2007-03-06 22:22:57

Resolution: fixed
