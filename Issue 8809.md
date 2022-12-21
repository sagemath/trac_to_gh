# Issue 8809: change local/bin/sage_fortran script to respect the SAGE_FORTRAN variable, if it is set

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-28 22:10:59

Assignee: GeorgSWeber

When building binaries that include fortran, etc., it would give developers and users a lot more control if the local/bin/sage_fortran script were changed from

```
!/bin/sh

/usr/bin/gfortran -fPIC $`@`
```

to

```
!/bin/sh

if [ x"$SAGE_FORTRAN" != x ]; then
     "$SAGE_FORTRAN" -fPIC $`@`
else
     /usr/bin/gfortran -fPIC $`@`
fi
```



---

Comment by jdemeyer created at 2013-05-19 13:16:58

`SAGE_FORTRAN` is deprecated and the `sage_fortran` script does use `$FC`.


---

Comment by jdemeyer created at 2013-05-19 13:16:58

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-05-19 13:17:42

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-21 07:26:14

Resolution: invalid
