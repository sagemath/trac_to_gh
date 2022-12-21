# Issue 4171: SR + long broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-09-23 01:12:46

Assignee: somebody

Adding a long to a symbolic variable is broken:


```
OK
sage: x + int(5) 
x + 5

Not OK:
sage: x + long(5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/wstein/<ipython console> in <module>()

/home/wstein/element.pyx in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:5748)()

/home/wstein/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6364)()

TypeError: unsupported operand parent(s) for '+': 'Symbolic Ring' and '<type 'long'>'
```



---

Comment by jason created at 2008-09-23 01:15:26

Related (and maybe the root of the problem): 


```
sage: SR(long(2))     
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/plot/<ipython console> in <module>()

/home/grout/downloads/sage-3.1.2/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __call__(self, x)

/home/grout/downloads/sage-3.1.2/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _coerce_impl(self, x)

TypeError: cannot coerce type '<type 'long'>' into a SymbolicExpression.
```



---

Comment by mabshoff created at 2008-09-23 01:16:33

This is a dupe if #4170 which robertwb opened. Since that ticket has a patch I am closing this one as a dupe.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-23 01:16:33

Resolution: duplicate
