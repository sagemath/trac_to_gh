# Issue 1458: Ipython bug -- the tracebacks in the sage command line list all absolute paths to Cython files totally incorrectly.

Issue created by migration from https://trac.sagemath.org/ticket/1458

Original creator: was

Original creation time: 2007-12-11 02:46:41

Assignee: was

On the command line:

```
sage: 1/0
---------------------------------------------------------------------------
<type 'exceptions.ZeroDivisionError'>     Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/element.pyx in sage.structure.element.RingElement.__div__()

/Users/was/coerce.pxi in sage.structure.element._div_c()

/Users/was/integer.pyx in sage.rings.integer.Integer._div_c_impl()

/Users/was/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class._div()

<type 'exceptions.ZeroDivisionError'>: Rational division by zero


```


Notice that the absolute paths are nonsense.

In the notebook:

```
1/0
```

outputs

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/was/.sage/sage_notebook/worksheets/admin/9/code/5.py", line 4, in <module>
    Integer(1)/Integer(0)
  File "/Users/was/s/data/extcode/sage/", line 1, in <module>
    
  File "element.pyx", line 1480, in sage.structure.element.RingElement.__div__
  File "coerce.pxi", line 138, in sage.structure.element._div_c
  File "integer.pyx", line 854, in sage.rings.integer.Integer._div_c_impl
  File "integer_ring.pyx", line 190, in sage.rings.integer_ring.IntegerRing_class._div
ZeroDivisionError: Rational division by zero
```


so there are no absolute paths.  This is the same as in Python itself:


```
>>> 1/sage.all.ZZ(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "element.pyx", line 1482, in sage.structure.element.RingElement.__div__
  File "coerce.pyx", line 252, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c
  File "element.pyx", line 1480, in sage.structure.element.RingElement.__div__
  File "coerce.pxi", line 138, in sage.structure.element._div_c
  File "integer.pyx", line 854, in sage.rings.integer.Integer._div_c_impl
  File "integer_ring.pyx", line 190, in sage.rings.integer_ring.IntegerRing_class._div
ZeroDivisionError: Rational division by zero
```



---

Comment by was created at 2007-12-11 17:06:57

From Fernando Perez:

```
More than a 'real' ipython bug, something tells me it's an issue with
the python inspect module, which we push a bit hard with our
tracebacks and has a long history of breaking left and right.  But
whenever we can, we work around its problems, and I'm sure we could do
so here too.

Could we start by you updating to the most recent ipython SVN?  In
case you prefer tarballs to SVN, I put one of the current code here:

http://ipython.scipy.org/dist/testing/ipython-0.8.3.svn.r2876.tar.gz

I ask because Robert Kern just last week fixed some things related to
this, and there's a small chance the problem is already gone (I can't
reproduce it with any of the pyrex code  I have locally).  If not,
I'll dig deeper.
```



---

Comment by rlm created at 2009-01-23 02:43:11

Duplicates #775.


---

Comment by rlm created at 2009-01-23 02:43:11

Resolution: duplicate
