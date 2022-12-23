# Issue 1127: modularSymbol complement fails for E=128a

Issue created by migration from https://trac.sagemath.org/ticket/1127

Original creator: syazdani

Original creation time: 2007-11-07 20:35:42

Assignee: was

CC:  robertwb

The following code raises the following exception:

```
sage: E=EllipticCurve("128a")
sage: ME=E.modular_symbol_space()
sage: ME.complement()
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/net/mathserv/1/home/syazdani/research/programs/<ipython console> in <module>()

/home/syazdani/sage/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py in complement(self, bound)
    200         else:
    201             # failed
--> 202             raise RuntimeError, "Computation of complementary space failed (cut down to rank %s, but should have cut down to rank %s)."%(V.rank(), self.rank())
    203
    204

<type 'exceptions.RuntimeError'>: Computation of complementary space failed (cut down to rank 18, but should have cut down to rank 1).
```



---

Comment by mabshoff created at 2007-12-18 09:11:46

This remains unfixed in Sage 2.9.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-20 02:59:34

And it is still open in Sage 2.10.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-26 06:53:19

And it is still broken in Sage 3.0.3. This looks like a job for Craig Citro :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-26 06:53:19

Changing assignee from was to craigcitro.


---

Comment by mabshoff created at 2008-11-02 16:27:56

Could #2535 be related?

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-22 23:33:05

For the record, there are other failures for conductors 144, 192, 225.  These are the only conductors smaller than 250 that fail.

The patch implements a naive fix.


---

Comment by craigcitro created at 2009-01-22 23:34:06

I'd review this, but I helped write it. :)


---

Comment by robertwb created at 2009-01-23 22:41:43

I'm still getting 


```
sage: E = EllipticCurve("128a") 
sage: E.congruence_number()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 2618, in congruence_number
    self.__congruence_number = W.congruence_number(V)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 938, in congruence_number
    W = other.q_expansion_module(prec, ZZ)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 770, in q_expansion_module
    return self._q_expansion_module_integral(prec)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 910, in _q_expansion_module_integral
    V = self.q_expansion_module(prec, QQ)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 772, in q_expansion_module
    return self._q_expansion_module_rational(prec)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 861, in _q_expansion_module_rational
    return self._q_expansion_module(prec)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 820, in _q_expansion_module
    return A.span([f.padded_list(prec) for f in self.q_expansion_basis(prec, algorithm)])
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 602, in q_expansion_basis
    return Sequence(self._q_expansion_basis_hecke_dual(prec), cr=True)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 1073, in _q_expansion_basis_hecke_dual
    v = [self.dual_hecke_matrix(n).column(i) for n in range(1,prec)]
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/hecke/module.py", line 797, in dual_hecke_matrix
    T = self._compute_dual_hecke_matrix(n)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py", line 110, in _compute_dual_hecke_matrix
    return A.restrict(self.dual_free_module(), check=check)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py", line 320, in dual_free_module
    "(cut down to rank %s, but should have cut down to rank %s)."%(V.rank(), self.rank())
RuntimeError: Computation of embedded dual vector space failed (cut down to rank 9, but should have cut down to rank 8).
```



---

Comment by robertwb created at 2009-01-24 00:31:56

This is a separate issue, see #5080. The patch fixes the issue that was raised.


---

Attachment

Merged in Sage 3.3.alpha2

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 19:30:30

Resolution: fixed
