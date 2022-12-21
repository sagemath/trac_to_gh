# Issue 722: GF(100) gives weird error message

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-09-20 23:01:00

Assignee: somebody


```
sage: GF(100)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/dmharvey/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/rings/finite_field.py in FiniteField(order, name, modulus, names, elem_cache, check_irreducible, *args, **kwds)
    184                 raise ValueError, "finite field modulus must be irreducible but it is not"
    185         if name is None:
--> 186             raise TypeError, "you must specify the generator name"
    187         if order < 2**16:  
    188             # DO *NOT* use for prime subfield, since that would lead to

<type 'exceptions.TypeError'>: you must specify the generator name
```




---

Comment by mhansen created at 2007-09-23 19:55:12

This happens because of the order of the checks in GF.  See below:


```
sage: GF(13)
Finite Field of size 13

sage: GF(2^5)
Traceback (most recent call last):
...
TypeError: you must specify the generator name

sage: GF(2^5, 'a')
Finite Field in a of size 2^5
sage: GF(12)
Traceback (most recent call last):
...
TypeError: you must specify the generator name

sage: GF(12, 'a')
Traceback (most recent call last):
...
ArithmeticError: q must be a prime power


```


I guess it's a matter of deciding which of the two errors should come up first.


---

Comment by was created at 2007-09-23 21:54:47

Changing priority from major to minor.


---

Attachment


---

Comment by was created at 2007-09-25 06:33:45

fixed.


---

Comment by was created at 2007-09-25 06:33:45

Resolution: fixed
