# Issue 9413: Bug in tamagawa_product_bsd for elliptic curves over QQ

Issue created by migration from https://trac.sagemath.org/ticket/9413

Original creator: davidloeffler

Original creation time: 2010-07-02 21:50:42

Assignee: cremona


```
sage: E = EllipticCurve('30a')
sage: E.tamagawa_product_bsd()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/schemes/elliptic_curves/<ipython console> in <module>()

/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_number_field.pyc in tamagawa_product_bsd(self)
   1144             # the differential associated to this particular equation E
   1145             uu = self.isomorphism_to(dav.minimal_model()).u
-> 1146             uu_abs_val = pp.smallest_integer()**(pp.residue_class_degree()*valuation(uu,pp))
   1147             pr *= cv * uu_abs_val
   1148         return pr

/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2632)()

/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2835)()

/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2629)()

AttributeError: 'Ideal_pid' object has no attribute 'smallest_integer'
```



---

Attachment


---

Comment by wuthrich created at 2010-07-27 17:59:34

Changing status from new to needs_review.


---

Comment by cremona created at 2010-08-21 16:19:50

Looks fine, applies ok to 4.5.3.alpha1 (with a little fuzz) and all tests in ell_number_field pass (no other files call this function).


---

Comment by cremona created at 2010-08-21 16:19:50

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 11:38:08

Resolution: fixed
