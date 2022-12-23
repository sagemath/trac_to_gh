# Issue 4467: clean up or delete the (unused?) hanke extension

Issue created by migration from https://trac.sagemath.org/ticket/4467

Original creator: mabshoff

Original creation time: 2008-11-08 05:51:58

Assignee: mabshoff

setup.py contains

```
hanke = Extension(name = "sage.libs.hanke.hanke",
              sources = ["sage/libs/hanke/hanke.pyx",
                         "sage/libs/hanke/wrap.cc",
                         "sage/libs/hanke/Matrix_mpz/Matrix_mpz.cc",
                         "sage/libs/hanke/Matrix_mpz/CountLocal2.cc",
                         "sage/libs/hanke/Matrix_mpz/CountLocal.cc",
                         "sage/libs/hanke/Matrix_mpz/Local_Constants.cc",
                         "sage/libs/hanke/Matrix_mpz/Local_Density_Front.cc",
                         "sage/libs/hanke/Matrix_mpz/Local_Density_Congruence.cc",
                         "sage/libs/hanke/Matrix_mpz/Local_Normal.cc",
                         "sage/libs/hanke/Matrix_mpz/Local_Invariants.cc",
                         "sage/libs/hanke/Utilities/string_utils.cc",
                         "sage/libs/hanke/GMP_class_extras/mpz_class_extras.cc",
                         "sage/libs/hanke/GMP_class_extras/vectors.cc" ],
                   libraries = ["gmp", "gmpxx", "stdc++"])
```


It looks like dead code to me, so it should be deleted IMHO. In case John wants to use it for something he should be given the chance to rescue it.

Cheers,

Mcihael


---

Comment by mabshoff created at 2008-11-08 20:37:40

I talked to John Hanke and he told me that the code can be deleted since it is no longer used.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-10 05:19:43

Craig will remove the actual setup.py extension in a separate cleanup patch of setup.py

Cheers,

Michael


---

Attachment

+1 since the code removes dead code only.


---

Comment by mabshoff created at 2008-11-10 09:06:47

Resolution: fixed


---

Comment by mabshoff created at 2008-11-10 09:06:47

Merged in Sage 3.2.rc0
