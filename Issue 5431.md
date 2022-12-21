# Issue 5431: Command line parser fails on hex values with 'e'

Issue created by migration from Trac.

Original creator: rhinton

Original creation time: 2009-03-03 19:18:40

Assignee: somebody

CC:  robertwb


```
sage: 0xe
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ryan/.sage/temp/fileserv/1535/_home_ryan__sage_init_sage_0.py in <module>()

/home/ryan/sage-well/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.create_RealNumber (sage/rings/real_mpfr.c:21774)()

/home/ryan/sage-well/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealLiteral.__init__ (sage/rings/real_mpfr.c:20990)()

/home/ryan/sage-well/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber.__init__ (sage/rings/real_mpfr.c:7454)()

/home/ryan/sage-well/local/lib/python2.5/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:7957)()

TypeError: Unable to convert x (='0xe') to real number.
```

The same thing happens with "0xE".  It appears the parser sees the E/e and assumes it is a floating-point number instead of using the leading "0x".  



---

Attachment

This was fixed by the preparser rewrite work by robertwb.


---

Comment by robertwb created at 2009-06-05 03:41:25

Patch adds doctest.


---

Comment by ncalexan created at 2009-06-13 21:50:12

Resolution: fixed
