# Issue 3809: reorder checks for creating a number field; prevents some silly errors

archive/issues_003809.json:
```json
{
    "body": "Assignee: was\n\nKeywords: number field check\n\nReordering the checks for creating a number field prevents such strange things as:\n\n\n```\nsage: x = GF(7)['x'].0\nsage: x.parent()\nUnivariate Polynomial Ring in x over Finite Field of size 7\nsage: x^4 + 23\nx^4 + 2\nsage: K.<a> = NumberField(x^4 + 23)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Users/ncalexan/sage-3.0.6/devel/sage-nca/<ipython console> in <module>()\n\n/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in NumberField(polynomial, name, check, names, cache)\n    278         K = NumberField_quadratic(polynomial, name, check)\n    279     else:\n--> 280         K = NumberField_absolute(polynomial, name, None, check)\n    281 \n    282     if cache:\n\n/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in __init__(self, polynomial, name, latex_name, check)\n   3219 \n   3220     def __init__(self, polynomial, name, latex_name=None, check=True):\n-> 3221         NumberField_generic.__init__(self, polynomial, name, latex_name, check)\n   3222         self._element_class = number_field_element.NumberFieldElement_absolute\n   3223 \n\n/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in __init__(self, polynomial, name, latex_name, check)\n    644         if check:\n    645             if not polynomial.is_irreducible():\n--> 646                 raise ValueError, \"defining polynomial (%s) must be irreducible\"%polynomial\n    647             if not polynomial.parent().base_ring() == QQ:\n    648                 raise TypeError, \"polynomial must be defined over rational field\"\n\nValueError: defining polynomial (x^4 + 2) must be irreducible\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3809\n\n",
    "created_at": "2008-08-12T04:48:24Z",
    "labels": [
        "number theory",
        "trivial",
        "enhancement"
    ],
    "title": "reorder checks for creating a number field; prevents some silly errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3809",
    "user": "ncalexan"
}
```
Assignee: was

Keywords: number field check

Reordering the checks for creating a number field prevents such strange things as:


```
sage: x = GF(7)['x'].0
sage: x.parent()
Univariate Polynomial Ring in x over Finite Field of size 7
sage: x^4 + 23
x^4 + 2
sage: K.<a> = NumberField(x^4 + 23)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/ncalexan/sage-3.0.6/devel/sage-nca/<ipython console> in <module>()

/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in NumberField(polynomial, name, check, names, cache)
    278         K = NumberField_quadratic(polynomial, name, check)
    279     else:
--> 280         K = NumberField_absolute(polynomial, name, None, check)
    281 
    282     if cache:

/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in __init__(self, polynomial, name, latex_name, check)
   3219 
   3220     def __init__(self, polynomial, name, latex_name=None, check=True):
-> 3221         NumberField_generic.__init__(self, polynomial, name, latex_name, check)
   3222         self._element_class = number_field_element.NumberFieldElement_absolute
   3223 

/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in __init__(self, polynomial, name, latex_name, check)
    644         if check:
    645             if not polynomial.is_irreducible():
--> 646                 raise ValueError, "defining polynomial (%s) must be irreducible"%polynomial
    647             if not polynomial.parent().base_ring() == QQ:
    648                 raise TypeError, "polynomial must be defined over rational field"

ValueError: defining polynomial (x^4 + 2) must be irreducible
```


Issue created by migration from https://trac.sagemath.org/ticket/3809





---

archive/issue_comments_027063.json:
```json
{
    "body": "Attachment [3809-ncalexan-number-field-checking.patch](tarball://root/attachments/some-uuid/ticket3809/3809-ncalexan-number-field-checking.patch) by ncalexan created at 2008-08-12 04:49:10",
    "created_at": "2008-08-12T04:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3809#issuecomment-27063",
    "user": "ncalexan"
}
```

Attachment [3809-ncalexan-number-field-checking.patch](tarball://root/attachments/some-uuid/ticket3809/3809-ncalexan-number-field-checking.patch) by ncalexan created at 2008-08-12 04:49:10



---

archive/issue_comments_027064.json:
```json
{
    "body": "Attachment [sage-3809-referee.patch](tarball://root/attachments/some-uuid/ticket3809/sage-3809-referee.patch) by was created at 2008-08-13 02:31:52",
    "created_at": "2008-08-13T02:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3809#issuecomment-27064",
    "user": "was"
}
```

Attachment [sage-3809-referee.patch](tarball://root/attachments/some-uuid/ticket3809/sage-3809-referee.patch) by was created at 2008-08-13 02:31:52



---

archive/issue_comments_027065.json:
```json
{
    "body": "The referee patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-13T08:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3809#issuecomment-27065",
    "user": "mabshoff"
}
```

The referee patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_027066.json:
```json
{
    "body": "Merged both patches in Sage 3.1.alpha2",
    "created_at": "2008-08-13T08:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3809#issuecomment-27066",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.1.alpha2



---

archive/issue_comments_027067.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-13T08:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3809#issuecomment-27067",
    "user": "mabshoff"
}
```

Resolution: fixed
