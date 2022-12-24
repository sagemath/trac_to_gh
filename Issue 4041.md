# Issue 4041: Implementing non-monic number fields

archive/issues_004041.json:
```json
{
    "body": "Assignee: was\n\nImplementing non-monic number fields would be hard, but not if the   \nleading coefficient is a unit :)\n\n```\nsage: NumberField(x^2 - 2, 'a') \nNumber Field in a with defining polynomial x^2 - 2 \nsage: NumberField(-x^2 - 2, 'a') \n--------------------------------------------------------------------------- \nNotImplementedError                       Traceback (most recent call   \nlast) \n/Users/ncalexan/Devel/Squeak-3.10-1/platforms/unix/bld/<ipython   \nconsole> in <module>() \n/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/ \nrings/number_field/number_field.py in NumberField(polynomial, name,   \ncheck, names, cache) \n     288 \n     289     if polynomial.degree() == 2: \n--> 290         K = NumberField_quadratic(polynomial, name, check) \n     291     else: \n     292         K = NumberField_absolute(polynomial, name, None, check) \n/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/ \nrings/number_field/number_field.py in __init__(self, polynomial, name,   \ncheck) \n    6001             Number Field in a with defining polynomial x^2 - 4 \n    6002         \"\"\" \n-> 6003         NumberField_absolute.__init__(self, polynomial,   \nname=name, check=check) \n    6004         self._element_class =   \nnumber_field_element_quadratic.NumberFieldElement_quadratic \n    6005         c, b, a = [rational.Rational(t) for t in   \nself.defining_polynomial().list()] \n/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/ \nrings/number_field/number_field.py in __init__(self, polynomial, name,   \nlatex_name, check) \n    3272 \n    3273     def __init__(self, polynomial, name, latex_name=None,   \ncheck=True): \n-> 3274         NumberField_generic.__init__(self, polynomial, name,   \nlatex_name, check) \n    3275         self._element_class =   \nnumber_field_element.NumberFieldElement_absolute \n    3276 \n/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/ \nrings/number_field/number_field.py in __init__(self, polynomial, name,   \nlatex_name, check) \n     668                 raise TypeError, \"polynomial must be defined   \nover rational field\" \n     669             if not polynomial.is_monic(): \n--> 670                 raise NotImplementedError, \"number fields for   \nnon-monic polynomials not yet implemented.\" \n     671             if not polynomial.is_irreducible(): \n     672                 raise ValueError, \"defining polynomial (%s)   \nmust be irreducible\"%polynomial \nNotImplementedError: number fields for non-monic polynomials not yet   \nimplemented. \n```\n \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4041\n\n",
    "created_at": "2008-09-02T20:40:36Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Implementing non-monic number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4041",
    "user": "mabshoff"
}
```
Assignee: was

Implementing non-monic number fields would be hard, but not if the   
leading coefficient is a unit :)

```
sage: NumberField(x^2 - 2, 'a') 
Number Field in a with defining polynomial x^2 - 2 
sage: NumberField(-x^2 - 2, 'a') 
--------------------------------------------------------------------------- 
NotImplementedError                       Traceback (most recent call   
last) 
/Users/ncalexan/Devel/Squeak-3.10-1/platforms/unix/bld/<ipython   
console> in <module>() 
/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/ 
rings/number_field/number_field.py in NumberField(polynomial, name,   
check, names, cache) 
     288 
     289     if polynomial.degree() == 2: 
--> 290         K = NumberField_quadratic(polynomial, name, check) 
     291     else: 
     292         K = NumberField_absolute(polynomial, name, None, check) 
/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/ 
rings/number_field/number_field.py in __init__(self, polynomial, name,   
check) 
    6001             Number Field in a with defining polynomial x^2 - 4 
    6002         """ 
-> 6003         NumberField_absolute.__init__(self, polynomial,   
name=name, check=check) 
    6004         self._element_class =   
number_field_element_quadratic.NumberFieldElement_quadratic 
    6005         c, b, a = [rational.Rational(t) for t in   
self.defining_polynomial().list()] 
/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/ 
rings/number_field/number_field.py in __init__(self, polynomial, name,   
latex_name, check) 
    3272 
    3273     def __init__(self, polynomial, name, latex_name=None,   
check=True): 
-> 3274         NumberField_generic.__init__(self, polynomial, name,   
latex_name, check) 
    3275         self._element_class =   
number_field_element.NumberFieldElement_absolute 
    3276 
/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/ 
rings/number_field/number_field.py in __init__(self, polynomial, name,   
latex_name, check) 
     668                 raise TypeError, "polynomial must be defined   
over rational field" 
     669             if not polynomial.is_monic(): 
--> 670                 raise NotImplementedError, "number fields for   
non-monic polynomials not yet implemented." 
     671             if not polynomial.is_irreducible(): 
     672                 raise ValueError, "defining polynomial (%s)   
must be irreducible"%polynomial 
NotImplementedError: number fields for non-monic polynomials not yet   
implemented. 
```
 


Issue created by migration from https://trac.sagemath.org/ticket/4041





---

archive/issue_comments_029145.json:
```json
{
    "body": "It's not clear to me exactly what Nick means: defining polys in Z[x] with leading coefficient -1, or something more general over Q, or also relative number fields.",
    "created_at": "2008-09-02T21:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4041#issuecomment-29145",
    "user": "cremona"
}
```

It's not clear to me exactly what Nick means: defining polys in Z[x] with leading coefficient -1, or something more general over Q, or also relative number fields.



---

archive/issue_comments_029146.json:
```json
{
    "body": "This ticket seems to be a duplicate of #252.  So I think this one can be deleted.",
    "created_at": "2008-09-04T15:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4041#issuecomment-29146",
    "user": "cremona"
}
```

This ticket seems to be a duplicate of #252.  So I think this one can be deleted.



---

archive/issue_comments_029147.json:
```json
{
    "body": "As John pointed out this is a dupe of #252, so close this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T17:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4041#issuecomment-29147",
    "user": "mabshoff"
}
```

As John pointed out this is a dupe of #252, so close this ticket.

Cheers,

Michael



---

archive/issue_comments_029148.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-04T17:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4041#issuecomment-29148",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029149.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-09-04T17:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4041#issuecomment-29149",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_029150.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-09-04T17:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4041#issuecomment-29150",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_029151.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-09-04T17:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4041#issuecomment-29151",
    "user": "mabshoff"
}
```

Resolution: duplicate
