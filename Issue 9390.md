# Issue 9390: is_galois_relative() not always right

archive/issues_009390.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  cturner @mstreng\n\nKeywords: galois extension\n\nIn 4.4.4 the following code produces a number field which is Galois over the rationals but (allegedly) not over an intermediate field.\n\n\n```\nsage: K.<a>=NumberField(x^2+1)\nsage: Kt.<t> = K[]\nsage: L.<b> = K.extension(t^3-3*t-1)\nsage: L.is_galois_absolute()\nTrue\nsage: L.is_galois_relative()\nFalse\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9390\n\n",
    "created_at": "2010-06-30T04:33:44Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "is_galois_relative() not always right",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9390",
    "user": "https://github.com/arminstraub"
}
```
Assignee: @loefflerd

CC:  cturner @mstreng

Keywords: galois extension

In 4.4.4 the following code produces a number field which is Galois over the rationals but (allegedly) not over an intermediate field.


```
sage: K.<a>=NumberField(x^2+1)
sage: Kt.<t> = K[]
sage: L.<b> = K.extension(t^3-3*t-1)
sage: L.is_galois_absolute()
True
sage: L.is_galois_relative()
False
```



Issue created by migration from https://trac.sagemath.org/ticket/9390





---

archive/issue_comments_089247.json:
```json
{
    "body": "This fails because the present definition for relative number fields:\n\n\n```\ndef is_galois_relative(self):\n    return self.Hom(self).order() == self.relative_degree()\n```\n\nis completely wrong.  In the case above\n\n\n```\nsage: L.Hom(L).order()\n6\n```\n\nwhile the relative degree is 3.  Clearly the Homset contains all endomorphisms of of L, not just the relative ones.  One obvious possibility would be to count those endomorphisms which fix the base field.  But the following might be better\n\n\n```\ndef is_galois_relative(self):\n    rel_poly = self.relative_polynomial()\n    return len(rel_poly.base_extend(self).factor()) == self.relative_degree()\n\n```\n\nI'll do some testing and post a patch later today.",
    "created_at": "2010-06-30T07:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89247",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

This fails because the present definition for relative number fields:


```
def is_galois_relative(self):
    return self.Hom(self).order() == self.relative_degree()
```

is completely wrong.  In the case above


```
sage: L.Hom(L).order()
6
```

while the relative degree is 3.  Clearly the Homset contains all endomorphisms of of L, not just the relative ones.  One obvious possibility would be to count those endomorphisms which fix the base field.  But the following might be better


```
def is_galois_relative(self):
    rel_poly = self.relative_polynomial()
    return len(rel_poly.base_extend(self).factor()) == self.relative_degree()

```

I'll do some testing and post a patch later today.



---

archive/issue_comments_089248.json:
```json
{
    "body": "After a rather longer than expected delay, I'm attaching a patch which gives correct results for `is_galois_relative`.  I've also rewritten `is_galois_absolute` using a corresponding algorithm because it is (i) faster than the existing code, and (ii) capable of handling extension of larger degree.",
    "created_at": "2010-12-10T15:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89248",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

After a rather longer than expected delay, I'm attaching a patch which gives correct results for `is_galois_relative`.  I've also rewritten `is_galois_absolute` using a corresponding algorithm because it is (i) faster than the existing code, and (ii) capable of handling extension of larger degree.



---

archive/issue_comments_089249.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-10T15:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89249",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089250.json:
```json
{
    "body": "Attachment [trac_9390.patch](tarball://root/attachments/some-uuid/ticket9390/trac_9390.patch) by fwclarke created at 2010-12-10 15:07:28",
    "created_at": "2010-12-10T15:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89250",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_9390.patch](tarball://root/attachments/some-uuid/ticket9390/trac_9390.patch) by fwclarke created at 2010-12-10 15:07:28



---

archive/issue_comments_089251.json:
```json
{
    "body": "Nice, that is a lot faster, and correct. There is one thing I don't like though: you introduced a difference between `is_galois` of absolute number fields and `is_galois_absolute` of relative number fields:\n\nWith your patch on Sage 4.6.1.alpha2:\n\n```\nsage: M.<c> = NumberField(cyclotomic_polynomial(100))\nsage: M\nNumber Field in c with defining polynomial x^40 - x^30 + x^20 - x^10 + 1\nsage: M.is_galois()\nNotImplementedError\nsage: M.relativize(1, 'd').is_galois_absolute()\nTrue\nsage: M.relativize(1, 'd').is_galois_relative()\nTrue\n```\n\nWithout your patch, it is NotImplementedError, NotImplementedError, False, so your patch is a definite improvement, but could be better.\n\nI think it would be better to put your new code in `is_galois` of absolute fields instead of `is_galois_absolute` of relative fields. Then `is_galois_absolute()` can simply call `self.absolute_field().is_galois()`\n\nPS grammar: line 1177 of number_field_rel.py after the patch, previous should be previously (or simply replace the line by \"Check that bug #9390 is fixed::\")",
    "created_at": "2010-12-13T12:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89251",
    "user": "https://github.com/mstreng"
}
```

Nice, that is a lot faster, and correct. There is one thing I don't like though: you introduced a difference between `is_galois` of absolute number fields and `is_galois_absolute` of relative number fields:

With your patch on Sage 4.6.1.alpha2:

```
sage: M.<c> = NumberField(cyclotomic_polynomial(100))
sage: M
Number Field in c with defining polynomial x^40 - x^30 + x^20 - x^10 + 1
sage: M.is_galois()
NotImplementedError
sage: M.relativize(1, 'd').is_galois_absolute()
True
sage: M.relativize(1, 'd').is_galois_relative()
True
```

Without your patch, it is NotImplementedError, NotImplementedError, False, so your patch is a definite improvement, but could be better.

I think it would be better to put your new code in `is_galois` of absolute fields instead of `is_galois_absolute` of relative fields. Then `is_galois_absolute()` can simply call `self.absolute_field().is_galois()`

PS grammar: line 1177 of number_field_rel.py after the patch, previous should be previously (or simply replace the line by "Check that bug #9390 is fixed::")



---

archive/issue_events_023168.json:
```json
{
    "actor": "https://github.com/mstreng",
    "created_at": "2010-12-13T12:10:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "milestone": "sage-4.6.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9390#event-23168"
}
```



---

archive/issue_comments_089252.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-13T12:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89252",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089253.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-16T08:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89253",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089254.json:
```json
{
    "body": "Replying to [comment:4 mstreng]:\n\n> I think it would be better to put your new code in `is_galois` of absolute fields instead of `is_galois_absolute` of relative fields. Then `is_galois_absolute()` can simply call `self.absolute_field().is_galois()`\n\nI've done this in a new replacement patch, and dealt with the grammatical point you raised.\n\nIt was also necessary to make a minor change to an unconnected doctest. \u00a0This is because of PARI's inconsistent behaviour when choosing ideal generators.  The same issue arose in #5842.",
    "created_at": "2010-12-16T08:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89254",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:4 mstreng]:

> I think it would be better to put your new code in `is_galois` of absolute fields instead of `is_galois_absolute` of relative fields. Then `is_galois_absolute()` can simply call `self.absolute_field().is_galois()`

I've done this in a new replacement patch, and dealt with the grammatical point you raised.

It was also necessary to make a minor change to an unconnected doctest.  This is because of PARI's inconsistent behaviour when choosing ideal generators.  The same issue arose in #5842.



---

archive/issue_comments_089255.json:
```json
{
    "body": "Attachment [trac_9390-replacement.patch](tarball://root/attachments/some-uuid/ticket9390/trac_9390-replacement.patch) by fwclarke created at 2010-12-16 08:37:06\n\nReplaces previous patch",
    "created_at": "2010-12-16T08:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89255",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_9390-replacement.patch](tarball://root/attachments/some-uuid/ticket9390/trac_9390-replacement.patch) by fwclarke created at 2010-12-16 08:37:06

Replaces previous patch



---

archive/issue_comments_089256.json:
```json
{
    "body": "On which Sage version is this a speedup for is_galois_absolute?\n\nWith Sage 4.6.1.alpha2 and no patches\n\n```\nsage: K.<a>=NumberField(x^2+1)\nsage: Kt.<t> = K[]\nsage: L.<b> = K.extension(t^3-3*t-1)\nsage: M.<c> = L.absolute_field()\nsage: time L.is_galois_absolute()\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.00 s\nTrue\nsage: time L.is_galois_relative()\nCPU times: user 0.08 s, sys: 0.00 s, total: 0.08 s\nWall time: 0.08 s\nFalse\nsage: time M.is_galois()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\nTrue\n```\n\n\nSame version, but with your patch:\n\n```\nsage: K.<a>=NumberField(x^2+1)\nsage: Kt.<t> = K[]\nsage: L.<b> = K.extension(t^3-3*t-1)\nsage: M.<c> = L.absolute_field()\nsage: time L.is_galois_absolute()\nCPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s\nWall time: 0.04 s\nTrue\nsage: time L.is_galois_relative()\nCPU times: user 0.04 s, sys: 0.01 s, total: 0.05 s\nWall time: 0.05 s\nTrue\nsage: time M.is_galois()\nCPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s\nWall time: 0.03 s\nTrue\n```\n\nSo you did correct (and apparently speed up) is_galois_relative. However, it seems to slow down is_galois and is_galois_absolute. This gets worse if you use is_galois multiple times for the same field, as the old version uses cached data and your version doesn't:\n\nWithout patch:\n\n```\nsage: K.<b> = NumberField(cyclotomic_polynomial(11))\nsage: time K.is_galois()\nCPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s\nWall time: 0.02 s\nTrue\nsage: time [K.is_galois() for i in range(500)];\nCPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s\nWall time: 0.03 s\n```\n\nWith patch:\n\n```\nsage: K.<b> = NumberField(cyclotomic_polynomial(11))\nsage: time K.is_galois()\nCPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s\nWall time: 0.06 s\nTrue\nsage: time [K.is_galois() for i in range(500)];\nCPU times: user 11.66 s, sys: 0.05 s, total: 11.71 s\nWall time: 11.72 s\n```\n\nI'm very sorry for not noticing this earlier and for letting you do make the changes you did after my first review.\n\nOn the other hand, my suggestion allowed for a good test of your code, as is_galois is ubiquitous:\n\n```\nsage -t -long devel/sage/sage/schemes/elliptic_curves/gal_reps.py\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n```\n\n\nMaybe it is better to stick with the is_galois_relative correction only.\n\nAlso, if you know about cached methods, then perhaps you could make is_galois_relative and is_galois_absolute cached while you're at it.\n\nYou can also make a distinction in is_galois between degree <= 11 (use the old method) and degree > 11 (old method only works if KASH is installed, use your method).\n\nI suppose it is good to still let is_galois_absolute() simply call absolute_field().is_galois().",
    "created_at": "2010-12-16T14:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89256",
    "user": "https://github.com/mstreng"
}
```

On which Sage version is this a speedup for is_galois_absolute?

With Sage 4.6.1.alpha2 and no patches

```
sage: K.<a>=NumberField(x^2+1)
sage: Kt.<t> = K[]
sage: L.<b> = K.extension(t^3-3*t-1)
sage: M.<c> = L.absolute_field()
sage: time L.is_galois_absolute()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.00 s
True
sage: time L.is_galois_relative()
CPU times: user 0.08 s, sys: 0.00 s, total: 0.08 s
Wall time: 0.08 s
False
sage: time M.is_galois()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
True
```


Same version, but with your patch:

```
sage: K.<a>=NumberField(x^2+1)
sage: Kt.<t> = K[]
sage: L.<b> = K.extension(t^3-3*t-1)
sage: M.<c> = L.absolute_field()
sage: time L.is_galois_absolute()
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.04 s
True
sage: time L.is_galois_relative()
CPU times: user 0.04 s, sys: 0.01 s, total: 0.05 s
Wall time: 0.05 s
True
sage: time M.is_galois()
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.03 s
True
```

So you did correct (and apparently speed up) is_galois_relative. However, it seems to slow down is_galois and is_galois_absolute. This gets worse if you use is_galois multiple times for the same field, as the old version uses cached data and your version doesn't:

Without patch:

```
sage: K.<b> = NumberField(cyclotomic_polynomial(11))
sage: time K.is_galois()
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
True
sage: time [K.is_galois() for i in range(500)];
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.03 s
```

With patch:

```
sage: K.<b> = NumberField(cyclotomic_polynomial(11))
sage: time K.is_galois()
CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
Wall time: 0.06 s
True
sage: time [K.is_galois() for i in range(500)];
CPU times: user 11.66 s, sys: 0.05 s, total: 11.71 s
Wall time: 11.72 s
```

I'm very sorry for not noticing this earlier and for letting you do make the changes you did after my first review.

On the other hand, my suggestion allowed for a good test of your code, as is_galois is ubiquitous:

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/gal_reps.py
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
```


Maybe it is better to stick with the is_galois_relative correction only.

Also, if you know about cached methods, then perhaps you could make is_galois_relative and is_galois_absolute cached while you're at it.

You can also make a distinction in is_galois between degree <= 11 (use the old method) and degree > 11 (old method only works if KASH is installed, use your method).

I suppose it is good to still let is_galois_absolute() simply call absolute_field().is_galois().



---

archive/issue_comments_089257.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-16T14:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89257",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089258.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-16T21:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89258",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089259.json:
```json
{
    "body": "Replying to [comment:6 mstreng]:\n\n> On which Sage version is this a speedup for is_galois_absolute? ...\n\nI'm sorry about this.  I don't know how I convinced myself that the absolute version was faster.\n\n> On the other hand, my suggestion allowed for a good test of your code, as is_galois is ubiquitous:\n\n```\nsage -t -long devel/sage/sage/schemes/elliptic_curves/gal_reps.py\n *** *** Error: TIMED OUT! PROCESS KILLED! *** *** \n```\n\n\nI can't reproduce this.  Actually `is_galois` is not particularly ubiquitous (and certainly does figure in `gal_reps.py`):\n\n\n```\nsage -grep -l is_galois\n----------------------------------------------------------------------\n----------------------------------------------------------------------\ncoding/linear_code.py\nrings/number_field/galois_group.py\nrings/number_field/number_field.py\nrings/number_field/number_field_rel.py\nrings/number_field/totallyreal_rel.py\nrings/padics/unramified_extension_generic.py\nrings/number_field/number_field_element.pyx\n```\n\n> Maybe it is better to stick with the is_galois_relative correction only.  Also, if you know about cached methods, then perhaps you could make is_galois_relative and is_galois_absolute cached while you're at it. You can also make a distinction in is_galois between degree <= 11 (use the old method) and degree > 11 (old method only works if KASH is installed, use your method). I suppose it is good to still let is_galois_absolute() simply call absolute_field().is_galois().\n| Sage Version 4.6, Release Date: 2010-10-30                         |\n| Type notebook() for the GUI, and license() for information.        |\nThe new patch implements this, except it doesn't do any caching.  `is_galois_absolute` is already cached in the degree <= 11 cases via `self.absolute_field()`.  In the other cases, I think what really needs caching is the factorisation of the defining polynomial over `self,` since it's also what's needed to compute endomorphisms. But that is for another patch, I think.",
    "created_at": "2010-12-16T21:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89259",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:6 mstreng]:

> On which Sage version is this a speedup for is_galois_absolute? ...

I'm sorry about this.  I don't know how I convinced myself that the absolute version was faster.

> On the other hand, my suggestion allowed for a good test of your code, as is_galois is ubiquitous:

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/gal_reps.py
 *** *** Error: TIMED OUT! PROCESS KILLED! *** *** 
```


I can't reproduce this.  Actually `is_galois` is not particularly ubiquitous (and certainly does figure in `gal_reps.py`):


```
sage -grep -l is_galois
----------------------------------------------------------------------
----------------------------------------------------------------------
coding/linear_code.py
rings/number_field/galois_group.py
rings/number_field/number_field.py
rings/number_field/number_field_rel.py
rings/number_field/totallyreal_rel.py
rings/padics/unramified_extension_generic.py
rings/number_field/number_field_element.pyx
```

> Maybe it is better to stick with the is_galois_relative correction only.  Also, if you know about cached methods, then perhaps you could make is_galois_relative and is_galois_absolute cached while you're at it. You can also make a distinction in is_galois between degree <= 11 (use the old method) and degree > 11 (old method only works if KASH is installed, use your method). I suppose it is good to still let is_galois_absolute() simply call absolute_field().is_galois().
| Sage Version 4.6, Release Date: 2010-10-30                         |
| Type notebook() for the GUI, and license() for information.        |
The new patch implements this, except it doesn't do any caching.  `is_galois_absolute` is already cached in the degree <= 11 cases via `self.absolute_field()`.  In the other cases, I think what really needs caching is the factorisation of the defining polynomial over `self,` since it's also what's needed to compute endomorphisms. But that is for another patch, I think.



---

archive/issue_comments_089260.json:
```json
{
    "body": "Replaces previous two patches",
    "created_at": "2010-12-16T21:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89260",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replaces previous two patches



---

archive/issue_comments_089261.json:
```json
{
    "body": "Attachment [trac_9390-2nd_replacement.patch](tarball://root/attachments/some-uuid/ticket9390/trac_9390-2nd_replacement.patch) by @mstreng created at 2010-12-17 11:49:08\n\nReplying to [comment:7 fwclarke]:\n> I can't reproduce this.  Actually `is_galois` is not particularly ubiquitous (and certainly does figure in `gal_reps.py`):\n\nHow could you be so sure about that? The timeout is caused by the long test `EllipticCurve([1,-1,0,-107,-379]).galois_representation().image_type(7)`\nThe image_type() part runs forever on 4.6.1.alpha2 with your second patch, and is quite fast without any patches. That method is a long piece of code, so I didn't read it all, but it does suggest that it uses is_galois somewhere via another function.",
    "created_at": "2010-12-17T11:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89261",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_9390-2nd_replacement.patch](tarball://root/attachments/some-uuid/ticket9390/trac_9390-2nd_replacement.patch) by @mstreng created at 2010-12-17 11:49:08

Replying to [comment:7 fwclarke]:
> I can't reproduce this.  Actually `is_galois` is not particularly ubiquitous (and certainly does figure in `gal_reps.py`):

How could you be so sure about that? The timeout is caused by the long test `EllipticCurve([1,-1,0,-107,-379]).galois_representation().image_type(7)`
The image_type() part runs forever on 4.6.1.alpha2 with your second patch, and is quite fast without any patches. That method is a long piece of code, so I didn't read it all, but it does suggest that it uses is_galois somewhere via another function.



---

archive/issue_comments_089262.json:
```json
{
    "body": "Replying to [comment:8 mstreng]:\n\n> > I can't reproduce this.  Actually `is_galois` is not particularly ubiquitous (and certainly does figure in `gal_reps.py`):\n> How could you be so sure about that?\n\nMy mistake was that I was using 4.6.  The long test in question was introduced in #8451 which was merged in sage-4.6.1.alpha2.  I haven't checked it fully, but it looks like in this case the function `image_type` calls `galois_group`, which calls `is_galois`.  It seem that `is_galois` is much more ubiquitous that I thought as it's used in several functions of the classes `GaloisGroup_v2` and `GaloisGroupElement`.  Sorry for not noticing this before.",
    "created_at": "2010-12-17T12:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89262",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:8 mstreng]:

> > I can't reproduce this.  Actually `is_galois` is not particularly ubiquitous (and certainly does figure in `gal_reps.py`):
> How could you be so sure about that?

My mistake was that I was using 4.6.  The long test in question was introduced in #8451 which was merged in sage-4.6.1.alpha2.  I haven't checked it fully, but it looks like in this case the function `image_type` calls `galois_group`, which calls `is_galois`.  It seem that `is_galois` is much more ubiquitous that I thought as it's used in several functions of the classes `GaloisGroup_v2` and `GaloisGroupElement`.  Sorry for not noticing this before.



---

archive/issue_comments_089263.json:
```json
{
    "body": "Strange: I remove all patches, build, and the long gal_reps.py test is fine, then I apply your latest patch, build, and it times out again after 1800 seconds.\n\nThe only thing I could think of is that (somewhere in a function called by `EllipticCurve([1,-1,0,-107,-379]).galois_representation().image_type(7)`) an Error of is_galois with degree > 11 is raised and handled in some way. With your patch, that computation will just go on and on.\n\nOr there is something wrong with my sage installation. Can anyone reproduce this increase in test time? (4.6.1.alpha2 with no other patches applied)\n\nFor [buildbot](http://wiki.sagemath.org/buildbot):\n\nApply trac_9390-2nd_replacement.patch",
    "created_at": "2010-12-18T22:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89263",
    "user": "https://github.com/mstreng"
}
```

Strange: I remove all patches, build, and the long gal_reps.py test is fine, then I apply your latest patch, build, and it times out again after 1800 seconds.

The only thing I could think of is that (somewhere in a function called by `EllipticCurve([1,-1,0,-107,-379]).galois_representation().image_type(7)`) an Error of is_galois with degree > 11 is raised and handled in some way. With your patch, that computation will just go on and on.

Or there is something wrong with my sage installation. Can anyone reproduce this increase in test time? (4.6.1.alpha2 with no other patches applied)

For [buildbot](http://wiki.sagemath.org/buildbot):

Apply trac_9390-2nd_replacement.patch



---

archive/issue_comments_089264.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-19T21:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89264",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089265.json:
```json
{
    "body": "Replying to [comment:10 mstreng]:\n> The only thing I could think of is that (somewhere in a function called by `EllipticCurve([1,-1,0,-107,-379]).galois_representation().image_type(7)`) an Error of is_galois with degree > 11 is raised and handled in some way. With your patch, that computation will just go on and on.\n\nSame problem with a fresh install.\n\nActually, something fishy happens in image_type(7). Without your patch, it outputs `'The image is a group of order 36.'` quickly. With your patch, it goes on and on, until I press Ctrl+C, in which case it catches my KeyboardInterrupt and outputs `'The image is a group of order 36.'` without showing me any Error! So image_type catches all errors, which is why it stops working with your improvement.\n\nSorry, but that means this patch can't go in the way it is: either fix gal_reps or don't touch is_galois.",
    "created_at": "2010-12-19T21:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89265",
    "user": "https://github.com/mstreng"
}
```

Replying to [comment:10 mstreng]:
> The only thing I could think of is that (somewhere in a function called by `EllipticCurve([1,-1,0,-107,-379]).galois_representation().image_type(7)`) an Error of is_galois with degree > 11 is raised and handled in some way. With your patch, that computation will just go on and on.

Same problem with a fresh install.

Actually, something fishy happens in image_type(7). Without your patch, it outputs `'The image is a group of order 36.'` quickly. With your patch, it goes on and on, until I press Ctrl+C, in which case it catches my KeyboardInterrupt and outputs `'The image is a group of order 36.'` without showing me any Error! So image_type catches all errors, which is why it stops working with your improvement.

Sorry, but that means this patch can't go in the way it is: either fix gal_reps or don't touch is_galois.



---

archive/issue_comments_089266.json:
```json
{
    "body": "With the #8451 patch, and with `is_galois` unchanged,  I find\n\n\n```\nsage: set_verbose(1)\nsage: EllipticCurve([1, -1, 0, -107, -379]).galois_representation().image_type(7)\nverbose 1 (1326: free_module.py, coordinate_module) rational in-place Gauss elimination on 0 x 0 matrix\n...\nverbose 1 (811: gal_reps.py, image_type) field of degree 36.  try to compute galois group (time = 14.321421)\n'The image is a group of order 36.'\n```\n\nderiving from the following lines in `gal_reps.py` (as patched by #8451):\n\n\n```\n        if p <= 13:\n            K = _division_field(self.E,p)\n            d = K.absolute_degree()\n\n            misc.verbose(\"field of degree %s.  try to compute galois group\"%(d),2)\n            try:\n                G = K.galois_group()\n            except:\n                self.__image_type[p] = \"The image is a group of order %s.\"%d\n                return self.__image_type[p]\n```\n\nSo what's happening is that `K.is_galois()` (called via `K.galois_group()`) is taking ages when my patch is implemented.  The unqualified `except:` is then catching the keyboard interrupt.  But with the existing implementation of `is_galois` applied to the degree 36 field in question, a `NotImplementedError` is raised and caught.\n\nAnyway, as you suggest, the way forward is a minimal patch which only changes  `is_galois_relative`.  I'm attaching this.",
    "created_at": "2010-12-20T19:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89266",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

With the #8451 patch, and with `is_galois` unchanged,  I find


```
sage: set_verbose(1)
sage: EllipticCurve([1, -1, 0, -107, -379]).galois_representation().image_type(7)
verbose 1 (1326: free_module.py, coordinate_module) rational in-place Gauss elimination on 0 x 0 matrix
...
verbose 1 (811: gal_reps.py, image_type) field of degree 36.  try to compute galois group (time = 14.321421)
'The image is a group of order 36.'
```

deriving from the following lines in `gal_reps.py` (as patched by #8451):


```
        if p <= 13:
            K = _division_field(self.E,p)
            d = K.absolute_degree()

            misc.verbose("field of degree %s.  try to compute galois group"%(d),2)
            try:
                G = K.galois_group()
            except:
                self.__image_type[p] = "The image is a group of order %s."%d
                return self.__image_type[p]
```

So what's happening is that `K.is_galois()` (called via `K.galois_group()`) is taking ages when my patch is implemented.  The unqualified `except:` is then catching the keyboard interrupt.  But with the existing implementation of `is_galois` applied to the degree 36 field in question, a `NotImplementedError` is raised and caught.

Anyway, as you suggest, the way forward is a minimal patch which only changes  `is_galois_relative`.  I'm attaching this.



---

archive/issue_comments_089267.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-20T19:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89267",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089268.json:
```json
{
    "body": "Attachment [trac_9390-3rd_replacement.patch](tarball://root/attachments/some-uuid/ticket9390/trac_9390-3rd_replacement.patch) by fwclarke created at 2010-12-20 19:31:51\n\nReplaces previous three patches",
    "created_at": "2010-12-20T19:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89268",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_9390-3rd_replacement.patch](tarball://root/attachments/some-uuid/ticket9390/trac_9390-3rd_replacement.patch) by fwclarke created at 2010-12-20 19:31:51

Replaces previous three patches



---

archive/issue_comments_089269.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-21T11:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89269",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089270.json:
```json
{
    "body": "Too bad about the improvements to is_galois. I suppose that code from trac_9390-2nd_replacement.patch can go into a new ticket, if someone wants to revise image_type.\n\nApply trac_9390-3rd_replacement.patch",
    "created_at": "2010-12-21T11:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89270",
    "user": "https://github.com/mstreng"
}
```

Too bad about the improvements to is_galois. I suppose that code from trac_9390-2nd_replacement.patch can go into a new ticket, if someone wants to revise image_type.

Apply trac_9390-3rd_replacement.patch



---

archive/issue_events_023169.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-12-24T10:16:45Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "milestone": "sage-4.6.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9390#event-23169"
}
```



---

archive/issue_events_023170.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-12-24T10:16:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9390#event-23170"
}
```



---

archive/issue_comments_089271.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9390#issuecomment-89271",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_023171.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-19T22:21:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9390",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9390#event-23171"
}
```
