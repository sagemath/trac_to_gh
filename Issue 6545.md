# Issue 6545: sorting of ideal bases

archive/issues_006545.json:
```json
{
    "body": "Assignee: @malb\n\n`MPolynomialIdeal.interreduced_basis()` should return the same sorted list as `MPolynomialIdeal.interreduced_basis()`, also the input to `MPolynomialIdeal.triangular_decomposition()` must be sorted to avoid confusing Singular.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6545\n\n",
    "created_at": "2009-07-16T19:23:45Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "sorting of ideal bases",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6545",
    "user": "@malb"
}
```
Assignee: @malb

`MPolynomialIdeal.interreduced_basis()` should return the same sorted list as `MPolynomialIdeal.interreduced_basis()`, also the input to `MPolynomialIdeal.triangular_decomposition()` must be sorted to avoid confusing Singular.

Issue created by migration from https://trac.sagemath.org/ticket/6545





---

archive/issue_comments_053362.json:
```json
{
    "body": "Attachment [trac_6545_mpolynomial_ideal_sorted_outputs.patch](tarball://root/attachments/some-uuid/ticket6545/trac_6545_mpolynomial_ideal_sorted_outputs.patch) by @malb created at 2009-07-16 19:24:52",
    "created_at": "2009-07-16T19:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53362",
    "user": "@malb"
}
```

Attachment [trac_6545_mpolynomial_ideal_sorted_outputs.patch](tarball://root/attachments/some-uuid/ticket6545/trac_6545_mpolynomial_ideal_sorted_outputs.patch) by @malb created at 2009-07-16 19:24:52



---

archive/issue_comments_053363.json:
```json
{
    "body": "I don't understand the description of the comment: \"MPolynomialIdeal.interreduced_basis() should return the same sorted list as MPolynomialIdeal.interreduced_basis()\" Can someone elaborate?",
    "created_at": "2009-08-18T20:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53363",
    "user": "@johnperry-math"
}
```

I don't understand the description of the comment: "MPolynomialIdeal.interreduced_basis() should return the same sorted list as MPolynomialIdeal.interreduced_basis()" Can someone elaborate?



---

archive/issue_comments_053364.json:
```json
{
    "body": "Sorry, my bad. It should read\n\n\n`MPolynomialIdeal.interreduced_basis()` should return the same sorted list as `MPolynomialIdeal.groebner_basis()` when called on an ideal which has a  (not reduced) Groebner basis as set of generators.",
    "created_at": "2009-08-18T20:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53364",
    "user": "@malb"
}
```

Sorry, my bad. It should read


`MPolynomialIdeal.interreduced_basis()` should return the same sorted list as `MPolynomialIdeal.groebner_basis()` when called on an ideal which has a  (not reduced) Groebner basis as set of generators.



---

archive/issue_comments_053365.json:
```json
{
    "body": "Still applies against 4.1.1. One hunk might fail if #6596 and #6628 are applied (they fix the same annoying doctest output).",
    "created_at": "2009-08-26T12:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53365",
    "user": "@malb"
}
```

Still applies against 4.1.1. One hunk might fail if #6596 and #6628 are applied (they fix the same annoying doctest output).



---

archive/issue_comments_053366.json:
```json
{
    "body": "I'm working on an unmodified sage 4.1.1 and I can't get the patch to work. Nearly all the hunks fail.",
    "created_at": "2009-08-26T17:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53366",
    "user": "@johnperry-math"
}
```

I'm working on an unmodified sage 4.1.1 and I can't get the patch to work. Nearly all the hunks fail.



---

archive/issue_comments_053367.json:
```json
{
    "body": "Strange, here is what I do:\n* hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6545/trac_6545_mpolynomial_ideal_sorted_outputs.patch\n* hg qpush (no hunk fails)\n* sage -b\n\nDid you mix up raw-attachment and attachment?",
    "created_at": "2009-08-26T17:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53367",
    "user": "@malb"
}
```

Strange, here is what I do:
* hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6545/trac_6545_mpolynomial_ideal_sorted_outputs.patch
* hg qpush (no hunk fails)
* sage -b

Did you mix up raw-attachment and attachment?



---

archive/issue_comments_053368.json:
```json
{
    "body": "I tried your suggestion and it failed with the same errors. This will sound weird, but I'm looking at the diff and at the file, and it looks as if the patch applied anyway. I don't get it; maybe this thing isn't unmodified, or something is mucked up in the hg. I'm trying to work it out...",
    "created_at": "2009-08-26T18:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53368",
    "user": "@johnperry-math"
}
```

I tried your suggestion and it failed with the same errors. This will sound weird, but I'm looking at the diff and at the file, and it looks as if the patch applied anyway. I don't get it; maybe this thing isn't unmodified, or something is mucked up in the hg. I'm trying to work it out...



---

archive/issue_comments_053369.json:
```json
{
    "body": "This seems to be working, with one exception. When I run it, I get one error:\n\n    TypeError: factor() got an unexpected keyword argument 'proof'\n\nThis is ticket #5958, isn't it?",
    "created_at": "2009-08-26T18:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53369",
    "user": "@johnperry-math"
}
```

This seems to be working, with one exception. When I run it, I get one error:

    TypeError: factor() got an unexpected keyword argument 'proof'

This is ticket #5958, isn't it?



---

archive/issue_comments_053370.json:
```json
{
    "body": "Yep, that should be it.",
    "created_at": "2009-08-26T19:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53370",
    "user": "@malb"
}
```

Yep, that should be it.



---

archive/issue_comments_053371.json:
```json
{
    "body": "Should I mark this as a positive review? Once the patch to ticket 5958 is applied, this should work.",
    "created_at": "2009-08-26T20:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53371",
    "user": "@johnperry-math"
}
```

Should I mark this as a positive review? Once the patch to ticket 5958 is applied, this should work.



---

archive/issue_comments_053372.json:
```json
{
    "body": "I just did a {{{make test}} with the following patches applied on sage.math\n\n\n```\nvariety_CC.patch\nvariety_CC2.patch\ntrac_6545_mpolynomial_ideal_sorted_outputs.patch\n```\n\n\nand all tests passed. So I guess it is a **positive review** then? I leave it up to you.",
    "created_at": "2009-08-26T21:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53372",
    "user": "@malb"
}
```

I just did a {{{make test}} with the following patches applied on sage.math


```
variety_CC.patch
variety_CC2.patch
trac_6545_mpolynomial_ideal_sorted_outputs.patch
```


and all tests passed. So I guess it is a **positive review** then? I leave it up to you.



---

archive/issue_comments_053373.json:
```json
{
    "body": "I say positive review. If anyone says otherwise I'll leave academia and become a hermit.\n\nWell, maybe not. But I'll want to. ;-)",
    "created_at": "2009-08-26T22:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53373",
    "user": "@johnperry-math"
}
```

I say positive review. If anyone says otherwise I'll leave academia and become a hermit.

Well, maybe not. But I'll want to. ;-)



---

archive/issue_comments_053374.json:
```json
{
    "body": "First I merged patches at #6596 and #6628. Merging `trac_6545_mpolynomial_ideal_sorted_outputs.patch` results in a hunk failure:\n\n```\n[mvngu@mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6545/trac_6545_mpolynomial_ideal_sorted_outputs.patch && hg qpush\nadding trac_6545_mpolynomial_ideal_sorted_outputs.patch to series file\napplying trac_6545_mpolynomial_ideal_sorted_outputs.patch\npatching file sage/schemes/hyperelliptic_curves/jacobian_morphism.py\nHunk #1 FAILED at 294\n1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/jacobian_morphism.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh trac_6545_mpolynomial_ideal_sorted_outputs.patch\n```\n",
    "created_at": "2009-09-03T06:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53374",
    "user": "mvngu"
}
```

First I merged patches at #6596 and #6628. Merging `trac_6545_mpolynomial_ideal_sorted_outputs.patch` results in a hunk failure:

```
[mvngu@mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6545/trac_6545_mpolynomial_ideal_sorted_outputs.patch && hg qpush
adding trac_6545_mpolynomial_ideal_sorted_outputs.patch to series file
applying trac_6545_mpolynomial_ideal_sorted_outputs.patch
patching file sage/schemes/hyperelliptic_curves/jacobian_morphism.py
Hunk #1 FAILED at 294
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/jacobian_morphism.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_6545_mpolynomial_ideal_sorted_outputs.patch
```




---

archive/issue_comments_053375.json:
```json
{
    "body": "You can ignore this hunk failure it was also fixed in either #6596 or #6628. It was just this really annoying doctest failure which would crop up everytime one changes anything related to multivariate polynomial ideals.",
    "created_at": "2009-09-03T08:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53375",
    "user": "@malb"
}
```

You can ignore this hunk failure it was also fixed in either #6596 or #6628. It was just this really annoying doctest failure which would crop up everytime one changes anything related to multivariate polynomial ideals.



---

archive/issue_comments_053376.json:
```json
{
    "body": "rebased against Sage 4.1.2.alpha1",
    "created_at": "2009-09-09T06:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53376",
    "user": "mvngu"
}
```

rebased against Sage 4.1.2.alpha1



---

archive/issue_comments_053377.json:
```json
{
    "body": "Attachment [trac_6545-rebased.patch](tarball://root/attachments/some-uuid/ticket6545/trac_6545-rebased.patch) by mvngu created at 2009-09-09 06:04:43\n\nThe patch `trac_6545-rebased.patch` is a rebase of `trac_6545_mpolynomial_ideal_sorted_outputs.patch` against Sage 4.1.2.alpha1. The rebased patch is the same as the previous patch, but without this hunk:\n\n```\n--- jacobian_morphism.py                                                                                                                                                                                             \n+++ jacobian_morphism.py                                                                                                                                                                                             \n@@ -295,7 +295,7 @@\n         sage: H = HyperellipticCurve(f, 2*x); H                                                                                                                                                                     \n         Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1                                                                                        \n         sage: J = H.jacobian()(F); J                                                                                                                                                                                \n-        verbose 0 (919: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.                                                                                                \n+        verbose 0 (...: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.                                                                                                \n         Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 10000000000000000000000\\\n00000057                                                                                                                                                                                                             \n         sage: Q = J(H.lift_x(F(1))); Q                                                                                                                                                                              \n         (x + 1000000000000000000000000000056, y + 1000000000000000000000000000056)\n```\n",
    "created_at": "2009-09-09T06:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53377",
    "user": "mvngu"
}
```

Attachment [trac_6545-rebased.patch](tarball://root/attachments/some-uuid/ticket6545/trac_6545-rebased.patch) by mvngu created at 2009-09-09 06:04:43

The patch `trac_6545-rebased.patch` is a rebase of `trac_6545_mpolynomial_ideal_sorted_outputs.patch` against Sage 4.1.2.alpha1. The rebased patch is the same as the previous patch, but without this hunk:

```
--- jacobian_morphism.py                                                                                                                                                                                             
+++ jacobian_morphism.py                                                                                                                                                                                             
@@ -295,7 +295,7 @@
         sage: H = HyperellipticCurve(f, 2*x); H                                                                                                                                                                     
         Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1                                                                                        
         sage: J = H.jacobian()(F); J                                                                                                                                                                                
-        verbose 0 (919: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.                                                                                                
+        verbose 0 (...: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.                                                                                                
         Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 10000000000000000000000\
00000057                                                                                                                                                                                                             
         sage: Q = J(H.lift_x(F(1))); Q                                                                                                                                                                              
         (x + 1000000000000000000000000000056, y + 1000000000000000000000000000056)
```




---

archive/issue_comments_053378.json:
```json
{
    "body": "Merged `trac_6545-rebased.patch`.",
    "created_at": "2009-09-09T06:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53378",
    "user": "mvngu"
}
```

Merged `trac_6545-rebased.patch`.



---

archive/issue_comments_053379.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-09T06:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6545#issuecomment-53379",
    "user": "mvngu"
}
```

Resolution: fixed
