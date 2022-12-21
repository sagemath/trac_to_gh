# Issue 8157: why the bit limit of 2^24 in RealField?

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-02-02 21:23:35

Assignee: AlexGhitza


```
sage: R = RealField(16777217)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/users/caramel/zimmerma/.sage/temp/patate.loria.fr/31828/_users_caramel_zimmerm\
a__sage_init_sage_0.py in <module>()

/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so\
 in sage.rings.real_mpfr.RealField_constructor (sage/rings/real_mpfr.c:3723)()

/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so\
 in sage.rings.real_mpfr.RealField.__init__ (sage/rings/real_mpfr.c:3945)()

ValueError: prec (=16777217) must be >= 2 and <= 16777216.
```

Note that 2^24 bits is only slightly above 5M digits, which is
quite small (Fabrice Bellard recently computed 2700 billions of digits of Pi on a personal desktop, i.e., about 500,000 times more).
of Pi


---

Attachment


---

Comment by zimmerma created at 2010-02-23 21:53:18

The attached patch solves this problem, for example:

```
sage: time a=n(pi,digits=10^7)
CPU times: user 113.52 s, sys: 0.22 s, total: 113.73 s
Wall time: 114.21 s
```



---

Comment by zimmerma created at 2010-02-23 21:53:18

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-02-25 10:49:07

Looks good and passes tests.

The referee patch adds a couple of doctests (bug fixes should be accompanied by doctests so that we don't regress again).  The slightly weird "OverflowError: ..." in the second test is due to the fact that the error messages are slightly different on 32-bit than on 64-bit machines.


---

Comment by AlexGhitza created at 2010-02-25 10:49:07

Changing status from needs_review to positive_review.


---

Attachment

apply after the first patch


---

Comment by mvngu created at 2010-03-02 21:11:17

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 21:11:17

Merged in this order:

 1. [trac_8157.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8157/trac_8157.patch)
 1. [trac_8157-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8157/trac_8157-doctest.patch)

Paul: I merged [trac_8157.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8157/trac_8157.patch), putting the ticket number in the commit message.


---

Comment by chapoton created at 2017-07-19 08:34:16

cedille
