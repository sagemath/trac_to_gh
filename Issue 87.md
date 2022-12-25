# Issue 87: multivariable FractionField vs MPolynomial

archive/issues_000087.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  jdc@uwo.ca\n\nThis bug is a bit more subtle than I expected:\n\n--------------------------------------------------------\n--------------------------------------------------------\n| SAGE Version 1.3.7.3.3, Build Date: 2006-09-21       |\n| Distributed under the GNU General Public License V2. |\nsage: Qx=QQ['x']; x,=Qx.gens()\n\nsage: (1/x)*x                                                                  \n 1\n\nsage: Qyz=QQ['y,z']; y,z=Qyz.gens()                                            \n\nsage: (1/y)*y                                                                  \n 1\n\nsage: (y^2/y)*y                                                                \n---------------------------------------------------------------------------\nexceptions.TypeError                                 Traceback (most recent call last)\n\n/home/scratchy/math/me/CayleyDickson/python/symbolic/<ipython console> \n\n/home/scratchy/math/me/CayleyDickson/python/symbolic/element.pyx in element.RingElement.__mul__()\n\n/home/scratchy/math/me/CayleyDickson/python/symbolic/coerce.pyx in coerce.bin_op()\n\nTypeError: unable to find an unambiguous parent\n\nsage: type(1/y)                                                                \n <class 'sage.rings.fraction_field_element.FractionFieldElement'>\n\nsage: type(y^2/y)                                                              \n <class 'sage.rings.fraction_field_element.FractionFieldElement'>\n\nsage: type(y)                                                                  \n <class 'sage.rings.multi_polynomial_element.MPolynomial_polydict'>\n\nDan\n\nIssue created by migration from https://trac.sagemath.org/ticket/87\n\n",
    "created_at": "2006-09-26T21:22:36Z",
    "labels": [
        "component: algebraic geometry",
        "minor",
        "bug"
    ],
    "title": "multivariable FractionField vs MPolynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/87",
    "user": "https://github.com/jdchristensen"
}
```
Assignee: @williamstein

CC:  jdc@uwo.ca

This bug is a bit more subtle than I expected:

--------------------------------------------------------
--------------------------------------------------------
| SAGE Version 1.3.7.3.3, Build Date: 2006-09-21       |
| Distributed under the GNU General Public License V2. |
sage: Qx=QQ['x']; x,=Qx.gens()

sage: (1/x)*x                                                                  
 1

sage: Qyz=QQ['y,z']; y,z=Qyz.gens()                                            

sage: (1/y)*y                                                                  
 1

sage: (y^2/y)*y                                                                
---------------------------------------------------------------------------
exceptions.TypeError                                 Traceback (most recent call last)

/home/scratchy/math/me/CayleyDickson/python/symbolic/<ipython console> 

/home/scratchy/math/me/CayleyDickson/python/symbolic/element.pyx in element.RingElement.__mul__()

/home/scratchy/math/me/CayleyDickson/python/symbolic/coerce.pyx in coerce.bin_op()

TypeError: unable to find an unambiguous parent

sage: type(1/y)                                                                
 <class 'sage.rings.fraction_field_element.FractionFieldElement'>

sage: type(y^2/y)                                                              
 <class 'sage.rings.fraction_field_element.FractionFieldElement'>

sage: type(y)                                                                  
 <class 'sage.rings.multi_polynomial_element.MPolynomial_polydict'>

Dan

Issue created by migration from https://trac.sagemath.org/ticket/87





---

archive/issue_comments_000429.json:
```json
{
    "body": "It works fine now:\n\n\n```\n\nsage: Qyz=QQ['y,z']; y,z=Qyz.gens()\nsage: (1/y)*y\n1\nsage: (y^2/y)*y\ny^2\n```\n",
    "created_at": "2007-01-13T02:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/87",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/87#issuecomment-429",
    "user": "https://github.com/williamstein"
}
```

It works fine now:


```

sage: Qyz=QQ['y,z']; y,z=Qyz.gens()
sage: (1/y)*y
1
sage: (y^2/y)*y
y^2
```




---

archive/issue_comments_000430.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-13T02:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/87",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/87#issuecomment-430",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000087.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-13T02:16:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/87",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/87#event-87"
}
```
