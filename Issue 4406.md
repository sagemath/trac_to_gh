# Issue 4406: make polynomail truncation cpdef method

archive/issues_004406.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @craigcitro\n\nCurrently we have _c variants, some of which call one direction, and some which call the other. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4406\n\n",
    "created_at": "2008-10-30T20:07:21Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "make polynomail truncation cpdef method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4406",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd

CC:  @craigcitro

Currently we have _c variants, some of which call one direction, and some which call the other. 

Issue created by migration from https://trac.sagemath.org/ticket/4406





---

archive/issue_comments_032334.json:
```json
{
    "body": "Attachment [4406-cpdef-truncate.patch](tarball://root/attachments/some-uuid/ticket4406/4406-cpdef-truncate.patch) by @robertwb created at 2008-10-30 21:21:40\n\nThis wasn't as invasive as I had expected. Apply on top of fix at #2462.",
    "created_at": "2008-10-30T21:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4406#issuecomment-32334",
    "user": "https://github.com/robertwb"
}
```

Attachment [4406-cpdef-truncate.patch](tarball://root/attachments/some-uuid/ticket4406/4406-cpdef-truncate.patch) by @robertwb created at 2008-10-30 21:21:40

This wasn't as invasive as I had expected. Apply on top of fix at #2462.



---

archive/issue_comments_032335.json:
```json
{
    "body": "Patch looks good to me, but I will wait on a review #2462 before testing this. Also fixed a spelling mistake in the subject.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T00:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4406#issuecomment-32335",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me, but I will wait on a review #2462 before testing this. Also fixed a spelling mistake in the subject.

Cheers,

Michael



---

archive/issue_comments_032336.json:
```json
{
    "body": "This patch causes the following doctest failures:\n\n```\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/rings/power_series_ring_element.pyx # 2 doctests failed\n\tsage -t -long devel/sage/sage/rings/power_series_poly.pyx # 2 doctests failed\n\tsage -t -long devel/sage/sage/modular/modform/theta.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/modular/modform/j_invariant.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/crypto/lfsr.py # 5 doctests failed\n```\n\nThe error seems to always be\n\n```\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_11[3]>\", line 8, in <module>\n        g = Rx(g, len(g))\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/rings/power_series_ring.py\", line 326, in __call__\n        return self.__power_series_class(self, f, prec, check=check)\n      File \"power_series_poly.pyx\", line 47, in sage.rings.power_series_poly.PowerSeries_poly.__init__ (sage/rings/power_series_poly.c:2073)\n      File \"polynomial_element.pyx\", line 3928, in sage.rings.polynomial.polynomial_element.Polynomial.truncate (sage/rings/polynomial/polynomial_element.c:25338)\n      File \"polynomial_gf2x.pyx\", line 43, in sage.rings.polynomial.polynomial_gf2x.Polynomial_GF2X.__getitem__ (sage/rings/polynomial/polynomial_gf2x.cpp:6652)\n    TypeError: an integer is required\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T02:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4406#issuecomment-32336",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch causes the following doctest failures:

```
	sage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 1 doctests failed
	sage -t -long devel/sage/sage/rings/power_series_ring_element.pyx # 2 doctests failed
	sage -t -long devel/sage/sage/rings/power_series_poly.pyx # 2 doctests failed
	sage -t -long devel/sage/sage/modular/modform/theta.py # 1 doctests failed
	sage -t -long devel/sage/sage/modular/modform/j_invariant.py # 1 doctests failed
	sage -t -long devel/sage/sage/crypto/lfsr.py # 5 doctests failed
```

The error seems to always be

```
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_11[3]>", line 8, in <module>
        g = Rx(g, len(g))
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/rings/power_series_ring.py", line 326, in __call__
        return self.__power_series_class(self, f, prec, check=check)
      File "power_series_poly.pyx", line 47, in sage.rings.power_series_poly.PowerSeries_poly.__init__ (sage/rings/power_series_poly.c:2073)
      File "polynomial_element.pyx", line 3928, in sage.rings.polynomial.polynomial_element.Polynomial.truncate (sage/rings/polynomial/polynomial_element.c:25338)
      File "polynomial_gf2x.pyx", line 43, in sage.rings.polynomial.polynomial_gf2x.Polynomial_GF2X.__getitem__ (sage/rings/polynomial/polynomial_gf2x.cpp:6652)
    TypeError: an integer is required
```


Cheers,

Michael



---

archive/issue_comments_032337.json:
```json
{
    "body": "Are you sure this is with my patch? I just tried these and they work fine in my branch. Or maybe it's some incompatibility with your alpha.",
    "created_at": "2008-10-31T18:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4406#issuecomment-32337",
    "user": "https://github.com/robertwb"
}
```

Are you sure this is with my patch? I just tried these and they work fine in my branch. Or maybe it's some incompatibility with your alpha.



---

archive/issue_comments_032338.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> Are you sure this is with my patch? I just tried these and they work fine in my branch. Or maybe it's some incompatibility with your alpha. \n\nYes, I tried with this and the patch at #2462 and initially suspected #2462, but it turns out to be this patch. Reverting this patch only fixed the issue for me. 3.2.alpha2 is coming today, so there should be a binary for sage.math shortly.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T18:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4406#issuecomment-32338",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 robertwb]:
> Are you sure this is with my patch? I just tried these and they work fine in my branch. Or maybe it's some incompatibility with your alpha. 

Yes, I tried with this and the patch at #2462 and initially suspected #2462, but it turns out to be this patch. Reverting this patch only fixed the issue for me. 3.2.alpha2 is coming today, so there should be a binary for sage.math shortly.

Cheers,

Michael



---

archive/issue_comments_032339.json:
```json
{
    "body": "OK, I'll look at it there.",
    "created_at": "2008-10-31T18:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4406#issuecomment-32339",
    "user": "https://github.com/robertwb"
}
```

OK, I'll look at it there.



---

archive/issue_comments_032340.json:
```json
{
    "body": "I tried fixing this on sage.math, but I'm having issues with the unpacked tar. I copied over sage-3.2.alpha2-sage.math-only-x86_64-Linux and extracted it, but when I run ./sage I get\n\n\n```\nsage: sage.all.__file__\n '/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/all.pyc'\n```\n\n\nand I can't figure out how test my changes. However, I'm pretty sure the error is because line 467 of sage/rings/polynomial/polynomial_template.pxi is still def (rather than cpdef). I'm attaching a patch that should fix the problem.",
    "created_at": "2008-11-01T23:13:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4406#issuecomment-32340",
    "user": "https://github.com/robertwb"
}
```

I tried fixing this on sage.math, but I'm having issues with the unpacked tar. I copied over sage-3.2.alpha2-sage.math-only-x86_64-Linux and extracted it, but when I run ./sage I get


```
sage: sage.all.__file__
 '/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/all.pyc'
```


and I can't figure out how test my changes. However, I'm pretty sure the error is because line 467 of sage/rings/polynomial/polynomial_template.pxi is still def (rather than cpdef). I'm attaching a patch that should fix the problem.



---

archive/issue_comments_032341.json:
```json
{
    "body": "Attachment [4406-truncate-fix.patch](tarball://root/attachments/some-uuid/ticket4406/4406-truncate-fix.patch) by @robertwb created at 2008-11-01 23:14:37",
    "created_at": "2008-11-01T23:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4406#issuecomment-32341",
    "user": "https://github.com/robertwb"
}
```

Attachment [4406-truncate-fix.patch](tarball://root/attachments/some-uuid/ticket4406/4406-truncate-fix.patch) by @robertwb created at 2008-11-01 23:14:37



---

archive/issue_comments_032342.json:
```json
{
    "body": "I will test the patch and see if that fixes it. More than likely you are getting bitten by #4317, so following the instructions there you should be able to fix the problem.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-01T23:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4406#issuecomment-32342",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will test the patch and see if that fixes it. More than likely you are getting bitten by #4317, so following the instructions there you should be able to fix the problem.

Cheers,

Michael



---

archive/issue_comments_032343.json:
```json
{
    "body": "The second patch Robert posted resolves the issue I found. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-02T00:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4406#issuecomment-32343",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The second patch Robert posted resolves the issue I found. Positive review.

Cheers,

Michael



---

archive/issue_comments_032344.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-02T00:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4406#issuecomment-32344",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha3



---

archive/issue_comments_032345.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-02T00:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4406#issuecomment-32345",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004651.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-02T00:47:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4406",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4406#event-4651"
}
```
