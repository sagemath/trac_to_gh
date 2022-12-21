# Issue 8024: Update prereq to check for Fortran compiler

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-21 12:05:49

Assignee: GeorgSWeber

CC:  was

Prior to 4.3.1.rc2, Sage included a Fortran compiler for Linux and OS X, so there was no need to have one. 

As such, the 'prereq' script did not check for it. #7485 merged in sage-4.3.1.rc2 removed the Fortran compiler. 

It would appear from at least one log posted

http://sporadic.stanford.edu/bump/sage-4.3.1-errors

that despite gcc being built with Fortran support


```
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang 
--prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext 
--enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.2 --program-suffix=-4.2 
--enable-clocale=gnu --enable-libstdcxx-debug 
--enable-objc-gc --enable-mpfr --enable-targets=all 
--enable-checking=release --build=i486-linux-gnu 
--host=i486-linux-gnu --target=i486-linux-gnu
```


Fortran it is not installed on some Ubunta systems. As such, prereq should be modified to check for a Fortran compiler on every platform except OS X. 

Dave 


---

Comment by drkirkby created at 2010-01-24 22:33:05

Changing priority to critical, as William created a duplicate (#8026) and marked that as critical.


---

Comment by drkirkby created at 2010-01-24 22:33:05

Changing priority from major to critical.


---

Comment by drkirkby created at 2010-01-24 23:53:36

#8026 is a duplicate of this, with one minor difference being this checks for a Fortran compiler, not gfortran.


---

Comment by drkirkby created at 2010-01-31 06:19:54

This is solved by #8052, which currently needs review


---

Comment by mvngu created at 2010-01-31 22:31:51

Close as fixed by #8052.


---

Comment by mvngu created at 2010-01-31 22:31:51

Resolution: fixed
