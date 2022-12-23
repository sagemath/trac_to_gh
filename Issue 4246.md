# Issue 4246: bug in coercing symbolic expressions to polynomial rings

Issue created by migration from https://trac.sagemath.org/ticket/4246

Original creator: AlexGhitza

Original creation time: 2008-10-05 21:46:40

Assignee: AlexGhitza

CC:  robertwb

This was reported by William Stein at #4106:

  I did notice this unfortunate property of the _polynomial_ function that is used
  to implement this patch, namely it does something dumb when given x+y as input: 

  {{{
  sage: var('x')
  x
  sage: var('y')
  y
  sage: S = PolynomialRing(Integers(4),1,'x')
  sage: S(x+y)
  2*x
  sage: (x+y)._polynomial_(S)
  2*x
  }}}

  I think in this case it should raise a TypeError. 



---

Attachment


---

Comment by AlexGhitza created at 2008-10-05 21:49:01

Changing status from new to assigned.


---

Comment by mhansen created at 2008-10-05 23:23:13

Looks good to me.


---

Comment by mabshoff created at 2008-10-07 20:59:20

This patch breaks two doctests in coerce_maps.pyx:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3$ ./sage -t -long devel/sage/sage/structure/coerce_maps.pyx
sage -t -long devel/sage/sage/structure/coerce_maps.pyx     
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/tmp/coerce_maps.py", line 110:
    sage: mor(x^2/4+1)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[4]>", line 1, in <module>
        mor(x**Integer(2)/Integer(4)+Integer(1))###line 110:
    sage: mor(x^2/4+1)
      File "map.pyx", line 133, in sage.categories.map.Map.__call__ (sage/categories/map.c:2755)
      File "coerce_maps.pyx", line 146, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:3348)
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1886, in _polynomial_
        raise TypeError, "%s is not a variable of %s" %(v, R)
    TypeError: x is not a variable of Univariate Polynomial Ring in t over Rational Field
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/tmp/coerce_maps.py", line 113:
    sage: mor(x^2/4+1)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[6]>", line 1, in <module>
        mor(x**Integer(2)/Integer(4)+Integer(1))###line 113:
    sage: mor(x^2/4+1)
      File "map.pyx", line 133, in sage.categories.map.Map.__call__ (sage/categories/map.c:2755)
      File "coerce_maps.pyx", line 146, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:3348)
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1886, in _polynomial_
        raise TypeError, "%s is not a variable of %s" %(v, R)
    TypeError: x is not a variable of Power Series Ring in t over Finite Field of size 7
**********************************************************************
```


Since this is coercion related I am adding RobertWB to the CC.

Cheers,

Michael


---

Attachment


---

Comment by AlexGhitza created at 2008-11-29 07:29:04

I added a small patch that changes the two failing doctests slightly so that they pass now.  I thought about the behaviour a bit and it seems sensible to me, but Robert should feel free to defend the original doctests if necessary.


---

Comment by mhansen created at 2008-12-04 11:37:57

I think the new doctests are fine.


---

Comment by mabshoff created at 2008-12-04 14:55:00

Merged both patches in Sage 3.2.2.alpha0


---

Comment by mabshoff created at 2008-12-04 14:55:00

Resolution: fixed
