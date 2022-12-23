# Issue 1294: v.n() function blows up when v is a vector

archive/issues_001294.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: v=vector(QQ,[1,2,3])\nsage: v.n()\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/grout/sage/devel/sage-main/sage/graphs/<ipython console> in <module>()\n\n/home/grout/sage/devel/sage-main/sage/graphs/element.pyx in sage.structure.element.Element.n()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/misc/functional.py in numerical_approx(x, prec, digits)\n    731             return sage.rings.real_mpfr.RealField(prec)(x)\n    732         except TypeError:\n--> 733             return sage.rings.complex_field.ComplexField(prec)(x)\n    734\n    735 n = numerical_approx\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/rings/complex_field.py in __call__(self, x, im)\n    179             except AttributeError:\n    180                 pass\n--> 181         return complex_number.ComplexNumber(self, x, im)\n    182\n    183     def _coerce_impl(self, x):\n\n/home/grout/sage/devel/sage-main/sage/graphs/complex_number.pyx in sage.rings.complex_number.ComplexNumber.__init__()\n\n<type 'exceptions.TypeError'>: unable to coerce to a ComplexNumber\n```\n\n\nI'm not sure what it should do, but maybe call n() on each entry would make sense.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1294\n\n",
    "created_at": "2007-11-27T23:13:24Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "v.n() function blows up when v is a vector",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1294",
    "user": "jason"
}
```
Assignee: was


```
sage: v=vector(QQ,[1,2,3])
sage: v.n()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/graphs/<ipython console> in <module>()

/home/grout/sage/devel/sage-main/sage/graphs/element.pyx in sage.structure.element.Element.n()

/home/grout/sage/local/lib/python2.5/site-packages/sage/misc/functional.py in numerical_approx(x, prec, digits)
    731             return sage.rings.real_mpfr.RealField(prec)(x)
    732         except TypeError:
--> 733             return sage.rings.complex_field.ComplexField(prec)(x)
    734
    735 n = numerical_approx

/home/grout/sage/local/lib/python2.5/site-packages/sage/rings/complex_field.py in __call__(self, x, im)
    179             except AttributeError:
    180                 pass
--> 181         return complex_number.ComplexNumber(self, x, im)
    182
    183     def _coerce_impl(self, x):

/home/grout/sage/devel/sage-main/sage/graphs/complex_number.pyx in sage.rings.complex_number.ComplexNumber.__init__()

<type 'exceptions.TypeError'>: unable to coerce to a ComplexNumber
```


I'm not sure what it should do, but maybe call n() on each entry would make sense.

Issue created by migration from https://trac.sagemath.org/ticket/1294





---

archive/issue_comments_008126.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-22T10:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1294#issuecomment-8126",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_008127.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-22T10:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1294#issuecomment-8127",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008128.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-12-22T10:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1294#issuecomment-8128",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_008129.json:
```json
{
    "body": "Frustrating that the same snippet of code is duplicated, but this is the correct way to fix this.  Apply.",
    "created_at": "2008-01-20T06:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1294#issuecomment-8129",
    "user": "ncalexan"
}
```

Frustrating that the same snippet of code is duplicated, but this is the correct way to fix this.  Apply.



---

archive/issue_comments_008130.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T05:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1294#issuecomment-8130",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_008131.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T05:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1294#issuecomment-8131",
    "user": "mabshoff"
}
```

Resolution: fixed
