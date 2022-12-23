# Issue 1786: coercion error with fraction field of multivariate polynomials

Issue created by migration from https://trac.sagemath.org/ticket/1786

Original creator: mhansen

Original creation time: 2008-01-15 19:19:10

Assignee: malb


```
vars = ",".join([ 'c%s'%i for i in range(1, 23)])
BR  = QQ[ 't,'+vars ].fraction_field()
t = BR.gens()[0]
MS = MatrixSpace(BR, 3, 3)

def x(alpha, k, c):
    m = MS(1)
    if alpha == 'a1':
        m[0,1] = BR(c*t^k)
    elif alpha == 'a2':
        m[1,2] = BR(c*t^k)
    elif alpha == 'phi':
        m[0,2] = BR(c*t^k)
    elif alpha == '-a1':
        m[1,0] = BR(c*t^k)
    elif alpha == '-a2':
        m[2,1] = BR(c*t^k)
    elif alpha == '-phi':
        m[2,0] = BR(c*t^k)
    return m
    
    
def n(alpha, k, c):
    if alpha[0] == '-':
        minusalpha = alpha[1:]
    else:
        minusalpha = "-"+alpha
    return x(alpha, k, c)*x(minusalpha,-k,-1/c)*x(alpha, k, c)
    
n0 = n('-phi', 1, 1)

n0*~n0
```


gives


```

/home/mike/<ipython console> in <module>()

/home/mike/element.pyx in sage.structure.element.Matrix.__mul__()

/home/mike/matrix0.pyx in sage.matrix.matrix0.Matrix._matrix_times_matrix_c_impl()

/home/mike/matrix_generic_dense.pyx in sage.matrix.matrix_generic_dense.Matrix_generic_dense._multiply_classical()

/home/mike/element.pyx in sage.structure.element.ModuleElement.__add__()

/home/mike/coerce.pxi in sage.structure.element._add_c()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.py in _add_(self, right)
    249         if self.parent().is_exact():
    250             try:
--> 251                 gcd_denom = self.__denominator.gcd(right.__denominator)
    252                 if not gcd_denom.is_unit():
    253                     right_mul = self.__denominator // gcd_denom

/home/mike/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.gcd()

/home/mike/parent.pyx in sage.structure.parent.Parent._coerce_c()

/home/mike/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular._coerce_c_impl()

/home/mike/parent.pyx in sage.structure.parent.Parent._coerce_c()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/rational_field.py in _coerce_impl(self, x)
    199                           sage.rings.rational.Rational)):
    200             return self(x)
--> 201         raise TypeError, 'no implicit coercion of element to the rational numbers'
    202         
    203     def coerce_map_from_impl(self, S):

<type 'exceptions.TypeError'>: no implicit coercion of element to the rational numbers

```



---

Attachment


---

Comment by mhansen created at 2008-01-16 01:20:59

Changing assignee from malb to mhansen.


---

Comment by mhansen created at 2008-01-16 01:20:59

The issue was that _pow_ was creating a new fraction field element with the numerator and denominator as fraction field elements rather than elements of the underlying ring.


---

Comment by mhansen created at 2008-01-16 01:20:59

Changing status from new to assigned.


---

Comment by cwitty created at 2008-01-16 02:04:18

Looks good to me.  (Patch looks good, doctests pass in rings/.)


---

Comment by mabshoff created at 2008-01-16 02:13:58

Merged in Sage 2.10.alpha4


---

Comment by mabshoff created at 2008-01-16 02:13:58

Resolution: fixed
