# Issue 4621: '2' not in QQbar -- canonical embedding of subfields

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2008-11-26 11:26:25

Assignee: tbd

CC:  @kliem slelievre

Keywords: canonical embedding subfield

Reported by Alex Raichev at http://groups.google.com/group/sage-support/browse_thread/thread/c11289d794299903


```
sage: F.<a>= NumberField(x^2-2)
sage: a^2
2
sage: a^2 in QQ
True
sage: a^2 in QQbar
False
sage: 2 in QQbar
True 
```

or more directly

```
sage: F(2) in QQbar
False
```


Perhaps related to this is

```
sage: F.<a>=NumberField(x^2-2)
sage: QQ.is_subring(F)
True
sage: F.is_subring(QQbar)
False 
```


Robert Bradshow comments that `F.is_subring(QQbar)` should be `False`, because `QQbar` has a canonical embedding into `CC`, but `F` has not.

So, from that point of view, it makes sense that `a^2` is in `F` but not in `QQbar`. However, `a^2` is equal to `2` after all, and hence is in a part of `F` that _does_ have a canonical embedding.

In other words, we have a field element x in F_1 such that there is in fact a subfield F_2 of F_1 with x in F_1. Moreover, we have a field F_3 such that F_2 has a canonical embedding into F_3, but F_1 has no canonical embedding.

Is it possible for Sage to detect that situation? 

Idea: Is there a _unique_ maximal subfield F_m of F_1 that has a canonical embedding into F_3? If there is, there could be a method `max_subfield_coercing_into(...)`. 

Then, in the original example, we probably have 

```
sage: F.max_subfield_coercing_into(QQbar)
Rational Field
```

and then `x in QQbar` would answer True, since 

```
sage: x in F_1.max_subfield_coercing_into(QQbar)
True
```


Sorry if that idea is not realistic.


---

Attachment

This issue is fixed. Followup about embedding into QQbar at #7960.


---

Comment by robertwb created at 2010-01-17 00:26:53

Changing status from new to needs_review.


---

Comment by wjp created at 2010-01-17 20:07:54

A side effect of this patch is the following because it now tries to explicitly convert its argument to QQ. Is that desirable?


```
sage: GF(7)(2) in QQbar
True
```


(Related 'in's:

```
sage: GF(7)(2) in ZZ
True
sage: GF(7)(2) in QQ
False
sage: GF(7)(2) in QQbar
True
```

)


---

Comment by wjp created at 2010-01-17 20:07:54

Changing status from needs_review to needs_info.


---

Comment by robertwb created at 2010-01-18 19:53:36

This exposes a separate but that == for QQbar is not symetric...


```
sage: GF(7)(2) == QQbar(2)
False
sage: QQbar(2) == GF(7)(2)
True # after the patch, BOOM before, should be False
```



---

Comment by robertwb created at 2010-01-18 20:32:31

Changing status from needs_info to needs_review.


---

Comment by robertwb created at 2010-01-18 20:32:31

See #7984 for a fix for QQbar cmp.


---

Comment by robertwb created at 2010-01-20 08:29:29

For this to return True, one would have to change the definition of canonical comparison--not something that should be done lightly.


---

Comment by robertwb created at 2010-01-20 08:29:29

Changing status from needs_review to needs_info.


---

Comment by mhansen created at 2011-12-17 20:45:24

Just a note -- this patch no longer works with #7984.


---

Comment by vdelecroix created at 2015-04-08 22:15:15

The reason why this fails is

```
sage: F.<a>= NumberField(x^2-2)
sage: two = F(2)
sage: QQbar(two)
Traceback (most recent call last):
...
TypeError: Illegal initializer for algebraic number
```

One way to fix it is to be more flexible on creation of algebraic number (in `AA._element_constructor_` or `QQbar._element_constructor_`) or to implement a method `_algebraic_` to number field elements.

Vincent


---

Comment by vdelecroix created at 2016-04-27 22:42:23

Replying to [comment:12 vdelecroix]:
> The reason why this fails is
> {{{
> sage: F.<a>= NumberField(x^2-2)
> sage: two = F(2)
> sage: QQbar(two)
> Traceback (most recent call last):
> ...
> TypeError: Illegal initializer for algebraic number
> }}}
> One way to fix it is to be more flexible on creation of algebraic number (in `AA._element_constructor_` or `QQbar._element_constructor_`) or to implement a method `_algebraic_` to number field elements.

the above is fixed in #14485 and #20400 but it does not solve the containment test!


---

Comment by slelievre created at 2021-03-27 16:29:15

To put it another way.

In Sage 9.3.rc0:

```
sage: root2 = QuadraticField(2).gen()
sage: root2 in QQbar, root2^2 in QQbar  # expected: (True, True)
(False, False)
```



---

Comment by vdelecroix created at 2021-03-27 16:51:14

Replying to [comment:16 slelievre]:
> To put it another way.
> 
> In Sage 9.3.rc0:
> {{{
> sage: root2 = QuadraticField(2).gen()
> sage: root2 in QQbar, root2^2 in QQbar  # expected: (True, True)
> (False, False)
> }}}

The embedding is not set by writing only `QuadraticField(2)` (see also [#30518 comment:10](https://trac.sagemath.org/ticket/30518#comment:10)). You can compare with

```
sage: root2 = QuadraticField(2, embedding=AA(2).sqrt()).gen()
sage: root2 in QQbar, root2^2 in QQbar
(True, True)
```

Though the following is definitely annoying

```
sage: QuadraticField(2).one() in QQbar  # would better be true
False
```



---

Comment by vdelecroix created at 2021-03-27 16:59:42

Note that it will quickly become annoying with extensions

```
sage: K.<a> = QuadraticField(2, embedding=AA(2).sqrt())
sage: x = polygen(ZZ)
sage: L.<b> = K.extension(x**3 - x**2 - x - 1) 
```


- Do you expect `QQbar(L(a))` to work?
- What should be the result of `L(a) in QQbar`?


---

Comment by vdelecroix created at 2021-03-27 17:07:05

Note also that `1 == 1` does not hold in the following situation

```
sage: QuadraticField(2).one() == QuadraticField(3).one()
True
```

Again, with properly set embeddings it compares as a user might expect

```
sage: K2 = QuadraticField(2, embedding=AA(2).sqrt())
sage: K3 = QuadraticField(3, embedding=AA(3).sqrt())
sage: K2.one() == K3.one()
True
```



---

Comment by vdelecroix created at 2021-03-27 17:14:05

The only way I can imagine a fix would be to implement intersection of parents as part of the coercion model. It would have at least the following requirements
- `C = A.intersection(B)` is a parent with injective coercions in both `A` and `B`
- `A.intersection(B)` is identical to `B.intersection(A)`

Given that, we could design a more reasonable `sage.structure.element.Element.__richcmp__`.


---

Comment by slelievre created at 2021-04-04 17:05:21

Thanks for launching a discussion on sage-devel:

- https://groups.google.com/g/sage-devel/c/7-C6cpUyJdI


---

Comment by mkoeppe created at 2021-04-07 19:29:15

Sage development has entered the release candidate phase for 9.3. Setting a new milestone for this ticket based on a cursory review.


---

Comment by mkoeppe created at 2021-07-19 00:44:56

Setting a new milestone for this ticket based on a cursory review.


---

Comment by mkoeppe created at 2021-12-18 19:53:12

Stalled in `needs_review` or `needs_info`; likely won't make it into Sage 9.5.
