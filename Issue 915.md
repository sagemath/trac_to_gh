# Issue 915: Make LinBox used PID_Integer instead of using old header as workaround

Issue created by migration from https://trac.sagemath.org/ticket/915

Original creator: mabshoff

Original creation time: 2007-10-18 03:04:35

Assignee: mabshoff

Keywords: LinBox gmp

To quote William from linbox-use:

```
I would also like to know the answer to this.  In SAGE were currently do this
conversion by not using PID_Integer, and instead using an old header file
from an old version of Linbox that defined a GMP Integer wrapper type.
Fast conversion to/from mpz_t is critical for what we're doing.
```

Dave Saunders came up with the following suggestion:

```
PID_integer ZZ;
SparseMatrix<PID_integer> A (ZZ,m,m);  //defines empty sparse matrix

mpz_t x;
mpz_init_set_ui(x, 5);


// Assign x into A, avoiding conversions and double copy.
mpz_set ( SpyInteger::get_mpz(A.refEntry(1,2)), x);

ZZ.write(std::cout, A.getEntry(1,2)) << std::endl;

-dave

PS.  A more direct function could be desirable.
```

This ticket is related to #824. For details see http://groups.google.com/group/linbox-use/t/7a687e8e5a5f4a81

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-18 03:04:42

Changing status from new to assigned.


---

Attachment

Remove the usage of GMP-Integer implementation of Z


---

Attachment

Remove the work-around with gmp-integers


---

Comment by mabshoff created at 2008-03-03 04:44:04

Patch looks good to me :)


---

Comment by mabshoff created at 2008-03-03 04:50:01

Merged Clement's patch in

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.3/rc1/linbox-1.1.5rc2.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-03 04:54:17

Merged in Sage 2.10.3.rc1


---

Comment by mabshoff created at 2008-03-03 04:54:17

Resolution: fixed
