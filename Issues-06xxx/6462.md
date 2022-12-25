# Issue 6462: [with patch, positive review] Unpickling problem for orders in a number field

archive/issues_006462.json:
```json
{
    "body": "Assignee: @williamstein\n\nUnpickling elements of number field orders doesn't work:\n\n```\nsage: L = QuadraticField(-11,'a'); OL = L.maximal_order(); w = OL.0\nsage: loads(dumps(w))\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/david/.sage/temp/groke/24319/_home_david__sage_init_sage_0.py in <module>()\n\n/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:8076)()\n\n/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element_quadratic.so in sage.rings.number_field.number_field_element_quadratic.__make_NumberFieldElement_quadratic0 (sage/rings/number_field/number_field_element_quadratic.cpp:2792)()\n\n/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element_quadratic.so in sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic.__init__ (sage/rings/number_field/number_field_element_quadratic.cpp:2897)()\n\n<type 'str'>: (<type 'exceptions.AttributeError'>, AttributeError(\"'AbsoluteOrder' object has no attribute '_is_maximal'\",))\n```\n\nWith orders in higher-degree fields, I get a different error message:\n\n```\nsage: L = NumberField(x^3 - x - 1,'a'); OL = L.maximal_order(); w = OL.0\nsage: loads(dumps(w))\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/david/.sage/temp/groke/24319/_home_david__sage_init_sage_0.py in <module>()\n\n/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:8076)()\n\n/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element.so in sage.rings.number_field.number_field_element.__create__NumberFieldElement_version1 (sage/rings/number_field/number_field_element.cpp:3696)()\n\n/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element.so in sage.rings.number_field.number_field_element.OrderElement_absolute.__init__ (sage/rings/number_field/number_field_element.cpp:20595)()\n\nAttributeError: (\"'NumberField_absolute' object has no attribute 'number_field'\", <built-in function __create__NumberFieldElement_version1>, (Number Field in a with defining polynomial x^3 - x - 1, <type 'sage.rings.number_field.number_field_element.OrderElement_absolute'>, 1))\n```\n(and the analogous thing for relative fields as well.)\n\nThis is a real problem because I am working on a computation where I need to be able to save results to disc, and this result is preventing me from loading what I've saved. (Elements of the fields rather than the orders unpickle OK, but it's next to impossible to prevent elements of the orders creeping in somehow when I pickle stuff.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6462\n\n",
    "closed_at": "2009-07-16T21:09:28Z",
    "created_at": "2009-07-04T10:56:44Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, positive review] Unpickling problem for orders in a number field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6462",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @williamstein

Unpickling elements of number field orders doesn't work:

```
sage: L = QuadraticField(-11,'a'); OL = L.maximal_order(); w = OL.0
sage: loads(dumps(w))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/david/.sage/temp/groke/24319/_home_david__sage_init_sage_0.py in <module>()

/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:8076)()

/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element_quadratic.so in sage.rings.number_field.number_field_element_quadratic.__make_NumberFieldElement_quadratic0 (sage/rings/number_field/number_field_element_quadratic.cpp:2792)()

/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element_quadratic.so in sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic.__init__ (sage/rings/number_field/number_field_element_quadratic.cpp:2897)()

<type 'str'>: (<type 'exceptions.AttributeError'>, AttributeError("'AbsoluteOrder' object has no attribute '_is_maximal'",))
```

With orders in higher-degree fields, I get a different error message:

```
sage: L = NumberField(x^3 - x - 1,'a'); OL = L.maximal_order(); w = OL.0
sage: loads(dumps(w))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/david/.sage/temp/groke/24319/_home_david__sage_init_sage_0.py in <module>()

/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:8076)()

/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element.so in sage.rings.number_field.number_field_element.__create__NumberFieldElement_version1 (sage/rings/number_field/number_field_element.cpp:3696)()

/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element.so in sage.rings.number_field.number_field_element.OrderElement_absolute.__init__ (sage/rings/number_field/number_field_element.cpp:20595)()

AttributeError: ("'NumberField_absolute' object has no attribute 'number_field'", <built-in function __create__NumberFieldElement_version1>, (Number Field in a with defining polynomial x^3 - x - 1, <type 'sage.rings.number_field.number_field_element.OrderElement_absolute'>, 1))
```
(and the analogous thing for relative fields as well.)

This is a real problem because I am working on a computation where I need to be able to save results to disc, and this result is preventing me from loading what I've saved. (Elements of the fields rather than the orders unpickle OK, but it's next to impossible to prevent elements of the orders creeping in somehow when I pickle stuff.)

Issue created by migration from https://trac.sagemath.org/ticket/6462





---

archive/issue_comments_052126.json:
```json
{
    "body": "patch against 4.1.alpha2",
    "created_at": "2009-07-04T15:39:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6462#issuecomment-52126",
    "user": "https://github.com/loefflerd"
}
```

patch against 4.1.alpha2



---

archive/issue_comments_052127.json:
```json
{
    "body": "Attachment [trac_6462-order_elt_pickle_bug.patch](tarball://root/attachments/some-uuid/ticket6462/trac_6462-order_elt_pickle_bug.patch) by @loefflerd created at 2009-07-04 15:40:08",
    "created_at": "2009-07-04T15:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6462#issuecomment-52127",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6462-order_elt_pickle_bug.patch](tarball://root/attachments/some-uuid/ticket6462/trac_6462-order_elt_pickle_bug.patch) by @loefflerd created at 2009-07-04 15:40:08



---

archive/issue_comments_052128.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2009-07-14T21:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6462#issuecomment-52128",
    "user": "https://github.com/ncalexan"
}
```

Fine by me.



---

archive/issue_comments_052129.json:
```json
{
    "body": "David, the patch `trac_6462-order_elt_pickle_bug.patch` doesn't contain your username. So I'm committing it in your name. Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(",
    "created_at": "2009-07-16T20:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6462#issuecomment-52129",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

David, the patch `trac_6462-order_elt_pickle_bug.patch` doesn't contain your username. So I'm committing it in your name. Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(



---

archive/issue_events_015251.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-16T21:09:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6462",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6462#event-15251"
}
```



---

archive/issue_comments_052130.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6462#issuecomment-52130",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
