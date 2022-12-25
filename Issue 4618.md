# Issue 4618: Request for Puiseux series in SAGE

archive/issues_004618.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @mezzarobba @videlec @dkrenn\n\nIn MAGMA, one can have fractional exponents for power series (which it calls Puiseux series), but SAGE does not seem to support this:\n\n```\nsage: PSR.<q>=PowerSeriesRing(QQ)\nsage: q^(1/5)\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/home/ljpk/.sage/temp/sage/2339/_home_ljpk_Eisenstein_sage_9.py in <module>()\n----> 1\n      2\n      3\n      4\n      5\n\n/home/was/s/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__pow__ (sage/structure/element.c:8866)()\n   1131\n   1132\n-> 1133\n   1134\n   1135\n\n/home/was/s/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.generic_power_c (sage/structure/element.c:17789)()\n   2601\n   2602\n-> 2603\n   2604\n   2605\n\nNotImplementedError: non-integral exponents not supported\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4618\n\n",
    "created_at": "2008-11-25T17:04:14Z",
    "labels": [
        "component: linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.1",
    "title": "Request for Puiseux series in SAGE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4618",
    "user": "https://trac.sagemath.org/admin/accounts/users/ljpk"
}
```
Assignee: @williamstein

CC:  @mezzarobba @videlec @dkrenn

In MAGMA, one can have fractional exponents for power series (which it calls Puiseux series), but SAGE does not seem to support this:

```
sage: PSR.<q>=PowerSeriesRing(QQ)
sage: q^(1/5)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/ljpk/.sage/temp/sage/2339/_home_ljpk_Eisenstein_sage_9.py in <module>()
----> 1
      2
      3
      4
      5

/home/was/s/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__pow__ (sage/structure/element.c:8866)()
   1131
   1132
-> 1133
   1134
   1135

/home/was/s/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.generic_power_c (sage/structure/element.c:17789)()
   2601
   2602
-> 2603
   2604
   2605

NotImplementedError: non-integral exponents not supported
```


Issue created by migration from https://trac.sagemath.org/ticket/4618





---

archive/issue_comments_034593.json:
```json
{
    "body": "Hi ljpk,\n\nrequests like this shouls always go to [sage-devel] too since people generally do not look for things to do in trac. Sending the same request to [sage-devel] will make people aware of the problem and might get some design discussion going. Obviously if you are working on code this is different, but if you expect someone else to do the dirty work a little advertisement cannot hurt :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T19:15:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34593",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi ljpk,

requests like this shouls always go to [sage-devel] too since people generally do not look for things to do in trac. Sending the same request to [sage-devel] will make people aware of the problem and might get some design discussion going. Obviously if you are working on code this is different, but if you expect someone else to do the dirty work a little advertisement cannot hurt :)

Cheers,

Michael



---

archive/issue_comments_034594.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34594",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_034595.json:
```json
{
    "body": "Changing component from linear algebra to algebra.",
    "created_at": "2010-01-03T06:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34595",
    "user": "https://github.com/aghitza"
}
```

Changing component from linear algebra to algebra.



---

archive/issue_comments_034596.json:
```json
{
    "body": "Changing assignee from @williamstein to @aghitza.",
    "created_at": "2010-01-03T06:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34596",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @aghitza.



---

archive/issue_comments_034597.json:
```json
{
    "body": "See also #9555.",
    "created_at": "2011-06-29T01:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34597",
    "user": "https://github.com/kcrisman"
}
```

See also #9555.



---

archive/issue_events_010499.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10499"
}
```



---

archive/issue_events_010500.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10500"
}
```



---

archive/issue_events_010501.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10501"
}
```



---

archive/issue_comments_034598.json:
```json
{
    "body": "Changing keywords from \"\" to \"Puiseux\".",
    "created_at": "2014-03-06T15:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34598",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "Puiseux".



---

archive/issue_events_010502.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10502"
}
```



---

archive/issue_events_010503.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10503"
}
```



---

archive/issue_events_010504.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10504"
}
```



---

archive/issue_events_010505.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10505"
}
```



---

archive/issue_comments_034599.json:
```json
{
    "body": "See also #9289.",
    "created_at": "2015-02-12T15:01:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34599",
    "user": "https://github.com/kcrisman"
}
```

See also #9289.



---

archive/issue_events_010506.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2015-02-17T13:57:33Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10506"
}
```



---

archive/issue_events_010507.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2015-02-17T13:57:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10507"
}
```



---

archive/issue_comments_034600.json:
```json
{
    "body": "some code is available here:\n\nhttps://github.com/abelfunctions/abelfunctions/tree/master/abelfunctions",
    "created_at": "2016-03-28T14:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34600",
    "user": "https://github.com/fchapoton"
}
```

some code is available here:

https://github.com/abelfunctions/abelfunctions/tree/master/abelfunctions



---

archive/issue_comments_034601.json:
```json
{
    "body": "As mentioned in an email correspondence with **chapoton** I believe my implementation of `PuiseuxSeriesRing` and `PuiseuxSeriesRingElement`to be pretty complete in regards to fitting into Sage's coercion model. Hopefully it will, at the very least, be a good starting point.\n\nThanks to **chapoton** for offering to plug this code into Sage!\n\nOn a side note, I also have some code for computing Puiseux series representations of places on a plane algebraic curve. The entry function is `abelfunctions.puiseux_series.puiseux_series`. I'm sure someone with better Sage skills than myself can improve the algorithm and plug that in as well.",
    "created_at": "2016-03-28T14:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34601",
    "user": "https://github.com/cswiercz"
}
```

As mentioned in an email correspondence with **chapoton** I believe my implementation of `PuiseuxSeriesRing` and `PuiseuxSeriesRingElement`to be pretty complete in regards to fitting into Sage's coercion model. Hopefully it will, at the very least, be a good starting point.

Thanks to **chapoton** for offering to plug this code into Sage!

On a side note, I also have some code for computing Puiseux series representations of places on a plane algebraic curve. The entry function is `abelfunctions.puiseux_series.puiseux_series`. I'm sure someone with better Sage skills than myself can improve the algorithm and plug that in as well.



---

archive/issue_comments_034602.json:
```json
{
    "body": "just made a git branch, not tested at all\n----\nNew commits:",
    "created_at": "2016-03-28T15:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34602",
    "user": "https://github.com/fchapoton"
}
```

just made a git branch, not tested at all
----
New commits:



---

archive/issue_comments_034603.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-28T17:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34603",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034604.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-28T17:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34604",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034605.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-28T19:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34605",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034606.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-29T11:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34606",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034607.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-30T18:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34607",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034608.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-05-11T13:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34608",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034609.json:
```json
{
    "body": "This is a nice addition. Is it ready for review?\n\nA few comments:\n\n- Is it planned to extend it to the multivariate case?\n- It would be nice to add a more detailed mathematical explanation about what a Puiseux series is in the docstring.",
    "created_at": "2016-12-21T18:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34609",
    "user": "https://github.com/miguelmarco"
}
```

This is a nice addition. Is it ready for review?

A few comments:

- Is it planned to extend it to the multivariate case?
- It would be nice to add a more detailed mathematical explanation about what a Puiseux series is in the docstring.



---

archive/issue_comments_034610.json:
```json
{
    "body": "It is probably not ready, there seems to be a bug lurking around.\n\nNo plan to implement the multivariate case.\n\nand the coverage is not 100%",
    "created_at": "2017-01-01T18:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34610",
    "user": "https://github.com/fchapoton"
}
```

It is probably not ready, there seems to be a bug lurking around.

No plan to implement the multivariate case.

and the coverage is not 100%



---

archive/issue_comments_034611.json:
```json
{
    "body": "This is needed to allow `extend=True` for the `nth_root` method in #10720 (see also [this sage-devel thread](https://groups.google.com/forum/#!topic/sage-devel/ijYyZ4IduF0)).",
    "created_at": "2017-12-21T11:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34611",
    "user": "https://github.com/videlec"
}
```

This is needed to allow `extend=True` for the `nth_root` method in #10720 (see also [this sage-devel thread](https://groups.google.com/forum/#!topic/sage-devel/ijYyZ4IduF0)).



---

archive/issue_comments_034612.json:
```json
{
    "body": "An innocent operation like the following will multiply the memory footprint by 24 with no change in information\n\n```\nsage: p = prod(1 - q^n + O(q^100) for n in range(1,100))   # fine: 100 * coeff size\nsage: q^(1/24) * p   # bad: 100 * 24 * coeff size\n```\n\nThe above example is the q-series expansion of the [Dedekind eta function](https://en.wikipedia.org/wiki/Dedekind_eta_function). There might be a more clever data structure to use as this kind of series is frequently encountered when dealing with modular forms.",
    "created_at": "2017-12-21T11:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34612",
    "user": "https://github.com/videlec"
}
```

An innocent operation like the following will multiply the memory footprint by 24 with no change in information

```
sage: p = prod(1 - q^n + O(q^100) for n in range(1,100))   # fine: 100 * coeff size
sage: q^(1/24) * p   # bad: 100 * 24 * coeff size
```

The above example is the q-series expansion of the [Dedekind eta function](https://en.wikipedia.org/wiki/Dedekind_eta_function). There might be a more clever data structure to use as this kind of series is frequently encountered when dealing with modular forms.



---

archive/issue_events_010508.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2017-12-26T16:12:37Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10508"
}
```



---

archive/issue_events_010509.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2017-12-26T16:12:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10509"
}
```



---

archive/issue_comments_034613.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2019-04-24T19:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34613",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034614.json:
```json
{
    "body": "I do the following changes:\n\n1. Adaptation to current version 8.8.beta3 in order to have the code compile again.\n2. I replace the method `_cmp_` of `PuiseuxSeries` by `_richcmp_` and let it completely rely on the corresponding method of class `LaurentSeries`. The reason for this is not only modernisation, but also that the former method doesn't work correctly (for example comparison with zero returns wrong results).\n3. I add a specification of the representative of the Puiseux series inside the constructor of `PuiseuxSeries` in such a way that the ramification index is minimized. This improves the methods `laurent_series` and `power_series` (the examples given there would not work else-wise).\n4. I add more doctests.\n\nThere is still work to do, for example:\n\n1. There are several workarounds on other bugs in Sage. In general I think, these workarounds should be removed and the corresponding bugs should be treated in separate tickets. Examples:\n   a. In the methods `_repr_`, `exponents` and `coefficients` there is the following comment: *NOTE: `self.__l.coefficients()` is bugged when the coefficients are in QQbar but coerced into SR ...*. I have no idea how far it makes sense to consider Puiseux series (Laurent series, polynomial rings, ...) over the `SymbolicRing`. But since these constructions are possible, they should work (or should be blocked). There are simple examples where this is not the case:\n\n```\nsage: PS = PolynomialRing(SR,'x')\nsage: P = PolynomialRing(QQ,'x')\nsage: q = P((1,1,5)); q\n5*x^2 + x + 1\nsage: p = PS(q)\nsage: p.coefficients()\n[5*x^2 + x + 1]\nsage: p in SR\nTrue\n```\n \n    Is this a known bug? Concerning the methods in question, I think that they should rely more directly on the according methods of `LaurentSeries`.\nb. In the method `add_bigoh` the following error is caught:\n\n```\nsage: L.<x> = LaurentSeriesRing(QQ)\nsage: q = x^2 + x^3\nsage: q.add_bigoh(-1)\nTraceback (most recent call last):\n...\nValueError: prec (= -3) must be non-negative\n```\n\n    This should be fixed in `LaurentSeries`.\n\n2. I think we should clarify the following behavior of the method `add_bigoh`:\n\n```\nsage: R.<x> = PuiseuxSeriesRing(ZZ)\nsage: p = x**(-1/3) + 2*x**(1/5)\nsage: p.add_bigoh(1/2)\nx^(-1/3) + 2*x^(1/5) + O(x^(7/15))\n```\n\n   is this acceptable?\n\n3. The method `_repr_` needs work:\n\n```\nsage: R.<x> = PuiseuxSeriesRing(Zp(5))\nsage: x**(1/2) + 5 * x^(1/3)\n5 + O(5^21)*x^(1/3) + (1 + O(5^20))*x^(1/2)\n```\n\n\n4. Further doctests are needed.\n5. Integration into documentation.\n\nI will continue to work on this ticket according to feedback!",
    "created_at": "2019-04-24T20:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34614",
    "user": "https://github.com/soehms"
}
```

I do the following changes:

1. Adaptation to current version 8.8.beta3 in order to have the code compile again.
2. I replace the method `_cmp_` of `PuiseuxSeries` by `_richcmp_` and let it completely rely on the corresponding method of class `LaurentSeries`. The reason for this is not only modernisation, but also that the former method doesn't work correctly (for example comparison with zero returns wrong results).
3. I add a specification of the representative of the Puiseux series inside the constructor of `PuiseuxSeries` in such a way that the ramification index is minimized. This improves the methods `laurent_series` and `power_series` (the examples given there would not work else-wise).
4. I add more doctests.

There is still work to do, for example:

1. There are several workarounds on other bugs in Sage. In general I think, these workarounds should be removed and the corresponding bugs should be treated in separate tickets. Examples:
   a. In the methods `_repr_`, `exponents` and `coefficients` there is the following comment: *NOTE: `self.__l.coefficients()` is bugged when the coefficients are in QQbar but coerced into SR ...*. I have no idea how far it makes sense to consider Puiseux series (Laurent series, polynomial rings, ...) over the `SymbolicRing`. But since these constructions are possible, they should work (or should be blocked). There are simple examples where this is not the case:

```
sage: PS = PolynomialRing(SR,'x')
sage: P = PolynomialRing(QQ,'x')
sage: q = P((1,1,5)); q
5*x^2 + x + 1
sage: p = PS(q)
sage: p.coefficients()
[5*x^2 + x + 1]
sage: p in SR
True
```
 
    Is this a known bug? Concerning the methods in question, I think that they should rely more directly on the according methods of `LaurentSeries`.
b. In the method `add_bigoh` the following error is caught:

```
sage: L.<x> = LaurentSeriesRing(QQ)
sage: q = x^2 + x^3
sage: q.add_bigoh(-1)
Traceback (most recent call last):
...
ValueError: prec (= -3) must be non-negative
```

    This should be fixed in `LaurentSeries`.

2. I think we should clarify the following behavior of the method `add_bigoh`:

```
sage: R.<x> = PuiseuxSeriesRing(ZZ)
sage: p = x**(-1/3) + 2*x**(1/5)
sage: p.add_bigoh(1/2)
x^(-1/3) + 2*x^(1/5) + O(x^(7/15))
```

   is this acceptable?

3. The method `_repr_` needs work:

```
sage: R.<x> = PuiseuxSeriesRing(Zp(5))
sage: x**(1/2) + 5 * x^(1/3)
5 + O(5^21)*x^(1/3) + (1 + O(5^20))*x^(1/2)
```


4. Further doctests are needed.
5. Integration into documentation.

I will continue to work on this ticket according to feedback!



---

archive/issue_comments_034615.json:
```json
{
    "body": "Changing keywords from \"Puiseux\" to \"Puiseux, days100\".",
    "created_at": "2019-07-19T20:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34615",
    "user": "https://github.com/soehms"
}
```

Changing keywords from "Puiseux" to "Puiseux, days100".



---

archive/issue_events_010510.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2019-07-19T20:11:11Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10510"
}
```



---

archive/issue_events_010511.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2019-07-19T20:11:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10511"
}
```



---

archive/issue_comments_034616.json:
```json
{
    "body": "There is a hash doctest failure with python3:\n\n```\nsage -t --long src/sage/rings/puiseux_series_ring_element.pyx\n**********************************************************************\nFile \"src/sage/rings/puiseux_series_ring_element.pyx\", line 549, in sage.rings.puiseux_series_ring_element.PuiseuxSeries.__hash__\nFailed example:\n    hash(p)  # indirect doctest\nExpected:\n    -15360174648385722\nGot:\n    8039939419124139326\n```\n",
    "created_at": "2019-07-23T07:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34616",
    "user": "https://github.com/fchapoton"
}
```

There is a hash doctest failure with python3:

```
sage -t --long src/sage/rings/puiseux_series_ring_element.pyx
**********************************************************************
File "src/sage/rings/puiseux_series_ring_element.pyx", line 549, in sage.rings.puiseux_series_ring_element.PuiseuxSeries.__hash__
Failed example:
    hash(p)  # indirect doctest
Expected:
    -15360174648385722
Got:
    8039939419124139326
```




---

archive/issue_comments_034617.json:
```json
{
    "body": "In agreement with Fr\u00e9d\u00e9ric I have created the tickets #28238 and #28239 to treat the external bugs mentioned in comment 32. The according workarounds in the code can be removed.",
    "created_at": "2019-07-23T15:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34617",
    "user": "https://github.com/soehms"
}
```

In agreement with Frédéric I have created the tickets #28238 and #28239 to treat the external bugs mentioned in comment 32. The according workarounds in the code can be removed.



---

archive/issue_comments_034618.json:
```json
{
    "body": "Replying to [comment:36 chapoton]:\n> There is a hash doctest failure with python3:\n> {{{\n> sage -t --long src/sage/rings/puiseux_series_ring_element.pyx\n> **********************************************************************\n> File \"src/sage/rings/puiseux_series_ring_element.pyx\", line 549, in sage.rings.puiseux_series_ring_element.PuiseuxSeries.__hash__\n> Failed example:\n>     hash(p)  # indirect doctest\n> Expected:\n>     -15360174648385722\n> Got:\n>     8039939419124139326\n> }}}\n\nI will look at that at home (since I have no sage with python3 on the computer I am carrying with me)!",
    "created_at": "2019-07-23T15:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34618",
    "user": "https://github.com/soehms"
}
```

Replying to [comment:36 chapoton]:
> There is a hash doctest failure with python3:
> {{{
> sage -t --long src/sage/rings/puiseux_series_ring_element.pyx
> **********************************************************************
> File "src/sage/rings/puiseux_series_ring_element.pyx", line 549, in sage.rings.puiseux_series_ring_element.PuiseuxSeries.__hash__
> Failed example:
>     hash(p)  # indirect doctest
> Expected:
>     -15360174648385722
> Got:
>     8039939419124139326
> }}}

I will look at that at home (since I have no sage with python3 on the computer I am carrying with me)!



---

archive/issue_comments_034619.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2019-07-24T12:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34619",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034620.json:
```json
{
    "body": "Replying to [comment:28 vdelecroix]:\n> An innocent operation like the following will multiply the memory footprint by 24 with no change in information\n> {{{\n> sage: p = prod(1 - q^n + O(q^100) for n in range(1,100))   # fine: 100 * coeff size\n> sage: q^(1/24) * p   # bad: 100 * 24 * coeff size\n> }}}\n> The above example is the q-series expansion of the [Dedekind eta function](https://en.wikipedia.org/wiki/Dedekind_eta_function). There might be a more clever data structure to use as this kind of series is frequently encountered when dealing with modular forms.\n\nConcerning this example, you might want to read https://oscar.computeralgebra.de/blogs/2018/08/03/PuiseuxSeries/",
    "created_at": "2019-07-24T14:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34620",
    "user": "https://github.com/videlec"
}
```

Replying to [comment:28 vdelecroix]:
> An innocent operation like the following will multiply the memory footprint by 24 with no change in information
> {{{
> sage: p = prod(1 - q^n + O(q^100) for n in range(1,100))   # fine: 100 * coeff size
> sage: q^(1/24) * p   # bad: 100 * 24 * coeff size
> }}}
> The above example is the q-series expansion of the [Dedekind eta function](https://en.wikipedia.org/wiki/Dedekind_eta_function). There might be a more clever data structure to use as this kind of series is frequently encountered when dealing with modular forms.

Concerning this example, you might want to read https://oscar.computeralgebra.de/blogs/2018/08/03/PuiseuxSeries/



---

archive/issue_comments_034621.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2019-07-24T16:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34621",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034622.json:
```json
{
    "body": "Replying to [comment:40 vdelecroix]:\n> Replying to [comment:28 vdelecroix]:\n> > An innocent operation like the following will multiply the memory footprint by 24 with no change in information\n> > {{{\n> > sage: p = prod(1 - q^n + O(q^100) for n in range(1,100))   # fine: 100 * coeff size\n> > sage: q^(1/24) * p   # bad: 100 * 24 * coeff size\n> > }}}\n> > The above example is the q-series expansion of the [Dedekind eta function](https://en.wikipedia.org/wiki/Dedekind_eta_function). There might be a more clever data structure to use as this kind of series is frequently encountered when dealing with modular forms.\n> \n> Concerning this example, you might want to read https://oscar.computeralgebra.de/blogs/2018/08/03/PuiseuxSeries/\n\n\n\nThe multiplication of memory-size is caused by the call of the `V`-method (implemented for  Puiseux series) in the Laurent series class but it happens in the polynomial attached to the power series of the attached Laurent series.\n\n\n```\nsage: P.<q> = PuiseuxSeriesRing(QQ)\nsage: p = prod((1 - q^n).add_bigoh(100) for n in range(1,100))\nsage: t = q^(1/24) * p\nsage: s = t.laurent_part().valuation_zero_part().polynomial()\nsage: len(s.list())\n2209\nsage: len(p.laurent_part().valuation_zero_part().polynomial().list())\n93\n```\n\n\nSo the most generic option would be to implement a data-compression in the corresponding polynomial class. But this may involve external software as in the case of the example:\n\n\n```\nsage: type(s)\n<type 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_flint'>\n```\n\n\nThe same thing is true concerening the level of power series (for exmaple choosing `implementation='pari'`). So I think, the best place for implementing a smarter data structure would be the Laurent series class and could be done there by a //scale factor// as it is mentined in the article concerning the implementation in OSCAR: \"Laurent series themselves are also stored with a valuation, precision and a scale factor\".\n\nMy suggestion is, to open a new ticket on that task concerning such an implementation for the Laurent series. The method `V` should than just change the scale factor (instead of stretching the data volume). The implementaion of the Puiseux series could stay as it is. In opposite to `ramifications_index` to new scale factor could be named `covering_index`, for instance.\n\nBTW: what does this `V` stand for?",
    "created_at": "2019-07-26T09:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34622",
    "user": "https://github.com/soehms"
}
```

Replying to [comment:40 vdelecroix]:
> Replying to [comment:28 vdelecroix]:
> > An innocent operation like the following will multiply the memory footprint by 24 with no change in information
> > {{{
> > sage: p = prod(1 - q^n + O(q^100) for n in range(1,100))   # fine: 100 * coeff size
> > sage: q^(1/24) * p   # bad: 100 * 24 * coeff size
> > }}}
> > The above example is the q-series expansion of the [Dedekind eta function](https://en.wikipedia.org/wiki/Dedekind_eta_function). There might be a more clever data structure to use as this kind of series is frequently encountered when dealing with modular forms.
> 
> Concerning this example, you might want to read https://oscar.computeralgebra.de/blogs/2018/08/03/PuiseuxSeries/



The multiplication of memory-size is caused by the call of the `V`-method (implemented for  Puiseux series) in the Laurent series class but it happens in the polynomial attached to the power series of the attached Laurent series.


```
sage: P.<q> = PuiseuxSeriesRing(QQ)
sage: p = prod((1 - q^n).add_bigoh(100) for n in range(1,100))
sage: t = q^(1/24) * p
sage: s = t.laurent_part().valuation_zero_part().polynomial()
sage: len(s.list())
2209
sage: len(p.laurent_part().valuation_zero_part().polynomial().list())
93
```


So the most generic option would be to implement a data-compression in the corresponding polynomial class. But this may involve external software as in the case of the example:


```
sage: type(s)
<type 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_flint'>
```


The same thing is true concerening the level of power series (for exmaple choosing `implementation='pari'`). So I think, the best place for implementing a smarter data structure would be the Laurent series class and could be done there by a //scale factor// as it is mentined in the article concerning the implementation in OSCAR: "Laurent series themselves are also stored with a valuation, precision and a scale factor".

My suggestion is, to open a new ticket on that task concerning such an implementation for the Laurent series. The method `V` should than just change the scale factor (instead of stretching the data volume). The implementaion of the Puiseux series could stay as it is. In opposite to `ramifications_index` to new scale factor could be named `covering_index`, for instance.

BTW: what does this `V` stand for?



---

archive/issue_comments_034623.json:
```json
{
    "body": "I think that V stand for Verschiebung.",
    "created_at": "2019-07-26T10:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34623",
    "user": "https://github.com/fchapoton"
}
```

I think that V stand for Verschiebung.



---

archive/issue_comments_034624.json:
```json
{
    "body": "Replying to [comment:43 chapoton]:\n> I think that V stand for Verschiebung.\n\nThat sounds as if we should look for a better name! I even don't see a connection. The only mathematical meaning of *Verschiebung* I know is that of a *translation* in euclidean geometry.\nWhat about to replace `V` by `power_inflation`?",
    "created_at": "2019-07-28T11:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34624",
    "user": "https://github.com/soehms"
}
```

Replying to [comment:43 chapoton]:
> I think that V stand for Verschiebung.

That sounds as if we should look for a better name! I even don't see a connection. The only mathematical meaning of *Verschiebung* I know is that of a *translation* in euclidean geometry.
What about to replace `V` by `power_inflation`?



---

archive/issue_comments_034625.json:
```json
{
    "body": "Replying to [comment:44 soehms]:\n> Replying to [comment:43 chapoton]:\n> > I think that V stand for Verschiebung.\n> \n> That sounds as if we should look for a better name! I even don't see a connection. The only mathematical meaning of *Verschiebung* I know is that of a *translation* in euclidean geometry.\n\nIt is probably from Witt vector terminology, where that is a standard term?",
    "created_at": "2019-08-12T15:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34625",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:44 soehms]:
> Replying to [comment:43 chapoton]:
> > I think that V stand for Verschiebung.
> 
> That sounds as if we should look for a better name! I even don't see a connection. The only mathematical meaning of *Verschiebung* I know is that of a *translation* in euclidean geometry.

It is probably from Witt vector terminology, where that is a standard term?



---

archive/issue_comments_034626.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2019-08-16T11:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34626",
    "user": "https://github.com/soehms"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_034627.json:
```json
{
    "body": "Replying to [comment:45 kcrisman]:\n> Replying to [comment:44 soehms]:\n> > Replying to [comment:43 chapoton]:\n> > > I think that V stand for Verschiebung.\n> > \n> > That sounds as if we should look for a better name! I even don't see a connection. The only mathematical meaning of *Verschiebung* I know is that of a *translation* in euclidean geometry.\n> \n> It is probably from Witt vector terminology, where that is a standard term?\n\nThanks for the explanation! Indeed, that meaning of *Verschiebung* hasn't been present in my mind. But anyway, I would prefer a method name that doesn't dependent on any special context (and has more than just one letter). The `V` could by kept as an alias (together with an appropriate explanation). Opinions?",
    "created_at": "2019-08-16T11:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34627",
    "user": "https://github.com/soehms"
}
```

Replying to [comment:45 kcrisman]:
> Replying to [comment:44 soehms]:
> > Replying to [comment:43 chapoton]:
> > > I think that V stand for Verschiebung.
> > 
> > That sounds as if we should look for a better name! I even don't see a connection. The only mathematical meaning of *Verschiebung* I know is that of a *translation* in euclidean geometry.
> 
> It is probably from Witt vector terminology, where that is a standard term?

Thanks for the explanation! Indeed, that meaning of *Verschiebung* hasn't been present in my mind. But anyway, I would prefer a method name that doesn't dependent on any special context (and has more than just one letter). The `V` could by kept as an alias (together with an appropriate explanation). Opinions?



---

archive/issue_comments_034628.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2019-12-16T01:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34628",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034629.json:
```json
{
    "body": "I added a long form `verschiebung` to the Laurent series with `V` as an alias. I also brought the class up to our current framework with `UniqueRepresentation` and better use of the category framework. I also fixed a bunch of places in the doc and other misc code changes. There are still some doctests missing, but code-wise I think this is acceptable for inclusion (we can always make additional changes later).\n\nAlthough there is a substantial overlap with the code for Laurent series. I almost feel like we should just extend the Laurent series class with the necessary features with `_e` to avoid duplication (that one extra little bit of information shouldn't change the speed or have a real affect on memory).",
    "created_at": "2019-12-16T01:43:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34629",
    "user": "https://github.com/tscrim"
}
```

I added a long form `verschiebung` to the Laurent series with `V` as an alias. I also brought the class up to our current framework with `UniqueRepresentation` and better use of the category framework. I also fixed a bunch of places in the doc and other misc code changes. There are still some doctests missing, but code-wise I think this is acceptable for inclusion (we can always make additional changes later).

Although there is a substantial overlap with the code for Laurent series. I almost feel like we should just extend the Laurent series class with the necessary features with `_e` to avoid duplication (that one extra little bit of information shouldn't change the speed or have a real affect on memory).



---

archive/issue_comments_034630.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2019-12-21T18:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34630",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034631.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2019-12-21T19:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34631",
    "user": "https://github.com/soehms"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_034632.json:
```json
{
    "body": "Thanks for bringing this ahead that much, Travis!\n\nThe only tasks being left from my comment #33 are 3) and 5). With respect to the former item I rewrite `_repr_` such that it just transforms the representation string of the corresponding Laurent series. Concerning the latter I include the docs. They look well formatted.\n\nFurthermore I add some more doctests and fix the bugs I've detected along that. The `verschiebung` method did allow negative input on finite precision. I fixed that, as well. I've just realized that the `V` method in the `PowerSeries`-class is previous code. So, the naming has been overtaken from there. Shall we introduce the alias there, as well?\n\nFurthermore, I think we could speed up these methods (in `LaurentSeries` and `PowerSeries`) replacing the operations on the coefficient list by operations on the corresponding dictionaries. I made some tests and observed improvements up to 250 times faster. Shall I work that out?\n\n\n\n> Although there is a substantial overlap with the code for Laurent series. I almost feel like we should just extend the Laurent series class with the necessary features with _e to avoid duplication (that one extra little bit of information shouldn't change the speed or have a real affect on memory).\n\n\nDo you mean to make the Laurent series be Puiseux series with ramification index 1? I like this idea, but wouldn't this lead to larger changes in the Laurent series classes? Shall we deal with that in this ticket?",
    "created_at": "2019-12-21T19:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34632",
    "user": "https://github.com/soehms"
}
```

Thanks for bringing this ahead that much, Travis!

The only tasks being left from my comment #33 are 3) and 5). With respect to the former item I rewrite `_repr_` such that it just transforms the representation string of the corresponding Laurent series. Concerning the latter I include the docs. They look well formatted.

Furthermore I add some more doctests and fix the bugs I've detected along that. The `verschiebung` method did allow negative input on finite precision. I fixed that, as well. I've just realized that the `V` method in the `PowerSeries`-class is previous code. So, the naming has been overtaken from there. Shall we introduce the alias there, as well?

Furthermore, I think we could speed up these methods (in `LaurentSeries` and `PowerSeries`) replacing the operations on the coefficient list by operations on the corresponding dictionaries. I made some tests and observed improvements up to 250 times faster. Shall I work that out?



> Although there is a substantial overlap with the code for Laurent series. I almost feel like we should just extend the Laurent series class with the necessary features with _e to avoid duplication (that one extra little bit of information shouldn't change the speed or have a real affect on memory).


Do you mean to make the Laurent series be Puiseux series with ramification index 1? I like this idea, but wouldn't this lead to larger changes in the Laurent series classes? Shall we deal with that in this ticket?



---

archive/issue_comments_034633.json:
```json
{
    "body": "Replying to [comment:40 vdelecroix]:\n> Replying to [comment:28 vdelecroix]:\n> > An innocent operation like the following will multiply the memory footprint by 24 with no change in information\n> > {{{\n> > sage: p = prod(1 - q^n + O(q^100) for n in range(1,100))   # fine: 100 * coeff size\n> > sage: q^(1/24) * p   # bad: 100 * 24 * coeff size\n> > }}}\n> > The above example is the q-series expansion of the [Dedekind eta function](https://en.wikipedia.org/wiki/Dedekind_eta_function). There might be a more clever data structure to use as this kind of series is frequently encountered when dealing with modular forms.\n> \n> Concerning this example, you might want to read https://oscar.computeralgebra.de/blogs/2018/08/03/PuiseuxSeries/\n\n\nVincent, I had a look at that problem, again. Did you declare a sparse `PuiseuxSeriesRing`? How did you measure the consumption of memory? Declaring a sparse ring at least produces a 9 times smaller dump string:\n\n\n```\nsage: P.<q> = PuiseuxSeriesRing(ZZ)\nsage: p = prod((1 - q^n).add_bigoh(100) for n in range(1,100))\nsage: t = q^(1/24) * p\nsage: len(p.dumps())\n826\nsage: len(t.dumps())\n8688\n\nsage: P.<q> = PuiseuxSeriesRing(ZZ, sparse=True)\nsage: p = prod((1 - q^n).add_bigoh(100) for n in range(1,100))\nsage: t = q^(1/24) * p\nsage: len(p.dumps())\n903\nsage: len(t.dumps())\n923\n```\n\n\nI think, it would make sense to have the default on `sparse` to be `True` in the case of Puiseux series, since for non trivial ramification index its attached Laurent series is sparse by construction.\n\nBtw, in the blog you have linked to the ticket William Bruce Hart seems to have worked out his 'SageMath example' using a dense representation (see for example `R.<q> = PowerSeriesRing(ZZ, default_prec=9001)` and this citation \"Because of the dense representation in Sage, this would kill performance\"). A reason for this choice is not given. I guess that Sage would have produced better scores with a sparse representation.",
    "created_at": "2019-12-21T19:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34633",
    "user": "https://github.com/soehms"
}
```

Replying to [comment:40 vdelecroix]:
> Replying to [comment:28 vdelecroix]:
> > An innocent operation like the following will multiply the memory footprint by 24 with no change in information
> > {{{
> > sage: p = prod(1 - q^n + O(q^100) for n in range(1,100))   # fine: 100 * coeff size
> > sage: q^(1/24) * p   # bad: 100 * 24 * coeff size
> > }}}
> > The above example is the q-series expansion of the [Dedekind eta function](https://en.wikipedia.org/wiki/Dedekind_eta_function). There might be a more clever data structure to use as this kind of series is frequently encountered when dealing with modular forms.
> 
> Concerning this example, you might want to read https://oscar.computeralgebra.de/blogs/2018/08/03/PuiseuxSeries/


Vincent, I had a look at that problem, again. Did you declare a sparse `PuiseuxSeriesRing`? How did you measure the consumption of memory? Declaring a sparse ring at least produces a 9 times smaller dump string:


```
sage: P.<q> = PuiseuxSeriesRing(ZZ)
sage: p = prod((1 - q^n).add_bigoh(100) for n in range(1,100))
sage: t = q^(1/24) * p
sage: len(p.dumps())
826
sage: len(t.dumps())
8688

sage: P.<q> = PuiseuxSeriesRing(ZZ, sparse=True)
sage: p = prod((1 - q^n).add_bigoh(100) for n in range(1,100))
sage: t = q^(1/24) * p
sage: len(p.dumps())
903
sage: len(t.dumps())
923
```


I think, it would make sense to have the default on `sparse` to be `True` in the case of Puiseux series, since for non trivial ramification index its attached Laurent series is sparse by construction.

Btw, in the blog you have linked to the ticket William Bruce Hart seems to have worked out his 'SageMath example' using a dense representation (see for example `R.<q> = PowerSeriesRing(ZZ, default_prec=9001)` and this citation "Because of the dense representation in Sage, this would kill performance"). A reason for this choice is not given. I guess that Sage would have produced better scores with a sparse representation.



---

archive/issue_comments_034634.json:
```json
{
    "body": "Replying to [comment:50 soehms]:\n> The only tasks being left from my comment:33 are 3) and 5). With respect to the former item I rewrite `_repr_` such that it just transforms the representation string of the corresponding Laurent series. Concerning the latter I include the docs. They look well formatted.\n\nI didn't see your comment when I was making my changes. Thank you for taking care of it.\n\n> Furthermore I add some more doctests and fix the bugs I've detected along that. The `verschiebung` method did allow negative input on finite precision. I fixed that, as well. I've just realized that the `V` method in the `PowerSeries`-class is previous code. So, the naming has been overtaken from there. Shall we introduce the alias there, as well?\n\nThat would be something for a separate ticket (well, ideally adding such methods to the Laurent series should be done on another ticket as well, but it was already included here so, I continued to be lazy about it).\n\n> Furthermore, I think we could speed up these methods (in `LaurentSeries` and `PowerSeries`) replacing the operations on the coefficient list by operations on the corresponding dictionaries. I made some tests and observed improvements up to 250 times faster. Shall I work that out?\n\nPlease do, although that might depend on the sparsity too. However, I leave it to people who are more expert in the area to determine whether or not the default should be sparse or not.\n\n> > Although there is a substantial overlap with the code for Laurent series. I almost feel like we should just extend the Laurent series class with the necessary features with _e to avoid duplication (that one extra little bit of information shouldn't change the speed or have a real affect on memory).\n> \n> \n> Do you mean to make the Laurent series be Puiseux series with ramification index 1? I like this idea, but wouldn't this lead to larger changes in the Laurent series classes? Shall we deal with that in this ticket?\n\nYes, that is correct. It shouldn't require many changes I would think as it should be a matter of just (re)moving methods from the Laurent series and setting the Laurent series as a subclass. However, I haven't looked too closely at it.",
    "created_at": "2019-12-23T16:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34634",
    "user": "https://github.com/tscrim"
}
```

Replying to [comment:50 soehms]:
> The only tasks being left from my comment:33 are 3) and 5). With respect to the former item I rewrite `_repr_` such that it just transforms the representation string of the corresponding Laurent series. Concerning the latter I include the docs. They look well formatted.

I didn't see your comment when I was making my changes. Thank you for taking care of it.

> Furthermore I add some more doctests and fix the bugs I've detected along that. The `verschiebung` method did allow negative input on finite precision. I fixed that, as well. I've just realized that the `V` method in the `PowerSeries`-class is previous code. So, the naming has been overtaken from there. Shall we introduce the alias there, as well?

That would be something for a separate ticket (well, ideally adding such methods to the Laurent series should be done on another ticket as well, but it was already included here so, I continued to be lazy about it).

> Furthermore, I think we could speed up these methods (in `LaurentSeries` and `PowerSeries`) replacing the operations on the coefficient list by operations on the corresponding dictionaries. I made some tests and observed improvements up to 250 times faster. Shall I work that out?

Please do, although that might depend on the sparsity too. However, I leave it to people who are more expert in the area to determine whether or not the default should be sparse or not.

> > Although there is a substantial overlap with the code for Laurent series. I almost feel like we should just extend the Laurent series class with the necessary features with _e to avoid duplication (that one extra little bit of information shouldn't change the speed or have a real affect on memory).
> 
> 
> Do you mean to make the Laurent series be Puiseux series with ramification index 1? I like this idea, but wouldn't this lead to larger changes in the Laurent series classes? Shall we deal with that in this ticket?

Yes, that is correct. It shouldn't require many changes I would think as it should be a matter of just (re)moving methods from the Laurent series and setting the Laurent series as a subclass. However, I haven't looked too closely at it.



---

archive/issue_comments_034635.json:
```json
{
    "body": "Replying to [comment:52 tscrim]:\n> Replying to [comment:50 soehms]:\n> > Furthermore, I think we could speed up these methods (in `LaurentSeries` and `PowerSeries`) replacing the operations on the coefficient list by operations on the corresponding dictionaries. I made some tests and observed improvements up to 250 times faster. Shall I work that out?\n> \n> Please do, although that might depend on the sparsity too. However, I leave it to people who are more expert in the area to determine whether or not the default should be sparse or not.\n\nIn the meantime I've realized, that it isn't a good idea to have `sparse=True` as the default, since inversion (explicitly the method `inverse_series_trunc`) becomes very slow for this setting. Probably that's the reason why William Bruce Hurt worked with the dense representation.",
    "created_at": "2019-12-24T07:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34635",
    "user": "https://github.com/soehms"
}
```

Replying to [comment:52 tscrim]:
> Replying to [comment:50 soehms]:
> > Furthermore, I think we could speed up these methods (in `LaurentSeries` and `PowerSeries`) replacing the operations on the coefficient list by operations on the corresponding dictionaries. I made some tests and observed improvements up to 250 times faster. Shall I work that out?
> 
> Please do, although that might depend on the sparsity too. However, I leave it to people who are more expert in the area to determine whether or not the default should be sparse or not.

In the meantime I've realized, that it isn't a good idea to have `sparse=True` as the default, since inversion (explicitly the method `inverse_series_trunc`) becomes very slow for this setting. Probably that's the reason why William Bruce Hurt worked with the dense representation.



---

archive/issue_comments_034636.json:
```json
{
    "body": "Ticket retargeted after milestone closed",
    "created_at": "2019-12-30T14:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34636",
    "user": "https://github.com/embray"
}
```

Ticket retargeted after milestone closed



---

archive/issue_events_010512.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-12-30T14:48:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10512"
}
```



---

archive/issue_events_010513.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-12-30T14:48:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "milestone": "sage-9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10513"
}
```



---

archive/issue_comments_034637.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-01-12T15:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34637",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034638.json:
```json
{
    "body": "I do the following changes:\n\n1. I add a dependency to ticket #28239, since this bug of the Laurent series, becomes much more relevant for Puiseux series.\n\n2. I add the keyword `prec` to the _element constructor_, to achieve compatibility with the power series (see ticket #28993, but observe that my implementation is independent of that ticket).\n\n3. I let the Puiseux series be recognized by the global `bigoh` function `O`.\n\n4. I add the still missing doctests and do related small fixes.\n\n5. I insert missing copyright notes.\n\nConcerning the introduction of a scale factor according to comment 42, I've opened ticket #28992.",
    "created_at": "2020-01-12T15:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34638",
    "user": "https://github.com/soehms"
}
```

I do the following changes:

1. I add a dependency to ticket #28239, since this bug of the Laurent series, becomes much more relevant for Puiseux series.

2. I add the keyword `prec` to the _element constructor_, to achieve compatibility with the power series (see ticket #28993, but observe that my implementation is independent of that ticket).

3. I let the Puiseux series be recognized by the global `bigoh` function `O`.

4. I add the still missing doctests and do related small fixes.

5. I insert missing copyright notes.

Concerning the introduction of a scale factor according to comment 42, I've opened ticket #28992.



---

archive/issue_comments_034639.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-01-16T22:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34639",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034640.json:
```json
{
    "body": "The `EXAMPLES::` in `_coerce_map_from_` needs a blank line after it. Also, you are not passing `prec` in the `_element_constructor_` it seems. There might be some more comments later on.\n\nWe can include this implementation in since it is mostly in good shape without #28992 and then make the relevant changes here in that ticket. It would be good to at least have some implementation of Puiseux series, which we can then improve upon later.",
    "created_at": "2020-01-18T16:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34640",
    "user": "https://github.com/tscrim"
}
```

The `EXAMPLES::` in `_coerce_map_from_` needs a blank line after it. Also, you are not passing `prec` in the `_element_constructor_` it seems. There might be some more comments later on.

We can include this implementation in since it is mostly in good shape without #28992 and then make the relevant changes here in that ticket. It would be good to at least have some implementation of Puiseux series, which we can then improve upon later.



---

archive/issue_comments_034641.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-01-19T20:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34641",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034642.json:
```json
{
    "body": "Replying to [comment:58 tscrim]:\n\n\n> We can include this implementation in since it is mostly in good shape without #28992 and then make the relevant changes here in that ticket. It would be good to at least have some implementation of Puiseux series, which we can then improve upon later.\n\nI agree! Shall we switch to positive review, now?",
    "created_at": "2020-01-19T20:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34642",
    "user": "https://github.com/soehms"
}
```

Replying to [comment:58 tscrim]:


> We can include this implementation in since it is mostly in good shape without #28992 and then make the relevant changes here in that ticket. It would be good to at least have some implementation of Puiseux series, which we can then improve upon later.

I agree! Shall we switch to positive review, now?



---

archive/issue_comments_034643.json:
```json
{
    "body": "Unfortunately I have some more comments that I think should be addressed before a positive review:\n\nIn `_coerce_map_from_`:\n\n```diff\n         EXAMPLES::\n+\n             sage: R.<x> = PuiseuxSeriesRing(ZZ)\n```\n\n\nAlso, some small doc tweaks:\n\n```diff\n cdef class PuiseuxSeries(AlgebraElement):\n     r\"\"\"\n+    A Puiseux series.\n+\n     We store a Puiseux series\n```\n\nCommon practice is to have the `__init__` be the first method, and all of its doc should be moved to the class-level doc (with some formatting improvements done) with a `TestSuite(foo).run()` being in the `__init__`'s docstring.\n\nIIRC `long` is going away in Python3, and better overall I think would be a `size_t` for the `_e` attribute. Also, since `_l` is a Laurent series, shouldn't it also be a `LaurentSeries` object.\n\nWhy also is `laurent_part` a ``@`property` and not just a normal method? (I think `p.laurent_part()` is actually wrong because of this and should be `p.laurent_part`, but that is moot if that changes.)\n\nProbably good idea to break encapsulation and not have the function call here: `return self._l.laurent_polynomial()(t)` (i.e., just access the underlying polynomial).\n\nFor the `_richcmp_`, I think it would be a good idea to not call `V` on the underlying Laurent polynomials and instead implement a proper comparison as this will be significantly faster.\n\nI think we should change the MIT license to our standard license. I believe this is compatible.",
    "created_at": "2020-01-20T03:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34643",
    "user": "https://github.com/tscrim"
}
```

Unfortunately I have some more comments that I think should be addressed before a positive review:

In `_coerce_map_from_`:

```diff
         EXAMPLES::
+
             sage: R.<x> = PuiseuxSeriesRing(ZZ)
```


Also, some small doc tweaks:

```diff
 cdef class PuiseuxSeries(AlgebraElement):
     r"""
+    A Puiseux series.
+
     We store a Puiseux series
```

Common practice is to have the `__init__` be the first method, and all of its doc should be moved to the class-level doc (with some formatting improvements done) with a `TestSuite(foo).run()` being in the `__init__`'s docstring.

IIRC `long` is going away in Python3, and better overall I think would be a `size_t` for the `_e` attribute. Also, since `_l` is a Laurent series, shouldn't it also be a `LaurentSeries` object.

Why also is `laurent_part` a ``@`property` and not just a normal method? (I think `p.laurent_part()` is actually wrong because of this and should be `p.laurent_part`, but that is moot if that changes.)

Probably good idea to break encapsulation and not have the function call here: `return self._l.laurent_polynomial()(t)` (i.e., just access the underlying polynomial).

For the `_richcmp_`, I think it would be a good idea to not call `V` on the underlying Laurent polynomials and instead implement a proper comparison as this will be significantly faster.

I think we should change the MIT license to our standard license. I believe this is compatible.



---

archive/issue_comments_034644.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-01-21T17:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34644",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034645.json:
```json
{
    "body": "All your suggestions seem to be reasonable to me.",
    "created_at": "2020-01-21T17:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34645",
    "user": "https://github.com/soehms"
}
```

All your suggestions seem to be reasonable to me.



---

archive/issue_comments_034646.json:
```json
{
    "body": "Thank you. Some last little things: all `INPUT:` blocks should not end in a period/full-stop (unless it is really long). Also these specific changes:\n\n```diff\n         - ``prec`` -- (default: ``infinity``) the precision of the series\n-            as a rational number.\n+          as a rational number\n```\n\n\n```diff\n-    - ``parent`` -- Ring, the target parent.\n+    - ``parent`` -- the parent ring\n \n     - ``f``  -- one of the following types of inputs:\n-        - instance of :class:`PuiseuxSeries`\n-        - instance that can be coerced into the Laurent sersies ring of the parent.\n+\n+      * instance of :class:`PuiseuxSeries`\n+      * instance that can be coerced into the Laurent series ring of the parent\n \n-    - ``e`` -- integer (optional, default 1) for setting the ramification index.\n+    - ``e`` -- integer (default: 1); the ramification index\n```\n\n\n```diff\n     def __init__(self, parent, f, e=1):\n         r\"\"\"\n+        Initialize ``self``.\n+\n-        TESTS:\n+        TESTS::\n```\n\n\n```diff\n-Applies :meth:`shift` using the operator `<<`\n+Apply :meth:`shift` using the operator `<<`.\n```\n",
    "created_at": "2020-01-21T18:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34646",
    "user": "https://github.com/tscrim"
}
```

Thank you. Some last little things: all `INPUT:` blocks should not end in a period/full-stop (unless it is really long). Also these specific changes:

```diff
         - ``prec`` -- (default: ``infinity``) the precision of the series
-            as a rational number.
+          as a rational number
```


```diff
-    - ``parent`` -- Ring, the target parent.
+    - ``parent`` -- the parent ring
 
     - ``f``  -- one of the following types of inputs:
-        - instance of :class:`PuiseuxSeries`
-        - instance that can be coerced into the Laurent sersies ring of the parent.
+
+      * instance of :class:`PuiseuxSeries`
+      * instance that can be coerced into the Laurent series ring of the parent
 
-    - ``e`` -- integer (optional, default 1) for setting the ramification index.
+    - ``e`` -- integer (default: 1); the ramification index
```


```diff
     def __init__(self, parent, f, e=1):
         r"""
+        Initialize ``self``.
+
-        TESTS:
+        TESTS::
```


```diff
-Applies :meth:`shift` using the operator `<<`
+Apply :meth:`shift` using the operator `<<`.
```




---

archive/issue_comments_034647.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-01-22T07:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34647",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_034648.json:
```json
{
    "body": "Replying to [comment:64 tscrim]:\n> Thank you. Some last little things: \n\nDone!",
    "created_at": "2020-01-22T08:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34648",
    "user": "https://github.com/soehms"
}
```

Replying to [comment:64 tscrim]:
> Thank you. Some last little things: 

Done!



---

archive/issue_comments_034649.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-01-22T12:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34649",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034650.json:
```json
{
    "body": "Thank you. Positive review.",
    "created_at": "2020-01-22T12:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34650",
    "user": "https://github.com/tscrim"
}
```

Thank you. Positive review.



---

archive/issue_comments_034651.json:
```json
{
    "body": "Thanks a lot, as well!",
    "created_at": "2020-01-22T16:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34651",
    "user": "https://github.com/soehms"
}
```

Thanks a lot, as well!



---

archive/issue_events_010514.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2020-01-25T17:27:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4618#event-10514"
}
```



---

archive/issue_comments_034652.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-01-25T17:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34652",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_034653.json:
```json
{
    "body": "Did this also solve #9289 (Implement Puiseux polynomials)?",
    "created_at": "2020-07-15T02:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34653",
    "user": "https://github.com/slel"
}
```

Did this also solve #9289 (Implement Puiseux polynomials)?



---

archive/issue_comments_034654.json:
```json
{
    "body": "Replying to [comment:70 slelievre]:\n> Did this also solve #9289 (Implement Puiseux polynomials)?\n\nImplicitly, but not really since we should have a dedicated parent and element for the polynomials.",
    "created_at": "2020-07-15T02:30:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34654",
    "user": "https://github.com/tscrim"
}
```

Replying to [comment:70 slelievre]:
> Did this also solve #9289 (Implement Puiseux polynomials)?

Implicitly, but not really since we should have a dedicated parent and element for the polynomials.



---

archive/issue_comments_034655.json:
```json
{
    "body": "Replying to [comment:71 tscrim]:\n> Replying to [comment:70 slelievre]:\n> > Did this also solve #9289 (Implement Puiseux polynomials)?\n> \n> Implicitly, but not really since we should have a dedicated parent and element for the polynomials.\n\nBut maybe it's a good idea to have the implementation of the Puiseux polynomial rely as much as possible on the Puiseux series. That would avoid having a lot of duplicated code. At the moment the code attached to ticket #9289 is not far away from being copy pasted from the corresponding classes for Laurent polynomials with some name refactoring done. So we would not loose that much if we decide to implement the Puiseux polynomials as \"restricted Puiseux series\".\n\nWhat is standing against that?",
    "created_at": "2020-07-15T21:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34655",
    "user": "https://github.com/soehms"
}
```

Replying to [comment:71 tscrim]:
> Replying to [comment:70 slelievre]:
> > Did this also solve #9289 (Implement Puiseux polynomials)?
> 
> Implicitly, but not really since we should have a dedicated parent and element for the polynomials.

But maybe it's a good idea to have the implementation of the Puiseux polynomial rely as much as possible on the Puiseux series. That would avoid having a lot of duplicated code. At the moment the code attached to ticket #9289 is not far away from being copy pasted from the corresponding classes for Laurent polynomials with some name refactoring done. So we would not loose that much if we decide to implement the Puiseux polynomials as "restricted Puiseux series".

What is standing against that?



---

archive/issue_comments_034656.json:
```json
{
    "body": "That would work, but it would likely be slow. I think the thing to do is follow the same pattern as here: extend the Laurent polynomials by wrapping them as a Puiseux polynomial with the ramification index and associated methods. Perhaps to avoid some code duplication, one could be clever with a template class or common ABC.",
    "created_at": "2020-07-17T03:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34656",
    "user": "https://github.com/tscrim"
}
```

That would work, but it would likely be slow. I think the thing to do is follow the same pattern as here: extend the Laurent polynomials by wrapping them as a Puiseux polynomial with the ramification index and associated methods. Perhaps to avoid some code duplication, one could be clever with a template class or common ABC.



---

archive/issue_comments_034657.json:
```json
{
    "body": "Replying to [comment:73 tscrim]:\n> That would work, but it would likely be slow. \n\nTravis, I don't see the point of what would make that noticeable slower. I think all calculation that could harm performance will be executed inside polynomial classes independent on how we translate it to them. A little bit more time used for the translation because there is one step more cannot amount that much.\n\nWhat I have in mind is similar to how I did the embedding of the localization into the fraction field (via a value attribute). In the meantime I've seen that there is a special class `ElementWrapper` for such constructions (I hadn't been aware of it when implementing the localization).",
    "created_at": "2020-07-17T22:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34657",
    "user": "https://github.com/soehms"
}
```

Replying to [comment:73 tscrim]:
> That would work, but it would likely be slow. 

Travis, I don't see the point of what would make that noticeable slower. I think all calculation that could harm performance will be executed inside polynomial classes independent on how we translate it to them. A little bit more time used for the translation because there is one step more cannot amount that much.

What I have in mind is similar to how I did the embedding of the localization into the fraction field (via a value attribute). In the meantime I've seen that there is a special class `ElementWrapper` for such constructions (I hadn't been aware of it when implementing the localization).



---

archive/issue_comments_034658.json:
```json
{
    "body": "It is a bit more than that one step. IIRC, there are also a lot more optimizations than can and are done for polynomials that are not available for power series. For one, they don't have to worry about precision. So arithmetic starts to get bogged down by this. Plus that extra level of indirection does add a bit of time (also in creating the extra elements, which is much slower than the function call). While it is not much, perhaps 2-5%, because arithmetic operations are often used in tight loops (and frequently), this can have an outsized impact on algorithm run times.",
    "created_at": "2020-07-17T23:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34658",
    "user": "https://github.com/tscrim"
}
```

It is a bit more than that one step. IIRC, there are also a lot more optimizations than can and are done for polynomials that are not available for power series. For one, they don't have to worry about precision. So arithmetic starts to get bogged down by this. Plus that extra level of indirection does add a bit of time (also in creating the extra elements, which is much slower than the function call). While it is not much, perhaps 2-5%, because arithmetic operations are often used in tight loops (and frequently), this can have an outsized impact on algorithm run times.



---

archive/issue_comments_034659.json:
```json
{
    "body": "Replying to [comment:75 tscrim]:\n\n\nThanks for the explanations! I will think about your suggestion to capsule common functionalities in a template class. Do you mean a class that will be put in between `CommutativeAlgebraElement` and `PuiseuxPolynomial` repectively in between  `AlgebraElement` and `PuiseuxSeries`? But maybe, we should have done #28992 before.\n\nBTW: is there a special reason why the series are not inherited from `CommutativeAlgebraElement`?",
    "created_at": "2020-07-22T13:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34659",
    "user": "https://github.com/soehms"
}
```

Replying to [comment:75 tscrim]:


Thanks for the explanations! I will think about your suggestion to capsule common functionalities in a template class. Do you mean a class that will be put in between `CommutativeAlgebraElement` and `PuiseuxPolynomial` repectively in between  `AlgebraElement` and `PuiseuxSeries`? But maybe, we should have done #28992 before.

BTW: is there a special reason why the series are not inherited from `CommutativeAlgebraElement`?



---

archive/issue_comments_034660.json:
```json
{
    "body": "There is the `Polynomial` class IIRC, but between that and `PuiseuxPolynomial`, yes. It would mostly be the Laurent polynomial code with the rammification index, but for the more time critical operations, it would just use the fact that the index is `1`. Hopefully this would be minimal, but definitely all of the arithmetic operations would fall under this.",
    "created_at": "2020-07-24T00:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34660",
    "user": "https://github.com/tscrim"
}
```

There is the `Polynomial` class IIRC, but between that and `PuiseuxPolynomial`, yes. It would mostly be the Laurent polynomial code with the rammification index, but for the more time critical operations, it would just use the fact that the index is `1`. Hopefully this would be minimal, but definitely all of the arithmetic operations would fall under this.



---

archive/issue_comments_034661.json:
```json
{
    "body": "I also don't remember if there was some specific reason why it doesn't.",
    "created_at": "2020-07-24T00:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4618#issuecomment-34661",
    "user": "https://github.com/tscrim"
}
```

I also don't remember if there was some specific reason why it doesn't.
