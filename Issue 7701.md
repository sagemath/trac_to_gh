# Issue 7701: update the openmpi spkg to the latest version

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-16 02:03:02

Assignee: tbd

CC:  jdemeyer




---

Comment by was created at 2009-12-16 02:13:58

Spkg in progress here:

    http://sage.math.washington.edu/home/wstein/patches/openmpi-1.4.spkg

This doesn't work, and fails with this error:

```
/bin/bash ./libtool --tag=CC   --mode=link gcc  -O3 -DNDEBUG   -fvisibility=hidden -module -avoid-version  -o dlopen.la  dlopen.lo -ldl -ldl -lnsl -lutil  -lm
libtool: link: ar cru .libs/dlopen.a .libs/dlopen.o
libtool: link: ranlib .libs/dlopen.a
rm: cannot remove `dlopen.la': No such file or directory
libtool: link: ( cd ".libs" && rm "dlopen.la" && ln -s "../dlopen.la" "dlopen.la" )
rm: cannot remove `dlopen.la': No such file or directory
make[3]: *** [dlopen.la] Error 1
make[3]: Leaving directory `/scratch/wstein/build/sage-4.3.rc0/spkg/build/openmpi-1.4/src/opal/libltdl'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/scratch/wstein/build/sage-4.3.rc0/spkg/build/openmpi-1.4/src/opal/libltdl'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/scratch/wstein/build/sage-4.3.rc0/spkg/build/openmpi-1.4/src/opal'
make: *** [all-recursive] Error 1
Error building
```



---

Comment by vbraun created at 2010-01-25 22:30:38

The reason for this error is that newer versions of libtool break when you define $RM="rm", see http://trac.sagemath.org/sage_trac/ticket/7818#comment:28

Temporary work-around is adding `unset RM` to spkg-install


---

Comment by thisch created at 2011-03-02 15:07:12

this ticket should be fixed according to the release notes of sage 4.6.2, right ?

#8537: Stefan Reiterer: Update Open MPI package to latest - Sage version is 3 years old! [Reviewed by Volker Braun]


---

Comment by vbraun created at 2011-03-02 15:09:54

Sage-4.6.2 has openmpi-1.4.3 as optional spkg. 

Release manager: Please close this ticket.


---

Comment by thisch created at 2011-05-28 14:42:24

any reason why this ticket is still open?


---

Comment by jdemeyer created at 2011-05-30 07:38:21

Replying to [comment:4 vbraun]:
> Sage-4.6.2 has openmpi-1.4.3 as optional spkg. 
> 
> Release manager: Please close this ticket.


---

Comment by jdemeyer created at 2011-05-30 07:38:21

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2011-05-30 07:38:38

Resolution: duplicate
