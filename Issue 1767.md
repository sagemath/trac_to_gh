# Issue 1767: Add SAGE_ATLAS_LIB, SAGE_ATLAS_TARGZ flags to allow use of external atlas

Issue created by migration from https://trac.sagemath.org/ticket/1767

Original creator: jkantor

Original creation time: 2008-01-13 23:48:24

Assignee: mabshoff

We currently provide a SAGE_FORTRAN flag that lets external fortran be used if the user desires.
Since atlas takes a long time to build, we should have an optional SAGE_ATLAS_LIB flag 
that would accept the path to a directory that contained libatlas, libcblas, libf77blas, and liblapack. The atlas install script will do some tests to ensure these work and will then create symlinks to them in $SAGE_LOCAL/lib

There should also be a SAGE_ATLAS_TARGZ with would be the path to a tar or tar.gz with libatlas, libcblas, libf77blas, and liblapack. These would just be copied into $SAGE_LOCAL/lib

As mentioned some checking needs to be done to ensure the atlas provided is compatible with the fortran we are using, that it actually works, as well as to check that the lapack is the full lapack (8Mb or so) and not a crippled lapack.




---

Comment by aapitzsch created at 2014-07-25 23:12:10

`SAGE_ATLAS_LIB` has been introduced long time ago (ticket:1721#comment:7) and IMO there is no need for `SAGE_ATLAS_TARGZ`. So let's close this.


---

Comment by aapitzsch created at 2014-07-25 23:12:10

Changing status from new to needs_review.


---

Comment by chapoton created at 2014-07-26 08:23:55

I agree. But we should try to make it more easy to learn how to avoid ATLAS compilation, see #15371.


---

Comment by chapoton created at 2014-07-26 08:23:55

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-08-20 20:32:31

Resolution: fixed
