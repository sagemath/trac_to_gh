# Issue 2502: [with patch, needs review] doctest coverage for finite fields

archive/issues_002502.json:
```json
{
    "body": "Assignee: failure\n\n**Before patch:**\n\n```\n----------------------------------------------------------------------\nfinite_field_givaro.pyx\nSCORE finite_field_givaro.pyx: 100% (61 of 61)\n----------------------------------------------------------------------\n\n----------------------------------------------------------------------\nfinite_field_ntl_gf2e.pyx\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE finite_field_ntl_gf2e.pyx: 64% (25 of 39)\n\nMissing documentation:\n         * __init__(FiniteField_ntl_gf2e self, q, names=\"a\", modulus=None, repr=\"poly\")\n         * __richcmp__(left, right, int op)\n         * _pari_(self, var=None)\n         * unpickleFiniteField_ntl_gf2eElement(parent, elem)\n\n\nMissing doctests:\n         * __neg__(FiniteField_ntl_gf2eElement self)\n         * __invert__(FiniteField_ntl_gf2eElement self)\n         * polynomial(FiniteField_ntl_gf2eElement self, name=None)\n         * _finite_field_ext_pari_element(FiniteField_ntl_gf2eElement self, k=None)\n         * _magma_init_(self)\n         * __copy__(self)\n         * _gap_init_(self)\n         * __hash__(FiniteField_ntl_gf2eElement self)\n         * vector(FiniteField_ntl_gf2eElement self, reverse=False)\n         * __reduce__(FiniteField_ntl_gf2eElement self)\n\n----------------------------------------------------------------------\n\n----------------------------------------------------------------------\nfinite_field_prime_modn.py\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE finite_field_prime_modn.py: 91% (11 of 12)\n\nMissing doctests:\n         * polynomial(self, name=None)\n\n----------------------------------------------------------------------\n\n----------------------------------------------------------------------\nfinite_field.py\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE finite_field.py: 100% (4 of 4)\n----------------------------------------------------------------------\n```\n\n\n**After patch:**\n\n\n```\n----------------------------------------------------------------------\nfinite_field_ext_pari.py\nSCORE finite_field_ext_pari.py: 100% (14 of 14)\n----------------------------------------------------------------------\n\n----------------------------------------------------------------------\nfinite_field_givaro.pyx\nSCORE finite_field_givaro.pyx: 100% (61 of 61)\n----------------------------------------------------------------------\n\n----------------------------------------------------------------------\nfinite_field_ntl_gf2e.pyx\nSCORE finite_field_ntl_gf2e.pyx: 100% (39 of 39)\n----------------------------------------------------------------------\n\n----------------------------------------------------------------------\nfinite_field_prime_modn.py\nSCORE finite_field_prime_modn.py: 100% (12 of 12)\n----------------------------------------------------------------------\n\n----------------------------------------------------------------------\nfinite_field.py\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE finite_field.py: 100% (4 of 4)\n----------------------------------------------------------------------\n```\n\n\nNote that the last \"Please define a s == loads(dumps(s)) doctest.\" is wrong. There is no class defined in `finite_field.py`.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2502\n\n",
    "created_at": "2008-03-12T19:02:32Z",
    "labels": [
        "doctest coverage",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, needs review] doctest coverage for finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2502",
    "user": "@malb"
}
```
Assignee: failure

**Before patch:**

```
----------------------------------------------------------------------
finite_field_givaro.pyx
SCORE finite_field_givaro.pyx: 100% (61 of 61)
----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field_ntl_gf2e.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE finite_field_ntl_gf2e.pyx: 64% (25 of 39)

Missing documentation:
         * __init__(FiniteField_ntl_gf2e self, q, names="a", modulus=None, repr="poly")
         * __richcmp__(left, right, int op)
         * _pari_(self, var=None)
         * unpickleFiniteField_ntl_gf2eElement(parent, elem)


Missing doctests:
         * __neg__(FiniteField_ntl_gf2eElement self)
         * __invert__(FiniteField_ntl_gf2eElement self)
         * polynomial(FiniteField_ntl_gf2eElement self, name=None)
         * _finite_field_ext_pari_element(FiniteField_ntl_gf2eElement self, k=None)
         * _magma_init_(self)
         * __copy__(self)
         * _gap_init_(self)
         * __hash__(FiniteField_ntl_gf2eElement self)
         * vector(FiniteField_ntl_gf2eElement self, reverse=False)
         * __reduce__(FiniteField_ntl_gf2eElement self)

----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field_prime_modn.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE finite_field_prime_modn.py: 91% (11 of 12)

Missing doctests:
         * polynomial(self, name=None)

----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE finite_field.py: 100% (4 of 4)
----------------------------------------------------------------------
```


**After patch:**


```
----------------------------------------------------------------------
finite_field_ext_pari.py
SCORE finite_field_ext_pari.py: 100% (14 of 14)
----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field_givaro.pyx
SCORE finite_field_givaro.pyx: 100% (61 of 61)
----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field_ntl_gf2e.pyx
SCORE finite_field_ntl_gf2e.pyx: 100% (39 of 39)
----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field_prime_modn.py
SCORE finite_field_prime_modn.py: 100% (12 of 12)
----------------------------------------------------------------------

----------------------------------------------------------------------
finite_field.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE finite_field.py: 100% (4 of 4)
----------------------------------------------------------------------
```


Note that the last "Please define a s == loads(dumps(s)) doctest." is wrong. There is no class defined in `finite_field.py`.



Issue created by migration from https://trac.sagemath.org/ticket/2502





---

archive/issue_comments_016955.json:
```json
{
    "body": "Attachment [gf_doctests.patch](tarball://root/attachments/some-uuid/ticket2502/gf_doctests.patch) by @malb created at 2008-03-12 19:03:03\n\nnote that finite_field_element.py is not addressed in this patch",
    "created_at": "2008-03-12T19:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2502#issuecomment-16955",
    "user": "@malb"
}
```

Attachment [gf_doctests.patch](tarball://root/attachments/some-uuid/ticket2502/gf_doctests.patch) by @malb created at 2008-03-12 19:03:03

note that finite_field_element.py is not addressed in this patch



---

archive/issue_comments_016956.json:
```json
{
    "body": "Works for me. All test passed.\n\nNo surprises in the code.\n\nJaap",
    "created_at": "2008-03-14T16:09:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2502#issuecomment-16956",
    "user": "@jaapspies"
}
```

Works for me. All test passed.

No surprises in the code.

Jaap



---

archive/issue_comments_016957.json:
```json
{
    "body": "Merged in Sage 2.10.4.rc0",
    "created_at": "2008-03-15T19:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2502#issuecomment-16957",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.rc0



---

archive/issue_comments_016958.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T19:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2502#issuecomment-16958",
    "user": "mabshoff"
}
```

Resolution: fixed
