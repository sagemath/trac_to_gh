# Issue 9595: Conversion from constant PARI polynomials to QQ doesn't work

Issue created by migration from https://trac.sagemath.org/ticket/9595

Original creator: jdemeyer

Original creation time: 2010-07-25 12:03:14

Assignee: robertwb

We create a constant PARI polynomial with value 1/2 and coerce it to QQ:

```
sage: constpol = pari('Pol([1/2])')
sage: QQ(constpol)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/usr/local/src/sage-4.5.2.alpha0/<ipython console> in <module>()

/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()

/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)()

/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:6853)()

/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6285)()

TypeError: Unable to coerce PARI 1/2 to an Integer.
```


Note how the error message indicated conversion to Integer somehow.  Indeed, `QQ(pari('Pol([1])'))` works


---

Attachment


---

Comment by jdemeyer created at 2010-07-25 12:38:29

Changing status from new to needs_review.


---

Comment by cremona created at 2010-07-31 18:57:40

Patch looks good and applies fine to 4.5.1.  Runnng a full test on 32-bit now.


---

Comment by cremona created at 2010-08-01 21:28:23

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-08-01 21:28:23

Full long test worked fine.


---

Comment by mpatel created at 2010-08-09 09:47:37

Resolution: fixed
