# Issue 214: bug in small finite field error checking and modulus type

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-24 20:01:23

Assignee: somebody


```
It worries me that the outputs live in different rings for different
classes, and the latter is not even a field 
 
sage: x = ZZ['x'].0
 
sage: K.<a> = GF(11**11, name='a', modulus=x^11 - x + 1)
sage: type(K)
 <class 'sage.rings.finite_field.FiniteField_ext_pari'>
sage: K.modulus()
 x^11 - x + 1
 
sage: K.<a> = GF(5**5, name='a', modulus=x^5 - x + 1)
sage: type(K)
 <type 'sage.rings.finite_field_givaro.FiniteField_givaro'>
sage: K.modulus()
 a^5
 
Nick
```



---

Comment by was created at 2007-01-25 14:35:32

Resolution: fixed


---

Comment by was created at 2007-01-25 14:35:32

Fixed. for sage-1.9.
