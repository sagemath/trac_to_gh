# Issue 5307: Bug in conductor() over number fields

Issue created by migration from https://trac.sagemath.org/ticket/5307

Original creator: cremona

Original creation time: 2009-02-18 17:17:51

Assignee: was

Keywords: elliptic curve

There is something wrong in the conductor computation of an elliptic curve over a field of class number >1:


```
sage: K.<w>=NumberField(x^2+x+6)
sage: E=EllipticCurve([w,-1,0,-w-6,0])
sage: E.conductor()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/7547/_home_masgaj__sage_init_sage_0.py in <module>()

/local/jec/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.pyc in conductor(self)
    745         OK = self.base_ring().ring_of_integers()
    746         self._conductor = prod([d.prime()**(d.conductor_valuation()) \
--> 747                                 for d in self.local_data()],\
    748                                OK.ideal(1))
    749         return self._conductor

/local/jec/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.pyc in local_data(self, P, proof)
    394         if P is None:
    395             primes = self.base_ring()(self.discriminant()).support()
--> 396             return [self._get_local_data(pr, proof) for pr in primes]
    397
    398         from sage.schemes.elliptic_curves.ell_local_data import check_prime

/local/jec/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.pyc in _get_local_data(self, P, proof)
    416             pass
    417         from sage.schemes.elliptic_curves.ell_local_data import EllipticCurveLocalData
--> 418         self._local_data[P] = EllipticCurveLocalData(self, P, proof)
    419         return self._local_data[P]
    420

/local/jec/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_local_data.pyc in __init__(self, E, P, proof, algorithm)
    138                 self._reduction_type = Eint.ap(p) # = 0,-1 or +1
    139         else:
--> 140             self._Emin, ch, self._val_disc, self._fp, self._KS, self._cp, self._split = self._tate(proof)
    141             if self._fp>0:
    142                 if self._Emin.c4().valuation(p)>0:

/local/jec/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_local_data.pyc in _tate(self, proof)
    748                 a6 /= pi**6
    749                 verbose("Non-minimal equation, dividing out...\nNew model is %s"%([a1, a2, a3, a4, a6]), t, 1)
--> 750         C = C._tidy_model()
    751         return (C, p, val_disc, fp, KS, cp, split)
    752

/local/jec/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.pyc in _tidy_model(self)
    297             (a1, a2, a3, a4, a6) = [ZK(a) for a in self.a_invariants()]
    298         except TypeError:
--> 299             raise TypeError, "_tidy_model() requires an integral model."
    300         # N.B. Must define s, r, t in the right order.
    301         if ZK.degree() == 1:

TypeError: _tidy_model() requires an integral model.
```


I think I wrote most of the relevant code, so it is my fault and I will fix it!



---

Comment by cremona created at 2009-02-18 22:42:21

Diagnosis of the problem, while lies in the implementation of Tate's algorithm at a prime ideal P when P is not principal:  we use a uniformiser pi of P, but we use it in two different ways.  First, there are various places where integers (of the field) which are known to have valuation at least i are divided by `pi^i`.  Here, in order to keep everything integral, we use a uniformizer computed via K.uniformizer(P, 'negative'), which has valuation 1 at P (of course) and nagative or zero valuation elsewhere.  But there is a second way in which pi is used:  in computing the appropriate [u,r,s,t]-transforms.  For example, in one place we need an r-transform where r is 0 mod P but something specific mod `P^2`;  so we write r=r0*pi and compute r0 mod P and then multiply by pi.  But now, it matters if pi is not integral!

The solution I came up with was to compute two uniformisers, one (pi) as above and another (called ipi) integral at all primes.  I use the appropriate one in the appropriate places.

I made a patch to implement this, and the example above works fine (doctest added to conductor() in ell_number_field.py).

__But__ I think this needs to be looked at more carefully;  while it is no worse than before (and no different at all at principal primes) I don't think it is quite right yet.

NB Magma has essentially the same code (I wrote it) but is not fussy about integrality at all since it does not give local minimal models.


---

Comment by mabshoff created at 2009-03-01 02:26:51

Better luck in 3.4.1.

Cheers,

Michael


---

Attachment


---

Comment by cremona created at 2009-06-15 19:31:54

This patch fixes the problem.


---

Comment by ncalexan created at 2009-06-15 20:44:28

I can't say for sure that the new algorithm is correct, but I have read the code and I believe that the patch produces the behaviour John documented in the ticket and the comments.  It certainly fixes the presenting issue, so apply!


---

Comment by rlm created at 2009-06-24 09:50:45

Resolution: fixed
