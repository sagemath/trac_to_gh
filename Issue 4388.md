# Issue 4388: elliptic curves: basis_matrix command totally broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-30 05:15:58

Assignee: was


```
sage: EllipticCurve('11a').period_lattice().basis_matrix()
Traceback (most recent call last):
...
TypeError: Unable to coerce 0.634604652139777 + 1.45881661693850*I (<type 'sage.rings.complex_number.ComplexNumber'>) to Rational
```



---

Comment by cremona created at 2008-10-30 17:05:27

Comment:  I noticed this when I reworked the whole of period_lattice.py recently.  But the function basis_matrix only exists because  PeriodLattice_ell derives from  PeriodLattice and hence from FreeModule_generic_pid.  But I don't think it makes a lot of sense to ask for a basis matrix in a case like this, when the thing is a Z-module but it does not sit in an ambient Q-vector space.

If people agree, we should at least add the function but have it raise a sensible error.


---

Comment by was created at 2008-10-30 18:03:18

But I really wanted basis_matrix(), since I wanted to compute the determinant of the basis matrix in order to find the volume of the period lattice. 

There is no volume method.  That would also be nice.   

I think at least mathematically the idea of "basis matrix" makes sense, and I was happy it was there (except that it is broken).


---

Comment by cremona created at 2008-10-30 18:23:07

Replying to [comment:2 was]:
> But I really wanted basis_matrix(), since I wanted to compute the determinant of the basis matrix in order to find the volume of the period lattice. 
> 
> There is no volume method.  That would also be nice.   

It _is_ there:  complex_area()  (not my choice of name)!

> 
> I think at least mathematically the idea of "basis matrix" makes sense, and I was happy it was there (except that it is broken).

You'll have to explain it to me.  Do you want the 2x2 matrix of reals consisting of the real and imaginary parts of the period basis?  That would be easy to add, like this:


```
sage: E = EllipticCurve('389a1')
sage: L = E.period_lattice()
sage: M = Matrix([[CC(w).real(), CC(w).imag()] for w in L.basis()]); M

[ 2.49021256085505 0.000000000000000]
[0.000000000000000  1.97173770155165]
sage: M.det()
4.91004599111539
sage: L.complex_area()
4.91004599111539
```



and


```
sage: E = EllipticCurve('11a1')
sage: L = E.period_lattice()
sage: M = Matrix([[CC(w).real(), CC(w).imag()] for w in L.basis()]); M

[ 1.26920930427955 0.000000000000000]
[0.634604652139777  1.45881661693850]
sage: M.det()
1.85154362345596
sage: L.complex_area()
1.85154362345596
```



---

Attachment


---

Comment by cremona created at 2008-10-30 18:46:31

Patch sage-trac4388.patch attached (based on 3.2.alpha1).


---

Comment by davidloeffler created at 2008-11-03 15:05:52

Looks good to me. I agree with was's statement that the concept of a basis matrix makes sense here, and that basis_matrix() should return this rather than an error; patch applies fine in 3.2.alpha1; and all doctests in sage/schemes/elliptic_curves pass.


---

Comment by mabshoff created at 2008-11-04 14:05:18

Merged in Sage 3.2.alpha3


---

Comment by mabshoff created at 2008-11-04 14:05:18

Resolution: fixed
