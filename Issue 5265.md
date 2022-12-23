# Issue 5265: Link the matrix_mod2_dense extension against png12

Issue created by migration from https://trac.sagemath.org/ticket/5265

Original creator: mabshoff

Original creation time: 2009-02-14 09:53:07

Assignee: mabshoff

Right now we link the matrix_mod2_dense.pyx aginst libpng:

```
     Extension('sage.matrix.matrix_mod2_dense',
               sources = ['sage/matrix/matrix_mod2_dense.pyx'],
               libraries = ['gmp','m4ri', 'png', 'gd']),
```

We need to link against png12 since the new libpng.spkg will only provide libpng12.*.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 09:53:14

Changing status from new to assigned.


---

Attachment


---

Attachment

Please review both patches. The second patch is needed to make 100% the extension is rebuild in case of an upgrade. Sorry for the two patches, but I couldn't fold them since I committed the first one to my local repo already.

Cheers,

Michael


---

Comment by jason created at 2009-02-14 10:11:07

I applied both patches, touched matrix_mod2_dense.pyx, did sage -b, and then ran the tests in matrix_mod2_dense.pyx, and everything passed.  If that's all that is needed to review this patch, then positive review.  If not, the take my positive review off.


---

Comment by mabshoff created at 2009-02-14 13:24:41

Resolution: fixed


---

Comment by mabshoff created at 2009-02-14 13:24:41

Merged both patches in Sage 3.3.rc1.

Cheers,

Michael
