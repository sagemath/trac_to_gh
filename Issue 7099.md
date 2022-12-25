# Issue 7099: serious incomplete gamma function precision bugs

archive/issues_007099.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @kcrisman\n\n\n```\nsage: C = ComplexField(1000)\nsage: C(2+I).gamma_inc(C(3+I))\n0.1215156446645086956511068454478419198494520969688892364501953125000000\\\n000000000000000000000000000000000000000000000000000000000000000000000000\\\n000000000000000000000000000000000000000000000000000000000000000000000000\\\n000000000000000000000000000000000000000000000000000000000000000000000000\\\n00000000000000 +\n0.1015339090798260332775427433604775728781532961875200271606445312500000\\\n000000000000000000000000000000000000000000000000000000000000000000000000\\\n000000000000000000000000000000000000000000000000000000000000000000000000\\\n000000000000000000000000000000000000000000000000000000000000000000000000\\\n00000000000000*I\n```\n\n\nWhat's with all the zeros?   Same bad behavior for higher precision and any other random input.  This is undoubtedly the typical mistake of not setting the pari precision correctly, etc., etc. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7099\n\n",
    "created_at": "2009-10-02T18:58:08Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "serious incomplete gamma function precision bugs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7099",
    "user": "https://github.com/williamstein"
}
```
Assignee: jkantor

CC:  @kcrisman


```
sage: C = ComplexField(1000)
sage: C(2+I).gamma_inc(C(3+I))
0.1215156446645086956511068454478419198494520969688892364501953125000000\
000000000000000000000000000000000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000\
00000000000000 +
0.1015339090798260332775427433604775728781532961875200271606445312500000\
000000000000000000000000000000000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000\
00000000000000*I
```


What's with all the zeros?   Same bad behavior for higher precision and any other random input.  This is undoubtedly the typical mistake of not setting the pari precision correctly, etc., etc. 

Issue created by migration from https://trac.sagemath.org/ticket/7099





---

archive/issue_comments_058632.json:
```json
{
    "body": "Correct.  Here's the problem, I think.\n\n```\n\nsage: C = ComplexField(1000)\nsage: c = C(2+I)\nsage: c\n2.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 + 1.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*I\nsage: d = c.real()\nsage: d\n2.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\nsage: d._pari_()\n2.00000000000000\n```\n\nSo here is the problem, right in the change to Pari from the RealField.",
    "created_at": "2011-08-19T14:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58632",
    "user": "https://github.com/kcrisman"
}
```

Correct.  Here's the problem, I think.

```

sage: C = ComplexField(1000)
sage: c = C(2+I)
sage: c
2.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 + 1.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*I
sage: d = c.real()
sage: d
2.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
sage: d._pari_()
2.00000000000000
```

So here is the problem, right in the change to Pari from the RealField.



---

archive/issue_comments_058633.json:
```json
{
    "body": "A probably related bug was just reported on [sage-support](https://groups.google.com/forum/#!topic/sage-support/RrveCpPgoKU):\n\n```\nsage: numerical_approx(gamma(9, 10^(-3))-gamma(9), digits=40)\n0.000000000000000\n```\n\nThe correct answer is approximately -1.1101115655 * 10<sup>-28</sup>.",
    "created_at": "2014-05-03T23:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58633",
    "user": "https://github.com/pjbruin"
}
```

A probably related bug was just reported on [sage-support](https://groups.google.com/forum/#!topic/sage-support/RrveCpPgoKU):

```
sage: numerical_approx(gamma(9, 10^(-3))-gamma(9), digits=40)
0.000000000000000
```

The correct answer is approximately -1.1101115655 * 10<sup>-28</sup>.



---

archive/issue_comments_058634.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2014-05-04T00:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58634",
    "user": "https://github.com/pjbruin"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_058635.json:
```json
{
    "body": "Here is a somewhat rough fix.  It doesn't take into account the precisions of both input parameters separately, but uses the precision of the desired parent in `Function_gamma_inc`, and the precision of the parent of the first argument in `ComplexNumber.gamma_inc()` et al.  Maybe an expert on this can say whether this behaviour is consistent with other special functions in Sage?\n\n(Note that the relatively low precision in the new doctest is because of cancellation.)",
    "created_at": "2014-05-04T00:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58635",
    "user": "https://github.com/pjbruin"
}
```

Here is a somewhat rough fix.  It doesn't take into account the precisions of both input parameters separately, but uses the precision of the desired parent in `Function_gamma_inc`, and the precision of the parent of the first argument in `ComplexNumber.gamma_inc()` et al.  Maybe an expert on this can say whether this behaviour is consistent with other special functions in Sage?

(Note that the relatively low precision in the new doctest is because of cancellation.)



---

archive/issue_comments_058636.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-04T00:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58636",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_058637.json:
```json
{
    "body": "I'm wondering if this a bug in the `gamma` function or in symbolic functions in general...",
    "created_at": "2014-05-04T09:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58637",
    "user": "https://github.com/jdemeyer"
}
```

I'm wondering if this a bug in the `gamma` function or in symbolic functions in general...



---

archive/issue_comments_058638.json:
```json
{
    "body": "Isn't this the only and actual bug? That the following doesn't depend on the `prec` parameter.\n\n```\nsage: numerical_approx(gamma(9,10^-3), prec=1024)                                    \n40320.0000000000\n```\n",
    "created_at": "2014-05-04T09:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58638",
    "user": "https://github.com/jdemeyer"
}
```

Isn't this the only and actual bug? That the following doesn't depend on the `prec` parameter.

```
sage: numerical_approx(gamma(9,10^-3), prec=1024)                                    
40320.0000000000
```




---

archive/issue_comments_058639.json:
```json
{
    "body": "I don't know whether the change to `src/sage/functions/other.py` is right (I'm not saying it is wrong, just don't know), but the adding of the precision arguments is obviously needed.",
    "created_at": "2014-05-04T09:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58639",
    "user": "https://github.com/jdemeyer"
}
```

I don't know whether the change to `src/sage/functions/other.py` is right (I'm not saying it is wrong, just don't know), but the adding of the precision arguments is obviously needed.



---

archive/issue_comments_058640.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-04T13:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58640",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_058641.json:
```json
{
    "body": "Setting priority to critical because the bug leads to mathematically incorrect answers.\n\nThe original bug is already solved by passing the correct precision to PARI's `incgam()`.\n\nThe bug in comment:5 should be solved by the additional changes to `Function_gamma_inc._evalf_()`.",
    "created_at": "2014-05-04T13:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58641",
    "user": "https://github.com/pjbruin"
}
```

Setting priority to critical because the bug leads to mathematically incorrect answers.

The original bug is already solved by passing the correct precision to PARI's `incgam()`.

The bug in comment:5 should be solved by the additional changes to `Function_gamma_inc._evalf_()`.



---

archive/issue_comments_058642.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-05-04T13:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58642",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_058643.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2014-05-04T13:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58643",
    "user": "https://github.com/pjbruin"
}
```

Changing priority from major to critical.



---

archive/issue_comments_058644.json:
```json
{
    "body": "Replying to [comment:12 pbruin]:\n> The bug in comment:5 should be solved by the additional changes to `Function_gamma_inc._evalf_()`.\nI think it is better not to confuse these 2 different bugs.",
    "created_at": "2014-05-04T19:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58644",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:12 pbruin]:
> The bug in comment:5 should be solved by the additional changes to `Function_gamma_inc._evalf_()`.
I think it is better not to confuse these 2 different bugs.



---

archive/issue_comments_058645.json:
```json
{
    "body": "Replying to [comment:9 jdemeyer]:\n> Isn't this the only and actual bug? That the following doesn't depend on the `prec` parameter.\n> {{{\n> sage: numerical_approx(gamma(9,10^-3), prec=1024)                                    \n> 40320.0000000000\n> }}}\n\nis `prec` parameter mentioned in the doc on `gamma`? It doesn't, IMHO. \nAre there other transcendentals for which this parameter does work?",
    "created_at": "2014-05-04T19:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58645",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:9 jdemeyer]:
> Isn't this the only and actual bug? That the following doesn't depend on the `prec` parameter.
> {{{
> sage: numerical_approx(gamma(9,10^-3), prec=1024)                                    
> 40320.0000000000
> }}}

is `prec` parameter mentioned in the doc on `gamma`? It doesn't, IMHO. 
Are there other transcendentals for which this parameter does work?



---

archive/issue_comments_058646.json:
```json
{
    "body": "\"`TestsPassed 6.2.rc2`\" http://patchbot.sagemath.org/ticket/7099/",
    "created_at": "2014-05-05T06:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58646",
    "user": "https://github.com/rwst"
}
```

"`TestsPassed 6.2.rc2`" http://patchbot.sagemath.org/ticket/7099/



---

archive/issue_comments_058647.json:
```json
{
    "body": "> > Isn't this the only and actual bug? That the following doesn't depend on the `prec` parameter.\n> > {{{\n> > sage: numerical_approx(gamma(9,10^-3), prec=1024)                                    \n> > 40320.0000000000\n> > }}}\n> \n> is `prec` parameter mentioned in the doc on `gamma`? It doesn't, IMHO. \n> Are there other transcendentals for which this parameter does work?\nI was pretty sure we were deprecating the `prec` keyword **inside** such functions.  But this is apparently a keyword of `numerical_approx`, which is different.  In which case it should just pass the precision on correctly somewhere else.",
    "created_at": "2014-05-05T17:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58647",
    "user": "https://github.com/kcrisman"
}
```

> > Isn't this the only and actual bug? That the following doesn't depend on the `prec` parameter.
> > {{{
> > sage: numerical_approx(gamma(9,10^-3), prec=1024)                                    
> > 40320.0000000000
> > }}}
> 
> is `prec` parameter mentioned in the doc on `gamma`? It doesn't, IMHO. 
> Are there other transcendentals for which this parameter does work?
I was pretty sure we were deprecating the `prec` keyword **inside** such functions.  But this is apparently a keyword of `numerical_approx`, which is different.  In which case it should just pass the precision on correctly somewhere else.



---

archive/issue_comments_058648.json:
```json
{
    "body": "With #16697 the output is as expected:\n\n```\nsage: C = ComplexField(1000)\nsage: gamma_inc(C(2+I),C(3+I))\n0.121515644664508695525971545977439666159749344176962379708992904126499444842886620664991650378432544392118359044438541514683402245033018771644222346410367471459456844674335147722343580581945662693850674590491020834632434082710800093315646442975240326569517738365018117780134100101636704042869033248174 + 0.101533909079826033296475736021224621546966200987295663190553587086145836461236284668967411665020429964946098113930918849948956425984499549094441904693395768367238320065064071027383069839637218088862214571990869510941211277488169032567679631037683814516738122300220474252081775895835843619616213883517*I\n```\n\nThis is because I changed the default to mpmath for the gamma functions. The ticket is still relevant for `C(2+I).gamma_inc(C(3+I))` however.",
    "created_at": "2014-08-10T09:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58648",
    "user": "https://github.com/rwst"
}
```

With #16697 the output is as expected:

```
sage: C = ComplexField(1000)
sage: gamma_inc(C(2+I),C(3+I))
0.121515644664508695525971545977439666159749344176962379708992904126499444842886620664991650378432544392118359044438541514683402245033018771644222346410367471459456844674335147722343580581945662693850674590491020834632434082710800093315646442975240326569517738365018117780134100101636704042869033248174 + 0.101533909079826033296475736021224621546966200987295663190553587086145836461236284668967411665020429964946098113930918849948956425984499549094441904693395768367238320065064071027383069839637218088862214571990869510941211277488169032567679631037683814516738122300220474252081775895835843619616213883517*I
```

This is because I changed the default to mpmath for the gamma functions. The ticket is still relevant for `C(2+I).gamma_inc(C(3+I))` however.



---

archive/issue_comments_058649.json:
```json
{
    "body": "Patchbot was happy at 6.2beta2 so I guess it's still good. The changes look straightforward, anyway.",
    "created_at": "2014-08-10T13:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58649",
    "user": "https://github.com/rwst"
}
```

Patchbot was happy at 6.2beta2 so I guess it's still good. The changes look straightforward, anyway.



---

archive/issue_comments_058650.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-08-10T13:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58650",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058651.json:
```json
{
    "body": "On the Arando buildbot:\n\n```\nsage -t --long src/sage/rings/complex_mpc.pyx\n**********************************************************************\nFile \"src/sage/rings/complex_mpc.pyx\", line 2241, in sage.rings.complex_mpc.MPComplexNumber.gamma_inc\nFailed example:\n    (1+i).gamma_inc(2 + 3*i)\nExpected:\n    0.0020969149 - 0.059981914*I\nGot:\n    0.0020969148 - 0.059981914*I\n**********************************************************************\n1 item had failures:\n   1 of   5 in sage.rings.complex_mpc.MPComplexNumber.gamma_inc\n    [375 tests, 1 failure, 0.27 s]\nsage -t --long src/sage/rings/complex_number.pyx\n**********************************************************************\nFile \"src/sage/rings/complex_number.pyx\", line 2023, in sage.rings.complex_number.ComplexNumber.gamma_inc\nFailed example:\n    (1+i).gamma_inc(2 + 3*i)\nExpected:\n    0.0020969149 - 0.059981914*I\nGot:\n    0.0020969148 - 0.059981914*I\n**********************************************************************\n1 item had failures:\n   1 of   8 in sage.rings.complex_number.ComplexNumber.gamma_inc\n    [378 tests, 1 failure, 3.12 s]\n```\n",
    "created_at": "2014-08-10T23:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58651",
    "user": "https://github.com/vbraun"
}
```

On the Arando buildbot:

```
sage -t --long src/sage/rings/complex_mpc.pyx
**********************************************************************
File "src/sage/rings/complex_mpc.pyx", line 2241, in sage.rings.complex_mpc.MPComplexNumber.gamma_inc
Failed example:
    (1+i).gamma_inc(2 + 3*i)
Expected:
    0.0020969149 - 0.059981914*I
Got:
    0.0020969148 - 0.059981914*I
**********************************************************************
1 item had failures:
   1 of   5 in sage.rings.complex_mpc.MPComplexNumber.gamma_inc
    [375 tests, 1 failure, 0.27 s]
sage -t --long src/sage/rings/complex_number.pyx
**********************************************************************
File "src/sage/rings/complex_number.pyx", line 2023, in sage.rings.complex_number.ComplexNumber.gamma_inc
Failed example:
    (1+i).gamma_inc(2 + 3*i)
Expected:
    0.0020969149 - 0.059981914*I
Got:
    0.0020969148 - 0.059981914*I
**********************************************************************
1 item had failures:
   1 of   8 in sage.rings.complex_number.ComplexNumber.gamma_inc
    [378 tests, 1 failure, 3.12 s]
```




---

archive/issue_comments_058652.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2014-08-10T23:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58652",
    "user": "https://github.com/vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_058653.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-11T09:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58653",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_058654.json:
```json
{
    "body": "I'm assuming this fix does not absolutely require another review round...",
    "created_at": "2014-08-11T09:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58654",
    "user": "https://github.com/pjbruin"
}
```

I'm assuming this fix does not absolutely require another review round...



---

archive/issue_comments_058655.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-08-11T09:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58655",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_058656.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-08-11T15:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7099#issuecomment-58656",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_007321.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-08-11T15:01:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7099",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7099#event-7321"
}
```
