# Issue 8095: is_primitive of WordMorphism is broken

Issue created by migration from https://trac.sagemath.org/ticket/8095

Original creator: slabbe

Original creation time: 2010-01-27 13:59:46

Assignee: slabbe

CC:  abmasse

Let us define the following morphism over 3 letters:

```
sage: substitution=WordMorphism('a->b,b->ac,c->a')
```

Then we get

```
sage: substitution.is_primitive()
False
```

but also

```
sage: (substitution^2).is_primitive()
True
```


------

expected behaviour:

See the description of ".is_primitive()":
Returns True if self is primitive.
A morphism ϕ is primitive if there exists an positive integer k such
that for all α∈Σ, ϕk(α) contains all the letters of Σ.

So, if a morphism is primitive, so are all its powers. And if there is
a power which is primitive, so is the morphism itself. In the example
above, both outputs should be "True".


---

Comment by slabbe created at 2010-01-27 15:22:25

I just posted a patch which solves the described problem. The solution uses the following algorithm:


```
ALGORITHM: 
 
   Let `m` be the incidence matrix of a endomorphism on a monoid  
   of `d` letters. The endomorphism is primitive if and only if 
   there exists `k` such that `1 \leq k \leq (d-1)^2+1` and `m^k`  
   contains no zero. 
```


Are we sure this is true? Is there a proof of that somewhere?


---

Comment by slabbe created at 2010-01-27 15:22:25

Changing status from new to needs_review.


---

Comment by slabbe created at 2010-01-28 16:41:20

Changing status from needs_review to needs_work.


---

Attachment

tested on sage-4.3.1


---

Comment by slabbe created at 2010-01-29 14:24:07

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2010-01-29 14:24:07

I found a reference for the above statement (Automatic sequences of Allouche and Shallit).


---

Comment by abmasse created at 2010-01-29 14:44:43

Tested on sage-4.3.1 as well and it works.
It fixes the reported problem as well.
All tests passed when running ``sage -t morphism.py".
Positive review.


---

Comment by abmasse created at 2010-01-29 14:44:43

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-30 23:41:54

Resolution: fixed
