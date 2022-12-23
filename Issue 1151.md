# Issue 1151: Bug in creating elements in multivariate quotient rings that cannot be coerced to singular

Issue created by migration from https://trac.sagemath.org/ticket/1151

Original creator: roed

Original creation time: 2007-11-12 00:16:56

Assignee: was

A.<x> = QQ[]
Gauss.<i> = A.quotient(x^2+1)
R.<c,d,X1,Y1,X2,Y2,Z1,Z2> = Gauss[]
S = R.quotient([(X1<sup>2+Y1</sup>2)*Z1<sup>2-c</sup>2*(Z1<sup>4+d*X1</sup>2*Y1^2),
                    (X2<sup>2+Y2</sup>2)*Z2<sup>2-c</sup>2*(Z2<sup>4+d*X2</sup>2*Y2^2)])
S(1)

Produces the traceback:
sage: S(1)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/users/spaces/zimmerma/try/<ipython console> in <module>()

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py in __call__(self, x, coerce)
   257             R = self.cover_ring()
   258             x = R(x)
--> 259         return quotient_ring_element.QuotientRingElement(self, x)
   260
   261     def _coerce_impl(self, x):

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py in __init__(self, parent, rep, reduce)
    70         self.__rep = rep
    71         if reduce:
---> 72             self._reduce_()
    73
    74     def _reduce_(self):

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py in _reduce_(self)
    74     def _reduce_(self):
    75         I = self.parent().defining_ideal()
---> 76         self.__rep = I.reduce(self.__rep)
    77
    78     def copy(self):

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in reduce(self, f)
   805
   806         try:
--> 807             singular = self._singular_groebner_basis().parent()
   808         except (AttributeError, RuntimeError):
   809             singular = self._singular_groebner_basis().parent()

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in _singular_groebner_basis(self)
   623             S = self.__singular_groebner_basis
   624         except AttributeError:
--> 625             G = self.groebner_basis()
   626             try:
   627                 return self.__singular_groebner_basis

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in groebner_basis(self, algorithm)
  1348                 return self._macaulay2_groebner_basis()
  1349             else:
-> 1350                 return self._groebner_basis_using_singular("groebner")
  1351         elif algorithm.startswith('singular:'):
  1352             return self._groebner_basis_using_singular(algorithm[9:])

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in _groebner_basis_using_singular(self, algorithm)
   565         except AttributeError:
   566             if algorithm=="groebner":
--> 567                 S = self._singular_().groebner()
   568             elif algorithm=="std":
   569                 S = self._singular_().std()

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in _singular_(self, singular)
   214         if singular is None: singular = singular_default
   215         try:
--> 216             self.ring()._singular_(singular).set_ring()
   217             I = self.__singular
   218             if not (I.parent() is singular):

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in _singular_(self, singular, force)
   169             return R
   170         except (AttributeError, ValueError):
--> 171             return self._singular_init_(singular, force)
   172
   173     def _singular_init_(self, singular=singular_default, force=False):

/local/spaces/logiciels/sage-2.8.10/p4/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in _singular_init_(self, singular, force)
   176         """
   177         if not self._can_convert_to_singular() and not force:
--> 178             raise TypeError, "no conversion of this ring to a Singular ring defined"
   179
   180         if self.ngens()==1:

<type 'exceptions.TypeError'>: no conversion of this ring to a Singular ring defined

The problem is that QQ[x]/(x^2+1) cannot be a base ring in singular, and when we try to reduce (in creating an element), we can't compute a Grobner basis.

We need to handle multivariable quotients better over general rings.  One solution would be to write a naive groebner basis implementation that works over an arbitrary ring.


---

Comment by AlexGhitza created at 2008-01-24 08:59:45

Changing component from algebraic geometry to commutative algebra.


---

Comment by AlexGhitza created at 2008-01-24 08:59:45

Changing assignee from was to malb.


---

Comment by malb created at 2008-01-24 11:24:13

I've got a possibly very stupid question first. Isn't 


```
sage: A.<x> = QQ[]
sage: Gauss.<i> = A.quotient(x^2+1)
```


equivalent to:


```
sage: A.<x> = QQ[]
sage: Gauss.<i> = NumberField(x^2+1)
```


? If so, then the base field can be coerced to Singular:


```
sage: R.<c,d,X1,Y1,X2,Y2,Z1,Z2> = Gauss[]
sage: S = R.quotient([(X1^2+Y1^2)*Z1^2-c^2*(Z1^4+d*X1^2*Y1^2),
....:                     (X2^2+Y2^2)*Z2^2-c^2*(Z2^4+d*X2^2*Y2^2)])
sage: S(1)
1
```


The behaviour described above would still be a bug but a different one.

Besides that detail, I have a 100% generic Gröbner basis implementation in pure Python (very very slow) that -- once integrated -- will resolve this bug for any base field (and ZZ).


---

Comment by malb created at 2008-01-24 11:24:13

Changing status from new to assigned.


---

Comment by was created at 2008-01-24 16:21:34

malb -- A number field is a totally different sort of object in Sage than
`A.quotient(x^2 + 1)`.   It happens that the two are  abstractly isomorphic, though, so whatever coercion you're thinking about can probably be made to work.


---

Attachment

after #2111 has been merged, this patch fixes the issue of this ticket


---

Comment by malb created at 2008-02-18 15:18:38

I claim that this issue was resolved in Sage 2.10.2.alpha0.


---

Comment by mabshoff created at 2008-02-18 15:27:08

When I apply trac_1151.patch the above example works, so if somebody gives it a positive review I will merge it.

Cheers,

Michael


---

Comment by malb created at 2008-02-27 13:03:02

patch still applies to 2.10.2 and make test passes.


---

Comment by burcin created at 2008-02-27 13:40:48

The patch looks good to me.

Maybe we should add the original example as a test somewhere, but where?


---

Comment by mabshoff created at 2008-02-27 23:20:14

Merged in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-27 23:20:14

Resolution: fixed
