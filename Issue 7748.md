# Issue 7748: Make incomplete gamma function symbolic

archive/issues_007748.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  mvngu\n\nWe don't appear to have this, though perhaps it is in Pynac/Ginac already.  We also need to translate Maxima's gamma_incomplete to our gamma_inc or incomplete_gamma as part of this ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7748\n\n",
    "created_at": "2009-12-22T17:18:07Z",
    "labels": [
        "symbolics",
        "minor",
        "bug"
    ],
    "title": "Make incomplete gamma function symbolic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7748",
    "user": "kcrisman"
}
```
Assignee: burcin

CC:  mvngu

We don't appear to have this, though perhaps it is in Pynac/Ginac already.  We also need to translate Maxima's gamma_incomplete to our gamma_inc or incomplete_gamma as part of this ticket.

Issue created by migration from https://trac.sagemath.org/ticket/7748





---

archive/issue_comments_066696.json:
```json
{
    "body": "After a quick look at the GiNaC sources, I don't think there is an implementation of the incomplete gamma function in there.\n\nNumerical evaluation of this can be done with the `gammainc()` function of mpmath.\n\nThe conversion should just work, if the conversions dictionary argument of `BuiltinFunction.__init__` contains `maxima='gamma_incomplete'`.",
    "created_at": "2009-12-22T23:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66696",
    "user": "burcin"
}
```

After a quick look at the GiNaC sources, I don't think there is an implementation of the incomplete gamma function in there.

Numerical evaluation of this can be done with the `gammainc()` function of mpmath.

The conversion should just work, if the conversions dictionary argument of `BuiltinFunction.__init__` contains `maxima='gamma_incomplete'`.



---

archive/issue_comments_066697.json:
```json
{
    "body": "Replying to [comment:1 burcin]:\n> After a quick look at the GiNaC sources, I don't think there is an implementation of the incomplete gamma function in there.\n> \nOkay.\n> Numerical evaluation of this can be done with the `gammainc()` function of mpmath.\nBut will it give us symbolic evaluation ala gamma_inc(1,1)=1/e?  That would be best.\n\n> The conversion should just work, if the conversions dictionary argument of `BuiltinFunction.__init__` contains `maxima='gamma_incomplete'`.\nYes, of course, but we still have to do it :)",
    "created_at": "2009-12-23T04:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66697",
    "user": "kcrisman"
}
```

Replying to [comment:1 burcin]:
> After a quick look at the GiNaC sources, I don't think there is an implementation of the incomplete gamma function in there.
> 
Okay.
> Numerical evaluation of this can be done with the `gammainc()` function of mpmath.
But will it give us symbolic evaluation ala gamma_inc(1,1)=1/e?  That would be best.

> The conversion should just work, if the conversions dictionary argument of `BuiltinFunction.__init__` contains `maxima='gamma_incomplete'`.
Yes, of course, but we still have to do it :)



---

archive/issue_comments_066698.json:
```json
{
    "body": "> Numerical evaluation of this can be done with the gammainc() function of mpmath.\n\nDoesn't PARI also have an incomplete gamma implementation (it's used by RR and CC, I think)?",
    "created_at": "2009-12-24T20:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66698",
    "user": "was"
}
```

> Numerical evaluation of this can be done with the gammainc() function of mpmath.

Doesn't PARI also have an incomplete gamma implementation (it's used by RR and CC, I think)?



---

archive/issue_comments_066699.json:
```json
{
    "body": "Make Ei symbolic.",
    "created_at": "2010-02-07T11:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66699",
    "user": "fstan"
}
```

Make Ei symbolic.



---

archive/issue_comments_066700.json:
```json
{
    "body": "Attachment\n\nMake incomplete gamma function symbolic.",
    "created_at": "2010-02-07T11:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66700",
    "user": "fstan"
}
```

Attachment

Make incomplete gamma function symbolic.



---

archive/issue_comments_066701.json:
```json
{
    "body": "The 2 patches should make the incomplete gamma function symbolic. The exponential integral Ei was used in its symbolic evaluation, therefore it was also made symbolic.",
    "created_at": "2010-02-07T11:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66701",
    "user": "fstan"
}
```

The 2 patches should make the incomplete gamma function symbolic. The exponential integral Ei was used in its symbolic evaluation, therefore it was also made symbolic.



---

archive/issue_comments_066702.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-07T11:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66702",
    "user": "fstan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066703.json:
```json
{
    "body": "I tried the exponential integral patch and it works ok. However I don't understand the changes in\nrandom_tests.py. Also the following could be evaluated:\n\n```\nsage: diff(Ei(x),x)\nD[0](Ei)(x)\nsage: integrate(Ei(x),x)\nintegrate(Ei(x), x)\n```\n\nShould this be in a separate ticket?",
    "created_at": "2010-02-07T21:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66703",
    "user": "zimmerma"
}
```

I tried the exponential integral patch and it works ok. However I don't understand the changes in
random_tests.py. Also the following could be evaluated:

```
sage: diff(Ei(x),x)
D[0](Ei)(x)
sage: integrate(Ei(x),x)
integrate(Ei(x), x)
```

Should this be in a separate ticket?



---

archive/issue_comments_066704.json:
```json
{
    "body": "Replying to [comment:5 zimmerma]:\n> I tried the exponential integral patch and it works ok. However I don't understand the changes in\n> random_tests.py. \n\nThis makes a 'random' symbolic expression, and when we add new symbolic functions (and sometimes when we change them) this doctest needs to be changed, not because anything bad happened.",
    "created_at": "2010-02-08T02:19:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66704",
    "user": "kcrisman"
}
```

Replying to [comment:5 zimmerma]:
> I tried the exponential integral patch and it works ok. However I don't understand the changes in
> random_tests.py. 

This makes a 'random' symbolic expression, and when we add new symbolic functions (and sometimes when we change them) this doctest needs to be changed, not because anything bad happened.



---

archive/issue_comments_066705.json:
```json
{
    "body": "Replying to [comment:5 zimmerma]:\n> I tried the exponential integral patch and it works ok. However I don't understand the changes in\n> random_tests.py. Also the following could be evaluated:\n\n```\nsage: diff(Ei(x),x)\nD[0](Ei)(x)\nsage: integrate(Ei(x),x)\nintegrate(Ei(x), x)\n```\n\n> Should this be in a separate ticket?\n\nThank you for the review. I'll include the derivative and submit again. Integration looks more complicated.\n\nGreetings, \n\nFlavia",
    "created_at": "2010-02-08T11:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66705",
    "user": "fstan"
}
```

Replying to [comment:5 zimmerma]:
> I tried the exponential integral patch and it works ok. However I don't understand the changes in
> random_tests.py. Also the following could be evaluated:

```
sage: diff(Ei(x),x)
D[0](Ei)(x)
sage: integrate(Ei(x),x)
integrate(Ei(x), x)
```

> Should this be in a separate ticket?

Thank you for the review. I'll include the derivative and submit again. Integration looks more complicated.

Greetings, 

Flavia



---

archive/issue_comments_066706.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-08T11:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66706",
    "user": "fstan"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066707.json:
```json
{
    "body": "Changing assignee from burcin to zimmerma.",
    "created_at": "2010-02-08T13:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66707",
    "user": "zimmerma"
}
```

Changing assignee from burcin to zimmerma.



---

archive/issue_comments_066708.json:
```json
{
    "body": "I tried sage -t * with both patches, and I get one additional failure with respect to those I get\ndue to #7773:\n\n```\ntarte% sage -t \"rings/complex_number.pyx\"\nsage -t  \"rings/complex_number.pyx\"                         \n**********************************************************************\nFile \"/usr/local/sage-4.3-core2/devel/sage-main/sage/rings/complex_number.pyx\", line 1611:\n    sage: gamma_inc(2, 5)\nExpected:\n    0.0404276819945128\nGot:\n    gamma(2, 5)\n```\n\nConsider also the following:\n\n```\nsage: gamma_inc(2, 5.)\n0.0404276819945128\nsage: gamma(2, 5) \n1\n```\n",
    "created_at": "2010-02-08T13:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66708",
    "user": "zimmerma"
}
```

I tried sage -t * with both patches, and I get one additional failure with respect to those I get
due to #7773:

```
tarte% sage -t "rings/complex_number.pyx"
sage -t  "rings/complex_number.pyx"                         
**********************************************************************
File "/usr/local/sage-4.3-core2/devel/sage-main/sage/rings/complex_number.pyx", line 1611:
    sage: gamma_inc(2, 5)
Expected:
    0.0404276819945128
Got:
    gamma(2, 5)
```

Consider also the following:

```
sage: gamma_inc(2, 5.)
0.0404276819945128
sage: gamma(2, 5) 
1
```




---

archive/issue_comments_066709.json:
```json
{
    "body": "Replying to [comment:8 zimmerma]:\n\n> Consider also the following:\n\n```\nsage: gamma_inc(2, 5.)\n0.0404276819945128\nsage: gamma(2, 5) \n1\n```\n\n\nWe should write a python function wrapping `gamma_inc` and `gamma`, similar to the provided for `psi()` in #6961.\n\nThe fact that `gamma()` accepts two arguments at the moment is a bug that I introduced in #7490. Looking at the code, it also doesn't handle the `prec` parameter correctly. I'll upload a patch with a wrapper `gamma()` function and a fix for the `prec` issue.\n\nReplying to [comment:7 fstan]:\n\n> Integration looks more complicated. \n\nIntegration cannot be handled with a custom method in symbolic functions. The patches attached to #6465 should make this easier.",
    "created_at": "2010-02-08T16:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66709",
    "user": "burcin"
}
```

Replying to [comment:8 zimmerma]:

> Consider also the following:

```
sage: gamma_inc(2, 5.)
0.0404276819945128
sage: gamma(2, 5) 
1
```


We should write a python function wrapping `gamma_inc` and `gamma`, similar to the provided for `psi()` in #6961.

The fact that `gamma()` accepts two arguments at the moment is a bug that I introduced in #7490. Looking at the code, it also doesn't handle the `prec` parameter correctly. I'll upload a patch with a wrapper `gamma()` function and a fix for the `prec` issue.

Replying to [comment:7 fstan]:

> Integration looks more complicated. 

Integration cannot be handled with a custom method in symbolic functions. The patches attached to #6465 should make this easier.



---

archive/issue_comments_066710.json:
```json
{
    "body": "Flavia, please can you fix the rings/complex_number.pyx issue?",
    "created_at": "2010-02-10T12:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66710",
    "user": "zimmerma"
}
```

Flavia, please can you fix the rings/complex_number.pyx issue?



---

archive/issue_comments_066711.json:
```json
{
    "body": "Attachment\n\nAdded derivative method.",
    "created_at": "2010-02-15T23:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66711",
    "user": "fstan"
}
```

Attachment

Added derivative method.



---

archive/issue_comments_066712.json:
```json
{
    "body": "Fixed tests from complex_number.pyx",
    "created_at": "2010-02-15T23:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66712",
    "user": "fstan"
}
```

Fixed tests from complex_number.pyx



---

archive/issue_comments_066713.json:
```json
{
    "body": "Attachment\n\nI've uploaded new patches which should fix the docs and the derivative.\n\nGreetings,\n\nFlavia",
    "created_at": "2010-02-15T23:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66713",
    "user": "fstan"
}
```

Attachment

I've uploaded new patches which should fix the docs and the derivative.

Greetings,

Flavia



---

archive/issue_comments_066714.json:
```json
{
    "body": "Attachment\n\nrebased to 4.3.3.alpha1",
    "created_at": "2010-02-20T17:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66714",
    "user": "burcin"
}
```

Attachment

rebased to 4.3.3.alpha1



---

archive/issue_comments_066715.json:
```json
{
    "body": "rebased to 4.3.3.alpha1",
    "created_at": "2010-02-20T17:51:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66715",
    "user": "burcin"
}
```

rebased to 4.3.3.alpha1



---

archive/issue_comments_066716.json:
```json
{
    "body": "Attachment\n\nwrapper for gamma and incomplete gamma",
    "created_at": "2010-02-20T17:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66716",
    "user": "burcin"
}
```

Attachment

wrapper for gamma and incomplete gamma



---

archive/issue_comments_066717.json:
```json
{
    "body": "Attachment\n\nwrapper for gamma and incomplete gamma",
    "created_at": "2010-02-20T17:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66717",
    "user": "burcin"
}
```

Attachment

wrapper for gamma and incomplete gamma



---

archive/issue_comments_066718.json:
```json
{
    "body": "attachment:trac_7748-gamma_wrapper.2.patch adds a new wrapper function to call gamma or incomplete gamma depending on the number of arguments. It also corrects the way `prec` parameter to `gamma` was handled.\n\nFlavia's patches needed to be rebased to 4.3.3.alpha1 since the changes to `random_tests.py` didn't apply anymore.\n\nThe patches to be applied are (in this order):\n* attachment:trac_7748-exp_integral_ver2.4.3.3.alpha1.patch\n* attachment:trac_7748-incomplete_gamma_ver2.4.3.3.alpha1.patch\n* attachment:trac_7748-gamma_wrapper.2.patch\n\nI'm changing this to needs review. :)",
    "created_at": "2010-02-20T18:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66718",
    "user": "burcin"
}
```

attachment:trac_7748-gamma_wrapper.2.patch adds a new wrapper function to call gamma or incomplete gamma depending on the number of arguments. It also corrects the way `prec` parameter to `gamma` was handled.

Flavia's patches needed to be rebased to 4.3.3.alpha1 since the changes to `random_tests.py` didn't apply anymore.

The patches to be applied are (in this order):
* attachment:trac_7748-exp_integral_ver2.4.3.3.alpha1.patch
* attachment:trac_7748-incomplete_gamma_ver2.4.3.3.alpha1.patch
* attachment:trac_7748-gamma_wrapper.2.patch

I'm changing this to needs review. :)



---

archive/issue_comments_066719.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-20T18:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66719",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066720.json:
```json
{
    "body": "a partial review against 4.3.3:\n\n```\nsage -t  \"devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py\"\n...\n    sage: E.Lambda(1.4+0.5*I, 50)\n      File \"/usr/local/sage-4.3.3/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3088, in Lambda\n        Gamma_inc = transcendental.gamma_inc\n    AttributeError: 'module' object has no attribute 'gamma_inc'\n```\n\nThis test was ok with vanilla 4.3.3.",
    "created_at": "2010-02-24T07:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66720",
    "user": "zimmerma"
}
```

a partial review against 4.3.3:

```
sage -t  "devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py"
...
    sage: E.Lambda(1.4+0.5*I, 50)
      File "/usr/local/sage-4.3.3/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 3088, in Lambda
        Gamma_inc = transcendental.gamma_inc
    AttributeError: 'module' object has no attribute 'gamma_inc'
```

This test was ok with vanilla 4.3.3.



---

archive/issue_comments_066721.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-24T07:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66721",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066722.json:
```json
{
    "body": "apart from the above failure, all tests pass with sage 4.3.3 (apart from the Fedora 12 Segfaults).",
    "created_at": "2010-02-24T08:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66722",
    "user": "zimmerma"
}
```

apart from the above failure, all tests pass with sage 4.3.3 (apart from the Fedora 12 Segfaults).



---

archive/issue_comments_066723.json:
```json
{
    "body": "Attachment\n\nfix new doctest failure",
    "created_at": "2010-03-02T11:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66723",
    "user": "burcin"
}
```

Attachment

fix new doctest failure



---

archive/issue_comments_066724.json:
```json
{
    "body": "I added a fix for the doctest failure in comment:13 to my patch, attachment:trac_7748-gamma_wrapper.3.patch.\n\nThe patches to be applied are (in this order): \n\n* attachment:trac_7748-exp_integral_ver2.4.3.3.alpha1.patch\n* attachment:trac_7748-incomplete_gamma_ver2.4.3.3.alpha1.patch\n* attachment:trac_7748-gamma_wrapper.3.patch\n\nI am OK with Flavia's changes. If someone can review my patch this can still get in 4.3.4. :)",
    "created_at": "2010-03-02T11:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66724",
    "user": "burcin"
}
```

I added a fix for the doctest failure in comment:13 to my patch, attachment:trac_7748-gamma_wrapper.3.patch.

The patches to be applied are (in this order): 

* attachment:trac_7748-exp_integral_ver2.4.3.3.alpha1.patch
* attachment:trac_7748-incomplete_gamma_ver2.4.3.3.alpha1.patch
* attachment:trac_7748-gamma_wrapper.3.patch

I am OK with Flavia's changes. If someone can review my patch this can still get in 4.3.4. :)



---

archive/issue_comments_066725.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-02T11:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66725",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066726.json:
```json
{
    "body": "Everything works now. Great work!\n\nPaul",
    "created_at": "2010-03-03T12:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66726",
    "user": "zimmerma"
}
```

Everything works now. Great work!

Paul



---

archive/issue_comments_066727.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-03T12:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66727",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066728.json:
```json
{
    "body": "Hi Minh,\n\nWhat is holding up this ticket? Note that it has a positive review and the patches to be applied are listed in comment:15.\n\nCheers,\n\nBurcin",
    "created_at": "2010-03-17T08:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66728",
    "user": "burcin"
}
```

Hi Minh,

What is holding up this ticket? Note that it has a positive review and the patches to be applied are listed in comment:15.

Cheers,

Burcin



---

archive/issue_comments_066729.json:
```json
{
    "body": "Replying to [comment:17 burcin]:\n> What is holding up this ticket?\nI can't merge this ticket. We are now in feature freeze.",
    "created_at": "2010-03-17T08:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66729",
    "user": "mvngu"
}
```

Replying to [comment:17 burcin]:
> What is holding up this ticket?
I can't merge this ticket. We are now in feature freeze.



---

archive/issue_comments_066730.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n\n- trac_7748-exp_integral_ver2.4.3.3.alpha1.patch\n- trac_7748-incomplete_gamma_ver2.4.3.3.alpha1.patch\n- trac_7748-gamma_wrapper.3.patch",
    "created_at": "2010-04-15T20:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66730",
    "user": "jhpalmieri"
}
```

Merged in 4.4.alpha0:

- trac_7748-exp_integral_ver2.4.3.3.alpha1.patch
- trac_7748-incomplete_gamma_ver2.4.3.3.alpha1.patch
- trac_7748-gamma_wrapper.3.patch



---

archive/issue_comments_066731.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7748#issuecomment-66731",
    "user": "jhpalmieri"
}
```

Resolution: fixed
