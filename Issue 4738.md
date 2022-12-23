# Issue 4738: base_ring of orders in relative number fields is wrong

Issue created by migration from https://trac.sagemath.org/ticket/4738

Original creator: ncalexan

Original creation time: 2008-12-07 20:03:53

Assignee: was

CC:  was

Keywords: base ring relative number field order

I think that the last ring should be the ring of integers of the relative number field.


```
sage: K = NumberField([x^2 + 2, x^2 + 3], 'a')
sage: K.base_ring()
Number Field in a1 with defining polynomial x^2 + 3
sage: K.maximal_order()
Relative Order in Number Field in a0 with defining polynomial x^2 + 2 over its base field
sage: K.maximal_order().base_ring()
Integer Ring
```



---

Comment by ncalexan created at 2008-12-07 20:04:27

Sorry, the ring of integesr of the base field of the relative number field.


---

Comment by ncalexan created at 2008-12-07 20:33:49

While trying to fix this, I discovered that finding orders in relative number fields is ridiculously slow.  I think pari probably will help here, either but computing it directly or by computing a basis for the absolute order and then constructing a basis for the relative order from it.


```
sage: K.<a,b> = NumberField([x^4 + 1, x^4 - 3])
sage: K.base_field().maximal_order()
Maximal Order in Number Field in b with defining polynomial x^4 - 3
sage: K.absolute_field('c').maximal_order()
Maximal Order in Number Field in c with defining polynomial x^16 - 8*x^12 + 432*x^8 + 640*x^4 + 256
sage: K.absolute_field('c').maximal_order().basis()
[3/512*c^14 + 3/352*c^12 + 3/128*c^10 + 3/704*c^8 + 1/32*c^6 + 15/176*c^4 + 1/44, 7/1024*c^15 + 1/512*c^14 + 3/704*c^13 + 1/256*c^12 + 3/256*c^11 + 1/128*c^10 + 3/1408*c^9 + 3/64*c^8 + 1/64*c^7 + 1/32*c^6 + 15/352*c^5 + 1/16*c^4 + 1/88*c, 35/5632*c^14 + 3/256*c^12 + 7/704*c^10 + 3/64*c^8 + 1/88*c^6 + 1/16*c^4 + 1/88*c^2, 79/11264*c^15 + 3/512*c^14 + 7/512*c^13 + 1/128*c^12 + 7/1408*c^11 + 1/128*c^10 + 3/128*c^9 + 1/32*c^8 + 1/176*c^7 + 1/32*c^6 + 1/32*c^5 + 1/176*c^3, 1/128*c^12 + 1/32*c^8 + 1/8*c^4, 1/256*c^15 + 3/256*c^13 + 1/64*c^9 + 1/16*c^5, 1/256*c^14 + 1/64*c^10 + 1/16*c^6, 1/512*c^15 + 1/128*c^13 + 1/128*c^11 + 1/32*c^7, 1/16*c^8, 1/256*c^15 + 1/32*c^9, 1/32*c^10, 1/256*c^15 + 1/128*c^13 + 1/64*c^11, 1/64*c^12, 1/64*c^13, 1/128*c^14, 1/128*c^15]
sage: K.maximal_order()
  C-c C-c---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/47346/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in maximal_order(self)
   4894         O = K.maximal_order()
   4895         B = [from_K(z) for z in O.basis()]
-> 4896         OK = self.order(B, check_is_integral=False, check_rank=False)
   4897         self.__maximal_order = OK
   4898         return OK

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in order(self, *gens, **kwds)
   5630             gens = gens[0]
   5631         gens = [self(x) for x in gens]
-> 5632         return order.relative_order_from_ring_generators(gens, **kwds)
   5633         
   5634 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc in relative_order_from_ring_generators(gens, check_is_integral, check_rank, is_maximal, allow_subfield)
   1640     module_gens = [to_Kabs(a) for a in gens]
   1641     n = [a.absolute_minpoly().degree() for a in gens]
-> 1642     absolute_order_module_gens = monomials(module_gens, n)
   1643 
   1644     abs_order =  absolute_order_from_module_generators(absolute_order_module_gens,

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     15         nn = list(n)
     16         del nn[i]
---> 17         v = monomials(w, nn)
     18         k = len(v)
     19         for _ in range(n[i]-1):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in monomials(v, n)
     52     v = Sequence(v)
     53     R = v.universe()
---> 54     return _monomials(v, R, n, 0)
     55 
     56 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/monomials.pyc in _monomials(gens, R, n, i)
     19         for _ in range(n[i]-1):
     20             for j in range(k):
---> 21                 v.append(v[j]*z)
     22             z *= gens[i]
     23         return v

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)
      7 
      8 def my_sigint(x, n):
----> 9     raise KeyboardInterrupt
     10 
     11 def my_sigfpe(x, n):

KeyboardInterrupt:
```



---

Comment by fwclarke created at 2009-04-21 08:41:08

The problem of the slowness of computing relative maximal orders is solved
by the patch in #5842.  A doctest is included at line 532 of the patched
`number_field_rel.py`


---

Comment by davidloeffler created at 2009-07-21 08:12:20

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-21 08:12:20

Changing assignee from was to davidloeffler.


---

Comment by AlexGhitza created at 2014-04-18 01:19:35

Changing status from new to needs_review.


---

Comment by pbruin created at 2014-04-18 10:08:51

Do we really want the _maximal_ order of the base field?  I would say the base ring should be the intersection of the relative order with the base field.  In the following example, the order _R_ in _L_ does not contain the maximal order of _K_:

```
sage: K.<s> = QuadraticField(5)
sage: O = K.order(s)  # of index 2 in the maximal order of K
sage: L.<t> = K.extension(x^2 + 1)
sage: R = L.order((s, t))
sage: a = (1 + s)/2
sage: a.is_integral()
True
sage: L(a) in R  # check that R does not contain the maximal order of K
False
```

Note the `L(a)` in the last line; this is because there is also the following bug:

```
sage: s in R
False  # clearly wrong because R = ZZ[s, t] as a subring of L
```

----
New commits:


---

Comment by pbruin created at 2014-04-18 10:38:19

> Note the `L(a)` in the last line; this is because there is also the following bug:
> {{{
> sage: s in R
> False  # clearly wrong because R = ZZ[s, t] as a subring of L
> }}}
This would probably be fixed by implementing a coercion morphism from the base order to the relative order.  However, we currently cannot construct this morphism at all:

```
sage: O.hom((R(s),))
...
TypeError: images do not define a valid homomorphism
```

The error probably arises because `Order._is_valid_homomorphism_()` is not implemented.


---

Comment by pbruin created at 2014-05-03 15:54:36

Changing status from needs_review to needs_info.


---

Comment by pbruin created at 2014-05-03 15:54:36

The base ring should be either *Z* or the order intersected with the base field (which is in general not the maximal order of the base field).  We have to decide which is better.


---

Comment by jdemeyer created at 2017-03-01 11:17:46

Doctest failures.


---

Comment by jdemeyer created at 2017-03-01 11:17:46

Changing status from needs_info to needs_work.
