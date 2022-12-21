# Issue 7032: symmetrica ignores CC

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-27 14:44:54

Assignee: tbd

CC:  jsp

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used  (#7021)

CC was set to the Sun C compiler, and CXX to the Sun C++ compiler. It's apparent that singular is ignoring CC and using gcc instead. 

```
symmetrica-2.0.p4/src/zyk.c
symmetrica-2.0.p4/src/zyk.doc
symmetrica-2.0.p4/src/zykelind.c
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
make[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/symmetrica-2.0.p4/src'
gcc -c -O1 -fPIC -g -DFAST -DALLTRUE bar.c
gcc -c -O1 -fPIC -g -DFAST -DALLTRUE bi.c
```


It does build ok with gcc, even though CC is set to the Sun compiler. There is no C++ code, so I can't immediately tell whether CXX is ignored too, but I suspect it is. 


---

Comment by drkirkby created at 2010-01-07 01:57:39

I've created a fix for this long standing bug. Basically replacing 'gcc' with '$(CC)' in the makefile. 

I also changed spkg-install so SAGE64 was respected at the same time (in fact, that was my main motivation for fixing this ticket, as the failure to observe CC is not fatal, but a failure to observe SAGE64 is). 

The symmetica package is odd, in that the SPKG.txt makes it clear that fixes are applied to the source directly, not via patches. I find that a bit odd, but followed in the same way. I needed to fix the 'makefile' but left a copy of what I think is the original makefile as /src/makefile.original 

The package now add -m64 with SAGE64 set to yes, and fully respects CC. 

*This must be updated as a package, and not simply a patch applied, due to the fact that changes are made directly in the src directory.*

I've put everything at 

http://boxen.math.washington.edu/home/kirkby/portability/symmetrica-2.0.p5/


---

Comment by drkirkby created at 2010-01-07 01:57:39

Changing status from new to needs_review.


---

Comment by jsp created at 2010-01-10 22:27:50

Looks good, works on Fedora and Open Solaris.

Positive review.

Jaap


---

Comment by jsp created at 2010-01-10 22:27:50

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-14 02:01:31

Resolution: fixed
