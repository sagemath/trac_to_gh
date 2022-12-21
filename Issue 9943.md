# Issue 9943: categories for polynomial rings

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-09-18 22:39:23

Assignee: nthiery

CC:  sage-combinat

Currently, they're always just commutative rings.


---

Attachment


---

Comment by robertwb created at 2010-09-18 22:41:54

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-09-19 21:00:26

Hi Robert!

I have been through the patch, and it sounds good! I won't have the time to actually test it before some time, so please anyone beat me to it!

Just one micro question: does PolynomialRing actually check that the ring is commutative?

Cheers


---

Attachment

I went ahead and moved the functionality to it's own category since we want the mathematical information at the category level.  Could someone look over these changes?


---

Comment by robertwb created at 2010-09-20 22:03:18

The first patch only concerned univarite polynomial rings, the logic is not all correct for multivariate polynomial rings (though on an orthogonal note, that could use some fixing up as well). It seems odd to have a category of univariate polynomial rings over a fixed basering, which is why I put the logic into the concrete object. I suppose the category should a be declared as a graded R-algebra as well (do we have join categories yet?). 

I don't know if PolynomialRing asserts its basering is commutative, but IIRC it's been assumed for a long time.


---

Comment by robertwb created at 2010-12-03 19:41:36

Apply only 9944-poly-cat.patch


---

Attachment


---

Comment by robertwb created at 2011-01-26 06:27:28

Apply 9944-poly-cat.patch and 9944-poly-cat-doctests.patch .


---

Attachment

I would give this a positive review for Robert's idea and I would open a new ticket for the multivariate rings. I'll just send a mail to Mike whether he is ok with that or no.


---

Comment by nthiery created at 2011-03-29 09:23:31

Replying to [comment:4 robertwb]:
> The first patch only concerned univarite polynomial rings, the logic is not all correct for multivariate polynomial rings (though on an orthogonal note, that could use some fixing up as well). It seems odd to have a category of univariate polynomial rings over a fixed basering, which is why I put the logic into the concrete object. I suppose the category should a be declared as a graded R-algebra as well (do we have join categories yet?). 

Sorry for the very late answer. In MuPAD, we had a category for
univariate polynomial rings: there are several possible
implementations of such, and it's natural to factor out the generic
code, together with the category inheritance logic, in a category.

And yes, we have join categories. See Category.join.

I let you see whether to create the UnivariatePolynomialRing category
in this ticket or in a later ticket.


---

Comment by SimonKing created at 2011-03-29 15:47:34

Replying to [comment:8 nthiery]:
> Sorry for the very late answer. In MuPAD, we had a category for
> univariate polynomial rings: there are several possible
> implementations of such, and it's natural to factor out the generic
> code, together with the category inheritance logic, in a category.

Aparently there is a doctest failure. I fixed it, but unfortunately it went into my patch submitted for #9138. Therefore, "needs work".

Question: Do we really want a category of polynomial rings? Or do we want that (1) polynomial rings use the category framework (that's the purpose of my patch for #9138) and (2) the category to which a given polynomial ring belongs is a bit narrower than simply "category of rings"? I hope it is the latter.

My suggestion is that I submit a small patch fixing the doctests. Please tell whether my patch for #9138 improves the multivariate case. Then, perhaps it would be possible to give Roberts patches (+ doctest fix) a positive review, so that we can focus on #9138.


---

Comment by SimonKing created at 2011-03-29 16:31:53

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-03-29 17:07:08

At #9138, Jason Bandlow reported a slow-down, that is at least partially caused by the patches here. Do you have any idea what could be the reason?


---

Comment by SimonKing created at 2011-03-30 06:23:00

Replying to [comment:9 SimonKing]:
> Aparently there is a doctest failure. I fixed it, but unfortunately it went into my patch submitted for #9138. Therefore, "needs work".

Strange: Although the patch bot did see that error in one run, I can not reproduce it (but I had to change that test in my patch for #9138, because it turns `QQ['x'].category()` into the join of the category of euclidean domains and commutative algebras over `QQ`.

The other issue, namely the performance loss, was studied on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e4af3f1705b76955).

Florent Hivert found that a long mro does not matter for Python, but it _does_ matter if the classes inherit from a cdef class. That is the case for most classes in Sage (inheriting from `SageObject`), so, we should address the problem of a long mro.

Eventually, that should be fixed in Cython (and I think Florent reported it upstream). But for now, it seems to me we should think of a work-around.

Would it be acceptable coding practice to explicitly state in a derived class (say, `MPolynomialRing_generic`), that frequently used methods such as base or base_ring are the same as `Parent.base` or `Parent.base_ring`? David Roe stated that it might be dangerous to do so, at least if `cpdef` methods are involved.


---

Comment by SimonKing created at 2011-03-30 09:53:50

Concerning performance loss:

It seems to me that part of the reason is the fact that with the patchse, `__init_extra__` is not executed when it should. Sometimes, the parent methods of a category provide a useful `__init_extra__`, for example the category of algebras.

I am not sure yet why that happens, but I think it would happen if `Parent.__init__` is called without providing the category: Namely, doing `self._init_category_(...)` alone will _not_ trigger the execution of `__init_extra__`.


---

Comment by SimonKing created at 2011-03-30 10:01:40

It seems I was right!

Namely, the whole ring stuff is (unfortunately) inherited from `ParentWithGens`, which inherits from `ParentWithBase`, which inherits from `parent_old.Parent`.

And `parent_old.Parent` inherits from "the one and only Parent" -- but forgets to call `Parent.__init__`!! Instead, it just does `self._init_category_(...)`.

I'll change it and see what happens.


---

Comment by SimonKing created at 2011-03-30 10:17:01

Very bad things happen. As soon as `parent.Parent.__init__` is called in `parent_old.Parent.__init__`, an infinite recursion occurs.


---

Comment by SimonKing created at 2011-03-30 11:25:25

Call Parent.__init__ during initialisation of a ring


---

Attachment

I attached a small patch to solve part of the problem of the missing parent initialisation: I call `Parent.__init__` and `ParentWithGens.__init__` explicitly, during initialisation of a ring. In that way, the `__init_extra__` methods are correctly picked up.

However, that does not solve the performance problem.

Question one: How can one come to speed?

Question two: Is my patch really trivial enough to be called a referee patch?

For the patchbot:

Apply 9944-poly-cat.patch 9944-poly-cat-doctests.patch trac-9944-poly-cat-review.patch trac9944_second_referee.patch


---

Comment by SimonKing created at 2011-03-30 13:10:18

Changing status from needs_work to needs_info.


---

Comment by SimonKing created at 2011-03-30 13:10:18

FWIW: The doc tests pass.

Here is another idea what the slow down may come from. It was pointed out by Nicolas that the mro from the polynomial ring to `Parent` does not become longer by initialising the category properly: The inheritance from category parent classes comes _after_ Python inheritance. However, when all the parent classes of all super categories must be searched, it takes considerably longer before an `AttributeError` can be raised.

A similar issue has been studied at #10467. It seems to be important that an attribute error is raised as quickly as possible. That becomes difficult, if 60 parent classes need to be searched, before one eventually finds that the requested attribute does not exist.

But probably that question is out of the scope of this ticket.

So, what shall one do? Give it a positive review and accept the deceleration, or wait until someone has a model for improved attribute access?


---

Comment by SimonKing created at 2011-03-30 13:22:22

Replying to [comment:17 SimonKing]:
> A similar issue has been studied at #10467. It seems to be important that an attribute error is raised as quickly as possible. That becomes difficult, if 60 parent classes need to be searched, before one eventually finds that the requested attribute does not exist.

No, that is not the problem here! I was inserting print statements into `getattr_from_other_class` in order to find out what attributes are actually requested from the category when doing arithmetic. It turned out that, during the first computation of `(2*x-1)^2+5`, some attributes are requested. But when one repeats that computation, `getattr_from_other_class` is _not_ involved.

But what else could be the reason?


---

Comment by SimonKing created at 2011-03-30 19:12:21

Perhaps it is a conversion map that is slower than necessary?

If you look at `sage.categories.algebras.Algebras.ParentMethods.__init_extra__`, you see that it tries to register a certain set morphism as a coercion from the base ring into the algebra (that obviously works only if the algebra is unital). 

But aparently a different coercion is used -- a slower coercion!

Namely, together with my patch from #9138:

```
sage: R.<x> = ZZ[]
sage: R.category() # the __init_extra__ was supposed to be used.
Join of Category of unique factorization domains and Category of commutative algebras over Integer Ring
sage: c = R.convert_map_from(R.base_ring())
sage: c
Polynomial base injection morphism:
  From: Integer Ring
  To:   Univariate Polynomial Ring in x over Integer Ring
```


That is not what `__init_extra__` attempted to register!

Let us compare:

```
sage: from sage.categories.morphism import SetMorphism
sage: H = R.base().Hom(R)
sage: f = SetMorphism(H,R.from_base_ring)
sage: timeit('c(100)',number=10^5)
100000 loops, best of 3: 8.13 Âµs per loop
sage: timeit('f(100)',number=10^5)
100000 loops, best of 3: 1.75 Âµs per loop
```


So, things could be considerably improved. Obvious questions: Will `from_base` always yield a faster approach than the base injection morphism? And can we enforce to use the faster coercion?

Aparently it is not so easy:

```
sage: AC = Algebras(ZZ).parent_class
sage: R._unset_coercions_used()
sage: AC.__init_extra__(R)
sage: R.convert_map_from(R.base_ring())
Polynomial base injection morphism:
  From: Integer Ring
  To:   Univariate Polynomial Ring in x over Integer Ring
sage: R._unset_coercions_used()
sage: f.register_as_coercion()
sage: R.convert_map_from(R.base_ring())
Polynomial base injection morphism:
  From: Integer Ring
  To:   Univariate Polynomial Ring in x over Integer Ring
```


Can you explain how to force the use of a particular map for coercion of the base ring?


---

Comment by SimonKing created at 2011-03-30 19:28:03

And aparently the univariate polynomial rings are special in their choice of a conversion from the base ring. Again with #9138

```
sage: R.<m> = ZZ[]
sage: R.convert_map_from(R.base_ring())
Polynomial base injection morphism:
  From: Integer Ring
  To:   Univariate Polynomial Ring in m over Integer Ring
sage: R.<x,y> = QQ['t'][]
sage: R.convert_map_from(R.base_ring())
Generic morphism:
  From: Univariate Polynomial Ring in t over Rational Field
  To:   Multivariate Polynomial Ring in x, y over Univariate Polynomial Ring in t over Rational Field
```



---

Comment by SimonKing created at 2011-03-31 05:45:41

I suggest to speed things up by modifying "Polynomial base injection morphism". Internally, it uses rather slow ways of creating a polynomial of degree zero. It is likely to be faster to do what `R.from_base` does: Take the One of the ring (if it exists!) and use its `_lmul_` method (if it has `_lmul_`).

I also understand why `Algebras(...).parent_class.__init_extra__(R)` has no effect on the choice of a conversion map from `R.base()` to `R`: It calls `R.one()` in order to create a better coercion map; but `R.one()` will, internally, construct a conversion from the base to `R`. At that point, the "better" coercion is not defined, and thus the usual conversion is created and cached.

In other words, `R.from_base` will only be used for conversion if `R` does _not_ obey the rules of the new coercion framework (e.g., if it has a custom `__call__`).

Since the polynomial base injection morphism is a specialised method, it should be possible to internally construct the One of R without invoking coercion. My plan is to combine it with [attachment:trac9944_second_referee.patch] and submit a patch that then certainly needs a reviewer.


---

Comment by SimonKing created at 2011-03-31 05:45:41

Changing status from needs_info to needs_work.


---

Comment by SimonKing created at 2011-03-31 11:15:01

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-03-31 11:15:01

Good news! Things are now _faster_ than without the patches!

I found that one can considerably improve the conversion of an element of the base ring into a polynomial ring. Some polynomial rings used a generic conversion map, some used a polynomial base injection map -- and both were slow.

My inspiration came from `Algebras.ParentMethods.__init_extra__`: If R is a polynomial ring, then multiplication of a scalar with `R.one()` often is a very fast method to convert the scalar into R.

Problems:

 * We should not assume that any ring has a unit (ok, polynomial rings over a unital ring have...).
 * Calling `R.one()` will usually trigger the creation of a generic conversion - hence, it would be difficult to register it as conversion.
 * Not all flavours of polynomial elements have a `_rmul_` (polynomial_element_generic has not).
 * Sometimes, other conversion maps are registered when one wants to register the polynomial base injection map.

So, I implemented `_rmul_` and `_lmul_` for polynomial_element_generic, try various ways (old and new coercion model) of creating a One bypassing conversion maps, and in one init method of polynomial rings I decided to re-initialise the conversion maps.

*__Timings__*

I tried to test as many cases (multi- versus univariate, `libSingular` and others, different base rings,...). Without all the patches, we have the following:

```
sage: R.<x> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 23.4 µs per loop
sage: R.<x> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 24.6 µs per loop
sage: R.<x> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 87.9 µs per loop
sage: R.<x> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 113 µs per loop
sage: R.<x,y> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 13 µs per loop
sage: R.<x,y> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 16.6 µs per loop
sage: R.<x,y> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 10.8 µs per loop
sage: R.<x,y> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 238 µs per loop
sage: R.<x,y> = Qp(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 511 µs per loop
sage: R.<x> = Qp(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 1.06 ms per loop
```


With the patches, I get

```
sage: R.<x> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 8.97 µs per loop
sage: R.<x> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 8.3 µs per loop
sage: R.<x> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 70.3 µs per loop
sage: R.<x> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 82.6 µs per loop
sage: R.<x,y> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 12.6 µs per loop
sage: R.<x,y> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 16.4 µs per loop
sage: R.<x,y> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 10.5 µs per loop
sage: R.<x,y> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 187 µs per loop
sage: R.<x,y> = Qp(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 503 µs per loop
sage: R.<x> = Qp(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 1.08 ms per loop
```


So, there is no significant slow down at all, but a considerable speed up in most cases.

I suppose it can now be reviewed. I understood that the Robert's patches essentially have a positive review, except for the slow-down. So, would it suffice if some of you test my patch?

Apply 9944-poly-cat.patch 9944-poly-cat-doctests.patch trac-9944-poly-cat-review.patch trac9944_polynomial_speedup.patch


---

Comment by mraum created at 2011-03-31 11:43:44

Wow, that is an amazingly good result! I will take my time to review this by next week. But if anybody is faster than me, feel free to go for it!


---

Comment by nthiery created at 2011-03-31 17:48:58

That's excellent indeed! Thanks!

Simon: I guess I'll focus on the reviewing of the other patches.

                              Nicolas


---

Comment by nthiery created at 2011-03-31 17:58:52

Replying to [comment:22 SimonKing]:
> Problems:
> 
>  * We should not assume that any ring has a unit (ok, polynomial rings over a unital ring have...).

Rings() assumes its objects to be unital. If we want to support
polynomials over non unital rings, then this should go through the use
of Rngs(). If we make sure the coercion morphism from the base ring is always declared by Algebras(), all we will have to do is to use some new category NonUnitalAlgebras() when the base ring is just in Rngs(). Bwt: having a PolynomialRings() (PolynomialRngs?) category would be a good way to factor out this logic.

But one thing at a time :-)

Cheers,
			Nicolas


---

Attachment


---

Comment by mraum created at 2011-04-01 00:38:58

I applied the second patch and exported the commit, so that Jeroen will have an easier life (http://groups.google.com/group/sage-devel/browse_thread/thread/f5a9c012f6299a9e).

The patchs are very good. I am waiting for the tests to finish, but I guess this will be through very soon.


---

Comment by mraum created at 2011-04-01 00:53:06

The speed up is significant and all tests pass. This gets a positive review.

Let me point out the following (that won't show up in many use case, but still might deserve some consideration later):

unpatched:

```
sage: R = PolynomialRing(ZZ, ['a' + str(n) for n in range(10000)])
sage: x = R.gen(0)
sage: timeit('(2*x - 1)^2 + 5', number = 10^4)
10000 loops, best of 3: 94.5 µs per loop
```


patched:

```
sage: R = PolynomialRing(ZZ, ['a' + str(n) for n in range(10000)])
sage: x = R.gen(0)
sage: timeit('(2*x - 1)^2 + 5', number = 10^4)
10000 loops, best of 3: 131 µs per loop
```



---

Comment by mraum created at 2011-04-01 00:53:06

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-12 11:51:09

The PDF documentation doesn't build:

```
! Missing { inserted.
<to be read again>
                   $
l.358009 ...ment with the One by means of $_rmul_$
                                                  .
?
! Emergency stop.
<to be read again>
                   $
l.358009 ...ment with the One by means of $_rmul_$
                                                  .
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on reference.log.
make[1]: *** [reference.pdf] Error 1
```



---

Comment by jdemeyer created at 2011-04-12 11:51:09

Changing status from positive_review to needs_work.


---

Comment by SimonKing created at 2011-04-13 12:44:19

Changing status from needs_work to positive_review.


---

Comment by SimonKing created at 2011-04-13 12:44:19

It should now be fine. The problem was single back tick (Latex math mode) versus double back tick (verbose code).


---

Comment by SimonKing created at 2011-04-13 13:59:59

Changing status from positive_review to needs_work.


---

Comment by SimonKing created at 2011-04-13 13:59:59

Sorry, I changed but one instance of single back tick versus double back tick. But there are more left. So, needs work, for now.


---

Comment by SimonKing created at 2011-04-13 14:12:55

Speedup of polynomial arithmetic by improved base ring conversion


---

Comment by SimonKing created at 2011-04-13 14:14:03

Changing status from needs_work to positive_review.


---

Attachment

Now it seems solved. `sage -docbuild all html` did not complain!

Apply 9944-poly-cat.patch 9944-poly-cat-doctests.patch trac-9944-poly-cat-review.patch trac9944_polynomial_speedup.patch


---

Comment by jdemeyer created at 2011-04-13 19:45:23

Resolution: fixed


---

Comment by jdemeyer created at 2011-05-05 20:50:53

For some obscure reason, this breaks the following test on 32-bit systems:

```
sage -t "devel/sage-main/sage/modular/abvar/morphism.py"
```


The problem is that the following command hangs forever:

```
sage: J = J1(12345)
sage: J.hecke_operator(997)
```


Interestingly, interrupting at this point makes the command return the *correct output* without raising a `KeyboardInterrupt` which is a bug within the bug.


---

Comment by jdemeyer created at 2011-05-05 20:50:53

Changing status from closed to new.


---

Comment by jdemeyer created at 2011-05-05 20:50:53

Resolution changed from fixed to 


---

Comment by SimonKing created at 2011-05-05 21:15:50

Replying to [comment:34 jdemeyer]:
> For some obscure reason, this breaks the following test on 32-bit systems:
> The problem is that the following command hangs forever:
> {{{
> sage: J = J1(12345)
> sage: J.hecke_operator(997)
> }}}

Interesting. If I remember correctly, I had problems with that exact doctest on my machine and was able to solve it. But my machine is 64 bit.

So, I'll try with a 32 bit installation on bsd.math.


---

Comment by SimonKing created at 2011-05-05 21:24:21

I get a different error on bsd.math in 32bit mode:

```
sage: J = J1(12345)
sage: J.hecke_operator(997)
python(6506) malloc: *** mmap(size=1870024854642688) failed (error code=12)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
python(6506) malloc: *** mmap(size=1870024854642688) failed (error code=12)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
Hecke operator T_997 on Abelian variety J1(12345) of dimension 5405473
```


So, it reports problem with memory allocation, but in almost no time it still returns the correct answer!


---

Comment by SimonKing created at 2011-05-06 07:19:06

I think I remember what turned out to be the problem: In `J.hecke_operator(...)`, some matrix space is created - a very big one (kind of 5405473x5405473). And if I am not mistaken, the changes in the patch make the matrix space create a zero and a unit matrix - perhaps too much for 32 bit.

But perhaps I _am_ mistaken. After all, the memory consumption is not big at all when I do the computation on my computer.


---

Comment by jdemeyer created at 2011-05-06 07:27:57

Replying to [comment:36 SimonKing]:
> So, it reports problem with memory allocation, but in almost no time it still returns the correct answer!

The fact that errors (including interrupts) are ignored in this code is very bad in itself, I think there must be some `except:` catching all this.


---

Comment by SimonKing created at 2011-05-06 07:54:05

Using `trace`, it seems to me that the error occurs in line 245 of `sage/matrix/matrix_space.py`:

```
if nrows >= 2**63 or ncols >= 2**63:
```


Is computing `2**63` (with Python ints) a problem on 32 bit?? Apparently not:

```
sage: int(2)**int(63)
9223372036854775808L
```


So, the problem isn't solved, yet.


---

Comment by SimonKing created at 2011-05-06 07:57:34

Sorry, I had misinterpreted something.


---

Comment by SimonKing created at 2011-05-06 07:59:24

But there is something else:

```
sage: sage.misc.misc.is_64_bit
True
sage: os.environ['SAGE64']
'no'
```


Could that be the problem?


---

Comment by SimonKing created at 2011-05-06 08:41:58

It seems that trace does not show the whole story. I see that some memory errors are raise (when it is attempted to create huge zero or unit matrices), but I don't see where they are caught. So, there seems Cython code involved that is invisible to trace.


---

Comment by SimonKing created at 2011-05-06 13:20:36

I think I found it!

The problem occurs during initialisation of `sage.modular.abvar.homspace.EndomorphismSubring`. It is first initialised as a homset with a specific category `cat` that does not belong to the category of rings, and then as a ring. The second initialisation tries to put it into the category of rings, which seems to be a bad idea after the first initialisation.

Solution:

Form the join of `cat` with the category of rings. Initialise it as a ring with that join category (which became possible with #9944!). Eventually, initialise it as a homspace, with the same category.

With that little magic, the error seems to disappear. But now I need to do tests.

Cheers,

Simon


---

Attachment

Fix a problem with initialisation of endomorphism rings of abelian varieties on 32 bit


---

Comment by SimonKing created at 2011-05-06 13:49:07

The problem seems solved.

What I did: Initialise the endomorphism ring first as a ring, and provide it with the intended category. Then initialise it as a homset as well. That solves the problem in the sense that it disappears.

Admittedly I can not explain how exactly the problem has originally emerged. But I guess it makes sense that it is a problem if a homset gives itself a certain category and then sage.rings.ring.Ring tries to work with another category.

With the new patch, we have (also as an additional doc test)

```
sage: J = J1(12345)
sage: J.endomorphism_ring()
Endomorphism ring of Abelian variety J1(12345) of dimension 5405473
```

both on my machine (x86_64 Linux) and on bsd.math in a 32 bit installation. Moreover, on both machines, the tests in sage.modular pass.

Needs review, I guess.

Apply 9944-poly-cat.patch 9944-poly-cat-doctests.patch trac-9944-poly-cat-review.patch trac9944_polynomial_speedup.patch trac9944_abvar_endomorphism.patch


---

Comment by SimonKing created at 2011-05-06 13:49:07

Changing status from new to needs_review.


---

Comment by SimonKing created at 2011-05-06 15:41:11

FWIW: The long doctests pass on bsd.math in 32bit installation.


---

Comment by jdemeyer created at 2011-05-07 18:46:05

The patch at #11310 solves the "exceptions are ignored" problem.


---

Comment by jdemeyer created at 2011-05-08 10:10:06

There is a huge performance regression in creating iterated polynomial rings:

BEFORE:

```
sage: S = GF(9,'a')
sage: %time for n in range(11): S = PolynomialRing(S,'w')
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
```


AFTER:

```
sage: S = GF(9,'a')
sage: %time for n in range(11): S = PolynomialRing(S,'w')
CPU times: user 53.38 s, sys: 0.19 s, total: 53.57 s
Wall time: 53.58 s
```



---

Comment by jdemeyer created at 2011-05-08 10:10:06

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-05-08 11:20:28

Replying to [comment:47 jdemeyer]:
> There is a huge performance regression in creating iterated polynomial rings:
> ...
> sage: %time for n in range(11): S = PolynomialRing(S,'w')

Note that the whole point of this ticket is to do more things during initialisation of polynomial rings. So, no surprise that initialisation becomes a lot slower. However, I agree that it should not be _that_ slow.


---

Comment by SimonKing created at 2011-05-08 11:23:18

Strange. With the patches, I get

```
sage: S = GF(9,'a')
sage: %time for n in range(5): S = PolynomialRing(S,'w')
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
```

So, that's quick. Continuing:

```
sage: %time S = PolynomialRing(S,'w')
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: %time S = PolynomialRing(S,'w')
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: %time S = PolynomialRing(S,'w')
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: %time S = PolynomialRing(S,'w')
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: %time S = PolynomialRing(S,'w')
CPU times: user 8.38 s, sys: 0.00 s, total: 8.38 s
Wall time: 8.38 s
```


So, suddenly there is a jump in the initialisation time.


---

Comment by SimonKing created at 2011-05-08 11:28:22

Sorry, my fault. I did not restart before doing the test above, so, rings were found in the cache.

After restart with all patches, I get

```
sage: S = GF(9,'a')
sage: %time S = PolynomialRing(S,'w')
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.01 s
sage: %time S = PolynomialRing(S,'w')
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.01 s
sage: %time S = PolynomialRing(S,'w')
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.01 s
sage: %time S = PolynomialRing(S,'w')
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
sage: %time S = PolynomialRing(S,'w')
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.03 s
sage: %time S = PolynomialRing(S,'w')
CPU times: user 0.09 s, sys: 0.00 s, total: 0.09 s
Wall time: 0.10 s
sage: %time S = PolynomialRing(S,'w')
CPU times: user 0.22 s, sys: 0.00 s, total: 0.22 s
Wall time: 0.22 s
sage: %time S = PolynomialRing(S,'w')
CPU times: user 0.70 s, sys: 0.00 s, total: 0.70 s
Wall time: 0.70 s
sage: %time S = PolynomialRing(S,'w')
CPU times: user 2.58 s, sys: 0.00 s, total: 2.58 s
Wall time: 2.58 s
```


I found that the problem comes up with [attachment:trac9944-polynomial_speedup.patch]. So, let's work on it.


---

Comment by SimonKing created at 2011-05-08 11:42:45

Using prun, I found for one case:

```
   Ordered by: internal time
 
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.141    0.141    0.238    0.238 polynomial_ring.py:178(__init__)
     1414    0.055    0.000    0.071    0.000 polynomial_ring.py:234(_element_constructor_)
    11104    0.020    0.000    0.020    0.000 polynomial_ring.py:1821(modulus)
     1420    0.005    0.000    0.005    0.000 finite_field_givaro.py:153(degree)
...
```


In other words: In order to construct just _one_ polynomial ring over an iterated polynomial ring, the element constructor is called 1414 times and the modulus method 11104 times. At a different ticket, I suggested to turn the modulus method into a cached method. Perhaps that should already be done here. However, there should be no need to construct 1414 elements, just to initialise one ring!


---

Comment by SimonKing created at 2011-05-08 11:50:55

Interesting. Now it seems to me that the element constructor is in fact called from the `_repr_` method of `sage.rings.polynomial.polynomial_element.Polynomial_generic_dense`. That sound like using the string representation of elements in order to convert something.


---

Comment by SimonKing created at 2011-05-08 14:44:10

I think I somehow located the problem. I created recursively a univariate polynomial ring, as in your example, with a total of 8 variables:

```
sage: S
Univariate Polynomial Ring in w over Univariate Polynomial Ring in w over Univariate Polynomial Ring in w over Univariate Polynomial Ring in w over Univariate Polynomial Ring in w over Univariate Polynomial Ring in w over Univariate Polynomial Ring in w over Univariate Polynomial Ring in w over Finite Field in a of size 3^2
```


Then, with the patches

```
sage: timeit("S(0)")
5 loops, best of 3: 83 ms per loop
```

but without the patches

```
sage: timeit("S(0)")
625 loops, best of 3: 121 µs per loop
```


Since the above relies on coercion maps, which are compositions of polynomial base injection maps, and since my patch touched the polynomial base injection maps, it is conceivable that we'll find the problem there.

Note, however, that it might be a better solution to let the composition of two polynomial base injection maps be another polynomial base injection map -- that ought to be a lot faster than a composite map.


---

Comment by SimonKing created at 2011-05-09 07:43:20

The original implementation of a polynomial basering injection relies on a method `_new_constant_poly`, which turns out to be rather slow in most cases except the case of dense univariate polynomials -- they have a custom version of `_new_constant_poly`, while the others rely on a generic implementation.

So, instead of my former suggestion ("use `one._rmul_(x)` to coerce x into P with `one = P.one_element()`), it may be better to provide the other polynomial classes with a faster implementation of `_new_constant_poly`. That's what I am trying now.


---

Comment by SimonKing created at 2011-05-09 09:54:27

Or, even better: Implement `_new_constant_poly` not (only) for the _elements_ of a polynomial ring, but for the ring itself - that should be more natural, provided that there is only one possible polynomial class.


---

Comment by SimonKing created at 2011-05-12 06:42:05

I am totally frustrated.

I made some improvements to `_new_constant_poly`, whose purpose is to provide the quickest way in the given implementation to construct a constant polynomial, and made some other changes that should improve the coercions. There were improvements in all examples above.

However, I am now getting tons of failures and even segfaults in sage/schemes.

I tracked one type of error down, I thought. But apparently I only covered one special case of that one type of error.

While I was at it, I fixed the documentation for `hyperelliptic_padic_field`, which is not yet included into the manual, and which had syntax errors in all doc strings.


---

Comment by SimonKing created at 2011-05-12 06:45:32

Replying to [comment:56 SimonKing]:
> While I was at it, I fixed the documentation for `hyperelliptic_padic_field`, which is not yet included into the manual, and which had syntax errors in all doc strings.

Or perhaps the inclusion of sage/schemes into the manual should be on a different ticket, since most files are missing.


---

Comment by SimonKing created at 2011-05-13 05:49:18

Replying to [comment:56 SimonKing]:
> I am totally frustrated.

Still the case, although I am already down to 251 doctest failures and one timeout. That's the disadvantage of doing changes in coercion.


---

Comment by SimonKing created at 2011-05-13 15:44:45

Finally I got my new patch to work. Here are the new features and, in particular, the new timings. I think it was worth the effort!

__Polynomial Construction Functors__


```
sage: R.<x> = PolynomialRing(GF(5), sparse=True)
sage: F,B = R.construction()
sage: F(B) is R
True   # was False
```


__zero_element__

In various places, constructions such as self.parent()(0) are used. It should be more efficient to have self.parent().zero_element() instead, in particular if this is cached using the improved cached methods from #11115.

That means I had to introduce zero_element() for various classes, mostly in sage/modular.

__Fix zero element of free module homomorphisms__

The following used to fail with an error:

```
sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ)
sage: V.Hom(V).zero()
Free module morphism defined by the matrix
[0 0 0]
[0 0 0]
[0 0 0]
Domain: Free module of degree 3 and rank 3 over Integer Ring
Echelon ...
Codomain: Free module of degree 3 and rank 3 over Integer Ring
Echelon ...
```


__Calling any parent with None should return zero__

This used to be true for finite prime fields, but failed with an error
for finite non-prime fields:

```
sage: GF(5)(None)
0
sage: GF(5^2,'a')(None)
0
```


__Implement/improve `_new_constant_poly` for various polynomial classes__

This is the main reason why the timings stated below have improved. I thought that `_new_constant_poly` should be a method of a polynomial ring, but I think it should better stay as a method of polynomials: Polynomials are often implemented in Cython, but polynomial rings in Python.

In order to get a little bit of more speed, I introduce another parameter to `_new_constant_poly`, namely the parent in which the new polynomial is supposed to be created. This is because often the parent `P` of a polynomial `self` is already known when calling `self._new_constant_poly(a, P)`, so that it would be a waste of time to call `self.parent()` internally to determine the parent.

__Improve Polynomial Base Injection Morphisms and use it for coercion__

Conversion into a polynomial ring P from its base ring occurs frequently and should be as quick as possible.

I had already improved the performance in the old patch version. However, it turned out to be better to use `_new_constant_poly`, rather than always using multiplication with `P.one()`.

The rule is now: If `P.an_element()` has a `_new_constant_poly` method then it is used. Otherwise, if one can construct a one element in `P` without calling coercion, and if it has `_rmul_` and if `_rmul_` does not return `None` then it is used. Otherwise, `P._element_constructor_` is used.

Polynomial base injection morphisms are now always registered as coercion.

__Call method for compiled polynomials__

The documentation for compiled polynomials states that it can be called, although the cdef method `.eval(...)` has less overhead. That was not true, there has been no `__call__` method. I added one.

__Constant polynomial section__

It was stated that it uses the `constant_coefficient` method, which can be optimized for a particulare polynomial type. However, in fact a generic `constant_coefficient` method was *explicitly* called, even if a polynomial type did provide a more efficient method. That has now changed.

__Sparse versus dense versus differently implemented polynomial rings__

A univariate polynomial ring can be sparse or dense, and if it is dense and over `ZZ` (or also `QQ`) they can be implemented with `FLINT` or `NTL`. Dense and sparse rings used to be equal, but they were not identical - a violation to the unique parent assumption.

Moreover, in the multivariate case, the `implementation` and `sparse` arguments had no effect on the resulting ring, but were used in the cache key, yielding another violation of the unique parent assumption.

I resolved these violations. I was not sure whether one should silently ignore arguments that are not used, or should raise an error if they are provided. I decided to ignore `sparse` if it is not supported, and raise an error for dense or multivariate rings if an implementation is not supported.

We have, e.g.:

```
sage: S.<x,y> = PolynomialRing(ZZ,sparse=True)
sage: S is ZZ['x','y']
True  # used to be False
sage: R.<x> = PolynomialRing(ZZ,sparse=True,implementation='FLINT')
sage: S.<x> = PolynomialRing(ZZ,sparse=True,implementation='NTL')
sage: R is S
True  # used to be False
sage: R == ZZ['x']
False # used to be True
sage: S.<x,y> = PolynomialRing(ZZ, implementation='NTL')
Traceback (most recent call last):
...
ValueError: The NTL implementation is not known for multivariate polynomial rings
```


The last example used to return a ring that was equal but not identic to `ZZ['x','y']`!

Polynomial rings are now equal if and only if they are identical. Coercions exist from the non-default to the default version of a ring (hence, from sparse to dense, from NTL to FLINT.

```
sage: R.<x> = PolynomialRing(ZZ)
sage: S.<x> = PolynomialRing(ZZ, implementation='NTL')
sage: R == S
False
sage: R.has_coerce_map_from(S)
True
sage: S.has_coerce_map_from(R)
False
sage: S.<x> = PolynomialRing(ZZ, sparse=True)
sage: R == S
False
sage: R.has_coerce_map_from(S)
True
sage: S.has_coerce_map_from(R)
False
```


By consequence, the parent of a sum of polynomials is now unique - it used to depend on the summation order if dense and sparse summands were involved.

__Documentation and examples__

I think all changes are covered by doctests. Occasionally I fixed wrongly formatted docstrings.

__Performance__

Here are the new timings for the examples that we had discussed above. I use sage-4.7.alpha5 with the patches from this ticket applied, and I compare with timings that I had obtained with an unpatched version of sage-4.7.alpha5

There is no significant change in the startup time: I got `1.253` for sage.all in unpatched sage, but the margin of error seems rather wide.

```
$ sage -startuptime
...
## Slowest (including children)
1.100 sage.all (None)
0.279 sage.schemes.all (sage.all)
0.178 twisted.persisted.styles (sage.all)
0.164 elliptic_curves.all (sage.schemes.all)
0.162 ell_rational_field (elliptic_curves.all)
0.150 ell_number_field (ell_rational_field)
...
```


Here is the example brought up by Jeroen. There is now a drastic speedup were previously was a drastic slow down:

```
sage: S = GF(9,'a')
sage: %time for n in range(8): S = PolynomialRing(S,'w')
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.03 s
# unpatched: 0.04 s
sage: len(S.variable_names_recursive())
8
sage: timeit("S(0)")
625 loops, best of 3: 27.9 µs per loop
# with only the other patches: 83 ms
# unpatched: 121 µs
```


Here is the example brought up by Martin Raum:

```
sage: R = PolynomialRing(ZZ, ['a' + str(n) for n in range(10000)])
sage: x = R.gen(0)
sage: timeit('(2*x - 1)^2 + 5', number = 10^4)
10000 loops, best of 3: 58.2 µs per loop
# unpatched: 66.9 µs
```


Here are the arithmetic examples that I had provided earlier:

```
sage: R.<x> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 8.58 µs per loop
# unpatched: 23.6 µs
sage: R.<x> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 8.4 µs per loop
# unpatched: 25.8 µs
sage: R.<x> = GF(3)[]   # sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 66.4 µs per loop
# unpatched: 90.1 µs
sage: R.<x> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 75.4 µs per loop
# unpatched: 117 µs
sage: R.<x,y> = ZZ[]  # sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 7.85 µs per loop
# unpatched: 13.6 µs
sage: R.<x,y> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 7.33 µs per loop
# unpatched: 16.9 µs
sage: R.<x,y> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 6.59 µs per loop
# unpatched: 11.2 µs
sage: R.<x,y> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 158 µs per loop
# unpatched: 251 µs
sage: R.<x,y> = Qp(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 488 µs per loop
# unpatched: 521 µs
sage: R.<x> = Qp(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 894 µs per loop
# unpatched: 1.06 ms
sage: R.<x> = PolynomialRing(GF(9,'a'), sparse=True)
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 236 µs per loop
# unpatched: 265 µs
```


So, in *all* examples there is a noticeable speedup.

__Conclusion__

The new patch cleans coercion of polynomial rings, by enforcing uniqueness of parents.

It considerably improves the performance, even when comparing with the improvements that were introduced in the previous patches.

`sage -testall -long` passed. So, it is finally ready for review again.

Depends on sage-4.7

Apply Apply 9944-poly-cat.patch 9944-poly-cat-doctests.patch trac-9944-poly-cat-review.patch trac9944_polynomial_speedup.patch trac9944_abvar_endomorphism.patch trac9944_faster_and_cleaner_coercion.patch


---

Comment by SimonKing created at 2011-05-13 15:44:45

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-05-13 17:02:21

Replying to [comment:59 SimonKing]:
> ...
> __Improve Polynomial Base Injection Morphisms and use it for coercion__
> 
>...
> 
> The rule is now: If `P.an_element()` has a `_new_constant_poly` method then it is used. Otherwise, if one can construct a one element in `P` without calling coercion, and if it has `_rmul_` and if `_rmul_` does not return `None` then it is used. Otherwise, `P._element_constructor_` is used.

I stand corrected. The above rule did hold for an intermediate (unpublished) patch version. With the new patch, all polynomial classes have `_new_constant_poly`, and it will _always_ be used for basering injection.

Hence, there is a return statement after getting `_new_constant_poly`, and the subsequent lines of `sage.rings.polynomial.polynomial_element.PolynomialBaseInjection.__init__` will never be executed. I will remove them in the final patch version, but I first wait for input of a referee.


---

Comment by jdemeyer created at 2011-05-16 08:59:14

Please rebase the last patch to #11139.


---

Comment by jdemeyer created at 2011-05-16 08:59:14

Changing status from needs_review to needs_work.


---

Comment by mraum created at 2011-05-16 09:22:40

This should clearly be reviewed as quick as possible, since otherwise it will need frequent rebaseing. I just don't have the time to do it all, but if anybody was willing to share the effort, I could spend some time on this in the next two or three days.


---

Comment by mraum created at 2011-05-16 11:00:22

So far I read till sage/rings/polynomial/laurent_polynomial_ring.py in the order that the patch is printed. Only one issue here:
in free_module_homspace.py l.128 (new counting) a doctest is missing that checks that passing a function works fine.

Simon, if you rebase this, could you also upload a diff file for the new and old patch? That would make my and possibly the life of all others easier.

Martin

PS: I am still building 4.7, so I haven't run any tests yet.


---

Comment by SimonKing created at 2011-05-16 11:14:49

Replying to [comment:64 mraum]:
> So far I read till sage/rings/polynomial/laurent_polynomial_ring.py in the order that the patch is printed. Only one issue here:
> in free_module_homspace.py l.128 (new counting) a doctest is missing that checks that passing a function works fine.

It *is* tested. The patch has added the following test:

```

            sage: V = span([[1/2,1,1],[3/2,2,1],[0,0,1]],ZZ)
            sage: V.Hom(V).zero()
            Free module morphism defined by the matrix
            [0 0 0]
            [0 0 0]
            [0 0 0]
            Domain: Free module of degree 3 and rank 3 over Integer Ring
            Echelon ...
            Codomain: Free module of degree 3 and rank 3 over Integer Ring
            Echelon ...
```

In unpatched sage-4.7.alpha5, you would get

```
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (396, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (6924, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: 'function' object is not iterable
```


> Simon, if you rebase this, could you also upload a diff file for the new and old patch? That would make my and possibly the life of all others easier.

OK.


---

Comment by SimonKing created at 2011-05-16 11:22:16

Patch's up!

For the record: I started with sage-4.7.alpha5, then the first five patches from here, then from #11139, and finally the sixth patch from here.

I verified that the tests of sage.rings.ring pass, because that is what was modified, and sage.rings.ideal, because that is what the modification from #11139 is about.


---

Comment by SimonKing created at 2011-05-16 11:22:16

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-05-16 11:24:22

Replying to [comment:66 SimonKing]:
> Patch's up!

And diff file as well.


---

Comment by mraum created at 2011-05-16 19:42:30

With a freshly built 4.7 I get a reject in polynomial_element.pyx.  This only concerns the doctest for the BaseringInjection, so for the moment I leave it as it is and I run tests.


---

Comment by SimonKing created at 2011-05-17 21:01:01

Replying to [comment:68 mraum]:
> With a freshly built 4.7 I get a reject in polynomial_element.pyx.

Strange. I started with sage.4.7.alpha5, imported the patch from #11139 (it is only one, if I am not mistaken), and then the patches apply cleanly for me. Is there another merged ticket that interferes?


---

Comment by mraum created at 2011-05-17 21:57:08

For the record: I'm at sage/rings/polynomial/polynomial_zmod_flint.pxd

Simon, you are completely right about the doctest with span. Could we add #indirect doctest so that attention is drawn to this?

Some issues, that I encountered:
in polynomial_element.pxy new line 5352 : what about p-adics? I haven't had the time to check, but perhaps you can already say something about it.
in polynomial_element.pxy new line 6180ff : there are two returns that do not belong there

in polynomial_real_mpfr_dense.pxy new line 57: Do you mean [0]?
in polynomial_ring.py new line 468 : The coercing is the other way around.

Please don't forget to check the rejects that I've mentioned above. This could be a real problem for Jeroen.

So far, these are amazingly few issues for such a huge patch!

Hope to continue this by tomorrow (night).

Martin


---

Comment by mraum created at 2011-05-18 06:33:35

hg blame gives me that some changes were, for example, made to denominator. My last tags are 15689, so my version is the same as 4.7rc2.


---

Comment by SimonKing created at 2011-05-18 07:25:27

Replying to [comment:70 mraum]:
> Simon, you are completely right about the doctest with span. Could we add #indirect doctest so that attention is drawn to this?

OK, and perhaps I even add a comment like "The method zero() calls this hom space with a function, not with a matrix, and that case had previously not been taken care of".

> Some issues, that I encountered:
> in polynomial_element.pxy new line 5352 : what about p-adics? I haven't had the time to check, but perhaps you can already say something about it.

You mean the fact that I return `<Polynomial>self._parent(self[:n])` when it previously was `<Polynomial>self._parent(self[:n], check=False)`?

I tried to reconstruct what made me do that change. It now seems to me that it was not because of a bug but because I thought `self[:n]` would return a truncated list of coefficients, which apparently is not the case (at least not always).

Anyway. _If_ you feed a truncated list of coefficients into the element constructor of a univariate polynomial ring, and if you give `check=False`, then you could create a polynomial whose list of coefficients ends with a zero. That is a problem for non-padic polynomials, since `valuation()` and other methods will result in an error.

So, `if` there are polynomials p so that `p[:n]` returns the list of the first n coefficients, then `check=False` is a bug.

However, if `p[:n]` returns a polynomial that actually has the right parent, then the argument `check` will not be tested at all. So, `False` or `True` does not matter.

*Conclusion:* Removing `check=True` should have no influence on performance, but may fix a potential problem (depending on the behaviour of `p[:n]`).


In any case, it can not be a problem for padics, even _if_ `self[:n]` returns a list: I do not remove trailing zeroes from the coefficient list, but simply let the element constructor of `self._parent` decide what to do -- and the element constructor of padic and non-padic polynomial rings will do the right thing.

Here is a padic example:

```
sage: P.<x> = Zp(5)[]
sage: p = x^4
sage: p.truncate(3).valuation()
+Infinity
```

and that is because `p[:3].parent() is P`.

I just found that the existing test for the `truncate` method in `sage.rings.polynomial.polynomial_element` does _not_ test that method. Namely:

```
sage: R.<x> = ZZ[]; S.<y> = R[]
sage: f = y^3 + x*y -3*x
sage: from sage.misc.sageinspect import sage_getfile, sage_getsourcelines
sage: sage_getfile(f.truncate)
'/mnt/local/king/SAGE/sage-4.7.alpha5/devel/sage/sage/rings/polynomial/polynomial_element.pyx'
sage: sage_getsourcelines(f.truncate)[1]
6000
```


So, `f.truncate` is a different truncate method. I'll change that doctest by making S a sparse polynomial ring:

```
sage: R.<x> = ZZ[]; S.<y> = PolynomialRing(R, sparse=True)
sage: f = y^3 + x*y -3*x
sage: sage_getfile(f.truncate)
'/mnt/local/king/SAGE/sage-4.7.alpha5/devel/sage/sage/rings/polynomial/polynomial_element.pyx'
sage: sage_getsourcelines(f.truncate)[1]
5335
```


> in polynomial_element.pxy new line 6180ff : there are two returns that do not belong there

Yep. See post 60. I promised to remove the lines starting with the comment `# this is likely to be overridden below:` in the final patch version, but wanted to wait for input of a reviewer (thank you, reviewer!)

> in polynomial_real_mpfr_dense.pxy new line 57: Do you mean [0]?

Yes, and I'm changing it, although `i` works as well:

```
sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
sage: PolynomialRealDense(RR['x'],None)
0
```


> in polynomial_ring.py new line 468 : The coercing is the other way around.

Thank you!

> Please don't forget to check the rejects that I've mentioned above. This could be a real problem for Jeroen.

I'll try it, and will soon submit a new version of the last patch.


---

Comment by SimonKing created at 2011-05-18 07:41:40

Replying to [comment:71 mraum]:
> hg blame gives me that some changes were, for example, made to denominator. My last tags are 15689, so my version is the same as 4.7rc2.

I went through all patches that where merged since 4.7.alpha5 according to http://boxen.math.washington.edu/home/release/sage-4.7.rc2/tickets.html

I found no patch touching sage.rings.polynomial.polynomial_element.pyx, actually no patch that contains the word fragment "poly".

So, I am still puzzled. Perhaps the release manager can state what ticket (in addition to #11139) I have to take into account.


---

Comment by jdemeyer created at 2011-05-18 10:34:09

There shouldn't be any other patch to take into account (apart from #11139).  Could it be that you rebased to a non-clean sage-4.7.alpha5?

Actually, the best would be to rebase to [http://boxen.math.washington.edu/home/release/sage-4.7.1.alpha0/](http://boxen.math.washington.edu/home/release/sage-4.7.1.alpha0/).  It's not yet released, but it gives a good target for rebasing.


---

Comment by jdemeyer created at 2011-05-18 10:41:15

To be clear, I meant rebase to sage-4.7.1.alpha0 + #11139.


---

Comment by SimonKing created at 2011-05-18 12:22:08

Replying to [comment:74 jdemeyer]:
> There shouldn't be any other patch to take into account (apart from #11139).  Could it be that you rebased to a non-clean sage-4.7.alpha5?

I don't think so.

Anyway. I just finished the built of sage-4.7.rc2, and I found no problems at all with my patches. [attachment:trac9944_polynomial_speedup.patch] succeeded with a little fuzz, but there has been no rejection.

Therefore I just submitted a new version of [attachment:trac9944_faster_and_cleaner_coercion.patch] that addresses Martin's comments, but the other patches can stay as they are, IMHO.


---

Comment by SimonKing created at 2011-05-18 14:05:25

diff file for old and new patch version


---

Attachment

I also added the result of `diff trac9944_faster_and_cleaner_coercion.patch.orig trac9944_faster_and_cleaner_coercion.patch`, where `trac9944_faster_and_cleaner_coercion.patch.orig` is the patch version from before Mai 16, if that helps with the review.


---

Comment by mraum created at 2011-05-18 21:09:11

I'm done with reading. All tests (-long) passed, but with the latest version I want to try again. This might take some time.

I encountered only two further issues:
in polynomial_zz_pex.pyx new line 107f there is no specification of the except clause and I think raise TypeError ... is what belongs there. I know this is not your code, but it would be nice to fix this "on the fly". Can we have a doctest for this?

I don't understand the changes to qqbar.py. And also I have the feeling I saw this kind of change already. Have you, perhaps, confused this change? If not, could you say, why you made it?

There is still the issue with the rejects. Will you rebase to 4.7.1? In that case the problem might disappear. I will start compiling the latest version right now. So by tomorrow, if you could provide a rebased version and all tests pass, I can give this a positive review.
But already: Greate work!

Martin


---

Comment by SimonKing created at 2011-05-19 06:09:46

Replying to [comment:78 mraum]:
> I encountered only two further issues:
> in polynomial_zz_pex.pyx new line 107f there is no specification of the except clause and I think raise TypeError ... is what belongs there. I know this is not your code, but it would be nice to fix this "on the fly". Can we have a doctest for this?

I am trying. But probably you are right, it should probably be `except TypeError`.
 
> I don't understand the changes to qqbar.py. And also I have the feeling I saw this kind of change already. Have you, perhaps, confused this change? If not, could you say, why you made it?

That change only concerns a doctest involving the function `sage_input`. Its purpose is to give a construction to any given object. Apparently, the coercion changes led to a different but equivalent construction in one of the examples.

> There is still the issue with the rejects. 

Is there really? Meanwhile I got sage-4.7.rc2, and I did _not_ get any rejects for any of the patches. I merely got an "applied with fuzz", but that's not a reject. Are you sure that you started with a fresh sage-4.7.rc2, applied #11139, and then applied the 6 patches in order as listed in the ticket description, and only these? Please do not apply [attachment:trac9944_second_referee.patch], if that was the problem.

> Will you rebase to 4.7.1?

I don't see the need, since it does apply to 4.7.rc2, IMHO.

Cheers,
Simon


---

Comment by SimonKing created at 2011-05-19 06:19:09

Replying to [comment:79 SimonKing]:
> Replying to [comment:78 mraum]:
> > I encountered only two further issues:
> > in polynomial_zz_pex.pyx new line 107f there is no specification of the except clause and I think raise TypeError ... is what belongs there. I know this is not your code, but it would be nice to fix this "on the fly". Can we have a doctest for this?
> 
> I am trying. But probably you are right, it should probably be `except TypeError`.

I think I misunderstood your remark: You do not complain about the fact that there is a bare `except`, but you noticed that the TypeError is constructed but not raised. That's odd, of course.

I found the following example, in which the error should be raised:

```
sage: K.<a>=GF(next_prime(2**60)**3)
sage: R.<x> = PolynomialRing(K,implementation='NTL')
sage: R([3,'1234'])
3*x + 3
```

Hence, currently there is no error raised and the result is absolute nonsense.

I'll fix that.


---

Comment by SimonKing created at 2011-05-19 06:30:35

The bug in polynomial_zz_pex.pyx is fixed, and the fix is doctested.

But having done that, I wonder whether raising an error is really what we want in this example. After all, the semantics of `R(...)` is: "Make sense of the arguments, if possible at all - even if there is no coercion, there could still be a conversion."

So, here, `R([3,'1234'])` should perhaps better not result in an error but in `1234*x + 3`. What do you think?


---

Comment by mraum created at 2011-05-19 06:41:31

To me this sounds reasonable.

I have just made the changes to rebase to 4.7.1.alpha0. I think the point of Jeroen was that he will work with this version anyway and its only two tiny changes. Send your new patches, I will do the rebase and then I think Jeroen can imediatelly go for it (if he wants to).


---

Comment by SimonKing created at 2011-05-19 06:50:54

Replying to [comment:82 mraum]:
> To me this sounds reasonable.

What is "this"? Do you mean, raising an error is reasonable, or trying conversion rather than coercion is reasonable?


---

Comment by SimonKing created at 2011-05-19 08:38:00

I found another bug in polynomial_zz_pex.pyx:

```
sage: K.<a>=GF(next_prime(2**60)**3)
sage: R.<x> = PolynomialRing(K,implementation='NTL')
sage: R([3,x])
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1154, 0))
Traceback (most recent call last):
...
TypeError: polynomial() takes exactly one argument (0 given)
```


I suggest to not only catch an attribute error (namely when requesting `e.polynomial()`) but also a type error.

And my preference is to do try a conversion, before raising an error on a failing coercion. If that sounds reasonable to you then I'll submit an update of my patch.


---

Comment by mraum created at 2011-05-19 09:58:11

I would say this sounds indeed reasonable. No coercion was demanded for, so why to restrict to it. This was what you were talking about before, weren't you?


---

Comment by SimonKing created at 2011-05-19 10:45:27

Enforce uniqueness of parents for polynomial rings; further perfomance improvement for coercion


---

Attachment

With the new patch version, we have

```
sage: K.<a>=GF(next_prime(2**60)**3)
sage: R.<x> = PolynomialRing(K,implementation='NTL')
sage: R([3,'1234'])
1234*x + 3
sage: R([3,'12e34'])
Traceback (most recent call last):
...
TypeError: unable to convert '12e34' into the base ring
sage: R([3,x])
Traceback (most recent call last):
...
TypeError: unable to convert x into the base ring
```

So, a conversion is attempted, and the error message is mentioning conversion and not coercion.

The tests of polynomial_zz_pex.pyx pass. I didn't test the rest of Sage.


---

Attachment

Rebase to 4.7.1.alpha0


---

Comment by mraum created at 2011-05-19 12:43:51

Rebase to 4.7.1.alpha0


---

Attachment

I couldn't replace the patches so the rebased versions have new names. I will attach a diff file in a second (only line numbers changed).

Everything looks good to me now. I just want to run all tests one more time and then this can get a positive review.


---

Attachment


---

Attachment

Updating the apply statements.


---

Comment by SimonKing created at 2011-05-19 13:19:27

Hi Martin,

could it be that you had worked with an old version of [attachment:trac9944_polynomial_speedup.patch]?

There was a misspelling that I had introduced into the documentation of polynomial base injection maps, in the original version of that patch: It was

```
We use `_rmul_` and not `_lmul_` since...
```

where it should have been

```
We use ``_rmul_`` and not ``_lmul_`` since...
```


I had corrected that typo and updated the patch. But in your version [attachment:trac-9944-polynomial_speedup.patch], you still have the single back tick.

Anyway. If you apply my version or your version of the two patches, the result will be the same, namely two backticks around _rmul_ and _lmul_


---

Comment by SimonKing created at 2011-05-19 13:51:24

Replying to [comment:89 SimonKing]:
> Anyway. If you apply my version or your version of the two patches, the result will be the same, namely two backticks around _rmul_ and _lmul_

Or rather: The result will be in both cases that that text line will be completely removed.


---

Comment by mraum created at 2011-05-19 13:55:21

Ok, all tests still pass.


---

Comment by mraum created at 2011-05-19 13:55:21

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2011-05-22 18:25:14

By now, all patches have a positive review, so, I am changing the distinction of patches with or without positive review in the list of to-be-applied patches in the ticket description.


---

Comment by SimonKing created at 2011-05-23 18:46:19

Changing status from positive_review to needs_work.


---

Comment by SimonKing created at 2011-05-23 18:46:19

I hope it is OK that I modified one test in sage.rings.polynomial.polynomial_ring, by the new patch [attachment:trac9944_addendum.patch].

That test used to be

```
sage: QQ['y'] < QQ['x']
False
sage: QQ['y'] < QQ['z']
True
```


But that is unsafe, because this ticket removes the custom `__cmp__` method of polynomial rings. So, the comparison relies on virtually random data such as `id(QQ['x'])`, if I am not mistaken.

Therefore, it seems safer to me to replace it by

```
sage: QQ['y'] != QQ['x']
True
sage: QQ['y'] != QQ['z']
True
```



---

Comment by SimonKing created at 2011-05-23 18:46:40

Changing status from needs_work to needs_review.


---

Comment by mraum created at 2011-05-23 20:00:18

I'm not sure how happy the release manager is with changing tickets after positive review (except it is him who is doing it).
But I completely agree that this change makes sense. As expected, all tests pass, so I can change this back to positive review.


---

Comment by mraum created at 2011-05-23 20:00:18

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2011-05-23 21:02:49

Replying to [comment:96 mraum]:
> I'm not sure how happy the release manager is with changing tickets after positive review (except it is him who is doing it).

I reckon that it does not matter to the release manager, unless one re-opens a ticket that is already closed (but that has not been the case here).

> But I completely agree that this change makes sense. As expected, all tests pass, so I can change this back to positive review.

Thank you!


---

Comment by SimonKing created at 2011-05-24 06:55:34

I removed the comment "needs review" from the ticket description.


---

Comment by jdemeyer created at 2011-05-24 12:51:49

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-05-24 12:51:49

One minor issue: [attachment:trac9944_addendum.patch] needs a proper commit message.


---

Attachment

Making one doctest safer


---

Comment by SimonKing created at 2011-05-24 13:52:18

Done!


---

Comment by SimonKing created at 2011-05-24 13:52:18

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-05-31 09:50:01

Resolution: fixed
