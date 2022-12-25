# Issue 4376: Implement conversion of power series over more rings (e.g. GF(p)) to pari

archive/issues_004376.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  salmanhb@gmail.com @loefflerd @nilesjohnson @jdemeyer\n\nKeywords: power series pari gp\n\nsalmanhb`@`gmail.com would like to be able to do linear algebra over `GF(p)[This is the Trac macro *X* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#X-macro)` using pari, but currently conversion of power series in `R[This is the Trac macro *X* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#X-macro)` to pari is only implemented when R=QQ or R=ZZ (via strings).\n\nWe should improve the _pari_() function for power series rings to allow R to be any ring in which pari conversion is already defined.\n\nDepends on #7644\n\nIssue created by migration from https://trac.sagemath.org/ticket/4376\n\n",
    "closed_at": "2011-03-24T20:39:02Z",
    "created_at": "2008-10-28T09:44:11Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "Implement conversion of power series over more rings (e.g. GF(p)) to pari",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4376",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

CC:  salmanhb@gmail.com @loefflerd @nilesjohnson @jdemeyer

Keywords: power series pari gp

salmanhb`@`gmail.com would like to be able to do linear algebra over `GF(p)[This is the Trac macro *X* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#X-macro)` using pari, but currently conversion of power series in `R[This is the Trac macro *X* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#X-macro)` to pari is only implemented when R=QQ or R=ZZ (via strings).

We should improve the _pari_() function for power series rings to allow R to be any ring in which pari conversion is already defined.

Depends on #7644

Issue created by migration from https://trac.sagemath.org/ticket/4376





---

archive/issue_comments_032115.json:
```json
{
    "body": "Currently pari conversion doesn't even work for series with integer coefficients.  This was pointed out in the docstring for `sage.modular.overconvergent.genus0.OverconvergentModularFormElement._pari_`.\n\nThe attached patch extends the range of possible base rings significantly, but is still limited by what `sage.rings.polynomial.polynomial_element.Polynomial._pari_` can do; see its extensive docstring.",
    "created_at": "2010-08-27T10:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32115",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Currently pari conversion doesn't even work for series with integer coefficients.  This was pointed out in the docstring for `sage.modular.overconvergent.genus0.OverconvergentModularFormElement._pari_`.

The attached patch extends the range of possible base rings significantly, but is still limited by what `sage.rings.polynomial.polynomial_element.Polynomial._pari_` can do; see its extensive docstring.



---

archive/issue_comments_032116.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-27T10:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32116",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_032117.json:
```json
{
    "body": "Attachment [trac_4376.patch](tarball://root/attachments/some-uuid/ticket4376/trac_4376.patch) by fwclarke created at 2010-08-27 10:19:27",
    "created_at": "2010-08-27T10:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32117",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_4376.patch](tarball://root/attachments/some-uuid/ticket4376/trac_4376.patch) by fwclarke created at 2010-08-27 10:19:27



---

archive/issue_comments_032118.json:
```json
{
    "body": "I wonder if making a new comment will get [Patch Buildbot](http://wiki.sagemath.org/buildbot) to look at this . . .",
    "created_at": "2010-12-04T16:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32118",
    "user": "https://github.com/nilesjohnson"
}
```

I wonder if making a new comment will get [Patch Buildbot](http://wiki.sagemath.org/buildbot) to look at this . . .



---

archive/issue_comments_032119.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-12-06T10:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32119",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_032120.json:
```json
{
    "body": "Applies and builds without any problems on top of 4.6.1.alpha2 on the machine that I tried it on. All tests pass, the code looks good, and the patch seems to do what it says.\n\nI would have made it \"positive review\", but then there is the new \"Buildbot\" link at the top of this page, which says \"TestsFailed ...\"\n\nWhat should I do with that?",
    "created_at": "2010-12-06T10:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32120",
    "user": "https://github.com/mstreng"
}
```

Applies and builds without any problems on top of 4.6.1.alpha2 on the machine that I tried it on. All tests pass, the code looks good, and the patch seems to do what it says.

I would have made it "positive review", but then there is the new "Buildbot" link at the top of this page, which says "TestsFailed ..."

What should I do with that?



---

archive/issue_comments_032121.json:
```json
{
    "body": "The buildbot is a tool to help you. If you check the fail. You will see that the tests that fail are stratup.py and setup0.py. These two are failing in all tickets, the fail does not have to do with this ticket. So if you have checked that the code is ok and your tests pass, feel free to give a positive review.",
    "created_at": "2010-12-06T11:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32121",
    "user": "https://github.com/lftabera"
}
```

The buildbot is a tool to help you. If you check the fail. You will see that the tests that fail are stratup.py and setup0.py. These two are failing in all tickets, the fail does not have to do with this ticket. So if you have checked that the code is ok and your tests pass, feel free to give a positive review.



---

archive/issue_comments_032122.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-12-06T11:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32122",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_032123.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-06T11:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32123",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032124.json:
```json
{
    "body": "As a possible follow-up, we should also implement/check conversion to GP.",
    "created_at": "2010-12-06T13:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32124",
    "user": "https://github.com/jdemeyer"
}
```

As a possible follow-up, we should also implement/check conversion to GP.



---

archive/issue_events_009895.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-12-06T13:22:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4376#event-9895"
}
```



---

archive/issue_comments_032125.json:
```json
{
    "body": "Changing keywords from \"power series pari\" to \"power series pari gp\".",
    "created_at": "2010-12-06T13:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32125",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "power series pari" to "power series pari gp".



---

archive/issue_comments_032126.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-27T14:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32126",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_032127.json:
```json
{
    "body": "Test failures on sage-4.6.2.alpha1:\n\n```\nsage -t  \"devel/sage/sage/rings/power_series_poly.pyx\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx\", line 766:\n    sage: g = f.reversion(); g\nExpected:\n    1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)\nGot:\n    O(t^4)\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx\", line 770:\n    sage: f(g)\nExpected:\n    t + O(t^4)\nGot:\n    O(t^4)\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx\", line 772:\n    sage: g(f)\nExpected:\n    t + O(t^4)\nGot:\n    0\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx\", line 779:                                      sage: b = a.reversion(); b                                                                                                            Exception raised:                                                                                                                             Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_32[31]>\", line 1, in <module>\n        b = a.reversion(); b###line 779:\n    sage: b = a.reversion(); b\n      File \"power_series_poly.pyx\", line 847, in sage.rings.power_series_poly.PowerSeries_poly.reversion (sage/rings/power_series_poly.c:6881)\n      File \"gen.pyx\", line 9851, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:46023)\n    PariError:  (20)\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx\", line 781:\n    sage: a(b)\nExpected:\n    t + O(t^6)\nGot:\n    b^5 + 6*b^4 + b^2 + b\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx\", line 783:\n    sage: b(a)\nExpected:\n    t + O(t^6)\nGot:\n    t + t^2 + 6*t^4 + t^5 + O(t^6)\n**********************************************************************\n```",
    "created_at": "2011-01-27T14:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32127",
    "user": "https://github.com/jdemeyer"
}
```

Test failures on sage-4.6.2.alpha1:

```
sage -t  "devel/sage/sage/rings/power_series_poly.pyx"
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx", line 766:
    sage: g = f.reversion(); g
Expected:
    1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
Got:
    O(t^4)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx", line 770:
    sage: f(g)
Expected:
    t + O(t^4)
Got:
    O(t^4)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx", line 772:
    sage: g(f)
Expected:
    t + O(t^4)
Got:
    0
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx", line 779:                                      sage: b = a.reversion(); b                                                                                                            Exception raised:                                                                                                                             Traceback (most recent call last):
      File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_32[31]>", line 1, in <module>
        b = a.reversion(); b###line 779:
    sage: b = a.reversion(); b
      File "power_series_poly.pyx", line 847, in sage.rings.power_series_poly.PowerSeries_poly.reversion (sage/rings/power_series_poly.c:6881)
      File "gen.pyx", line 9851, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:46023)
    PariError:  (20)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx", line 781:
    sage: a(b)
Expected:
    t + O(t^6)
Got:
    b^5 + 6*b^4 + b^2 + b
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx", line 783:
    sage: b(a)
Expected:
    t + O(t^6)
Got:
    t + t^2 + 6*t^4 + t^5 + O(t^6)
**********************************************************************
```



---

archive/issue_comments_032128.json:
```json
{
    "body": "Apply on top of previous patch",
    "created_at": "2011-01-27T14:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32128",
    "user": "https://github.com/jdemeyer"
}
```

Apply on top of previous patch



---

archive/issue_comments_032129.json:
```json
{
    "body": "Attachment [4376_no_strings.patch](tarball://root/attachments/some-uuid/ticket4376/4376_no_strings.patch) by @jdemeyer created at 2011-01-27 14:58:07\n\nThe attached patch removes the conversion PARI -> string -> PARI.  It does not address the doctest failures.",
    "created_at": "2011-01-27T14:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32129",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [4376_no_strings.patch](tarball://root/attachments/some-uuid/ticket4376/4376_no_strings.patch) by @jdemeyer created at 2011-01-27 14:58:07

The attached patch removes the conversion PARI -> string -> PARI.  It does not address the doctest failures.



---

archive/issue_comments_032130.json:
```json
{
    "body": "Replying to [comment:9 jdemeyer]:\n\n> Test failures on sage-4.6.2.alpha1: \n> ...\n\n\nWhat's happened is that #7644 means that many more series can be converted to Pari and reversion performed using `sereverse`.  But when the degree-one coefficient is not a unit, converting the result back to Sage has exposed the following problem:\n\n```\nsage: P.<x> = Q[]\nsage: Q = P.fraction_field()\nsage: Q(1/x)\n1/x\nsage: Q(pari(1/x))\n0\n```\nThis is caused by \n\n```\nsage: P(pari(1/x))\n0\n```\nwhereas `P(1/x)` raises `TypeError: denominator must be a unit`.\n\nThe other group of failures is caused when conversion to a Pari series is successful but reversion raises a Pari error.\n\nI will shortly post a patch which sorts these difficulties out. I've added a doctest for `reversion` in order to provide another example where Pari fails and the Lagrange inversion code needs to be used.",
    "created_at": "2011-01-31T18:58:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32130",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:9 jdemeyer]:

> Test failures on sage-4.6.2.alpha1: 
> ...


What's happened is that #7644 means that many more series can be converted to Pari and reversion performed using `sereverse`.  But when the degree-one coefficient is not a unit, converting the result back to Sage has exposed the following problem:

```
sage: P.<x> = Q[]
sage: Q = P.fraction_field()
sage: Q(1/x)
1/x
sage: Q(pari(1/x))
0
```
This is caused by 

```
sage: P(pari(1/x))
0
```
whereas `P(1/x)` raises `TypeError: denominator must be a unit`.

The other group of failures is caused when conversion to a Pari series is successful but reversion raises a Pari error.

I will shortly post a patch which sorts these difficulties out. I've added a doctest for `reversion` in order to provide another example where Pari fails and the Lagrange inversion code needs to be used.



---

archive/issue_comments_032131.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-31T19:56:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32131",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_032132.json:
```json
{
    "body": "The attached patch makes the changes made in the previous patchescompatible with those made in !#7644.",
    "created_at": "2011-01-31T19:56:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32132",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

The attached patch makes the changes made in the previous patchescompatible with those made in !#7644.



---

archive/issue_comments_032133.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-31T20:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32133",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_032134.json:
```json
{
    "body": "On lines 316 and 317 of sage/rings/polynomial/polynomial_ring.py, you write\n\n```\nexcept (NotImplementedError, ValueError): \n    raise TypeError, \"denominator must be a unit\" \n```\nI don't think a `NotImplementedError` should lead to a `TypeError`: that would give a lot of confusion.\n\nOtherwise, this all looks very good.\n\n(this ticket now depends on #7644)",
    "created_at": "2011-01-31T20:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32134",
    "user": "https://github.com/mstreng"
}
```

On lines 316 and 317 of sage/rings/polynomial/polynomial_ring.py, you write

```
except (NotImplementedError, ValueError): 
    raise TypeError, "denominator must be a unit" 
```
I don't think a `NotImplementedError` should lead to a `TypeError`: that would give a lot of confusion.

Otherwise, this all looks very good.

(this ticket now depends on #7644)



---

archive/issue_comments_032135.json:
```json
{
    "body": "I'm wondering if we shouldn't simply do\n\n```\nif x.type() == 't_RFRAC':\n    raise TypeError, \"denominator must be a unit\"\n```\n\nI doubt that a PARI RFRAC can ever have a denominator which *is* a unit.",
    "created_at": "2011-02-01T14:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32135",
    "user": "https://github.com/jdemeyer"
}
```

I'm wondering if we shouldn't simply do

```
if x.type() == 't_RFRAC':
    raise TypeError, "denominator must be a unit"
```

I doubt that a PARI RFRAC can ever have a denominator which *is* a unit.



---

archive/issue_comments_032136.json:
```json
{
    "body": "Attachment [4376_reversion_fixes.patch](tarball://root/attachments/some-uuid/ticket4376/4376_reversion_fixes.patch) by fwclarke created at 2011-02-02 09:14:23\n\nApply after previous two patches",
    "created_at": "2011-02-02T09:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32136",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [4376_reversion_fixes.patch](tarball://root/attachments/some-uuid/ticket4376/4376_reversion_fixes.patch) by fwclarke created at 2011-02-02 09:14:23

Apply after previous two patches



---

archive/issue_comments_032137.json:
```json
{
    "body": "Replying to [comment:14 jdemeyer]:\n> ...\n> I doubt that a PARI RFRAC can ever have a denominator which *is* a unit.\n\n\nI agree. So I've replaced the patch with one which implements your suggestion.",
    "created_at": "2011-02-02T09:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32137",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:14 jdemeyer]:
> ...
> I doubt that a PARI RFRAC can ever have a denominator which *is* a unit.


I agree. So I've replaced the patch with one which implements your suggestion.



---

archive/issue_comments_032138.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-02T09:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32138",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_032139.json:
```json
{
    "body": "Francis: your patches look fine to me.  Can somebody review my patch and give this ticket positive review?",
    "created_at": "2011-02-02T10:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32139",
    "user": "https://github.com/jdemeyer"
}
```

Francis: your patches look fine to me.  Can somebody review my patch and give this ticket positive review?



---

archive/issue_comments_032140.json:
```json
{
    "body": "[attachment:4376_no_strings.patch] looks good: it accomplishes the same thing as the \"with strings\" version of the code, but skips the step of converting a pari polynomial to a string and then back to a pari polynomial.  The patch includes some good corner-case tests, and a comment referencing the ticket number and what's being fixed.\n\nTherefore, positive review for this patch.  If I understand the above correctly, the other patches here have already been positively reviewed, so I'm switching the whole ticket to `positive review`.",
    "created_at": "2011-03-18T14:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32140",
    "user": "https://github.com/nilesjohnson"
}
```

[attachment:4376_no_strings.patch] looks good: it accomplishes the same thing as the "with strings" version of the code, but skips the step of converting a pari polynomial to a string and then back to a pari polynomial.  The patch includes some good corner-case tests, and a comment referencing the ticket number and what's being fixed.

Therefore, positive review for this patch.  If I understand the above correctly, the other patches here have already been positively reviewed, so I'm switching the whole ticket to `positive review`.



---

archive/issue_comments_032141.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-18T14:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32141",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009896.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-03-24T20:39:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4376#event-9896"
}
```



---

archive/issue_comments_032142.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-24T20:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4376#issuecomment-32142",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
