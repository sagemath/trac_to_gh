# Issue 610: padics have no doctests

archive/issues_000610.json:
```json
{
    "body": "Assignee: @roed314\n\nAll files in the rings/padics directory need doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/610\n\n",
    "created_at": "2007-09-07T01:09:01Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "padics have no doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/610",
    "user": "boothby"
}
```
Assignee: @roed314

All files in the rings/padics directory need doctests.

Issue created by migration from https://trac.sagemath.org/ticket/610





---

archive/issue_comments_003138.json:
```json
{
    "body": "While it isn't 0% any more it certainly isn't close to 100% yet.\n\n```\n./sage -coverageall devel/sage-main/sage/rings/padics\nOverall weighted coverage score:  11.3%\nTotal number of functions:  796\n./sage -coverageall devel/sage-main/sage/rings/polynomial/padics\n[snip]\nOverall weighted coverage score:  42.4%\nTotal number of functions:  47\n./sage -coverageall devel/sage-main/sage/matrix/padics\n[snip]\nOverall weighted coverage score:  0.0%\nTotal number of functions:  4\n\nCheers,\n\nMichael",
    "created_at": "2007-12-24T09:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/610#issuecomment-3138",
    "user": "mabshoff"
}
```

While it isn't 0% any more it certainly isn't close to 100% yet.

```
./sage -coverageall devel/sage-main/sage/rings/padics
Overall weighted coverage score:  11.3%
Total number of functions:  796
./sage -coverageall devel/sage-main/sage/rings/polynomial/padics
[snip]
Overall weighted coverage score:  42.4%
Total number of functions:  47
./sage -coverageall devel/sage-main/sage/matrix/padics
[snip]
Overall weighted coverage score:  0.0%
Total number of functions:  4

Cheers,

Michael



---

archive/issue_comments_003139.json:
```json
{
    "body": "Things are improving. With 2.10.4 final I get:\n\n```\nsage-2.10.4.final$ ./sage -coverageall devel/sage/sage/rings/padics/\ncapped_absolute_generic.py: 0% (0 of 1)\ncapped_relative_generic.py: 0% (0 of 1)\neisenstein_extension_generic.py: 0% (0 of 18)\nfactory.py: 13% (3 of 22)\nfixed_mod_generic.py: 0% (0 of 1)\nlazy_generic.py: 0% (0 of 3)\nlocal_generic_element.pyx: 70% (7 of 10)\nlocal_generic.py: 27% (10 of 37)\nmisc.py: 0% (0 of 2)\npadic_base_generic_element.pyx: 0% (0 of 1)\npadic_base_generic.py: 0% (0 of 5)\npadic_capped_absolute_element.pyx: 84% (22 of 26)\npadic_capped_relative_element.pyx: 48% (16 of 33)\npadic_ext_element.pyx: 0% (0 of 1)\npadic_extension_generic.py: 0% (0 of 20)\npadic_extension_leaves.py: 0% (0 of 8)\npadic_field_capped_relative.py: 20% (1 of 5)\npadic_field_generic.py: 0% (0 of 14)\npadic_field_lazy.py: 11% (2 of 17)\npadic_fixed_mod_element.pyx: 42% (12 of 28)\npadic_generic_element.pyx: 31% (10 of 32)\npadic_generic.py: 42% (14 of 33)\npadic_lazy_element.py: 0% (1 of 110)\npadic_lazy_field_generic.py: 0% (0 of 1)\npadic_lazy_generic.py: 0% (0 of 2)\npadic_lazy_ring_generic.py: 0% (0 of 1)\npadic_printing.pyx: 33% (7 of 21)\npadic_ring_base_generic.py: 0% (0 of 3)\npadic_ring_capped_absolute.py: 0% (0 of 5)\npadic_ring_capped_relative.py: 0% (0 of 5)\npadic_ring_fixed_mod.py: 0% (0 of 5)\npadic_ring_generic.py: 0% (0 of 6)\npadic_ring_lazy.py: 7% (1 of 13)\npadic_ZZ_pX_CA_element.pyx: 72% (21 of 29)\npadic_ZZ_pX_CR_element.pyx: 70% (22 of 31)\npadic_ZZ_pX_element.pyx: 40% (2 of 5)\npadic_ZZ_pX_FM_element.pyx: 74% (23 of 31)\npow_computer_ext.pyx: 77% (21 of 27)\npow_computer.pyx: 93% (14 of 15)\nrigid_functions.pyx: 0% (0 of 37)\nunramified_extension_generic.py: 0% (0 of 20)\nvaluation.py: 0% (0 of 114)\n\nOverall weighted coverage score:  25.8%\nTotal number of functions:  799\n```\n\nand\n\n```\nsage-2.10.4.final$ ./sage -coverageall devel/sage-main/sage/rings/polynomial/padics/\npolynomial_padic_capped_relative_dense.py: 42% (19 of 45)\npolynomial_padic_flat.py: 25% (1 of 4)\n\nOverall weighted coverage score:  40.6%\nTotal number of functions:  49\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-17T01:03:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/610#issuecomment-3139",
    "user": "mabshoff"
}
```

Things are improving. With 2.10.4 final I get:

```
sage-2.10.4.final$ ./sage -coverageall devel/sage/sage/rings/padics/
capped_absolute_generic.py: 0% (0 of 1)
capped_relative_generic.py: 0% (0 of 1)
eisenstein_extension_generic.py: 0% (0 of 18)
factory.py: 13% (3 of 22)
fixed_mod_generic.py: 0% (0 of 1)
lazy_generic.py: 0% (0 of 3)
local_generic_element.pyx: 70% (7 of 10)
local_generic.py: 27% (10 of 37)
misc.py: 0% (0 of 2)
padic_base_generic_element.pyx: 0% (0 of 1)
padic_base_generic.py: 0% (0 of 5)
padic_capped_absolute_element.pyx: 84% (22 of 26)
padic_capped_relative_element.pyx: 48% (16 of 33)
padic_ext_element.pyx: 0% (0 of 1)
padic_extension_generic.py: 0% (0 of 20)
padic_extension_leaves.py: 0% (0 of 8)
padic_field_capped_relative.py: 20% (1 of 5)
padic_field_generic.py: 0% (0 of 14)
padic_field_lazy.py: 11% (2 of 17)
padic_fixed_mod_element.pyx: 42% (12 of 28)
padic_generic_element.pyx: 31% (10 of 32)
padic_generic.py: 42% (14 of 33)
padic_lazy_element.py: 0% (1 of 110)
padic_lazy_field_generic.py: 0% (0 of 1)
padic_lazy_generic.py: 0% (0 of 2)
padic_lazy_ring_generic.py: 0% (0 of 1)
padic_printing.pyx: 33% (7 of 21)
padic_ring_base_generic.py: 0% (0 of 3)
padic_ring_capped_absolute.py: 0% (0 of 5)
padic_ring_capped_relative.py: 0% (0 of 5)
padic_ring_fixed_mod.py: 0% (0 of 5)
padic_ring_generic.py: 0% (0 of 6)
padic_ring_lazy.py: 7% (1 of 13)
padic_ZZ_pX_CA_element.pyx: 72% (21 of 29)
padic_ZZ_pX_CR_element.pyx: 70% (22 of 31)
padic_ZZ_pX_element.pyx: 40% (2 of 5)
padic_ZZ_pX_FM_element.pyx: 74% (23 of 31)
pow_computer_ext.pyx: 77% (21 of 27)
pow_computer.pyx: 93% (14 of 15)
rigid_functions.pyx: 0% (0 of 37)
unramified_extension_generic.py: 0% (0 of 20)
valuation.py: 0% (0 of 114)

Overall weighted coverage score:  25.8%
Total number of functions:  799
```

and

```
sage-2.10.4.final$ ./sage -coverageall devel/sage-main/sage/rings/polynomial/padics/
polynomial_padic_capped_relative_dense.py: 42% (19 of 45)
polynomial_padic_flat.py: 25% (1 of 4)

Overall weighted coverage score:  40.6%
Total number of functions:  49
```


Cheers,

Michael



---

archive/issue_comments_003140.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-15T00:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/610#issuecomment-3140",
    "user": "@craigcitro"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_003141.json:
```json
{
    "body": "Replying to [comment:4 craigcitro]:\n\n> type changed from defect to enhancement.\n\nWell, given the fact that the padics code was merged at SD 7 under the assumption that someone would write more doctests I could see this being a defect given the amount of time elapsed since then :)\n\nCheers,\n\nMichael",
    "created_at": "2009-01-15T00:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/610#issuecomment-3141",
    "user": "mabshoff"
}
```

Replying to [comment:4 craigcitro]:

> type changed from defect to enhancement.

Well, given the fact that the padics code was merged at SD 7 under the assumption that someone would write more doctests I could see this being a defect given the amount of time elapsed since then :)

Cheers,

Michael



---

archive/issue_comments_003142.json:
```json
{
    "body": "We changed this since the \"defects\" in trac should be actual bugs.  This will be helpful, e.g., next week at Sage Days 12 -- fix many bugs in Sage.  There are at least 600 (or so) *open* \"defects\" in trac right now.",
    "created_at": "2009-01-15T03:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/610#issuecomment-3142",
    "user": "@williamstein"
}
```

We changed this since the "defects" in trac should be actual bugs.  This will be helpful, e.g., next week at Sage Days 12 -- fix many bugs in Sage.  There are at least 600 (or so) *open* "defects" in trac right now.



---

archive/issue_comments_003143.json:
```json
{
    "body": "Is this now a duplicate of the behemoth work at #5778?",
    "created_at": "2009-04-30T00:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/610#issuecomment-3143",
    "user": "@kcrisman"
}
```

Is this now a duplicate of the behemoth work at #5778?



---

archive/issue_comments_003144.json:
```json
{
    "body": "yes.  This is subsumed by #5778.",
    "created_at": "2009-04-30T00:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/610#issuecomment-3144",
    "user": "@roed314"
}
```

yes.  This is subsumed by #5778.



---

archive/issue_comments_003145.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-04-30T00:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/610#issuecomment-3145",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_003146.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> Is this now a duplicate of the behemoth work at #5778?\n\nYes, David opened a new ticket, so nuke this as a dupe.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T00:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/610#issuecomment-3146",
    "user": "mabshoff"
}
```

Replying to [comment:7 kcrisman]:
> Is this now a duplicate of the behemoth work at #5778?

Yes, David opened a new ticket, so nuke this as a dupe.

Cheers,

Michael
