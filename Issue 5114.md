# Issue 5114: something wrong in the initializer for elements of QuaternionAlgebra

archive/issues_005114.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  was\n\nConsider:\n\n```\nsage: QA = QuaternionAlgebra(QQ, -1, -1)\nsage: foo = QA(3.0); foo\n3.00000000000000\nsage: parent(foo)\nQuaternion algebra with generators (i, j, k) over Rational Field\nsage: parent(foo.vector()[0])\nReal Field with 53 bits of precision\n```\n\nI don't think the initializer should let you construct an element with RR members but still claim to be over QQ.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5114\n\n",
    "created_at": "2009-01-28T03:55:28Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "something wrong in the initializer for elements of QuaternionAlgebra",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5114",
    "user": "cwitty"
}
```
Assignee: tbd

CC:  was

Consider:

```
sage: QA = QuaternionAlgebra(QQ, -1, -1)
sage: foo = QA(3.0); foo
3.00000000000000
sage: parent(foo)
Quaternion algebra with generators (i, j, k) over Rational Field
sage: parent(foo.vector()[0])
Real Field with 53 bits of precision
```

I don't think the initializer should let you construct an element with RR members but still claim to be over QQ.

Issue created by migration from https://trac.sagemath.org/ticket/5114





---

archive/issue_comments_039087.json:
```json
{
    "body": "I think that QA(3.0) should definitely throw an exception, just as the following does:\n\n\n```\nsage: K.<a> = QuadraticField(11)\nsage: K(3.0)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (858, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (863, 0))\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/ghitza/.sage/temp/artin/9038/_home_ghitza__sage_init_sage_0.py in <module>()\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3645)()\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2793)()\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2700)()\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in _element_constructor_(self, x)\n   1417                 raise ValueError, \"vector must be of length equal to the degree of this number field\"\n   1418             return sum([ x[i]*self.gen(0)**i for i in range(self.degree()) ])\n-> 1419         return self._coerce_non_number_field_element_in(x)\n   1420 \n   1421     def _coerce_from_str(self, x):\n\n/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in _coerce_non_number_field_element_in(self, x)\n   1527         except (TypeError, AttributeError), msg:\n   1528             pass\n-> 1529         raise TypeError, type(x)\n   1530 \n   1531     def _coerce_map_from_(self, R):\n\nTypeError: <type 'sage.rings.real_mpfr.RealLiteral'>\n```\n",
    "created_at": "2009-01-28T22:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5114#issuecomment-39087",
    "user": "AlexGhitza"
}
```

I think that QA(3.0) should definitely throw an exception, just as the following does:


```
sage: K.<a> = QuadraticField(11)
sage: K(3.0)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (858, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (863, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ghitza/.sage/temp/artin/9038/_home_ghitza__sage_init_sage_0.py in <module>()

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3645)()

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2793)()

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2700)()

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in _element_constructor_(self, x)
   1417                 raise ValueError, "vector must be of length equal to the degree of this number field"
   1418             return sum([ x[i]*self.gen(0)**i for i in range(self.degree()) ])
-> 1419         return self._coerce_non_number_field_element_in(x)
   1420 
   1421     def _coerce_from_str(self, x):

/opt/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in _coerce_non_number_field_element_in(self, x)
   1527         except (TypeError, AttributeError), msg:
   1528             pass
-> 1529         raise TypeError, type(x)
   1530 
   1531     def _coerce_map_from_(self, R):

TypeError: <type 'sage.rings.real_mpfr.RealLiteral'>
```




---

archive/issue_comments_039088.json:
```json
{
    "body": "For what it's worth, this behaviour changed and became more consistent with the recent reworking of the quaternion algebra code:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage: QA = QuaternionAlgebra(QQ, -1, -1)\nsage: sage: foo = QA(3.0); foo\n3\nsage: parent(foo)\nQuaternion Algebra (-1, -1) with base ring Rational Field\nsage: foo[0]\n3\nsage: parent(foo[0])\nRational Field\n```\n\n| Sage Version 3.4, Release Date: 2009-03-11                         |\n| Type notebook() for the GUI, and license() for information.        |\nDo we want to consider this fixed now?",
    "created_at": "2009-03-29T03:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5114#issuecomment-39088",
    "user": "AlexGhitza"
}
```

For what it's worth, this behaviour changed and became more consistent with the recent reworking of the quaternion algebra code:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: QA = QuaternionAlgebra(QQ, -1, -1)
sage: sage: foo = QA(3.0); foo
3
sage: parent(foo)
Quaternion Algebra (-1, -1) with base ring Rational Field
sage: foo[0]
3
sage: parent(foo[0])
Rational Field
```

| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |
Do we want to consider this fixed now?



---

archive/issue_comments_039089.json:
```json
{
    "body": "Yes, it looks like the bug is fixed; but somebody should create a doctest so that we can make sure it stays fixed forever.",
    "created_at": "2009-03-31T03:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5114#issuecomment-39089",
    "user": "cwitty"
}
```

Yes, it looks like the bug is fixed; but somebody should create a doctest so that we can make sure it stays fixed forever.



---

archive/issue_comments_039090.json:
```json
{
    "body": "The attached patch adds the requested doctest.",
    "created_at": "2009-04-29T13:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5114#issuecomment-39090",
    "user": "AlexGhitza"
}
```

The attached patch adds the requested doctest.



---

archive/issue_comments_039091.json:
```json
{
    "body": "Changing assignee from tbd to AlexGhitza.",
    "created_at": "2009-04-29T13:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5114#issuecomment-39091",
    "user": "AlexGhitza"
}
```

Changing assignee from tbd to AlexGhitza.



---

archive/issue_comments_039092.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-29T13:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5114#issuecomment-39092",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039093.json:
```json
{
    "body": "Attachment [trac_5114.patch](tarball://root/attachments/some-uuid/ticket5114/trac_5114.patch) by AlexGhitza created at 2009-04-29 13:52:25",
    "created_at": "2009-04-29T13:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5114#issuecomment-39093",
    "user": "AlexGhitza"
}
```

Attachment [trac_5114.patch](tarball://root/attachments/some-uuid/ticket5114/trac_5114.patch) by AlexGhitza created at 2009-04-29 13:52:25



---

archive/issue_comments_039094.json:
```json
{
    "body": "Looks good to me: patch applies fine to 4.0.rc1, all doctests in the quatalg directory pass, and the docs build OK. Positive review.",
    "created_at": "2009-05-28T10:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5114#issuecomment-39094",
    "user": "davidloeffler"
}
```

Looks good to me: patch applies fine to 4.0.rc1, all doctests in the quatalg directory pass, and the docs build OK. Positive review.



---

archive/issue_comments_039095.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T04:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5114#issuecomment-39095",
    "user": "mhansen"
}
```

Merged in 4.0.1.alpha0.



---

archive/issue_comments_039096.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T04:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5114#issuecomment-39096",
    "user": "mhansen"
}
```

Resolution: fixed
