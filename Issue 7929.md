# Issue 7929: Pickling fails for some residue fields

Issue created by migration from https://trac.sagemath.org/ticket/7929

Original creator: nthiery

Original creation time: 2010-01-14 14:09:55

Assignee: davidloeffler

Catched with #7921:


```
sage: K.<a> = NumberField(x^3-17)
sage: P = K.ideal(29).factor()[0][0]
sage: k = K.residue_field(P) # indirect doctest
sage: F = ZZ.residue_field(17)  # indirect doctest
sage: loads(dumps(k))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "sage_object.pyx", line 740, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8021)
  File "ring.pyx", line 2424, in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12853)
TypeError: 'NoneType' object is unsubscriptable

sage: loads(dumps(k.an_element()))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "sage_object.pyx", line 740, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8021)
  File "ring.pyx", line 2424, in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12853)
TypeError: 'NoneType' object is unsubscriptable

sage: loads(dumps(F))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "sage_object.pyx", line 740, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8021)
  File "ring.pyx", line 2424, in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12853)
TypeError: 'NoneType' object is unsubscriptable

sage: loads(dumps(F.an_element()))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "sage_object.pyx", line 740, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8021)
  File "ring.pyx", line 2424, in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12853)
TypeError: 'NoneType' object is unsubscriptable
```



---

Comment by roed created at 2011-11-19 02:38:55

This works in 4.7.2.


---

Comment by roed created at 2011-11-19 04:20:31

Changing status from new to needs_review.


---

Comment by roed created at 2011-11-19 04:20:37

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-11-26 13:07:22

Resolution: duplicate
