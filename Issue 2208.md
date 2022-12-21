# Issue 2208: implement is_field for rings of integers

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-19 02:29:00

Assignee: was


```
sage: R = CyclotomicField(4).ring_of_integers()
sage: R.is_field()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/<ipython console> in <module>()

/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.IntegralDomain.is_field()

/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.Ring.is_finite()

<type 'exceptions.NotImplementedError'>: 
```


Also

```
sage: R = NumberField(x^3 + 2, 'a').ring_of_integers()
sage: R.is_field()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/<ipython console> in <module>()

/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.IntegralDomain.is_field()

/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.Ring.is_finite()

<type 'exceptions.NotImplementedError'>:
```



---

Comment by craigcitro created at 2008-02-19 03:30:39

Made the obvious fix, both the examples above now work (though there are different doctests).


---

Comment by craigcitro created at 2008-02-19 03:30:39

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-02-19 03:30:39

Changing assignee from was to craigcitro.


---

Comment by was created at 2008-02-19 04:23:47

I would delete "This exists for compatibility purposes." from the docstring.   It really says nothing useful and if we're going to write that we could write that sort of thing all over the place.


---

Attachment

New patch posted, removes the questionable verbiage. Adds another doctest.


---

Comment by ncalexan created at 2008-02-21 07:48:23

Looks good to me.


---

Comment by mabshoff created at 2008-02-25 01:51:22

Resolution: fixed


---

Comment by mabshoff created at 2008-02-25 01:51:22

Merged in Sage 2.10.3.alpha0
