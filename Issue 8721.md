# Issue 8721: Residue fields for relative number fields broken (again)

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2010-04-20 08:57:22

Assignee: davidloeffler


```
sage: L.<a, b> = NumberField([x^2 - 3, x^2 - 5])
sage: L.ideal(a).residue_field()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (921, 0))

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/masiao/<ipython console> in <module>()

/storage/masiao/sage-4.4.alpha0/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_ideal.pyc in residue_field(self, names)
   2372         if not self.is_prime():
   2373             raise ValueError, "The ideal must be prime"
-> 2374         return self.number_field().residue_field(self, names = names)
   2375 
   2376     def residue_class_degree(self):

/storage/masiao/sage-4.4.alpha0/local/lib/python2.6/site-packages/sage/rings/number_field/number_field.pyc in residue_field(self, prime, names, check)
   4171             raise ValueError, "%s is not a prime ideal"%prime
   4172         from sage.rings.residue_field import ResidueField
-> 4173         return ResidueField(prime, names = names, check = False)
   4174 
   4175     def signature(self):

/storage/masiao/sage-4.4.alpha0/local/lib/python2.6/site-packages/sage/rings/residue_field.so in sage.rings.residue_field.ResidueField (sage/rings/residue_field.c:4132)()

/storage/masiao/sage-4.4.alpha0/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_ideal.pyc in __call__(self, x)
   2476         # Write back in terms of K
   2477         z = w * self.__M_OK_map
-> 2478         return self.__OK(z.list())
   2479 
   2480     def __repr__(self):

/storage/masiao/sage-4.4.alpha0/local/lib/python2.6/site-packages/sage/rings/number_field/order.pyc in __call__(self, x)
   1399         """
   1400 
-> 1401         x = self._K(x)
   1402         abs_order = self._absolute_order
   1403         to_abs = abs_order._K.structure()[1]

/storage/masiao/sage-4.4.alpha0/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6161)()

/storage/masiao/sage-4.4.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3109)()

/storage/masiao/sage-4.4.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3011)()

/storage/masiao/sage-4.4.alpha0/local/lib/python2.6/site-packages/sage/rings/number_field/number_field.pyc in _element_constructor_(self, x)
   1019                  self.base_ring().has_coerce_map_from(x.parent().base_ring())):
   1020             if len(x) != self.relative_degree():
-> 1021                 raise ValueError, "Length must be equal to the degree of this number field"
   1022             result = x[0]
   1023             for i in xrange(1,self.relative_degree()):

ValueError: Length must be equal to the degree of this number field
```

We've had problems with similar issues before -- see #6463 -- and the doctest I added back then shows that not all relative residue fields are broken; but this one seems to be!


---

Comment by davidloeffler created at 2011-01-25 17:15:31

Here's a patch.


---

Comment by davidloeffler created at 2011-01-25 17:15:31

Changing status from new to needs_review.


---

Attachment


---

Comment by mstreng created at 2011-01-27 16:46:03

Changing status from needs_review to positive_review.


---

Comment by mstreng created at 2011-01-27 16:46:03

fixes at least this example, all tests pass, and everything I tried worked


---

Comment by jdemeyer created at 2011-02-07 08:14:28

Resolution: fixed
