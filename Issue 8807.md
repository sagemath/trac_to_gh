# Issue 8807: Adding support for morphisms to the category framework

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2010-04-28 18:17:42

Assignee: Simon King

CC:  kohel was wdj robertwb

Keywords: morphisms functors categories

Working on the doc tests for sage.category at #8800, I found that support for morphisms is missing in the category framework. I think this is important, and therefore I am opening this ticket.

Some thoughts on implementing support.

Let f be a morphism in a category C, and let F be a functor, F.domain()==C. Then F(f) should by default try F(f.domain()).hom(f,F(f.codomain())). This relies on the call method of F(f.domain()).Hom(F.codomain()), which in turn uses _coerce_impl. I think it is there where the support should be implemented.

Example:

In sage.rings.homset.RingHomset_generic_with_category._coerce_impl, one has

```
        ...
        if x.parent() == self:
            if isinstance(x, morphism.RingHomomorphism_im_gens):
                return morphism.RingHomomorphism_im_gens(self, x.im_gens())
            elif isinstance(x, morphism.RingHomomorphism_cover):
                return morphism.RingHomomorphism_cover(self)
        raise TypeError
```

Why not instead

```
        try:
            if isinstance(x, morphism.RingHomomorphism_im_gens):
                return morphism.RingHomomorphism_im_gens(self, x.im_gens())
            elif isinstance(x, morphism.RingHomomorphism_cover):
                return morphism.RingHomomorphism_cover(self)
        except:
            raise TypeError
```


If I do so, the following works:

```
sage: R.<x> = QQ[]
sage: f = R.hom([2*x],R)
sage: C = Fields()
sage: f2 = C(R).hom(f,C(R))
sage: f2
Ring endomorphism of Fraction Field of Univariate Polynomial Ring in x over Rational Field
  Defn: x |--> 2*x
sage: f2(1/x)
1/(2*x)
```


It should be straight forward to change the call method of ``C`` so that ``C(f)`` reproduces the above construction. Similarly, if ``F`` is a functor then ``F(f)`` should call ``F(f.domain()).hom(f,F(f.codomain()))``.


---

Comment by SimonKing created at 2010-04-30 13:58:22

Implementing induced homomorphisms; Functors on morphisms; some doc tests


---

Attachment

Fixing a buglet in the construction functor of Laurent Polynomial Rings. To be applied after the first patch


---

Attachment

Cc to the original authors.

I solved the problem. Please apply both patches in order.

*__New Code__*

I cleaned the framework for functors. There is a generic call method that (in contrast to the old generic call method) has a return value. It relies on three methods _coerce_into_domain, _apply_functor and _apply_functor_to_morphism. The default methods are already enough for forgetful functor and most construction functors.

I implemented a new class for Ring Homomorphisms that are induced by a homomorphism of the base ring. This enables the application of the construction functors for matrix and polynomial rings.

*__Tests__*

All new code is tested, and I added also some doc tests for old code. This is related with #8800. However, #8800 should not be closed, because the old code is still not completely covered by tests yet.

Suggestion: The further work on #8800 will build upon this ticket.

*__Showcases__*

We start with a homomorphism of polynomial rings.

```
sage: R.<x,y> = QQ[]
sage: S.<z> = QQ[]
sage: f = R.hom([2*z,3*z],S)
```


Now we construct polynomial rings based on ``R`` and ``S``, and let ``f`` act on the coefficients:

```
sage: PR.<t> = R[]
sage: PS = S['t']
sage: Pf = PR.hom(f,PS)
sage: Pf
Ring morphism:
  From: Univariate Polynomial Ring in t over Multivariate Polynomial Ring in x, y over Rational Field
  To:   Univariate Polynomial Ring in t over Univariate Polynomial Ring in z over Rational Field
  Defn: Induced from base ring by
        Ring morphism:
          From: Multivariate Polynomial Ring in x, y over Rational Field
          To:   Univariate Polynomial Ring in z over Rational Field
          Defn: x |--> 2*z
                y |--> 3*z
sage: p = (x - 4*y + 1/13)*t^2 + (1/2*x^2 - 1/3*y^2)*t + 2*y^2 + x
sage: Pf(p)
(-10*z + 1/13)*t^2 - z^2*t + 18*z^2 + 2*z
```


The construction of induced homomorphisms is recursive, and so we have:

```
sage: MPR = MatrixSpace(PR, 2)
sage: MPS = MatrixSpace(PS, 2)
sage: M = MPR([(- x + y)*t^2 + 58*t - 3*x^2 + x*y, (- 1/7*x*y - 1/40*x)*t^2 + (5*x^2 + y^2)*t + 2*y, (- 1/3*y + 1)*t^2 + 1/3*x*y + y^2 + 5/2*y + 1/4, (x + 6*y + 1)*t^2])
sage: MPf = MPR.hom(f,MPS); MPf
Ring morphism:
  From: Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in t over Multivariate Polynomial Ring in x, y over Rational Field
  To:   Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in t over Univariate Polynomial Ring in z over Rational Field
  Defn: Induced from base ring by
        Ring morphism:
          From: Univariate Polynomial Ring in t over Multivariate Polynomial Ring in x, y over Rational Field
          To:   Univariate Polynomial Ring in t over Univariate Polynomial Ring in z over Rational Field
          Defn: Induced from base ring by
                Ring morphism:
                  From: Multivariate Polynomial Ring in x, y over Rational Field
                  To:   Univariate Polynomial Ring in z over Rational Field
                  Defn: x |--> 2*z
                        y |--> 3*z
sage: MPf(M)
[                    z*t^2 + 58*t - 6*z^2 (-6/7*z^2 - 1/20*z)*t^2 + 29*z^2*t + 6*z]
[    (-z + 1)*t^2 + 11*z^2 + 15/2*z + 1/4                           (20*z + 1)*t^2]
```


And this can also be achieved using construction functors:

```
sage: from sage.categories.pushout import CompositConstructionFunctor
sage: F = CompositConstructionFunctor(QQ.construction()[0],ZZ['x'].construction()[0], QQ.construction()[0],ZZ['y'].construction()[0])
sage: R.<a,b> = QQ[]
sage: f = R.hom([a+b, a-b])
sage: F(f) # indirect doctest
Ring endomorphism of Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Fraction Field of Multivariate Polynomial Ring in a, b over Rational Field
  Defn: Induced from base ring by
        Ring endomorphism of Fraction Field of Univariate Polynomial Ring in x over Fraction Field of Multivariate Polynomial Ring in a, b over Rational Field
          Defn: Induced from base ring by
                Ring endomorphism of Univariate Polynomial Ring in x over Fraction Field of Multivariate Polynomial Ring in a, b over Rational Field
                  Defn: Induced from base ring by
                        Ring endomorphism of Fraction Field of Multivariate Polynomial Ring in a, b over Rational Field
                          Defn: a |--> a + b
                                b |--> a - b
```


With the second patch, Laurent polynomial rings work as well:

```
sage: P = LaurentPolynomialRing(QQ,'t')
sage: F = P.construction()[0]
sage: X.<t> = LaurentPolynomialRing(R)
sage: p = (a+b)*t^-1 + (a^2)*t + b
sage: F(f)(p)
(a^2 + 2*a*b + b^2)*t + a - b + 2*a*t^-1
```



---

Comment by SimonKing created at 2010-04-30 14:26:01

Changing status from new to needs_review.


---

Comment by was created at 2010-07-20 14:13:31

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-07-20 14:13:31

I applied this patch to sage-4.5, and ran "make ptestlong", and their are failures all over the place, e.g.,

```

wstein`@`sage:~/build/sage-4.5.alphastein1$ ./sage -t  -long devel/sage/sage/matrix/misc.pyx
sage -t -long "devel/sage/sage/matrix/misc.pyx"
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.5.alphastein1/devel/sage/sage/matrix/misc.pyx", line 67:
    sage: B = ((matrix(ZZ, 3,4, [1,2,3,-4,7,2,18,3,4,3,4,5])/3)%500).change_ring(ZZ)
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/wstein/build/sage-4.5.alphastein1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/wstein/build/sage-4.5.alphastein1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/wstein/build/sage-4.5.alphastein1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[2]>", line 1, in <module>
        B = ((matrix(ZZ, Integer(3),Integer(4), [Integer(1),Integer(2),Integer(3),-Integer(4),Integer(7),Integer(2),Integer(18),Integer(3),Inte
ger(4),Integer(3),Integer(4),Integer(5)])/Integer(3))%Integer(500)).change_ring(ZZ)###line 67:
    sage: B = ((matrix(ZZ, 3,4, [1,2,3,-4,7,2,18,3,4,3,4,5])/3)%500).change_ring(ZZ)
      File "element.pyx", line 1529, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:11992)
      File "coerce.pyx", line 765, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)
    TypeError: unsupported operand parent(s) for '/': 'Full MatrixSpace of 3 by 4 dense matrices over Integer Ring' and 'Integer Ring'
...
```



---

Comment by SimonKing created at 2010-07-20 19:40:26

Dear William,

thanks for looking at this! Indeed it has been a long time since I wrote it, so it is time to resume work, taking a fresh look at my own code. I think this will be my project for the rest of Sage Days 24!


---

Comment by SimonKing created at 2010-07-20 21:00:50

It seems that my patch crashed the coercion system. Funny coincidence that I held a tutorial on coercion today...

```
sage: cm = get_coercion_model()
sage: M = parent(matrix(ZZ, 3,4, [1,2,3,-4,7,2,18,3,4,3,4,5]))
sage: cm.explain(M,QQ)
Will try _r_action and _l_action
Unknown result parent.
```


Cheers,
Simon


---

Comment by SimonKing created at 2010-07-20 21:08:38

And there it is:

```
sage: M = parent(matrix(ZZ, 3,4, [1,2,3,-4,7,2,18,3,4,3,4,5]))
sage: mf = M.construction()[0]
sage: mf.domain()
Category of rings
sage: mf.codomain()
Category of rings
sage: M in Rings()
False
```


So, the problem is that I gave the matrix constructor got a wrong codomain, namely the category `Rings()` --- and my generic `__call__` method checks whether the output belongs to the intended category. What should be the right choice?

```
sage: M.categories()
[Category of modules over Integer Ring, Category of bimodules over Integer Ring on the left and Integer Ring on the right, Category of left modules over Integer Ring, Category of right modules over Integer Ring, Category of commutative additive groups, Category of commutative additive monoids, Category of commutative additive semigroups, Category of additive magmas, Category of sets, Category of sets with partial maps, Category of objects]
```

Since the construction functor can not know about the base ring, I guess `CommutativeAdditiveGroups()` would be the way to go.


---

Comment by SimonKing created at 2010-07-20 21:37:43

I went through the file and found that indeed in some cases wrong categories were chosen. I count this as an argument _pro_ my approach to have a generic `__call__` method, because this checks whether the result is in the expected category.

After doing the appropriate changes, I am running ptestlong as well.


---

Comment by SimonKing created at 2010-07-21 08:32:15

I produced a new patch (I hope I got the `hg -qfold` command right).

The problem was: 

 * Some construction functors used to be defined on the wrong categories. E.g., the `MatrixFunctor` was defined as a functor from Rings() to Rings(), which is of course wrong if the number of rows is different from the number of columns.
 * In the good old times, every functor had a custom `__call__` method. Therefore, it was not noticed that sometimes the return value did not belong to the expected category.
 * My default `__call__` method does check the output - and raises an error if it is wrong.
 * For some reason I forgot to run `sage -testall`

Solution:

 * Be more careful with defining domain and codomain of the construction functors.
 * Run `make ptestlong`. Result:
   {{{
All tests passed!
Total time for all tests: 4078.1 seconds
   }}}

One remark concerning doctests. The genuinely new code (induced morphisms) is doctested. In my patch, I however did not add tests for sage.categories.pushout. This is done in #8800. I hope that the ticket from #8800 still applies with the new patch that I posted here.


---

Comment by SimonKing created at 2010-07-21 08:32:15

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-07-21 08:43:04

Replying to [comment:7 SimonKing]:
> One remark concerning doctests. The genuinely new code (induced morphisms) is doctested. In my patch, I however did not add tests for sage.categories.pushout. This is done in #8800. I hope that the ticket from #8800 still applies with the new patch that I posted here.

Unfortunately, #8800 does not apply with the new patch from here. 

Suggestion: I'll rebase #8800 relative to the new patch here. So, #8807 would be reviewed first, and the next to review would be #8800, which contains many doctests. I hope this is acceptable.


---

Comment by cremona created at 2010-10-26 20:42:28

Review:

Just a few trivial comments, after which I could give this a positive review.  The patch applies fine to 4.6.rc0 (though the related one at #8800 does not then apply cleanly) and all tests pass.  There is no time regression (long tests took 667s before and 642s after, using -tp 20).

Here are the minor issues in docstrings:

line 44: "one should implement two methods" -- do you mean three?

_apply_functor_to_morphism: first line of docstring is a copy from the previous function but should presumably be "Apply the functor to a morphism between ... something" 

In the new `__call__` function, I would like to see a test of the branch which raises a `TypeError` ""%s is ill-defined, ..."

Is the spelling of "`CompositConstructionFunctor`" intentional?  Should it not be "`CompositeConstructionFunctor`"?


---

Comment by cremona created at 2010-10-26 20:42:28

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2010-10-26 22:31:31

Hi John!

Replying to [comment:9 cremona]:
> Review:
> 
> Just a few trivial comments, after which I could give this a positive review.  The patch applies fine to 4.6.rc0 (though the related one at #8800 does not then apply cleanly) and all tests pass.  There is no time regression (long tests took 667s before and 642s after, using -tp 20).

That's good news! As my patch only adds functionality, without changing the method resolution order of existing classes and without replacing existing algorithms, it is no surprise that the speed remains fine.

> Here are the minor issues in docstrings:
> 
> line 44: "one should implement two methods" -- do you mean three?

You know, there are three types of mathematicians: Some can count, and others can't.

But isn't it pythonesque? Recall the Holy Hand Grenade of Antioch from the movie "Monty Python and the Holy Grail"... :)

> _apply_functor_to_morphism: first line of docstring is a copy from the previous function but should presumably be "Apply the functor to a morphism between ... something" 

Right.

> In the new `__call__` function, I would like to see a test of the branch which raises a `TypeError` ""%s is ill-defined, ..."

OK, but I hope such example needs to be constructed on purpose. It used to happen with the matrix constructor, for example: The functor was supposed to take a ring R into the ring(!!) of m by n matrices over R. But if the matrix constructor does not produce square matrices, the result is of course not a ring. This bug existed before and is fixed in my patch (now, the functor's codomain is only expected to be the category of rings if m equals n). However, this is exactly the situation that is covered by the `TypeError`.

> Is the spelling of "`CompositConstructionFunctor`" intentional?  Should it not be "`CompositeConstructionFunctor`"?

This wasn't my idea. `CompositConstructionFunctor` existed earlier (see pushout.py).

As I mentioned on the other ticket, I will be unable to do any programming work at least until next week. But it should be one of the first things I'll do once I'm settled in Jena.

Best regards,

Simon


---

Comment by SimonKing created at 2010-11-24 07:51:58

Replying to [comment:9 cremona]:
> ...
> Here are the minor issues in docstrings:
> 
> line 44: "one should implement two methods" -- do you mean three?

Corrected.

> _apply_functor_to_morphism: first line of docstring is a copy from the previous function but should presumably be "Apply the functor to a morphism between ... something" 

Corrected.

> In the new `__call__` function, I would like to see a test of the branch which raises a `TypeError` ""%s is ill-defined, ..."

Done. I define a class that behaves like the matrix constructor used to.

> Is the spelling of "`CompositConstructionFunctor`" intentional?  Should it not be "`CompositeConstructionFunctor`"?

That spelling is old, so, I won't touch it.

I am running `sage -tp 3 sage` right now, but I am replacing the old patch in a minute.

Cheers,
Simon


---

Comment by SimonKing created at 2010-11-24 08:01:04

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-11-24 08:01:04

OK, patch is updated.

Please only apply `trac-8807_induced_morphisms.patch`.


---

Attachment

This patch applies to sage-4.6; it is the only patch to be applied


---

Comment by cremona created at 2010-11-24 09:22:26

Looks good, about to test with 4.6.1.alpha2.


---

Comment by cremona created at 2010-11-24 09:37:59

All tests pass -- but I forgot -long, so hold on...


---

Comment by cremona created at 2010-11-24 09:54:49

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-11-24 09:54:49

...all long tests pass!


---

Comment by cremona created at 2010-11-24 09:56:20

Changing status from positive_review to needs_work.


---

Comment by cremona created at 2010-11-24 09:56:20

Replying to [comment:15 cremona]:
> ...all long tests pass!
Sorry, I am a complete idiot.  I imported the patch and did sage -b but never qpushed it.  Back to square one.


---

Comment by cremona created at 2010-11-24 09:56:44

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-11-24 10:25:04

Third time lucky: I did apply the patch, and rebuild, and test the entire library with -long, and all tests pass.  (4.6.1.alpha2, 64-bit),


---

Comment by cremona created at 2010-11-24 10:25:04

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-11-24 13:58:30

Release manager: after merging this patch, please also do the one at #10318 which has a positive review and just does a lot of spelling corrections, mostly on the file which this one affects most.


---

Comment by SimonKing created at 2010-12-08 10:14:56

To the buildbot and the release manager:

Apply trac-8807_induced_morphisms.patch


---

Comment by jdemeyer created at 2011-01-12 06:31:57

Resolution: fixed
