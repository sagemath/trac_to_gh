# Issue 5607: confusing syntax for creating symbolic functions

Issue created by migration from https://trac.sagemath.org/ticket/5607

Original creator: burcin

Original creation time: 2009-03-25 10:57:55

Assignee: burcin

CC:  jason

In a [comment:ticket:5413:12 comment] to #5413 Jason pointed out the following confusing behavior:


```
sage: g(x)=sin
sage: g(3)
sin(3)
sage: g(x)=sin+x
sage: g(3)
sin + 3

sage: g(x)=sin+cos; g(3)
sin + cos
```


I think the syntax for this should be:


```
sage: g(x) = sin(x) + 3
sage: g(3)
sin(3) + 3

sage: g(x) = sin(x) + cos(x)
sage: g(3)
sin(3) + cos(3)
```


Since it is not clear which variable to use if only `sin` is specified. Also consider this situation:


```
sage: g(x,y) = sin + y
sage: g(3,4)
???
```


We have two options:

 * We could allow this syntax for convenience:


```
sage: g(x) = sin + x
```


and convert the function arguments to appropriate callable expressions if the number of arguments of `g` match the number of arguments of the given function, raise an error otherwise.

 * We raise an error whenever a function object is specified without variables.

Comments?


---

Comment by mhansen created at 2009-06-05 02:28:01

Resolution: invalid


---

Comment by mhansen created at 2009-06-05 02:28:01

In 4.0, we raise an error for this type of thing.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: g(x)=sin
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.0.1.rc1, Release Date: 2009-06-04                   |
| Type notebook() for the GUI, and license() for information.        |
/home/mhansen/.sage/temp/sage.math.washington.edu/31677/_home_mhansen__sage_init_sage_0.py in <module>()

/scratch/mhansen/release/4.0.1/rc2/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/calculus/all.pyc in symbolic_expression(x)
     63         return x._symbolic_(SR)
     64     else:
---> 65         return SR(x)
     66 
     67 import desolvers

/scratch/mhansen/release/4.0.1/rc2/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)()

/scratch/mhansen/release/4.0.1/rc2/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3058)()

/scratch/mhansen/release/4.0.1/rc2/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2949)()

/scratch/mhansen/release/4.0.1/rc2/sage-4.0.1.rc2/local/lib/python2.5/site-packages/sage/symbolic/ring.so in sage.symbolic.ring.SymbolicRing._element_constructor_ (sage/symbolic/ring.cpp:4416)()

TypeError: 
sage: g(x) = sin(x)
```

