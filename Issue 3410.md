# Issue 3410: [with patch, needs review] conversion of matrices over polynomial rings to magma is broken

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-06-13 05:29:44

Assignee: was

Attached patch fixes conversion of matrices over polynomial rings to magma.


---

Attachment

fix matrix conversion over polynomial ring to magma


---

Comment by was created at 2008-06-13 13:41:56

REPORT:

1. This directly conflicts with #3040

2. This patch will *massively suck* performance wise, since it changes _magma_ to make a call out to Magma for every single entry of a matrix.  Thus, e.g., converting a 500x500 matrix (which takes a reasonable amount of time with #3040) will go from one single  pexpect call to magma, to 250,000 separate pexpect calls to magma, which will take literally forever. 

For reason 2 this patch is not acceptable.


---

Attachment

fix conversion of matrices over polynomial rings to magma 2nd try


---

Comment by burcin created at 2008-06-14 00:15:03

attachment:trac3410-matrix_polyring_magma-2.patch addresses both of the problems pointed out in comment:1. It applies to 3.0.3.alpha2, doesn't call magma for each matrix element, and on the way probably optimizes conversion of polynomials to magma as well.


---

Comment by craigcitro created at 2008-06-15 21:55:04

Changing keywords from "" to "editor_craigcitro".


---

Comment by was created at 2008-06-20 04:05:07

REVIEW:

Great!  However the function 

```
def _magma_gens(self): 
```


needs documentation and doctests. 

Pending this big +1.


---

Attachment

conversion of matrices over polynomial rings to magma 3rd version


---

Comment by burcin created at 2008-06-26 15:36:13

attachment:trac3410-matrix_polyring_magma-3.patch adds doctests to `_magma_gens`. 

In the new patch, the `_magma_init_` method introduced in attachment:trac3410-matrix_polyring_magma-2.patch is moved to sage/rings/polynomial/                multi_polynomial.pyx. This allows us to remove the _magma_ method in MPolynomial_element and extends support of conversion of matrices over polynomial rings to rings not supported by libsingular. (I.e., now ZZ[x,y] is also supported.)


---

Comment by was created at 2008-07-01 06:46:54

REVIEW: 

  * Enthusiastic positive review.

  * Note to Mabshoff -- Just apply *only* trac3410-matrix_polyring_magma-3.patch -- don't apply either of the other patches (it took me like 10 minutes to figure this out).


---

Comment by mabshoff created at 2008-07-02 19:23:54

Resolution: fixed


---

Comment by mabshoff created at 2008-07-02 19:23:54

Merged trac3410-matrix_polyring_magma-3.patch in Sage 3.0.4.alpha2
