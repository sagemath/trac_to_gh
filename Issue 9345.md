# Issue 9345: Unhandled SIGFPE is rational_reconstruction if the modulus is zero

Issue created by migration from Trac.

Original creator: lftabera

Original creation time: 2010-06-26 10:42:28

Assignee: AlexGhitza

CC:  jdemeyer

Ssage crashes if try to perform a rational_reconstruction with zero modulus and compiled fast algorithm


```
sage: rational_reconstruction(1,0)


------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------

```



---

Comment by lftabera created at 2010-06-26 10:51:25

Changing status from new to needs_review.


---

Attachment


---

Attachment


---

Attachment

I'm mostly OK with lftabera's patch. Here are some changes that needs to be made:

 * Reference the ticket number in the relevant regression test.
 * Use the Python 3.x compliant way of raising exceptions.
 * Add a more general regression test.
 * Credit lftabera in his patch. (We don't accept anonymous patches.) Put a sensible commit message in lftabera's patch. So one now uses [trac_9345.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9345/trac_9345.2.patch) instead of [trac_9345.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9345/trac_9345.patch). 

See the ticket description for instructions on how to apply the relevant patches. Only my proposed changes need review by anyone but me. If they are OK, then the whole ticket receives a positive review.


---

Comment by lftabera created at 2010-06-26 11:51:14

Not quite solved, the problem is not in this method, but in the compiled rational reconstruction


```
sage: ZZ(1).rational_reconstruction(0)


------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```


I will update the patch to the correct function


---

Comment by lftabera created at 2010-06-26 11:51:14

Changing status from needs_review to needs_work.


---

Comment by lftabera created at 2010-06-30 13:55:50

The following files have a call to rational_reconstruction, computed using


```
sage: search_src('rational_reconstruction',interact=False)

```

and code to make Sage crash

 * rings/integer.pyx


```
 sage: ZZ(1).rational_reconstruction(0)
```

  Calls rational.pyrex_rational_reconstruction

 * rings/rational.pyx


```
 sage: sage.rings.rational.pyrex_rational_reconstruction(1,0)
```

 * rings/arith.py


```
 sage: rational_reconstruction(1,0)
```

  Calls ZZ.rational_reconstruction

 * rings/finite_rings/element_ext_pari.py

  Unable to crash, it is an element of a finite field. Anyway, it calls arith.rational_reconstruction

 * rings/finite_rings/integer_mod.pyx

  Unable to crash, an element mod 0 is an Integer. Anyway, it calls ZZ.rational_reconstruction

 * rings/padics/padic_generic_element.pyx

  Unable to crash, modulus of a p-adic element is not zero. anyway, it calls arith.rational_reconstruction

 * matrix/matrix_rational_dense.pyx

 1. _lift_crt_rr
 1. _lift_crt_rr_with_lcm


  Obsolete functions for crt? They seem not to be used anywhere. By the code, it seems tha mm should be a list of moduli matrices (call of _lift_crt). On the other hand, the product should be an integer 
m= mm.prod(); mpq_rational_reconstruction(Q_row[j], Z_row[j], m.value) So I cannot test whether there is a problem for these functions. I am not able to get crashes or any sensible output from these functions.

 * matrix/matrix_integer_sparse.pyx


```
 sage: M = random_matrix(ZZ, 3, 3, 'sparse')
 sage: M.rational_reconstruction()
```

  Calls misc.matrix_integer_sparse_rational_reconstruction

 * matrix/misc.pyx


```
 sage: M = random_matrix(ZZ, 3, 3, 'sparse')
 sage: sage.matrix.misc.matrix_integer_sparse_rational_reconstruction(M,0)
```


```
 sage: M = random_matrix(ZZ, 3, 3)
 sage: sage.matrix.misc.matrix_integer_dense_rational_reconstruction(M,0)
```

 * matrix/matrix_cyclo_dense.pyx

  Unable to crash. Used in a modular algorithm, calls misc.matrix_integer_dense_rational_reconstruction

 * matrix/matrix_integer_dense.pyx


```
 sage: M = random_matrix(ZZ,3)
 sage: M.rational_reconstruction(0)
```

  Calls misc.matrix_integer_dense_rational_reconstruction


---

Attachment

previous patches merged


---

Comment by lftabera created at 2010-07-02 10:11:33

New patch with all the modifications. Respecting the code, the patch only changes rings/rational.pyx and matrix/misc.pyx where the offending code is.

However, I have added doctests to check all the crashes in the previous post. This might be overkilling though.


---

Comment by lftabera created at 2010-07-02 10:11:33

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-08-10 06:15:43

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-08-10 06:15:43

I think one should find out which code really causes the crash, because _sig_on/_sig_off should be used there.  See [http://sagemath.org/doc/developer/coding_in_other.html#the-pari-c-library-interface](http://sagemath.org/doc/developer/coding_in_other.html#the-pari-c-library-interface) (the docs are about PARI but apply more generally to all C and Cython code).


---

Comment by lftabera created at 2010-09-06 09:03:03

Changing status from needs_work to needs_review.


---

Attachment

Well, there was a similar problem in #9357 and I got this answer to the question of _sig_onm, _sig_off

http://groups.google.com/group/sage-devel/browse_thread/thread/e8317365bfe9e6e8/2a4148024500dfd2

Note that if the exception is controlled by _sig, it will raise a RuntimeError instead of ZeroDivisionError. Moreover, with the patch I provided, all ocurrences of being zero are catched and never reaches the C functions.

Anyway, I have written a second patch that add the _sig_on, _sig_off to the problematic functions, so if they have to be added, apply the following patches (in order):

trac_9345.3.patch
trac-9345-sigs.patch


---

Comment by jdemeyer created at 2010-09-06 10:33:09

Replying to [comment:7 lftabera]:
> Note that if the exception is controlled by _sig, it will raise a RuntimeError instead of ZeroDivisionError. Moreover, with the patch I provided, all ocurrences of being zero are catched and never reaches the C functions.
I agree that your patch fixes the problem of division by zero, that wasn't my point.  My point was that, *in addition* you should add _sig_on and _sig_off to make the code more robust (for example, against crtl+C).

> Anyway, I have written a second patch that add the _sig_on, _sig_off to the problematic functions, so if they have to be added, apply the following patches (in order):
> 
> trac_9345.3.patch
> trac-9345-sigs.patch
Well, the _sig_on and _sig_off are in the wrong places (_sig_on should be before any mpz or mpq function is called and _sig_off after). I can have a look at this if you want.


---

Attachment

Better alternative to trac-9345-sigs.patch


---

Comment by jdemeyer created at 2010-09-07 21:01:07

Replying to [comment:5 lftabera]:
> However, I have added doctests to check all the crashes in the previous post. This might be overkilling though.

I agree that it is overkill, but I'm fine with it.  I'm giving positive_review for `trac_9345.3.patch`. Somebody else should review my `trac-9345-sigs-jd.patch`.


---

Attachment

I have corrected jdemeyer patch to also  include the sparse matrix case. The patch to review is trac-9345-sigs-jd-2.patch


---

Comment by jdemeyer created at 2010-09-08 12:02:01

Replying to [comment:10 lftabera]:
> I have corrected jdemeyer patch to also  include the sparse matrix case. The patch to review is trac-9345-sigs-jd-2.patch

Looks good to me, but I suppose somebody else should formally review it.


---

Comment by jdemeyer created at 2010-11-13 10:43:02

I will move the signals part to #10061, therefore positive review for [attachment:trac_9345.3.patch]


---

Comment by jdemeyer created at 2010-11-13 10:43:02

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-15 23:26:25

Resolution: fixed
