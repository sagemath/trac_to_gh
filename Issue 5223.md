# Issue 5223: [with patch; needs review] silly bug in flint wrapper makes it a factor of 10 slower for division of a polynomial by an integer

archive/issues_005223.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  roed\n\nBEFORE:\n\n```\nsage: R.<x> = ZZ['x']\nsage: f = 389*R.random_element(1000)\nsage: timeit('f//389')\n625 loops, best of 3: 228 \u00b5s per loop\n```\n\n\nAFTER:\n\n```\nsage: R.<x> = ZZ['x']\nsage: f = 389*R.random_element(1000)\nsage: timeit('f//389')\n625 loops, best of 3: 48.3 \u00b5s per loop\n```\n\n\nThe bug was doing the shortcut case, but then not returning and hence doing the long case *as well*.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5223\n\n",
    "created_at": "2009-02-09T20:03:19Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] silly bug in flint wrapper makes it a factor of 10 slower for division of a polynomial by an integer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5223",
    "user": "was"
}
```
Assignee: somebody

CC:  roed

BEFORE:

```
sage: R.<x> = ZZ['x']
sage: f = 389*R.random_element(1000)
sage: timeit('f//389')
625 loops, best of 3: 228 µs per loop
```


AFTER:

```
sage: R.<x> = ZZ['x']
sage: f = 389*R.random_element(1000)
sage: timeit('f//389')
625 loops, best of 3: 48.3 µs per loop
```


The bug was doing the shortcut case, but then not returning and hence doing the long case *as well*.



Issue created by migration from https://trac.sagemath.org/ticket/5223





---

archive/issue_comments_040028.json:
```json
{
    "body": "Attachment\n\nPatch looks good. Fixes obvious mistake on my part. :)",
    "created_at": "2009-02-09T20:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5223#issuecomment-40028",
    "user": "burcin"
}
```

Attachment

Patch looks good. Fixes obvious mistake on my part. :)



---

archive/issue_comments_040029.json:
```json
{
    "body": "This patch causes the following doctest failure:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.3.rc0$ ./sage -t -long devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py\nsage -t -long \"devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py\", line 592:\n    sage: b = a.rshift_coeffs(1); b\nExpected:\n    (O(13^3))*t^2 + (1 + O(13^2))*t + (13 + O(13^5))\nGot:\n    (O(13^3))*t^2 + (9 + 8*13 + O(13^2))*t + (7 + 12*13 + 7*13^2 + 6*13^3 + O(13^4))\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py\", line 594:\n    sage: b.list()\nExpected:\n    [13 + O(13^5), 1 + O(13^2), O(13^3)]\nGot:\n    [7 + 12*13 + 7*13^2 + 6*13^3 + O(13^4), 9 + 8*13 + O(13^2), O(13^3)]\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py\", line 596:\n    sage: b = a.rshift_coeffs(2); b\nExpected:\n    (O(13^2))*t^2 + (O(13))*t + (1 + O(13^4))\nGot:\n    (O(13^2))*t^2 + (7 + O(13))*t + (8 + 3*13 + 10*13^2 + 9*13^3 + O(13^4))\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py\", line 598:\n    sage: b.list()\nExpected:\n    [1 + O(13^4), O(13), O(13^2)]\nGot:\n    [8 + 3*13 + 10*13^2 + 9*13^3 + O(13^4), 7 + O(13), O(13^2)]\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-10T07:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5223#issuecomment-40029",
    "user": "mabshoff"
}
```

This patch causes the following doctest failure:

```
mabshoff@sage:/scratch/mabshoff/sage-3.3.rc0$ ./sage -t -long devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py
sage -t -long "devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py", line 592:
    sage: b = a.rshift_coeffs(1); b
Expected:
    (O(13^3))*t^2 + (1 + O(13^2))*t + (13 + O(13^5))
Got:
    (O(13^3))*t^2 + (9 + 8*13 + O(13^2))*t + (7 + 12*13 + 7*13^2 + 6*13^3 + O(13^4))
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py", line 594:
    sage: b.list()
Expected:
    [13 + O(13^5), 1 + O(13^2), O(13^3)]
Got:
    [7 + 12*13 + 7*13^2 + 6*13^3 + O(13^4), 9 + 8*13 + O(13^2), O(13^3)]
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py", line 596:
    sage: b = a.rshift_coeffs(2); b
Expected:
    (O(13^2))*t^2 + (O(13))*t + (1 + O(13^4))
Got:
    (O(13^2))*t^2 + (7 + O(13))*t + (8 + 3*13 + 10*13^2 + 9*13^3 + O(13^4))
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc0/devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py", line 598:
    sage: b.list()
Expected:
    [1 + O(13^4), O(13), O(13^2)]
Got:
    [8 + 3*13 + 10*13^2 + 9*13^3 + O(13^4), 7 + O(13), O(13^2)]
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_040030.json:
```json
{
    "body": "Bumped to 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T07:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5223#issuecomment-40030",
    "user": "mabshoff"
}
```

Bumped to 3.4.1.

Cheers,

Michael



---

archive/issue_comments_040031.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-15T13:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5223#issuecomment-40031",
    "user": "burcin"
}
```

Attachment



---

archive/issue_comments_040032.json:
```json
{
    "body": "Wrong function was called for scalar division in the existing code, so we returned wrong results if division was not exact. Using `fmpz_poly_scalar_div_mpz()` fixes this problem and removes the limit on the size of the divisor. I didn't measure it's effects on speed.\n\nAll tests under sage/rings/polynomial pass with attachment:trac_5223.take2.patch.",
    "created_at": "2009-03-15T13:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5223#issuecomment-40032",
    "user": "burcin"
}
```

Wrong function was called for scalar division in the existing code, so we returned wrong results if division was not exact. Using `fmpz_poly_scalar_div_mpz()` fixes this problem and removes the limit on the size of the divisor. I didn't measure it's effects on speed.

All tests under sage/rings/polynomial pass with attachment:trac_5223.take2.patch.



---

archive/issue_comments_040033.json:
```json
{
    "body": "Changing assignee from somebody to burcin.",
    "created_at": "2009-03-15T13:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5223#issuecomment-40033",
    "user": "burcin"
}
```

Changing assignee from somebody to burcin.



---

archive/issue_comments_040034.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-15T13:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5223#issuecomment-40034",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040035.json:
```json
{
    "body": "Looks good to me, even gets the degree right when the higher terms are truncated away.",
    "created_at": "2009-03-17T00:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5223#issuecomment-40035",
    "user": "robertwb"
}
```

Looks good to me, even gets the degree right when the higher terms are truncated away.



---

archive/issue_comments_040036.json:
```json
{
    "body": "Merged trac_5223.take2.patch in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-20T20:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5223#issuecomment-40036",
    "user": "mabshoff"
}
```

Merged trac_5223.take2.patch in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_040037.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-20T20:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5223#issuecomment-40037",
    "user": "mabshoff"
}
```

Resolution: fixed
