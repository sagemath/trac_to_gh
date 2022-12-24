# Issue 2507: Docstrings and Doctests for rings/quotient_ring_element.py

archive/issues_002507.json:
```json
{
    "body": "Assignee: failure\n\nKeywords: docstring, doctest\n\nCurrent coverage in Sage 2.10.3: SCORE quotient_ring_element.py: 3% (1 of 27)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2507\n\n",
    "created_at": "2008-03-13T17:47:37Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Docstrings and Doctests for rings/quotient_ring_element.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2507",
    "user": "@cswiercz"
}
```
Assignee: failure

Keywords: docstring, doctest

Current coverage in Sage 2.10.3: SCORE quotient_ring_element.py: 3% (1 of 27)

Issue created by migration from https://trac.sagemath.org/ticket/2507





---

archive/issue_comments_016983.json:
```json
{
    "body": "Changing assignee from failure to @cswiercz.",
    "created_at": "2008-03-14T03:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16983",
    "user": "@cswiercz"
}
```

Changing assignee from failure to @cswiercz.



---

archive/issue_comments_016984.json:
```json
{
    "body": "doctests and docstrings [SCORE quotient_ring_element.py: 37% (10 of 27)]",
    "created_at": "2008-04-02T21:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16984",
    "user": "@cswiercz"
}
```

doctests and docstrings [SCORE quotient_ring_element.py: 37% (10 of 27)]



---

archive/issue_comments_016985.json:
```json
{
    "body": "Attachment [rings.quotient_ring_element.patch](tarball://root/attachments/some-uuid/ticket2507/rings.quotient_ring_element.patch) by mabshoff created at 2008-04-07 22:54:34\n\nChris,\n\nplease make sure that you properly mark tickets with doctests added. Otherwise we cannot find them since attaching patches does not trigger an email to sage-trac.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T22:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16985",
    "user": "mabshoff"
}
```

Attachment [rings.quotient_ring_element.patch](tarball://root/attachments/some-uuid/ticket2507/rings.quotient_ring_element.patch) by mabshoff created at 2008-04-07 22:54:34

Chris,

please make sure that you properly mark tickets with doctests added. Otherwise we cannot find them since attaching patches does not trigger an email to sage-trac.

Cheers,

Michael



---

archive/issue_comments_016986.json:
```json
{
    "body": "Attachment [2507.patch](tarball://root/attachments/some-uuid/ticket2507/2507.patch) by @mwhansen created at 2008-04-07 23:01:13\n\n2507.patch applies against 3.0.alpha2 and passes tests.",
    "created_at": "2008-04-07T23:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16986",
    "user": "@mwhansen"
}
```

Attachment [2507.patch](tarball://root/attachments/some-uuid/ticket2507/2507.patch) by @mwhansen created at 2008-04-07 23:01:13

2507.patch applies against 3.0.alpha2 and passes tests.



---

archive/issue_comments_016987.json:
```json
{
    "body": "This patch needs to be rebase. It fails to apply cleanly against my current merge tree:\n\n```\nsage-3.0.alpha3/devel/sage$ patch -p1 < trac_2507_rings.quotient_ring_element.patch\npatching file sage/rings/quotient_ring_element.py\nHunk #1 FAILED at 66.\nHunk #2 succeeded at 147 (offset 2 lines).\nHunk #3 succeeded at 274 (offset 2 lines).\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T23:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16987",
    "user": "mabshoff"
}
```

This patch needs to be rebase. It fails to apply cleanly against my current merge tree:

```
sage-3.0.alpha3/devel/sage$ patch -p1 < trac_2507_rings.quotient_ring_element.patch
patching file sage/rings/quotient_ring_element.py
Hunk #1 FAILED at 66.
Hunk #2 succeeded at 147 (offset 2 lines).
Hunk #3 succeeded at 274 (offset 2 lines).
```

Cheers,

Michael



---

archive/issue_comments_016988.json:
```json
{
    "body": "I **really** like that someone sat down to write doctests for `quotient_ring_element.py`, but I see some issues:\n\n\n```\nsage: Q = ZZ.quotient(10*ZZ)\nsage: type(Q)\n<class 'sage.rings.integer_mod_ring.IntegerModRing_generic'>\nsage: type(Q.gen())\n<type 'sage.rings.integer_mod.IntegerMod_int'>\n```\n\n\nand\n\n\n```\nsage: R.<a> = QuotientRing(QQ[x], x^2 + 1)\nsage: type(R)\n<class 'sage.rings.polynomial.polynomial_quotient_ring.PolynomialQuotientRing_field'>\nsage: type(a)\n<class 'sage.rings.polynomial.polynomial_quotient_ring_element.PolynomialQuotientRingElement'>\n```\n\n\nThus, the documentation doesn't actually illustrate the class. AFAIK this class is mainly useful/used for multivariate polynomial rings. This theory reinforced by the `lm()` and `monomials()` methods. This class is just a mess, maybe?",
    "created_at": "2008-04-10T23:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16988",
    "user": "@malb"
}
```

I **really** like that someone sat down to write doctests for `quotient_ring_element.py`, but I see some issues:


```
sage: Q = ZZ.quotient(10*ZZ)
sage: type(Q)
<class 'sage.rings.integer_mod_ring.IntegerModRing_generic'>
sage: type(Q.gen())
<type 'sage.rings.integer_mod.IntegerMod_int'>
```


and


```
sage: R.<a> = QuotientRing(QQ[x], x^2 + 1)
sage: type(R)
<class 'sage.rings.polynomial.polynomial_quotient_ring.PolynomialQuotientRing_field'>
sage: type(a)
<class 'sage.rings.polynomial.polynomial_quotient_ring_element.PolynomialQuotientRingElement'>
```


Thus, the documentation doesn't actually illustrate the class. AFAIK this class is mainly useful/used for multivariate polynomial rings. This theory reinforced by the `lm()` and `monomials()` methods. This class is just a mess, maybe?



---

archive/issue_comments_016989.json:
```json
{
    "body": "Addresses (sort of) the issues brought up by malb. Will additional detailed examples in a later patch. APPLY AFTER 2507.patch.",
    "created_at": "2008-04-17T22:23:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16989",
    "user": "@cswiercz"
}
```

Addresses (sort of) the issues brought up by malb. Will additional detailed examples in a later patch. APPLY AFTER 2507.patch.



---

archive/issue_comments_016990.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-17T23:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16990",
    "user": "@cswiercz"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016991.json:
```json
{
    "body": "Attachment [2507_additional.patch](tarball://root/attachments/some-uuid/ticket2507/2507_additional.patch) by @cswiercz created at 2008-04-17 23:53:47",
    "created_at": "2008-04-17T23:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16991",
    "user": "@cswiercz"
}
```

Attachment [2507_additional.patch](tarball://root/attachments/some-uuid/ticket2507/2507_additional.patch) by @cswiercz created at 2008-04-17 23:53:47



---

archive/issue_comments_016992.json:
```json
{
    "body": "I am not sure this is the right fix: Doctests should test and demonstrate the class and it doesn't make sense to create the QuotientRing(ZZ,10) when ZZ.quotient(10) is available and much faster. Why not test it with the rings it is intended for (multivariate polynomials)?",
    "created_at": "2008-04-18T08:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16992",
    "user": "@malb"
}
```

I am not sure this is the right fix: Doctests should test and demonstrate the class and it doesn't make sense to create the QuotientRing(ZZ,10) when ZZ.quotient(10) is available and much faster. Why not test it with the rings it is intended for (multivariate polynomials)?



---

archive/issue_comments_016993.json:
```json
{
    "body": "Mmm, this patch might have bitrotted. Anyway, it still needs a review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T19:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16993",
    "user": "mabshoff"
}
```

Mmm, this patch might have bitrotted. Anyway, it still needs a review.

Cheers,

Michael



---

archive/issue_comments_016994.json:
```json
{
    "body": "I think this patch needs work since it doesn't doctest the main purpose of this class: multivariate polynomial quotients.",
    "created_at": "2008-09-28T14:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16994",
    "user": "@malb"
}
```

I think this patch needs work since it doesn't doctest the main purpose of this class: multivariate polynomial quotients.



---

archive/issue_comments_016995.json:
```json
{
    "body": "The patch at #5724 added examples but not actual documentation -- no descriptions of what the various methods do. So I took the docstrings from the patches here, rewrote them a little, and made a new patch.  This patch replaces all of the others.",
    "created_at": "2009-05-10T16:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16995",
    "user": "@jhpalmieri"
}
```

The patch at #5724 added examples but not actual documentation -- no descriptions of what the various methods do. So I took the docstrings from the patches here, rewrote them a little, and made a new patch.  This patch replaces all of the others.



---

archive/issue_comments_016996.json:
```json
{
    "body": "(cswiercz should get credit for this as well as me, since I took the docstrings from the previous patches here.)",
    "created_at": "2009-05-10T16:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16996",
    "user": "@jhpalmieri"
}
```

(cswiercz should get credit for this as well as me, since I took the docstrings from the previous patches here.)



---

archive/issue_comments_016997.json:
```json
{
    "body": "First, two trivial issues with the patch `trac_2507.patch`. The double colon on line 48 is not indented properly. It should be aligned with the double colon on line 53. Also, the docstring for `_div_` is a bit confusing due to excessive use of the word \"quotient\". The word \"quotient\" as used in\n\n```\n263\t        Quotient of quotient ring element ``self`` by another quotient ring \n264\t        element, ``right``. If the quotient is `R/I`, the division is \n265\t        carried out in `R` and then reduced to `R/I`.\n```\n\nhas two meanings: to denote division of one element by another; and to mean a quotient ring. When division is intended, I think \"division\" should be used instead of quotient. So line 263 of the docstring can be changed as follows to avoid confusion/ambiguity:\n\n```\n263\t        Division of quotient ring element ``self`` by another quotient ring \n264\t        element, ``right``. If the quotient is `R/I`, the division is \n265\t        carried out in `R` and then reduced to `R/I`.\n```\n\nThe other issue is that in the constructor signature\n\n```\n77\t    def __init__(self, parent, rep, reduce=True):\n```\n\nthe input are not documented. My knowledge of quotient rings is pretty limited, and it can be difficult to work out what each of the arguments `parent`, `rep` and `reduce=True` means, and how to use them properly.",
    "created_at": "2009-05-11T02:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16997",
    "user": "mvngu"
}
```

First, two trivial issues with the patch `trac_2507.patch`. The double colon on line 48 is not indented properly. It should be aligned with the double colon on line 53. Also, the docstring for `_div_` is a bit confusing due to excessive use of the word "quotient". The word "quotient" as used in

```
263	        Quotient of quotient ring element ``self`` by another quotient ring 
264	        element, ``right``. If the quotient is `R/I`, the division is 
265	        carried out in `R` and then reduced to `R/I`.
```

has two meanings: to denote division of one element by another; and to mean a quotient ring. When division is intended, I think "division" should be used instead of quotient. So line 263 of the docstring can be changed as follows to avoid confusion/ambiguity:

```
263	        Division of quotient ring element ``self`` by another quotient ring 
264	        element, ``right``. If the quotient is `R/I`, the division is 
265	        carried out in `R` and then reduced to `R/I`.
```

The other issue is that in the constructor signature

```
77	    def __init__(self, parent, rep, reduce=True):
```

the input are not documented. My knowledge of quotient rings is pretty limited, and it can be difficult to work out what each of the arguments `parent`, `rep` and `reduce=True` means, and how to use them properly.



---

archive/issue_comments_016998.json:
```json
{
    "body": "Here's a new patch.",
    "created_at": "2009-05-11T17:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16998",
    "user": "@jhpalmieri"
}
```

Here's a new patch.



---

archive/issue_comments_016999.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2009-05-11T17:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-16999",
    "user": "@jhpalmieri"
}
```

apply only this patch



---

archive/issue_comments_017000.json:
```json
{
    "body": "Attachment [trac_2507.patch](tarball://root/attachments/some-uuid/ticket2507/trac_2507.patch) by mvngu created at 2009-05-12 23:31:41\n\nAll my concerns have been addressed in the patch `trac_2507.patch`. Doctest coverage for `sage/rings/quotient_ring_element.py` is now 100%. Positive review.",
    "created_at": "2009-05-12T23:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-17000",
    "user": "mvngu"
}
```

Attachment [trac_2507.patch](tarball://root/attachments/some-uuid/ticket2507/trac_2507.patch) by mvngu created at 2009-05-12 23:31:41

All my concerns have been addressed in the patch `trac_2507.patch`. Doctest coverage for `sage/rings/quotient_ring_element.py` is now 100%. Positive review.



---

archive/issue_comments_017001.json:
```json
{
    "body": "Merged trac_2507.patch in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-13T18:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-17001",
    "user": "mabshoff"
}
```

Merged trac_2507.patch in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_017002.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-13T18:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2507#issuecomment-17002",
    "user": "mabshoff"
}
```

Resolution: fixed
