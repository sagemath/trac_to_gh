# Issue 7927: Extend coleman integration to handle Weierstrass points

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-01-14 06:53:58

Assignee: was

CC:  jen




---

Comment by robertwb created at 2010-01-14 06:54:39

some code, probably needs to be cleaned up


---

Attachment

more Weierstrass code


---

Comment by jen created at 2010-01-15 14:05:39

Here's a first attempt at some more code, with a little bit of overlap with Robert's code. I like his incorporation of the non-Teichmuller algorithm as an optional parameter in the main Coleman integral function, so we can mostly ignore what I do instead.

The main functions of interest are 
coleman_integral_from_weierstrass_via_boundary and
coleman_integral_from_weierstrass ; the latter can only be used for odd differentials, while the former is pretty slow, dependent on p-adic extensions. 

The auxiliary functions (e.g., P_to_S, S_to_Q, etc.) aren't likely to be of much interest to the user, but they give us good consistency checks. I'd appreciate input on renaming/restructuring things.

And my apologies for the messed-up line breaks in hyperelliptic_generic -- just noticed them now, but boxen.math (where I've been editing) has been difficult to access in the last hour from Guam. I can fix this (my) tomorrow morning.


---

Attachment

apply after 13535 to fix line break problems


---

Comment by kedlaya created at 2010-01-30 06:50:43

Changing status from new to needs_work.


---

Comment by kedlaya created at 2010-01-30 06:50:43

The overlap needs to be taken care of somehow. It might be easiest for Jen to incorporate whatever is appropriate from Robert's patch.

I'm dubious about the treatment of points in the infinite disc, on several counts. One is whether the Frobenius gets the y-coordinate right, since I think in both patches the check passes for trivial reasons whether or not the y-coordinate is right. Under Robert's patch, one gets lucky: you win as long as the square root of a p-adic number with unit part congruent to 1 mod p is guaranteed to be congruent to 1 mod p. This is undocumented but appears to be true. Under Jen's patch, one does not get lucky:

```
sage: K = pAdicField(11, 5)
sage: x = polygen(K)
sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
sage: P = C.lift_x(11^(-2))
sage: C.frobenius(P)
(11^-22 + O(11^-17) : 10*11^-55 + 10*11^-54 + 10*11^-53 + 10*11^-52 + 10*11^-51 + O(11^-50) : 1 + O(11^5))
```


More seriously, computing Coleman integrals even between two points in the infinite disc seems to be broken. Under Robert's patch, we have:

```
sage: K = pAdicField(11, 5)
sage: x = polygen(K)
sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
sage: P = C.lift_x(11^(-2))
sage: Q = C.lift_x(3*11^(-2))
sage: C.tiny_integrals_on_basis(P,Q)
[9*11^3 + 11^4 + 2*11^5 + 2*11^6 + 11^7 + O(11^8), 11^2 + 5*11^4 + 3*11^5 + O(11^6), 8*11^-1 + 5 + 5*11 + 5*11^2 + 6*11^3 + O(11^4), 10*11^-3 + 3*11^-2 + 7*11^-1 + 5 + 8*11 + O(11^2)]
sage: C.coleman_integrals_on_basis(P, Q)
(10*11^-102 + 2*11^-101 + 9*11^-100 + 3*11^-99 + O(11^-98), 8*11^-102 + 2*11^-101 + 2*11^-100 + O(11^-98), 10*11^-103 + 8*11^-102 + 3*11^-101 + 6*11^-100 + 7*11^-99 + O(11^-98), 2*11^-103 + 5*11^-102 + 8*11^-100 + 5*11^-99 + O(11^-98))
```

The last two lines should be the same; right now, they aren't even of the same return type (one is a list, one is a tuple).

Under Jen's patch, the last call returns an error instead:

```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/scratch/sage-4.3.2.alpha0/<ipython console> in <module>()

/scratch/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.pyc in coleman_integrals_on_basis(self, P, Q)
    136 
    137         prof("tiny integrals")
--> 138         TP = self.teichmuller(P)
    139 #        print "TP", TP
    140         P_to_TP = V(self.tiny_integrals_on_basis(P, TP))

/scratch/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.pyc in teichmuller(self, P)
    117         """
    118         K = P[0].parent()
--> 119         x = K.teichmuller(P[0])
    120         pts = self.lift_x(x, all=True)
    121         p = K.prime()

/scratch/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/rings/padics/padic_generic.pyc in teichmuller(self, x, prec)
    376             prec = min(Integer(prec), self.precision_cap())
    377         ans = self(x, prec)
--> 378         ans._teichmuller_set()
    379         return ans
    380 

/scratch/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/rings/padics/padic_capped_relative_element.so in sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement._teichmuller_set (sage/rings/padics/padic_capped_relative_element.c:17195)()

ValueError: cannot set negative valuation element to Teichmuller representative.
```



---

Comment by kedlaya created at 2010-01-30 12:06:36

Followup: the p-adic square root is computed using pari, which always chooses the branch of the square root so that the leading p-adic digit is in [0, p/2]. So Robert's treatment of the ambiguity does seem to work.


---

Comment by jen created at 2010-02-07 16:33:55

merged Robert's patch with mine, though still a work in progress


---

Attachment

fixing precision issues in the infinite disc


---

Comment by kedlaya created at 2010-02-16 23:18:36

The good news is, this looks fine on mathematical grounds. However, there are a few procedural issues before I can issue a positive review.

I am getting some doctest failures in hyperelliptic_padic_field.py. I think the problem is the indentation in the doctest for is_same_disc. If I fix that by hand, the doctests all pass.

In other news, coverage checking points up some missing documentation/doctests.
For hyperelliptic_padic_field.py:

```
Missing documentation:
	 * invariant_differential(self):

Missing doctests:
	 * is_in_weierstrass_disc(self,P):
	 * is_weierstrass(self,P):
	 * tiny_integrals(self, F, P, Q):
```

For hyperelliptic_generic.py:

```
Missing documentation:
	 * __init__(self, PP, f, h=None, names=None, genus=None):
	 * change_ring(self, R):
	 * __cmp__(self, other):
	 * lift_x(self, x, all=False):
	 * genus(self):
	 * jacobian(self):
	 * monsky_washnitzer_gens(self):

Missing doctests:
	 * local_coord(self, P, prec = 20, name = 't'):

Possibly wrong (function name doesn't occur in doctests):
	 * _repr_(self):
	 * _magma_init_(self, magma):
```

Of these, the ones that are new (is_in_weierstrass_disc, is_weierstrass, and maybe some others) absolutely need doctests. Improving the coverage for older functions would be helpful but is not an obstacle to a positive review on this ticket (we could create a separate ticket for that).

Another minor note: various release managers have requested that the commit line for patches start with the number of the relevant ticket, e.g.,

#7927: Extend coleman integration to handle Weierstrass points

This is helpful in case a rollback is needed after applying a whole bunch of disparate patches. This comment can be ignored unless you decide to build a single patch encompassing all of the changes so far.


---

Comment by kedlaya created at 2010-02-17 16:07:50

It appears I spoke to soon. An example which used to work but is now broken:

```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x^3+1)
sage: K = Qp(5,8)
sage: HK = H.change_ring(K)                                              
sage: P = HK(0,1)                                                        
sage: Q = HK.lift_x(5)                                                   
sage: HK.tiny_integrals_on_basis(P,Q)                                    
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/r1/kedlaya/.sage/temp/dwork.mit.edu/31681/_home_r1_kedlaya__sage_init_sage_0.py in <module>()

/scratch/sage-4.2.1/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.pyc in tiny_integrals_on_basis(self, P, Q)
    298         R = PolynomialRing(self.base_ring(), ['x', 'y'])
    299         x, y = R.gens()
--> 300         return self.tiny_integrals([x**i for i in range(2*self.genus())], P, Q)
    301 
    302                

/scratch/sage-4.2.1/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.pyc in tiny_integrals(self, F, P, Q)
    250         P and Q MUST be in the same residue disk for this result to make sense. 
    251         """
--> 252         x, y, z = self.local_analytic_interpolation(P, Q)  #homogeneous coordinates
    253         x = x/z
    254         y = y/z

/scratch/sage-4.2.1/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.pyc in local_analytic_interpolation(self, P, Q)
     82         """
     83         prec = self.base_ring().precision_cap()
---> 84         if self.is_same_disc(P,Q) == False:
     85             raise ValueError, "%s and %s are not in the same residue disc"%(P,Q)
     86         disc = self.residue_disc(P)

/scratch/sage-4.2.1/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.pyc in is_same_disc(self, P, Q)
    238             False        
    239         """
--> 240         if self.residue_disc(P) == self.residue_disc(Q):
    241             return True
    242         else:

/scratch/sage-4.2.1/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.pyc in residue_disc(self, P)
    203         yPv = P[1].valuation()
    204         F = self.base_ring().residue_field()
--> 205         HF = self.change_ring(F)
    206         if P == self(0,1,0):
    207             return HF(0,1,0)

/scratch/sage-4.2.1/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_generic.pyc in change_ring(self, R)
     78         y = self._printing_ring.gen()
     79         x = self._printing_ring.base_ring().gen()
---> 80         return HyperellipticCurve(f.change_ring(R), h, "%s,%s"%(x,y))
     81 
     82     def _repr_(self):

/scratch/sage-4.2.1/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/constructor.pyc in HyperellipticCurve(f, h, names, PP)
     94             return HyperellipticCurve_g2_finite_field(PP, f, h, names=names, genus=g)
     95         else:
---> 96             return HyperellipticCurve_finite_field(PP, f, h, names=names, genus=g)
     97     elif is_RationalField(R):
     98         if g == 2:

/scratch/sage-4.2.1/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_generic.pyc in __init__(self, PP, f, h, names, genus)
     66             names = names.split(",")
     67         self._names = names
---> 68         P1 = PolynomialRing(R,name=names[0])
     69         P2 = PolynomialRing(P1,name=names[1])
     70         self._PP = PP

/scratch/sage-4.2.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name, implementation)
    341                 raise TypeError, "if second arguments is a string with no commas, then there must be no other non-optional arguments"
    342             name = arg1
--> 343             R = _single_variate(base_ring, name, sparse, implementation)
    344         else:
    345             # 2-4. PolynomialRing(base_ring, names, order='degrevlex'):

/scratch/sage-4.2.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in _single_variate(base_ring, name, sparse, implementation)
    393 def _single_variate(base_ring, name, sparse, implementation):
    394     import sage.rings.polynomial.polynomial_ring as m
--> 395     name = normalize_names(1, name)
    396     key = (base_ring, name, sparse, implementation)
    397     R = _get_from_cache(key)

/scratch/sage-4.2.1/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.normalize_names (sage/structure/parent_gens.c:2089)()

/scratch/sage-4.2.1/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens._certify_names (sage/structure/parent_gens.c:1647)()

ValueError: variable names must be alphanumeric, but one is '(1 + O(5^8))*x' which is not.
```



---

Comment by kedlaya created at 2010-02-17 17:19:26

Replying to [comment:5 kedlaya]:
> It appears I spoke to soon. An example which used to work but is now broken:
...

This failure occurred using 4.2.1. I can't reproduce it using 4.3.3.alpha0, so it may be an artifact.


---

Comment by jen created at 2010-02-18 16:45:19

fixing things in comment #4 (doctests, etc.)


---

Attachment

doctesting exceptions; formatting of docstrings


---

Attachment


---

Comment by jen created at 2010-02-19 01:58:31

Changing status from needs_work to needs_review.


---

Comment by jen created at 2010-02-19 15:26:27

removed coleman_integrals_on_basis in ell_padic_field.py


---

Attachment

After applying 13535.patch through 13541.patch against 4.3.3.alpha0, I get no long doctest failures anywhere in sage/schemes/. Positive review.

For other issues with Coleman integration, see tickets #8304 and #8305.


---

Comment by kedlaya created at 2010-02-19 16:08:16

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-03 14:40:32

Resolution: fixed


---

Comment by mvngu created at 2010-03-03 14:40:32

Merged in this order:

 1. [13535.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7927/13535.patch)
 1. [13536.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7927/13536.patch)
 1. [13537.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7927/13537.patch)
 1. [13538.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7927/13538.patch)
 1. [13539.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7927/13539.patch)
 1. [13540.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7927/13540.patch)
 1. [13541.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7927/13541.patch)

Jennifer: you should put the ticket number in your patch.


---

Comment by jdemeyer created at 2017-11-22 13:39:27

What's up with this condition:

```
            x = f.parent().variable_name()
            if x!='a' :  #this is to distinguish between extensions of Qp that are finite vs. not
```

I totally cannot understand why you check whether the variable name is `"a"`. That makes no sense to me.


---

Comment by jdemeyer created at 2017-11-22 14:10:42

See #24267 for a follow-up.
