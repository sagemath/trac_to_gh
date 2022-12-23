# Issue 1901: mistake in the documentation for gens for Finite field pari

Issue created by migration from https://trac.sagemath.org/ticket/1901

Original creator: was

Original creation time: 2008-01-24 00:36:11

Assignee: somebody


```
sage: sage.rings.finite_field_ext_pari.FiniteField_ext_pari.gen?
[...]
Docstring:

           Return chosen generator of the finite field.  This generator
           is a root of the defining polynomial of the finite field, and
           is guaranteed to be a generator for the multiplicative group.

(This is wrong because in this case the generator is not guaranteed to
be a generator for the multiplicative group.)
```



---

Comment by cremona created at 2008-03-01 17:07:33

Changing assignee from somebody to cremona.


---

Attachment

Attached patch 8684.patch corrects the docstring and adds a relevant doctest.


---

Comment by cremona created at 2008-03-01 17:07:33

Changing status from new to assigned.


---

Comment by cwitty created at 2008-03-01 18:31:04

It looks like there's some randomness in `FiniteField_ext_pari(23^20, "b")`, such that the proposed doctests will often fail.  Here's one failure mode, with two failing doctests:

```
sage -t  devel/sage-review/sage/rings/finite_field_ext_pari.py**********************************************************************
File "finite_field_ext_pari.py", line 300:
    sage: F.gen().multiplicative_order() == F.order()-1
Expected:
    False
Got:
    True
**********************************************************************
File "finite_field_ext_pari.py", line 302:
    sage: F.multiplicative_generator()
Expected:
    b + 1
Got:
    b
**********************************************************************
```


And here's the other failure mode, with only one failing doctest:

```
sage -t  devel/sage-review/sage/rings/finite_field_ext_pari.py**********************************************************************
File "finite_field_ext_pari.py", line 302:
    sage: F.multiplicative_generator()
Expected:
    b + 1
Got:
    b + 14
**********************************************************************
```


And sometimes both tests pass.


---

Comment by cremona created at 2008-03-02 17:23:28

Apply this after 8684.patch!


---

Attachment

The second patch 8685.patch removes the doctests which are too random to be useful, and also adds to the docstring so that users are referred to multiplicative_generator() and warned that _both_ are random.


---

Comment by mabshoff created at 2008-03-11 03:03:27

I am setting the Summary field to the old setting. If that is incorrect please change it to something meaningful.

Cheers,

Michael


---

Comment by cremona created at 2008-03-11 09:19:48

Summary field is fine now -- I wish someone (cwitty?) would give this the thumbs up, otherwise the *wrong* doc sentence will go out with 2.10.3...


---

Comment by AlexGhitza created at 2008-03-11 15:43:50

The changes look good to me, the patches apply cleanly against 2.10.3.rc5, and doctests pass.


---

Comment by mabshoff created at 2008-03-12 22:04:12

Resolution: fixed


---

Comment by mabshoff created at 2008-03-12 22:04:12

Merged in Sage 2.10.4.alpha0
