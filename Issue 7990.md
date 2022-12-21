# Issue 7990: A new build failure on Solaris 10 SPARC.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-19 03:05:24

Assignee: drkirkby

Sage 4.3 built fine on Solaris 10 (SPARC), with the smallest of modifications needed if Sun Studio was installed. 

A gcc bug on Solaris causes #7932 to stop Sage building, though a workaround for that has been posted. 

However, another issue has arisen now. Whether it's related or not, I don't know, and have not had chance to investigate, though at first glance it looks unrelated.

See error below. 

```
/usr/local/gcc-4.4.1-sun-linker/bin/gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/export/home/drkirkby/sage-4.3.1.rc0/local/include/FLINT/ -I/export/home/drkirkby/sage-4.3.1.rc0/local//include -I/export/home/drkirkby/sage-4.3.1.rc0/local//include/csage -I/export/home/drkirkby/sage-4.3.1.rc0/devel//sage/sage/ext -I/export/home/drkirkby/sage-4.3.1.rc0/local/include/python2.6 -c sage/schemes/elliptic_curves/descent_two_isogeny.c -o build/temp.solaris-2.10-sun4u-2.6/sage/schemes/elliptic_curves/descent_two_isogeny.o -std=c99
In file included from /usr/include/limits.h:18,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/limits.h:122,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/syslimits.h:7,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/limits.h:11,
                 from /export/home/drkirkby/sage-4.3.1.rc0/local/include/python2.6/Python.h:19,
                 from sage/schemes/elliptic_curves/descent_two_isogeny.c:4:
/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/sys/feature_tests.h:341:2: error: #error "Compiler or options invalid for pre-UNIX 03 X/Open applications      and pre-2001 POSIX applications"
In file included from sage/schemes/elliptic_curves/descent_two_isogeny.c:148:
/export/home/drkirkby/sage-4.3.1.rc0/local//include/csage/ntl_wrap.h:142: warning: function declaration isn't a prototype
In file included from sage/schemes/elliptic_curves/descent_two_isogeny.c:148:
/export/home/drkirkby/sage-4.3.1.rc0/local//include/csage/ntl_wrap.h:310: warning: 'struct GF2X_c' declared inside parameter list
/export/home/drkirkby/sage-4.3.1.rc0/local//include/csage/ntl_wrap.h:310: warning: its scope is only this definition or declaration, which is probably not what you want
/export/home/drkirkby/sage-4.3.1.rc0/local//include/csage/ntl_wrap.h:319: warning: 'struct GF2E' declared inside parameter list
/export/home/drkirkby/sage-4.3.1.rc0/local//include/csage/ntl_wrap.h:327: warning: 'struct GF2' declared inside parameter list
In file included from /export/home/drkirkby/sage-4.3.1.rc0/local//include/FLINT/fmpz.h:36,
                 from sage/schemes/elliptic_curves/descent_two_isogeny.c:150:
/export/home/drkirkby/sage-4.3.1.rc0/local//include/FLINT/memory-manager.h:41: warning: function declaration isn't a prototype
/export/home/drkirkby/sage-4.3.1.rc0/local//include/FLINT/memory-manager.h:43: warning: function declaration isn't a prototype
/export/home/drkirkby/sage-4.3.1.rc0/local//include/FLINT/memory-manager.h:45: warning: function declaration isn't a prototype
In file included from /export/home/drkirkby/sage-4.3.1.rc0/local//include/FLINT/fmpz.h:38,
                 from sage/schemes/elliptic_curves/descent_two_isogeny.c:150:
/export/home/drkirkby/sage-4.3.1.rc0/local//include/FLINT/long_extras.h:287: warning: function declaration isn't a prototype
/export/home/drkirkby/sage-4.3.1.rc0/local//include/FLINT/long_extras.h:288: warning: function declaration isn't a prototype
In file included from /export/home/drkirkby/sage-4.3.1.rc0/local//include/FLINT/fmpz.h:39,
                 from sage/schemes/elliptic_curves/descent_two_isogeny.c:150:
/export/home/drkirkby/sage-4.3.1.rc0/local//include/FLINT/zn_poly/src/zn_poly.h:47: warning: function declaration isn't a prototype
error: command '/usr/local/gcc-4.4.1-sun-linker/bin/gcc' failed with exit status 1
sage: There was an error installing modified sage library code.

ERROR installing SAGE

real    113m16.782s
user    107m58.420s
sys     4m46.836s
sage: An error occurred while installing sage-4.3.1.rc0
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /export/home/drkirkby/sage-4.3.1.rc0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/export/home/drkirkby/sage-4.3.1.rc0/spkg/build/sage-4.3.1.rc0 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/export/home/drkirkby/sage-4.3.1.rc0/spkg/build/sage-4.3.1.rc0' && '/export/home/drkirkby/sage-4.3.1.rc0/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
make[1]: *** [installed/sage-4.3.1.rc0] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3.1.rc0/spkg'

real    405m36.430s
user    356m37.138s
sys     47m57.744s
Error building Sage.
```



---

Comment by drkirkby created at 2010-01-19 03:05:40

Changing priority from major to blocker.


---

Comment by dimpase created at 2010-03-18 16:36:44

Replying to [comment:1 drkirkby]:

can this be closed now? Apparently, whatever it was, has resolved itself.


---

Comment by dimpase created at 2010-03-18 16:36:44

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-03-19 15:49:50

Replying to [comment:2 dimpase]:
> Replying to [comment:1 drkirkby]:
> 
> can this be closed now? Apparently, whatever it was, has resolved itself.

Yes, it can. 

* Note to the release manager, whatever caused this, and I forget what, has now been resolved. As of Sage 4.3.4.rc0, Sage builds ok and passes all doc tests (including the long ones)*

Dave


---

Comment by jhpalmieri created at 2010-04-20 21:59:00

Resolution: worksforme
