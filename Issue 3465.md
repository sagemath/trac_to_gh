# Issue 3465: Number Field base rings for NumberFieldTower

Issue created by migration from Trac.

Original creator: roed

Original creation time: 2008-06-18 22:29:07

Assignee: was

CC:  craigcitro

Keywords: relative number fields

When creating towers of number fields, the base rings don't behave as I think they should.  The following is from the coercion branch (the opposite problem exists in the normal branch).

sage: sage: L.<cuberoot2, zeta3> = CyclotomicField(3).extension(x^3 - 2)
sage: type(L)
<class 'sage.rings.number_field.number_field.NumberField_relative'>
sage: L.ngens()
1 (2 in current Sage, I think it should be 1)
sage: L.base_ring()
Cyclotomic Field of order 3 and degree 2 (I agree)
sage: L.base_field()
Cyclotomic Field of order 3 and degree 2 (I agree)
sage: L.base()
Rational Field (I think it should be Cyclotomic Field of order 3 and degree 2)
sage: K.<a, b> = NumberField( [x^2 + x + 1, x^3 + 2] )
sage: K.ngens()
1 (2 in current Sage, I think it should be 2)sage: type(K)
<class 'sage.rings.number_field.number_field.NumberField_relative'>  
sage: K.base_ring()
Number Field in b with defining polynomial x^3 + 2 (I think it should be Rational Field)
sage: K.base_field()
Number Field in b with defining polynomial x^3 + 2 (I think it should be Rational Field)
sage: K.base()
Rational Field (um... ok, I agree)


---

Comment by roed created at 2008-06-18 22:34:46

Note that this affects the doctests for sage.rings.number_field.RelativeNumberFieldHomset.list


---

Comment by davidloeffler created at 2009-07-20 20:01:16

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-20 20:01:16

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2010-07-02 23:39:23

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-07-02 23:39:23

This ticket has been idle for nearly two years, and moreover it's not really clear to me exactly what the reporter considers to be a bug. Is the suggestion that the objects created via the NumberFieldTower constructor should somehow behave differently from ones created via the extension() method? That sounds like a bad idea to me.

I suggest closing this as wontfix. I'm setting this to "needs review" in order to request a second opinion on my proposal not to fix this.


---

Comment by lftabera created at 2010-07-03 10:27:20

Changing status from needs_review to positive_review.


---

Comment by lftabera created at 2010-07-03 10:27:20

I agree, the result should be homogenenous no matter how you have constructed the field.

I think that the problem is that base had no documentation.


---

Comment by mpatel created at 2010-07-20 07:03:14

Resolution: wontfix
