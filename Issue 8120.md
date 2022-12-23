# Issue 8120: UniqueRepresentation and hash value

Issue created by migration from https://trac.sagemath.org/ticket/8120

Original creator: hivert

Original creation time: 2010-01-29 15:31:33

Assignee: AlexGhitza

CC:  zimmerma nthiery

The documentation of `UniqueRepresentation` says 

```
    Similarly, the identity is used as hash function, which is also as
    fast as it can get. However this means that the hash function may
    change in between Sage sessions, or even within the same Sage
    session (see below). Subclasses should overload :meth:`__hash__`
    if this could be a problem.
```

But there is no implementation of `__hash__`.

I'm adding one.


---

Comment by hivert created at 2010-01-29 15:49:52

Changing assignee from AlexGhitza to hivert.


---

Comment by hivert created at 2010-01-29 15:55:58

Changing keywords from "" to "UniqueRepresentation hash".


---

Comment by hivert created at 2010-01-29 15:55:58

Changing status from new to needs_review.


---

Comment by hivert created at 2010-01-29 15:55:58

I just submitted a patch which comply with the documentation. However, since we are in `UniqueRepresentations` we could use `__classcall__` which knows the parameters that constructed the object to insert into the created object the hash value of those parameters in the same veins it insert some stuff needed for pickling/unpickling. Any comment about that ?

Florent


---

Comment by zimmerma created at 2010-02-06 20:26:26

I'd like to review that patch but I'm missing an example to try.

Paul


---

Comment by was created at 2010-02-07 06:03:41

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-02-07 09:01:10

Hi Paul,

Replying to [comment:3 zimmerma]:
> I'd like to review that patch but I'm missing an example to try.

I'm not sure what you want: in the patch you have the following tests example:

```
sage: class bla(UniqueRepresentation, SageObject): pass 
sage: x = bla(); hx = hash(x) 
sage: x.rename("toto")    
sage: hx == hash(x) 
True 
```

If you want more elaborated examples using `UniqueRepresentation`, they are dozens of them through sage library (the ultimate goal is that nearly each parent inherits from this). Pick you favorite one (prime.py is a good example see #7397):

```
tomahawk-*ge-combinat/sage $ grep -l UniqueRepresentation **/*.py
categories/category.py
categories/enumerated_sets.py
categories/examples/commutative_additive_monoids.py
categories/examples/commutative_additive_semigroups.py
categories/examples/finite_coxeter_groups.py
categories/examples/finite_enumerated_sets.py
categories/examples/finite_monoids.py
categories/examples/finite_semigroups.py
categories/examples/finite_weyl_groups.py
categories/examples/infinite_enumerated_sets.py
categories/examples/monoids.py
categories/examples/semigroups.py
categories/examples/sets_cat.py
categories/primer.py
categories/semigroups.py
categories/sets_cat.py
combinat/crystals/affine.py
combinat/crystals/letters.py
combinat/free_module.py
combinat/root_system/cartan_type.py
combinat/root_system/root_system.py
combinat/root_system/type_dual.py
combinat/root_system/type_relabel.py
combinat/root_system/weyl_group.py
combinat/sf/sf.py
groups/matrix_gps/general_linear.py
groups/matrix_gps/special_linear.py
groups/perm_gps/permgroup_named.py
misc/classcall_metaclass.py
misc/constant_function.py
misc/nested_class_test.py
sets/disjoint_union_enumerated_sets.py
sets/finite_enumerated_set.py
sets/non_negative_integers.py
sets/primes.py
structure/all.py
structure/dynamic_class.py
structure/unique_representation.py
```



---

Comment by zimmerma created at 2010-02-08 11:54:48

I tried the patch and sage -t * and got the same failures that I get without the patch
(on x86_64 Fedora12, see #7773). Thus a positive review for me.


---

Comment by hivert created at 2010-02-08 12:43:59

Replying to [comment:6 zimmerma]:
> I tried the patch and sage -t * and got the same failures that I get without the patch
> (on x86_64 Fedora12, see #7773). Thus a positive review for me.

So are you waiting for another review ? Or did you simply forgot to check the relevant box ?


---

Comment by hivert created at 2010-02-08 12:43:59

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-02-08 12:53:59

> So are you waiting for another review ?

no, I was waiting for the "needs review" status.


---

Comment by zimmerma created at 2010-02-08 12:53:59

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-02-08 13:34:33

Remove assignee hivert.


---

Comment by nthiery created at 2010-02-08 13:34:33

Just one thing Florent: please fix the following doctest:

```
sage: hash(x) # random 
True
```

so that the reader expects some integer result.

Maybe some test like:

```
sage: type(hash(x))
int
```

could be added.


---

Comment by hivert created at 2010-02-08 16:16:55

Changing status from positive_review to needs_work.


---

Comment by hivert created at 2010-02-08 16:16:55

Replying to [comment:9 nthiery]:
> 
> Just one thing Florent: please fix the following doctest:
> {{{
> sage: hash(x) # random 
> True
> }}}
> so that the reader expects some integer result.
> 
> Maybe some test like:
> {{{
> sage: type(hash(x))
> int
> }}}
> could be added.

Oups !!! I'm resubmitting a patch with the following diff:

```
diff --git a/sage/structure/unique_representation.py b/sage/structure/unique_represent
ation.py
--- a/sage/structure/unique_representation.py
+++ b/sage/structure/unique_representation.py
@@ -483,7 +483,9 @@ class UniqueRepresentation:
             sage: x = UniqueRepresentation()
             sage: y = UniqueRepresentation()
             sage: hash(x) # random
-            True
+            74153040
+            sage: type(hash(x))
+            <type 'int'>
             sage: hash(x) == hash(y)
             True
             sage: class bla(UniqueRepresentation, SageObject): pass
```


Please re-review...

Florent


---

Attachment


---

Comment by zimmerma created at 2010-02-08 16:24:33

> Please re-review... 

will do it as soon as my current sage -t * finishes. In the meantime you can click on
"needs review", unless more work is needed.


---

Comment by hivert created at 2010-02-08 16:31:33

Replying to [comment:11 zimmerma]:
> > Please re-review... 
> 
> will do it as soon as my current sage -t * finishes. In the meantime you can click on
> "needs review", unless more work is needed.

Actually, the precise button I needed to hit was "Submit Changes" ;-)


---

Comment by hivert created at 2010-02-08 16:31:33

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-02-08 16:35:51

Nicolas (and also Paul), you didn't comment about the following thought:

However, since we are in `UniqueRepresentations` we could use `__classcall__` which knows the parameters that constructed the object to insert into the created object the hash value of those parameters in the same veins it insert some stuff needed for pickling/unpickling. Any comment about that ?

Anyway, whatever is decided, I suggest to keep it for a forthcomming ticket, since it can raise some backward compatibility issues...


---

Comment by nthiery created at 2010-02-08 16:49:51

Replying to [comment:13 hivert]:
> Nicolas (and also Paul), you didn't comment about the following thought:
> 
> However, since we are in `UniqueRepresentations` we could use `__classcall__` which knows the parameters that constructed the object to insert into the created object the hash value of those parameters in the same veins it insert some stuff needed for pickling/unpickling. Any comment about that ?

That sounds good. We should probably include the class of the object in the hash calculation.

> Anyway, whatever is decided, I suggest to keep it for a forthcomming ticket, since it can raise some backward compatibility issues...

Yup.


---

Comment by zimmerma created at 2010-02-09 07:09:04

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-02-09 07:09:04

I did try with the new patch, and it is ok. Thus a positive review.


---

Comment by mpatel created at 2010-02-10 14:24:13

The ticket number is missing from the commit string.  I've refreshed the patch I've applied to 4.3.3.alpha0.


---

Comment by mpatel created at 2010-02-11 14:48:12

Resolution: fixed


---

Comment by mpatel created at 2010-02-11 15:24:31

Oops!
