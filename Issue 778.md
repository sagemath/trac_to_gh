# Issue 778: Finite Field __call__ doesn't accept polynomials over F_p

Issue created by migration from Trac.

Original creator: roed

Original creation time: 2007-10-02 01:42:34

Assignee: somebody

CC:  alexghitza

Keywords: finite fields

Neither Givaro nor pari finite fields accept polynomial arguments.


---

Comment by roed created at 2007-11-03 19:07:05

Sorry, should have given an example.

sage: Q.<q> = GF(5^7)
sage: L = GF(5)
sage: LL.<xx> = L[]
sage: Q(xx^2 + 2*xx + 4)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/roed/<ipython console> in <module>()

/Users/roed/Math/sage/local/lib/python2.5/site-packages/sage/rings/finite_field.py in __call__(self, x)
    624                 return self(x.constant_coefficient())
    625             else:
--> 626                 raise TypeError, "no coercion defined"
    627 
    628         elif isinstance(x, str):

<type 'exceptions.TypeError'>: no coercion defined


---

Comment by was created at 2007-11-03 20:01:34


```
Sorry.
sage: Q.<q> = GF(5^7)
sage: L = GF(5)
sage: LL.<xx> = L[]
sage: Q(xx^2 + 2*xx + 4)
---------------------------------------------------------------------------
<type 'exceptions.TypeError '>             Traceback (most recent call last)

/Users/roed/<ipython console> in <module>()

/Users/roed/Math/sage/local/lib/python2.5/site-packages/sage/rings/finite_field.py in __call__(self, x)
    624                 return self(x.constant_coefficient())
    625             else:
--> 626                 raise TypeError, "no coercion defined"
    627
    628         elif isinstance(x, str):

<type 'exceptions.TypeError'>: no coercion defined
- Show quoted text -
```



---

Comment by cremona created at 2008-02-18 11:47:49

I don't understamd what you expect to be done here.  How can you coerce a polynomial over GF(5) into the field GF(5**7)?  If you mean to coerce it into a polynomial over GF(5**7) then do this:

```
sage: PolynomialRing(Q,x)(xx^2 + 2*xx + 4)
x^2 + 2*x + 4
```


or this:

```
sage: f=LL.base_extend(Q)(xx^2 + 2*xx + 4)
sage: f
xx^2 + 2*xx + 4
sage: f.parent()
Univariate Polynomial Ring in xx over Finite Field in q of size 5^7
```


Can roed explain?  Otherwise I vote for this to be closed.


---

Comment by was created at 2008-02-19 00:08:36

David wants something like one has with quotients of polynomial rings, since finite extension fields can be thought of as polynomial quotient rings.  E.g.,:


```
sage: R.<x> = GF(5)[]
sage: Q.<q> = R.quotient(x^7 + 3*x + 3)
sage: Q(x^2 + 2*x + 4)
q^2 + 2*q + 4
```


I think this is a reasonable request, since there is a natural ring homomorphism
from GF(5)['x'] to GF(5^7), when the GF(5^7) is presented as an explicit quotient of a polynomial ring modulo an irred. polynomial, as our are. 

 -- William


---

Comment by cremona created at 2008-02-19 09:11:09

Now I understand.  In that case you can just evaluate the polynomial at the generator of the extension field:


```
sage: Q.<q> = GF(5^7)
sage: L = GF(5)
sage: LL.<xx> = L[]
sage: (xx^2 + 2*xx + 4)(q)
q^2 + 2*q + 4
```


So what roed wants is for Q(f) to evaluate as f(Q.gen()), where f is a polynomial over the base ring of Q.  That is now understandable, and reasonable, and presumably not hard to implement!


---

Attachment


---

Comment by cremona created at 2008-04-04 22:05:35

Attached patch (trac778.patch, based on 2.11) adds coercion of univariate polynomials into finite field elements, for all three finite field classes, with extra doctests.


---

Comment by mhansen created at 2008-04-04 22:18:22

Looks good to me.


---

Comment by mabshoff created at 2008-04-04 22:29:41

Merged in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-04 22:29:41

Resolution: fixed
