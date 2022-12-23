# Issue 9336: Improve doctest coverage for sage/rings/number_field

Issue created by migration from https://trac.sagemath.org/ticket/9336

Original creator: davidloeffler

Original creation time: 2010-06-25 15:10:10

Assignee: davidloeffler

CC:  cremona

Keywords: doctest




---

Comment by davidloeffler created at 2010-06-25 15:16:11

Changing status from new to needs_review.


---

Comment by cremona created at 2010-06-26 06:49:40

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-06-26 06:49:40

Good job!  Patch applies to 4.4.4 and tests pass and docs build fine.

After this the number_fields directory scores as follows:

```

SCORE sage/rings/number_field//unit_group.py: 100% (15 of 15)
SCORE sage/rings/number_field//number_field_element.pyx: 81% (91 of 111)
SCORE sage/rings/number_field//totallyreal.pyx: 100% (4 of 4)
SCORE sage/rings/number_field//number_field_base.pyx: 72% (8 of 11)
SCORE sage/rings/number_field//order.py: 100% (62 of 62)
SCORE sage/rings/number_field//number_field_element_quadratic.pyx: 95% (42 of 44)
SCORE sage/rings/number_field//number_field.py: 100% (183 of 183)
SCORE sage/rings/number_field//number_field_ideal.py: 92% (72 of 78)
SCORE sage/rings/number_field//totallyreal_dsage.py: 13% (2 of 15)
SCORE sage/rings/number_field//maps.py: 100% (23 of 23)
SCORE sage/rings/number_field//number_field_rel.py: 91% (62 of 68)
SCORE sage/rings/number_field//totallyreal_data.pyx: 100% (7 of 7)
SCORE sage/rings/number_field//small_primes_of_degree_one.py: 100% (4 of 4)
SCORE sage/rings/number_field//galois_group.py: 100% (29 of 29)
SCORE sage/rings/number_field//number_field_ideal_rel.py: 78% (22 of 28)
SCORE sage/rings/number_field//totallyreal_rel.py: 60% (3 of 5)
SCORE sage/rings/number_field//morphism.py: 100% (22 of 22)
SCORE sage/rings/number_field//class_group.py: 72% (13 of 18)
SCORE sage/rings/number_field//number_field_morphisms.pyx: 100% (13 of 13)
SCORE sage/rings/number_field//totallyreal_phc.py: 100% (2 of 2)
```



---

Comment by fwclarke created at 2010-06-27 19:47:14

Changing status from positive_review to needs_work.


---

Comment by fwclarke created at 2010-06-27 19:47:14

Just one little niggle: according to the developer's guide, code like

```
        try: 
            return self.list()[0] 
        except: 
            raise ValueError, "Set is empty"
```

(lines 91 to 94 in the patched morphism.py) should be avoided.  Better would be

```
        try: 
            return self[0] 
        except IndexError: 
            raise ValueError, "Set is empty"
```



---

Comment by cremona created at 2010-06-28 04:48:19

OK, I agree that would be better.


---

Attachment

patch against 4.4.4


---

Comment by davidloeffler created at 2010-06-28 08:53:08

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-06-28 08:53:08

Here's a new patch, which explicitly checks whether the length of the list is 0 rather than using try/except.


---

Comment by fwclarke created at 2010-06-28 17:46:12

Replying to [comment:6 davidloeffler]:
> Here's a new patch ...

That works fine, so back to positive review.


---

Comment by fwclarke created at 2010-06-28 17:46:12

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 07:52:58

Resolution: fixed
