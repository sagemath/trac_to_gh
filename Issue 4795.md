# Issue 4795: Modular forms over finite fields need work

Issue created by migration from https://trac.sagemath.org/ticket/4795

Original creator: craigcitro

Original creation time: 2008-12-14 07:55:10

Assignee: craigcitro

The modular forms code hasn't really been tested too much with the base ring being a finite field. There was an old file `sage/modular/modform/bugs.py` which contained two tests, both of which fail.

First, we have what seems to be an infinite loop:

```
 sage: m = ModularForms(DirichletGroup(8).1,2,GF(7)); m
   Modular Forms space of dimension 2, character [1, -1] and weight 2 over Finite Field of size 7
   sage: m.basis()   # this just goes into infinite loop (???)
```


And now for a `NotImplementedError` -- the following *should* work but doesn't:

```
   sage: ModularForms(DirichletGroup(13, GF(7)).0^6,3).base_ring()
   Finite Field of size 7
```




---

Comment by AlexGhitza created at 2009-01-23 19:47:39

Tracking the first problem:


```
sage: m = ModularForms(DirichletGroup(8).1, 2, GF(7))
sage: bas = m.free_module().basis(); bas
[
(1, 0, 0, 0, 0),
(0, 1, 0, 0, 0),
(0, 0, 1, 0, 0),
(0, 0, 0, 1, 0),
(0, 0, 0, 0, 1)
]
sage: m(bas[0])   # infinite loop and bug warning
```


Note that this seems to be specific to using Dirichlet characters over finite fields, since the following works:


```
sage: m = ModularForms(8, 2, GF(7))
sage: m.basis()
[
1 + 3*q^4 + O(q^6),
q + 4*q^3 + 6*q^5 + O(q^6),
q^2 + O(q^6)
]
```



---

Comment by AlexGhitza created at 2013-07-22 11:26:26

Under 5.10, there's a coercion issue at the very beginning:


```
sage: m = ModularForms(DirichletGroup(8).1, 2, GF(7))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-3-a5d6a0e5413b> in <module>()
----> 1 m = ModularForms(DirichletGroup(Integer(8)).gen(1), Integer(2), GF(Integer(7)))

/opt/sage/local/lib/python2.7/site-packages/sage/modular/modform/constructor.pyc in ModularForms(group, weight, base_ring, use_cache, prec)
    343         M = ambient_eps.ModularFormsAmbient_eps(eps, weight)
    344         if base_ring != eps.base_ring():
--> 345             M = M.base_extend(base_ring) # ambient_R.ModularFormsAmbient_R(M, base_ring)
    346 
    347     if M is None:

/opt/sage/local/lib/python2.7/site-packages/sage/modular/modform/space.pyc in base_extend(self, base_ring)
    430         """
    431         if not base_ring.has_coerce_map_from(self.base_ring()):
--> 432             raise ValueError, "No coercion defined"
    433         else:
    434             return self.change_ring(base_ring)

ValueError: No coercion defined
```



---

Comment by AlexGhitza created at 2013-07-22 11:40:25

... and the obvious modification raises a NotImplementedError:


```
sage: m = ModularForms(DirichletGroup(8, GF(7)).1, 2, GF(7))
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-12-a7072f0f67a6> in <module>()
----> 1 m = ModularForms(DirichletGroup(Integer(8), GF(Integer(7))).gen(1), Integer(2), GF(Integer(7)))

/opt/sage/local/lib/python2.7/site-packages/sage/modular/modform/constructor.pyc in ModularForms(group, weight, base_ring, use_cache, prec)
    335             # Need to add a lift_to_char_0 function for characters,
    336             # and need to still remember eps.
--> 337             raise NotImplementedError, "currently the character must be over a ring of characteristic 0."
    338         eps = eps.minimize_base_ring()
    339         if eps.is_trivial():

NotImplementedError: currently the character must be over a ring of characteristic 0.
```


Maybe we should turn this into an enhancement ticket.
