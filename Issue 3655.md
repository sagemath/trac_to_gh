# Issue 3655: left multiplication in piecewise does not work

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-07-15 01:46:22

Assignee: gfurnish

This was reported by C Boncelet.


```
sage: x = PolynomialRing(QQ,'x').gen()
sage: f = Piecewise([This is the Trac macro ** that was inherited from the migration called with arguments (0,1),1*x^0)](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: r = f*2
sage: r = 2*f
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call
last)
/Users/boncelet/<ipython console> in <module>()
/Users/boncelet/element.pyx in
sage.structure.element.RingElement.__mul__ (sage/structure/element.c:
8545)()
/Users/boncelet/coerce.pyx in
sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/
structure/coerce.c:5338)()
TypeError: unsupported operand parent(s) for '*': 'Integer Ring' and
'<type 'instance'>'
```


He then suggested simply defining __rmul__ = __mul__:


```
sage: f.__rmul__ = f.__mul__
sage: r = f*2
sage: r = 2*f
sage: r
Piecewise defined function with 1 parts, [This is the Trac macro ** that was inherited from the migration called with arguments (0, 1), 2)](https://trac.sagemath.org/wiki/WikiMacros#-macro)
```




---

Attachment

based on 3.0.4


---

Comment by wdj created at 2008-07-15 10:49:34

I added a patch implementing the suggestion above. It is just a few lines. Passes sage -testall.


---

Attachment


---

Comment by mhansen created at 2008-08-26 22:12:49

Looks good to me.  Apply both patches.


---

Comment by mabshoff created at 2008-08-26 22:54:16

Merged both patches in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-26 22:54:16

Resolution: fixed
