# Issue 3058: coercing a vector to symbolic entries doesn't work when the vector's parent has a user-defined basis

Issue created by migration from https://trac.sagemath.org/ticket/3058

Original creator: jason

Original creation time: 2008-04-29 23:37:30

Assignee: robertwb

The title is what I think is the real issue here:


```
sage: a=(QQ3).subspace([[1,0,1]])
sage: b=a.basis()[0]
sage: b/b.norm()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/element.pyx in sage.structure.element.Vector.__div__ 
(sage/structure/element.c:10962)()

/home/grout/element.pyx in sage.structure.element.Vector.__mul__ 
(sage/structure/element.c:10413)()

/home/grout/coerce.pyx in 
sage.structure.coerce.CoercionModel_cache_maps.bin_op_c 
(sage/structure/coerce.c:5292)()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 
'Vector space of degree 3 and dimension 1 over Rational Field
Basis matrix:
[1 0 1]' and 'Symbolic Ring'
```



Note that the following does work:


```
sage: b=vector(QQ,[1,0,1])
sage: b/b.norm()
(1/sqrt(2), 0, 1/sqrt(2))
```




---

Comment by jason created at 2008-12-19 18:42:07

This seems fixed now (in 3.2.1).  However there are other similar issues, like:


```
sage: a=(QQ^3).subspace([[1,0,1]])
sage: b=a.basis()[0]
sage: b/b.norm()
(1/sqrt(2), 0, 1/sqrt(2))
sage: b-b/b.norm()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__sub__ (sage/structure/element.c:6073)()

/home/grout/sage/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5805)()

TypeError: unsupported operand parent(s) for '-': 'Vector space of degree 3 and dimension 1 over Rational Field
Basis matrix:
[1 0 1]' and 'Vector space of degree 3 and dimension 1 over Symbolic Ring
User basis matrix:
[1 0 1]'
```



---

Comment by jason created at 2008-12-19 18:45:07

It also seems like the operation above takes *way* too long:


```
sage: %time b/b.norm()  
CPU times: user 0.48 s, sys: 0.14 s, total: 0.62 s
Wall time: 2.02 s
(1/sqrt(2), 0, 1/sqrt(2))
sage: %time b.norm()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sqrt(2)
```



---

Comment by mhansen created at 2009-06-04 23:05:06

Resolution: invalid


---

Comment by mhansen created at 2009-06-04 23:05:06

This looks good with 4.0.1.rc1:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: a=(QQ^3).subspace([[1,0,1]])
sage: sage: b=a.basis()[0]
sage: %time b/b.norm()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
(1/2*sqrt(2), 0, 1/2*sqrt(2))
sage: b-b/b.norm()
(-1/2*sqrt(2) + 1, 0, -1/2*sqrt(2) + 1)
```

