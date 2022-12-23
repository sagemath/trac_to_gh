# Issue 1186: Charpoly of a matrix of polynomials sometimes breaks

Issue created by migration from https://trac.sagemath.org/ticket/1186

Original creator: kedlaya

Original creation time: 2007-11-16 13:31:17

Assignee: was

The following:

```
P.<a,b,c> = PolynomialRing(Integers())
u = MatrixSpace(P,3)([[0,0,a],[1,0,b],[0,1,c]])
Q.<x> = PolynomialRing(P)
u.charpoly('x')
```

returns as intended:

```
x^3 + (-1*c)*x^2 + (-1*b)*x - a
```

but the following code:

```
P.<a,b,c> = PolynomialRing(Rationals())
u = MatrixSpace(P,3)([[0,0,a],[1,0,b],[0,1,c]])
Q.<x> = PolynomialRing(P)
u.charpoly('x')
```

does not, instead returning the traceback:

```
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/kedlaya/<ipython console> in <module>()

/home/kedlaya/matrix2.pyx in sage.matrix.matrix2.Matrix.charpoly()

/home/kedlaya/matrix2.pyx in sage.matrix.matrix2.Matrix._charpoly_hessenberg()

/home/kedlaya/sage-complete/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in __call__(self, x, check, is_gen, construct, absprec)
    240         C = self.__polynomial_class
    241         if absprec is None:
--> 242             return C(self, x, check, is_gen, construct=construct)
    243         else:
    244             return C(self, x, check, is_gen, construct=construct, absprec = absprec)

/home/kedlaya/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__init__()

/home/kedlaya/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__()

/home/kedlaya/sage-complete/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)
    180         if isinstance(x, sage.rings.rational.Rational):
    181             return x
--> 182         return sage.rings.rational.Rational(x, base)
    183 
    184     def construction(self):

/home/kedlaya/rational.pyx in sage.rings.rational.Rational.__init__()

/home/kedlaya/rational.pyx in sage.rings.rational.Rational.__set_value()

/home/kedlaya/sage-complete/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.py in _rational_(self)
    270         Z = integer_ring.IntegerRing()
    271         try:
--> 272             return Z(self.__numerator) / Z(self.__denominator)
    273         except AttributeError:
    274             pass

/home/kedlaya/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: lift() takes exactly one argument (0 given)
```




---

Comment by AlexGhitza created at 2007-11-17 18:11:28

I tracked the bug down to the function _charpoly_hessenberg() in matrix2.pyx.  The problem occurs at the very end of the function, when we want to turn the list v of coefficients into the characteristic polynomial.  More precisely, the elements of v live in the fraction field of the polynomial ring P (this is a side effect of hessenbergizing the matrix), and the function was trying to make them into coefficients of a polynomial over P itself; this is where the error was coming up.  I changed this to get a polynomial over the fraction field of P.


---

Comment by robertwb created at 2007-11-18 08:30:47

Do not apply this patch. 

Though the operations take place in the fraction field, the coefficients all live in the original ring (proof: use the determinant form of charpoly) and this is why this line was there. 

This should be fixed, but this is not the right fix.


---

Attachment

Excellent point.  I've done some more digging, and here's what I think is at the bottom of all this:


```
P.<a,b> = QQ[]
Q.<x> = PolynomialRing(P)
F = P.fraction_field()
f=F(a)*x
Q(f)
```


returns


```
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/opt/sage-2.8.12/devel/sage-alex/sage/matrix/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in __call__(self, x, check, is_gen, construct, absprec)
    240         C = self.__polynomial_class
    241         if absprec is None:
--> 242             return C(self, x, check, is_gen, construct=construct)
    243         else:
    244             return C(self, x, check, is_gen, construct=construct, absprec = absprec)

/opt/sage-2.8.12/devel/sage-alex/sage/matrix/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__init__()

/opt/sage-2.8.12/devel/sage-alex/sage/matrix/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)
    180         if isinstance(x, sage.rings.rational.Rational):
    181             return x
--> 182         return sage.rings.rational.Rational(x, base)
    183         
    184     def construction(self):

/opt/sage-2.8.12/devel/sage-alex/sage/matrix/rational.pyx in sage.rings.rational.Rational.__init__()

/opt/sage-2.8.12/devel/sage-alex/sage/matrix/rational.pyx in sage.rings.rational.Rational.__set_value()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.py in _rational_(self)
    270         Z = integer_ring.IntegerRing()
    271         try:
--> 272             return Z(self.__numerator) / Z(self.__denominator)
    273         except AttributeError:
    274             pass

/opt/sage-2.8.12/devel/sage-alex/sage/matrix/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: lift() takes exactly one argument (0 given)
```


The culprit is __call__ in multi_polynomial_libsingular.pyx, where the function tries a bunch of things and then, before giving up, tries to coerce a into QQ (which of course will not work).  Somehow our polynomial f is slipping through the cracks.  Note that this is a multivariable issue; the same thing works perfectly well over QQ[a].

I don't understand enough about how __call__ works to fix this properly.  I did however notice that, in this situation, working with the string 'a' fixes the issue.  I'm replacing the old patch with a very simple one that does this, but someone with more experience with these things should take a look at it.


---

Comment by cwitty created at 2008-02-16 02:10:48

The patch was changed after robertwb's review above, so somebody should look at the new patch.


---

Attachment


---

Comment by mhansen created at 2008-02-27 19:48:01

Apply both patches.  Works for me against 2.10.3.alpha0.


---

Comment by mabshoff created at 2008-02-28 00:24:02

Resolution: fixed


---

Comment by mabshoff created at 2008-02-28 00:24:02

Merged in Sage 2.10.3.rc0
