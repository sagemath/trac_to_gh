# Issue 5680: Use new bits from FLINT 1.2.4 (followup to #5240)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-04 05:19:10

Assignee: malb

CC:  burcin wbhart

Now that FLINT 1.2.4 is in Sage we should hook up various new methods:

 * factor
 * square free factoring
 * derivative
 * powermod

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-04 22:33:10

Bill suggested that I also CC Burcin on this ticket so he knows that it exists :)

Cheers,

Michael


---

Comment by burcin created at 2009-10-20 14:44:05

Changing component from misc to basic arithmetic.


---

Comment by burcin created at 2009-10-20 14:44:05

I attached a patch that exposes some more functionality from FLINT and adds a function for rational reconstruction to zmod_poly wrappers. Changes include:

 * factor
 * is_irreducible
 * scalar multiplication
 * is_irreducible
 * monic
 * evaluate
 * short products
 * rational function reconstruction (not a FLINT function)


---

Comment by burcin created at 2009-10-20 14:44:05

Changing status from new to needs_review.


---

Attachment


---

Comment by mhansen created at 2009-10-21 07:37:30

With Sage 4.2.alpha1, I get the following failures:


```
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/padics.py # 18 doctests failed
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py # 15 doctests failed
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py # 5 doctests failed
        sage -t -long devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py # 1 doctests failed
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_padic_field.py # 2 doctests failed
```


Also, in squarefree_decomposition, there is an "EXAMPLES:" that needs to be "EXAMPLES::".


---

Comment by mhansen created at 2009-10-21 07:37:30

Changing status from needs_review to needs_work.


---

Attachment

Oops, I hadn't run doctests on `schemes`, and it was a genuine bug with scalar multiplication.

New patch attachment:trac_5680-flint_zmod_poly_enhancements.take2.patch should fix all problems.


---

Comment by burcin created at 2009-10-21 17:13:17

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2009-11-05 01:19:04

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-05 01:19:04

Looks good to me.


---

Comment by mhansen created at 2009-11-05 01:19:13

Resolution: fixed
