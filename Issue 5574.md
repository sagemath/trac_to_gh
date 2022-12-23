# Issue 5574: taking symbolic powers should coerce objects to symbolic expressions

Issue created by migration from https://trac.sagemath.org/ticket/5574

Original creator: burcin

Original creation time: 2009-03-20 10:09:12

CC:  vdelecroix

Reported by Alex Raichev on sage-support:


```
sage: var('n',ns=1)
n
sage: (QQbar(2)^3)^n
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

<...>
<...>/sage/rings/qqbar.pyc in __pow__(self, e)
   2808             1
   2809         """
-> 2810         e = QQ._coerce_(e)
   2811         n = e.numerator()
   2812         d = e.denominator()

<...>/sage/structure/parent_old.so in 
sage.structure.parent_old.Parent._coerce_ (sage/structure
/parent_old.c:4031)()

<...>/site-packages/sage/structure/parent.so in 
sage.structure.parent.Parent.coerce (sage/structure/parent.c:4185)()

TypeError: no canonical coercion from New Symbolic Ring to Rational
Field
```


Since pynac supports using arbitrary Sage objects as numeric objects in symbolic expressions, we should return a symbolic expression as a result of the above commands.


---

Comment by burcin created at 2009-04-09 13:31:11

From sage-support `@`freenode today:


```
<base3___> raising a matrix to a variable power fails with 
NotImplementedError: non-integral exponents not supported,
even if i do assume(n, 'integer')
<base3___> am i missing something or should i file this as a bug?
<burcin> base3___, it's a bug
```



---

Comment by rws created at 2015-10-19 13:58:56

This is a general shortcoming of `AlgebraicNumber.__pow__()`:

```
sage: (QQbar(2)^3)^1.
...
TypeError: no canonical coercion from Real Field with 53 bits of precision to Rational Field
```



---

Comment by rws created at 2015-10-19 13:58:56

Changing component from symbolics to algebra.


---

Comment by vdelecroix created at 2018-01-08 11:14:03

Note that this is not a group action (because of the choice of an n-th root)

```
((-1)^(1/3))^2 != ((-1)^2)^(1/3).
```

Isn't that a requirement that `g.(h.x) = (gh).x` for an action in Sage?


---

Comment by jdemeyer created at 2018-01-08 11:30:09

Replying to [comment:10 vdelecroix]:
> Note that this is not a group action (because of the choice of an n-th root)
> {{{
> ((-1)<sup>(1/3))</sup>2 != ((-1)<sup>2)</sup>(1/3).
> }}}

So what? I don't plan to change any arithmetic, just the underlying implementation. Since we have an operation between 2 different parents (`QQbar` and `QQ`), an action is the right way to implement this.

> Isn't that a requirement that `g.(h.x) = (gh).x` for an action in Sage?

Why should there be such a requirement? I see an action purely as a technical way to implement a certain operation.


---

Comment by git created at 2018-01-08 13:27:11

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by jdemeyer created at 2018-01-08 13:29:56

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2018-01-09 09:46:16

Changing status from needs_review to needs_work.


---

Comment by git created at 2018-01-09 10:53:33

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by jdemeyer created at 2018-01-09 10:53:54

Changing status from needs_work to needs_review.


---

Comment by git created at 2018-01-18 10:11:31

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by jdemeyer created at 2018-01-18 10:12:19

Rebased to 8.2.beta3


---

Comment by jdemeyer created at 2018-01-18 10:14:32

This is a dependency for both #24256 and #24500, so it would be good to get this ticket done.


---

Comment by vdelecroix created at 2018-01-25 14:50:08

Is that complient with Sage documentation?

```
EXAMPLES in ``QQbar``::
...
EXAMPLES in ``AA``::
...
```

Why not

```
EXAMPLES:

powering in ``QQbar``::
...
powering in ``AA``::
...
```



---

Comment by vdelecroix created at 2018-01-25 14:54:17

Timings look like it will be a bit slower. Before

```
sage: a = AA(5)
sage: %timeit a^(1/3)
1000 loops, best of 3: 327 µs per loop
sage: a = AA(8)
sage: %timeit a^(1/3)
100000 loops, best of 3: 7.78 µs per loop
```

After

```
sage: a = AA(5)
sage: %timeit a^(1/3)
1000 loops, best of 3: 369 µs per loop
sage: a = AA(8)
sage: %timeit a^(1/3)
100000 loops, best of 3: 9.64 µs per loop
```



---

Comment by jdemeyer created at 2018-01-25 16:00:33

Timings should improve in #24500 but I obviously cannot promise that it will be as fast as before.


---

Comment by jdemeyer created at 2018-01-25 16:18:56

Replying to [comment:25 vdelecroix]:
> Is that complient with Sage documentation?
> {{{
> EXAMPLES in ``QQbar``::
> ...
> EXAMPLES in ``AA``::
> ...
> }}}

There are some cases like that already in Sage. I don't see the problem, but if you insist, then I will change it.


---

Comment by vdelecroix created at 2018-01-25 16:22:17

Replying to [comment:28 jdemeyer]:
> Replying to [comment:25 vdelecroix]:
> > Is that complient with Sage documentation?
> > {{{
> > EXAMPLES in ``QQbar``::
> > ...
> > EXAMPLES in ``AA``::
> > ...
> > }}}
> 
> There are some cases like that already in Sage. I don't see the problem, but if you insist, then I will change it.

My reference is http://doc.sagemath.org/html/en/developer/coding_basics.html#documentation-strings (and not the rest of Sage).


---

Comment by jdemeyer created at 2018-01-25 17:22:08

I don't see anything in the docs saying that an `EXAMPLES` block should start exactly with the line `EXAMPLES::`


---

Comment by jdemeyer created at 2018-01-25 17:23:00

This is different from Sphinx blocks like `.. WARNING::` because those are handled specially. But there is nothing special about `EXAMPLES`.


---

Comment by vdelecroix created at 2018-01-25 23:30:46

Replying to [comment:31 jdemeyer]:
> This is different from Sphinx blocks like `.. WARNING::` because those are handled specially. But there is nothing special about `EXAMPLES`.

`TESTS` is also handled specially (hided in the doc). And `EXAMPLES` might in the future (e.g. interactive execution in Jupyter).


---

Comment by jdemeyer created at 2018-01-26 08:47:10

Replying to [comment:32 vdelecroix]:
> And `EXAMPLES` might in the future (e.g. interactive execution in Jupyter).

That would be a bad idea. Executable commands should be limited to the `EXAMPLES` block.

And if some software really wants to treat `EXAMPLES` blocks specially, it should still recognize `EXAMPLES in ``QQbar``` as `EXAMPLES` block.

Anyway, if you really want me to change it, just say so.


---

Comment by vdelecroix created at 2018-01-26 09:03:40

Replying to [comment:33 jdemeyer]:
> Replying to [comment:32 vdelecroix]:
> > And `EXAMPLES` might in the future (e.g. interactive execution in Jupyter).
> 
> That would be a bad idea. Executable commands should be limited to the `EXAMPLES` block.
> 
> And if some software really wants to treat `EXAMPLES` blocks specially, it should still recognize `EXAMPLES in ``QQbar``` as `EXAMPLES` block.
> 
> Anyway, if you really want me to change it, just say so.

Please do.


---

Comment by git created at 2018-01-29 16:07:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2018-01-29 22:17:38

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2018-02-02 12:06:18

Resolution: fixed
