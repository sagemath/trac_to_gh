# Issue 7036: rubiks ignroes CC and uses gcc even if CC is Sun compiler

Issue created by migration from https://trac.sagemath.org/ticket/7036

Original creator: drkirkby

Original creation time: 2009-09-27 15:33:55

Assignee: tbd

Keywords: GNUism gcc CC

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 

CC was set to the Sun C compiler, CXX to the Sun C++ compiler and SAGE_FORTRAN to the Sun Fortran 95 compiler. 

rubiks-20070912.p9 totally ignores the setting of CC, and uses gcc which it finds in the path. This is unfortunately not an uncommon problem. 


```
rubiks-20070912.p9/src/dik/globals.h
rubiks-20070912.p9/src/dik/permcube.c
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
Building Rubiks cube solvers
make[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/rubiks-20070912.p9/src'
for dir in dietz/cu2 dietz/mcube dietz/solver dik reid; do \
        (cd ${dir} && make all)\
done
make[3]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/rubiks-20070912.p9/src/dietz/cu2'
g++ -O2 -c cu2.cpp
g++ -O2 -c main.cpp

```



---

Comment by drkirkby created at 2009-09-29 02:14:24

Having looked at this package, I can see it was broken in numerous ways. 

 * g++ was hard coded
 * An option was passed to the assembler in an attempt to suppress warnings, though this would only work with the GNU assembler
 * I don't think it could build 64-bit executables - there was nothing about SAGE64 in the spkg-install
 * CFLAGS were used when CXXFLAGS should have been used. 

Basically, the makefiles were a total mess. 

The revised .spkg has been tested on
 * 32-bit Solaris SPARC with gcc
 * 64-bit Solaris SPARC with gcc
 * 32-bit Solaris SPARC with Sun compiler
 * 64-bit Solaris SPARC with Sun compiler
 * Sage.math - I think the default is 64-bit there. 
 * 32-bit on bsd.math with gcc
 * 64-bit on bsd.math with gcc

There are now no hard-coded options, or compilers. Everything can be set from spkg-install, and is set sensibly. I've tested this with both 32 and 64-bit builds on Solaris, using both the GNU and Sun compilers. Also tested on sage.math. Also tested on bsd.math in both 

The new spkg can be found here. 
http://sage.math.washington.edu/home/kirkby/Solaris-fixes/rubiks-20070912.p10/rubiks-20070912.p10.spkg

The spkg-install is here
http://sage.math.washington.edu/home/kirkby/Solaris-fixes/rubiks-20070912.p10/spkg-install

The revised Makefiles, patches etc are in this directory:

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/rubiks-20070912.p10

Be warned, the patches are bigger than the makefiles - the chances are so many.


---

Comment by mhansen created at 2009-11-05 02:16:34

Looks good to me.


---

Comment by mhansen created at 2009-11-05 02:16:34

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2009-11-09 06:45:11

Since you gave this a positive review, I've changed the title from '[with spkg; needs review] ' to '[with spkg; positive review]' 

Now this new radio button has been added to trac that allows one to specify a positive review, should one still add '[with spkg; needs review]' to the title, or the 'needs review' bit ignored? 

Dave


---

Comment by mhansen created at 2009-11-17 06:12:27

Resolution: fixed
