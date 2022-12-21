# Issue 678: Solaris 10: fix scipy compiler selection

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-17 05:22:27

Assignee: mabshoff

On Solaris scipy looks for 

 * g77
 * f77
 * f90

but fails to detect either g95 or gfortran. It should look for those two, but a quick fix is usually to symbolically link gfortran or g95 as g77.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-17 05:50:06

Changing status from new to assigned.


---

Comment by jkantor created at 2007-11-18 09:02:38

I know how the scipy chooses fortran compilers (its actually in numpy's distutils/fcompiler).

I could probably help with this if I had access to a solaris box.


---

Comment by mabshoff created at 2007-12-04 14:15:11

I believe this has been fixed. I will investigate this.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-29 17:27:38

Resolution: fixed


---

Comment by mabshoff created at 2008-07-29 17:27:38

By introducing sage_fortran this issue has been fixed.

Cheers,

Michael
