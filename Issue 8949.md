# Issue 8949: symbolic functions dont work with numpy.int32

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2010-05-11 08:18:24

Assignee: burcin

CC:  jason


```
sage: import numpy
sage: a = numpy.array([1,2])
sage: type(a[0])
<type 'numpy.int32'>
sage: f(x) = x^2
sage: f(a[0])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
./sage-4.4.2/<ipython console> in <module>()

./sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__call__ (sage/symbolic/expression.cpp:15476)()

./sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/callable.pyc in _call_element_(self, _the_element, *args, **kwds)
    454         d = dict(zip(map(repr, self.arguments()), args))
    455         d.update(kwds)
--> 456         return SR(_the_element.substitute(**d))
    457
    458

./sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.substitute (sage/symbolic/expression.cpp:14850)()

./sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.coerce_in (sage/symbolic/expression.cpp:10193)()

./sage-4.4.2/local/lib/python2.6/site-packages/sage/structure/parent_old.so in sage.structure.parent_old.Parent._coerce_ (sage/structure/parent_old.c:3288)()

./sage-4.4.2/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.coerce (sage/structure/parent.c:6970)()

TypeError: no canonical coercion from <type 'numpy.int32'> to Callable function ring with arguments (x,)
```




---

Comment by jason created at 2010-05-11 20:57:07

I think #8824 may have the solution for this.


---

Comment by bascorp2 created at 2010-05-26 08:41:19

[computer pictures](http://like-search.info/)


---

Comment by vdelecroix created at 2015-03-28 12:01:57

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2015-03-28 12:01:57

Hello,

I propose to close this as duplicates because of #18076. With the branch applied

```
sage: import numpy
sage: cos(numpy.float('12'))
0.8438539587324921
```

Though it is not perfect since the result is a Python float and not a numpy float.

Vincent


---

Comment by jdemeyer created at 2015-04-23 10:10:31

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-04-23 14:51:54

Resolution: duplicate
