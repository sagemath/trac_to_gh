# Issue 5587: input of hexadecimal integers is corrupted

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2009-03-22 21:50:42

Assignee: somebody


```
sage: 0xabcdf
703711
sage: 0xabcdef
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/zimmerma/.sage/temp/toto.loria.fr/11913/_home_zimmerma__sage_init_sage_0.py in <module>()

/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.create_RealNumber (sage/rings/real_mpfr.c:22110)()

/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealLiteral.__init__ (sage/rings/real_mpfr.c:21326)()

/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber.__init__ (sage/rings/real_mpfr.c:7473)()

/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:7976)()

TypeError: Unable to convert x (='0xabcdef') to real number.
```

I understand that Sage tries to recognize a floating-point number
due to the 'e', but then how to input a hexadecimal integer?


---

Comment by mvngu created at 2009-07-26 03:46:20

Looks like this is fixed in Sage 4.1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: 0xabcdf
703711
sage: 0xabcdef
11259375
```

I'm closing this ticket as fixed.


---

Comment by mvngu created at 2009-07-26 03:46:20

Resolution: fixed
