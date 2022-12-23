# Issue 1007: Cyclotomic polynomial broken

archive/issues_001007.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: QQ['x'].cyclotomic_polynomial(12)\nx^4 - x^2 + 1\nsage: ZZ['x'].cyclotomic_polynomial(12)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/robert/<ipython console> in <module>()\n\n/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in cyclotomic_polynomial(self, n)\n    559         coeffs = str(f.Vec())\n    560         if C == polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl:\n--> 561             return self(coeffs, construct=True)\n    562 \n    563         coeffs = eval(coeffs)\n\n/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in __call__(self, x, check, is_gen, construct, absprec)\n    239         C = self.__polynomial_class\n    240         if absprec is None:\n--> 241             return C(self, x, check, is_gen, construct=construct)\n    242         else:\n    243             return C(self, x, check, is_gen, construct=construct, absprec = absprec)\n\n/Users/robert/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.__init__()\n\n/Users/robert/integer.pyx in sage.rings.integer.Integer.__init__()\n\n<type 'exceptions.TypeError'>: unable to convert x (=[1, 0, -1, 0, 1]) to an integer\n```\n\n\nI am sure we can do much better than just calling Pari, maybe even using Andrew Arnold's code. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1007\n\n",
    "created_at": "2007-10-27T01:52:01Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Cyclotomic polynomial broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1007",
    "user": "robertwb"
}
```
Assignee: was


```
sage: QQ['x'].cyclotomic_polynomial(12)
x^4 - x^2 + 1
sage: ZZ['x'].cyclotomic_polynomial(12)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/robert/<ipython console> in <module>()

/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in cyclotomic_polynomial(self, n)
    559         coeffs = str(f.Vec())
    560         if C == polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl:
--> 561             return self(coeffs, construct=True)
    562 
    563         coeffs = eval(coeffs)

/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in __call__(self, x, check, is_gen, construct, absprec)
    239         C = self.__polynomial_class
    240         if absprec is None:
--> 241             return C(self, x, check, is_gen, construct=construct)
    242         else:
    243             return C(self, x, check, is_gen, construct=construct, absprec = absprec)

/Users/robert/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.__init__()

/Users/robert/integer.pyx in sage.rings.integer.Integer.__init__()

<type 'exceptions.TypeError'>: unable to convert x (=[1, 0, -1, 0, 1]) to an integer
```


I am sure we can do much better than just calling Pari, maybe even using Andrew Arnold's code. 

Issue created by migration from https://trac.sagemath.org/ticket/1007





---

archive/issue_comments_006157.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-27T10:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1007#issuecomment-6157",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_006158.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2007-10-27T10:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1007#issuecomment-6158",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_006159.json:
```json
{
    "body": "As well as fixing broken ZZ[x], we have before\n\n```\nsage: time f = pari.polcyclo(5*7*13*100)\nCPU time: 0.18 s,  Wall time: 0.19 s\nsage: time f = pari.polcyclo(5*7*13*1000)\nCPU time: 14.68 s,  Wall time: 14.75 s\n```\n\nafter\n\n```\nsage: time f = ZZ['x'].cyclotomic_polynomial(5*7*13*100)\nCPU time: 0.02 s,  Wall time: 0.02 s\nsage: time f = ZZ['x'].cyclotomic_polynomial(5*7*13*1000)\nCPU time: 1.01 s,  Wall time: 1.02 s\n```\n\nNote that 99% of the time is spent in polynomial construction overhead\n\n```\nsage: from sage.rings.polynomial.cyclotomic import cyclotomic_coeffs\nsage: time v = cyclotomic_coeffs(5*7*13*1000)\nCPU time: 0.01 s,  Wall time: 0.01 s\n```\n",
    "created_at": "2007-10-27T10:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1007#issuecomment-6159",
    "user": "robertwb"
}
```

As well as fixing broken ZZ[x], we have before

```
sage: time f = pari.polcyclo(5*7*13*100)
CPU time: 0.18 s,  Wall time: 0.19 s
sage: time f = pari.polcyclo(5*7*13*1000)
CPU time: 14.68 s,  Wall time: 14.75 s
```

after

```
sage: time f = ZZ['x'].cyclotomic_polynomial(5*7*13*100)
CPU time: 0.02 s,  Wall time: 0.02 s
sage: time f = ZZ['x'].cyclotomic_polynomial(5*7*13*1000)
CPU time: 1.01 s,  Wall time: 1.02 s
```

Note that 99% of the time is spent in polynomial construction overhead

```
sage: from sage.rings.polynomial.cyclotomic import cyclotomic_coeffs
sage: time v = cyclotomic_coeffs(5*7*13*1000)
CPU time: 0.01 s,  Wall time: 0.01 s
```




---

archive/issue_comments_006160.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T19:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1007#issuecomment-6160",
    "user": "cwitty"
}
```

Resolution: fixed
