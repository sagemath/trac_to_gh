# Issue 8968: magma.Resultant() gives error

Issue created by migration from https://trac.sagemath.org/ticket/8968

Original creator: mariah

Original creation time: 2010-05-14 18:31:02

Assignee: was


```
eno% ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: poly0 = x^2 + x + 1
sage: poly1 = x^3 + x + 1
sage: p0 = magma(poly0)
sage: p1 = magma(poly1)
sage: magma.Resultant(p0,p1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.4.1, Release Date: 2010-05-02                       |
| Type notebook() for the GUI, and license() for information.        |
/home/mariah/sage/sage-4.4.1-x86_64-Linux-core2-fc/<ipython console> in <module>()

/home/mariah/sage/sage-4.4.1-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in __call__(self, *args, **kwds)
   1745                                list(args),
   1746                                params = kwds,
-> 1747                                nvals = nvals)
   1748     def _sage_doc_(self):
   1749         """

/home/mariah/sage/sage-4.4.1-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in function_call(self, function, args, params, nvals)
   1103         fun = "%s(%s%s)"%(function, ",".join([s.name() for s in args]), par)
   1104 
-> 1105         return self._do_call(fun, nvals)
   1106 
   1107     def _do_call(self, code, nvals):

/home/mariah/sage/sage-4.4.1-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in _do_call(self, code, nvals)
   1153             ans = None
   1154         elif nvals == 1:
-> 1155             return self(code)
   1156         else:
   1157             v = [self._next_var_name() for _ in range(nvals)]

/home/mariah/sage/sage-4.4.1-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in __call__(self, x, gens)
    735             pass
    736         
--> 737         A = Expect.__call__(self, x)
    738         if has_cache:
    739             x._magma_cache[self] = A

/home/mariah/sage/sage-4.4.1-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1030             
   1031         if isinstance(x, basestring):
-> 1032             return cls(self, x, name=name)
   1033         try:
   1034             return self._coerce_from_special_method(x)

/home/mariah/sage/sage-4.4.1-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1450                 self._session_number = -1
-> 1451                 raise TypeError, x
   1452         self._session_number = parent._session_number
   1453 

TypeError: Error evaluating Magma code.
IN:_sage_[3]:=Resultant(_sage_[1],_sage_[2]);
OUT:
>> _sage_[3]:=Resultant(_sage_[1],_sage_[2]);
                       ^
Runtime error in 'Resultant': Bad argument types
Argument types given: MonStgElt, MonStgElt

sage: 
```



---

Comment by was created at 2010-06-04 05:43:24

Resolution: wontfix


---

Comment by was created at 2010-06-04 05:43:24

You have to do `R.<x> = QQ[]` first, which is the analogue of Magma's `R<x> := PolynomialRing(RationalField());` .  Otherwise, x is merely a formal symbolic variable (in the sense of Sage's maple-like symbolic calculus package), and since Magma has no functionality for working with symbolic expressions, it just turns symbolic expressions into strings in Magma.  So here's the way to do the computation you want:


```

sage: R.<x> = QQ[]
sage: poly0 = x^2 + x + 1
sage: poly1 = x^3 + x + 1
sage: p0 = magma(poly0)
sage: p1 = magma(poly1)
sage:  magma.Resultant(p0,p1)
3
```

