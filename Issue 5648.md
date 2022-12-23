# Issue 5648: Multiplication for modular forms

Issue created by migration from https://trac.sagemath.org/ticket/5648

Original creator: davidloeffler

Original creation time: 2009-03-31 12:25:20

Assignee: davidloeffler

The attached patch implements !__mul!__ for ModularFormElement objects, so one can say

```
sage: M = ModularForms(DirichletGroup(3).0, 5)
sage: f = M.0
sage: f * f
```


and get back a modular form (in this case a weight 5 modular form of level 3 and trivial character).

In order to get this to work, I've made a few small adjustments elsewhere: 

* DirichletGroup objects now have a base_extend method

* a bug when multiplying two characters of the same modulus but different zeta orders is fixed

* Dirichlet characters now always compare as unequal unless they have the same modulus (in particular, == for Dirichlet characters is now transitive, which it previously wasn't)

* ambient spaces of modular forms with character now have a decent base_extend method (previously base_extend would forget the character and return an ambient space of modular forms for Gamma1(N)).



---

Attachment

patch against 3.4.1.alpha0


---

Comment by davidloeffler created at 2009-03-31 12:27:42

Changing status from new to assigned.


---

Comment by was created at 2009-03-31 14:10:58

Quick comment: I'm concerned the Sturm bound isn't enough when they are Eisenstein series (it's definitely enough for cusp forms):

```
	889	        m = newparent.sturm_bound() 
 	890	        newqexp = self.qexp(m) * other.qexp(m) 
 	891	         
 	892	        return newparent.base_extend(newqexp.base_ring())(newqexp) 
```

Maybe I'm just being dense at the moment.

You could remedy this by increasing m if a given value doesn't work.   There might (should) be a method on newparent that returns the actual precision needed to determine a q-expansion. 

I am happy with all the API changes you list in the ticket summary, including changing the meaning of equals for Dirichlet characters.


---

Comment by davidloeffler created at 2009-03-31 14:37:51

The function sturm_bound in sage.modular.dims is returning ceil( weight * index / 12), which is the Sturm bound for M_k(Gamma) according to theorem 9.18 in your book; so it should be fine for Eisenstein series.

(In fact, sage.modular.dims.sturm_bound for GammaH and Gamma1 is actually doing something a bit strange -- it calculates the Sturm bound for the corresponding Gamma0 and multiplies it by the index of the given group in Gamma0, so it is giving a wastefully high bound due to premature rounding. I noticed this, and fixed it, as part of #5180.) 

Ideally ModularForms(N, k).sturm_bound() and CuspForms(N, k).sturm_bound() should return different answers corresponding to the two statements in your theorem 9.18, in order to be really painfully efficient with not computing more terms than we need. Furthermore ModularForms(character, k).sturm_bound() should return the Buzzard-Sturm bound for forms of known character. (I think I might have already put the latter in #5180). But all this is optimisation; it should work fine as-is.


---

Comment by GeorgSWeber created at 2009-03-31 19:04:01

Looks good to me.

Keep pushing!

Cheers,
gsw


---

Comment by mabshoff created at 2009-03-31 20:17:30

Resolution: fixed


---

Comment by mabshoff created at 2009-03-31 20:17:30

Merged in Sage 3.4.1.rc0.

Cheers,

Michael
