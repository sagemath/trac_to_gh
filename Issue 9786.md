# Issue 9786: lagrange_polynomial(algorithm='divided_difference') fails over finite fields

Issue created by migration from https://trac.sagemath.org/ticket/9787

Original creator: mmezzarobba

Original creation time: 2010-08-23 13:09:53

Assignee: AlexGhitza

CC:  mmarco


```
sage: R.<x>=GF(101)[]
sage: R.lagrange_polynomial([[1,0],[2,0]])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/data/sage-4.5.1/<ipython console> in <module>()

/data/sage-4.5.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in lagrange_polynomial(self, points, algorithm, previous_row)
   1481             P = F[n-1]
   1482             for i in xrange(n-2, -1, -1):
-> 1483                 P *= (var - points[i][0])
   1484                 P += F[i]
   1485             return P

/data/sage-4.5.1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__imul__ (sage/structure/element.c:11631)()

/data/sage-4.5.1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)()

TypeError: unsupported operand parent(s) for '*': 'Rational Field' and 'Univariate Polynomial Ring in x over Finite Field of size 101'
sage: R.lagrange_polynomial([[1,0],[2,0]],'neville')
[0, 0]
```



---

Comment by mmezzarobba created at 2013-08-30 15:34:55

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2013-08-30 15:34:55

The issue does not exist anymore with sage-5.12β3.


---

Comment by chapoton created at 2013-09-22 18:34:14

In 5.12.beta5, the following still fails:

```
sage: R.<x>=GF(101)[]
sage: sage: R.lagrange_polynomial([[1,0],[2,0],[3,0]])
```



---

Comment by chapoton created at 2013-09-22 18:34:48

Changing status from needs_review to needs_work.


---

Comment by pbruin created at 2014-08-18 13:42:02

Here is a branch that should fix the bug.  The only changes to the code are a few extra coercions (and one conversion, for reasons explained in a comment) to make sure everything lives in the right parent.  A few doctests had to be fixed because they started with the wrong base ring (`QQ` vs. `RR`) for the given input and output.  The other changes are documentation improvements.


---

Comment by pbruin created at 2014-08-18 13:42:02

Changing status from needs_work to needs_review.


---

Comment by mmarco created at 2014-08-22 13:50:46

I would propose something like:


```
seqpoints = Sequence([self.base().an_element()]+list(points))
points = [seqpoints.universe()(p) for p in points]
```


That way we make sure that all the operations happen in the right parent (be it the base ring of the parent, or some other parent where both the input and the parent fit)


---

Comment by pbruin created at 2014-08-22 14:08:38

Replying to [comment:9 mmarco]:
> I would propose something like:
> 
> {{{
> seqpoints = Sequence([self.base().an_element()]+list(points))
> points = [seqpoints.universe()(p) for p in points]
> }}}
> 
> That way we make sure that all the operations happen in the right parent (be it the base ring of the parent, or some other parent where both the input and the parent fit)
Do you mean that `R.lagrange_polynomial()` should potentially return an element of a different ring than `R`?  That would be unnecessarily confusing in my opinion.


---

Comment by mmarco created at 2014-08-22 14:21:38

Well, you could have that even now:


```
sage: R.<x>=QQ[]
sage: R.lagrange_polynomial(((1,1.75),(2,0.2),(3,1.5)))
1.42500000000000*x^2 - 5.82500000000000*x + 6.15000000000000
```


You can either catch that and raise an exception (which is probably the mathematically strictly correct), or be more flexible and allow situations like the previous (which, i think, can be useful in several cases).

In this case, i would vote for the second option, but i understand it is a matter of opinion.


---

Comment by pbruin created at 2014-08-22 15:56:19

Replying to [comment:11 mmarco]:
> Well, you could have that even now:
> 
> {{{
> sage: R.<x>=QQ[]
> sage: R.lagrange_polynomial(((1,1.75),(2,0.2),(3,1.5)))
> 1.42500000000000*x^2 - 5.82500000000000*x + 6.15000000000000
> }}}
Actually, with this branch, you get

```
sage: R.<x>=QQ[]
sage: R.lagrange_polynomial(((1,1.75),(2,0.2),(3,1.5)))
57/40*x^2 - 233/40*x + 123/20
```

This is not ideal from my point of view (I would prefer to use `coerce` to put the coefficients into the base field of `R`, so this example would raise an error), but a doctest in a published book unfortunately depends on it.
> You can either catch that and raise an exception (which is probably the mathematically strictly correct), or be more flexible and allow situations like the previous (which, i think, can be useful in several cases).
I see that this could be the expected behaviour given the general permissiveness in Sage with respect to extending parents, but I would still find it strange if `R.lagrange_polynomial()` did not return a value in `R` but in a different ring depending on the input.  It would mean that `lagrange_polynomial()` basically had no relation to `R`.  If there were a standalone function `lagrange_polynomial()`, then it would be logical if `lagrange_polynomial()` returned a polynomial in a parent depending on the input, but the explicit presence of `R` in the notation `R.lagrange_polynomial()` does suggest to me that it should always return a polynomial in `R`.


---

Comment by mmarco created at 2014-08-24 13:32:20

Well, if it is clearly stated that the result should be in R, conversion should also be allowed, from my point of view. I can see solid arguments for any of the possible choices: coerce to R.basis(), convert to R.basis(), or extend for the common universe of R.basis() and the input. My personal choice would be the last one, but as long as it is clearly documented, i could live with any.

Another option would be to include a keyword (like 'extend', for example) to control the behaviour in this aspect. That way you can have a default functionality, but also another option for the user to choose. Although, it seems a bit overkill for this.


---

Comment by pbruin created at 2014-08-25 11:32:12

Replying to [comment:13 mmarco]:
> Well, if it is clearly stated that the result should be in R, conversion should also be allowed, from my point of view.
Fair point, I'll change that and improve the documentation.
> I can see solid arguments for any of the possible choices: coerce to R.basis(), convert to R.basis(), or extend for the common universe of R.basis() and the input. My personal choice would be the last one, but as long as it is clearly documented, i could live with any.
I still think that `R.lagrange_polynomial(...)` should return something in `R`.  In practice it should be easy to convert the input into the base ring, unless the user made this ring too small for some reason.  In that case the user can easily enlarge the base ring.
> Another option would be to include a keyword (like 'extend', for example) to control the behaviour in this aspect. That way you can have a default functionality, but also another option for the user to choose. Although, it seems a bit overkill for this.
This sounds like a reasonable option, but I do think it is a bit overkill, so someone who really wants it can implement it.


---

Comment by git created at 2014-08-25 11:39:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2015-04-18 12:26:23

Hello,

On sage-6.5 at least, I got the right answer.

```
sage: R.<x>=GF(101)[]
sage: R.lagrange_polynomial([[1,0],[2,0]])
0
```

It would be cool to add it to the documentation since it was the initial purpose of the ticket.

Vincent


---

Comment by git created at 2015-04-20 08:24:28

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2015-04-20 08:25:39

Replying to [comment:16 vdelecroix]:
> On sage-6.5 at least, I got the right answer.
> {{{
> sage: R.<x>=GF(101)[]
> sage: R.lagrange_polynomial([[1,0],[2,0]])
> 0
> }}}
This one was fixed at some point (see comment:2), but I added a doctest anyway.


---

Comment by vdelecroix created at 2015-04-20 09:20:03

Hello,

Looks good! Concerning the [comment:12 comment:12], where is this example in the sage book (I was not able to find it)? Should it be added to the documentation as an example with a warning?

Vincent

PS: Note that using coerce is justified... but not from the viewpoint of performances

```
sage: R.<x> = ZZ[]
sage: n = 2**123
sage: timeit("a = R(n)", number=300000)
300000 loops, best of 3: 633 ns per loop
sage: timeit("a = R.coerce(n)", number=300000)
300000 loops, best of 3: 936 ns per loop
```



---

Comment by pbruin created at 2015-04-20 10:03:04

When making the change

```diff
--- a/src/sage/rings/polynomial/polynomial_ring.py
+++ b/src/sage/rings/polynomial/polynomial_ring.py
@@ -1698,7 +1698,7 @@ class PolynomialRing_field(PolynomialRing_integral_domain,
            MATLAB*.  3rd edition, Prentice-Hall, 1999.
 
         """
-        to_base_ring = self.base_ring()
+        to_base_ring = self.base_ring().coerce
         points = map(lambda x: map(to_base_ring, x), points)
         n = len(points)
         F = [[points[i][1]] for i in xrange(n)]
@@ -1859,12 +1859,7 @@ class PolynomialRing_field(PolynomialRing_integral_domain,
            8th edition, Thomson Brooks/Cole, 2005.
 
         """
-        # Perhaps we should be slightly stricter on the input and use
-        # self.base_ring().coerce here and in the divided_difference()
-        # method above.  However, this breaks an example in
-        # sage.tests.french_book.nonlinear_doctest where the base ring
-        # is CC, but the function values lie in the symbolic ring.
-        to_base_ring = self.base_ring()
+        to_base_ring = self.base_ring().coerce
         points = map(lambda x: map(to_base_ring, x), points)
         var = self.gen()
 
```

I get

```
File "src/sage/tests/french_book/nonlinear_doctest.py", line 426, in sage.tests.french_book.nonlinear_doctest
Failed example:
    iterate(generator, check=checkconv)
Exception raised:
    Traceback (most recent call last):
    ...
    TypeError: no canonical coercion from Symbolic Ring to Complex Field with 53 bits of precision
```



---

Comment by vdelecroix created at 2015-04-20 10:10:53

Thanks for pointing the example! Once again the symbolic ring is wrong

```
sage: f(x) = 4 * sin(x) - exp(x) / 2 + 1
sage: f(1.2)
3.06809788250063
sage: parent(_)
Symbolic Ring
```

Parent should be `RR` as it is already the case for

```
sage: parent(exp(1.2))
Real Field with 53 bits of precision
sage: parent(sin(1.2))
Real Field with 53 bits of precision
```

But

```
sage: f(x) = x
sage: parent(f(1.2))
<type 'sage.symbolic.expression.Expression'>
```



---

Comment by pbruin created at 2015-04-20 10:51:23

Replying to [comment:21 vdelecroix]:
> Once again the symbolic ring is wrong
> {{{
> sage: f(x) = 4 * sin(x) - exp(x) / 2 + 1
> sage: f(1.2)
> 3.06809788250063
> sage: parent(_)
> Symbolic Ring
> }}}
> Parent should be `RR`
Indeed; compare

```
sage: f(x) = exp(x)
sage: parent(f(1.2))
Symbolic Ring
sage: parent(exp(1.2))
Real Field with 53 bits of precision
```

Related ticket: #18092


---

Comment by vdelecroix created at 2015-04-20 11:08:26

Replying to [comment:22 pbruin]:
> Replying to [comment:21 vdelecroix]:

Should we set a dependency and use `.coerce`? If you feel that it is too much, this ticket is good to go as it is.


---

Comment by pbruin created at 2015-04-20 11:14:58

Replying to [comment:23 vdelecroix]:
> Should we set a dependency and use `.coerce`?
If I understand #18092 correctly, it will only make `f.evaluate(x=1.2)` return an element of `RR`, while `f(1.2)` will remain a symbolic expression.  Hence I think #18092 would not automatically (transparently) solve this issue.

> If you feel that it is too much, this ticket is good to go as it is.
I interpret this as a positive review, correct me if I'm wrong.


---

Comment by pbruin created at 2015-04-20 11:14:58

Changing status from needs_review to positive_review.


---

Comment by dkrenn created at 2015-04-20 11:18:28

Replying to [comment:24 pbruin]:
> If I understand #18092 correctly, it will only make `f.evaluate(x=1.2)` return an element of `RR`, while `f(1.2)` will remain a symbolic expression.  Hence I think #18092 would not automatically (transparently) solve this issue.

Correct.


---

Comment by vdelecroix created at 2015-04-20 11:41:47

Replying to [comment:24 pbruin]:
> Replying to [comment:23 vdelecroix]:
> > Should we set a dependency and use `.coerce`?
> If I understand #18092 correctly, it will only make `f.evaluate(x=1.2)` return an element of `RR`, while `f(1.2)` will remain a symbolic expression.  Hence I think #18092 would not automatically (transparently) solve this issue.

I thought that `.evaluate` would be a modification of `.subs`!! With functions, this behavior would be *wrong*. It should be what it has to be

```
sage: f(x) = 2*x
sage: f.subs(x=3)
x |--> 6
```

In other words `f.evaluate(x=3)` should be a constant function!

> > If you feel that it is too much, this ticket is good to go as it is.
> I interpret this as a positive review, correct me if I'm wrong.

Perfect!

Vincent


---

Comment by vbraun created at 2015-04-21 00:10:51

Resolution: fixed
