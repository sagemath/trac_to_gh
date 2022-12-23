# Issue 1963: unramified and eisenstein extensions

archive/issues_001963.json:
```json
{
    "body": "Assignee: roed\n\nKeywords: p-adics\n\nAdds unramified and eisenstein extensions of Qp and Zp.  Adds printing features for p-adics, improves construction of p-adic elements, fixes some bugs and memleaks.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1963\n\n",
    "created_at": "2008-01-28T22:49:59Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "unramified and eisenstein extensions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1963",
    "user": "roed"
}
```
Assignee: roed

Keywords: p-adics

Adds unramified and eisenstein extensions of Qp and Zp.  Adds printing features for p-adics, improves construction of p-adic elements, fixes some bugs and memleaks.

Issue created by migration from https://trac.sagemath.org/ticket/1963





---

archive/issue_comments_012677.json:
```json
{
    "body": "Bundled against 2.10",
    "created_at": "2008-01-28T22:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12677",
    "user": "roed"
}
```

Bundled against 2.10



---

archive/issue_comments_012678.json:
```json
{
    "body": "Attachment\n\nI got the following merge conflict against 2.10.1.rc2:\n\n```\n<<<<<<< /scratch/mabshoff/release-cycle/sage-2.10.1.rc3/devel/sage-main/sage/schemes/elliptic_curves/padics.py.orig.2461327829\n    ALGORITHM:\n        Proposition 9 of ``Efficient Computation of p-adic Heights'' (David Harvey,\n        to appear in LMS JCM).\n\n        Complexity is soft-$O(\\log L \\log m + \\log^2 m)$.\n    Complexity is soft $O(\\log R \\log^2 m)$.\n=======\n    Complexity is soft $O(\\log R \\log m)$.\n>>>>>>> /tmp/padics.py~other.K30f_Q\n```\n\nBut I also have a compilation failure:\n\n```\n/usr/include/features.h:150:1: warning: this is the location of the previous definition\nsrc/ntl_wrap.cpp: In function \u2018void ZZ_pX_InvMod_newton_unram(NTL::ZZ_pX&, const NTL::ZZ_pX&, const NTL::ZZ_pXModulus&, const NTL::ZZ_pContext&, const NTL::ZZ_pContext&)\u2019:\nsrc/ntl_wrap.cpp:1136: error: reference to \u2018negate\u2019 is ambiguous\n```\n\nI will poke around a little more and update this if I find anything useful.\n||||||| /tmp/padics.py~base.ns4Mgb\nCheers,\n\nMichael",
    "created_at": "2008-01-28T23:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12678",
    "user": "mabshoff"
}
```

Attachment

I got the following merge conflict against 2.10.1.rc2:

```
<<<<<<< /scratch/mabshoff/release-cycle/sage-2.10.1.rc3/devel/sage-main/sage/schemes/elliptic_curves/padics.py.orig.2461327829
    ALGORITHM:
        Proposition 9 of ``Efficient Computation of p-adic Heights'' (David Harvey,
        to appear in LMS JCM).

        Complexity is soft-$O(\log L \log m + \log^2 m)$.
    Complexity is soft $O(\log R \log^2 m)$.
=======
    Complexity is soft $O(\log R \log m)$.
>>>>>>> /tmp/padics.py~other.K30f_Q
```

But I also have a compilation failure:

```
/usr/include/features.h:150:1: warning: this is the location of the previous definition
src/ntl_wrap.cpp: In function ‘void ZZ_pX_InvMod_newton_unram(NTL::ZZ_pX&, const NTL::ZZ_pX&, const NTL::ZZ_pXModulus&, const NTL::ZZ_pContext&, const NTL::ZZ_pContext&)’:
src/ntl_wrap.cpp:1136: error: reference to ‘negate’ is ambiguous
```

I will poke around a little more and update this if I find anything useful.
||||||| /tmp/padics.py~base.ns4Mgb
Cheers,

Michael



---

archive/issue_comments_012679.json:
```json
{
    "body": "The compilation issue is easy to fix: add `NTL::` before negate in lines 1136 and 1163. Patch is comping up shortly.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-28T23:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12679",
    "user": "mabshoff"
}
```

The compilation issue is easy to fix: add `NTL::` before negate in lines 1136 and 1163. Patch is comping up shortly.

Cheers,

Michael



---

archive/issue_comments_012680.json:
```json
{
    "body": "Attachment\n\nFix the compilation issue with negate with gcc 4.1 (and others?)",
    "created_at": "2008-01-28T23:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12680",
    "user": "mabshoff"
}
```

Attachment

Fix the compilation issue with negate with gcc 4.1 (and others?)



---

archive/issue_comments_012681.json:
```json
{
    "body": "I see doctest failures in \n\n```\n        sage -t  devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx\n        sage -t  devel/sage-main/sage/rings/padics/padic_generic.py\n        sage -t  devel/sage-main/sage/rings/padics/padic_generic_element.pyx\n        sage -t  devel/sage-main/sage/rings/padics/pow_computer_ext.pyx\n        sage -t  devel/sage-main/sage/rings/padics/tests.py\n        sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_CA_element.pyx\n        sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_CR_element.pyx\n        sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_FM_element.pyx\n        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx\n        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py\n        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_padic_field.py\n        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_point.py\n        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py\n        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_tate_curve.py\n        sage -t  devel/sage-main/sage/schemes/elliptic_curves/padic_lseries.py\n        sage -t  devel/sage-main/sage/schemes/elliptic_curves/padics.py\n        sage -t  devel/sage-main/sage/schemes/elliptic_curves/sha.py\n        sage -t  devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-29T01:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12681",
    "user": "mabshoff"
}
```

I see doctest failures in 

```
        sage -t  devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx
        sage -t  devel/sage-main/sage/rings/padics/padic_generic.py
        sage -t  devel/sage-main/sage/rings/padics/padic_generic_element.pyx
        sage -t  devel/sage-main/sage/rings/padics/pow_computer_ext.pyx
        sage -t  devel/sage-main/sage/rings/padics/tests.py
        sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_CA_element.pyx
        sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_CR_element.pyx
        sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_FM_element.pyx
        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_padic_field.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_point.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_tate_curve.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/padic_lseries.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/padics.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/sha.py
        sage -t  devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py
```


Cheers,

Michael



---

archive/issue_comments_012682.json:
```json
{
    "body": "Bundle vs 2.10.1 at http://sage.math.washington.edu/home/roed/giant_padics_vs_2_10_1.hg",
    "created_at": "2008-02-06T04:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12682",
    "user": "roed"
}
```

Bundle vs 2.10.1 at http://sage.math.washington.edu/home/roed/giant_padics_vs_2_10_1.hg



---

archive/issue_comments_012683.json:
```json
{
    "body": "With new patch, on Ubuntu 7.10, Intel Core Duo, four failures:\n\n```\nsage -t  devel/sage-padics_again/sage/rings/padics/padic_ZZ_pX_CA_element.pyx\nsage -t  devel/sage-padics_again/sage/rings/padics/factory.py\nsage -t  devel/sage-padics_again/sage/rings/padics/tutorial.py\nsage -t  devel/sage-padics_again/sage/rings/polynomial/multi_polynomial.\n```\n",
    "created_at": "2008-02-06T05:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12683",
    "user": "bober"
}
```

With new patch, on Ubuntu 7.10, Intel Core Duo, four failures:

```
sage -t  devel/sage-padics_again/sage/rings/padics/padic_ZZ_pX_CA_element.pyx
sage -t  devel/sage-padics_again/sage/rings/padics/factory.py
sage -t  devel/sage-padics_again/sage/rings/padics/tutorial.py
sage -t  devel/sage-padics_again/sage/rings/polynomial/multi_polynomial.
```




---

archive/issue_comments_012684.json:
```json
{
    "body": "\n```\nsage: R = Zp(5,5)\nsage: S.<x> = R[]\nsage: f = x^5 + 75*x^3 - 15*x^2 +125*x - 5\nsage: W.<w> = R.ext(f); W\nsage: W.residue_system()\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/padics/padic_generic.py\", line 274, in residue_system\n    return [self(i) for i in self.residue_class_field()]\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/padics/padic_generic.py\", line 84, in __call__\n    return self._element_class(self, x, absprec, relprec)\n  File \"padic_ZZ_pX_CR_element.pyx\", line 231, in sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement.__init__\n<type 'exceptions.TypeError'>: cannot coerce from the given integer mod ring (not a power of the same prime)\n```\n",
    "created_at": "2008-02-06T06:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12684",
    "user": "robertwb"
}
```


```
sage: R = Zp(5,5)
sage: S.<x> = R[]
sage: f = x^5 + 75*x^3 - 15*x^2 +125*x - 5
sage: W.<w> = R.ext(f); W
sage: W.residue_system()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/padics/padic_generic.py", line 274, in residue_system
    return [self(i) for i in self.residue_class_field()]
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/padics/padic_generic.py", line 84, in __call__
    return self._element_class(self, x, absprec, relprec)
  File "padic_ZZ_pX_CR_element.pyx", line 231, in sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement.__init__
<type 'exceptions.TypeError'>: cannot coerce from the given integer mod ring (not a power of the same prime)
```




---

archive/issue_comments_012685.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-06T06:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12685",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_012686.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-06T06:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12686",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_012687.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-06T09:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12687",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_012688.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-06T12:05:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12688",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_012689.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-06T19:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12689",
    "user": "kedlaya"
}
```

Attachment



---

archive/issue_comments_012690.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-08T18:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12690",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_012691.json:
```json
{
    "body": "Attachment\n\nMust apply against latest bundle",
    "created_at": "2008-02-08T23:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12691",
    "user": "kedlaya"
}
```

Attachment

Must apply against latest bundle



---

archive/issue_comments_012692.json:
```json
{
    "body": "Attachment\n\nMust apply against latest bundle",
    "created_at": "2008-02-08T23:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12692",
    "user": "kedlaya"
}
```

Attachment

Must apply against latest bundle



---

archive/issue_comments_012693.json:
```json
{
    "body": "Must apply against latest bundle",
    "created_at": "2008-02-08T23:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12693",
    "user": "kedlaya"
}
```

Must apply against latest bundle



---

archive/issue_comments_012694.json:
```json
{
    "body": "Attachment\n\nThe patches kedlaya2.patch and kedlaya2.2.patch are identical, so no need to grab the second one. Sorry about that.",
    "created_at": "2008-02-09T00:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12694",
    "user": "kedlaya"
}
```

Attachment

The patches kedlaya2.patch and kedlaya2.2.patch are identical, so no need to grab the second one. Sorry about that.



---

archive/issue_comments_012695.json:
```json
{
    "body": "Attachment\n\nBundle as of end of SD7",
    "created_at": "2008-02-10T02:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12695",
    "user": "roed"
}
```

Attachment

Bundle as of end of SD7



---

archive/issue_comments_012696.json:
```json
{
    "body": "Attachment\n\ndoctest fix",
    "created_at": "2008-02-10T03:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12696",
    "user": "roed"
}
```

Attachment

doctest fix



---

archive/issue_comments_012697.json:
```json
{
    "body": "Hi,\n\nwhat is the status of this now? I assume I need to apply 1963-padics-bundle-sd7-final.hg and padic-sd7-fix.patch. Let's get this merged :)\n\nCheers,\n\nMichael",
    "created_at": "2008-02-13T08:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12697",
    "user": "mabshoff"
}
```

Hi,

what is the status of this now? I assume I need to apply 1963-padics-bundle-sd7-final.hg and padic-sd7-fix.patch. Let's get this merged :)

Cheers,

Michael



---

archive/issue_comments_012698.json:
```json
{
    "body": "Status: waiting on David Roe for norm, degree, and trace. This is (almost) implemented, but not yet polished?? \n\nIf he's to busy to do this in the short term, perhaps we could put NotImplementedErrors in their place and merge, postponing the implementation of the above to a later ticket.",
    "created_at": "2008-02-14T05:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12698",
    "user": "robertwb"
}
```

Status: waiting on David Roe for norm, degree, and trace. This is (almost) implemented, but not yet polished?? 

If he's to busy to do this in the short term, perhaps we could put NotImplementedErrors in their place and merge, postponing the implementation of the above to a later ticket.



---

archive/issue_comments_012699.json:
```json
{
    "body": "Merged 1963-padics-bundle-sd7-final.hg and padic-sd7-fix.patch in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T02:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12699",
    "user": "mabshoff"
}
```

Merged 1963-padics-bundle-sd7-final.hg and padic-sd7-fix.patch in Sage 2.10.2.alpha0



---

archive/issue_comments_012700.json:
```json
{
    "body": "Running `-long` doctests showed (still) a lot of failures:\n\n```\n        sage -t -long devel/sage-main/sage/groups/group.pyx\n        sage -t -long devel/sage-main/sage/misc/functional.py\n        sage -t -long devel/sage-main/sage/rings/padics/padic_ZZ_pX_CA_element.pyx\n        sage -t -long devel/sage-main/sage/rings/padics/padic_ZZ_pX_CR_element.pyx\n        sage -t -long devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx\n        sage -t -long devel/sage-main/sage/rings/padics/padic_generic.py\n        sage -t -long devel/sage-main/sage/rings/padics/padic_generic_element.pyx\n        sage -t -long devel/sage-main/sage/rings/padics/pow_computer_ext.pyx\n        sage -t -long devel/sage-main/sage/rings/padics/tests.py\n        sage -t -long devel/sage-main/sage/rings/padics/padic_ZZ_pX_FM_element.pyx\n        sage -t -long devel/sage-main/sage/rings/padics/padic_ZZ_pX_element.pyx\n        sage -t -long devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx\n        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py\n        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_padic_field.py\n        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_point.py\n        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py\n        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_tate_curve.py\n        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/padic_lseries.py\n        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/padics.py\n        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/sha.py\n        sage -t -long devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\n```\n\nAm I missing something?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T04:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12700",
    "user": "mabshoff"
}
```

Running `-long` doctests showed (still) a lot of failures:

```
        sage -t -long devel/sage-main/sage/groups/group.pyx
        sage -t -long devel/sage-main/sage/misc/functional.py
        sage -t -long devel/sage-main/sage/rings/padics/padic_ZZ_pX_CA_element.pyx
        sage -t -long devel/sage-main/sage/rings/padics/padic_ZZ_pX_CR_element.pyx
        sage -t -long devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx
        sage -t -long devel/sage-main/sage/rings/padics/padic_generic.py
        sage -t -long devel/sage-main/sage/rings/padics/padic_generic_element.pyx
        sage -t -long devel/sage-main/sage/rings/padics/pow_computer_ext.pyx
        sage -t -long devel/sage-main/sage/rings/padics/tests.py
        sage -t -long devel/sage-main/sage/rings/padics/padic_ZZ_pX_FM_element.pyx
        sage -t -long devel/sage-main/sage/rings/padics/padic_ZZ_pX_element.pyx
        sage -t -long devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_padic_field.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_point.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_tate_curve.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/padic_lseries.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/padics.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/sha.py
        sage -t -long devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py
```

Am I missing something?

Cheers,

Michael



---

archive/issue_comments_012701.json:
```json
{
    "body": "Attachment\n\nThis patch fixes the import issue from 2.10.2.alpha0",
    "created_at": "2008-02-15T17:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12701",
    "user": "mabshoff"
}
```

Attachment

This patch fixes the import issue from 2.10.2.alpha0



---

archive/issue_comments_012702.json:
```json
{
    "body": "Here are some of the doctest failures:\n\n```\nsage -t  const.tex\n**********************************************************************\nFile \"const.py\", line 2503:\n    : b^4\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_82[8]>\", line 1, in <module>\n        b**Integer(4)###line 2503:\n    : b^4\n      File \"padic_capped_relative_element.pyx\", line 747, in sage.rings.padics.padic_capped_relative_element.pAdicCappedRela\ntiveElement.__pow__\n    ValueError: Valuation too large\n**********************************************************************\n```\n\nand\n\n```\nsage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_CA_element.pyx\n**********************************************************************\nFile \"padic_ZZ_pX_CA_element.pyx\", line 48:\n    sage: (1/w)^12+w\nExpected:\n    w^-12 + w + O(w^12)\nGot:\n    0\n**********************************************************************\nFile \"padic_ZZ_pX_CA_element.pyx\", line 62:\n    sage: 1/a\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[17]>\", line 1, in <module>\n        Integer(1)/a###line 62:\n    sage: 1/a\n      File \"element.pyx\", line 1482, in sage.structure.element.RingElement.__div__\n      File \"coerce.pyx\", line 253, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c\n      File \"element.pyx\", line 1480, in sage.structure.element.RingElement.__div__\n      File \"coerce.pxi\", line 138, in sage.structure.element._div_c\n      File \"padic_ZZ_pX_CA_element.pyx\", line 1303, in sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement._div_c_im\npl\n        return self.to_fraction_field() * (~right)\n      File \"element.pyx\", line 1372, in sage.structure.element.RingElement.__mul__\n      File \"coerce.pxi\", line 126, in sage.structure.element._mul_c\n      File \"padic_ZZ_pX_CR_element.pyx\", line 1789, in sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement._mul_c_im\npl\n        raise ValueError, \"valuation overflow\"\n    ValueError: valuation overflow\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T01:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12702",
    "user": "mabshoff"
}
```

Here are some of the doctest failures:

```
sage -t  const.tex
**********************************************************************
File "const.py", line 2503:
    : b^4
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_82[8]>", line 1, in <module>
        b**Integer(4)###line 2503:
    : b^4
      File "padic_capped_relative_element.pyx", line 747, in sage.rings.padics.padic_capped_relative_element.pAdicCappedRela
tiveElement.__pow__
    ValueError: Valuation too large
**********************************************************************
```

and

```
sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_CA_element.pyx
**********************************************************************
File "padic_ZZ_pX_CA_element.pyx", line 48:
    sage: (1/w)^12+w
Expected:
    w^-12 + w + O(w^12)
Got:
    0
**********************************************************************
File "padic_ZZ_pX_CA_element.pyx", line 62:
    sage: 1/a
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[17]>", line 1, in <module>
        Integer(1)/a###line 62:
    sage: 1/a
      File "element.pyx", line 1482, in sage.structure.element.RingElement.__div__
      File "coerce.pyx", line 253, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c
      File "element.pyx", line 1480, in sage.structure.element.RingElement.__div__
      File "coerce.pxi", line 138, in sage.structure.element._div_c
      File "padic_ZZ_pX_CA_element.pyx", line 1303, in sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement._div_c_im
pl
        return self.to_fraction_field() * (~right)
      File "element.pyx", line 1372, in sage.structure.element.RingElement.__mul__
      File "coerce.pxi", line 126, in sage.structure.element._mul_c
      File "padic_ZZ_pX_CR_element.pyx", line 1789, in sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement._mul_c_im
pl
        raise ValueError, "valuation overflow"
    ValueError: valuation overflow
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_012703.json:
```json
{
    "body": "#2233 fixes all 64 bit specific doctest failures. We currently have four NotYetImplemented and one fixme doctest failures left, that should happen on 32 as well as 64 bit.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-20T20:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12703",
    "user": "mabshoff"
}
```

#2233 fixes all 64 bit specific doctest failures. We currently have four NotYetImplemented and one fixme doctest failures left, that should happen on 32 as well as 64 bit.

Cheers,

Michael



---

archive/issue_comments_012704.json:
```json
{
    "body": "Craig Citro, Kiran Kedlaya, Robert Bradshaw and David Roe did extensive review and bug fixing at Sage Days 7. So I am giving this a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T03:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12704",
    "user": "mabshoff"
}
```

Craig Citro, Kiran Kedlaya, Robert Bradshaw and David Roe did extensive review and bug fixing at Sage Days 7. So I am giving this a positive review.

Cheers,

Michael



---

archive/issue_comments_012705.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T03:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12705",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012706.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1 - there are some small issues left, please open another ticket for any new patch. This ticket is overloaded as is.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T03:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1963#issuecomment-12706",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1 - there are some small issues left, please open another ticket for any new patch. This ticket is overloaded as is.

Cheers,

Michael
