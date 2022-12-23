# Issue 5136: sage-3.3.alpha3 gets stuck computing the ring of integers of a relative number field

archive/issues_005136.json:
```json
{
    "body": "Assignee: was\n\nDavid Loeffler reported this on sage-devel:\n\n\n```\nsage: K.<a> = QuadraticField(-23)\nsage: L.<b> = K.extension(x^3 - x - 1)\nsage: OL = L.ring_of_integers()   # infinite loop?\n```\n\n\nNote also that CTRL-C seems to have no effect.  I see the same problem on my 32-bit Archlinux machine.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5136\n\n",
    "created_at": "2009-01-30T09:40:00Z",
    "labels": [
        "number theory",
        "blocker",
        "bug"
    ],
    "title": "sage-3.3.alpha3 gets stuck computing the ring of integers of a relative number field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5136",
    "user": "AlexGhitza"
}
```
Assignee: was

David Loeffler reported this on sage-devel:


```
sage: K.<a> = QuadraticField(-23)
sage: L.<b> = K.extension(x^3 - x - 1)
sage: OL = L.ring_of_integers()   # infinite loop?
```


Note also that CTRL-C seems to have no effect.  I see the same problem on my 32-bit Archlinux machine.


Issue created by migration from https://trac.sagemath.org/ticket/5136





---

archive/issue_comments_039269.json:
```json
{
    "body": "Actually, CTRL-C does eventually stop this, with the following result:\n\n\n```\nKeyboardInterrupt                         Traceback (most recent call last)\n\n/home/ghitza/.sage/temp/artin/14950/_home_ghitza__sage_init_sage_0.py in <module>()\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_base.so in sage.rings.number_field.number_field_base.NumberField.ring_of_integers (sage/rings/number_field/number_field_base.c:1090)()\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_rel.pyc in maximal_order(self)\n    438         O = K.maximal_order()\n    439         B = [from_K(z) for z in O.basis()]\n--> 440         OK = self.order(B, check_is_integral=False, check_rank=False)\n    441         self.__maximal_order = OK\n    442         return OK\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_rel.pyc in order(self, *gens, **kwds)\n   1363             gens = gens[0]\n   1364         gens = [self(x) for x in gens]\n-> 1365         return order.relative_order_from_ring_generators(gens, **kwds)\n   1366         \n   1367 \n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc in relative_order_from_ring_generators(gens, check_is_integral, check_rank, is_maximal, allow_subfield)\n   1647     abs_order =  absolute_order_from_module_generators(absolute_order_module_gens,\n   1648                                                        check_integral=False, check_is_ring=False,\n-> 1649                                                        check_rank=check_rank)\n   1650     \n   1651     return RelativeOrder(K, abs_order, check=False, is_maximal=is_maximal)\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc in absolute_order_from_module_generators(gens, check_integral, check_rank, check_is_ring, is_maximal, allow_subfield)\n   1565     mod_gens = [to_V(x) for x in gens]\n   1566     ambient = ZZ**V.dimension()\n-> 1567     W = ambient.span(mod_gens)\n   1568 \n   1569     if allow_subfield:\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in span(self, gens, base_ring, check, already_echelonized)\n   2146         if base_ring is None or base_ring == self.base_ring():\n   2147             return FreeModule_submodule_pid(\n-> 2148                 self.ambient_module(), gens, check=check, already_echelonized=already_echelonized)\n   2149         else:\n   2150             try:\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in __init__(self, ambient, gens, check, already_echelonized)\n   4738         \"\"\"\n   4739         FreeModule_submodule_with_basis_pid.__init__(self, ambient, basis=gens, \n-> 4740             echelonize=True, already_echelonized=already_echelonized)\n   4741 \n   4742     def _repr_(self):\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in __init__(self, ambient, basis, check, echelonize, echelonized_basis, already_echelonized)\n   3929 \n   3930         if echelonize and not already_echelonized:\n-> 3931             basis = self._echelonized_basis(ambient, basis)\n   3932         \n   3933         FreeModule_generic.__init__(self, R, rank=len(basis), degree=ambient.degree(), sparse=ambient.is_sparse())\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in _echelonized_basis(self, ambient, basis)\n   4043         if d != 1:\n   4044             basis = [x*d for x in basis]\n-> 4045         A = MAT(basis)\n   4046         E = A.echelon_form()\n   4047         if d != 1:\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/matrix/matrix_space.pyc in __call__(self, entries, coerce, copy, rows)\n    341                 entries = e\n    342             else:\n--> 343                 entries = sum([v.list() for v in entries],[])\n    344 \n    345         if rows is None:\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)\n      7 \n      8 def my_sigint(x, n):\n----> 9     raise KeyboardInterrupt\n     10 \n     11 def my_sigfpe(x, n):\n\nKeyboardInterrupt: \n```\n",
    "created_at": "2009-01-30T09:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39269",
    "user": "AlexGhitza"
}
```

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

archive/issue_comments_039270.json:
```json
{
    "body": "It is, in fact, not an infinite loop.  It's just really, really slow.  It also seems to pre-date 3.3.alpha3:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: K.<a> = QuadraticField(-23)\nsage: L.<b> = K.extension(x^3 - x - 1)\nsage: time OL = L.ring_of_integers()\nCPU times: user 263.94 s, sys: 12.98 s, total: 276.92 s\nWall time: 280.13 s\n```\n",
    "created_at": "2009-01-30T11:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39270",
    "user": "AlexGhitza"
}
```

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

archive/issue_comments_039271.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2009-01-30T11:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39271",
    "user": "AlexGhitza"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_039272.json:
```json
{
    "body": "I do not think this is a problem with the relative number field patch; it was an existing problem.  I have code that I can submit if you want to compute the relative ring of integers; it uses pari's rnfbasis.\n\nThis issue has to with the fact that `L.ring_of_integers().base_ring()` is ZZ and not `K.ring_of_integers()`.  There's already a ticket for that.",
    "created_at": "2009-01-30T17:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39272",
    "user": "ncalexan"
}
```

I do not think this is a problem with the relative number field patch; it was an existing problem.  I have code that I can submit if you want to compute the relative ring of integers; it uses pari's rnfbasis.

This issue has to with the fact that `L.ring_of_integers().base_ring()` is ZZ and not `K.ring_of_integers()`.  There's already a ticket for that.



---

archive/issue_comments_039273.json:
```json
{
    "body": "This works for me now (in sage 4.0.2):\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: unitary\nsage: K.<a> = QuadraticField(-23)\nsage: L.<b> = K.extension(x^3 - x - 1)\nsage: time OL = L.ring_of_integers()\nCPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s\nWall time: 0.02 s\n```\n\n| Sage Version 4.0.2, Release Date: 2009-06-18                       |\n| Type notebook() for the GUI, and license() for information.        |\nI don't know what's changed -- presumably this is something to do with Francis Clarke's campaign to fix all the relative number field bugs over the last couple of months -- but presumably we can close this ticket now?",
    "created_at": "2009-06-26T18:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39273",
    "user": "davidloeffler"
}
```

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

archive/issue_comments_039274.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39274",
    "user": "davidloeffler"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_039275.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-21T08:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39275",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_039276.json:
```json
{
    "body": "Replying to [comment:4 davidloeffler]:\n> This works for me now (in sage 4.0.2):\n> ...\n> I don't know what's changed -- presumably this is something to do with Francis Clarke's campaign to fix all the relative number field bugs over the last couple of months -- but presumably we can close this ticket now?\nYes, this issue had already been raised in #4738, and I commented there that \"The problem of the slowness of computing relative maximal orders is solved by the patch in #5842.  A doctest is included at line 532 of the patched `number_field_rel.py`\" (It's become line 570 by 4.1)  \n\nWhat changed was a rewrite of `maximal_order` for relative number fields. The previous version was repetitive and grossly wasteful of memory.",
    "created_at": "2009-07-22T17:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39276",
    "user": "fwclarke"
}
```

Replying to [comment:4 davidloeffler]:
> This works for me now (in sage 4.0.2):
> ...
> I don't know what's changed -- presumably this is something to do with Francis Clarke's campaign to fix all the relative number field bugs over the last couple of months -- but presumably we can close this ticket now?
Yes, this issue had already been raised in #4738, and I commented there that "The problem of the slowness of computing relative maximal orders is solved by the patch in #5842.  A doctest is included at line 532 of the patched `number_field_rel.py`" (It's become line 570 by 4.1)  

What changed was a rewrite of `maximal_order` for relative number fields. The previous version was repetitive and grossly wasteful of memory.



---

archive/issue_comments_039277.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T17:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39277",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039278.json:
```json
{
    "body": "We should close this ticket -- two people agree that it's fixed and there are doctests to prove it.",
    "created_at": "2010-07-28T17:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39278",
    "user": "davidloeffler"
}
```

We should close this ticket -- two people agree that it's fixed and there are doctests to prove it.



---

archive/issue_comments_039279.json:
```json
{
    "body": "I'm setting this to \"positive review\" so the release manager can close it when convenient.",
    "created_at": "2010-07-28T17:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39279",
    "user": "davidloeffler"
}
```

I'm setting this to "positive review" so the release manager can close it when convenient.



---

archive/issue_comments_039280.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-28T17:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39280",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039281.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-08-07T04:58:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39281",
    "user": "mpatel"
}
```

Resolution: duplicate



---

archive/issue_comments_039282.json:
```json
{
    "body": "I'm closing this ticket as a \"duplicate.\"",
    "created_at": "2010-08-07T04:58:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5136#issuecomment-39282",
    "user": "mpatel"
}
```

I'm closing this ticket as a "duplicate."
