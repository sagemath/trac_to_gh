# Issue 5136: sage-3.3.alpha3 gets stuck computing the ring of integers of a relative number field

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-01-30 09:40:00

Assignee: was

David Loeffler reported this on sage-devel:


```
sage: K.<a> = QuadraticField(-23)
sage: L.<b> = K.extension(x^3 - x - 1)
sage: OL = L.ring_of_integers()   # infinite loop?
```


Note also that CTRL-C seems to have no effect.  I see the same problem on my 32-bit Archlinux machine.



---

Comment by AlexGhitza created at 2009-01-30 09:43:39

Actually, CTRL-C does eventually stop this, with the following result:


```
KeyboardInterrupt                         Traceback (most recent call last)

/home/ghitza/.sage/temp/artin/14950/_home_ghitza__sage_init_sage_0.py in <module>()

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_base.so in sage.rings.number_field.number_field_base.NumberField.ring_of_integers (sage/rings/number_field/number_field_base.c:1090)()

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_rel.pyc in maximal_order(self)
    438         O = K.maximal_order()
    439         B = [from_K(z) for z in O.basis()]
--> 440         OK = self.order(B, check_is_integral=False, check_rank=False)
    441         self.__maximal_order = OK
    442         return OK

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_rel.pyc in order(self, *gens, **kwds)
   1363             gens = gens[0]
   1364         gens = [self(x) for x in gens]
-> 1365         return order.relative_order_from_ring_generators(gens, **kwds)
   1366         
   1367 

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc in relative_order_from_ring_generators(gens, check_is_integral, check_rank, is_maximal, allow_subfield)
   1647     abs_order =  absolute_order_from_module_generators(absolute_order_module_gens,
   1648                                                        check_integral=False, check_is_ring=False,
-> 1649                                                        check_rank=check_rank)
   1650     
   1651     return RelativeOrder(K, abs_order, check=False, is_maximal=is_maximal)

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc in absolute_order_from_module_generators(gens, check_integral, check_rank, check_is_ring, is_maximal, allow_subfield)
   1565     mod_gens = [to_V(x) for x in gens]
   1566     ambient = ZZ**V.dimension()
-> 1567     W = ambient.span(mod_gens)
   1568 
   1569     if allow_subfield:

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in span(self, gens, base_ring, check, already_echelonized)
   2146         if base_ring is None or base_ring == self.base_ring():
   2147             return FreeModule_submodule_pid(
-> 2148                 self.ambient_module(), gens, check=check, already_echelonized=already_echelonized)
   2149         else:
   2150             try:

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in __init__(self, ambient, gens, check, already_echelonized)
   4738         """
   4739         FreeModule_submodule_with_basis_pid.__init__(self, ambient, basis=gens, 
-> 4740             echelonize=True, already_echelonized=already_echelonized)
   4741 
   4742     def _repr_(self):

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in __init__(self, ambient, basis, check, echelonize, echelonized_basis, already_echelonized)
   3929 
   3930         if echelonize and not already_echelonized:
-> 3931             basis = self._echelonized_basis(ambient, basis)
   3932         
   3933         FreeModule_generic.__init__(self, R, rank=len(basis), degree=ambient.degree(), sparse=ambient.is_sparse())

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in _echelonized_basis(self, ambient, basis)
   4043         if d != 1:
   4044             basis = [x*d for x in basis]
-> 4045         A = MAT(basis)
   4046         E = A.echelon_form()
   4047         if d != 1:

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/matrix/matrix_space.pyc in __call__(self, entries, coerce, copy, rows)
    341                 entries = e
    342             else:
--> 343                 entries = sum([v.list() for v in entries],[])
    344 
    345         if rows is None:

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)
      7 
      8 def my_sigint(x, n):
----> 9     raise KeyboardInterrupt
     10 
     11 def my_sigfpe(x, n):

KeyboardInterrupt: 
```



---

Comment by AlexGhitza created at 2009-01-30 11:18:08

It is, in fact, not an infinite loop.  It's just really, really slow.  It also seems to pre-date 3.3.alpha3:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: K.<a> = QuadraticField(-23)
sage: L.<b> = K.extension(x^3 - x - 1)
sage: time OL = L.ring_of_integers()
CPU times: user 263.94 s, sys: 12.98 s, total: 276.92 s
Wall time: 280.13 s
```



---

Comment by AlexGhitza created at 2009-01-30 11:18:08

Changing priority from blocker to major.


---

Comment by ncalexan created at 2009-01-30 17:31:54

I do not think this is a problem with the relative number field patch; it was an existing problem.  I have code that I can submit if you want to compute the relative ring of integers; it uses pari's rnfbasis.

This issue has to with the fact that `L.ring_of_integers().base_ring()` is ZZ and not `K.ring_of_integers()`.  There's already a ticket for that.


---

Comment by davidloeffler created at 2009-06-26 18:15:48

This works for me now (in sage 4.0.2):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: unitary
sage: K.<a> = QuadraticField(-23)
sage: L.<b> = K.extension(x^3 - x - 1)
sage: time OL = L.ring_of_integers()
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
```

| Sage Version 4.0.2, Release Date: 2009-06-18                       |
| Type notebook() for the GUI, and license() for information.        |
I don't know what's changed -- presumably this is something to do with Francis Clarke's campaign to fix all the relative number field bugs over the last couple of months -- but presumably we can close this ticket now?


---

Comment by davidloeffler created at 2009-07-21 08:14:01

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-21 08:14:01

Changing assignee from was to davidloeffler.


---

Comment by fwclarke created at 2009-07-22 17:16:36

Replying to [comment:4 davidloeffler]:
> This works for me now (in sage 4.0.2):
> ...
> I don't know what's changed -- presumably this is something to do with Francis Clarke's campaign to fix all the relative number field bugs over the last couple of months -- but presumably we can close this ticket now?
Yes, this issue had already been raised in #4738, and I commented there that "The problem of the slowness of computing relative maximal orders is solved by the patch in #5842.  A doctest is included at line 532 of the patched `number_field_rel.py`" (It's become line 570 by 4.1)  

What changed was a rewrite of `maximal_order` for relative number fields. The previous version was repetitive and grossly wasteful of memory.


---

Comment by davidloeffler created at 2010-07-28 17:10:21

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-07-28 17:10:21

We should close this ticket -- two people agree that it's fixed and there are doctests to prove it.


---

Comment by davidloeffler created at 2010-07-28 17:10:48

I'm setting this to "positive review" so the release manager can close it when convenient.


---

Comment by davidloeffler created at 2010-07-28 17:10:48

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-07 04:58:08

Resolution: duplicate


---

Comment by mpatel created at 2010-08-07 04:58:08

I'm closing this ticket as a "duplicate."
