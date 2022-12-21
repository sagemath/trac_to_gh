# Issue 6551: fix ugliness in printing of multivariate polynomials

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-07-18 00:25:01

Assignee: tbd

CC:  malb

Keywords: print latex multivariate polynomial

The printing (and latex-ing) of multivariate polynomials is sometimes quite ugly, and inconsistent with the much prettier printing of univariate polynomials.  One gets things like the following (taken from doctests in the Sage library):


```
(-6/5)*x^2*y^2 + (-3)*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 + (-18)*y^2 + (-3/4)*y
```


or even


```
sage: xgcd((b+g)*y^2, (a+g)*y+b)
((b^3 + (g)*b^2)/(a^2 + (2*g)*a + 3), 1, ((-b + (-g))/(a + (g)))*y + (b^2 + (g)*b)/(a^2 + (2*g)*a + 3))
```


The attached patch fixes this, factors out common code for printing and latex-ing, and makes printing consistent across various representations of multivariate polynomials.



---

Attachment


---

Comment by AlexGhitza created at 2009-07-18 00:26:40

Changing assignee from tbd to AlexGhitza.


---

Comment by AlexGhitza created at 2009-07-18 00:26:40

Changing status from new to assigned.


---

Comment by davidloeffler created at 2009-07-20 08:43:03

Bad news: this conflicts quite severely with my patches at #6500. I feel a bit guilty about this, because it was my referee comments on #6183 that pushed you into working on this, so I will handle preparing a rebased version.


---

Attachment

apply after the three patches at #6500


---

Comment by davidloeffler created at 2009-07-20 09:15:30

Here's a patch that applies cleanly on top of the #6500 patches. For what it's worth, the patch looks fine to me, but I'm not an expert on multivariate commutative algebra so probably it'd be better to get someone else to review it.


---

Comment by davidloeffler created at 2009-07-20 10:59:01

Hi Alex,

I decided to run all doctests just to check that I had rebased the patch correctly, but there seems to be some funny business in quaternion algebras. This is with the #6500 patches and the rebased patch here, applied to 4.1:


```
sage -t  "devel/sage/sage/algebras/quaternion_algebra_element.py"                                      
**********************************************************************                                 
File "/home/david/sage-4.1/devel/sage/sage/algebras/quaternion_algebra_element.py", line 17:           
    sage: sage.algebras.quaternion_algebra_element.unpickle_QuaternionAlgebraElement_generic_v0(*t)    
Expected:                                                                                              
    2/3 + X*i - X^2*j + X^3*k                                                                          
Got:                                                                                                   
    2/3 + X*i + (-X^2)*j + X^3*k                                                                       
**********************************************************************                                 
```

and

```
**********************************************************************                                 
File "/home/david/sage-4.1/devel/sage/sage/algebras/quatalg/quaternion_algebra.py", line 455:          
    sage: QuaternionAlgebra(GF(17)(2),3).random_element()                                              
Expected:                                                                                              
    11 + 16*i + 4*j + 13*k                                                                             
Got:                                                                                                   
    11 - i + 4*j + 13*k                                                                                
**********************************************************************                                 
```


This has nothing to do with the rebasing, because I ran these two tests again using your original patch and without the #6500 patches and they failed in exactly the same way. Any idea what is going on here?

David


---

Comment by AlexGhitza created at 2009-07-20 14:04:29

Hi David,

I just checked and I'm getting the same failures as you both on my laptop and sage.math (which is weird because I could swear I tested this about a million times).

I have an inkling of what might be going on but it's going to have to wait until tomorrow because I'm falling asleep in my chair.

Thanks for reviewing, and for the work you put in rebasing the patch.


---

Attachment


---

Comment by AlexGhitza created at 2009-07-21 00:56:35

Yes, the problem was indeed that I was mixing up some stuff with #6183.

I've added a small patch that takes care of this, and all tests (should) now pass.


---

Comment by malb created at 2009-08-18 09:55:18

Unfortunately, the patch has bit-rotted:


```
applying trac_6551-rebased_for_6500.patch
patching file sage/matrix/matrix_mpolynomial_dense.pyx
Hunk #1 FAILED at 0
1 out of 6 hunks FAILED -- saving rejects to file sage/matrix/matrix_mpolynomial_dense.pyx.rej
patching file sage/rings/polynomial/polydict.pyx
Hunk #5 succeeded at 887 with fuzz 1 (offset 0 lines).
patching file sage/rings/polynomial/toy_buchberger.py
Hunk #1 FAILED at 53
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/toy_buchberger.py.rej
patching file sage/schemes/elliptic_curves/ell_curve_isogeny.py
Hunk #7 FAILED at 1864
1 out of 21 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_curve_isogeny.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_6551-rebased_for_6500.patch
```


I read the patch and it looks fine so far. It is mainly a question of taste anyway IMHO. However, it might be worth checking for performance loses due to this patch (conversion to strings is used to communicate with Singular for instance)


---

Comment by malb created at 2009-08-26 17:16:38

After thinking about this some more time: I think the proposed implementation for libSingular polynomials is way too slow. I suggest someone (e.g. me) re-implements the PolyDict printing for those to make it reasonably efficient.


---

Comment by AlexGhitza created at 2009-08-26 23:19:45

Martin,

Thanks for looking at this carefully, and sorry for having left things somewhat half-baked.  In my defense, I had already spent a long time getting the formatting to be consistent, and I'm not sure I'd be very good at speed issues.  But I completely agree with you that this is ubiquitous code that should be fast.  Count on me to referee your implementation when you're done with it.


---

Comment by bruno created at 2016-04-13 14:28:52

This ticket seems invalid. For the first example:


```python
sage: R.<x,y> = QQ[]
sage: p = (-6/5)*x^2*y^2 + (-3)*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 + (-18)*y^2 + (-3/4)*y
sage: p
-6/5*x^2*y^2 - 3*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 - 18*y^2 - 3/4*y
```


I cannot make the second example work (and this does not appear in the doctests).


---

Comment by bruno created at 2016-04-18 08:46:25

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2016-06-12 12:02:30

Resolution: fixed
