# Issue 4821: Experimental scilab-5.0.3.spkg [with spkg, needs review]

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2008-12-17 18:32:04

Assignee: mabshoff

CC:  mkoeppe

Keywords: scilab, matlab

I made an experimental scilab-5.0.3.spkg

[http://sage.math.washington.edu/home/jsp/SPKGS/Scilab/scilab-5.0.3.spkg
]


```

Please test it by downloading it into $SAGEROOT
and type

./sage -f -m scilab-5.0.3.spkg

The -m argument keeps the package in the spkg/build directory for
further experimentation.

See spkg-install:
I did a minimal
./configure --without-javasci --without-gui --with-gfortran


There are two dependencies left: pcre and matio

I don't know how essential they are for a full functional scilab :(


```


Cheers,

Jaap


For me it worked on Fedora 9 and Fedora 10


```
real	36m7.756s
user	22m25.173s
sys	9m55.849s
Successfully installed scilab-5.0.3
You can safely delete the temporary build directory
/home/jaap/downloads/sage-3.2.2.alpha0/spkg/build/scilab-5.0.3
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing scilab-5.0.3.spkg
[jaap`@`paix sage-3.2.2.alpha0]$
[...]
sage: scilab.console()
graphics module not found.
javasci module not found.
         ___________________________________________
                        scilab-5.0.3

                  Consortium Scilab (DIGITEO)
                Copyright (c) 1989-2008 (INRIA)
                Copyright (c) 1989-2007 (ENPC)
         ___________________________________________


Startup execution:
   loading initial environment

-->
```



---

Comment by mabshoff created at 2008-12-30 11:05:52

This spkg needs at least to attempt to pick the right Fortran runtime at configure time.

Cheers,

Michael


---

Comment by jsp created at 2009-02-05 16:56:09

Replying to [comment:1 mabshoff]:
> This spkg needs at least to attempt to pick the right Fortran runtime at configure time.
> 

Of course you are right, but I don't know how to do that.

Besides there are other dependencies to be resolved.

What I did on Fedora was cycling .configure and installing missing dependencies.

Not very suited for inclusion in spkg-install :-)!

Jaap


---

Comment by chapoton created at 2020-05-13 11:25:42

Maybe we can close this ancient ticket now ?


---

Comment by chapoton created at 2020-05-13 11:25:42

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2020-05-13 21:35:53

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-05-14 09:17:58

thx


---

Comment by chapoton created at 2020-05-14 09:17:58

Resolution: invalid
