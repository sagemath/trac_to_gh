# Issue 3979: Power series composition messes up precision

archive/issues_003979.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @fchapoton\n\nKeywords: power series, composition, precision\n\nThe composition of two power series is sometimes returned with the wrong precision. A trivial example:\n\n```\nsage: pow.<u> = PowerSeriesRing(Rationals()); print (1 + O(u^4))(u)\n1\n```\nwhere the return value should have precision 4 rather than infinity. A more nontrivial example:\n\n```\nsage: pow.<u> = PowerSeriesRing(Rationals()); print (1 + u^2 + O(u^4))(u^2)\n1 + u^4 + O(u^10)\n```\nwhere the return value should have precision 8 instead of 10.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3979\n\n",
    "created_at": "2008-08-28T20:16:02Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.4",
    "title": "Power series composition messes up precision",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3979",
    "user": "https://github.com/kedlaya"
}
```
Assignee: @burcin

CC:  @fchapoton

Keywords: power series, composition, precision

The composition of two power series is sometimes returned with the wrong precision. A trivial example:

```
sage: pow.<u> = PowerSeriesRing(Rationals()); print (1 + O(u^4))(u)
1
```
where the return value should have precision 4 rather than infinity. A more nontrivial example:

```
sage: pow.<u> = PowerSeriesRing(Rationals()); print (1 + u^2 + O(u^4))(u^2)
1 + u^4 + O(u^10)
```
where the return value should have precision 8 instead of 10.

Issue created by migration from https://trac.sagemath.org/ticket/3979





---

archive/issue_comments_028522.json:
```json
{
    "body": "A closely related issue is #5075.",
    "created_at": "2009-01-23T19:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28522",
    "user": "https://github.com/kedlaya"
}
```

A closely related issue is #5075.



---

archive/issue_comments_028523.json:
```json
{
    "body": "Changing component from calculus to basic arithmetic.",
    "created_at": "2009-04-16T11:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28523",
    "user": "https://github.com/burcin"
}
```

Changing component from calculus to basic arithmetic.



---

archive/issue_comments_028524.json:
```json
{
    "body": "Changing assignee from @burcin to somebody.",
    "created_at": "2009-04-16T11:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28524",
    "user": "https://github.com/burcin"
}
```

Changing assignee from @burcin to somebody.



---

archive/issue_comments_028525.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-07-18T12:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28525",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_028526.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2011-07-18T12:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28526",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing priority from major to critical.



---

archive/issue_comments_028527.json:
```json
{
    "body": "Changing component from basic arithmetic to algebra.",
    "created_at": "2011-07-18T12:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28527",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing component from basic arithmetic to algebra.



---

archive/issue_comments_028528.json:
```json
{
    "body": "Attachment [trac_3979_power_series_substitution.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution.patch) by fwclarke created at 2011-07-18 12:11:24\n\nIn the attached patch I have completely rewritten `sage.rings.power_series_poly.__call__`.  Several errors in the old version have been corrected.  The new version more closely follows the corresponding function for polynomials, in particular referring to variables by name is now possible.\n\nIn order to make the `__call__` function work correctly it was necessary to change the behaviour of `sage.rings.power_series_poly.valuation`.  At the moment\n\n```\nsage: R.<x> = QQ[]\nsage: O(x^3).valuation()\n+Infinity\n```\nIf we interpret `O(x^3)` as `x^3` times an unknown power series, then the valuation could be anywhere between 3 and infinity, but 3 is a much better, and more cautious, estimate than infinity.  It is also very strange to have a series whose valuation is greater than its precision.  The new convention is also consistent with what happens for p-adic integers:\n\n```\nsage: O(7^3).valuation()\n3\n```\nIn the course of checking the power series code, a minor mistake in the polynomial code has been found and corrected.\n\nA doctest in `sage/rings/morphism.pyx` needed adjusting.\n\nI have also deleted the doctest in `sage.rings.power_series_mpoly.__call__` for two reason's : (1) it doesn't use this function; (2) it makes no sense anyway.  Besides the first line of the file is\n\n```\n# NOT ready to be used -- possibly should be deleted.\n```",
    "created_at": "2011-07-18T12:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28528",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_3979_power_series_substitution.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution.patch) by fwclarke created at 2011-07-18 12:11:24

In the attached patch I have completely rewritten `sage.rings.power_series_poly.__call__`.  Several errors in the old version have been corrected.  The new version more closely follows the corresponding function for polynomials, in particular referring to variables by name is now possible.

In order to make the `__call__` function work correctly it was necessary to change the behaviour of `sage.rings.power_series_poly.valuation`.  At the moment

```
sage: R.<x> = QQ[]
sage: O(x^3).valuation()
+Infinity
```
If we interpret `O(x^3)` as `x^3` times an unknown power series, then the valuation could be anywhere between 3 and infinity, but 3 is a much better, and more cautious, estimate than infinity.  It is also very strange to have a series whose valuation is greater than its precision.  The new convention is also consistent with what happens for p-adic integers:

```
sage: O(7^3).valuation()
3
```
In the course of checking the power series code, a minor mistake in the polynomial code has been found and corrected.

A doctest in `sage/rings/morphism.pyx` needed adjusting.

I have also deleted the doctest in `sage.rings.power_series_mpoly.__call__` for two reason's : (1) it doesn't use this function; (2) it makes no sense anyway.  Besides the first line of the file is

```
# NOT ready to be used -- possibly should be deleted.
```



---

archive/issue_comments_028529.json:
```json
{
    "body": "Replying to [comment:1 kedlaya]:\n> A closely related issue is #5075.\n\n\nRelated, but I don't believe it's the same.  The problem in #5075 is still there after the patch.",
    "created_at": "2011-07-18T12:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28529",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:1 kedlaya]:
> A closely related issue is #5075.


Related, but I don't believe it's the same.  The problem in #5075 is still there after the patch.



---

archive/issue_comments_028530.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-08-01T07:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28530",
    "user": "https://github.com/kedlaya"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_028531.json:
```json
{
    "body": "The patch looks reasonable on its own. However, changing the call syntax for power series generates quite a number of doctest failures elsewhere, by triggering the error message\n\n```\nValueError: Cannot substitute this value\n```\nHere are the examples I found in the rings and schemes directories; there may be more elsewhere that I didn't find. (This used 4.7.1.rc1, but I don't think the version much matters.)\n\n```\nsage -t  \"devel/sage/sage/rings/multi_power_series_ring.py\"\nsage -t  \"devel/sage/sage/rings/laurent_series_ring_element.pyx\"\nsage -t  \"devel/sage/sage/rings/multi_power_series_ring_element.py\"\nsage -t  \"devel/sage/sage/rings/power_series_ring.py\"\nsage -t  \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py\"\nsage -t  \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\"\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_wp.py\"\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/formal_group.py\"\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/padic_lseries.py\"\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/padics.py\"\n```\n\nThis patch can't receive a positive review with all these broken doctests. The best thing would be to fix them all now, but if that is infeasible, I would propose the following.\n\n1. Deprecate the old syntax: accept it while raising a `DeprecationWarning`.\n\n2. Once this ticket is closed, open a second ticket to modify the syntax in the other doctests.\n\n3. Once the second ticket is closed, open a third ticket to remove the old syntax.",
    "created_at": "2011-08-01T07:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28531",
    "user": "https://github.com/kedlaya"
}
```

The patch looks reasonable on its own. However, changing the call syntax for power series generates quite a number of doctest failures elsewhere, by triggering the error message

```
ValueError: Cannot substitute this value
```
Here are the examples I found in the rings and schemes directories; there may be more elsewhere that I didn't find. (This used 4.7.1.rc1, but I don't think the version much matters.)

```
sage -t  "devel/sage/sage/rings/multi_power_series_ring.py"
sage -t  "devel/sage/sage/rings/laurent_series_ring_element.pyx"
sage -t  "devel/sage/sage/rings/multi_power_series_ring_element.py"
sage -t  "devel/sage/sage/rings/power_series_ring.py"
sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py"
sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_wp.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/formal_group.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/padic_lseries.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/padics.py"
```

This patch can't receive a positive review with all these broken doctests. The best thing would be to fix them all now, but if that is infeasible, I would propose the following.

1. Deprecate the old syntax: accept it while raising a `DeprecationWarning`.

2. Once this ticket is closed, open a second ticket to modify the syntax in the other doctests.

3. Once the second ticket is closed, open a third ticket to remove the old syntax.



---

archive/issue_comments_028532.json:
```json
{
    "body": "Replying to [comment:5 kedlaya]:\n\nYes, I'm sorry to have missed those failures.\n\nI've been able to fix most of them. \u00a0The code in `schemes/elliptic_curves/formal_group.py` was problematic since iterated univariate power series were used to approximate a power series ring in two variables, but this should be simple to fix with the multiple variable power series available in 4.7.1.  More difficult to deal with may be the failures in `schemes/hyperelliptic_curves/hyperelliptic_padic_field.py` since the problem here is with substitutions in power series with a known p-adic radius of convergence.\n\nI'll get back to this in a couple of weeks.",
    "created_at": "2011-08-17T19:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28532",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:5 kedlaya]:

Yes, I'm sorry to have missed those failures.

I've been able to fix most of them.  The code in `schemes/elliptic_curves/formal_group.py` was problematic since iterated univariate power series were used to approximate a power series ring in two variables, but this should be simple to fix with the multiple variable power series available in 4.7.1.  More difficult to deal with may be the failures in `schemes/hyperelliptic_curves/hyperelliptic_padic_field.py` since the problem here is with substitutions in power series with a known p-adic radius of convergence.

I'll get back to this in a couple of weeks.



---

archive/issue_comments_028533.json:
```json
{
    "body": "Apply only this file",
    "created_at": "2011-09-21T17:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28533",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Apply only this file



---

archive/issue_comments_028534.json:
```json
{
    "body": "Attachment [trac_3979_power_series_substitution_rev1.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev1.patch) by fwclarke created at 2011-09-21 17:53:07\n\nI have attached a revised patch.  All the previous failures have been dealt with.  Some changes were essentially trivial, but more major were:\n\n1. Formal groups for elliptic curves have been rewritten to exploit the multi-variable power series code available since 4.7.1\n\n2. `local_coordinates_at_weierstrass` in `sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py` has been substantially simplified.\n\n3. At several places in `sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py` substitution in a power series has had to be replaced by substitution in the underlying polynomial.  This works for now because in these instances the p-adic radius of convergence is known.",
    "created_at": "2011-09-21T17:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28534",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_3979_power_series_substitution_rev1.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev1.patch) by fwclarke created at 2011-09-21 17:53:07

I have attached a revised patch.  All the previous failures have been dealt with.  Some changes were essentially trivial, but more major were:

1. Formal groups for elliptic curves have been rewritten to exploit the multi-variable power series code available since 4.7.1

2. `local_coordinates_at_weierstrass` in `sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py` has been substantially simplified.

3. At several places in `sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py` substitution in a power series has had to be replaced by substitution in the underlying polynomial.  This works for now because in these instances the p-adic radius of convergence is known.



---

archive/issue_comments_028535.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-09-21T17:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28535",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_028536.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-10-11T13:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28536",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_028537.json:
```json
{
    "body": "Some problems I have found\n\nThis should work\n\n```\nsage: x=polygen(QQ)\nsage: f = 1 + 3*x + O(x^2)\nsage: f(x)\n...\nValueError\n```\n\nThis should raise an error:\n\n```\nsage: x = LaurentSeriesRing(QQ,'x').gen()\nsage: f = x + O(x^2)\nsage: f(~x)\nO(x^-2)\n```\n\nYou cannot substitute x by 1/x on a power series unless it is a Laurent polynomial.\n\nSuggestions, comments:\n\nOn file laurent_series_ring_element.pyx\n\n`@`446 def laurentpolynomial(...\n\nImprove the documentation. By what is written it seems that the output should be a Laurent polynomial but the method actually returns a Laurent power series. \n\n`@`1141  __call__ documentation, specify that x needs to have a valuation at least 1.\n\n`@`1165  raise ValueError, \"must not specify %s keyword and positional argument\" % name\n\nAdd a doctest to the __call__ method with both keywords and positional arguments one that works (name!= keyword) and one that raises the error, other possibilities welcomed.\n\nOn file multi_power_series_ring\n\n`@`964,989 improve documentation, not clear if the input can be polynomials, powerseries, powerseries + bigoh or in which ring is the result. If we can use big_Oh in the input etc. Maybe for another ticket.\n\nOn file local_generic_element.pyx\n\n`@`140 I would write: Returns self up to reduced precision `prec`.\n\nOn file polynomial_element.pyx\n\n`@`461-467 doctest should go in the TESTS section.\n\n`@`567  raise ValueError, \"must not specify %s keyword and positional argument\" % name\n\nOn file power_series_mpoly\n\n`@`74 Add documentation and a valid example to the __call__ method.  Each method or function that is modified need to have a correct documentation and doctest.\n\nOn file power_series_poly\n\n`@`290 raise ValueError, \"must not specify %s keyword and positional argument\" % name\n\n`@`936 This is a bug and should be fixed. This is a regression since this works without the patch (except for the incorrect precision).\n\nOn file scheme.py\n\n`@`178 temp2 = temp.exp().change_ring(ZZ)\n\nIs there a reason you want a powerseries in ZZ instead of QQ?",
    "created_at": "2011-10-11T13:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28537",
    "user": "https://github.com/lftabera"
}
```

Some problems I have found

This should work

```
sage: x=polygen(QQ)
sage: f = 1 + 3*x + O(x^2)
sage: f(x)
...
ValueError
```

This should raise an error:

```
sage: x = LaurentSeriesRing(QQ,'x').gen()
sage: f = x + O(x^2)
sage: f(~x)
O(x^-2)
```

You cannot substitute x by 1/x on a power series unless it is a Laurent polynomial.

Suggestions, comments:

On file laurent_series_ring_element.pyx

`@`446 def laurentpolynomial(...

Improve the documentation. By what is written it seems that the output should be a Laurent polynomial but the method actually returns a Laurent power series. 

`@`1141  __call__ documentation, specify that x needs to have a valuation at least 1.

`@`1165  raise ValueError, "must not specify %s keyword and positional argument" % name

Add a doctest to the __call__ method with both keywords and positional arguments one that works (name!= keyword) and one that raises the error, other possibilities welcomed.

On file multi_power_series_ring

`@`964,989 improve documentation, not clear if the input can be polynomials, powerseries, powerseries + bigoh or in which ring is the result. If we can use big_Oh in the input etc. Maybe for another ticket.

On file local_generic_element.pyx

`@`140 I would write: Returns self up to reduced precision `prec`.

On file polynomial_element.pyx

`@`461-467 doctest should go in the TESTS section.

`@`567  raise ValueError, "must not specify %s keyword and positional argument" % name

On file power_series_mpoly

`@`74 Add documentation and a valid example to the __call__ method.  Each method or function that is modified need to have a correct documentation and doctest.

On file power_series_poly

`@`290 raise ValueError, "must not specify %s keyword and positional argument" % name

`@`936 This is a bug and should be fixed. This is a regression since this works without the patch (except for the incorrect precision).

On file scheme.py

`@`178 temp2 = temp.exp().change_ring(ZZ)

Is there a reason you want a powerseries in ZZ instead of QQ?



---

archive/issue_comments_028538.json:
```json
{
    "body": "Replying to [comment:8 lftabera]:\n\nThanks for your careful look at the patch.  Most of the problems can be fixed quite easily, though the one at line 936 in `power_series_poly` could be more difficult.  I hope to submit a new patch soon.\n\n> On file power_series_mpoly `@`74 Add documentation and a valid example to the __call__ method.  Each method or function that is modified need to have a correct documentation and doctest.\n\n\nThe reason I  removed rather than corrected the doctest in `power_series_mpoly` was that it does **not** test this `__call__` function but the one in  `power_series_poly` (I've seen too many such doctests).  In fact I'm not sure that this file is used at all.  In fact the first line is\n\n```\n# NOT ready to be used -- possibly should be deleted.\n```\nHowever I didn't have the confidence to delete it myself, and add other issues to an already complicated patch. \u00a0\n\nAdding documentation to this function would be hard to do since the whole file is so poorly documented that I can't understand what it's for.",
    "created_at": "2011-10-12T11:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28538",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:8 lftabera]:

Thanks for your careful look at the patch.  Most of the problems can be fixed quite easily, though the one at line 936 in `power_series_poly` could be more difficult.  I hope to submit a new patch soon.

> On file power_series_mpoly `@`74 Add documentation and a valid example to the __call__ method.  Each method or function that is modified need to have a correct documentation and doctest.


The reason I  removed rather than corrected the doctest in `power_series_mpoly` was that it does **not** test this `__call__` function but the one in  `power_series_poly` (I've seen too many such doctests).  In fact I'm not sure that this file is used at all.  In fact the first line is

```
# NOT ready to be used -- possibly should be deleted.
```
However I didn't have the confidence to delete it myself, and add other issues to an already complicated patch.  

Adding documentation to this function would be hard to do since the whole file is so poorly documented that I can't understand what it's for.



---

archive/issue_comments_028539.json:
```json
{
    "body": "Apologies for hijacking this ticket for this:  Francis, what is your email address?   F.Clarke`@`swansea.ac.uk is bouncing!  John (john.cremona`@`gmail.com)",
    "created_at": "2011-11-03T15:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28539",
    "user": "https://github.com/JohnCremona"
}
```

Apologies for hijacking this ticket for this:  Francis, what is your email address?   F.Clarke`@`swansea.ac.uk is bouncing!  John (john.cremona`@`gmail.com)



---

archive/issue_comments_028540.json:
```json
{
    "body": "Replaces previous revised patch",
    "created_at": "2012-05-13T09:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28540",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replaces previous revised patch



---

archive/issue_events_009115.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/fwclarke",
    "created_at": "2012-05-13T09:56:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "milestone": "sage-5.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3979#event-9115"
}
```



---

archive/issue_comments_028541.json:
```json
{
    "body": "Attachment [trac_3979_power_series_substitution_rev2.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev2.patch) by fwclarke created at 2012-05-13 09:56:54\n\nReplying to [comment:8 lftabera]:\n\nFinally I have a revised patch.  I have applied all your suggestions with two exceptions.  Comments on some of them follow:\n\n> On file laurent_series_ring_element.pyx `@`446 \n\n\nRather than changing the documentation I have changed the code, so it does now return a Laurent polynomial.\n\n> On file multi_power_series_ring  `@`964,989\n\n\nI've left this for another ticket, as you suggested.\n\n> On file power_series_mpoly `@`74 \n\n\nI've left this unchanged, for reasons explained [comment:9 above]. \n\n> On file scheme.py `@`178\n\n\nI've undone this change.  It belongs in another ticket.",
    "created_at": "2012-05-13T09:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28541",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_3979_power_series_substitution_rev2.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev2.patch) by fwclarke created at 2012-05-13 09:56:54

Replying to [comment:8 lftabera]:

Finally I have a revised patch.  I have applied all your suggestions with two exceptions.  Comments on some of them follow:

> On file laurent_series_ring_element.pyx `@`446 


Rather than changing the documentation I have changed the code, so it does now return a Laurent polynomial.

> On file multi_power_series_ring  `@`964,989


I've left this for another ticket, as you suggested.

> On file power_series_mpoly `@`74 


I've left this unchanged, for reasons explained [comment:9 above]. 

> On file scheme.py `@`178


I've undone this change.  It belongs in another ticket.



---

archive/issue_comments_028542.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-05-13T09:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28542",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_028543.json:
```json
{
    "body": "Note that the patch corrects a bug raised in #12931.",
    "created_at": "2012-05-13T10:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28543",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Note that the patch corrects a bug raised in #12931.



---

archive/issue_comments_028544.json:
```json
{
    "body": "Trying to help the bot:\n\nApply only trac_3979_power_series_substitution_rev2.patch",
    "created_at": "2012-08-26T09:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28544",
    "user": "https://github.com/fchapoton"
}
```

Trying to help the bot:

Apply only trac_3979_power_series_substitution_rev2.patch



---

archive/issue_comments_028545.json:
```json
{
    "body": "The patch must be rebased on a recent version.",
    "created_at": "2012-08-26T09:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28545",
    "user": "https://github.com/fchapoton"
}
```

The patch must be rebased on a recent version.



---

archive/issue_comments_028546.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-08-26T09:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28546",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_028547.json:
```json
{
    "body": "Rebased for 5.2",
    "created_at": "2012-08-26T21:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28547",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Rebased for 5.2



---

archive/issue_comments_028548.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-26T21:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28548",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_028549.json:
```json
{
    "body": "Attachment [trac_3979_power_series_substitution_rev3.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev3.patch) by fwclarke created at 2012-08-26 21:51:30\n\nReplying to [comment:15 chapoton]:\n> The patch must be rebased on a recent version.\n\n\nI've attached new patch.  \n\nI hope it can be reviewed before this has to be done again.",
    "created_at": "2012-08-26T21:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28549",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_3979_power_series_substitution_rev3.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev3.patch) by fwclarke created at 2012-08-26 21:51:30

Replying to [comment:15 chapoton]:
> The patch must be rebased on a recent version.


I've attached new patch.  

I hope it can be reviewed before this has to be done again.



---

archive/issue_comments_028550.json:
```json
{
    "body": "Apply only trac_3979_power_series_substitution_rev3.patch",
    "created_at": "2012-08-27T11:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28550",
    "user": "https://github.com/fchapoton"
}
```

Apply only trac_3979_power_series_substitution_rev3.patch



---

archive/issue_comments_028551.json:
```json
{
    "body": "Apply only trac_3979_power_series_substitution_rev4.patch",
    "created_at": "2012-08-27T17:08:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28551",
    "user": "https://github.com/fchapoton"
}
```

Apply only trac_3979_power_series_substitution_rev4.patch



---

archive/issue_comments_028552.json:
```json
{
    "body": "I would like to see, when possible, a more specific error instead of\n\n```\nraise ValueError, \"Cannot substitute this value\" \n```\nIn particular, when this is because of negative valuation, one should say it.",
    "created_at": "2012-08-27T19:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28552",
    "user": "https://github.com/fchapoton"
}
```

I would like to see, when possible, a more specific error instead of

```
raise ValueError, "Cannot substitute this value" 
```
In particular, when this is because of negative valuation, one should say it.



---

archive/issue_comments_028553.json:
```json
{
    "body": "apply after trac_3979_power_series_substitution_rev4.patch",
    "created_at": "2012-08-27T21:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28553",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

apply after trac_3979_power_series_substitution_rev4.patch



---

archive/issue_comments_028554.json:
```json
{
    "body": "Attachment [trac_3979_power_series_substitution_rev4_extra.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev4_extra.patch) by fwclarke created at 2012-08-27 21:45:46\n\nReplying to [comment:21 chapoton]:\n> I would like to see, when possible, a more specific error instead of\n> \n> ```\n> raise ValueError, \"Cannot substitute this value\" \n> ```\n> In particular, when this is because of negative valuation, one should say it.\n\n\nA good point.  The new patch (to be applied after trac_3979_power_series_substitution_rev4.patch) gives a more explicit error message.",
    "created_at": "2012-08-27T21:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28554",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_3979_power_series_substitution_rev4_extra.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev4_extra.patch) by fwclarke created at 2012-08-27 21:45:46

Replying to [comment:21 chapoton]:
> I would like to see, when possible, a more specific error instead of
> 
> ```
> raise ValueError, "Cannot substitute this value" 
> ```
> In particular, when this is because of negative valuation, one should say it.


A good point.  The new patch (to be applied after trac_3979_power_series_substitution_rev4.patch) gives a more explicit error message.



---

archive/issue_comments_028555.json:
```json
{
    "body": "Attachment [trac_3979_power_series_substitution_rev4.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev4.patch) by @fchapoton created at 2012-09-24 18:56:24",
    "created_at": "2012-09-24T18:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28555",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_3979_power_series_substitution_rev4.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev4.patch) by @fchapoton created at 2012-09-24 18:56:24



---

archive/issue_comments_028556.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-09-24T18:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28556",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_028557.json:
```json
{
    "body": "This looks good to me. The patches applies smoothly on 5.4beta1. All tests pass. This ticket solves some embarassing problems and is much wanted. Positive review !",
    "created_at": "2012-09-24T18:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28557",
    "user": "https://github.com/fchapoton"
}
```

This looks good to me. The patches applies smoothly on 5.4beta1. All tests pass. This ticket solves some embarassing problems and is much wanted. Positive review !



---

archive/issue_comments_028558.json:
```json
{
    "body": "The bot is back and is unhappy because the patch removes one test in rings/power_series_mpoly.pyx\n\nThis should be easy to correct, if really required to close the ticket.",
    "created_at": "2012-09-26T10:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28558",
    "user": "https://github.com/fchapoton"
}
```

The bot is back and is unhappy because the patch removes one test in rings/power_series_mpoly.pyx

This should be easy to correct, if really required to close the ticket.



---

archive/issue_comments_028559.json:
```json
{
    "body": "Replying to [comment:25 chapoton]:\n> The bot is back and is unhappy because the patch removes one test in rings/power_series_mpoly.pyx\n> \n> This should be easy to correct, if really required to close the ticket.\n\n\nAs I said in July last year:\n\n   I have also deleted the doctest in `sage.rings.power_series_mpoly.__call__` for two reasons : (1) it doesn't use this function; (2) it makes no sense anyway. Besides the first line of the file is\n\n```\n# NOT ready to be used -- possibly should be deleted.\n```\n\nAnd I explained this more fully a year ago:\n\n   The reason I removed rather than corrected the doctest in `power_series_mpoly` was that it does not test this `__call__` function but the one in `power_series_poly` (I've seen too many such doctests). In fact I'm not sure that this file is used at all. In fact the first line is\n\n```\n# NOT ready to be used -- possibly should be deleted.\n```\n   However I didn't have the confidence to delete it myself, and add other issues to an already complicated patch.  \n\n   Adding documentation to this function would be hard to do since the whole file is so poorly documented that I can't understand what it's for.\n\nI have now understood how to create an element of the relevant type (something that isn't done anywhere else, as far as I can see):\n\n```\nsage: S.<x> = QQ[]\nsage: R = sage.rings.power_series_ring.PowerSeriesRing_generic(S, \n            't', use_lazy_mpoly_ring=True)\nsage: t = R.gen()\nsage: f = 3 - x*t^3 + O(t^5)\nsage: type(f)\n<type 'sage.rings.power_series_mpoly.PowerSeries_mpoly'>\nsage: f(2)\n-2*t^3 + 3\nsage: f(2, t^2)\n3 - 2*t^6\n```\nThe final answers are wrong (they shouldn't have infinite precision), inconsistent (the first is a polynomial, the second a power series), and the syntax is non-standard.  Compare\n\n```\nsage: T.<u> = S[[]]\nsage: g = 3 - x*u^3 + O(u^5)\nsage: g(u^2, 2)\n3 - 2*u^6 + O(u^10)\nsage: g(u^2)\n3 - x*u^6 + O(u^10)\n```\nOf course `g(2)` raises an error.\n\nHowever, I have made a supplementary patch which reinserts into `power_series_mpoly.pyx` a doctest based on the above.  This should appease the patchbot, and though problematic it is less bad than before.  The alternative would be to rewrite much of the code in `power_series_mpoly.pyx`, which would seem to be a waste of time if it is destined for deletion.",
    "created_at": "2012-09-26T17:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28559",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:25 chapoton]:
> The bot is back and is unhappy because the patch removes one test in rings/power_series_mpoly.pyx
> 
> This should be easy to correct, if really required to close the ticket.


As I said in July last year:

   I have also deleted the doctest in `sage.rings.power_series_mpoly.__call__` for two reasons : (1) it doesn't use this function; (2) it makes no sense anyway. Besides the first line of the file is

```
# NOT ready to be used -- possibly should be deleted.
```

And I explained this more fully a year ago:

   The reason I removed rather than corrected the doctest in `power_series_mpoly` was that it does not test this `__call__` function but the one in `power_series_poly` (I've seen too many such doctests). In fact I'm not sure that this file is used at all. In fact the first line is

```
# NOT ready to be used -- possibly should be deleted.
```
   However I didn't have the confidence to delete it myself, and add other issues to an already complicated patch.  

   Adding documentation to this function would be hard to do since the whole file is so poorly documented that I can't understand what it's for.

I have now understood how to create an element of the relevant type (something that isn't done anywhere else, as far as I can see):

```
sage: S.<x> = QQ[]
sage: R = sage.rings.power_series_ring.PowerSeriesRing_generic(S, 
            't', use_lazy_mpoly_ring=True)
sage: t = R.gen()
sage: f = 3 - x*t^3 + O(t^5)
sage: type(f)
<type 'sage.rings.power_series_mpoly.PowerSeries_mpoly'>
sage: f(2)
-2*t^3 + 3
sage: f(2, t^2)
3 - 2*t^6
```
The final answers are wrong (they shouldn't have infinite precision), inconsistent (the first is a polynomial, the second a power series), and the syntax is non-standard.  Compare

```
sage: T.<u> = S[[]]
sage: g = 3 - x*u^3 + O(u^5)
sage: g(u^2, 2)
3 - 2*u^6 + O(u^10)
sage: g(u^2)
3 - x*u^6 + O(u^10)
```
Of course `g(2)` raises an error.

However, I have made a supplementary patch which reinserts into `power_series_mpoly.pyx` a doctest based on the above.  This should appease the patchbot, and though problematic it is less bad than before.  The alternative would be to rewrite much of the code in `power_series_mpoly.pyx`, which would seem to be a waste of time if it is destined for deletion.



---

archive/issue_comments_028560.json:
```json
{
    "body": "Apply after trac_3979_power_series_substitution_rev4_extra.patch",
    "created_at": "2012-09-26T17:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28560",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Apply after trac_3979_power_series_substitution_rev4_extra.patch



---

archive/issue_comments_028561.json:
```json
{
    "body": "Attachment [trac_3979_power_series_substitution_rev4_supplementary.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev4_supplementary.patch) by fwclarke created at 2012-09-26 17:38:05",
    "created_at": "2012-09-26T17:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28561",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_3979_power_series_substitution_rev4_supplementary.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev4_supplementary.patch) by fwclarke created at 2012-09-26 17:38:05



---

archive/issue_comments_028562.json:
```json
{
    "body": "Apply only this patch",
    "created_at": "2012-09-27T12:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28562",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Apply only this patch



---

archive/issue_comments_028563.json:
```json
{
    "body": "Attachment [trac_3979_power_series_substitution_rev5.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev5.patch) by fwclarke created at 2012-09-27 12:10:29\n\nThe patchbot tried (and failed) to apply only patches 2 and 3 out of three\n\nSo I have merged them all into one patch.  Hope this works.",
    "created_at": "2012-09-27T12:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28563",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_3979_power_series_substitution_rev5.patch](tarball://root/attachments/some-uuid/ticket3979/trac_3979_power_series_substitution_rev5.patch) by fwclarke created at 2012-09-27 12:10:29

The patchbot tried (and failed) to apply only patches 2 and 3 out of three

So I have merged them all into one patch.  Hope this works.



---

archive/issue_events_009116.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-09-28T07:46:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3979#event-9116"
}
```



---

archive/issue_comments_028564.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-28T07:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3979#issuecomment-28564",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
