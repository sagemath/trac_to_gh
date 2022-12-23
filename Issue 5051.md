# Issue 5051: tracebacks involving cython (etc.) seriously broken in sage-3.3.alpha0 (probably caused by ipython)

Issue created by migration from https://trac.sagemath.org/ticket/5051

Original creator: was

Original creation time: 2009-01-22 07:49:06

Assignee: cwitty

For example, a clean build of sage-3.3.alpha0 or sage-3.2 on sage.math:


```
wstein@sage:/space/wstein/build/sage-3.3.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: 1/0
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1507, 0))
| Sage Version 3.3.alpha0, Release Date: 2009-01-19                  |
| Type notebook() for the GUI, and license() for information.        |
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/scratch/wstein/sage/temp/sage.math.washington.edu/16649/_scratch_wstein_sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/space/wstein/build/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9099)()
   1180 
   1181 
-> 1182 
   1183 
   1184 

/space/wstein/build/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/integer.so in sage.rings.integer.Integer._div_ (sage/rings/integer.c:9516)()
   1175 
   1176 
-> 1177 
   1178 
   1179 

/space/wstein/build/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/integer_ring.so in sage.rings.integer_ring.IntegerRing_class._div (sage/rings/integer_ring.c:4745)()
    228 
    229 
--> 230 
    231 
    232 

ZeroDivisionError: Rational division by zero
```


In the notebook the traceback looks like this (i.e. we never show the actual lines, only the numbers).  So this is definitely some sort of ipython problem. 

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/space/wstein/build/sage-3.3.alpha0/here/worksheets/admin/1/code/1.py", line 9, in <module>
    _sage_const_1 /_sage_const_0
  File "/space/wstein/build/sage-3.3.alpha0/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "element.pyx", line 1182, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9099)
  File "integer.pyx", line 1177, in sage.rings.integer.Integer._div_ (sage/rings/integer.c:9516)
  File "integer_ring.pyx", line 230, in sage.rings.integer_ring.IntegerRing_class._div (sage/rings/integer_ring.c:4745)
ZeroDivisionError: Rational division by zero
```


One possible solution would be to tone down the default traceback of ipython to not show 5 lines of context at every step, which is kind of nuts. 


---

Comment by was created at 2009-01-23 00:08:30

I was wrong.  The tracebacks never showed the code:

```
wstein@sage:/disk/scratch/mabshoff-sage-releases$ sage-2.10/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10, Release Date: 2008-01-18                        |
| Type notebook() for the GUI, and license() for information.        |
sage: 1/0
---------------------------------------------------------------------------
<type 'exceptions.ZeroDivisionError'>     Traceback (most recent call last)

/disk/scratch/mabshoff-sage-releases/<ipython console> in <module>()

/disk/scratch/mabshoff-sage-releases/element.pyx in sage.structure.element.RingElement.__div__()

/disk/scratch/mabshoff-sage-releases/coerce.pxi in sage.structure.element._div_c()

/disk/scratch/mabshoff-sage-releases/integer.pyx in sage.rings.integer.Integer._div_c_impl()

/disk/scratch/mabshoff-sage-releases/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class._div()

<type 'exceptions.ZeroDivisionError'>: Rational division by zero
```



---

Comment by mhansen created at 2009-01-24 08:06:31

Changing assignee from cwitty to mhansen.


---

Comment by mhansen created at 2009-01-24 08:06:31

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-24 08:06:31

This is fixed in the patch at #5073.


---

Comment by mabshoff created at 2009-02-07 01:13:23

Fixed via #5073.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: 1/0
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1503, 0))
| Sage Version 3.3.alpha5, Release Date: 2009-02-03                  |
| Type notebook() for the GUI, and license() for information.        |
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/home/mabshoff/.sage/temp/geom/20328/_home_mabshoff__sage_init_sage_0.py in <module>()

/scratch/mabshoff/sage-3.3.alpha6/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9099)()

/scratch/mabshoff/sage-3.3.alpha6/local/lib/python2.5/site-packages/sage/rings/integer.so in sage.rings.integer.Integer._div_ (sage/rings/integer.c:9522)()

/scratch/mabshoff/sage-3.3.alpha6/local/lib/python2.5/site-packages/sage/rings/integer_ring.so in sage.rings.integer_ring.IntegerRing_class._div (sage/rings/integer_ring.c:4745)()

ZeroDivisionError: Rational division by zero
```

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-07 01:13:23

Resolution: fixed
