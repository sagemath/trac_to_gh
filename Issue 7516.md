# Issue 7516: bug in pickling quotient module over pid

Issue created by migration from https://trac.sagemath.org/ticket/7516

Original creator: was

Original creation time: 2009-11-23 04:56:05

Assignee: was

This is from the "report a problem" link in the notebook:

If you have a vector space, that is a quotient of a subspace of
another vector space, then after coercing elements into it, something
goes wrong in (un)pickling it.


```
sage: V = VectorSpace(QQ, 2)
sage: W = V.subspace([V([1,1])])
sage: Z = W.subspace([])
sage: WmodZ = W / Z
sage: WmodZ(W(0))
(0)
sage: loads(dumps(WmodZ))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/bosman/sage/<ipython console> in <module>()

/home/bosman/sage-4.2-linux-Ubuntu_9.04-i686-Linux/local/lib/python2.6/site-packages/sage/structure/sage_object.so
in sage.structure.sage_object.loads
(sage/structure/sage_object.c:8769)()

/home/bosman/sage-4.2-linux-Ubuntu_9.04-i686-Linux/local/lib/python2.6/site-packages/sage/modules/free_module.pyc
in __hash__(self)
  4576             True
  4577         """
-> 4578         return hash(self.__basis)
  4579
  4580     def construction(self):

AttributeError: 'FreeModule_submodule_field' object has no attribute
'_FreeModule_submodule_with_basis_pid__basis'
```





---

Comment by was created at 2010-01-19 12:13:23

NOTE:  This bug does not happen for Free modules over ZZ.  It's only over a field where the issue happens.  

```
sage: V = FreeModule(ZZ, 2)
sage: W = V.submodule([V([1,1])])
sage: Z = W.submodule([])
sage: WmodZ = W / Z
sage: loads(dumps(WmodZ))
Finitely generated module V/W over Integer Ring with invariants (0)
sage: WmodZ(W(0))
(0)
sage: loads(dumps(WmodZ))
Finitely generated module V/W over Integer Ring with invariants (0)
```



---

Attachment


---

Comment by was created at 2010-01-19 13:04:25

Changing status from new to needs_review.


---

Comment by SimonKing created at 2010-01-30 23:23:29

If I understand the patch correctly, it violates a very essential assumption about hash codes: The hash has to be the same for objects that are equal. But with the patch, it may be possible that during unpickling the hash "0" is returned,  while afterwards a completely different value is returned for _the same_ object.

This is giving me headache. Isn't it be possible that things are put in the wrong hash bucket?

Wouldn't it be a cleaner solution to ensure that self.!__basis is defined during unpickling before the hash is requested?

Could you explain why your solution is correct?


---

Comment by SimonKing created at 2010-01-30 23:23:29

Changing status from needs_review to needs_info.


---

Comment by sbrandhorst created at 2017-10-06 07:43:36


```
sage: V = VectorSpace(QQ, 2)
sage: W = V.subspace([V([1,1])])
sage: Z = W.subspace([])
sage: WmodZ = W / Z
sage: WmodZ(W(0))
(0)
sage: loads(dumps(WmodZ))

Vector space quotient V/W of dimension 1 over Rational Field where
V: Vector space of degree 2 and dimension 1 over Rational Field
Basis matrix:
[1 1]
W: Vector space of degree 2 and dimension 0 over Rational Field
Basis matrix:
[]
```


Works for me. Add a doctest and close?


---

Comment by tscrim created at 2017-10-09 04:32:41

Replying to [comment:8 sbrandhorst]:
> Works for me. Add a doctest and close?

Yep. Addendum - Also works for me.


---

Comment by sbrandhorst created at 2017-10-09 07:52:26

Changing status from needs_info to needs_review.


---

Comment by sbrandhorst created at 2017-10-09 07:52:26

New commits:


---

Comment by tscrim created at 2017-10-09 15:30:51

Once you put your real name as author, you can set a positive review.


---

Comment by sbrandhorst created at 2017-10-09 16:10:56

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-10-15 09:22:01

Resolution: fixed
