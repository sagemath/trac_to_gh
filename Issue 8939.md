# Issue 8939: matrix classes for flint polynomials

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-05-09 22:52:10

Assignee: jason, was

CC:  malb jpflori

Attached patch adds templated matrix classes for FLINT's `fmpz_poly` and `zmod_poly` structs.

At the moment there is no extra functionality provided by the classes, but fast nullspace (over the fraction field), and hopefully inverse implementations will be coming soon. In any case, this should be a good basis for implementing fast algorithms for these matrices.


---

Comment by burcin created at 2010-05-09 22:54:30

Changing status from new to needs_review.


---

Attachment

rebased to 4.4.2


---

Comment by burcin created at 2010-05-22 10:55:22

I uploaded a new patch rebased to 4.4.2.


---

Comment by malb created at 2010-06-03 14:51:57

I get one doctest failure with this patch applied on top of 4.4.2:


```
**********************************************************************
File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage/sage/modules/free_module.py", line 1125:
    sage: V.base_extend(QQ)
Expected:
    Vector space of dimension 7 over Rational Field
Got:
    V
```



---

Comment by malb created at 2010-06-03 15:00:20

Changing status from needs_review to needs_work.


---

Comment by malb created at 2010-06-03 15:00:20

The patch looks good. However, I'd prefer to have a bit more documentation.

 * I think there should be doctests in `fmpz_poly_linkage.pxi`. I know our policy does not require it, but it seems like a good pplace to put some
 * It would be nice to write a bit about how all the files (templates etc.) relate to each other, e.g. some documentation in `matrix_dense_template.pxi` which makes it explains a bit how to use it. (I guess I should do the same for the polynomial template thing.)
 *  I cannot see the "fast nullspace"


---

Attachment

address referee comments


---

Comment by burcin created at 2010-09-25 19:59:07

Replying to [comment:4 malb]:
> The patch looks good. However, I'd prefer to have a bit more documentation.
 
>  * I think there should be doctests in `fmpz_poly_linkage.pxi`. I know our policy does not require it, but it seems like a good pplace to put some

Done. I added a new file `sage/libs/flint/fmpz_poly_linkage_tests.pyx` with python functions wrapping the `celement_*()` functions. I don't know how to test the `celement_{construct,destruct}()` functions, so they are omitted.

>  * It would be nice to write a bit about how all the files (templates etc.) relate to each other, e.g. some documentation in `matrix_dense_template.pxi` which makes it explains a bit how to use it. (I guess I should do the same for the polynomial template thing.)

Done, with a brief description at the beginning of `matrix_dense_template.pxi`.

>  *  I cannot see the "fast nullspace"

This will be on a different ticket, when I get around to cleaning it up...


---

Comment by burcin created at 2010-09-25 19:59:07

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-11-23 17:50:59

Changing status from needs_review to needs_work.


---

Comment by malb created at 2010-11-23 17:50:59

This patch bitrotted a lot (sorry for not not reviewing your changes earlier!):


```
applying trac_8939-matrix_template-4.4.2-part2.patch
patching file module_list.py
Hunk #1 succeeded at 501 with fuzz 2 (offset 18 lines).
unable to find 'sage/libs/flint/fmpz_poly_linkage.pxi' for patching
2 out of 2 hunks FAILED -- saving rejects to file sage/libs/flint/fmpz_poly_linkage.pxi.rej
unable to find 'sage/matrix/matrix_dense_template.pxi' for patching
1 out of 1 hunks FAILED -- saving rejects to file sage/matrix/matrix_dense_template.pxi.rej
patch failed, unable to continue (try -v)
sage/libs/flint/fmpz_poly_linkage.pxi: No such file or directory
sage/matrix/matrix_dense_template.pxi: No such file or directory
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8939-matrix_template-4.4.2-part2.patch
```



---

Comment by mmezzarobba created at 2014-03-15 08:30:56

Wouldn't it be better now to wrap `fmpz_mat`, `fmpz_poly_mat`, `fmpq_mat`, `nmod_poly_mat` instead? Or do we need to do both to preserve existing features?
