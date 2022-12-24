# Issue 9786: lagrange_polynomial(algorithm='divided_difference') fails over finite fields

archive/issues_009786.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @miguelmarco\n\n\n```\nsage: R.<x>=GF(101)[]\nsage: R.lagrange_polynomial([[1,0],[2,0]])\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/data/sage-4.5.1/<ipython console> in <module>()\n\n/data/sage-4.5.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in lagrange_polynomial(self, points, algorithm, previous_row)\n   1481             P = F[n-1]\n   1482             for i in xrange(n-2, -1, -1):\n-> 1483                 P *= (var - points[i][0])\n   1484                 P += F[i]\n   1485             return P\n\n/data/sage-4.5.1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__imul__ (sage/structure/element.c:11631)()\n\n/data/sage-4.5.1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)()\n\nTypeError: unsupported operand parent(s) for '*': 'Rational Field' and 'Univariate Polynomial Ring in x over Finite Field of size 101'\nsage: R.lagrange_polynomial([[1,0],[2,0]],'neville')\n[0, 0]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9787\n\n",
    "created_at": "2010-08-23T13:09:53Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "lagrange_polynomial(algorithm='divided_difference') fails over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9786",
    "user": "@mezzarobba"
}
```
Assignee: @aghitza

CC:  @miguelmarco


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


Issue created by migration from https://trac.sagemath.org/ticket/9787





---

archive/issue_comments_096051.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-30T15:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96051",
    "user": "@mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096052.json:
```json
{
    "body": "The issue does not exist anymore with sage-5.12\u03b23.",
    "created_at": "2013-08-30T15:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96052",
    "user": "@mezzarobba"
}
```

The issue does not exist anymore with sage-5.12β3.



---

archive/issue_comments_096053.json:
```json
{
    "body": "In 5.12.beta5, the following still fails:\n\n```\nsage: R.<x>=GF(101)[]\nsage: sage: R.lagrange_polynomial([[1,0],[2,0],[3,0]])\n```\n",
    "created_at": "2013-09-22T18:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96053",
    "user": "@fchapoton"
}
```

In 5.12.beta5, the following still fails:

```
sage: R.<x>=GF(101)[]
sage: sage: R.lagrange_polynomial([[1,0],[2,0],[3,0]])
```




---

archive/issue_comments_096054.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-09-22T18:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96054",
    "user": "@fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096055.json:
```json
{
    "body": "Here is a branch that should fix the bug.  The only changes to the code are a few extra coercions (and one conversion, for reasons explained in a comment) to make sure everything lives in the right parent.  A few doctests had to be fixed because they started with the wrong base ring (`QQ` vs. `RR`) for the given input and output.  The other changes are documentation improvements.",
    "created_at": "2014-08-18T13:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96055",
    "user": "@pjbruin"
}
```

Here is a branch that should fix the bug.  The only changes to the code are a few extra coercions (and one conversion, for reasons explained in a comment) to make sure everything lives in the right parent.  A few doctests had to be fixed because they started with the wrong base ring (`QQ` vs. `RR`) for the given input and output.  The other changes are documentation improvements.



---

archive/issue_comments_096056.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-08-18T13:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96056",
    "user": "@pjbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096057.json:
```json
{
    "body": "I would propose something like:\n\n\n```\nseqpoints = Sequence([self.base().an_element()]+list(points))\npoints = [seqpoints.universe()(p) for p in points]\n```\n\n\nThat way we make sure that all the operations happen in the right parent (be it the base ring of the parent, or some other parent where both the input and the parent fit)",
    "created_at": "2014-08-22T13:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96057",
    "user": "@miguelmarco"
}
```

I would propose something like:


```
seqpoints = Sequence([self.base().an_element()]+list(points))
points = [seqpoints.universe()(p) for p in points]
```


That way we make sure that all the operations happen in the right parent (be it the base ring of the parent, or some other parent where both the input and the parent fit)



---

archive/issue_comments_096058.json:
```json
{
    "body": "Replying to [comment:9 mmarco]:\n> I would propose something like:\n> \n> {{{\n> seqpoints = Sequence([self.base().an_element()]+list(points))\n> points = [seqpoints.universe()(p) for p in points]\n> }}}\n> \n> That way we make sure that all the operations happen in the right parent (be it the base ring of the parent, or some other parent where both the input and the parent fit)\nDo you mean that `R.lagrange_polynomial()` should potentially return an element of a different ring than `R`?  That would be unnecessarily confusing in my opinion.",
    "created_at": "2014-08-22T14:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96058",
    "user": "@pjbruin"
}
```

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

archive/issue_comments_096059.json:
```json
{
    "body": "Well, you could have that even now:\n\n\n```\nsage: R.<x>=QQ[]\nsage: R.lagrange_polynomial(((1,1.75),(2,0.2),(3,1.5)))\n1.42500000000000*x^2 - 5.82500000000000*x + 6.15000000000000\n```\n\n\nYou can either catch that and raise an exception (which is probably the mathematically strictly correct), or be more flexible and allow situations like the previous (which, i think, can be useful in several cases).\n\nIn this case, i would vote for the second option, but i understand it is a matter of opinion.",
    "created_at": "2014-08-22T14:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96059",
    "user": "@miguelmarco"
}
```

Well, you could have that even now:


```
sage: R.<x>=QQ[]
sage: R.lagrange_polynomial(((1,1.75),(2,0.2),(3,1.5)))
1.42500000000000*x^2 - 5.82500000000000*x + 6.15000000000000
```


You can either catch that and raise an exception (which is probably the mathematically strictly correct), or be more flexible and allow situations like the previous (which, i think, can be useful in several cases).

In this case, i would vote for the second option, but i understand it is a matter of opinion.



---

archive/issue_comments_096060.json:
```json
{
    "body": "Replying to [comment:11 mmarco]:\n> Well, you could have that even now:\n> \n> {{{\n> sage: R.<x>=QQ[]\n> sage: R.lagrange_polynomial(((1,1.75),(2,0.2),(3,1.5)))\n> 1.42500000000000*x^2 - 5.82500000000000*x + 6.15000000000000\n> }}}\nActually, with this branch, you get\n\n```\nsage: R.<x>=QQ[]\nsage: R.lagrange_polynomial(((1,1.75),(2,0.2),(3,1.5)))\n57/40*x^2 - 233/40*x + 123/20\n```\n\nThis is not ideal from my point of view (I would prefer to use `coerce` to put the coefficients into the base field of `R`, so this example would raise an error), but a doctest in a published book unfortunately depends on it.\n> You can either catch that and raise an exception (which is probably the mathematically strictly correct), or be more flexible and allow situations like the previous (which, i think, can be useful in several cases).\nI see that this could be the expected behaviour given the general permissiveness in Sage with respect to extending parents, but I would still find it strange if `R.lagrange_polynomial()` did not return a value in `R` but in a different ring depending on the input.  It would mean that `lagrange_polynomial()` basically had no relation to `R`.  If there were a standalone function `lagrange_polynomial()`, then it would be logical if `lagrange_polynomial()` returned a polynomial in a parent depending on the input, but the explicit presence of `R` in the notation `R.lagrange_polynomial()` does suggest to me that it should always return a polynomial in `R`.",
    "created_at": "2014-08-22T15:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96060",
    "user": "@pjbruin"
}
```

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

archive/issue_comments_096061.json:
```json
{
    "body": "Well, if it is clearly stated that the result should be in R, conversion should also be allowed, from my point of view. I can see solid arguments for any of the possible choices: coerce to R.basis(), convert to R.basis(), or extend for the common universe of R.basis() and the input. My personal choice would be the last one, but as long as it is clearly documented, i could live with any.\n\nAnother option would be to include a keyword (like 'extend', for example) to control the behaviour in this aspect. That way you can have a default functionality, but also another option for the user to choose. Although, it seems a bit overkill for this.",
    "created_at": "2014-08-24T13:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96061",
    "user": "@miguelmarco"
}
```

Well, if it is clearly stated that the result should be in R, conversion should also be allowed, from my point of view. I can see solid arguments for any of the possible choices: coerce to R.basis(), convert to R.basis(), or extend for the common universe of R.basis() and the input. My personal choice would be the last one, but as long as it is clearly documented, i could live with any.

Another option would be to include a keyword (like 'extend', for example) to control the behaviour in this aspect. That way you can have a default functionality, but also another option for the user to choose. Although, it seems a bit overkill for this.



---

archive/issue_comments_096062.json:
```json
{
    "body": "Replying to [comment:13 mmarco]:\n> Well, if it is clearly stated that the result should be in R, conversion should also be allowed, from my point of view.\nFair point, I'll change that and improve the documentation.\n> I can see solid arguments for any of the possible choices: coerce to R.basis(), convert to R.basis(), or extend for the common universe of R.basis() and the input. My personal choice would be the last one, but as long as it is clearly documented, i could live with any.\nI still think that `R.lagrange_polynomial(...)` should return something in `R`.  In practice it should be easy to convert the input into the base ring, unless the user made this ring too small for some reason.  In that case the user can easily enlarge the base ring.\n> Another option would be to include a keyword (like 'extend', for example) to control the behaviour in this aspect. That way you can have a default functionality, but also another option for the user to choose. Although, it seems a bit overkill for this.\nThis sounds like a reasonable option, but I do think it is a bit overkill, so someone who really wants it can implement it.",
    "created_at": "2014-08-25T11:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96062",
    "user": "@pjbruin"
}
```

Replying to [comment:13 mmarco]:
> Well, if it is clearly stated that the result should be in R, conversion should also be allowed, from my point of view.
Fair point, I'll change that and improve the documentation.
> I can see solid arguments for any of the possible choices: coerce to R.basis(), convert to R.basis(), or extend for the common universe of R.basis() and the input. My personal choice would be the last one, but as long as it is clearly documented, i could live with any.
I still think that `R.lagrange_polynomial(...)` should return something in `R`.  In practice it should be easy to convert the input into the base ring, unless the user made this ring too small for some reason.  In that case the user can easily enlarge the base ring.
> Another option would be to include a keyword (like 'extend', for example) to control the behaviour in this aspect. That way you can have a default functionality, but also another option for the user to choose. Although, it seems a bit overkill for this.
This sounds like a reasonable option, but I do think it is a bit overkill, so someone who really wants it can implement it.



---

archive/issue_comments_096063.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-25T11:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96063",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096064.json:
```json
{
    "body": "Hello,\n\nOn sage-6.5 at least, I got the right answer.\n\n```\nsage: R.<x>=GF(101)[]\nsage: R.lagrange_polynomial([[1,0],[2,0]])\n0\n```\n\nIt would be cool to add it to the documentation since it was the initial purpose of the ticket.\n\nVincent",
    "created_at": "2015-04-18T12:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96064",
    "user": "@videlec"
}
```

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

archive/issue_comments_096065.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-04-20T08:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96065",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096066.json:
```json
{
    "body": "Replying to [comment:16 vdelecroix]:\n> On sage-6.5 at least, I got the right answer.\n> {{{\n> sage: R.<x>=GF(101)[]\n> sage: R.lagrange_polynomial([[1,0],[2,0]])\n> 0\n> }}}\nThis one was fixed at some point (see comment:2), but I added a doctest anyway.",
    "created_at": "2015-04-20T08:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96066",
    "user": "@pjbruin"
}
```

Replying to [comment:16 vdelecroix]:
> On sage-6.5 at least, I got the right answer.
> {{{
> sage: R.<x>=GF(101)[]
> sage: R.lagrange_polynomial([[1,0],[2,0]])
> 0
> }}}
This one was fixed at some point (see comment:2), but I added a doctest anyway.



---

archive/issue_comments_096067.json:
```json
{
    "body": "Hello,\n\nLooks good! Concerning the [comment:12 comment:12], where is this example in the sage book (I was not able to find it)? Should it be added to the documentation as an example with a warning?\n\nVincent\n\nPS: Note that using coerce is justified... but not from the viewpoint of performances\n\n```\nsage: R.<x> = ZZ[]\nsage: n = 2**123\nsage: timeit(\"a = R(n)\", number=300000)\n300000 loops, best of 3: 633 ns per loop\nsage: timeit(\"a = R.coerce(n)\", number=300000)\n300000 loops, best of 3: 936 ns per loop\n```\n",
    "created_at": "2015-04-20T09:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96067",
    "user": "@videlec"
}
```

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

archive/issue_comments_096068.json:
```json
{
    "body": "When making the change\n\n```diff\n--- a/src/sage/rings/polynomial/polynomial_ring.py\n+++ b/src/sage/rings/polynomial/polynomial_ring.py\n@@ -1698,7 +1698,7 @@ class PolynomialRing_field(PolynomialRing_integral_domain,\n            MATLAB*.  3rd edition, Prentice-Hall, 1999.\n \n         \"\"\"\n-        to_base_ring = self.base_ring()\n+        to_base_ring = self.base_ring().coerce\n         points = map(lambda x: map(to_base_ring, x), points)\n         n = len(points)\n         F = [[points[i][1]] for i in xrange(n)]\n@@ -1859,12 +1859,7 @@ class PolynomialRing_field(PolynomialRing_integral_domain,\n            8th edition, Thomson Brooks/Cole, 2005.\n \n         \"\"\"\n-        # Perhaps we should be slightly stricter on the input and use\n-        # self.base_ring().coerce here and in the divided_difference()\n-        # method above.  However, this breaks an example in\n-        # sage.tests.french_book.nonlinear_doctest where the base ring\n-        # is CC, but the function values lie in the symbolic ring.\n-        to_base_ring = self.base_ring()\n+        to_base_ring = self.base_ring().coerce\n         points = map(lambda x: map(to_base_ring, x), points)\n         var = self.gen()\n \n```\n\nI get\n\n```\nFile \"src/sage/tests/french_book/nonlinear_doctest.py\", line 426, in sage.tests.french_book.nonlinear_doctest\nFailed example:\n    iterate(generator, check=checkconv)\nException raised:\n    Traceback (most recent call last):\n    ...\n    TypeError: no canonical coercion from Symbolic Ring to Complex Field with 53 bits of precision\n```\n",
    "created_at": "2015-04-20T10:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96068",
    "user": "@pjbruin"
}
```

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

archive/issue_comments_096069.json:
```json
{
    "body": "Thanks for pointing the example! Once again the symbolic ring is wrong\n\n```\nsage: f(x) = 4 * sin(x) - exp(x) / 2 + 1\nsage: f(1.2)\n3.06809788250063\nsage: parent(_)\nSymbolic Ring\n```\n\nParent should be `RR` as it is already the case for\n\n```\nsage: parent(exp(1.2))\nReal Field with 53 bits of precision\nsage: parent(sin(1.2))\nReal Field with 53 bits of precision\n```\n\nBut\n\n```\nsage: f(x) = x\nsage: parent(f(1.2))\n<type 'sage.symbolic.expression.Expression'>\n```\n",
    "created_at": "2015-04-20T10:10:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96069",
    "user": "@videlec"
}
```

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

archive/issue_comments_096070.json:
```json
{
    "body": "Replying to [comment:21 vdelecroix]:\n> Once again the symbolic ring is wrong\n> {{{\n> sage: f(x) = 4 * sin(x) - exp(x) / 2 + 1\n> sage: f(1.2)\n> 3.06809788250063\n> sage: parent(_)\n> Symbolic Ring\n> }}}\n> Parent should be `RR`\nIndeed; compare\n\n```\nsage: f(x) = exp(x)\nsage: parent(f(1.2))\nSymbolic Ring\nsage: parent(exp(1.2))\nReal Field with 53 bits of precision\n```\n\nRelated ticket: #18092",
    "created_at": "2015-04-20T10:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96070",
    "user": "@pjbruin"
}
```

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

archive/issue_comments_096071.json:
```json
{
    "body": "Replying to [comment:22 pbruin]:\n> Replying to [comment:21 vdelecroix]:\n\nShould we set a dependency and use `.coerce`? If you feel that it is too much, this ticket is good to go as it is.",
    "created_at": "2015-04-20T11:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96071",
    "user": "@videlec"
}
```

Replying to [comment:22 pbruin]:
> Replying to [comment:21 vdelecroix]:

Should we set a dependency and use `.coerce`? If you feel that it is too much, this ticket is good to go as it is.



---

archive/issue_comments_096072.json:
```json
{
    "body": "Replying to [comment:23 vdelecroix]:\n> Should we set a dependency and use `.coerce`?\nIf I understand #18092 correctly, it will only make `f.evaluate(x=1.2)` return an element of `RR`, while `f(1.2)` will remain a symbolic expression.  Hence I think #18092 would not automatically (transparently) solve this issue.\n\n> If you feel that it is too much, this ticket is good to go as it is.\nI interpret this as a positive review, correct me if I'm wrong.",
    "created_at": "2015-04-20T11:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96072",
    "user": "@pjbruin"
}
```

Replying to [comment:23 vdelecroix]:
> Should we set a dependency and use `.coerce`?
If I understand #18092 correctly, it will only make `f.evaluate(x=1.2)` return an element of `RR`, while `f(1.2)` will remain a symbolic expression.  Hence I think #18092 would not automatically (transparently) solve this issue.

> If you feel that it is too much, this ticket is good to go as it is.
I interpret this as a positive review, correct me if I'm wrong.



---

archive/issue_comments_096073.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-20T11:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96073",
    "user": "@pjbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096074.json:
```json
{
    "body": "Replying to [comment:24 pbruin]:\n> If I understand #18092 correctly, it will only make `f.evaluate(x=1.2)` return an element of `RR`, while `f(1.2)` will remain a symbolic expression.  Hence I think #18092 would not automatically (transparently) solve this issue.\n\nCorrect.",
    "created_at": "2015-04-20T11:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96074",
    "user": "@dkrenn"
}
```

Replying to [comment:24 pbruin]:
> If I understand #18092 correctly, it will only make `f.evaluate(x=1.2)` return an element of `RR`, while `f(1.2)` will remain a symbolic expression.  Hence I think #18092 would not automatically (transparently) solve this issue.

Correct.



---

archive/issue_comments_096075.json:
```json
{
    "body": "Replying to [comment:24 pbruin]:\n> Replying to [comment:23 vdelecroix]:\n> > Should we set a dependency and use `.coerce`?\n> If I understand #18092 correctly, it will only make `f.evaluate(x=1.2)` return an element of `RR`, while `f(1.2)` will remain a symbolic expression.  Hence I think #18092 would not automatically (transparently) solve this issue.\n\nI thought that `.evaluate` would be a modification of `.subs`!! With functions, this behavior would be **wrong**. It should be what it has to be\n\n```\nsage: f(x) = 2*x\nsage: f.subs(x=3)\nx |--> 6\n```\n\nIn other words `f.evaluate(x=3)` should be a constant function!\n\n> > If you feel that it is too much, this ticket is good to go as it is.\n> I interpret this as a positive review, correct me if I'm wrong.\n\nPerfect!\n\nVincent",
    "created_at": "2015-04-20T11:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96075",
    "user": "@videlec"
}
```

Replying to [comment:24 pbruin]:
> Replying to [comment:23 vdelecroix]:
> > Should we set a dependency and use `.coerce`?
> If I understand #18092 correctly, it will only make `f.evaluate(x=1.2)` return an element of `RR`, while `f(1.2)` will remain a symbolic expression.  Hence I think #18092 would not automatically (transparently) solve this issue.

I thought that `.evaluate` would be a modification of `.subs`!! With functions, this behavior would be **wrong**. It should be what it has to be

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

archive/issue_comments_096076.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-04-21T00:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9786#issuecomment-96076",
    "user": "@vbraun"
}
```

Resolution: fixed
