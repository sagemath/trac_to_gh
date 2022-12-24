# Issue 6063: x^2 for x over QQ is really frickin' slow compared to over ZZ (nearly factor of 100!!)

archive/issues_006063.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nwstein@sage:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: R.<x> = ZZ[]\nsage: timeit('x^2')\n625 loops, best of 3: 1.4 \u00b5s per loop\nsage: R.<x> = QQ[]\nsage: timeit('x^2')\n625 loops, best of 3: 118 \u00b5s per loop\nsage: %prun x**2\n         34 function calls in 0.001 CPU seconds\n| Sage Version 3.4.1, Release Date: 2009-04-21                       |\n| Type notebook() for the GUI, and license() for information.        |\n   Ordered by: internal time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.000    0.000    0.001    0.001 <string>:1(<module>)\n        1    0.000    0.000    0.000    0.000 polynomial_element_generic.py:590(__init__)\n        4    0.000    0.000    0.000    0.000 polynomial_element_generic.py:656(__getitem__)\n        3    0.000    0.000    0.000    0.000 {method 'poldegree' of 'sage.libs.pari.gen.gen' objects}\n        3    0.000    0.000    0.000    0.000 polynomial_element_generic.py:874(degree)\n        2    0.000    0.000    0.000    0.000 {method 'Polrev' of 'sage.libs.pari.gen.gen' objects}\n        1    0.000    0.000    0.000    0.000 polynomial_ring.py:211(_element_constructor_)\n        1    0.000    0.000    0.000    0.000 polynomial_ring.py:741(gen)\n        9    0.000    0.000    0.000    0.000 {isinstance}\n        3    0.000    0.000    0.000    0.000 {max}\n        1    0.000    0.000    0.000    0.000 {hasattr}\n        1    0.000    0.000    0.000    0.000 polynomial_ring.py:810(is_sparse)\n        1    0.000    0.000    0.000    0.000 {method 'type' of 'sage.libs.pari.gen.gen' objects}\n        1    0.000    0.000    0.000    0.000 {len}\n        1    0.000    0.000    0.000    0.000 {sage.rings.fraction_field_element.is_FractionFieldElement}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n\nsage: R.<x> = ZZ[]\nsage: %prun x**2\n         3 function calls in 0.000 CPU seconds\n\n   Ordered by: internal time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.000    0.000    0.000    0.000 <string>:1(<module>)\n        1    0.000    0.000    0.000    0.000 polynomial_ring.py:741(gen)\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6063\n\n",
    "created_at": "2009-05-18T05:28:40Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "x^2 for x over QQ is really frickin' slow compared to over ZZ (nearly factor of 100!!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6063",
    "user": "was"
}
```
Assignee: somebody


```
wstein@sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x> = ZZ[]
sage: timeit('x^2')
625 loops, best of 3: 1.4 µs per loop
sage: R.<x> = QQ[]
sage: timeit('x^2')
625 loops, best of 3: 118 µs per loop
sage: %prun x**2
         34 function calls in 0.001 CPU seconds
| Sage Version 3.4.1, Release Date: 2009-04-21                       |
| Type notebook() for the GUI, and license() for information.        |
   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 polynomial_element_generic.py:590(__init__)
        4    0.000    0.000    0.000    0.000 polynomial_element_generic.py:656(__getitem__)
        3    0.000    0.000    0.000    0.000 {method 'poldegree' of 'sage.libs.pari.gen.gen' objects}
        3    0.000    0.000    0.000    0.000 polynomial_element_generic.py:874(degree)
        2    0.000    0.000    0.000    0.000 {method 'Polrev' of 'sage.libs.pari.gen.gen' objects}
        1    0.000    0.000    0.000    0.000 polynomial_ring.py:211(_element_constructor_)
        1    0.000    0.000    0.000    0.000 polynomial_ring.py:741(gen)
        9    0.000    0.000    0.000    0.000 {isinstance}
        3    0.000    0.000    0.000    0.000 {max}
        1    0.000    0.000    0.000    0.000 {hasattr}
        1    0.000    0.000    0.000    0.000 polynomial_ring.py:810(is_sparse)
        1    0.000    0.000    0.000    0.000 {method 'type' of 'sage.libs.pari.gen.gen' objects}
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {sage.rings.fraction_field_element.is_FractionFieldElement}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

sage: R.<x> = ZZ[]
sage: %prun x**2
         3 function calls in 0.000 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 polynomial_ring.py:741(gen)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

```


Issue created by migration from https://trac.sagemath.org/ticket/6063





---

archive/issue_comments_048259.json:
```json
{
    "body": "See also #4000, which might be the best way to fix this.",
    "created_at": "2009-07-13T13:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6063#issuecomment-48259",
    "user": "AlexGhitza"
}
```

See also #4000, which might be the best way to fix this.



---

archive/issue_comments_048260.json:
```json
{
    "body": "This is because polynomials over QQ are still pure Python.   This is an enhancement, not a bug.",
    "created_at": "2010-01-18T01:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6063#issuecomment-48260",
    "user": "was"
}
```

This is because polynomials over QQ are still pure Python.   This is an enhancement, not a bug.



---

archive/issue_comments_048261.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-01-18T01:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6063#issuecomment-48261",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_048262.json:
```json
{
    "body": "This appears to be fixed now - the QQ one is even slightly faster.",
    "created_at": "2011-01-21T22:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6063#issuecomment-48262",
    "user": "jrp"
}
```

This appears to be fixed now - the QQ one is even slightly faster.



---

archive/issue_comments_048263.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-22T15:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6063#issuecomment-48263",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_048264.json:
```json
{
    "body": "Yes, this is fixed. Release manager: please close this ticket.",
    "created_at": "2011-01-22T15:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6063#issuecomment-48264",
    "user": "davidloeffler"
}
```

Yes, this is fixed. Release manager: please close this ticket.



---

archive/issue_comments_048265.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-22T15:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6063#issuecomment-48265",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_048266.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-01-22T19:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6063#issuecomment-48266",
    "user": "jdemeyer"
}
```

Resolution: duplicate
