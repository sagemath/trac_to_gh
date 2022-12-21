# Issue 9367: S_unit return type is incorrect,

Issue created by migration from Trac.

Original creator: syazdani

Original creation time: 2010-06-28 21:54:48

Assignee: davidloeffler

CC:  mjo

Keywords: S_units

Here is a sample error:

```
sage: _.<x>=QQ[]
sage: L.<alpha>=NumberField(x^3+x+1)
sage: p=L.S_units([ L.ideal(7) ] )
sage: p[0].parent()
Rational Field
```

The correct output should be

```
Number Field in alpha with defining polynomial x^3 + x + 1
```


The attached patch solves this problem.


---

Attachment

Fixes the return type.


---

Comment by mjo created at 2012-01-16 04:20:50

Add a doctest for the correct behavior.


---

Attachment

It looks like someone beat you to it! I get the correct answer with 4.8.alpha6, so I've added a doctest for it.


---

Comment by mjo created at 2012-01-16 04:22:20

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2012-03-12 20:10:42

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2012-03-12 20:10:42

Apply sage-trac_9367.patch

(for patchbot).


---

Comment by davidloeffler created at 2012-03-12 20:10:42

Changing priority from major to minor.


---

Comment by jdemeyer created at 2012-03-21 22:03:49

Resolution: fixed
