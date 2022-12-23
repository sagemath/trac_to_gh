# Issue 8278: cygwin: cvxopt doesn't work at all

Issue created by migration from https://trac.sagemath.org/ticket/8278

Original creator: was

Original creation time: 2010-02-15 22:44:34

Assignee: tbd

CC:  pjeremy

Using either cvxopt-0.9.p8 (in sage-4.3.3) or cvxopt-1.1.2.p2, which is at http://boxen.math.washington.edu/home/schilly/sage/spkg/, we get this huge error very quickly upon trying to build:


```
building 'base' extension                                                            
creating build/temp.cygwin-1.7.1-i686-2.6                                                                                  
creating build/temp.cygwin-1.7.1-i686-2.6/C                                                                                
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/home/wstein/build/sage-4.3.3.alpha0/local/include/python2.6 -c C/base.c -o build/temp.cygwin-1.7.1-i686-2.6/C/base.o                                                            
In file included from C/base.c:23:                                                                                         
C/cvxopt.h:29:21: error: complex.h: No such file or directory                                                              
In file included from C/base.c:24:                                                                                         
C/misc.h:29: error: expected specifier-qualifier-list before ‘complex’                                                     
C/base.c:58: error: ‘complex’ undeclared here (not in a function)                                                          
C/base.c: In function ‘write_znum’:                             
```


IDEAS:

 1. Look for complex.h on this page:  http://www.cygwin.com/ml/cygwin/2006-07/threads.html#00763  That has some ideas.

 2. I think Mike Hansen said that he recently released (then unreleased!?) numpy-1.4 had a drop-in complex.h?


---

Comment by was created at 2010-02-15 23:04:50

I put in some fake #defines to get past the complex.h import problem.  Then linking fails due to no libcblas. 

```
gcc -shared -Wl,--enable-auto-image-base build/temp.cygwin-1.7.1-i686-2.6/C/base.o build/temp.cygwin-1.7.1-i686-2.6/C/dense.o build/temp.cygwin-1.7.1-i686-2.6/C/sparse.o -L/home/wstein/build/sage-4.3.3.alpha0/local/lib -L/home/wstein/build/sage-4.3.3.alpha0/local/lib/python2.6/config -lm -llapack -lcblas -lf77blas -latlas -lgfortran -lpython2.6 -o build/lib.cygwin-1.7.1-i686-2.6/cvxopt/base.dll
/usr/lib/gcc/i686-pc-cygwin/4.3.4/../../../../i686-pc-cygwin/bin/ld: cannot find -lcblas
collect2: ld returned 1 exit status
```

Changing the libraries= line in setup.py to

```
    libraries = ['m','lapack','blas','gfortran']
```

(like it is for OS X) gets past this problem.

I think it may be easy to implement complex.h, at least enough for cvxopt, just using what is in GSL...  since cvxopt doesn't need much.  

To get cvxopt to build, I replaced all references to atlas and cblas by "blas".    This *did* work.  I've attached my hacked setup.py (based on the one in cvxopt-1.1.2.p2) to this ticket just 'cause:

```
/home/wstein/build/sage-4.3.3.alpha0
sage subshell$ python
Python 2.6.4 (r264:75706, Feb 12 2010, 22:06:32)
[GCC 4.3.4 20090804 (release) 1] on cygwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import cvxopt
>>>
```



---

Comment by was created at 2010-02-15 23:07:06

hacked setup.py that allowed me to build and install cvxopt (though i had to make a fake complex.h)


---

Attachment


---

Attachment

I would like to merge this with cvxopt-1.1.2.p2 (well, p3) that I just finished porting to Solaris, and cleaning up. For the latter, e.g. there is no random stuff in cvxopt any more, they can hook up to GSL (and we can enable this, as GSL is a standard Sage package).

Can I use winxp2.math.washington.edu ?
I suppose I need a login, and I don't seem to have one (I tried logging in from 
boxen...)

Dima


---

Comment by mhansen created at 2010-04-27 17:34:47

This is fixed by #8780 which provides a working complex.h


---

Comment by mhansen created at 2010-05-24 23:54:01

This is actually not fixed by #8780.


---

Comment by drkirkby created at 2010-08-02 04:49:18

complex.h is the header file that you need, but you almost certainly need the C99 libraries too. So it's not as simple as just adding a complex.h file.  

I'm cc'ing Peter on this, as I know he has (or at least did have), C99 issues on FreeBSD. I got similar issues when trying to build Sage on HP-UX, though that is of course not a high priority port. 

Dave


---

Comment by pjeremy created at 2010-08-02 11:14:54

Replying to [comment:6 drkirkby]:
> complex.h is the header file that you need, but you almost certainly need the C99 libraries too. So it's not as simple as just adding a complex.h file.

And the complex.h needs to match the C99 libraries.

> I'm cc'ing Peter on this, as I know he has (or at least did have), C99 issues on FreeBSD.

cephes was introduced to provide C99 functions for Cygwin.  FreeBSD does not provide a complete C99 library and I've written a number of tickets to use cephes to provide the missing functionality.  See trac tickets #9543 and #9601 (both of which include patches, though they haven't been converted to new SPKG files yet).  numpy also needs the same patch as #9601 but I haven't updated the relevant trac ticket for that yet.

Note that the patch in #9543 relies on some ELF shared library magic (and installs a $SAGE_LOCAL/libm.so that includes the cephes functions and automatically falls back to the base libm.so for other functions) that may not work in Cygwin (on Cygwin, cephes installs C99 libraries as $SAGE_LOCAL/libm{c,d,f,l}.a and any other SPKGs needing to reference those libraries will need patches to their link steps).


---

Comment by kcrisman created at 2011-06-16 02:20:35

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-06-16 02:20:35

#6456 fixed this.  Please close.

cvxopt builds, which is how I found this out :)


---

Comment by kcrisman created at 2011-06-16 02:20:46

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-06-20 18:55:37

Resolution: duplicate
