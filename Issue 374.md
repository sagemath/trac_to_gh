# Issue 374: Bug in factorization of polynomial over number field

archive/issues_000374.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nx = polygen(QQ, 'x')\nf = x^6 + 10/7*x^5 - 867/49*x^4 - 76/245*x^3 + 3148/35*x^2 - 25944/245*x + 48771/1225\n```\n\n\n\n```\nlegendre_symbol(-7,73)\n///\n-1\n```\n\n\n\n```\nf.factor_mod(73)\n///\n(x^2 + 12*x + 47) * (x^2 + 15*x + 21) * (x^2 + 37*x + 21)\n```\n\n\n\n```\nK.<a> = NumberField(f/1225)\nS.<T> = K[]\nff = S(f)\nprint ff\n///\n1225*T^6 + 1750*T^5 + (-21675)*T^4 + (-380)*T^3 + 110180*T^2 + (-129720)*T + 48771\n```\n\n\n\n```\nff.factor()\n///\nMulMod: bad args\nAborted\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/374\n\n",
    "created_at": "2007-05-23T01:56:09Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Bug in factorization of polynomial over number field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/374",
    "user": "was"
}
```
Assignee: somebody


```
x = polygen(QQ, 'x')
f = x^6 + 10/7*x^5 - 867/49*x^4 - 76/245*x^3 + 3148/35*x^2 - 25944/245*x + 48771/1225
```



```
legendre_symbol(-7,73)
///
-1
```



```
f.factor_mod(73)
///
(x^2 + 12*x + 47) * (x^2 + 15*x + 21) * (x^2 + 37*x + 21)
```



```
K.<a> = NumberField(f/1225)
S.<T> = K[]
ff = S(f)
print ff
///
1225*T^6 + 1750*T^5 + (-21675)*T^4 + (-380)*T^3 + 110180*T^2 + (-129720)*T + 48771
```



```
ff.factor()
///
MulMod: bad args
Aborted
```



Issue created by migration from https://trac.sagemath.org/ticket/374





---

archive/issue_comments_001784.json:
```json
{
    "body": "This was fixed by Joel Mohler's latest patch.",
    "created_at": "2007-05-31T14:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/374#issuecomment-1784",
    "user": "was"
}
```

This was fixed by Joel Mohler's latest patch.



---

archive/issue_comments_001785.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-05-31T14:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/374#issuecomment-1785",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_001786.json:
```json
{
    "body": "Actually #374 can be removed, because creating number fields with non-monic polys is no longer supported.\n\n\n\n```\nsage: x = polygen(QQ, 'x')\nsage: f = x^6 + 10/7*x^5 - 867/49*x^4 - 76/245*x^3 + 3148/35*x^2 - 25944/245*x + 48771/1225\nsage: K.<a> = NumberField(f/1225)\nsage: S.<T> = K[]\nsage: ff = S(f)\nsage: print ff\nsage: 1225*T^6 + 1750*T^5 + (-21675)*T^4 + (-380)*T^3 + 110180*T^2 + (-129720)*T + 48771\nTraceback (most recent call last):\n...\nNotImplementedError: number fields for non-monic polynomials not yet implemented.\n```\n",
    "created_at": "2007-08-19T06:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/374#issuecomment-1786",
    "user": "was"
}
```

Actually #374 can be removed, because creating number fields with non-monic polys is no longer supported.



```
sage: x = polygen(QQ, 'x')
sage: f = x^6 + 10/7*x^5 - 867/49*x^4 - 76/245*x^3 + 3148/35*x^2 - 25944/245*x + 48771/1225
sage: K.<a> = NumberField(f/1225)
sage: S.<T> = K[]
sage: ff = S(f)
sage: print ff
sage: 1225*T^6 + 1750*T^5 + (-21675)*T^4 + (-380)*T^3 + 110180*T^2 + (-129720)*T + 48771
Traceback (most recent call last):
...
NotImplementedError: number fields for non-monic polynomials not yet implemented.
```

