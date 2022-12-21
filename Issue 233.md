# Issue 233: Create QDRF -- quad double real field

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-30 19:08:51

Assignee: somebody

This would be like the RealDoubleField in rings/real_double.pyx or like riungs/real_mpfr.pyx, except that the quad double library is a C++ library -- so actually this might be similar to the Givaro wrapper in rings/finite_field_givaro.*.  

The quaddouble library (and docs?) are available at 

    http://www.cs.berkeley.edu/~yozo/

Also, I made a SAGE package, which you get by doing
    sage -i quaddouble-2.1.213.1.spkg


---

Comment by was created at 2007-02-04 04:11:32

Changing assignee from somebody to didier deshommes.


---

Comment by mabshoff created at 2007-08-22 20:30:56

Hello,

I assume this has been done, due to the fact that we have

```
-rw-rw-r--  1 mabshoff mabshoff 436943 Aug 22 09:22 real_rqdf.cpp
-rw-r--r--  1 mabshoff mabshoff   3592 Jun 30 09:09 real_rqdf.pxd
-rw-r--r--  1 mabshoff mabshoff  49291 Aug 18 06:41 real_rqdf.pyx
```

in sage-2.8.2.rc3/devel/sage/sage/rings.

Feel free to correct me.

Cheers,

Michael


---

Comment by mhansen created at 2007-08-22 22:46:18

Yep, I think this one can be closed:

sage: RQDF(pi)
3.141592653589793238462643383279502884197169399375105820974944590


---

Comment by was created at 2007-08-23 05:47:50

closed, thanks to bradshaw and deshomme.


---

Comment by was created at 2007-08-23 05:47:50

Resolution: fixed
