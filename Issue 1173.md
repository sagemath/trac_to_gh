# Issue 1173: implement numerical evaluation of erf at complex arguments via mpmath algorithm

archive/issues_001173.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @benjaminfjones\n\nKeywords: sd35.5\n\nWhen implemented, this would work:\n\n```\nsage: erf(2.0, algorithm='mpmath')\n...\n```\n\n---\n\nApply patch [attachment:trac_1173_complex_erf_v3.patch trac_1173_complex_erf_v3.patch]  attached to this ticket to the Sage library.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1173\n\n",
    "closed_at": "2013-06-19T12:16:37Z",
    "created_at": "2007-11-15T07:45:25Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "implement numerical evaluation of erf at complex arguments via mpmath algorithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1173",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @benjaminfjones

Keywords: sd35.5

When implemented, this would work:

```
sage: erf(2.0, algorithm='mpmath')
...
```

---

Apply patch [attachment:trac_1173_complex_erf_v3.patch trac_1173_complex_erf_v3.patch]  attached to this ticket to the Sage library.

Issue created by migration from https://trac.sagemath.org/ticket/1173





---

archive/issue_comments_007174.json:
```json
{
    "body": "See also\nhttp://trac.sagemath.org/sage_trac/ticket/1174",
    "created_at": "2007-11-15T07:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7174",
    "user": "https://github.com/williamstein"
}
```

See also
http://trac.sagemath.org/sage_trac/ticket/1174



---

archive/issue_comments_007175.json:
```json
{
    "body": "The following has a GPL'd implementation in c:\n\nhttp://velveeta.che.wisc.edu/octave/lists/archive/octave-sources.1998/msg00032.html",
    "created_at": "2007-11-15T08:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7175",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

The following has a GPL'd implementation in c:

http://velveeta.che.wisc.edu/octave/lists/archive/octave-sources.1998/msg00032.html



---

archive/issue_comments_007176.json:
```json
{
    "body": "This looks like the wya to go:\n\nJosh Kantor:\n\n```\nscipy has an error function that takes complex arguments\n\nsage:  import numpy, scipy\nsage:  from scipy import special\nsage:  j=numpy.complex(0,1)\nsage: -j*float(sqrt(pi))*special.erf(2*j)/2\n(16.45262776550727+0j)\n\nUnfortunately numpy and sage's complex numbers are not compatible yet.\n\n\n```",
    "created_at": "2007-11-16T18:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7176",
    "user": "https://github.com/williamstein"
}
```

This looks like the wya to go:

Josh Kantor:

```
scipy has an error function that takes complex arguments

sage:  import numpy, scipy
sage:  from scipy import special
sage:  j=numpy.complex(0,1)
sage: -j*float(sqrt(pi))*special.erf(2*j)/2
(16.45262776550727+0j)

Unfortunately numpy and sage's complex numbers are not compatible yet.


```



---

archive/issue_comments_007177.json:
```json
{
    "body": "Numpy and Sage numbers now seem to work well, at least to some extent:\n\n```\nsage: import numpy\nsage: CC(numpy.complex(0,1))\n1.00000000000000*I\nsage: CC(numpy.complex(1,1))\n1.00000000000000 + 1.00000000000000*I\nsage: import scipy\nsage: CC(scipy.special.erf(numpy.complex(1,1)))\n1.31615128169795 + 0.190453469237835*I\n```\nIs it time to wrap this now, two years after opening?",
    "created_at": "2009-12-30T04:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7177",
    "user": "https://github.com/kcrisman"
}
```

Numpy and Sage numbers now seem to work well, at least to some extent:

```
sage: import numpy
sage: CC(numpy.complex(0,1))
1.00000000000000*I
sage: CC(numpy.complex(1,1))
1.00000000000000 + 1.00000000000000*I
sage: import scipy
sage: CC(scipy.special.erf(numpy.complex(1,1)))
1.31615128169795 + 0.190453469237835*I
```
Is it time to wrap this now, two years after opening?



---

archive/issue_comments_007178.json:
```json
{
    "body": "This can also be done by mpmath in arbitrary precision, see\n\n```\nsage: import mpmath\nsage: mpmath.erf?\n```",
    "created_at": "2010-01-02T07:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7178",
    "user": "https://github.com/aghitza"
}
```

This can also be done by mpmath in arbitrary precision, see

```
sage: import mpmath
sage: mpmath.erf?
```



---

archive/issue_comments_007179.json:
```json
{
    "body": "Replying to [comment:5 AlexGhitza]:\n> This can also be done by mpmath in arbitrary precision, see\n> \n> \n> ```\n> sage: import mpmath\n> sage: mpmath.erf?\n> ```\n\n\nAnd erf already has an _eval_f method, so maybe this could be changed to use mpmath?  Even a loss in speed would be worth having the complex values.    This could apply to error_fcn/erfc and others as well.",
    "created_at": "2010-02-05T20:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7179",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:5 AlexGhitza]:
> This can also be done by mpmath in arbitrary precision, see
> 
> 
> ```
> sage: import mpmath
> sage: mpmath.erf?
> ```


And erf already has an _eval_f method, so maybe this could be changed to use mpmath?  Even a loss in speed would be worth having the complex values.    This could apply to error_fcn/erfc and others as well.



---

archive/issue_comments_007180.json:
```json
{
    "body": "Update - yes, we should definitely do this because of the complex values - just had a support request about not being able to do \n\n```\nsage: integrate(sin(x^2),(x,2,6))\n```\nand then use n() because of this (partly).  See also #9044.",
    "created_at": "2010-06-09T01:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7180",
    "user": "https://github.com/kcrisman"
}
```

Update - yes, we should definitely do this because of the complex values - just had a support request about not being able to do 

```
sage: integrate(sin(x^2),(x,2,6))
```
and then use n() because of this (partly).  See also #9044.



---

archive/issue_comments_007181.json:
```json
{
    "body": "Okay, here's v0.prealpha0.0_1a of a patch which uses mpmath to get complex and arbitrary-precision behaviour for erf.  (If it works out we can do error_fcn the same way, as noted by kcrisman).\n\nUnfortunately it does introduce a speed regression:\n\n```\n# 4.6.1, via pari\nsage: timeit('float(erf(0))',number=1000) # must be float because 4.6.1 doesn't evaluate\n1000 loops, best of 3: 109 \u00b5s per loop\nsage: timeit('erf(0.1)',number=1000)\n1000 loops, best of 3: 98.4 \u00b5s per loop\nsage: timeit('erf(0.99)',number=1000)\n1000 loops, best of 3: 98.5 \u00b5s per loop\n\n# 4.6.2rc0 with patch\nsage: timeit('erf(0)',number=1000)\n1000 loops, best of 3: 68.3 \u00b5s per loop\nsage: timeit('erf(0.1)',number=1000)\n1000 loops, best of 3: 154 \u00b5s per loop\nsage: timeit('erf(0.99)',number=1000)\n1000 loops, best of 3: 165 \u00b5s per loop\n```\n\nI attempted to fix this by using the old approach for the default precision, but it usually wound up being more expensive to do the tests.  Someone with better speed-fu is encouraged to look at it.  I haven't finished a long testall yet, so there's probably something somewhere which breaks, but here's the first attempt.",
    "created_at": "2011-02-24T02:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7181",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Okay, here's v0.prealpha0.0_1a of a patch which uses mpmath to get complex and arbitrary-precision behaviour for erf.  (If it works out we can do error_fcn the same way, as noted by kcrisman).

Unfortunately it does introduce a speed regression:

```
# 4.6.1, via pari
sage: timeit('float(erf(0))',number=1000) # must be float because 4.6.1 doesn't evaluate
1000 loops, best of 3: 109 µs per loop
sage: timeit('erf(0.1)',number=1000)
1000 loops, best of 3: 98.4 µs per loop
sage: timeit('erf(0.99)',number=1000)
1000 loops, best of 3: 98.5 µs per loop

# 4.6.2rc0 with patch
sage: timeit('erf(0)',number=1000)
1000 loops, best of 3: 68.3 µs per loop
sage: timeit('erf(0.1)',number=1000)
1000 loops, best of 3: 154 µs per loop
sage: timeit('erf(0.99)',number=1000)
1000 loops, best of 3: 165 µs per loop
```

I attempted to fix this by using the old approach for the default precision, but it usually wound up being more expensive to do the tests.  Someone with better speed-fu is encouraged to look at it.  I haven't finished a long testall yet, so there's probably something somewhere which breaks, but here's the first attempt.



---

archive/issue_comments_007182.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-02-24T09:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7182",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_007183.json:
```json
{
    "body": "Attachment [trac_1173_add_complex_argument_erf.patch](tarball://root/attachments/some-uuid/ticket1173/trac_1173_add_complex_argument_erf.patch) by @burcin created at 2011-02-24 09:31:45\n\nThe patch looks really good. The only problem I spotted after a quick reading is that the code blocks in the documentation should be after `::`. If the `TESTS` title is followed by text, you don't need the `::` after that.\n\nAFAIR, mpmath now supports extracting the precision from the input type in Sage. It is not necessary to do this in each calling function any more. I don't have an example handy though.\n\nFor examples of fast methods to check the type of the input you can look at `sage/symbolic/pynac.pyx`. If you replace the `PY_TYPE_CHECK()` calls with `isinstance()` you should get a reasonable speed from python.",
    "created_at": "2011-02-24T09:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7183",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_1173_add_complex_argument_erf.patch](tarball://root/attachments/some-uuid/ticket1173/trac_1173_add_complex_argument_erf.patch) by @burcin created at 2011-02-24 09:31:45

The patch looks really good. The only problem I spotted after a quick reading is that the code blocks in the documentation should be after `::`. If the `TESTS` title is followed by text, you don't need the `::` after that.

AFAIR, mpmath now supports extracting the precision from the input type in Sage. It is not necessary to do this in each calling function any more. I don't have an example handy though.

For examples of fast methods to check the type of the input you can look at `sage/symbolic/pynac.pyx`. If you replace the `PY_TYPE_CHECK()` calls with `isinstance()` you should get a reasonable speed from python.



---

archive/issue_comments_007184.json:
```json
{
    "body": "`@`burcin:\n\nOkay, so just to be clear: EXAMPLES and TESTS don't need trailing colons, whether double or single (although double does seem pretty common; is it okay to use it?), but I should definitely use a double colon after test descriptions, e.g.\n\n```\nTESTS[::?]\n\nTest that addition works::\n\n    sage: 2+3\n    5\n\nTest that subtraction works::\n\n    sage: 3-2\n    1\n\n```\n\ninstead of\n\n```\nTESTS::\n\nTest that addition works:\n\n    sage: 2+3\n    5\n\nTest that subtraction works:\n\n    sage: 3-2\n    1\n```\n\nThat's easy enough to fix.  The other two will take a bit more work, but I'll see what I can find.  Examples to pattern after are very welcome.  `:-)`",
    "created_at": "2011-02-24T09:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7184",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

`@`burcin:

Okay, so just to be clear: EXAMPLES and TESTS don't need trailing colons, whether double or single (although double does seem pretty common; is it okay to use it?), but I should definitely use a double colon after test descriptions, e.g.

```
TESTS[::?]

Test that addition works::

    sage: 2+3
    5

Test that subtraction works::

    sage: 3-2
    1

```

instead of

```
TESTS::

Test that addition works:

    sage: 2+3
    5

Test that subtraction works:

    sage: 3-2
    1
```

That's easy enough to fix.  The other two will take a bit more work, but I'll see what I can find.  Examples to pattern after are very welcome.  `:-)`



---

archive/issue_comments_007185.json:
```json
{
    "body": "Usually we use one colon after `TEST` if there is text after it.  The double colon needs to be before any actual test block.  Also, doing `./sage -docbuild reference html` should give warning messages if it's wrong, if the file is in the reference manual (not all are).",
    "created_at": "2011-02-24T14:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7185",
    "user": "https://github.com/kcrisman"
}
```

Usually we use one colon after `TEST` if there is text after it.  The double colon needs to be before any actual test block.  Also, doing `./sage -docbuild reference html` should give warning messages if it's wrong, if the file is in the reference manual (not all are).



---

archive/issue_comments_007186.json:
```json
{
    "body": "It seems like most of the speed decrease isn't due to anything I'm doing in _evalf_ but in _eval_, namely that I have one as opposed to the default BuiltinFunction._eval_.  When I switch back to the default one I recover the old speeds, except that I no longer know how to get erf(0)=0 without wrapping the whole thing, and it has strange ideas about which arguments shouldn't be evaluated (such as ComplexField).  I also didn't manage to find whatever mpmath magic will allow me to avoid the if isinstance(parent, Parent) and hasattr(parent, 'prec') or try: parent.prec() approach.\n\nI'm at a loss for ways to proceed that don't involve modifying function.pyx, cythonizing, or wrapping the entire function to patch the holes.",
    "created_at": "2011-02-25T15:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7186",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

It seems like most of the speed decrease isn't due to anything I'm doing in _evalf_ but in _eval_, namely that I have one as opposed to the default BuiltinFunction._eval_.  When I switch back to the default one I recover the old speeds, except that I no longer know how to get erf(0)=0 without wrapping the whole thing, and it has strange ideas about which arguments shouldn't be evaluated (such as ComplexField).  I also didn't manage to find whatever mpmath magic will allow me to avoid the if isinstance(parent, Parent) and hasattr(parent, 'prec') or try: parent.prec() approach.

I'm at a loss for ways to proceed that don't involve modifying function.pyx, cythonizing, or wrapping the entire function to patch the holes.



---

archive/issue_comments_007187.json:
```json
{
    "body": "Replying to [comment:12 dsm]:\n> I'm at a loss for ways to proceed that don't involve modifying function.pyx, cythonizing, or wrapping the entire function to patch the holes.  \n\n\nThe speed problems can be solved by replacing the zero test `x == 0` with the example in comment:17:ticket:11143. The patch attached to that ticket also contains an example call to mpmath without the `prec` clutter. AFAICT, the only remaining issue with this ticket is the docstring formatting.\n\nI'd be happy to give positive review to a patch with these changes... :)",
    "created_at": "2011-06-17T19:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7187",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:12 dsm]:
> I'm at a loss for ways to proceed that don't involve modifying function.pyx, cythonizing, or wrapping the entire function to patch the holes.  


The speed problems can be solved by replacing the zero test `x == 0` with the example in comment:17:ticket:11143. The patch attached to that ticket also contains an example call to mpmath without the `prec` clutter. AFAICT, the only remaining issue with this ticket is the docstring formatting.

I'd be happy to give positive review to a patch with these changes... :)



---

archive/issue_comments_007188.json:
```json
{
    "body": "I'd say that it should also add one *very* minor additional doctest, for `erf(sqrt(2))`.  That would allow us to close #9044 without not having a doctest.  I realize that symbolic input is checked, but it would be nice to have for completeness and addressing specific user requests :)",
    "created_at": "2011-06-17T19:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7188",
    "user": "https://github.com/kcrisman"
}
```

I'd say that it should also add one *very* minor additional doctest, for `erf(sqrt(2))`.  That would allow us to close #9044 without not having a doctest.  I realize that symbolic input is checked, but it would be nice to have for completeness and addressing specific user requests :)



---

archive/issue_comments_007189.json:
```json
{
    "body": "Here's another thing that should be added, reported by one of the PREP workshop participants before this patch was in:\n\n```\nerf(4500).n()\n1.0000000\nerf(45000).n()\n<boom>\n```\nSo Pari was not handling big number in erf before.  With this patch, though\n\n```\nsage: erf(4500).n()\n1.00000000000000\nsage: erf(45000).n()\n1.00000000000000\nsage: erf(4500000000).n()\n1.00000000000000\n```\nSince none of the doctests in the current patch seem to test \"big\" real input to erf, we should add this too.",
    "created_at": "2011-06-20T15:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7189",
    "user": "https://github.com/kcrisman"
}
```

Here's another thing that should be added, reported by one of the PREP workshop participants before this patch was in:

```
erf(4500).n()
1.0000000
erf(45000).n()
<boom>
```
So Pari was not handling big number in erf before.  With this patch, though

```
sage: erf(4500).n()
1.00000000000000
sage: erf(45000).n()
1.00000000000000
sage: erf(4500000000).n()
1.00000000000000
```
Since none of the doctests in the current patch seem to test "big" real input to erf, we should add this too.



---

archive/issue_comments_007190.json:
```json
{
    "body": "This should also solve #11626, I think?",
    "created_at": "2011-08-01T16:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7190",
    "user": "https://github.com/kcrisman"
}
```

This should also solve #11626, I think?



---

archive/issue_comments_007191.json:
```json
{
    "body": "Replying to [comment:16 kcrisman]:\n> This should also solve #11626, I think?\n\n\nright, thus #11626 can be closed as soon as this ticket is closed\n(or maybe right now?).\n\nDouglas, can you implement the work issues in your patch?\n\nPaul",
    "created_at": "2011-08-18T10:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7191",
    "user": "https://github.com/zimmermann6"
}
```

Replying to [comment:16 kcrisman]:
> This should also solve #11626, I think?


right, thus #11626 can be closed as soon as this ticket is closed
(or maybe right now?).

Douglas, can you implement the work issues in your patch?

Paul



---

archive/issue_comments_007192.json:
```json
{
    "body": "So, to review:\n* Burcin and I want a small formatting change so the doc would build correctly.\n* Burcin wants the speed to be fixed using the thing referenced at #11143, using the patch at #11513.\n* I want a doctest that checks big numbers will work (as in [comment:15 comment 15]).\n* Paul and I want a doctest for #11626, to verify it is fixed.\n* Burcin *recommends* calling mpmath without prec as at #11143.\n\nThis would make this depend on #11513.  I'm still a little skeptical on this; will we really not get any wrong answers with that?",
    "created_at": "2011-08-18T14:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7192",
    "user": "https://github.com/kcrisman"
}
```

So, to review:
* Burcin and I want a small formatting change so the doc would build correctly.
* Burcin wants the speed to be fixed using the thing referenced at #11143, using the patch at #11513.
* I want a doctest that checks big numbers will work (as in [comment:15 comment 15]).
* Paul and I want a doctest for #11626, to verify it is fixed.
* Burcin *recommends* calling mpmath without prec as at #11143.

This would make this depend on #11513.  I'm still a little skeptical on this; will we really not get any wrong answers with that?



---

archive/issue_comments_007193.json:
```json
{
    "body": "Replying to [comment:18 kcrisman]:\n> So, to review:\n> * I want a doctest that checks big numbers will work (as in [comment:15 comment 15]).\n> * Paul and I want a doctest for #11626, to verify it is fixed.\n\n\nthe current patch already contains examples with prec=100, both for real and complex numbers,\nand thus is fine to me.\n\nPaul",
    "created_at": "2011-08-18T15:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7193",
    "user": "https://github.com/zimmermann6"
}
```

Replying to [comment:18 kcrisman]:
> So, to review:
> * I want a doctest that checks big numbers will work (as in [comment:15 comment 15]).
> * Paul and I want a doctest for #11626, to verify it is fixed.


the current patch already contains examples with prec=100, both for real and complex numbers,
and thus is fine to me.

Paul



---

archive/issue_comments_007194.json:
```json
{
    "body": "Replying to [comment:19 zimmerma]:\n> Replying to [comment:18 kcrisman]:\n> > So, to review:\n> > * I want a doctest that checks big numbers will work (as in [comment:15 comment 15]).\n> > * Paul and I want a doctest for #11626, to verify it is fixed.\n\n> \n> the current patch already contains examples with prec=100, both for real and complex numbers,\n> and thus is fine to me.\n\n\nOkay.  I was thinking that because was not yet a test with the syntax `n(erf(2),100)`, which some users might find nicer than the other one, but of course they mean the same thing.  I'll leave that up to Doug, then.",
    "created_at": "2011-08-18T15:31:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7194",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:19 zimmerma]:
> Replying to [comment:18 kcrisman]:
> > So, to review:
> > * I want a doctest that checks big numbers will work (as in [comment:15 comment 15]).
> > * Paul and I want a doctest for #11626, to verify it is fixed.

> 
> the current patch already contains examples with prec=100, both for real and complex numbers,
> and thus is fine to me.


Okay.  I was thinking that because was not yet a test with the syntax `n(erf(2),100)`, which some users might find nicer than the other one, but of course they mean the same thing.  I'll leave that up to Doug, then.



---

archive/issue_comments_007195.json:
```json
{
    "body": "So:\n* Burcin and I want a small formatting change so the doc would build correctly.\n* Burcin wants the speed to be fixed using the thing referenced at #11143, using the patch at #11513.\n* I want a doctest that checks big numbers like `erf(45000).n()` will work (as in [comment:15 comment 15]).\n* I want a doctest for `erf(sqrt(2))` so #9044 can stay closed.\n* Burcin *recommends* calling mpmath without prec as at #11143.",
    "created_at": "2011-08-19T14:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7195",
    "user": "https://github.com/kcrisman"
}
```

So:
* Burcin and I want a small formatting change so the doc would build correctly.
* Burcin wants the speed to be fixed using the thing referenced at #11143, using the patch at #11513.
* I want a doctest that checks big numbers like `erf(45000).n()` will work (as in [comment:15 comment 15]).
* I want a doctest for `erf(sqrt(2))` so #9044 can stay closed.
* Burcin *recommends* calling mpmath without prec as at #11143.



---

archive/issue_comments_007196.json:
```json
{
    "body": "See also #11948.",
    "created_at": "2011-10-25T01:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7196",
    "user": "https://github.com/kcrisman"
}
```

See also #11948.



---

archive/issue_comments_007197.json:
```json
{
    "body": "I ran into this problem (https://groups.google.com/d/topic/sage-support/SNw_6mLFnrg/discussion) and this patch fixes it. This patch seems to have some issues with a speed regression and some doctests, but it does fix a problem that I have.",
    "created_at": "2011-10-25T02:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7197",
    "user": "https://github.com/dandrake"
}
```

I ran into this problem (https://groups.google.com/d/topic/sage-support/SNw_6mLFnrg/discussion) and this patch fixes it. This patch seems to have some issues with a speed regression and some doctests, but it does fix a problem that I have.



---

archive/issue_comments_007198.json:
```json
{
    "body": "</lurk>\n\nOkay, I'm back.  Is it worth finishing this patch or should we follow the #11948 path instead?",
    "created_at": "2011-10-29T00:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7198",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

</lurk>

Okay, I'm back.  Is it worth finishing this patch or should we follow the #11948 path instead?



---

archive/issue_comments_007199.json:
```json
{
    "body": "> Okay, I'm back.  Is it worth finishing this patch or should we follow the #11948 path instead?\n\n\nGo for it!",
    "created_at": "2011-10-29T02:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7199",
    "user": "https://github.com/kcrisman"
}
```

> Okay, I'm back.  Is it worth finishing this patch or should we follow the #11948 path instead?


Go for it!



---

archive/issue_comments_007200.json:
```json
{
    "body": "Now I remember why I found this so frustrating.  I rewrote the patch following -- plagiarizing is more like it! -- the pattern used in #11143, but the speed issue hasn't gone away.  \n\n```\n\n# 4.7.1, OS X 10.6.8\nsage: timeit('erf(0.1)',number=1000)\n1000 loops, best of 3: 82.9 \u00b5s per loop\nsage: timeit('erf(10.0)',number=1000)\n1000 loops, best of 3: 72.8 \u00b5s per loop\nsage: timeit('erf(100.0)',number=1000)\n1000 loops, best of 3: 73.5 \u00b5s per loop\n\n# 4.7.2 before patch\nsage: timeit('erf(0.1)',number=1000)\n1000 loops, best of 3: 69.4 \u00b5s per loop\nsage: timeit('erf(10.0)',number=1000)\n1000 loops, best of 3: 62.6 \u00b5s per loop\nsage: timeit('erf(100.0)',number=1000)\n1000 loops, best of 3: 62 \u00b5s per loop\n\n# 4.7.2 after patch\nsage: timeit('erf(0.1)',number=1000)\n1000 loops, best of 3: 137 \u00b5s per loop\nsage: timeit('erf(10.0)',number=1000)\n1000 loops, best of 3: 116 \u00b5s per loop\nsage: timeit('erf(100.0)',number=1000)\n1000 loops, best of 3: 116 \u00b5s per loop\n\nsage: import mpmath\nsage: timeit('mpmath.erf(0.1)')\n625 loops, best of 3: 95 \u00b5s per loop\nsage: timeit('mpmath.erf(10.0)')\n625 loops, best of 3: 75.4 \u00b5s per loop\nsage: timeit('mpmath.erf(100.0)')\n625 loops, best of 3: 76.2 \u00b5s per loop\n\n```\n\nThat is, there's about a factor of two penalty in speed for the standard case, but it's not because the underlying mpmath code is slow:\n\n```\nsage: timeit('mpmath.erf(0.1r)')\n625 loops, best of 3: 27.7 \u00b5s per loop\nsage: timeit('mpmath.erf(10.0r)')\n625 loops, best of 3: 9.85 \u00b5s per loop\nsage: timeit('mpmath.erf(100.0r)')\n625 loops, best of 3: 9.95 \u00b5s per loop\n```\n\nIn fact, mpmath isn't that much slower than MPFR:\n\n```\nsage: z = RR(2); timeit('z.erf()')\n625 loops, best of 3: 20 \u00b5s per loop\nsage: z = 2.0r; timeit('mpmath.erf(z)')\n625 loops, best of 3: 57.9 \u00b5s per loop\nsage: timeit('erf(2.0)') # new code\n625 loops, best of 3: 181 \u00b5s per loop\n```\n\nSo not much of the total time is spent actually doing any calculations: it's all overhead.  :-(  This affects #11143 as well:\n\n```\nsage: timeit('exp_integral_e1(2.0)')\n625 loops, best of 3: 165 \u00b5s per loop\nsage: z = exp_integral_e1(2); timeit('z.n()')\n625 loops, best of 3: 143 \u00b5s per loop\nsage: timeit('exponential_integral_1(2.0)')\n625 loops, best of 3: 44.7 \u00b5s per loop\nsage: timeit('mpmath.e1(2.0)')\n625 loops, best of 3: 123 \u00b5s per loop\nsage: timeit('mpmath.e1(2.0r)')\n625 loops, best of 3: 51 \u00b5s per loop\n\n```\n\n\nTo wrap up:\n\n(1) Both this patch and #11143 suffer a significant slowdown relative to PARI, and have major overheads relative to calling mpmath.  Some of that's unavoidable given the symbolic path, but ISTM we should be able to do better.  Ideally there would be a reasonably efficient general special function implementation pattern, along the lines of what Benjamin used, that intermittent developers like me could be pointed to as a reference.\n\n(2) In the case of erf and erfc, mpfr offers a very fast evaluation for real numbers, fast enough that it might be worth using as the default in those cases (although Python-level branching is slow in my experience, maybe slow enough to wash away the benefits).  Once we settle on an approach for erf I'll do the same for erfc.\n\n(3) Should I move this out of other.py to special.py, where the complementary error_fcn function lives now?  It would seem a more natural location for it.  We also have some unfortunate naming (erf and error_fcn) it might be worth addressing.\n\nI don't have numbers for #11948 -- too many dependencies -- but it's probably considerably faster than this approach.  I figure it's probably worth getting the #11143 -style mpmath wrapper to be faster, though, even if we went #11948 instead for erf/erfc.\n\n[There are a few doctest failures: \"devel/sage/doc/en/bordeaux_2008/l_series.rst\", which I think is unrelated; a timeout in devel/sage/sage/modules/free_module.py, again probably unrelated.]",
    "created_at": "2011-10-29T20:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7200",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Now I remember why I found this so frustrating.  I rewrote the patch following -- plagiarizing is more like it! -- the pattern used in #11143, but the speed issue hasn't gone away.  

```

# 4.7.1, OS X 10.6.8
sage: timeit('erf(0.1)',number=1000)
1000 loops, best of 3: 82.9 µs per loop
sage: timeit('erf(10.0)',number=1000)
1000 loops, best of 3: 72.8 µs per loop
sage: timeit('erf(100.0)',number=1000)
1000 loops, best of 3: 73.5 µs per loop

# 4.7.2 before patch
sage: timeit('erf(0.1)',number=1000)
1000 loops, best of 3: 69.4 µs per loop
sage: timeit('erf(10.0)',number=1000)
1000 loops, best of 3: 62.6 µs per loop
sage: timeit('erf(100.0)',number=1000)
1000 loops, best of 3: 62 µs per loop

# 4.7.2 after patch
sage: timeit('erf(0.1)',number=1000)
1000 loops, best of 3: 137 µs per loop
sage: timeit('erf(10.0)',number=1000)
1000 loops, best of 3: 116 µs per loop
sage: timeit('erf(100.0)',number=1000)
1000 loops, best of 3: 116 µs per loop

sage: import mpmath
sage: timeit('mpmath.erf(0.1)')
625 loops, best of 3: 95 µs per loop
sage: timeit('mpmath.erf(10.0)')
625 loops, best of 3: 75.4 µs per loop
sage: timeit('mpmath.erf(100.0)')
625 loops, best of 3: 76.2 µs per loop

```

That is, there's about a factor of two penalty in speed for the standard case, but it's not because the underlying mpmath code is slow:

```
sage: timeit('mpmath.erf(0.1r)')
625 loops, best of 3: 27.7 µs per loop
sage: timeit('mpmath.erf(10.0r)')
625 loops, best of 3: 9.85 µs per loop
sage: timeit('mpmath.erf(100.0r)')
625 loops, best of 3: 9.95 µs per loop
```

In fact, mpmath isn't that much slower than MPFR:

```
sage: z = RR(2); timeit('z.erf()')
625 loops, best of 3: 20 µs per loop
sage: z = 2.0r; timeit('mpmath.erf(z)')
625 loops, best of 3: 57.9 µs per loop
sage: timeit('erf(2.0)') # new code
625 loops, best of 3: 181 µs per loop
```

So not much of the total time is spent actually doing any calculations: it's all overhead.  :-(  This affects #11143 as well:

```
sage: timeit('exp_integral_e1(2.0)')
625 loops, best of 3: 165 µs per loop
sage: z = exp_integral_e1(2); timeit('z.n()')
625 loops, best of 3: 143 µs per loop
sage: timeit('exponential_integral_1(2.0)')
625 loops, best of 3: 44.7 µs per loop
sage: timeit('mpmath.e1(2.0)')
625 loops, best of 3: 123 µs per loop
sage: timeit('mpmath.e1(2.0r)')
625 loops, best of 3: 51 µs per loop

```


To wrap up:

(1) Both this patch and #11143 suffer a significant slowdown relative to PARI, and have major overheads relative to calling mpmath.  Some of that's unavoidable given the symbolic path, but ISTM we should be able to do better.  Ideally there would be a reasonably efficient general special function implementation pattern, along the lines of what Benjamin used, that intermittent developers like me could be pointed to as a reference.

(2) In the case of erf and erfc, mpfr offers a very fast evaluation for real numbers, fast enough that it might be worth using as the default in those cases (although Python-level branching is slow in my experience, maybe slow enough to wash away the benefits).  Once we settle on an approach for erf I'll do the same for erfc.

(3) Should I move this out of other.py to special.py, where the complementary error_fcn function lives now?  It would seem a more natural location for it.  We also have some unfortunate naming (erf and error_fcn) it might be worth addressing.

I don't have numbers for #11948 -- too many dependencies -- but it's probably considerably faster than this approach.  I figure it's probably worth getting the #11143 -style mpmath wrapper to be faster, though, even if we went #11948 instead for erf/erfc.

[There are a few doctest failures: "devel/sage/doc/en/bordeaux_2008/l_series.rst", which I think is unrelated; a timeout in devel/sage/sage/modules/free_module.py, again probably unrelated.]



---

archive/issue_comments_007201.json:
```json
{
    "body": "11143-style mpmath erf",
    "created_at": "2011-10-29T20:40:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7201",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

11143-style mpmath erf



---

archive/issue_comments_007202.json:
```json
{
    "body": "Attachment [trac_1173_complex_erf_v2.patch](tarball://root/attachments/some-uuid/ticket1173/trac_1173_complex_erf_v2.patch) by @burcin created at 2011-10-30 11:07:58\n\nReplying to [comment:26 dsm]:\n<snip>\n> To wrap up:\n> \n> (1) Both this patch and #11143 suffer a significant slowdown relative to PARI, and have major overheads relative to calling mpmath.  Some of that's unavoidable given the symbolic path, but ISTM we should be able to do better.  Ideally there would be a reasonably efficient general special function implementation pattern, along the lines of what Benjamin used, that intermittent developers like me could be pointed to as a reference.\n\n\nI agree that we should do better. Note that the pattern you request is being developed in #11143  and here. Even though pynac based symbolics was merged in Sage quite a while ago, it hasn't been used properly yet.\n\nThe code path to call symbolic functions is rather convoluted. This is inevitable since symbolic functions have to play well with many different subsystems, such as fast float, numpy, etc. But it should still be possible to reduce the overhead.\n\nFor `BuiltinFunction`s the code path for evaluation goes through `Function.__call__()` in `sage/symbolic/function.pyx`, then into pynac, then to the python method you define for `_eval_()`, if numeric evaluation is needed to `_evalf_()` later. Here, between the python and C++ code, conversion functions are called to wrap pynac objects in Expression instances or to remove these wrappers.\n\nI believe most of the overhead comes from the `__call__()` method, then having to decide if the arguments are numeric in `_eval_()`, and checking if an argument is zero (#11513).\n\n> (2) In the case of erf and erfc, mpfr offers a very fast evaluation for real numbers, fast enough that it might be worth using as the default in those cases (although Python-level branching is slow in my experience, maybe slow enough to wash away the benefits).  Once we settle on an approach for erf I'll do the same for erfc.\n\n\nMPFR should be the default numeric evaluation method if it is available. In general, it's better to let the types choose the numeric evaluation method. Most special functions in Sage first see if an object implements a method with the same name first and calls that. For instance `erf()` should call `.erf()` for element of `RR`.\n\nI see that for subclasses of `GinacFunction` the `__call__()` method does this automatically. This is not used for other `BuiltinFunction`s though. It might make sense to move this method to `BuiltinFunction`. This would speed up most of the timings for real numbers above.\n\nUnfortunately, floats would still go through the long path. Since these are used quite often in plotting, perhaps we should add a special case in `__call__()` to go directly to `_evalf_()` as well.\n\nI made this change in attachment:trac_1173-move_call.patch. Now I get:\n\n```\nsage: t = RR(2.0)\nsage: %timeit z = t.erf()\n625 loops, best of 3: 16.9 \u00b5s per loop\nsage: %timeit z = erf(t)\n625 loops, best of 3: 18.2 \u00b5s per loop\n```\n\nPerformance for `float` is still pretty bad.\n\n```\nsage: u = 2.0r\nsage: %timeit z = erf(u)\n625 loops, best of 3: 156 \u00b5s per loop\n```\n\nI didn't check if this patch breaks anything.\n\n> (3) Should I move this out of other.py to special.py, where the complementary error_fcn function lives now?  It would seem a more natural location for it.  We also have some unfortunate naming (erf and error_fcn) it might be worth addressing.\n\n\nI don't think there is a need to move this to `special.py`. That file is also overcrowded and needs serious cleanup. You could create a new file names `error_fn.py` if you think that's necessary.\n\nWhat names do other systems use for these functions? AFAIK, `erf()` and `erfc()` are pretty much standard. I wonder where `error_fcn()` came from.",
    "created_at": "2011-10-30T11:07:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7202",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_1173_complex_erf_v2.patch](tarball://root/attachments/some-uuid/ticket1173/trac_1173_complex_erf_v2.patch) by @burcin created at 2011-10-30 11:07:58

Replying to [comment:26 dsm]:
<snip>
> To wrap up:
> 
> (1) Both this patch and #11143 suffer a significant slowdown relative to PARI, and have major overheads relative to calling mpmath.  Some of that's unavoidable given the symbolic path, but ISTM we should be able to do better.  Ideally there would be a reasonably efficient general special function implementation pattern, along the lines of what Benjamin used, that intermittent developers like me could be pointed to as a reference.


I agree that we should do better. Note that the pattern you request is being developed in #11143  and here. Even though pynac based symbolics was merged in Sage quite a while ago, it hasn't been used properly yet.

The code path to call symbolic functions is rather convoluted. This is inevitable since symbolic functions have to play well with many different subsystems, such as fast float, numpy, etc. But it should still be possible to reduce the overhead.

For `BuiltinFunction`s the code path for evaluation goes through `Function.__call__()` in `sage/symbolic/function.pyx`, then into pynac, then to the python method you define for `_eval_()`, if numeric evaluation is needed to `_evalf_()` later. Here, between the python and C++ code, conversion functions are called to wrap pynac objects in Expression instances or to remove these wrappers.

I believe most of the overhead comes from the `__call__()` method, then having to decide if the arguments are numeric in `_eval_()`, and checking if an argument is zero (#11513).

> (2) In the case of erf and erfc, mpfr offers a very fast evaluation for real numbers, fast enough that it might be worth using as the default in those cases (although Python-level branching is slow in my experience, maybe slow enough to wash away the benefits).  Once we settle on an approach for erf I'll do the same for erfc.


MPFR should be the default numeric evaluation method if it is available. In general, it's better to let the types choose the numeric evaluation method. Most special functions in Sage first see if an object implements a method with the same name first and calls that. For instance `erf()` should call `.erf()` for element of `RR`.

I see that for subclasses of `GinacFunction` the `__call__()` method does this automatically. This is not used for other `BuiltinFunction`s though. It might make sense to move this method to `BuiltinFunction`. This would speed up most of the timings for real numbers above.

Unfortunately, floats would still go through the long path. Since these are used quite often in plotting, perhaps we should add a special case in `__call__()` to go directly to `_evalf_()` as well.

I made this change in attachment:trac_1173-move_call.patch. Now I get:

```
sage: t = RR(2.0)
sage: %timeit z = t.erf()
625 loops, best of 3: 16.9 µs per loop
sage: %timeit z = erf(t)
625 loops, best of 3: 18.2 µs per loop
```

Performance for `float` is still pretty bad.

```
sage: u = 2.0r
sage: %timeit z = erf(u)
625 loops, best of 3: 156 µs per loop
```

I didn't check if this patch breaks anything.

> (3) Should I move this out of other.py to special.py, where the complementary error_fcn function lives now?  It would seem a more natural location for it.  We also have some unfortunate naming (erf and error_fcn) it might be worth addressing.


I don't think there is a need to move this to `special.py`. That file is also overcrowded and needs serious cleanup. You could create a new file names `error_fn.py` if you think that's necessary.

What names do other systems use for these functions? AFAIK, `erf()` and `erfc()` are pretty much standard. I wonder where `error_fcn()` came from.



---

archive/issue_comments_007203.json:
```json
{
    "body": "Attachment [trac_1173-move_call.patch](tarball://root/attachments/some-uuid/ticket1173/trac_1173-move_call.patch) by @burcin created at 2011-10-30 11:11:04",
    "created_at": "2011-10-30T11:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7203",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_1173-move_call.patch](tarball://root/attachments/some-uuid/ticket1173/trac_1173-move_call.patch) by @burcin created at 2011-10-30 11:11:04



---

archive/issue_comments_007204.json:
```json
{
    "body": "Okay, this looks a bit better.  With trac_1173-move_call.patch, trac_11885_v2.patch, trac_11513-is_numerically_zero.patch, and trac_1173_complex_erf_v3.patch:\n\n```\nalpha3:\n\n0.100000000000000 float               121 \u00b5s per loop\n0.100000000000000 RDF                 51.6 \u00b5s per loop\n0.100000000000000 RR                  61.2 \u00b5s per loop\n0.100000000000000 RealField(100)      64.5 \u00b5s per loop\n0.100000000000000 RealField(1000)     304 \u00b5s per loop\n\nnew:\n0.100000000000000 float               49.3 \u00b5s per loop\n0.100000000000000 RDF                 773 ns per loop\n0.100000000000000 RR                  7.07 \u00b5s per loop\n0.100000000000000 RealField(100)      10.6 \u00b5s per loop\n0.100000000000000 RealField(1000)     248 \u00b5s per loop\n0.100000000000000 complex             131 \u00b5s per loop\n0.100000000000000 CDF                 185 \u00b5s per loop\n0.100000000000000 CC                  254 \u00b5s per loop\n0.100000000000000 ComplexField(100)   262 \u00b5s per loop\n0.100000000000000 ComplexField(1000)  470 \u00b5s per loop\n0.100000000000000*I complex             247 \u00b5s per loop\n0.100000000000000*I CDF                 389 \u00b5s per loop\n0.100000000000000*I CC                  405 \u00b5s per loop\n0.100000000000000*I ComplexField(100)   470 \u00b5s per loop\n0.100000000000000*I ComplexField(1000)  565 \u00b5s per loop\n\n```\n\nNow not only is there no regression, we've improved.  The speedups relative to alpha3 for reals are due to using the existing mpfr .erf()s instead of pari; float was special-cased through RDF.  As I mentioned, I don't have the new pari, and that's probably faster than mpmath.  But at least it's not killing me anymore.\n\nThere's a doctest failure in gamma_inc due to trac_1173-move_call.patch, I think-- formerly,\n\n```\nsage: parent(gamma_inc(RDF(1),3))\nComplex Field with 53 bits of precision\n```\nbut now \n\n```\nsage: parent(gamma_inc(RDF(1),3))\nReal Double Field\n```\n\nbut gamma_inc doesn't preserve types the way I'd have expected.  Anyway, I think this is a step in the right direction.",
    "created_at": "2011-10-30T21:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7204",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Okay, this looks a bit better.  With trac_1173-move_call.patch, trac_11885_v2.patch, trac_11513-is_numerically_zero.patch, and trac_1173_complex_erf_v3.patch:

```
alpha3:

0.100000000000000 float               121 µs per loop
0.100000000000000 RDF                 51.6 µs per loop
0.100000000000000 RR                  61.2 µs per loop
0.100000000000000 RealField(100)      64.5 µs per loop
0.100000000000000 RealField(1000)     304 µs per loop

new:
0.100000000000000 float               49.3 µs per loop
0.100000000000000 RDF                 773 ns per loop
0.100000000000000 RR                  7.07 µs per loop
0.100000000000000 RealField(100)      10.6 µs per loop
0.100000000000000 RealField(1000)     248 µs per loop
0.100000000000000 complex             131 µs per loop
0.100000000000000 CDF                 185 µs per loop
0.100000000000000 CC                  254 µs per loop
0.100000000000000 ComplexField(100)   262 µs per loop
0.100000000000000 ComplexField(1000)  470 µs per loop
0.100000000000000*I complex             247 µs per loop
0.100000000000000*I CDF                 389 µs per loop
0.100000000000000*I CC                  405 µs per loop
0.100000000000000*I ComplexField(100)   470 µs per loop
0.100000000000000*I ComplexField(1000)  565 µs per loop

```

Now not only is there no regression, we've improved.  The speedups relative to alpha3 for reals are due to using the existing mpfr .erf()s instead of pari; float was special-cased through RDF.  As I mentioned, I don't have the new pari, and that's probably faster than mpmath.  But at least it's not killing me anymore.

There's a doctest failure in gamma_inc due to trac_1173-move_call.patch, I think-- formerly,

```
sage: parent(gamma_inc(RDF(1),3))
Complex Field with 53 bits of precision
```
but now 

```
sage: parent(gamma_inc(RDF(1),3))
Real Double Field
```

but gamma_inc doesn't preserve types the way I'd have expected.  Anyway, I think this is a step in the right direction.



---

archive/issue_comments_007205.json:
```json
{
    "body": "Attachment [trac_1173_complex_erf_v3.patch](tarball://root/attachments/some-uuid/ticket1173/trac_1173_complex_erf_v3.patch) by dsm created at 2011-10-30 21:29:01\n\n11143-style erf, use mpfr where possible",
    "created_at": "2011-10-30T21:29:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7205",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Attachment [trac_1173_complex_erf_v3.patch](tarball://root/attachments/some-uuid/ticket1173/trac_1173_complex_erf_v3.patch) by dsm created at 2011-10-30 21:29:01

11143-style erf, use mpfr where possible



---

archive/issue_comments_007206.json:
```json
{
    "body": "Qs, as this is now official fodder for [wiki/days35.5/bugs Sage Days 35.5]:\n* What patches should be applied here?  \n* Are we ready for review?   (I.e., are all work issues taken care of?)\n* What's the status of #11513 with respect to this patch?\n\nThanks!",
    "created_at": "2011-11-22T01:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7206",
    "user": "https://github.com/kcrisman"
}
```

Qs, as this is now official fodder for [wiki/days35.5/bugs Sage Days 35.5]:
* What patches should be applied here?  
* Are we ready for review?   (I.e., are all work issues taken care of?)
* What's the status of #11513 with respect to this patch?

Thanks!



---

archive/issue_comments_007207.json:
```json
{
    "body": "Replying to [comment:29 kcrisman]:\n> Qs, as this is now official fodder for [wiki/days35.5/bugs Sage Days 35.5]:\n> * What patches should be applied here?  \n> * Are we ready for review?   (I.e., are all work issues taken care of?)\n> * What's the status of #11513 with respect to this patch?\n> \n> Thanks!\n\n\nI started to review the patch. Looks like:\n\n* The only dependency is #11513 which should be applied before [trac_1173_complex_erf_v3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/1173/trac_1173_complex_erf_v3.patch)\n* All of the work issues are taken care of\n* #11513 hasn't changed since Burcin uploaded the initial draft patch. I don't have the expertise to work on it or else I would in support of the various tickets we've got now that depend on it. \n\nThe patch trac_1173_complex_erf_v3.patch applies to 4.8.alpha3 cleanly (as does the patch at #11513) and all doctests pass. \n\nIt also looks like the \"move call\" patch should be applied to speed things up after some doctests are fixed. I'd say this should go into a new ticket because the issue is independent of evaluation of erf() at complex inputs.\n\nPositive review.",
    "created_at": "2011-12-16T01:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7207",
    "user": "https://github.com/benjaminfjones"
}
```

Replying to [comment:29 kcrisman]:
> Qs, as this is now official fodder for [wiki/days35.5/bugs Sage Days 35.5]:
> * What patches should be applied here?  
> * Are we ready for review?   (I.e., are all work issues taken care of?)
> * What's the status of #11513 with respect to this patch?
> 
> Thanks!


I started to review the patch. Looks like:

* The only dependency is #11513 which should be applied before [trac_1173_complex_erf_v3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/1173/trac_1173_complex_erf_v3.patch)
* All of the work issues are taken care of
* #11513 hasn't changed since Burcin uploaded the initial draft patch. I don't have the expertise to work on it or else I would in support of the various tickets we've got now that depend on it. 

The patch trac_1173_complex_erf_v3.patch applies to 4.8.alpha3 cleanly (as does the patch at #11513) and all doctests pass. 

It also looks like the "move call" patch should be applied to speed things up after some doctests are fixed. I'd say this should go into a new ticket because the issue is independent of evaluation of erf() at complex inputs.

Positive review.



---

archive/issue_comments_007208.json:
```json
{
    "body": "Does this also take care of #8983?",
    "created_at": "2011-12-19T17:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7208",
    "user": "https://github.com/kcrisman"
}
```

Does this also take care of #8983?



---

archive/issue_comments_007209.json:
```json
{
    "body": "Yes, both of these doctests are in DSM's patch:\n\n```\nsage: erf(0) \n0 \nsage: solve(erf(x)==0,x) \n[x == 0] \n```",
    "created_at": "2011-12-19T18:47:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7209",
    "user": "https://github.com/benjaminfjones"
}
```

Yes, both of these doctests are in DSM's patch:

```
sage: erf(0) 
0 
sage: solve(erf(x)==0,x) 
[x == 0] 
```



---

archive/issue_comments_007210.json:
```json
{
    "body": "Benjamin or Burcin, please could you add in the description which patches have to be applied, and in which order?\n\nPaul",
    "created_at": "2011-12-24T14:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7210",
    "user": "https://github.com/zimmermann6"
}
```

Benjamin or Burcin, please could you add in the description which patches have to be applied, and in which order?

Paul



---

archive/issue_comments_007211.json:
```json
{
    "body": "Benjamin, you gave a positive review in comment [comment:31] but forgot to change the status accordingly.\n\nPaul",
    "created_at": "2011-12-24T14:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7211",
    "user": "https://github.com/zimmermann6"
}
```

Benjamin, you gave a positive review in comment [comment:31] but forgot to change the status accordingly.

Paul



---

archive/issue_comments_007212.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-12-24T16:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7212",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_007213.json:
```json
{
    "body": "Done. I was waiting to see if anyone else had comments or concerns before setting the status to positive review, but looks like it's been long enough. I've done some work on #11513 in the last few days. I'll update there the next change I get.",
    "created_at": "2011-12-24T16:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7213",
    "user": "https://github.com/benjaminfjones"
}
```

Done. I was waiting to see if anyone else had comments or concerns before setting the status to positive review, but looks like it's been long enough. I've done some work on #11513 in the last few days. I'll update there the next change I get.



---

archive/issue_events_003146.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-26T09:33:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1173#event-3146"
}
```



---

archive/issue_comments_007214.json:
```json
{
    "body": "This obviously conflicts with #11948",
    "created_at": "2011-12-26T09:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7214",
    "user": "https://github.com/jdemeyer"
}
```

This obviously conflicts with #11948



---

archive/issue_events_003147.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-26T09:33:50Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1173#event-3147"
}
```



---

archive/issue_events_003148.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-26T09:33:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1173#event-3148"
}
```



---

archive/issue_comments_007215.json:
```json
{
    "body": "Fixed in #11948, so I the release manager should close this ticket as duplicate.",
    "created_at": "2012-01-08T18:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7215",
    "user": "https://github.com/vbraun"
}
```

Fixed in #11948, so I the release manager should close this ticket as duplicate.



---

archive/issue_comments_007216.json:
```json
{
    "body": "Though perhaps we should check that all doctests are still included!",
    "created_at": "2012-01-08T20:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7216",
    "user": "https://github.com/kcrisman"
}
```

Though perhaps we should check that all doctests are still included!



---

archive/issue_comments_007217.json:
```json
{
    "body": "Replying to [comment:41 kcrisman]:\n> Though perhaps we should check that all doctests are still included!\n\n\nWhich is certainly not the case.  In fact, this ticket here does more than simply implementing `erf()` for complex arguments.",
    "created_at": "2012-01-09T13:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7217",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:41 kcrisman]:
> Though perhaps we should check that all doctests are still included!


Which is certainly not the case.  In fact, this ticket here does more than simply implementing `erf()` for complex arguments.



---

archive/issue_comments_007218.json:
```json
{
    "body": "It seems to me that both PARI and mpmath should be an option via an `algorithm` keyword argument. I'm at Sage Days 35.5 working on this stuff, so one thing I could do is take the improvements in this ticket and rebase them on top of #11948 which has been merged in 4.8.alpha6. If folks agree, I guess that should be a new ticket and this one could be closed.",
    "created_at": "2012-01-09T15:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7218",
    "user": "https://github.com/benjaminfjones"
}
```

It seems to me that both PARI and mpmath should be an option via an `algorithm` keyword argument. I'm at Sage Days 35.5 working on this stuff, so one thing I could do is take the improvements in this ticket and rebase them on top of #11948 which has been merged in 4.8.alpha6. If folks agree, I guess that should be a new ticket and this one could be closed.



---

archive/issue_comments_007219.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd35.5\".",
    "created_at": "2012-01-09T15:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7219",
    "user": "https://github.com/benjaminfjones"
}
```

Changing keywords from "" to "sd35.5".



---

archive/issue_comments_007220.json:
```json
{
    "body": "Sounds good, as long as you keep any \"good stuff\" from this ticket.",
    "created_at": "2012-01-09T16:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7220",
    "user": "https://github.com/kcrisman"
}
```

Sounds good, as long as you keep any "good stuff" from this ticket.



---

archive/issue_comments_007221.json:
```json
{
    "body": "Hi Benjamin,\n\nnote that 4.8.rc1 is already out, should be newer than 4.8.alpha6.\n\nPaul (at SD 35.5 too, but remotely)",
    "created_at": "2012-01-09T16:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7221",
    "user": "https://github.com/zimmermann6"
}
```

Hi Benjamin,

note that 4.8.rc1 is already out, should be newer than 4.8.alpha6.

Paul (at SD 35.5 too, but remotely)



---

archive/issue_comments_007222.json:
```json
{
    "body": "Hi Paul, are you on IRC? We're using the #sagemath-days channel. It looks like the 4.8.rc1 is still under construction according to the README. I'm looking in http://sage.math.washington.edu/home/release/sage-4.8.rc1/",
    "created_at": "2012-01-09T16:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7222",
    "user": "https://github.com/benjaminfjones"
}
```

Hi Paul, are you on IRC? We're using the #sagemath-days channel. It looks like the 4.8.rc1 is still under construction according to the README. I'm looking in http://sage.math.washington.edu/home/release/sage-4.8.rc1/



---

archive/issue_comments_007223.json:
```json
{
    "body": "no I'm not on IRC. Ok, then I'll use 4.8.alpha6 instead.\n\nPaul",
    "created_at": "2012-01-09T16:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7223",
    "user": "https://github.com/zimmermann6"
}
```

no I'm not on IRC. Ok, then I'll use 4.8.alpha6 instead.

Paul



---

archive/issue_comments_007224.json:
```json
{
    "body": "Replying to [comment:45 zimmerma]:\n> Hi Benjamin,\n> \n> note that 4.8.rc1 is already out, should be newer than 4.8.alpha6.\n\n\nIt certainly isn't out yet (and maybe it will never even exist if rc0 solves all our problems).  The easiest way to find out the latest development release is [http://www.sagemath.org/download-latest.html](http://www.sagemath.org/download-latest.html), accessible as www.sagemath.org -> Download -> Development Release.\nAlternatively, look at the sage-release announcements.",
    "created_at": "2012-01-09T20:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7224",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:45 zimmerma]:
> Hi Benjamin,
> 
> note that 4.8.rc1 is already out, should be newer than 4.8.alpha6.


It certainly isn't out yet (and maybe it will never even exist if rc0 solves all our problems).  The easiest way to find out the latest development release is [http://www.sagemath.org/download-latest.html](http://www.sagemath.org/download-latest.html), accessible as www.sagemath.org -> Download -> Development Release.
Alternatively, look at the sage-release announcements.



---

archive/issue_comments_007225.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-01-09T21:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7225",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_007226.json:
```json
{
    "body": "OK, the feeling here at SD35.5 is to hijack this ticket (change the ticket description) to rebase the work done by DSM on top of Sage-4.8.alpha6 (rather than making a new ticket) so the work and documentation improvements here are preserved and compatible with #11948. Please pipe up if you're following this ticket and have an opinion.",
    "created_at": "2012-01-09T21:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7226",
    "user": "https://github.com/benjaminfjones"
}
```

OK, the feeling here at SD35.5 is to hijack this ticket (change the ticket description) to rebase the work done by DSM on top of Sage-4.8.alpha6 (rather than making a new ticket) so the work and documentation improvements here are preserved and compatible with #11948. Please pipe up if you're following this ticket and have an opinion.



---

archive/issue_comments_007227.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2012-01-09T21:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7227",
    "user": "https://github.com/jdemeyer"
}
```

Fine by me.



---

archive/issue_events_003149.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-01-09T21:10:21Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1173#event-3149"
}
```



---

archive/issue_events_003150.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-01-09T21:10:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1173#event-3150"
}
```



---

archive/issue_comments_007228.json:
```json
{
    "body": "See comments at #11948 for why we probably want to do this or #13050 as soon as possible.",
    "created_at": "2012-07-02T14:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7228",
    "user": "https://github.com/kcrisman"
}
```

See comments at #11948 for why we probably want to do this or #13050 as soon as possible.



---

archive/issue_comments_007229.json:
```json
{
    "body": "With respect to the move call patch, see also #13933.",
    "created_at": "2013-06-12T20:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7229",
    "user": "https://github.com/kcrisman"
}
```

With respect to the move call patch, see also #13933.



---

archive/issue_comments_007230.json:
```json
{
    "body": "Apply trac_1173_complex_erf_v3.patch",
    "created_at": "2013-06-12T20:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7230",
    "user": "https://github.com/kcrisman"
}
```

Apply trac_1173_complex_erf_v3.patch



---

archive/issue_comments_007231.json:
```json
{
    "body": "Pretty much everything here was done at #11948 or #13001.  So let's close this (just a little I moved to #13050.",
    "created_at": "2013-06-19T06:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7231",
    "user": "https://github.com/kcrisman"
}
```

Pretty much everything here was done at #11948 or #13001.  So let's close this (just a little I moved to #13050.



---

archive/issue_comments_007232.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-06-19T06:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7232",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_events_003151.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2013-06-19T06:20:18Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1173#event-3151"
}
```



---

archive/issue_events_003152.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2013-06-19T06:20:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1173#event-3152"
}
```



---

archive/issue_comments_007233.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-06-19T12:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1173#issuecomment-7233",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_003153.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-06-19T12:16:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1173",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1173#event-3153"
}
```
