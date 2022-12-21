# Issue 3812: add apply_morphism to ideal

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-08-12 05:30:18

Assignee: malb

Keywords: ideal apply_morphism morphism apply

apply_morphism is so useful on matrices, and I didn't know that psi(J) was valid for ideals -- so here is documentation and tests for both functions for general ideals.


---

Attachment


---

Comment by was created at 2008-08-13 02:48:54

The __call__ method on morphisms implements the same thing already.

```
sage: psi = CC['x'].hom([-CC['x'].0]) 
sage: J = ideal([CC['x'].0 + 1]); J 
Principal ideal (1.00000000000000*x + 1.00000000000000) of Univariate Polynomial Ring in x over Complex Field with 53 bits of precision
sage: psi(J)
Principal ideal ((-1.00000000000000)*x + 1.00000000000000) of Univariate Polynomial Ring in x over Complex Field with 53 bits of precision
```


Thus it seems to me that  the following three lines 


```
 	337	        R = phi.codomain() 
 	338	        image = R.ideal([phi(z) for z in self.gens()]) 
 	339	        return image 
```


should be replaced by

```
return phi(R)
```


 -- William


---

Attachment

`3812-ncalexan-number-field-ideal-apply-morphism-2.patch` replaces earlier patch and addresses referee comment.


---

Comment by malb created at 2008-08-18 14:06:34

Changing assignee from malb to ncalexan.


---

Comment by cremona created at 2008-08-23 17:54:43

In view of William's comment that this already works, do we need the patch at all?  In other words, why implement a function I.apply_morphism(tau) when all it does is tau(I)?

Having said that, the patch does apply ok and works.


---

Comment by mabshoff created at 2009-04-06 05:56:05

John: Is this a positive review? I am changing this to "needs review" so it is picked up by the right reports.

Cheers,

Michael


---

Attachment

Apply after previous patch


---

Comment by cremona created at 2009-04-06 09:35:32

Apologies.  My original thought had been that this was unnecessary, but now (in the light of many more months of Sage experience) I can see that it is a Good Thing, since anyone with an ideal can now see that apply_morphism() is something valid to do to the ideal.

The patch applies fine to 3.4.1.rc0.  Some doctests needed purely cosmetic adjustments (halrdly surprising after 8 months) which are in the patch 3812_doctest.patch (which need to be applied after Nick's patch).


---

Comment by mabshoff created at 2009-04-11 00:58:16

Ok, looking at all the patches it seems that 3812_doctest.patch contains the previous latest release of Nick's patch with the doctest fix by John. The credit of the patch still goes to Nick, so assuming this patch only passes doctests for me I will merge it shortly. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-11 01:04:46

Resolution: fixed


---

Comment by mabshoff created at 2009-04-11 01:04:46

Merged 3812_doctest.patch *only* in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by cremona created at 2009-04-11 13:46:47

Replying to [comment:9 mabshoff]:
> Merged 3812_doctest.patch *only* in Sage 3.4.1.rc2.
> 
> Cheers,
> 
> Michael
Sorry for the confusion: you are right, 100% credit to Nick and the last patch on its own includes his original plus my trivial fix.  John
