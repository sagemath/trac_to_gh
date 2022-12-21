# Issue 6462: Unpickling problem for orders in a number field

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-07-04 10:56:44

Assignee: was

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


sage: L = NumberField(x^3 - x - 1,'a'); OL = L.maximal_order(); w = OL.0
sage: loads(dumps(w))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/david/.sage/temp/groke/24319/_home_david__sage_init_sage_0.py in <module>()

/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:8076)()

/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element.so in sage.rings.number_field.number_field_element.__create__NumberFieldElement_version1 (sage/rings/number_field/number_field_element.cpp:3696)()

/home/david/sage-4.1/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element.so in sage.rings.number_field.number_field_element.OrderElement_absolute.__init__ (sage/rings/number_field/number_field_element.cpp:20595)()

AttributeError: ("'NumberField_absolute' object has no attribute 'number_field'", <built-in function __create__NumberFieldElement_version1>, (Number Field in a with defining polynomial x^3 - x - 1, <type 'sage.rings.number_field.number_field_element.OrderElement_absolute'>, 1))
}}}
(and the analogous thing for relative fields as well.)

This is a real problem because I am working on a computation where I need to be able to save results to disc, and this result is preventing me from loading what I've saved. (Elements of the fields rather than the orders unpickle OK, but it's next to impossible to prevent elements of the orders creeping in somehow when I pickle stuff.)


---

Comment by davidloeffler created at 2009-07-04 15:39:51

patch against 4.1.alpha2


---

Attachment


---

Comment by ncalexan created at 2009-07-14 21:12:21

Fine by me.


---

Comment by mvngu created at 2009-07-16 20:18:46

David, the patch `trac_6462-order_elt_pickle_bug.patch` doesn't contain your username. So I'm committing it in your name. Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:09:28

Resolution: fixed
