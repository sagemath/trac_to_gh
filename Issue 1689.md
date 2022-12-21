# Issue 1689: document SAGE_FORTRAN_LIB

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-05 00:42:56

Assignee: tba

It is certainly a special option, but we need to document this.


---

Comment by mabshoff created at 2008-04-09 18:26:45

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-04-09 18:26:45

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-09 18:26:45

Changing assignee from tba to mabshoff.


---

Comment by mabshoff created at 2008-04-09 18:26:45

This is biting people in practice and causes build failures on Itanium for example unless you know what you are doing. So *fix* this. Since this is my ticket now I am yelling at myself :)

Cheers,

Michael


---

Comment by was created at 2008-04-11 00:06:24


```
Note that you absolutely cannot build Sage on itanium by
just extracting the tarball and typing make, because Sage
includes binaries for Fortran but not on Itanium. Thus you
have to explicitly tell the build process about the fortran
compiler and library location.  Do this by typing

  export SAGE_FORTRAN=/exact/path/to/gfortran
  export SAGE_FORTRAN_LIB=/path/to/fortran/libs/

Note that SAGE_FORTRAN_LIB is not documented
anywhere (http://trac.sagemath.org/sage_trac/ticket/1689),
and we've got away with this so far since there is only
one Itanium user of Sage in the world, at present.

 -- William
```



---

Comment by was created at 2008-04-11 00:08:21

this is a modified version of README.txt from sage-3.0.alpha3


---

Attachment

The "patch" is just a new README.txt


---

Attachment

corrected  version which also removes the outdated Solaris section


---

Comment by mabshoff created at 2008-04-11 20:44:56

Merged in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-11 20:44:56

Resolution: fixed
