# Issue 8671: FieldElement.quo_rem broken

Issue created by migration from https://trac.sagemath.org/ticket/8671

Original creator: burcin

Original creation time: 2010-04-11 12:19:05

Assignee: burcin


```
sage: P.<n> = QQ[]
sage: F = P.fraction_field()
sage: P.one_element()//F.one_element()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

.../sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.__floordiv__ (sage/rings/polynomial/polynomial_element.c:14608)()

.../sage/structure/element.so in sage.structure.element.NamedBinopMethod.__call__ (sage/structure/element.c:22812)()

.../sage/structure/element.so in sage.structure.element.FieldElement.quo_rem (sage/structure/element.c:16670)()

...
AttributeError: 'sage.rings.fraction_field_element.FractionFieldElement' object has no attribute '_parent'
```



---

Comment by burcin created at 2010-04-11 12:29:32

Changing status from new to needs_review.


---

Attachment


---

Comment by cremona created at 2010-04-25 16:29:44

I'm worried by the fact that right._parent fails while parent(right) succeeds.


---

Comment by burcin created at 2010-05-05 03:18:43

`_parent` is a cdef'd attribute. At the point this code is used, Cython doesn't know that `right` is an `Element`, so it generates code to look for a python attribute `_parent` which fails.

One solution would be to use a type cast by writing `(<Element>right)._parent`, but we'd have to handle python types like `int` manually before this. The function `parent()`, which in turn calls `sage.structure.parent.parent_c` is used exactly for this purpose.

Calling parent_c directly would be faster, but that is not exported in `sage/structure/parent.pxd`.


---

Comment by cremona created at 2010-05-16 15:49:25

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-05-16 15:49:25

That makes sense.

Patch applies fine to 4.4.2.rc0 and tests in sage/structure and sage/rings/ pass.  So, positive review.


---

Comment by mhansen created at 2010-06-06 01:20:33

Resolution: fixed
