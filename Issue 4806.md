# Issue 4806: broken real number exponent preparsing

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-12-15 17:04:37

Assignee: was

In sage 3.2:


```
sage: 1.656e02
165.600000000000      # ok
sage: 1.656e-02
0.0165600000000000     # ok
sage: 1.656e+02
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/david/<ipython console> in <module>()

/Users/david/sage-3.2/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.create_RealNumber (sage/rings/real_mpfr.c:21490)()

/Users/david/sage-3.2/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealLiteral.__init__ (sage/rings/real_mpfr.c:20706)()

/Users/david/sage-3.2/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber.__init__ (sage/rings/real_mpfr.c:7305)()

/Users/david/sage-3.2/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:7782)()

TypeError: Unable to convert x (='1.656e') to real number.
```


In plain python 2.5.2:

```
>>> 1.656e+02
165.59999999999999
```




---

Comment by boothby created at 2009-01-23 22:30:01

Rolled into #5079


---

Comment by boothby created at 2009-01-23 22:30:01

Resolution: duplicate
