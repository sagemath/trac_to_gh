# Issue 8972: Inversion and fraction fields for power series rings

archive/issues_008972.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  tscrim mkoeppe nbruin jhpalmieri dkrenn bruno tmonteil vdelecroix @davewittemorris\n\nKeywords: power series ring, fraction field\n\nThis ticket is about at least three bugs related with inversion of elements of power series rings.\n\nHere is the first:\n\n```\nsage: R.<x> = ZZ[[]]\nsage: (1/x).parent()\nLaurent Series Ring in x over Integer Ring\nsage: (x/x).parent()\nPower Series Ring in x over Integer Ring\n```\n\n*Both* parents are wrong. Usually, the parent of ``a/b`` is the fraction field of the parent of ``a,b``, even if ``a==b``. And neither above parent is a field.\n\nNext bug:\n\n```\nsage: (1/(2*x)).parent()\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (919, 0))\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n... very long traceback\nTypeError: no conversion of this rational to integer\n```\n\n\nAnd the third:\n\n```\nsage: F = FractionField(R)\nsage: 1/x in F\nFalse\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8972\n\n",
    "created_at": "2010-05-15T15:46:05Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.3",
    "title": "Inversion and fraction fields for power series rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8972",
    "user": "SimonKing"
}
```
Assignee: AlexGhitza

CC:  tscrim mkoeppe nbruin jhpalmieri dkrenn bruno tmonteil vdelecroix @davewittemorris

Keywords: power series ring, fraction field

This ticket is about at least three bugs related with inversion of elements of power series rings.

Here is the first:

```
sage: R.<x> = ZZ[[]]
sage: (1/x).parent()
Laurent Series Ring in x over Integer Ring
sage: (x/x).parent()
Power Series Ring in x over Integer Ring
```

*Both* parents are wrong. Usually, the parent of ``a/b`` is the fraction field of the parent of ``a,b``, even if ``a==b``. And neither above parent is a field.

Next bug:

```
sage: (1/(2*x)).parent()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (919, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
... very long traceback
TypeError: no conversion of this rational to integer
```


And the third:

```
sage: F = FractionField(R)
sage: 1/x in F
False
```


Issue created by migration from https://trac.sagemath.org/ticket/8972





---

archive/issue_comments_082677.json:
```json
{
    "body": "OK, here is a patch.\n\nIdea: \n\n* Introduce a fraction_field method to power series rings that returns the Laurent series ring over the fraction field of the base ring. I hope that the base_extend method for Laurent polynomials works stably enough, otherwise it should be rewritten.\n* In the division method of power serise, construct the fraction field of the parent, move numerator and denominator into the fraction field, and divide there. The original form of the method is preserved as a fail safe.\n\nWith the patch, I get:\n\n```\nsage: P.<t> = ZZ[]\nsage: R.<x> = P[[]]\nsage: FractionField(R)\nLaurent Series Ring in x over Fraction Field of Univariate Polynomial Ring in t over Integer Ring\n```\n\n\nO dear. I just realise that there will be more work. There is a segmentation fault, as follows:\n\n```\nsage: R1.<x> = ZZ[[]]\nsage: F = FractionField(R1)\nsage: F\nLaurent Series Ring in x over Rational Field\nsage: F(x)\nx\nsage: ~F(x)\n/home/king/SAGE/sage-4.3.1/local/bin/sage-sage: line 206:  4437 Segmentation fault      sage-ipython \"$@\" -i\n```\n\n\nSo, the division of elements of a Laurent series ring fails with a segmentation fault. By consequence, division of power series segfaults as well, with the patch. \"Needs work\", I presume.",
    "created_at": "2010-05-15T16:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82677",
    "user": "SimonKing"
}
```

OK, here is a patch.

Idea: 

* Introduce a fraction_field method to power series rings that returns the Laurent series ring over the fraction field of the base ring. I hope that the base_extend method for Laurent polynomials works stably enough, otherwise it should be rewritten.
* In the division method of power serise, construct the fraction field of the parent, move numerator and denominator into the fraction field, and divide there. The original form of the method is preserved as a fail safe.

With the patch, I get:

```
sage: P.<t> = ZZ[]
sage: R.<x> = P[[]]
sage: FractionField(R)
Laurent Series Ring in x over Fraction Field of Univariate Polynomial Ring in t over Integer Ring
```


O dear. I just realise that there will be more work. There is a segmentation fault, as follows:

```
sage: R1.<x> = ZZ[[]]
sage: F = FractionField(R1)
sage: F
Laurent Series Ring in x over Rational Field
sage: F(x)
x
sage: ~F(x)
/home/king/SAGE/sage-4.3.1/local/bin/sage-sage: line 206:  4437 Segmentation fault      sage-ipython "$@" -i
```


So, the division of elements of a Laurent series ring fails with a segmentation fault. By consequence, division of power series segfaults as well, with the patch. "Needs work", I presume.



---

archive/issue_comments_082678.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-15T16:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82678",
    "user": "SimonKing"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_082679.json:
```json
{
    "body": "Strangely, without the patch, the construction works:\n\n```\nsage: R.<x> = ZZ[[]]\nsage: F = LaurentSeriesRing(FractionField(R.base()),R.variable_names())\nsage: 1/F(x)\nx^-1\n```\n\n\nThe patch does this construction as well -- but segfaults. There seems to be a nasty side effect.",
    "created_at": "2010-05-15T17:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82679",
    "user": "SimonKing"
}
```

Strangely, without the patch, the construction works:

```
sage: R.<x> = ZZ[[]]
sage: F = LaurentSeriesRing(FractionField(R.base()),R.variable_names())
sage: 1/F(x)
x^-1
```


The patch does this construction as well -- but segfaults. There seems to be a nasty side effect.



---

archive/issue_comments_082680.json:
```json
{
    "body": "The segfault problem seems to come from the fact that the div method for Laurent series relies on the div method for power series -- and with my patch, the div method for power series uses the div method for Laurent series. Not good. But that seems solvable.",
    "created_at": "2010-05-15T18:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82680",
    "user": "SimonKing"
}
```

The segfault problem seems to come from the fact that the div method for Laurent series relies on the div method for power series -- and with my patch, the div method for power series uses the div method for Laurent series. Not good. But that seems solvable.



---

archive/issue_comments_082681.json:
```json
{
    "body": "Attachment [8972_power_series_inverses.patch](tarball://root/attachments/some-uuid/ticket8972/8972_power_series_inverses.patch) by SimonKing created at 2010-05-15 19:24:00\n\nBugfixes for fraction field and inverses of power series over non-fields",
    "created_at": "2010-05-15T19:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82681",
    "user": "SimonKing"
}
```

Attachment [8972_power_series_inverses.patch](tarball://root/attachments/some-uuid/ticket8972/8972_power_series_inverses.patch) by SimonKing created at 2010-05-15 19:24:00

Bugfixes for fraction field and inverses of power series over non-fields



---

archive/issue_comments_082682.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-15T19:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82682",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082683.json:
```json
{
    "body": "OK, I replaced the old patch, and now it seems to work!\n\nFor example:\n\n```\nsage: P.<t> = ZZ[]\nsage: R.<x> = P[[]]\nsage: 1/(t*x)\n1/t*x^-1\nsage: (1/x).parent() is FractionField(R)\nTrue\nsage: Frac(R)\nLaurent Series Ring in x over Fraction Field of Univariate Polynomial Ring in t over Integer Ring\n```\n\n\nThe doc tests for the two modified files pass. So, ready for review!",
    "created_at": "2010-05-15T19:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82683",
    "user": "SimonKing"
}
```

OK, I replaced the old patch, and now it seems to work!

For example:

```
sage: P.<t> = ZZ[]
sage: R.<x> = P[[]]
sage: 1/(t*x)
1/t*x^-1
sage: (1/x).parent() is FractionField(R)
True
sage: Frac(R)
Laurent Series Ring in x over Fraction Field of Univariate Polynomial Ring in t over Integer Ring
```


The doc tests for the two modified files pass. So, ready for review!



---

archive/issue_comments_082684.json:
```json
{
    "body": "PS: Even the following works:\n\n```\nsage: 1/(t+x)\n1/t - 1/t^2*x + (-1/-t^3)*x^2 + (1/-t^4)*x^3 + 1/t^5*x^4 - 1/t^6*x^5 + 1/t^7*x^6 - 1/t^8*x^7 + 1/t^9*x^8 + (1/-t^10)*x^9 + 1/t^11*x^10 + (1/-t^12)*x^11 + 1/t^13*x^12 + (1/-t^14)*x^13 + (-1/-t^15)*x^14 + (1/-t^16)*x^15 + (-1/-t^17)*x^16 + (1/-t^18)*x^17 + 1/t^19*x^18 - 1/t^20*x^19 + O(x^20)\n```\n",
    "created_at": "2010-05-15T19:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82684",
    "user": "SimonKing"
}
```

PS: Even the following works:

```
sage: 1/(t+x)
1/t - 1/t^2*x + (-1/-t^3)*x^2 + (1/-t^4)*x^3 + 1/t^5*x^4 - 1/t^6*x^5 + 1/t^7*x^6 - 1/t^8*x^7 + 1/t^9*x^8 + (1/-t^10)*x^9 + 1/t^11*x^10 + (1/-t^12)*x^11 + 1/t^13*x^12 + (1/-t^14)*x^13 + (-1/-t^15)*x^14 + (1/-t^16)*x^15 + (-1/-t^17)*x^16 + (1/-t^18)*x^17 + 1/t^19*x^18 - 1/t^20*x^19 + O(x^20)
```




---

archive/issue_comments_082685.json:
```json
{
    "body": "I'm wary of such a big change until we have some timing tests in place. In particular, I'm worried about potential slowdowns in the Monsky-Washnitzer code.",
    "created_at": "2010-05-15T21:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82685",
    "user": "robertwb"
}
```

I'm wary of such a big change until we have some timing tests in place. In particular, I'm worried about potential slowdowns in the Monsky-Washnitzer code.



---

archive/issue_comments_082686.json:
```json
{
    "body": "Replying to [comment:6 robertwb]:\n> I'm wary of such a big change until we have some timing tests in place. In particular, I'm worried about potential slowdowns in the Monsky-Washnitzer code. \n\nYou are right, timing should be taken into account, and this is something my patch doesn't provide. Without the patch:\n\n```\nsage: R.<x> = ZZ[[]]\nsage: timeit('a=1/(1+x)')\n625 loops, best of 3: 1.08 ms per loop\n```\n\nWith the patch\n\n```\nsage: R.<x> = ZZ[[]]\nsage: timeit('a=1/(1+x)')\n125 loops, best of 3: 6 ms per loop\n```\n\nSo, it is slower by more than a factor five.",
    "created_at": "2010-05-15T22:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82686",
    "user": "SimonKing"
}
```

Replying to [comment:6 robertwb]:
> I'm wary of such a big change until we have some timing tests in place. In particular, I'm worried about potential slowdowns in the Monsky-Washnitzer code. 

You are right, timing should be taken into account, and this is something my patch doesn't provide. Without the patch:

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 1.08 ms per loop
```

With the patch

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/(1+x)')
125 loops, best of 3: 6 ms per loop
```

So, it is slower by more than a factor five.



---

archive/issue_comments_082687.json:
```json
{
    "body": "Concerning timings, I see a couple of things that might help improve the div method:\n\n1. My patch calls the fraction_field method; *in addition* the original code calls the laurent_series_ring method. But the purpose of both is the same. So, only one should be done.\n2. The fraction_field method should better be cached; this would save a lot of time, since the fradtion field construction involves the construction of a Laurent series ring and the construction of the fraction field of the base ring.\n3. Currently the div methods of power series and of Laurent series call each other; I don't know if this is done efficiently (e.g., avoiding Python calls). I could imagine that this can be stratified.\n\nSo, something to do for tomorrow. And I guess the ticket is again \"needs work\".",
    "created_at": "2010-05-15T23:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82687",
    "user": "SimonKing"
}
```

Concerning timings, I see a couple of things that might help improve the div method:

1. My patch calls the fraction_field method; *in addition* the original code calls the laurent_series_ring method. But the purpose of both is the same. So, only one should be done.
2. The fraction_field method should better be cached; this would save a lot of time, since the fradtion field construction involves the construction of a Laurent series ring and the construction of the fraction field of the base ring.
3. Currently the div methods of power series and of Laurent series call each other; I don't know if this is done efficiently (e.g., avoiding Python calls). I could imagine that this can be stratified.

So, something to do for tomorrow. And I guess the ticket is again "needs work".



---

archive/issue_comments_082688.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-15T23:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82688",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082689.json:
```json
{
    "body": "Replying to [comment:8 SimonKing]:\n> Concerning timings, I see a couple of things that might help improve the div method:\n\nOne more thing: The old code is quick if the result actually belongs to the power series ring, which is quite often the case; if this is not the case then often an error results. And I guess the parent should always be the fraction field, eventually.\n\nWhat I just tested (but I really should get some sleep now...) is to cache the fraction_field method, and to *try* to use the old code if the valuation of the denominator is not bigger than the valuation of the numerator; if this fails, then put numerator and denominator into the fraction field, and try again.\n\nDoing so brings the above timing to about 2ms, which is still a loss of factor two, but two is less than 5 or 6. I'll submit another patch after trying to lift the dependency of the two div methods on each other.",
    "created_at": "2010-05-16T00:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82689",
    "user": "SimonKing"
}
```

Replying to [comment:8 SimonKing]:
> Concerning timings, I see a couple of things that might help improve the div method:

One more thing: The old code is quick if the result actually belongs to the power series ring, which is quite often the case; if this is not the case then often an error results. And I guess the parent should always be the fraction field, eventually.

What I just tested (but I really should get some sleep now...) is to cache the fraction_field method, and to *try* to use the old code if the valuation of the denominator is not bigger than the valuation of the numerator; if this fails, then put numerator and denominator into the fraction field, and try again.

Doing so brings the above timing to about 2ms, which is still a loss of factor two, but two is less than 5 or 6. I'll submit another patch after trying to lift the dependency of the two div methods on each other.



---

archive/issue_comments_082690.json:
```json
{
    "body": "Attachment [8972_power_series_timing.patch](tarball://root/attachments/some-uuid/ticket8972/8972_power_series_timing.patch) by SimonKing created at 2010-05-16 22:32:03\n\nImproving the timings, to be applied after the bug fix patch",
    "created_at": "2010-05-16T22:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82690",
    "user": "SimonKing"
}
```

Attachment [8972_power_series_timing.patch](tarball://root/attachments/some-uuid/ticket8972/8972_power_series_timing.patch) by SimonKing created at 2010-05-16 22:32:03

Improving the timings, to be applied after the bug fix patch



---

archive/issue_comments_082691.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-16T22:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82691",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082692.json:
```json
{
    "body": "The second patch does several things:\n\n1. It turned out that in several places it is assumed that the quotient of two power series is a power series, not a Laurent series. I tried to take care of this.\n\n2. I improved the timings, so that (according to the timings below) the performance is competitive (sometimes clearly better, sometimes very little worse) then the original performance.\n\nThe reason why the old timings were good was some kind of lazyness: The result of a division was not in the fraction field (as it should be!), but in a simpler ring, so that subsequent computations became easier. On the other hand, transformation into a Laurent polynomial was quite expensive, since there *always* was a transformation into the Laurent Series Ring's underlying Power Series Ring -- even if the given data already belong to it.\n\nSolution (as usual): Add an optional argument \"check\" to the init method of Laurent Series.\n\nAnd then I tried to benefit from keeping the results as simple as possible (like the old code did), but in a more proper way. Let ``f`` be a Laurent series in a Laurent series ring ``L``. In the old code, one always had ``L.power_series_ring() is f.valuation_zero_part().parent()``. I suggest to relax this condition: It is sufficient to have a coercion:\n\n```\nsage: R.<x> = ZZ[[]]\nsage: f = 1/(1+2*x)\nsage: f.parent()\nLaurent Series Ring in x over Rational Field\nsage: f.parent().power_series_ring()\nPower Series Ring in x over Rational Field\nsage: f.power_series().parent()\nPower Series Ring in x over Integer Ring\n```\n\n\n**__Timings__**\n\nWithout the two patches:\n\n```\nsage: R.<x> = ZZ[[]]\nsage: timeit('a=1/x')\n625 loops, best of 3: 291 \u00b5s per loop\nsage: timeit('a=(1+x)/x')\n625 loops, best of 3: 295 \u00b5s per loop\nsage: timeit('a=1/(1+x)')\n625 loops, best of 3: 1.07 ms per loop\nsage: timeit('a=(1+x)/(1-x)')\n625 loops, best of 3: 1.07 ms per loop\nsage: y = (3*x+2)/(1+x)\nsage: y=y/x\nsage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)\nsage: z=y/x\nsage: timeit('y+z')\n625 loops, best of 3: 213 \u00b5s per loop\nsage: timeit('y*z')\n625 loops, best of 3: 118 \u00b5s per loop\nsage: timeit('y-z')\n625 loops, best of 3: 212 \u00b5s per loop\nsage: timeit('y/z')\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (27, 0))\n\n---------------------------------------------------------------------------\nArithmeticError                           Traceback (most recent call last)\n...\nArithmeticError: division not defined\n```\n\n\nWith the two patches:\n\n```\nsage: R.<x> = ZZ[[]]\nsage: timeit('a=1/x')\n625 loops, best of 3: 220 \u00b5s per loop\nsage: timeit('a=(1+x)/x')\n625 loops, best of 3: 228 \u00b5s per loop\nsage: timeit('a=1/(1+x)')\n625 loops, best of 3: 1.25 ms per loop\nsage: timeit('a=(1+x)/(1-x)')\n625 loops, best of 3: 1.26 ms per loop\nsage: y = (3*x+2)/(1+x)\nsage: y=y/x\nsage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)\nsage: z=y/x\nsage: timeit('y+z')\n625 loops, best of 3: 191 \u00b5s per loop\nsage: timeit('y*z')\n625 loops, best of 3: 92.6 \u00b5s per loop\nsage: timeit('y-z')\n625 loops, best of 3: 191 \u00b5s per loop\nsage: timeit('y/z')\n25 loops, best of 3: 9.35 ms per loop\n```\n\n\nSo, my patches not only fix some bugs, but they also slightly improve the performance.\n\nI tested all files that I have changed, but I can not exclude errors in other files.\n\nI forgot to insert my name as an author, but presumably there will be a revision needed anyway, after comments of referees...",
    "created_at": "2010-05-16T22:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82692",
    "user": "SimonKing"
}
```

The second patch does several things:

1. It turned out that in several places it is assumed that the quotient of two power series is a power series, not a Laurent series. I tried to take care of this.

2. I improved the timings, so that (according to the timings below) the performance is competitive (sometimes clearly better, sometimes very little worse) then the original performance.

The reason why the old timings were good was some kind of lazyness: The result of a division was not in the fraction field (as it should be!), but in a simpler ring, so that subsequent computations became easier. On the other hand, transformation into a Laurent polynomial was quite expensive, since there *always* was a transformation into the Laurent Series Ring's underlying Power Series Ring -- even if the given data already belong to it.

Solution (as usual): Add an optional argument "check" to the init method of Laurent Series.

And then I tried to benefit from keeping the results as simple as possible (like the old code did), but in a more proper way. Let ``f`` be a Laurent series in a Laurent series ring ``L``. In the old code, one always had ``L.power_series_ring() is f.valuation_zero_part().parent()``. I suggest to relax this condition: It is sufficient to have a coercion:

```
sage: R.<x> = ZZ[[]]
sage: f = 1/(1+2*x)
sage: f.parent()
Laurent Series Ring in x over Rational Field
sage: f.parent().power_series_ring()
Power Series Ring in x over Rational Field
sage: f.power_series().parent()
Power Series Ring in x over Integer Ring
```


**__Timings__**

Without the two patches:

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/x')
625 loops, best of 3: 291 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 295 µs per loop
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 1.07 ms per loop
sage: timeit('a=(1+x)/(1-x)')
625 loops, best of 3: 1.07 ms per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 213 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 118 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 212 µs per loop
sage: timeit('y/z')
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (27, 0))

---------------------------------------------------------------------------
ArithmeticError                           Traceback (most recent call last)
...
ArithmeticError: division not defined
```


With the two patches:

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/x')
625 loops, best of 3: 220 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 228 µs per loop
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 1.25 ms per loop
sage: timeit('a=(1+x)/(1-x)')
625 loops, best of 3: 1.26 ms per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 191 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 92.6 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 191 µs per loop
sage: timeit('y/z')
25 loops, best of 3: 9.35 ms per loop
```


So, my patches not only fix some bugs, but they also slightly improve the performance.

I tested all files that I have changed, but I can not exclude errors in other files.

I forgot to insert my name as an author, but presumably there will be a revision needed anyway, after comments of referees...



---

archive/issue_comments_082693.json:
```json
{
    "body": "I forgot one remark:\n\nI don't know how this happens, but the ``truncate`` method of Laurent series behaves different than before, although the ``truncate`` method of power series did not change:\n\n```\nsage: A.<t> = QQ[[]]\nsage: f = (1+t)^100\nsage: f.truncate(5)\n3921225*t^4 + 161700*t^3 + 4950*t^2 + 100*t + 1\nsage: f.truncate(5).parent()\nUnivariate Polynomial Ring in t over Rational Field\nsage: g = 1/f\nsage: g.truncate(5)\n1 - 100*t + 5050*t^2 - 171700*t^3 + 4421275*t^4 + O(t^5)\nsage: g.truncate(5).parent()\nLaurent Series Ring in t over Rational Field\n```\n\n\nIn other words, ``g.truncate(5)`` is now returning a Laurent series, but without the patch it used to return return a univariate polynomial, similar to ``f.truncate(5)``.\n\nI don't know if this is acceptable, and also I don't understand how that happened. Shall I change it?",
    "created_at": "2010-05-17T07:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82693",
    "user": "SimonKing"
}
```

I forgot one remark:

I don't know how this happens, but the ``truncate`` method of Laurent series behaves different than before, although the ``truncate`` method of power series did not change:

```
sage: A.<t> = QQ[[]]
sage: f = (1+t)^100
sage: f.truncate(5)
3921225*t^4 + 161700*t^3 + 4950*t^2 + 100*t + 1
sage: f.truncate(5).parent()
Univariate Polynomial Ring in t over Rational Field
sage: g = 1/f
sage: g.truncate(5)
1 - 100*t + 5050*t^2 - 171700*t^3 + 4421275*t^4 + O(t^5)
sage: g.truncate(5).parent()
Laurent Series Ring in t over Rational Field
```


In other words, ``g.truncate(5)`` is now returning a Laurent series, but without the patch it used to return return a univariate polynomial, similar to ``f.truncate(5)``.

I don't know if this is acceptable, and also I don't understand how that happened. Shall I change it?



---

archive/issue_comments_082694.json:
```json
{
    "body": "Replying to [comment:11 SimonKing]:\n> I forgot one remark:\n> \n> I don't know how this happens, but the ``truncate`` method of Laurent series behaves different than before, although the ``truncate`` method of power series did not change:\n\nOutch, now I see my mistake.\n\n* The documentation of ``LaurentSeries.truncate`` states that indeed it returns a Laurent series. It does not have a doc test, so, I will add one.\n\n* The old doc test of ``PowerSeries.truncate`` fails with my patch. The reason is that the *power* series constructed in this doc test is now in fact a *Laurent* series; this is what made me believe that the behaviour of the method has changed. So, I only have to change the doc test.\n\nBut before submitting a patch to add/correct these doc tests, I'll wait for input of a referee.",
    "created_at": "2010-05-17T08:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82694",
    "user": "SimonKing"
}
```

Replying to [comment:11 SimonKing]:
> I forgot one remark:
> 
> I don't know how this happens, but the ``truncate`` method of Laurent series behaves different than before, although the ``truncate`` method of power series did not change:

Outch, now I see my mistake.

* The documentation of ``LaurentSeries.truncate`` states that indeed it returns a Laurent series. It does not have a doc test, so, I will add one.

* The old doc test of ``PowerSeries.truncate`` fails with my patch. The reason is that the *power* series constructed in this doc test is now in fact a *Laurent* series; this is what made me believe that the behaviour of the method has changed. So, I only have to change the doc test.

But before submitting a patch to add/correct these doc tests, I'll wait for input of a referee.



---

archive/issue_comments_082695.json:
```json
{
    "body": "Do you have any timings for power series sqrt()?",
    "created_at": "2010-05-18T06:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82695",
    "user": "robertwb"
}
```

Do you have any timings for power series sqrt()?



---

archive/issue_comments_082696.json:
```json
{
    "body": "Replying to [comment:13 robertwb]:\n> Do you have any timings for power series sqrt()? \n\nTentatively.\n\nWithout the patch:\n\n```\nsage: P.<t> = QQ[[]]\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)\nsage: p.sqrt()\n3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)\nsage: timeit('q = p.sqrt()')\n25 loops, best of 3: 13.3 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n25 loops, best of 3: 13.6 ms per loop\nsage: timeit('q = (p^4).sqrt()')\n25 loops, best of 3: 14.5 ms per loop\nsage: PZ = ZZ[['t']]\nsage: timeit('q = (PZ(p)^2).sqrt()')\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (27, 0))\n...\nTypeError: no conversion of this rational to integer\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9\nsage: timeit('q = p.sqrt()')\n25 loops, best of 3: 20.7 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n25 loops, best of 3: 21.9 ms per loop\n```\n\n\nWith the patch:\n\n```\nsage: P.<t> = QQ[[]]\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)\nsage: p.sqrt()\n3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)\nsage: timeit('q = p.sqrt()')\n25 loops, best of 3: 15.5 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n25 loops, best of 3: 15.7 ms per loop\nsage: timeit('q = (p^4).sqrt()')\n25 loops, best of 3: 16.6 ms per loop\nsage: PZ = ZZ[['t']]\nsage: timeit('q = (PZ(p)^2).sqrt()')\n25 loops, best of 3: 19.2 ms per loop\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9\nsage: timeit('q = p.sqrt()')\n25 loops, best of 3: 23.8 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n25 loops, best of 3: 24.5 ms per loop\n```\n\n\nSo, over QQ, there is a slight regression (both with exact and inexact input). Over ZZ, it only works with my patch, even for a polynomial that is quadratic by definition.\n\nI will have a closer look at sqrt - perhaps I'll find something.",
    "created_at": "2010-05-18T08:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82696",
    "user": "SimonKing"
}
```

Replying to [comment:13 robertwb]:
> Do you have any timings for power series sqrt()? 

Tentatively.

Without the patch:

```
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
25 loops, best of 3: 13.3 ms per loop
sage: timeit('q = (p^2).sqrt()')
25 loops, best of 3: 13.6 ms per loop
sage: timeit('q = (p^4).sqrt()')
25 loops, best of 3: 14.5 ms per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (27, 0))
...
TypeError: no conversion of this rational to integer
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
25 loops, best of 3: 20.7 ms per loop
sage: timeit('q = (p^2).sqrt()')
25 loops, best of 3: 21.9 ms per loop
```


With the patch:

```
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
25 loops, best of 3: 15.5 ms per loop
sage: timeit('q = (p^2).sqrt()')
25 loops, best of 3: 15.7 ms per loop
sage: timeit('q = (p^4).sqrt()')
25 loops, best of 3: 16.6 ms per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')
25 loops, best of 3: 19.2 ms per loop
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
25 loops, best of 3: 23.8 ms per loop
sage: timeit('q = (p^2).sqrt()')
25 loops, best of 3: 24.5 ms per loop
```


So, over QQ, there is a slight regression (both with exact and inexact input). Over ZZ, it only works with my patch, even for a polynomial that is quadratic by definition.

I will have a closer look at sqrt - perhaps I'll find something.



---

archive/issue_comments_082697.json:
```json
{
    "body": "Replying to [comment:14 SimonKing]:\n> I will have a closer look at sqrt - perhaps I'll find something.\n\nIt seems so. \n\nFirst, the reason why the old version failed for a power series over ZZ is the fact that the invert method raises an error if the result has coefficients in QQ rather than ZZ. I guess this must change.\n\nSecond, there is a division inside the sqrt method. By my patch, this division returns a Laurent series, which slows things slightly down. If I do ``a*s.__invert__()`` instead of ``a/s`` then the timings are as good as with the old code.\n\nSo, there will soon be a third patch...",
    "created_at": "2010-05-18T09:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82697",
    "user": "SimonKing"
}
```

Replying to [comment:14 SimonKing]:
> I will have a closer look at sqrt - perhaps I'll find something.

It seems so. 

First, the reason why the old version failed for a power series over ZZ is the fact that the invert method raises an error if the result has coefficients in QQ rather than ZZ. I guess this must change.

Second, there is a division inside the sqrt method. By my patch, this division returns a Laurent series, which slows things slightly down. If I do ``a*s.__invert__()`` instead of ``a/s`` then the timings are as good as with the old code.

So, there will soon be a third patch...



---

archive/issue_comments_082698.json:
```json
{
    "body": "Attachment [8972_power_series_sqrt_timing.patch](tarball://root/attachments/some-uuid/ticket8972/8972_power_series_sqrt_timing.patch) by SimonKing created at 2010-05-18 10:55:19\n\nImproving timings for sqrt, further bug fixes, more doc tests. To be applied after the two other patches",
    "created_at": "2010-05-18T10:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82698",
    "user": "SimonKing"
}
```

Attachment [8972_power_series_sqrt_timing.patch](tarball://root/attachments/some-uuid/ticket8972/8972_power_series_sqrt_timing.patch) by SimonKing created at 2010-05-18 10:55:19

Improving timings for sqrt, further bug fixes, more doc tests. To be applied after the two other patches



---

archive/issue_comments_082699.json:
```json
{
    "body": "It was worth it!\n\nFirst, I found one division bug for Laurent series left, which is now fixed (and doc tested):\n\n```\nsage: L.<x> = LaurentSeriesRing(ZZ)\nsage: 1/(2+x)\n1/2 - 1/4*x + 1/8*x^2 - 1/16*x^3 + 1/32*x^4 - 1/64*x^5 + 1/128*x^6 - 1/256*x^7 + 1/512*x^8 - 1/1024*x^9 + 1/2048*x^10 - 1/4096*x^11 + 1/8192*x^12 - 1/16384*x^13 + 1/32768*x^14 - 1/65536*x^15 + 1/131072*x^16 - 1/262144*x^17 + 1/524288*x^18 - 1/1048576*x^19 + O(x^20)\n```\n\nThis used to result in an error.\n\nSecond, I added more doc tests (and inserted my name to the author list).\n\nThird, the new timings for sqrt are fully competitive (even very slightly faster than before), and we still have the bug fix:\n\n```\nLoading Sage library. Current Mercurial branch is: powerseries\nsage: P.<t> = QQ[[]]\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)\nsage: p.sqrt()\n3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)\nsage: timeit('q = p.sqrt()')\n25 loops, best of 3: 13.2 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n25 loops, best of 3: 13.5 ms per loop\nsage: timeit('q = (p^4).sqrt()')\n25 loops, best of 3: 14.5 ms per loop\nsage: PZ = ZZ[['t']]\nsage: timeit('q = (PZ(p)^2).sqrt()')\n25 loops, best of 3: 16.4 ms per loop\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9\nsage: timeit('q = p.sqrt()')\n25 loops, best of 3: 20.6 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n25 loops, best of 3: 21.7 ms per loop\n```\n\n\nThe trick is that I do ``s*a.__invert__()`` instead of ``s/a``, where ``s`` and ``a`` are power series. This helps, because (after a little change) the invert method returns a power series whenever possible -- and since I know that ``a.valuation()>=0``, I can use fast multiplication of power series rather than slow multiplication of Laurent series.",
    "created_at": "2010-05-18T11:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82699",
    "user": "SimonKing"
}
```

It was worth it!

First, I found one division bug for Laurent series left, which is now fixed (and doc tested):

```
sage: L.<x> = LaurentSeriesRing(ZZ)
sage: 1/(2+x)
1/2 - 1/4*x + 1/8*x^2 - 1/16*x^3 + 1/32*x^4 - 1/64*x^5 + 1/128*x^6 - 1/256*x^7 + 1/512*x^8 - 1/1024*x^9 + 1/2048*x^10 - 1/4096*x^11 + 1/8192*x^12 - 1/16384*x^13 + 1/32768*x^14 - 1/65536*x^15 + 1/131072*x^16 - 1/262144*x^17 + 1/524288*x^18 - 1/1048576*x^19 + O(x^20)
```

This used to result in an error.

Second, I added more doc tests (and inserted my name to the author list).

Third, the new timings for sqrt are fully competitive (even very slightly faster than before), and we still have the bug fix:

```
Loading Sage library. Current Mercurial branch is: powerseries
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
25 loops, best of 3: 13.2 ms per loop
sage: timeit('q = (p^2).sqrt()')
25 loops, best of 3: 13.5 ms per loop
sage: timeit('q = (p^4).sqrt()')
25 loops, best of 3: 14.5 ms per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')
25 loops, best of 3: 16.4 ms per loop
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
25 loops, best of 3: 20.6 ms per loop
sage: timeit('q = (p^2).sqrt()')
25 loops, best of 3: 21.7 ms per loop
```


The trick is that I do ``s*a.__invert__()`` instead of ``s/a``, where ``s`` and ``a`` are power series. This helps, because (after a little change) the invert method returns a power series whenever possible -- and since I know that ``a.valuation()>=0``, I can use fast multiplication of power series rather than slow multiplication of Laurent series.



---

archive/issue_comments_082700.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-18T11:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82700",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082701.json:
```json
{
    "body": "O dear, I have to mark it \"needs work\", because the following fails:\n\n```\nsage: R.<x> = ZZ[[]]\nsage: y = (3*x+2)/(1+x)\nsage: y=y/x\n```\n",
    "created_at": "2010-05-18T11:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82701",
    "user": "SimonKing"
}
```

O dear, I have to mark it "needs work", because the following fails:

```
sage: R.<x> = ZZ[[]]
sage: y = (3*x+2)/(1+x)
sage: y=y/x
```




---

archive/issue_comments_082702.json:
```json
{
    "body": "Attachment [8972_laurent_div_fix.patch](tarball://root/attachments/some-uuid/ticket8972/8972_laurent_div_fix.patch) by SimonKing created at 2010-05-18 12:00:35\n\nBugfix for LaurentSeries._div_; to be applied after the other three patches",
    "created_at": "2010-05-18T12:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82702",
    "user": "SimonKing"
}
```

Attachment [8972_laurent_div_fix.patch](tarball://root/attachments/some-uuid/ticket8972/8972_laurent_div_fix.patch) by SimonKing created at 2010-05-18 12:00:35

Bugfix for LaurentSeries._div_; to be applied after the other three patches



---

archive/issue_comments_082703.json:
```json
{
    "body": "Replying to [comment:17 SimonKing]:\n> sage: y=y/x\n\nOK, the last (hopefully the last...) patch fixes this. I was verifying the timings for basic arithmetic (the timings without patches are posted above), and here is the positive result:\n\n```\nsage: R.<x> = ZZ[[]]\nsage: timeit('a=1/x')\n625 loops, best of 3: 218 \u00b5s per loop\nsage: timeit('a=(1+x)/x')\n625 loops, best of 3: 228 \u00b5s per loop\nsage: timeit('a=1/(1+x)')\n625 loops, best of 3: 1.22 ms per loop\nsage: timeit('a=(1+x)/(1-x)')\n625 loops, best of 3: 1.24 ms per loop\nsage: y = (3*x+2)/(1+x)\nsage: y=y/x\nsage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)\nsage: z=y/x\nsage: timeit('y+z')\n625 loops, best of 3: 189 \u00b5s per loop\nsage: timeit('y*z')\n625 loops, best of 3: 92.6 \u00b5s per loop\nsage: timeit('y-z')\n625 loops, best of 3: 189 \u00b5s per loop\nsage: timeit('y/z')\n125 loops, best of 3: 7.1 ms per loop\n```\n\n\nNow, ready for review, and I'll do something else...",
    "created_at": "2010-05-18T12:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82703",
    "user": "SimonKing"
}
```

Replying to [comment:17 SimonKing]:
> sage: y=y/x

OK, the last (hopefully the last...) patch fixes this. I was verifying the timings for basic arithmetic (the timings without patches are posted above), and here is the positive result:

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/x')
625 loops, best of 3: 218 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 228 µs per loop
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 1.22 ms per loop
sage: timeit('a=(1+x)/(1-x)')
625 loops, best of 3: 1.24 ms per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 189 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 92.6 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 189 µs per loop
sage: timeit('y/z')
125 loops, best of 3: 7.1 ms per loop
```


Now, ready for review, and I'll do something else...



---

archive/issue_comments_082704.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-18T12:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82704",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082705.json:
```json
{
    "body": "Minor cosmetic changes, apply on top of previous.",
    "created_at": "2010-05-25T06:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82705",
    "user": "robertwb"
}
```

Minor cosmetic changes, apply on top of previous.



---

archive/issue_comments_082706.json:
```json
{
    "body": "Attachment [8972-referee.patch](tarball://root/attachments/some-uuid/ticket8972/8972-referee.patch) by robertwb created at 2010-05-25 06:40:43\n\nNice work. Apply all 5 patches.",
    "created_at": "2010-05-25T06:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82706",
    "user": "robertwb"
}
```

Attachment [8972-referee.patch](tarball://root/attachments/some-uuid/ticket8972/8972-referee.patch) by robertwb created at 2010-05-25 06:40:43

Nice work. Apply all 5 patches.



---

archive/issue_comments_082707.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-25T06:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82707",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082708.json:
```json
{
    "body": "The reviewer field was not filled in. I just added it. \n\nDave",
    "created_at": "2010-06-05T08:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82708",
    "user": "drkirkby"
}
```

The reviewer field was not filled in. I just added it. 

Dave



---

archive/issue_comments_082709.json:
```json
{
    "body": "Sorry about the spelling mistake!",
    "created_at": "2010-06-05T10:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82709",
    "user": "drkirkby"
}
```

Sorry about the spelling mistake!



---

archive/issue_comments_082710.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82710",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_082711.json:
```json
{
    "body": "I had to back these patches out since they caused lots of errors in schemes/elliptic_curves.",
    "created_at": "2010-06-06T08:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82711",
    "user": "mhansen"
}
```

I had to back these patches out since they caused lots of errors in schemes/elliptic_curves.



---

archive/issue_comments_082712.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-06-06T08:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82712",
    "user": "mhansen"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_082713.json:
```json
{
    "body": "Hi Mike!\n\nThat probably means that the elliptic curves code expects the result of a division of two power series to be another power series. But now, the division yields a Laurent series.\n\nI see two possibilities to proceed:\n\n1. Search for all occurences of power series in Sage, see if a division occurs, and change it so that things still work.\n2. Change/extend the methods provided by Laurent series so that they match those provided by power series. In that way, the code in schemes/elliptic_curves still has a chance to work.\n\nI'll see what I can do.\n\nBest regards,\nSimon",
    "created_at": "2010-06-06T12:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82713",
    "user": "SimonKing"
}
```

Hi Mike!

That probably means that the elliptic curves code expects the result of a division of two power series to be another power series. But now, the division yields a Laurent series.

I see two possibilities to proceed:

1. Search for all occurences of power series in Sage, see if a division occurs, and change it so that things still work.
2. Change/extend the methods provided by Laurent series so that they match those provided by power series. In that way, the code in schemes/elliptic_curves still has a chance to work.

I'll see what I can do.

Best regards,
Simon



---

archive/issue_comments_082714.json:
```json
{
    "body": "I think the problem boils down to two problems:\n\n1. Laurent series have no attribute ``exp``, unlike power series.\n\n2. In some situations, there still occurs a formal fraction field when it should be a Laurent series ring. The result is an attribute error.\n\nFor the first situation, I suggest to implement ``exp`` for Laurent series of non-negative valuation (using exp of the underlying power series). For the second situation, I have to analyse what goes wrong.",
    "created_at": "2010-06-06T15:20:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82714",
    "user": "SimonKing"
}
```

I think the problem boils down to two problems:

1. Laurent series have no attribute ``exp``, unlike power series.

2. In some situations, there still occurs a formal fraction field when it should be a Laurent series ring. The result is an attribute error.

For the first situation, I suggest to implement ``exp`` for Laurent series of non-negative valuation (using exp of the underlying power series). For the second situation, I have to analyse what goes wrong.



---

archive/issue_comments_082715.json:
```json
{
    "body": "The problem is that some code *expects* the fraction field of a power series ring to be a formal fraction field. So, assume that one changes it, so that the fraction field is in fact a Laurent polynomial ring. When creating elements of the fraction field, the code fails, because it tries to initialise the element by numerator and denominator -- but Laurent series are initialised by a power series and an integer.\n\nA possible solution would be to make the init method of Laurent series accept numerator and denominator. But I think that's a nasty hack, because what happens if the arguments are one power series and one integer? Is the integer supposed to be the valuation of the Laurent series, or the denominator of a formal fraction field element?",
    "created_at": "2010-06-06T17:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82715",
    "user": "SimonKing"
}
```

The problem is that some code *expects* the fraction field of a power series ring to be a formal fraction field. So, assume that one changes it, so that the fraction field is in fact a Laurent polynomial ring. When creating elements of the fraction field, the code fails, because it tries to initialise the element by numerator and denominator -- but Laurent series are initialised by a power series and an integer.

A possible solution would be to make the init method of Laurent series accept numerator and denominator. But I think that's a nasty hack, because what happens if the arguments are one power series and one integer? Is the integer supposed to be the valuation of the Laurent series, or the denominator of a formal fraction field element?



---

archive/issue_comments_082716.json:
```json
{
    "body": "It is really frustrating how many doc tests fail. I solved the problem with ``exp`` and one other attribute error. But there remain many problems: `ZeroDivisionError`, wrong precision of the result (!), and so on.",
    "created_at": "2010-06-06T20:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82716",
    "user": "SimonKing"
}
```

It is really frustrating how many doc tests fail. I solved the problem with ``exp`` and one other attribute error. But there remain many problems: `ZeroDivisionError`, wrong precision of the result (!), and so on.



---

archive/issue_comments_082717.json:
```json
{
    "body": "In most cases, the problems seem to come from using `f/g` on power series in situations where `g` is of valuation zero. This used to return a power series, which I consider the wrong answer (it should be a Laurent series). Now, if one wants `f/g` as a power series, one should use `f * ~g` instead.\n\nI am now confident that I'll soon be able to submit another patch that resolves it.",
    "created_at": "2010-06-07T00:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82717",
    "user": "SimonKing"
}
```

In most cases, the problems seem to come from using `f/g` on power series in situations where `g` is of valuation zero. This used to return a power series, which I consider the wrong answer (it should be a Laurent series). Now, if one wants `f/g` as a power series, one should use `f * ~g` instead.

I am now confident that I'll soon be able to submit another patch that resolves it.



---

archive/issue_comments_082718.json:
```json
{
    "body": "After fixing what I mentioned above, I get for `sage -testall`:\n\n```\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/crypto/lfsr.py\"\n        sage -t  \"devel/sage/sage/modular/modform/find_generators.py\"\n        sage -t  \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\"\n```\n\n\nThis seems doable.\n\nPerhaps I was too strict when I implemented `_div_`: I wanted that the result *always* lives in the fraction field, and I wanted that an error is raised if no fraction field exists. But I guess it is better to proceed as it is known from other rings that are no integral domains:\n\n```\nsage: K = ZZ.quo(15)\nsage: parent(K(3)/K(4))\nRing of integers modulo 15\nsage: parent(K(4)/K(3))\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n...\nZeroDivisionError: Inverse does not exist.\n```\n\n\nSo, rule:\n\n1. *If* a fraction field exists then the result of a division must live in it (example: 1/1 is a rational, not an integer).\n2. If no fraction field exists, then devision shall yield an element of the original ring, if that's possible, and raise a `ZeroDivisionError` otherwise.",
    "created_at": "2010-06-07T09:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82718",
    "user": "SimonKing"
}
```

After fixing what I mentioned above, I get for `sage -testall`:

```
The following tests failed:


        sage -t  "devel/sage/sage/crypto/lfsr.py"
        sage -t  "devel/sage/sage/modular/modform/find_generators.py"
        sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
```


This seems doable.

Perhaps I was too strict when I implemented `_div_`: I wanted that the result *always* lives in the fraction field, and I wanted that an error is raised if no fraction field exists. But I guess it is better to proceed as it is known from other rings that are no integral domains:

```
sage: K = ZZ.quo(15)
sage: parent(K(3)/K(4))
Ring of integers modulo 15
sage: parent(K(4)/K(3))
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
...
ZeroDivisionError: Inverse does not exist.
```


So, rule:

1. *If* a fraction field exists then the result of a division must live in it (example: 1/1 is a rational, not an integer).
2. If no fraction field exists, then devision shall yield an element of the original ring, if that's possible, and raise a `ZeroDivisionError` otherwise.



---

archive/issue_comments_082719.json:
```json
{
    "body": "Fixing some remaining bugs of Laurent/power series arithmetic; fixing doc tests on elliptic curves.",
    "created_at": "2010-06-07T18:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82719",
    "user": "SimonKing"
}
```

Fixing some remaining bugs of Laurent/power series arithmetic; fixing doc tests on elliptic curves.



---

archive/issue_comments_082720.json:
```json
{
    "body": "Attachment [8972_elliptic_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket8972/8972_elliptic_doctest_fix.patch) by SimonKing created at 2010-06-07 18:55:23\n\nI think the problems are now solved. With the last patch, that is to be applied after all others, `sage -testall` works without errors (at least in version sage-4.4.2).\n\n**__Changes introduced by the patch__**\n\n* In some cases, if the code expects a power series, I replaced `a/b` for power series `a,b` by `a*~b`. Namely, the latter returns a power series (not a Laurent series), if possible. \n\n* I added a method `exp` for Laurent series, that returns the exponential if the Laurent series happens to be a power series.\n\n* With my previous patches, the underlying data of a Laurent series is not necessarily a power series. Therefore `add_bigoh` (similarly `_rmul_` and `_lmul_`) did in some cases not work. This is now fixed and doctested.\n\n* Some Power Series Rings still returned a *formal* fraction field. This is now fixed, they return a Laurent series ring.\n\n* If `a,b` are elements of a power series ring `R`, the rule is now:\n\n  1. If `R` is an integral domain, then `a/b` always belongs to `Frac(R)`. This is similar to `1/1` being rational, not integer.\n\n  2. If `R` is no integral domain, then `a/b` is an element of `R` or of the Laurent series ring over the base ring of `R`, if `b` is invertible. This is similar to division in `ZZ.quo(15)`.\n\n  3. If possible, `~b` is a power series (possibly over the fraction field of the base of `R`). So, we always have `~b==1/b`, but the parents may be different. I hope this is acceptable.\n\n* A change in the default `_div_` method of `RingElement`: Previously, the default for `a._div_(b)` was to return `a.parent().fraction_field()(a,b)`. But this may be a problem (e.g., if the fraction field is not a formal fraction field but a Laurent series ring). Therefore, if the old default results in an error, `a.parent().fraction_field(a)/a.parent().fraction_field(b)` is tried.\n\n**__Timings__**\n\nRobert was worried about potential slowdowns in the Monsky-Washnitzer code. It seems to me that my patches actually provide a considerably speedup.\n\nWithout my patches:\n\n```\nsage -t  \"devel/sage-powerseries/sage/schemes/elliptic_curves/monsky_washnitzer.py\"\n         [3.9 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 3.9 seconds\n```\n\n\nWith my patches:\n\n```\nsage -t  \"devel/sage-powerseries/sage/schemes/elliptic_curves/monsky_washnitzer.py\"\n         [2.3 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 2.3 seconds\n```\n\n\nSo, the code seems to become faster by more than 33%!\n\nReady for review again...",
    "created_at": "2010-06-07T18:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82720",
    "user": "SimonKing"
}
```

Attachment [8972_elliptic_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket8972/8972_elliptic_doctest_fix.patch) by SimonKing created at 2010-06-07 18:55:23

I think the problems are now solved. With the last patch, that is to be applied after all others, `sage -testall` works without errors (at least in version sage-4.4.2).

**__Changes introduced by the patch__**

* In some cases, if the code expects a power series, I replaced `a/b` for power series `a,b` by `a*~b`. Namely, the latter returns a power series (not a Laurent series), if possible. 

* I added a method `exp` for Laurent series, that returns the exponential if the Laurent series happens to be a power series.

* With my previous patches, the underlying data of a Laurent series is not necessarily a power series. Therefore `add_bigoh` (similarly `_rmul_` and `_lmul_`) did in some cases not work. This is now fixed and doctested.

* Some Power Series Rings still returned a *formal* fraction field. This is now fixed, they return a Laurent series ring.

* If `a,b` are elements of a power series ring `R`, the rule is now:

  1. If `R` is an integral domain, then `a/b` always belongs to `Frac(R)`. This is similar to `1/1` being rational, not integer.

  2. If `R` is no integral domain, then `a/b` is an element of `R` or of the Laurent series ring over the base ring of `R`, if `b` is invertible. This is similar to division in `ZZ.quo(15)`.

  3. If possible, `~b` is a power series (possibly over the fraction field of the base of `R`). So, we always have `~b==1/b`, but the parents may be different. I hope this is acceptable.

* A change in the default `_div_` method of `RingElement`: Previously, the default for `a._div_(b)` was to return `a.parent().fraction_field()(a,b)`. But this may be a problem (e.g., if the fraction field is not a formal fraction field but a Laurent series ring). Therefore, if the old default results in an error, `a.parent().fraction_field(a)/a.parent().fraction_field(b)` is tried.

**__Timings__**

Robert was worried about potential slowdowns in the Monsky-Washnitzer code. It seems to me that my patches actually provide a considerably speedup.

Without my patches:

```
sage -t  "devel/sage-powerseries/sage/schemes/elliptic_curves/monsky_washnitzer.py"
         [3.9 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.9 seconds
```


With my patches:

```
sage -t  "devel/sage-powerseries/sage/schemes/elliptic_curves/monsky_washnitzer.py"
         [2.3 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2.3 seconds
```


So, the code seems to become faster by more than 33%!

Ready for review again...



---

archive/issue_comments_082721.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-07T18:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82721",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082722.json:
```json
{
    "body": "I upgraded to sage-4.4.3.\n\nI verified that all patches still apply.\n\nWith the patches, `sage -testall` passes.\n\nOn sage-devel, Robert asked how stable my Monsky-Washnitzer timing is. Here is the answer:\n\nWithout the patches, I was running `sage -t  \"devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py\"` 5 times, and got\n \n  7.9 s, 2.4 s, 2.4 s, 2.4 s, 2.4 s\n\nWith the patches, I obtain\n\n  2.4 s, 2.5 s, 2.4 s, 2.4 s, 2.4 s\n\nSo, the timing did not improve, except for the first run. But at least there was no slowdown.",
    "created_at": "2010-06-07T21:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82722",
    "user": "SimonKing"
}
```

I upgraded to sage-4.4.3.

I verified that all patches still apply.

With the patches, `sage -testall` passes.

On sage-devel, Robert asked how stable my Monsky-Washnitzer timing is. Here is the answer:

Without the patches, I was running `sage -t  "devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py"` 5 times, and got
 
  7.9 s, 2.4 s, 2.4 s, 2.4 s, 2.4 s

With the patches, I obtain

  2.4 s, 2.5 s, 2.4 s, 2.4 s, 2.4 s

So, the timing did not improve, except for the first run. But at least there was no slowdown.



---

archive/issue_comments_082723.json:
```json
{
    "body": "Accidentally, I found that this ticket is rotting.\n\nRecall that it used to be \"fixed\", but then it was reopened by mhansen, since there was a problem in sage-4.4.alpha0. Subsequently, I fixed these problems, but still the resolution is set to \"fixed\".\n\nI guess this is why nobody took care of the ticket afterwards.\n\nI don't know if the patch would still apply (probably not), but at least I verified that the original problem did not disappear.",
    "created_at": "2010-11-30T07:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82723",
    "user": "SimonKing"
}
```

Accidentally, I found that this ticket is rotting.

Recall that it used to be "fixed", but then it was reopened by mhansen, since there was a problem in sage-4.4.alpha0. Subsequently, I fixed these problems, but still the resolution is set to "fixed".

I guess this is why nobody took care of the ticket afterwards.

I don't know if the patch would still apply (probably not), but at least I verified that the original problem did not disappear.



---

archive/issue_comments_082724.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-11-30T09:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82724",
    "user": "mvngu"
}
```

Changing status from closed to new.



---

archive/issue_comments_082725.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-11-30T09:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82725",
    "user": "mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_082726.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-30T09:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82726",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082727.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-08T03:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82727",
    "user": "gagansekhon"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082728.json:
```json
{
    "body": "test of sage/modular/modform/find_generators.py failed. \n\n```\n./sage -t sage/modular/modform/find_generators.py\nsage -t  \"devel/sage-main/sage/modular/modform/find_generators.py\"\n**********************************************************************\nFile \"/Applications/sage4.6/devel/sage-main/sage/modular/modform/find_generators.py\", line 74:\n    sage: span_of_series(v)\nException raised:\n    Traceback (most recent call last):\n      File \"/Applications/sage4.6/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Applications/sage4.6/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Applications/sage4.6/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[8]>\", line 1, in <module>\n        span_of_series(v)###line 74:\n    sage: span_of_series(v)\n      File \"/Applications/sage4.6/local/lib/python/site-packages/sage/modular/modform/find_generators.py\", line 116, in span_of_series\n        B = [V(g.padded_list(n)) for g in v]\n      File \"element.pyx\", line 306, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2666)\n      File \"parent.pyx\", line 272, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2840)\n      File \"parent.pyx\", line 170, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2611)\n    AttributeError: 'sage.rings.laurent_series_ring_element.LaurentSeries' object has no attribute 'padded_list'\n**********************************************************************\nFile \"/Applications/sage4.6/devel/sage-main/sage/modular/modform/find_generators.py\", line 79:\n    sage: span_of_series(v,10)\nException raised:\n    Traceback (most recent call last):\n      File \"/Applications/sage4.6/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Applications/sage4.6/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Applications/sage4.6/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[9]>\", line 1, in <module>\n        span_of_series(v,Integer(10))###line 79:\n    sage: span_of_series(v,10)\n      File \"/Applications/sage4.6/local/lib/python/site-packages/sage/modular/modform/find_generators.py\", line 116, in span_of_series\n        B = [V(g.padded_list(n)) for g in v]\n      File \"element.pyx\", line 306, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2666)\n      File \"parent.pyx\", line 272, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2840)\n      File \"parent.pyx\", line 170, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2611)\n    AttributeError: 'sage.rings.laurent_series_ring_element.LaurentSeries' object has no attribute 'padded_list'\n**********************************************************************\n1 items had failures:\n   2 of  14 in __main__.example_1\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /Users/sekhon/.sage//tmp/.doctest_find_generators.py\n\t [4.0 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"devel/sage-main/sage/modular/modform/find_generators.py\"\nTotal time for all tests: 4.0 seconds\n```\n",
    "created_at": "2011-01-08T03:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82728",
    "user": "gagansekhon"
}
```

test of sage/modular/modform/find_generators.py failed. 

```
./sage -t sage/modular/modform/find_generators.py
sage -t  "devel/sage-main/sage/modular/modform/find_generators.py"
**********************************************************************
File "/Applications/sage4.6/devel/sage-main/sage/modular/modform/find_generators.py", line 74:
    sage: span_of_series(v)
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage4.6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage4.6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage4.6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[8]>", line 1, in <module>
        span_of_series(v)###line 74:
    sage: span_of_series(v)
      File "/Applications/sage4.6/local/lib/python/site-packages/sage/modular/modform/find_generators.py", line 116, in span_of_series
        B = [V(g.padded_list(n)) for g in v]
      File "element.pyx", line 306, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2666)
      File "parent.pyx", line 272, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2840)
      File "parent.pyx", line 170, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2611)
    AttributeError: 'sage.rings.laurent_series_ring_element.LaurentSeries' object has no attribute 'padded_list'
**********************************************************************
File "/Applications/sage4.6/devel/sage-main/sage/modular/modform/find_generators.py", line 79:
    sage: span_of_series(v,10)
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage4.6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage4.6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage4.6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[9]>", line 1, in <module>
        span_of_series(v,Integer(10))###line 79:
    sage: span_of_series(v,10)
      File "/Applications/sage4.6/local/lib/python/site-packages/sage/modular/modform/find_generators.py", line 116, in span_of_series
        B = [V(g.padded_list(n)) for g in v]
      File "element.pyx", line 306, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2666)
      File "parent.pyx", line 272, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2840)
      File "parent.pyx", line 170, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2611)
    AttributeError: 'sage.rings.laurent_series_ring_element.LaurentSeries' object has no attribute 'padded_list'
**********************************************************************
1 items had failures:
   2 of  14 in __main__.example_1
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/sekhon/.sage//tmp/.doctest_find_generators.py
	 [4.0 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main/sage/modular/modform/find_generators.py"
Total time for all tests: 4.0 seconds
```




---

archive/issue_comments_082729.json:
```json
{
    "body": "'''\nApply trac-8972_fraction_of_power_series_combined.patch\n\n(for the patchbot)",
    "created_at": "2011-02-18T08:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82729",
    "user": "SimonKing"
}
```

'''
Apply trac-8972_fraction_of_power_series_combined.patch

(for the patchbot)



---

archive/issue_comments_082730.json:
```json
{
    "body": "For simplicity, I produced a patch that combines all previous patches and is rebased to sage-4.6.2.alpha4.\n\nI will now try to take care about the failing doc tests.",
    "created_at": "2011-02-18T08:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82730",
    "user": "SimonKing"
}
```

For simplicity, I produced a patch that combines all previous patches and is rebased to sage-4.6.2.alpha4.

I will now try to take care about the failing doc tests.



---

archive/issue_comments_082731.json:
```json
{
    "body": "I managed to fix the remaining issues, and all tests pass (unless a last minute change that I just did was a bad idea). Hence, this ticket needs review again. \n\nSince the computation time was a point of critique, let me give you some timings:\n\nWithout the patch:\n\n```\n# Basic arithmetic\nsage: R.<x> = ZZ[[]]\nsage: timeit('a=1/(1+x)')\n625 loops, best of 3: 803 \u00b5s per loop\nsage: timeit('a=1/x')\n625 loops, best of 3: 279 \u00b5s per loop\nsage: timeit('a=(1+x)/x')\n625 loops, best of 3: 285 \u00b5s per loop\nsage: timeit('a=1/(1+x)')\n625 loops, best of 3: 801 \u00b5s per loop\nsage: y = (3*x+2)/(1+x)\nsage: y=y/x\nsage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)\nsage: z=y/x\nsage: timeit('y+z')\n625 loops, best of 3: 167 \u00b5s per loop\nsage: timeit('y*z')\n625 loops, best of 3: 100 \u00b5s per loop\nsage: timeit('y-z')\n625 loops, best of 3: 166 \u00b5s per loop\n\n# square roots\nsage: P.<t> = QQ[[]]\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)\nsage: p.sqrt()\n3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)\nsage: timeit('q = p.sqrt()')\n625 loops, best of 3: 767 \u00b5s per loop\nsage: timeit('q = (p^2).sqrt()')\n625 loops, best of 3: 791 \u00b5s per loop\nsage: timeit('q = (p^4).sqrt()')\n625 loops, best of 3: 828 \u00b5s per loop\nsage: PZ = ZZ[['t']]\nsage: timeit('q = (PZ(p)^2).sqrt()')\n<BOOM>\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9\nsage: timeit('q = p.sqrt()')\n625 loops, best of 3: 1 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n625 loops, best of 3: 1.04 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n625 loops, best of 3: 1.04 ms per loop\n```\n\n\nWith the patch:\n\n```\n# Basic arithmetic\nsage: R.<x> = ZZ[[]]\nsage: timeit('a=1/(1+x)')\n625 loops, best of 3: 897 \u00b5s per loop\nsage: timeit('a=1/x')\n625 loops, best of 3: 173 \u00b5s per loop\nsage: timeit('a=(1+x)/x')\n625 loops, best of 3: 179 \u00b5s per loop\nsage: timeit('a=1/(1+x)')\n625 loops, best of 3: 911 \u00b5s per loop\nsage: timeit('a=(1+x)/(1-x)')\n625 loops, best of 3: 900 \u00b5s per loop\nsage: y = (3*x+2)/(1+x)\nsage: y=y/x\nsage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)\nsage: z=y/x\nsage: timeit('y+z')\n625 loops, best of 3: 38.4 \u00b5s per loop\nsage: timeit('y*z')\n625 loops, best of 3: 23.6 \u00b5s per loop\nsage: timeit('y-z')\n625 loops, best of 3: 23.6 \u00b5s per loop\nsage: timeit('y/z')\n625 loops, best of 3: 309 \u00b5s per loop\n\n# square roots\nsage: P.<t> = QQ[[]]\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)\nsage: p.sqrt()\n3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)\nsage: timeit('q = p.sqrt()')\n625 loops, best of 3: 938 \u00b5s per loop\nsage: timeit('q = (p^2).sqrt()')\n625 loops, best of 3: 962 \u00b5s per loop\nsage: timeit('q = (p^4).sqrt()')\n625 loops, best of 3: 1 ms per loop\nsage: PZ = ZZ[['t']]\nsage: timeit('q = (PZ(p)^2).sqrt()')\n125 loops, best of 3: 2.39 ms per loop\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9\nsage: timeit('q = p.sqrt()')\n625 loops, best of 3: 1.22 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n625 loops, best of 3: 1.26 ms per loop\n```\n\n\nSo, in some cases the patch brings a big speedup (such as 38.4 \u00b5s versus 167 \u00b5s), in other cases it brings a mild slowdown (such as 962 \u00b5s versus 791 \u00b5s)\n\nObvious question to the referee: Should I try to squeeze even more \u00b5s out of it, or can it stay as it is (assuming that the long tests pass, as I will try now).",
    "created_at": "2011-02-18T13:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82731",
    "user": "SimonKing"
}
```

I managed to fix the remaining issues, and all tests pass (unless a last minute change that I just did was a bad idea). Hence, this ticket needs review again. 

Since the computation time was a point of critique, let me give you some timings:

Without the patch:

```
# Basic arithmetic
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 803 µs per loop
sage: timeit('a=1/x')
625 loops, best of 3: 279 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 285 µs per loop
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 801 µs per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 167 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 100 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 166 µs per loop

# square roots
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 767 µs per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 791 µs per loop
sage: timeit('q = (p^4).sqrt()')
625 loops, best of 3: 828 µs per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')
<BOOM>
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 1 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.04 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.04 ms per loop
```


With the patch:

```
# Basic arithmetic
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 897 µs per loop
sage: timeit('a=1/x')
625 loops, best of 3: 173 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 179 µs per loop
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 911 µs per loop
sage: timeit('a=(1+x)/(1-x)')
625 loops, best of 3: 900 µs per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 38.4 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 23.6 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 23.6 µs per loop
sage: timeit('y/z')
625 loops, best of 3: 309 µs per loop

# square roots
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 938 µs per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 962 µs per loop
sage: timeit('q = (p^4).sqrt()')
625 loops, best of 3: 1 ms per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')
125 loops, best of 3: 2.39 ms per loop
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 1.22 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.26 ms per loop
```


So, in some cases the patch brings a big speedup (such as 38.4 µs versus 167 µs), in other cases it brings a mild slowdown (such as 962 µs versus 791 µs)

Obvious question to the referee: Should I try to squeeze even more µs out of it, or can it stay as it is (assuming that the long tests pass, as I will try now).



---

archive/issue_comments_082732.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-18T13:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82732",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082733.json:
```json
{
    "body": "FWIW: Long tests pass.",
    "created_at": "2011-02-18T13:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82733",
    "user": "SimonKing"
}
```

FWIW: Long tests pass.



---

archive/issue_comments_082734.json:
```json
{
    "body": "Apply trac-8972_fraction_of_power_series_combined.patch",
    "created_at": "2011-02-18T14:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82734",
    "user": "SimonKing"
}
```

Apply trac-8972_fraction_of_power_series_combined.patch



---

archive/issue_comments_082735.json:
```json
{
    "body": "Don't be irritated by the patchbot. The patch is for 4.6.2.alpha4, not for 4.6.1",
    "created_at": "2011-02-18T14:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82735",
    "user": "SimonKing"
}
```

Don't be irritated by the patchbot. The patch is for 4.6.2.alpha4, not for 4.6.1



---

archive/issue_comments_082736.json:
```json
{
    "body": "This fails to apply against 4.7, so more rebasing is needed.\n\n```\ncd \"/home/kedlaya/Downloads/sage-4.7/devel/sage\" && hg import   \"/home/kedlaya/Downloads/trac-8972_fraction_of_power_series_combined.patch\"\napplying /home/kedlaya/Downloads/trac-8972_fraction_of_power_series_combined.patch\npatching file sage/modular/overconvergent/genus0.py\nHunk #1 FAILED at 1653\n1 out of 1 hunks FAILED -- saving rejects to file sage/modular/overconvergent/genus0.py.rej\npatching file sage/rings/power_series_poly.pyx\nHunk #4 FAILED at 843\nHunk #5 succeeded at 876 with fuzz 2 (offset 11 lines).\n1 out of 5 hunks FAILED -- saving rejects to file sage/rings/power_series_poly.pyx.rej\npatching file sage/rings/power_series_ring_element.pyx\nHunk #11 FAILED at 1771\nHunk #12 FAILED at 1783\n2 out of 12 hunks FAILED -- saving rejects to file sage/rings/power_series_ring_element.pyx.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2011-06-17T15:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82736",
    "user": "kedlaya"
}
```

This fails to apply against 4.7, so more rebasing is needed.

```
cd "/home/kedlaya/Downloads/sage-4.7/devel/sage" && hg import   "/home/kedlaya/Downloads/trac-8972_fraction_of_power_series_combined.patch"
applying /home/kedlaya/Downloads/trac-8972_fraction_of_power_series_combined.patch
patching file sage/modular/overconvergent/genus0.py
Hunk #1 FAILED at 1653
1 out of 1 hunks FAILED -- saving rejects to file sage/modular/overconvergent/genus0.py.rej
patching file sage/rings/power_series_poly.pyx
Hunk #4 FAILED at 843
Hunk #5 succeeded at 876 with fuzz 2 (offset 11 lines).
1 out of 5 hunks FAILED -- saving rejects to file sage/rings/power_series_poly.pyx.rej
patching file sage/rings/power_series_ring_element.pyx
Hunk #11 FAILED at 1771
Hunk #12 FAILED at 1783
2 out of 12 hunks FAILED -- saving rejects to file sage/rings/power_series_ring_element.pyx.rej
abort: patch failed to apply
```




---

archive/issue_comments_082737.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-17T15:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82737",
    "user": "kedlaya"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082738.json:
```json
{
    "body": "Remove assignee AlexGhitza.",
    "created_at": "2012-03-29T14:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82738",
    "user": "SimonKing"
}
```

Remove assignee AlexGhitza.



---

archive/issue_comments_082739.json:
```json
{
    "body": "Apparently the trac is locked in \"bold face mode\". Trying to ''' change it.",
    "created_at": "2012-03-29T14:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82739",
    "user": "SimonKing"
}
```

Apparently the trac is locked in "bold face mode". Trying to ''' change it.



---

archive/issue_comments_082740.json:
```json
{
    "body": "Attachment [trac-8972_fraction_of_power_series_combined.patch](tarball://root/attachments/some-uuid/ticket8972/trac-8972_fraction_of_power_series_combined.patch) by SimonKing created at 2012-03-29 14:45:39\n\nReplaces all previous patches",
    "created_at": "2012-03-29T14:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82740",
    "user": "SimonKing"
}
```

Attachment [trac-8972_fraction_of_power_series_combined.patch](tarball://root/attachments/some-uuid/ticket8972/trac-8972_fraction_of_power_series_combined.patch) by SimonKing created at 2012-03-29 14:45:39

Replaces all previous patches



---

archive/issue_comments_082741.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-29T14:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82741",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082742.json:
```json
{
    "body": "I have rebased the patch. The test suite needs to be run, but the patch should now apply to sage-5.0.beta10. Here is some supporting evidence:\n\n**__First section: The bugs to be fixed__**\n\n*sage-5.0.beta10-gcc without the patch*\n\n```\nsage: R.<x> = ZZ[[]]\nsage: (1/x).parent()  # bug\nLaurent Series Ring in x over Integer Ring\nsage: (x/x).parent()  # bug\nPower Series Ring in x over Integer Ring\nsage: (1/(2*x)).parent()  # bug\nTraceback (most recent call last):\n...\nTypeError: no conversion of this rational to integer\nsage: F = FractionField(R)\nsage: 1/x in F    # bug\nFalse\nsage: F           # I think a Laurent series ring would be better\nFraction Field of Power Series Ring in x over Integer Ring\nsage: F(x)\nx\nsage: ~F(x)   # was a problem with an early form of my patches.\n1/x\n```\n\n\n*sage-5.0.beta10-gcc with the patch*\n\n```\nage: R.<x> = ZZ[[]]\nsage: (1/x).parent()   # bug fixed\nLaurent Series Ring in x over Rational Field\nsage: (x/x).parent()   # bug fixed\nLaurent Series Ring in x over Rational Field\nsage: (1/(2*x)).parent() # bug fixed\nLaurent Series Ring in x over Rational Field\nsage: F = FractionField(R)\nsage: 1/x in F         # bug fixed\nTrue\nsage: F                # I think that's much better!\nLaurent Series Ring in x over Rational Field\nsage: F(x)\nx\nsage: ~F(x)            # new bug avoided\nx^-1\n```\n\n\n**__Second section: Timings__**\n\nHere I am collecting the examples that were studied in the comments above.\n\n*sage-5.0.beta10-gcc without the patch*\n\n```\nsage: R.<x> = ZZ[[]]\nsage: timeit('a=1/(1+x)')\n625 loops, best of 3: 445 \u00b5s per loop\nsage: timeit('a=1/x')\n625 loops, best of 3: 283 \u00b5s per loop\nsage: timeit('a=(1+x)/x')\n625 loops, best of 3: 290 \u00b5s per loop\nsage: timeit('a=(1+x)/(1-x)')\n625 loops, best of 3: 450 \u00b5s per loop\nsage: y = (3*x+2)/(1+x)\nsage: y=y/x\nsage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)\nsage: z=y/x\nsage: timeit('y+z')\n625 loops, best of 3: 104 \u00b5s per loop\nsage: timeit('y*z')\n625 loops, best of 3: 76.2 \u00b5s per loop\nsage: timeit('y-z')\n625 loops, best of 3: 103 \u00b5s per loop\nsage: timeit('y/z')    # bug\nTraceback (most recent call last):\n...\nArithmeticError: division not defined\nsage: P.<t> = QQ[[]]\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)\nsage: p.sqrt()\n3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)\nsage: timeit('q = p.sqrt()')\n625 loops, best of 3: 810 \u00b5s per loop\nsage: timeit('q = (p^2).sqrt()')\n625 loops, best of 3: 829 \u00b5s per loop\nsage: timeit('q = (p^4).sqrt()')\n625 loops, best of 3: 890 \u00b5s per loop\nsage: PZ = ZZ[['t']]\nsage: timeit('q = (PZ(p)^2).sqrt()')    # bug\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (2017, 0))\nTraceback (most recent call last):\n...\nTypeError: no conversion of this rational to integer\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9\nsage: timeit('q = p.sqrt()')\n125 loops, best of 3: 1.07 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n625 loops, best of 3: 1.12 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n625 loops, best of 3: 1.12 ms per loop\n```\n\n\n*sage-5.0.beta10-gcc with the patch*\n\n```\nsage: R.<x> = ZZ[[]]\nsage: timeit('a=1/(1+x)')\n625 loops, best of 3: 506 \u00b5s per loop\nsage: timeit('a=1/x')\n625 loops, best of 3: 153 \u00b5s per loop\nsage: timeit('a=(1+x)/x')\n625 loops, best of 3: 160 \u00b5s per loop\nsage: timeit('a=(1+x)/(1-x)')\n625 loops, best of 3: 516 \u00b5s per loop\nsage: y = (3*x+2)/(1+x)\nsage: y=y/x\nsage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)\nsage: z=y/x\nsage: timeit('y+z')\n625 loops, best of 3: 37.8 \u00b5s per loop\nsage: timeit('y*z')\n625 loops, best of 3: 26.9 \u00b5s per loop\nsage: timeit('y-z')\n625 loops, best of 3: 20.6 \u00b5s per loop\nsage: timeit('y/z')      # bug fixed\n625 loops, best of 3: 277 \u00b5s per loop\nsage: P.<t> = QQ[[]]\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)\nsage: p.sqrt()\n3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)\nsage: timeit('q = p.sqrt()')\n625 loops, best of 3: 847 \u00b5s per loop\nsage: timeit('q = (p^2).sqrt()')\n625 loops, best of 3: 872 \u00b5s per loop\nsage: timeit('q = (p^4).sqrt()')\n625 loops, best of 3: 932 \u00b5s per loop\nsage: PZ = ZZ[['t']]\nsage: timeit('q = (PZ(p)^2).sqrt()')    # bug fixed\n125 loops, best of 3: 1.46 ms per loop\nsage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9\nsage: timeit('q = p.sqrt()')\n625 loops, best of 3: 1.11 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n625 loops, best of 3: 1.17 ms per loop\nsage: timeit('q = (p^2).sqrt()')\n625 loops, best of 3: 1.17 ms per loop\n```\n\n\nI think, given that various bugs are fixed, and I think the timings tend to be better (not in all examples, but it seems to me that the loss is less than the gain), I guess it is \"needs review\", modulo doc test suite.\n\nApply trac-8972_fraction_of_power_series_combined.patch",
    "created_at": "2012-03-29T14:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82742",
    "user": "SimonKing"
}
```

I have rebased the patch. The test suite needs to be run, but the patch should now apply to sage-5.0.beta10. Here is some supporting evidence:

**__First section: The bugs to be fixed__**

*sage-5.0.beta10-gcc without the patch*

```
sage: R.<x> = ZZ[[]]
sage: (1/x).parent()  # bug
Laurent Series Ring in x over Integer Ring
sage: (x/x).parent()  # bug
Power Series Ring in x over Integer Ring
sage: (1/(2*x)).parent()  # bug
Traceback (most recent call last):
...
TypeError: no conversion of this rational to integer
sage: F = FractionField(R)
sage: 1/x in F    # bug
False
sage: F           # I think a Laurent series ring would be better
Fraction Field of Power Series Ring in x over Integer Ring
sage: F(x)
x
sage: ~F(x)   # was a problem with an early form of my patches.
1/x
```


*sage-5.0.beta10-gcc with the patch*

```
age: R.<x> = ZZ[[]]
sage: (1/x).parent()   # bug fixed
Laurent Series Ring in x over Rational Field
sage: (x/x).parent()   # bug fixed
Laurent Series Ring in x over Rational Field
sage: (1/(2*x)).parent() # bug fixed
Laurent Series Ring in x over Rational Field
sage: F = FractionField(R)
sage: 1/x in F         # bug fixed
True
sage: F                # I think that's much better!
Laurent Series Ring in x over Rational Field
sage: F(x)
x
sage: ~F(x)            # new bug avoided
x^-1
```


**__Second section: Timings__**

Here I am collecting the examples that were studied in the comments above.

*sage-5.0.beta10-gcc without the patch*

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 445 µs per loop
sage: timeit('a=1/x')
625 loops, best of 3: 283 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 290 µs per loop
sage: timeit('a=(1+x)/(1-x)')
625 loops, best of 3: 450 µs per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 104 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 76.2 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 103 µs per loop
sage: timeit('y/z')    # bug
Traceback (most recent call last):
...
ArithmeticError: division not defined
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 810 µs per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 829 µs per loop
sage: timeit('q = (p^4).sqrt()')
625 loops, best of 3: 890 µs per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')    # bug
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2017, 0))
Traceback (most recent call last):
...
TypeError: no conversion of this rational to integer
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
125 loops, best of 3: 1.07 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.12 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.12 ms per loop
```


*sage-5.0.beta10-gcc with the patch*

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 506 µs per loop
sage: timeit('a=1/x')
625 loops, best of 3: 153 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 160 µs per loop
sage: timeit('a=(1+x)/(1-x)')
625 loops, best of 3: 516 µs per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 37.8 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 26.9 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 20.6 µs per loop
sage: timeit('y/z')      # bug fixed
625 loops, best of 3: 277 µs per loop
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 847 µs per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 872 µs per loop
sage: timeit('q = (p^4).sqrt()')
625 loops, best of 3: 932 µs per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')    # bug fixed
125 loops, best of 3: 1.46 ms per loop
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 1.11 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.17 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.17 ms per loop
```


I think, given that various bugs are fixed, and I think the timings tend to be better (not in all examples, but it seems to me that the loss is less than the gain), I guess it is "needs review", modulo doc test suite.

Apply trac-8972_fraction_of_power_series_combined.patch



---

archive/issue_comments_082743.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-29T17:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82743",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082744.json:
```json
{
    "body": "The patchbot reports a doctest failure with 5.0.beta11:\n\n```\nsage -t  -force_lib devel/sage-8972/sage/rings/multi_power_series_ring_element.py\n**********************************************************************\nFile \"/storage/masiao/sage-5.0.beta11-patchbot/devel/sage-8972/sage/rings/multi_power_series_ring_element.py\", line 139:\n    sage: h = 1/f; h\nException raised:\n    Traceback (most recent call last):\n      File \"/storage/masiao/sage-5.0.beta11-patchbot/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/storage/masiao/sage-5.0.beta11-patchbot/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/storage/masiao/sage-5.0.beta11-patchbot/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[46]>\", line 1, in <module>\n        h = Integer(1)/f; h###line 139:\n    sage: h = 1/f; h\n      File \"element.pyx\", line 1799, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:13260)\n      File \"coerce.pyx\", line 738, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6583)\n      File \"coerce.pyx\", line 1210, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:11424)\n      File \"coerce.pyx\", line 1378, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:13135)\n      File \"ring.pyx\", line 1420, in sage.rings.ring.CommutativeRing._pseudo_fraction_field (sage/rings/ring.c:9929)\n        return self.fraction_field()\n      File \"/storage/masiao/sage-5.0.beta11-patchbot/local/lib/python/site-packages/sage/rings/power_series_ring.py\", line 672, in fraction_field\n        return LaurentSeriesRing(self.base().fraction_field(),self.variable_names())\n      File \"/storage/masiao/sage-5.0.beta11-patchbot/local/lib/python/site-packages/sage/rings/laurent_series_ring.py\", line 91, in LaurentSeriesRing\n        R = LaurentSeriesRing_field(base_ring, name, sparse)\n      File \"/storage/masiao/sage-5.0.beta11-patchbot/local/lib/python/site-packages/sage/rings/laurent_series_ring.py\", line 400, in __init__\n        LaurentSeriesRing_generic.__init__(self, base_ring, name, sparse)\n      File \"/storage/masiao/sage-5.0.beta11-patchbot/local/lib/python/site-packages/sage/rings/laurent_series_ring.py\", line 121, in __init__\n        commutative_ring.CommutativeRing.__init__(self, base_ring, names=name, category=_Fields)\n      File \"ring.pyx\", line 1365, in sage.rings.ring.CommutativeRing.__init__ (sage/rings/ring.c:9627)\n        Ring.__init__(self, base_ring, names=names, normalize=normalize,\n      File \"ring.pyx\", line 156, in sage.rings.ring.Ring.__init__ (sage/rings/ring.c:1903)\n        Parent.__init__(self, base=base, names=names, normalize=normalize,\n      File \"parent.pyx\", line 532, in sage.structure.parent.Parent.__init__ (sage/structure/parent.c:4484)\n      File \"parent_gens.pyx\", line 331, in sage.structure.parent_gens.ParentWithGens._assign_names (sage/structure/parent_gens.c:3052)\n      File \"parent_gens.pyx\", line 213, in sage.structure.parent_gens.normalize_names (sage/structure/parent_gens.c:2360)\n    IndexError: the number of names must equal the number of generators\n**********************************************************************\n```\n",
    "created_at": "2012-03-29T17:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82744",
    "user": "davidloeffler"
}
```

The patchbot reports a doctest failure with 5.0.beta11:

```
sage -t  -force_lib devel/sage-8972/sage/rings/multi_power_series_ring_element.py
**********************************************************************
File "/storage/masiao/sage-5.0.beta11-patchbot/devel/sage-8972/sage/rings/multi_power_series_ring_element.py", line 139:
    sage: h = 1/f; h
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[46]>", line 1, in <module>
        h = Integer(1)/f; h###line 139:
    sage: h = 1/f; h
      File "element.pyx", line 1799, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:13260)
      File "coerce.pyx", line 738, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6583)
      File "coerce.pyx", line 1210, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:11424)
      File "coerce.pyx", line 1378, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:13135)
      File "ring.pyx", line 1420, in sage.rings.ring.CommutativeRing._pseudo_fraction_field (sage/rings/ring.c:9929)
        return self.fraction_field()
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/lib/python/site-packages/sage/rings/power_series_ring.py", line 672, in fraction_field
        return LaurentSeriesRing(self.base().fraction_field(),self.variable_names())
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/lib/python/site-packages/sage/rings/laurent_series_ring.py", line 91, in LaurentSeriesRing
        R = LaurentSeriesRing_field(base_ring, name, sparse)
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/lib/python/site-packages/sage/rings/laurent_series_ring.py", line 400, in __init__
        LaurentSeriesRing_generic.__init__(self, base_ring, name, sparse)
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/lib/python/site-packages/sage/rings/laurent_series_ring.py", line 121, in __init__
        commutative_ring.CommutativeRing.__init__(self, base_ring, names=name, category=_Fields)
      File "ring.pyx", line 1365, in sage.rings.ring.CommutativeRing.__init__ (sage/rings/ring.c:9627)
        Ring.__init__(self, base_ring, names=names, normalize=normalize,
      File "ring.pyx", line 156, in sage.rings.ring.Ring.__init__ (sage/rings/ring.c:1903)
        Parent.__init__(self, base=base, names=names, normalize=normalize,
      File "parent.pyx", line 532, in sage.structure.parent.Parent.__init__ (sage/structure/parent.c:4484)
      File "parent_gens.pyx", line 331, in sage.structure.parent_gens.ParentWithGens._assign_names (sage/structure/parent_gens.c:3052)
      File "parent_gens.pyx", line 213, in sage.structure.parent_gens.normalize_names (sage/structure/parent_gens.c:2360)
    IndexError: the number of names must equal the number of generators
**********************************************************************
```




---

archive/issue_comments_082745.json:
```json
{
    "body": "Arrgh. That's nasty. The reason for the doctest problems is that meanwhile there are multivariate power series rings -- but there are still no multivariate Laurent series rings.\n\nSpontaneously, I suggest a temporary work-around: In the case of multivariate case, the old behaviour (namely: using a formal fraction field) should be used, until multivariate Laurent series are available.",
    "created_at": "2012-03-30T08:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82745",
    "user": "SimonKing"
}
```

Arrgh. That's nasty. The reason for the doctest problems is that meanwhile there are multivariate power series rings -- but there are still no multivariate Laurent series rings.

Spontaneously, I suggest a temporary work-around: In the case of multivariate case, the old behaviour (namely: using a formal fraction field) should be used, until multivariate Laurent series are available.



---

archive/issue_comments_082746.json:
```json
{
    "body": "My spontaneous suggestion does not work easily. Sorry.",
    "created_at": "2012-03-30T09:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82746",
    "user": "SimonKing"
}
```

My spontaneous suggestion does not work easily. Sorry.



---

archive/issue_comments_082747.json:
```json
{
    "body": "I think it would be great for this ticket to come back to life! Is it possible to just take the current power series classes append _old to all the class names and have the multivariable power series inherit from those?\n\n(Since no one has posted a ticket for creating multivariable Laurent series, let me ask here what is wrong with making them a multivariable power series ring with a univariate Laurent series ring in the background?)",
    "created_at": "2013-03-14T06:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82747",
    "user": "robharron"
}
```

I think it would be great for this ticket to come back to life! Is it possible to just take the current power series classes append _old to all the class names and have the multivariable power series inherit from those?

(Since no one has posted a ticket for creating multivariable Laurent series, let me ask here what is wrong with making them a multivariable power series ring with a univariate Laurent series ring in the background?)



---

archive/issue_comments_082748.json:
```json
{
    "body": "Converted the patch into a Git branch and resolved merge conflicts.  Fixed a few relatively straightforward doctest failures in the second commit.  Summary of remaining failures:\n\n```\nsage -t --long src/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py  # 4 doctests failed\nsage -t --long src/sage/tests/french_book/polynomes.py  # 2 doctests failed\nsage -t --long src/sage/rings/multi_power_series_ring_element.py  # 4 doctests failed\n```\n",
    "created_at": "2014-05-04T19:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82748",
    "user": "pbruin"
}
```

Converted the patch into a Git branch and resolved merge conflicts.  Fixed a few relatively straightforward doctest failures in the second commit.  Summary of remaining failures:

```
sage -t --long src/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py  # 4 doctests failed
sage -t --long src/sage/tests/french_book/polynomes.py  # 2 doctests failed
sage -t --long src/sage/rings/multi_power_series_ring_element.py  # 4 doctests failed
```




---

archive/issue_comments_082749.json:
```json
{
    "body": "just rebased on 6.3.beta5\n----\nNew commits:",
    "created_at": "2014-07-09T19:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82749",
    "user": "chapoton"
}
```

just rebased on 6.3.beta5
----
New commits:



---

archive/issue_comments_082750.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-09-07T12:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82750",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_082751.json:
```json
{
    "body": "Failures in src/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py seem to be just about slight changes in precision (either gain or loss by one). Maybe one can just correct the result of the doctests. \n\nFailures in src/sage/rings/multi_power_series_ring_element.py are more serious: they come from trying to build a Laurent series ring in several variables, that we currently do not have !",
    "created_at": "2014-12-27T08:38:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82751",
    "user": "chapoton"
}
```

Failures in src/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py seem to be just about slight changes in precision (either gain or loss by one). Maybe one can just correct the result of the doctests. 

Failures in src/sage/rings/multi_power_series_ring_element.py are more serious: they come from trying to build a Laurent series ring in several variables, that we currently do not have !



---

archive/issue_comments_082752.json:
```json
{
    "body": "I have a question about the description of this issue. Please forgive that I'm no algebraist.\n\n```\nsage: (1/(2*x)).parent()\n...\nTypeError: no conversion of this rational to integer\n```\n\nIsn't this correct, with the ring over ZZ? With QQ there is no error.\n\nIf so, the description should be corrected.",
    "created_at": "2015-01-24T16:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82752",
    "user": "rws"
}
```

I have a question about the description of this issue. Please forgive that I'm no algebraist.

```
sage: (1/(2*x)).parent()
...
TypeError: no conversion of this rational to integer
```

Isn't this correct, with the ring over ZZ? With QQ there is no error.

If so, the description should be corrected.



---

archive/issue_comments_082753.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-02-01T10:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82753",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_082754.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-02-01T12:22:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82754",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_082755.json:
```json
{
    "body": "Since the power series issue is somewhat separate, I created #21283 to deal with it on its own.",
    "created_at": "2016-08-18T13:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82755",
    "user": "kedlaya"
}
```

Since the power series issue is somewhat separate, I created #21283 to deal with it on its own.



---

archive/issue_comments_082756.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2021-01-19T23:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82756",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_082757.json:
```json
{
    "body": "Approach might be too naive, but it seems to solve the first and the last bug without compromising the timing.",
    "created_at": "2021-01-19T23:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82757",
    "user": "@mjungmath"
}
```

Approach might be too naive, but it seems to solve the first and the last bug without compromising the timing.



---

archive/issue_comments_082758.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-01-19T23:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82758",
    "user": "@mjungmath"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082759.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2021-01-19T23:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82759",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_082760.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2021-01-20T08:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82760",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_082761.json:
```json
{
    "body": "This should do.",
    "created_at": "2021-01-20T08:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82761",
    "user": "@mjungmath"
}
```

This should do.



---

archive/issue_comments_082762.json:
```json
{
    "body": "Replying to [comment:64 gh-mjungmath]:\n> Approach might be too naive, but it seems to solve the first and the last bug without compromising the timing.\nDoes this also address the dependency #21283?",
    "created_at": "2021-01-20T08:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82762",
    "user": "pbruin"
}
```

Replying to [comment:64 gh-mjungmath]:
> Approach might be too naive, but it seems to solve the first and the last bug without compromising the timing.
Does this also address the dependency #21283?



---

archive/issue_comments_082763.json:
```json
{
    "body": "Replying to [comment:70 pbruin]:\n> Replying to [comment:64 gh-mjungmath]:\n> > Approach might be too naive, but it seems to solve the first and the last bug without compromising the timing.\n> Does this also address the dependency #21283?\n\nNope. I just wanted to see what the patchbot has to say before I modify the ticket description. Here we go.",
    "created_at": "2021-01-20T08:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82763",
    "user": "@mjungmath"
}
```

Replying to [comment:70 pbruin]:
> Replying to [comment:64 gh-mjungmath]:
> > Approach might be too naive, but it seems to solve the first and the last bug without compromising the timing.
> Does this also address the dependency #21283?

Nope. I just wanted to see what the patchbot has to say before I modify the ticket description. Here we go.



---

archive/issue_comments_082764.json:
```json
{
    "body": "Yay! Patchbot is green! :)",
    "created_at": "2021-01-20T12:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82764",
    "user": "@mjungmath"
}
```

Yay! Patchbot is green! :)



---

archive/issue_comments_082765.json:
```json
{
    "body": "Would be nice to have this ticket reviewed. Thanks. :)",
    "created_at": "2021-01-23T01:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82765",
    "user": "@mjungmath"
}
```

Would be nice to have this ticket reviewed. Thanks. :)



---

archive/issue_comments_082766.json:
```json
{
    "body": "Patchbot seems still be satisfied with beta7. It'd be nice to have this change in version 9.3 though. Otherwise, a rebase might become necessary soon...",
    "created_at": "2021-02-15T10:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82766",
    "user": "@mjungmath"
}
```

Patchbot seems still be satisfied with beta7. It'd be nice to have this change in version 9.3 though. Otherwise, a rebase might become necessary soon...



---

archive/issue_comments_082767.json:
```json
{
    "body": "There are a few details that still fixing:\n\nThis seems strange:\n\n```\n:doc:`laurent_series_ring_element`.\n```\n\nWouldn't it be better to be a specific reference to the class? Although I am not sure it is worth the direct reference.\n\nThis is wrong:\n\n```\n        If we try a non-zero, non-unit leading coefficient, we end up in the in\n        the fraction field, i.e. Laurent series ring::\n```\n\nEven for units, you still end up in the fraction field.\n\n\n```diff\n-However, this must fail if the underlying ring is no integral domain::\n+However, this must fail if the underlying ring is not an integral domain::\n```\n",
    "created_at": "2021-02-16T00:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82767",
    "user": "tscrim"
}
```

There are a few details that still fixing:

This seems strange:

```
:doc:`laurent_series_ring_element`.
```

Wouldn't it be better to be a specific reference to the class? Although I am not sure it is worth the direct reference.

This is wrong:

```
        If we try a non-zero, non-unit leading coefficient, we end up in the in
        the fraction field, i.e. Laurent series ring::
```

Even for units, you still end up in the fraction field.


```diff
-However, this must fail if the underlying ring is no integral domain::
+However, this must fail if the underlying ring is not an integral domain::
```




---

archive/issue_comments_082768.json:
```json
{
    "body": "Thank you Travis for taking a look!\n\nReplying to [comment:82 tscrim]:\n> There are a few details that still fixing:\n> \n> This seems strange:\n> {{{\n> :doc:`laurent_series_ring_element`.\n> }}}\n> Wouldn't it be better to be a specific reference to the class? Although I am not sure it is worth the direct reference.\n\nAlright, I'll change it.\n \n> This is wrong:\n> {{{\n>         If we try a non-zero, non-unit leading coefficient, we end up in the in\n>         the fraction field, i.e. Laurent series ring::\n> }}}\n> Even for units, you still end up in the fraction field.\n\nOh right. I think the previous author already meant constant terms instead of leading terms. At least that would make more sense.\n\n> \n> {{{#!diff\n> -However, this must fail if the underlying ring is no integral domain::\n> +However, this must fail if the underlying ring is not an integral domain::\n> }}}\n\nWill do.",
    "created_at": "2021-02-16T11:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82768",
    "user": "@mjungmath"
}
```

Thank you Travis for taking a look!

Replying to [comment:82 tscrim]:
> There are a few details that still fixing:
> 
> This seems strange:
> {{{
> :doc:`laurent_series_ring_element`.
> }}}
> Wouldn't it be better to be a specific reference to the class? Although I am not sure it is worth the direct reference.

Alright, I'll change it.
 
> This is wrong:
> {{{
>         If we try a non-zero, non-unit leading coefficient, we end up in the in
>         the fraction field, i.e. Laurent series ring::
> }}}
> Even for units, you still end up in the fraction field.

Oh right. I think the previous author already meant constant terms instead of leading terms. At least that would make more sense.

> 
> {{{#!diff
> -However, this must fail if the underlying ring is no integral domain::
> +However, this must fail if the underlying ring is not an integral domain::
> }}}

Will do.



---

archive/issue_comments_082769.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2021-02-16T11:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82769",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_082770.json:
```json
{
    "body": "That should be better.",
    "created_at": "2021-02-16T11:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82770",
    "user": "@mjungmath"
}
```

That should be better.



---

archive/issue_comments_082771.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-02-16T23:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82771",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082772.json:
```json
{
    "body": "Thanks. LGTM.",
    "created_at": "2021-02-16T23:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82772",
    "user": "tscrim"
}
```

Thanks. LGTM.



---

archive/issue_comments_082773.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2021-03-01T00:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8972#issuecomment-82773",
    "user": "vbraun"
}
```

Resolution: fixed
