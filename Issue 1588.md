# Issue 1588: after #1566, new errors in converting symbolic compositions to polynomials are exposed.

Issue created by migration from https://trac.sagemath.org/ticket/1588

Original creator: mhansen

Original creation time: 2007-12-22 16:51:12

Assignee: was


```
sage: sqrt(2).polynomial(RQDF)
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/opt/sage/devel/sage-main/sage/calculus/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in polynomial(self, base_ring)
   1342         V = R.variable_names()
   1343         return self.substitute_over_ring(
-> 1344              dict([(var(V[i]),G[i]) for i in range(len(G))]), ring=R)
   1345     
   1346     def _polynomial_(self, R):

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in substitute_over_ring(self, in_dict, ring, **kwds)
   2823             return X._recursive_sub(kwds)
   2824         else:
-> 2825             return X._recursive_sub_over_ring(kwds, ring)
   2826 
   2827         

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _recursive_sub_over_ring(self, kwds, ring)
   4900     def _recursive_sub_over_ring(self, kwds, ring):
   4901         ops = self._operands
-> 4902         return ring(ops[0](ops[1]._recursive_sub_over_ring(kwds, ring=ring)))
   4903 
   4904     def _is_atomic(self):

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __call__(self, x, *args, **kwds)
   6012             except AttributeError:
   6013                 pass
-> 6014         return self._do_sqrt(x, *args, **kwds)
   6015 
   6016     def _approx_(self, x):

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _do_sqrt(self, x, prec, extend, all)
   5985         if prec:
   5986             return ComplexField(prec)(x).sqrt(all=all)
-> 5987         z = SymbolicComposition(self, SR(x))
   5988         if all:
   5989             return [z, -z]

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __call__(self, x)
    378         elif hasattr(x, '_symbolic_'):
    379             return x._symbolic_(self)
--> 380         return self._coerce_impl(x)
    381 
    382     def _coerce_impl(self, x):

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _coerce_impl(self, x)
    400         elif is_Polynomial(x) or is_MPolynomial(x):
    401             if x.base_ring() != self:  # would want coercion to go the other way
--> 402                 return SymbolicPolynomial(x)
    403             else:
    404                 raise TypeError, "Basering is Symbolic Ring, please coerce in the other direction."

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __init__(self, p)
   3409     # not clear to me why we need anything else in this class -Bobby
   3410     def __init__(self, p):
-> 3411         if p.parent().base_ring().characteristic() != 0:
   3412             raise TypeError, "polynomial must be over a field of characteristic 0."
   3413         Symbolic_object.__init__(self, p)

/opt/sage/devel/sage-main/sage/calculus/ring.pyx in sage.rings.ring.Ring.characteristic()

/opt/sage/devel/sage-main/sage/calculus/element.pyx in sage.structure.element.RingElement.additive_order()

<type 'exceptions.NotImplementedError'>: 


sage: sqrt(2).polynomial(CDF)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/opt/sage/devel/sage-main/sage/calculus/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in polynomial(self, base_ring)
   1342         V = R.variable_names()
   1343         return self.substitute_over_ring(
-> 1344              dict([(var(V[i]),G[i]) for i in range(len(G))]), ring=R)
   1345     
   1346     def _polynomial_(self, R):

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in substitute_over_ring(self, in_dict, ring, **kwds)
   2823             return X._recursive_sub(kwds)
   2824         else:
-> 2825             return X._recursive_sub_over_ring(kwds, ring)
   2826 
   2827         

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _recursive_sub_over_ring(self, kwds, ring)
   4900     def _recursive_sub_over_ring(self, kwds, ring):
   4901         ops = self._operands
-> 4902         return ring(ops[0](ops[1]._recursive_sub_over_ring(kwds, ring=ring)))
   4903 
   4904     def _is_atomic(self):

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in __call__(self, x, check, is_gen, construct, absprec)
    216                 return self([x])
    217         if hasattr(x, '_polynomial_'):
--> 218             return x._polynomial_(self)        
    219         if is_SingularElement(x) and self._has_singular:
    220             self._singular_().set_ring()

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _polynomial_(self, R)
   4864             #Convert self into R's base ring and then into R since
   4865             #self must be a constant.
-> 4866             return R( R.base_ring()(self) )
   4867         else:
   4868             raise TypeError, "cannot convert self (= %s) to a polynomial"%str(self).strip()

/opt/sage/devel/sage-main/sage/calculus/complex_double.pyx in sage.rings.complex_double.ComplexDoubleField_class.__call__()

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _complex_double_(self, field)
   5032         f = self._operands[0]
   5033         g = self._operands[1]
-> 5034         z = f(g._complex_double_(field))
   5035         if isinstance(z, SymbolicExpression):
   5036             return field(complex(z))

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _complex_double_(self, C)
   3069         EXAMPLES:
   3070         """
-> 3071         return C(self._obj)
   3072 
   3073     def _real_double_(self, R):

/opt/sage/devel/sage-main/sage/calculus/complex_double.pyx in sage.rings.complex_double.ComplexDoubleField_class.__call__()

/opt/sage/devel/sage-main/sage/calculus/complex_double.pyx in sage.rings.complex_double.ComplexDoubleElement.__init__()

/opt/sage/devel/sage-main/sage/calculus/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.__float__()

/opt/sage/devel/sage-main/sage/calculus/complex_double.pyx in sage.rings.complex_double.ComplexDoubleElement.__float__()

<type 'exceptions.TypeError'>: can't convert complex to float; use abs(z)
```



---

Comment by mabshoff created at 2008-12-02 01:49:43

This now throws a not implemented error in Sage 3.2.1.rc1:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.1.final$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sqrt(2).polynomial(RQDF)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
| Sage Version 3.2.1.rc1, Release Date: 2008-12-01                   |
| Type notebook() for the GUI, and license() for information.        |
/scratch/mabshoff/release-cycle/sage-3.2.1.final/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in polynomial(self, base_ring)
   1803         V = R.variable_names()
   1804         return self.substitute_over_ring(
-> 1805              dict([(var(V[i]),G[i]) for i in range(len(G))]), ring=R)
   1806     
   1807     def _polynomial_(self, R):

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in substitute_over_ring(self, in_dict, ring, **kwds)
   3763             return X._recursive_sub(kwds)
   3764         else:
-> 3765             return X._recursive_sub_over_ring(kwds, ring)
   3766 
   3767         

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in _recursive_sub_over_ring(self, kwds, ring)
   6164     def _recursive_sub_over_ring(self, kwds, ring):
   6165         ops = self._operands
-> 6166         return ring(ops[0](ops[1]._recursive_sub_over_ring(kwds, ring=ring)))
   6167 
   6168     def _is_atomic(self):

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in __call__(self, x, *args, **kwds)
   8259         except AttributeError:
   8260             pass
-> 8261         return self._do_sqrt(x, *args, **kwds)
   8262 
   8263     def _approx_(self, x):

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in _do_sqrt(self, x, prec, extend, all)
   8234             else:
   8235                  return ComplexField(prec)(x).sqrt(all=all)
-> 8236         z = SymbolicComposition(self, SR(x))
   8237         if all:
   8238             return [z, -z]

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in __call__(self, x)
    452                 msg, s, pos = err.args
    453                 raise TypeError, "%s: %s !!! %s" % (msg, s[:pos], s[pos:])
--> 454         return self._coerce_impl(x)
    455 
    456     def _coerce_impl(self, x):

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in _coerce_impl(self, x)
    476         elif is_Polynomial(x) or is_MPolynomial(x):
    477             if x.base_ring() != self:  # would want coercion to go the other way
--> 478                 return SymbolicPolynomial(x)
    479             else:
    480                 raise TypeError, "Basering is Symbolic Ring, please coerce in the other direction."

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in __init__(self, p)
   4396     # not clear to me why we need anything else in this class -Bobby
   4397     def __init__(self, p):
-> 4398         if p.parent().base_ring().characteristic() != 0:
   4399             raise TypeError, "polynomial must be over a field of characteristic 0."
   4400         Symbolic_object.__init__(self, p)

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.characteristic (sage/rings/ring.c:4377)()

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement.additive_order (sage/structure/element.c:9573)()

NotImplementedError: 
sage: 
```


Cheers,

Michael


---

Comment by burcin created at 2009-05-25 13:45:05

This works on 4.0.rc0:


```
sage: sqrt(2).polynomial(RealField(212))
1.41421356237309504880168872420969807856967187537694807317667974
sage: sqrt(2).polynomial(ComplexField(212))
1.41421356237309504880168872420969807856967187537694807317667974
sage: (sqrt(2)*x).polynomial(RDF['x'])
1.41421356237*x
```


The doctests after line 3635 of sage/symbolic/expression.pyx test this.

This bug should be closed as fixed.


---

Comment by mhansen created at 2009-05-26 16:23:22

Resolution: fixed
