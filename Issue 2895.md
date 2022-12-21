# Issue 2895: [with patch, needs review] add support for Laurent polynomials in Sage

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-04-12 11:20:24

Assignee: somebody

David Roe did the initial implementation, and Jason Bandlow and I cleaned it up and got it ready for inclusion.


---

Comment by mabshoff created at 2008-04-13 02:57:45

Applying this to my alpha4 merge tree I get a bunch of doctest failures:

```
        sage -t -long devel/sage/sage/schemes/generic/morphism.py # 2 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/pbori.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_element.py # 4 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 2 doctests failed
        sage -t -long devel/sage/sage/rings/quotient_ring_element.pyx # 9 doctests failed
        sage -t -long devel/sage/sage/rings/ring.pyx # 5 doctests failed
        sage -t -long devel/sage/sage/rings/quotient_ring_element.py # 13 doctests failed
        sage -t -long devel/sage/sage/rings/quotient_ring.py # 16 doctests failed
        sage -t -long devel/sage/sage/rings/morphism.pyx # 11 doctests failed
        sage -t -long devel/sage/sage/rings/homset.py # 5 doctests failed
        sage -t -long devel/sage/sage/ext/interactive_constructors_c.pyx # 4 doctests failed
```

The issue in most of not all cases seems to be:

```
AttributeError: 'QuotientRing_generic' object has no attribute '_print_element'
```


Cheers,

Michael


---

Comment by bump created at 2008-04-13 03:19:40

If the base ring is a field of rational functions 
in another indeterminate I encounter a problem:

sage: P.<q>=QQ[]
sage: F = FractionField(P)
sage: R.<x,y> = LaurentPolynomialRing(F,2); R
Multivariate Laurent Polynomial Ring in x, y over Fraction Field of Univariate Polynomial Ring in q over Rational Field
sage: (x+1/y)^2

This would work if F = QQ but not for this field of fractions.

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '/': 'Integer Ring' and 'Multivariate Laurent Polynomial Ring in x, y over Fraction Field of Univariate Polynomial Ring in q over Rational Field'


---

Comment by bump created at 2008-04-13 04:04:42

To elaborate, 1/y raises an error if the base ring is ZZ, a polynomial
ring or a field of fractions of a polynomial ring.

HOWEVER y^(-1) can be used in its place, and no error result.

This may be acceptable.


---

Comment by bump created at 2008-04-13 04:58:16

Regarding the exceptions in schemes/generic/morphisms.py that mabshoff reported
I can confirm that they appear if only the patch 2895.1 is applied to unaltered
alpha3.


---

Comment by bump created at 2008-04-13 20:56:59

Here's what appears to have happened. The old QuotientRingElement is in
rings/quotient_ring_element.py and it contains the following:


```
    def _repr_(self):
        from sage.structure.parent_gens import localvars
        P = self.parent()
        R = P.cover_ring()
        # We print by temporarily (and safely!) changing the variable
        # names of the covering structure R to those of P.
        # These names get changed back, since we're using "with".
        with localvars(R, P.variable_names(), normalize=False):
            return str(self.__rep)
```


The new version is in the file quotient_ring_elements.pyx. The
above code will not work in cython. In its place, we find:


```
     def _repr_(self):
         self._reduce_()
         return self.parent()._print_element(self)
```


But the parent quotient ring has no method _print_element.


---

Attachment


---

Comment by mhansen created at 2008-04-18 05:40:21

I put up some new patches which remove the conversion of quotient_ring_element.py to Cython.


---

Comment by mabshoff created at 2008-04-18 07:14:05

The new patch passes doctests when applied against my 3.0.alpha6 merged tree. Now we need a positive review to get this merged.

Cheers,

Michael


---

Comment by bump created at 2008-04-18 15:52:38

An issue with putting this patch in close to release of 3.0 is whether it could break anything. Revised by mhansen it does not convert quotient_polynomial_element to cython as the previous patch did. Moreover after importing both revised 2895-1.patch and 2895-2.patch I read the diffs carefully and there is nothing that alters any existing functionality. So the patch is safe from this point of view.

I tested it and it seems to work as it should.

I don't think substitution is working yet. In a multivariate polynomial ring you can do:
sage: g=(q+u)*(q+v)
sage: g.substitute(u=1)
(q + 1)*v + q^2 + q
In the Laurent polynomial ring this raises an exception.

This is not a reason not to include the patch. Substitution can be implemented later. 

I recommend acceptance.


---

Attachment


---

Comment by mhansen created at 2008-04-18 18:56:15

Changing status from new to assigned.


---

Comment by mhansen created at 2008-04-18 18:56:15

I've added a patch which makes .substitute() work and .subs() work with dictionary arguments.


---

Comment by mhansen created at 2008-04-18 18:56:15

Changing assignee from somebody to mhansen.


---

Comment by bump created at 2008-04-18 19:11:15

Substitution works if the ground ring is QQ but the
following returns an exception:

```
sage: R.<q>=QQ[]
sage: L.<x,y,z> = LaurentPolynomialRing(R)
sage: f=(x+y+z^-1)^2
sage: f.substitute(z=1)
```

I repeat that my review is positive and I'd urge these patches to be merged in alpha6.


---

Comment by mhansen created at 2008-04-18 19:27:32

Thanks for testing this out Dan. 

The underlying problem is with coercing between elements of a fraction field and the Laurent polynomial ring.  I'm not familiar enough with the coercion system so I'll send an email to David Roe since he probably knows exactly how to fix it.


---

Comment by mabshoff created at 2008-04-18 20:22:25

Ok, I consider this a positive review by Dan Bump and will merge this as is into 3.0.alpha6.

Mike: can you open a ticket for the coercion issue and make it a blocker for 3.0. We might get the patch in if David or somebody else comes up with patch in time. If not there is still 3.0.x ;)


---

Comment by mabshoff created at 2008-04-18 20:22:41

Resolution: fixed


---

Comment by mabshoff created at 2008-04-18 20:22:41

Merged in Sage 3.0.alpha6
