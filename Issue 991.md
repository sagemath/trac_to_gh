# Issue 991: problem in interaction with Singular subprocesses

Issue created by migration from https://trac.sagemath.org/ticket/991

Original creator: cwitty

Original creation time: 2007-10-25 01:19:31

Assignee: was

The following happens in 2.8.9.rc1, on 32-bit and 64-bit x86 Linux.
Note that the problem does not occur if the "T = ..." line is omitted.


```
cwitty@comet:~/sage-2.8.9.rc1$ ./sage

sage: K.<w> = GF(27)
sage: P.<x, y> = PolynomialRing(K, 2, order='lex')
sage: I = Ideal([ x^8 + y + 2, y^6 + x*y^5 + x^2 ])
sage: T = I.triangular_decomposition('singular:triangLfak')
sage: I.variety()
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/home/cwitty/sage-2.8.9.rc1/<ipython console> in <module>()

/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in variety(self)
   1113 
   1114         P = self.ring()
-> 1115         T = self.triangular_decomposition('singular:triangLfak')
   1116 
   1117         V = []

/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in triangular_decomposition(self, algorithm)
    426         P = self.ring()
    427 
--> 428         is_groebner = self.basis_is_groebner()
    429 
    430         # make sure to work w.r.t. 'lex'

/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in basis_is_groebner(self)
    913         LTF = singular( [f.lt() for f in self.gens()] , "module" )
    914 
--> 915         M = (F * LTF.syz()).reduce(self._singular_())
    916 
    917         for i in range(M.nrows()):

/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in _singular_(self, singular)
    214         if singular is None: singular = singular_default
    215         try:
--> 216             self.ring()._singular_(singular).set_ring()            
    217             I = self.__singular
    218             if not (I.parent() is singular):

/home/cwitty/sage-2.8.9.rc1/multi_polynomial_libsingular.pyx in multi_polynomial_libsingular.MPolynomialRing_libsingular._singular_()

/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/interfaces/singular.py in eval(self, x, allow_semicolon, strip)
    372 
    373             if s.find("error") != -1 or s.find("Segment fault") != -1:
--> 374                 raise RuntimeError, 'Singular error:\n%s'%s
    375         finally:
    376             gc.enable()

<type 'exceptions.RuntimeError'>: Singular error:
   ? type 444 too complex...set minpoly before
   ? error occurred in STDIN line 166: `minpoly=(w^3+2*w+1);`
sage: 
```



---

Comment by malb created at 2007-11-17 17:21:29

Changing component from algebraic geometry to commutative algebra.


---

Comment by malb created at 2007-11-17 17:21:29

Changing status from new to assigned.


---

Attachment

The attached patch fixes this issue for me.


---

Comment by malb created at 2007-11-17 17:21:29

Changing assignee from was to malb.


---

Attachment

Looks good to me, probably.  It's just a format issue anyways.


---

Comment by mabshoff created at 2007-11-20 15:51:03

Resolution: fixed


---

Comment by mabshoff created at 2007-11-20 15:51:03

Merged in 2.8.13.rc1.
