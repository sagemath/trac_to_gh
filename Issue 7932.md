# Issue 7932: _Complex_I undeclared - a new bug totally stops a Solaris 10 build.

Issue created by migration from https://trac.sagemath.org/ticket/7932

Original creator: drkirkby

Original creation time: 2010-01-15 01:32:35

Assignee: drkirkby

#6595 fixed a long standing bug which prevented Sage building on Solaris 10 (SPARC) if Sun Studio was installed. That allowed Sage to build properly on Solaris 10, so I set up 

http://t2nb.math.washington.edu:8000/

which clearly states 

_v4.3-patched-for-Solaris(SPARC)_

*Some changes(s) between Sage 4.3 and sage-4.3.1.alpha2 have completely broken the build on Solaris, so sage-4.3.1.alpha2 will not build on Solaris 10 (SPARC)*. I noticed this on my own Sun Blade 2000, but have also observed it on 't2'. 

Both my Sun Blade 2000 and 't2' use gcc 4.4.1. Neither compiler has been changed in any way since 4.3 was released. 

I'm marking this as a blocker, as Sage would have built for the first time in years on Solaris 10 if this bug had not been introduced. This newly introduced bug needs fixing.

I have created a tar file /rootpool2/local/kirkby/newly-broken-Solaris-build-sage-4.3.1.alpha2.tar on 't2' so I have record of this. I've made the permissions on /rootpool2/local/kirkby/sage-4.3.1.alpha2 world writable, so anyone who feels able to try to test this. (or grab the tar file and do it elsewhere). 

Dave 



```
gcc -shared build/temp.solaris-2.10-sun4v-2.6/sage/quadratic_forms/quadratic_form__evaluate.o -L/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//lib -lcsage -lstdc++ -lntl -o build/lib.solaris-2.10-sun4v-2.6/sage/quadratic_forms/quadratic_form__evaluate.so
building 'sage.rings.bernmm' extension
creating build/temp.solaris-2.10-sun4v-2.6/sage/rings/bernmm
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -DUSE_THREADS=1 -DTHREAD_STACK_SIZE=4096 -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//include -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//include/csage -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/devel//sage/sage/ext -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local/include/python2.6 -c sage/rings/bernmm.cpp -o build/temp.solaris-2.10-sun4v-2.6/sage/rings/bernmm.o -w
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -DUSE_THREADS=1 -DTHREAD_STACK_SIZE=4096 -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//include -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//include/csage -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/devel//sage/sage/ext -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local/include/python2.6 -c sage/rings/bernmm/bern_modp.cpp -o build/temp.solaris-2.10-sun4v-2.6/sage/rings/bernmm/bern_modp.o -w
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -DUSE_THREADS=1 -DTHREAD_STACK_SIZE=4096 -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//include -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//include/csage -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/devel//sage/sage/ext -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local/include/python2.6 -c sage/rings/bernmm/bern_modp_util.cpp -o build/temp.solaris-2.10-sun4v-2.6/sage/rings/bernmm/bern_modp_util.o -w
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -DUSE_THREADS=1 -DTHREAD_STACK_SIZE=4096 -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//include -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//include/csage -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/devel//sage/sage/ext -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local/include/python2.6 -c sage/rings/bernmm/bern_rat.cpp -o build/temp.solaris-2.10-sun4v-2.6/sage/rings/bernmm/bern_rat.o -w
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
g++ -shared build/temp.solaris-2.10-sun4v-2.6/sage/rings/bernmm.o build/temp.solaris-2.10-sun4v-2.6/sage/rings/bernmm/bern_modp.o build/temp.solaris-2.10-sun4v-2.6/sage/rings/bernmm/bern_modp_util.o build/temp.solaris-2.10-sun4v-2.6/sage/rings/bernmm/bern_rat.o -L/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//lib -lcsage -lgmp -lntl -lstdc++ -lpthread -lstdc++ -lntl -o build/lib.solaris-2.10-sun4v-2.6/sage/rings/bernmm.so
building 'sage.rings.bernoulli_mod_p' extension
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -Isage/libs/ntl/ -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//include -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//include/csage -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/devel//sage/sage/ext -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local/include/python2.6 -c sage/rings/bernoulli_mod_p.cpp -o build/temp.solaris-2.10-sun4v-2.6/sage/rings/bernoulli_mod_p.o -w
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
g++ -shared build/temp.solaris-2.10-sun4v-2.6/sage/rings/bernoulli_mod_p.o -L/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//lib -lcsage -lntl -lstdc++ -lstdc++ -lntl -o build/lib.solaris-2.10-sun4v-2.6/sage/rings/bernoulli_mod_p.so
building 'sage.rings.complex_double' extension
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//include -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local//include/csage -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/devel//sage/sage/ext -I/rootpool2/local/kirkby/sage-4.3.1.alpha2/local/include/python2.6 -c sage/rings/complex_double.c -o build/temp.solaris-2.10-sun4v-2.6/sage/rings/complex_double.o -std=c99 -D_XPG6 -w
sage/rings/complex_double.c: In function ‘__pyx_t_double_complex_from_parts’:
sage/rings/complex_double.c:14891: error: ‘_Complex_I’ undeclared (first use in this function)
sage/rings/complex_double.c:14891: error: (Each undeclared identifier is reported only once
sage/rings/complex_double.c:14891: error: for each function it appears in.)
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.

ERROR installing SAGE

real    181m48.343s
user    147m51.334s
sys     7m45.185s
sage: An error occurred while installing sage-4.3.1.alpha2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /rootpool2/local/kirkby/sage-4.3.1.alpha2/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/rootpool2/local/kirkby/sage-4.3.1.alpha2/spkg/build/sage-4.3.1.alpha2 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/rootpool2/local/kirkby/sage-4.3.1.alpha2/spkg/build/sage-4.3.1.alpha2' && '/rootpool2/local/kirkby/sage-4.3.1.alpha2/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
make[1]: *** [installed/sage-4.3.1.alpha2] Error 1
make[1]: Leaving directory `/rootpool2/local/kirkby/sage-4.3.1.alpha2/spkg'

real    1536m11.177s
user    1092m45.904s
sys     102m19.699s
Error building Sage.
```



---

Comment by robertwb created at 2010-01-15 02:42:03

This is probably my fault--maybe adding a --std=c99 flags or the like to the module list will help. (I know this code is valid, as we use it elsewhere, e.g. for the CDF fast float). 

I'll try to track it down during Sage days if I don't see a resolution sooner.


---

Comment by drkirkby created at 2010-01-15 03:07:54

The compiler line that is causing the problem does have _-std=c99_ I don't really understand what is going on in that library, the modules file, and I don't know C++ anyway, though I realise this bit is C. 

The Sun compiler wont even build previous versions of the Sage library, complaining the code is invalid. It tends to be a lot more fussy than gcc/g++. 

As can be seen in this patch, 

http://trac.sagemath.org/sage_trac/attachment/ticket/6595/sagelib_6595.patch

a couple of functions that were declared to return something, did not, yet gcc/g++ did not complain about it. Line 1078 shows an answer calculated, but it was never returned to the function calling it. Likewise William added line 282, which the Sun compiler chocked on, but the GNU compilers accept. These are clear errors.


---

Comment by robertwb created at 2010-01-15 05:33:46

I think it boils down to this: the file http://sage.math.washington.edu/home/robertwb/solaris/simple_complex.c compiles fine on sage.math, but not on t2. Any ideas why?


---

Comment by drkirkby created at 2010-01-15 08:05:08

I've no idea why, but it does build and run as expected with the Sun Studio compiler on t2.math.washington.edu (a Sun T5240 SPARC)


```
kirkby@t2:[~] $ /opt/SUNWspro/bin/cc  simple_complex.c
kirkby@t2:[~] $ ./a.out
CYTHON_CCOMPLEX 1
```


and also on my Sun Sun Ultra 27 (Intel Xeon) with Sun Studio 12.1


```
drkirkby@hawk:~$ /opt/sunstudio12.1/bin/cc simple_complex.c
drkirkby@hawk:~$ ./a.out
CYTHON_CCOMPLEX 1
```


but as you say, not on t2 if one uses 'gcc'. Nor does it build with gcc on my Sun Ultra 27 which has gcc 4.3.4 (the least buggy gcc according to some). 


```
drkirkby@hawk:~$ gcc  simple_complex.c
simple_complex.c: In function ‘__pyx_t_double_complex_from_parts’:
simple_complex.c:20: error: ‘_Complex_I’ undeclared (first use in this function)
simple_complex.c:20: error: (Each undeclared identifier is reported only once
simple_complex.c:20: error: for each function it appears in.)
```


This rather makes me think it is gcc bug, rather than a system header file. 

Dave


---

Comment by drkirkby created at 2010-01-15 10:47:35

I've submitted bug reports for Solaris 10 (SPARC)

http://gcc.gnu.org/bugzilla/show_bug.cgi?id=42753

and Open Solaris (x86)

http://gcc.gnu.org/bugzilla/show_bug.cgi?id=42755

Dave


---

Comment by robertwb created at 2010-01-16 00:25:43

See spkg at http://sage/home/robertwb/cython/cython-0.12.p1

This changes 


```
#if CYTHON_CCOMPLEX
  #ifdef __cplusplus
    #include <complex>
  #else
    #include <complex.h>
  #endif
#endif
```


to


```
#if CYTHON_CCOMPLEX
  #ifdef __cplusplus
    #include <complex>
  #else
    #include <complex.h>
    #if defined(__sun__) && defined(__GNUC__)
      #undef _Complex_I
      #define _Complex_I 1j
    #endif
  #endif
#endif
```


but it feels a bit hackish.


---

Comment by robertwb created at 2010-01-16 00:26:02

Also, http://gcc.gnu.org/bugzilla/show_bug.cgi?id=42753


---

Comment by drkirkby created at 2010-02-12 23:22:37

This does actually solve the problem, so if you could make this into an updated package, it would allow the Solaris build to get further, though it has recently been broken again by #7867 

Dave


---

Comment by drkirkby created at 2010-02-13 00:40:12

I should rephrase that. 

The .spkg you posted the other day did solve the problem, but I can't see it so obviously now. 

I hunted around a bit more, and found this one:

http://sage/home/robertwb/cython/cython-0.12.p1.spkg

which seems as though it was probably the one that solved the problem, but now I still have it. There's nothing in SPKG.txt to indicate whether this the one you patched for Solaris or not, so I am not sure. But whatever you changed before, did get this building. But now I find it failing at the same point. I suspect I downloaded the wrong file, or I need to remake more of the build. I can't power up the machine where I put the file - it is too noisy to start up just now, as my wife is asleep! 

Dave


---

Comment by robertwb created at 2010-02-15 19:49:43

The new version of Cython at #8163 fixes this issue. You need to do a sage -ba after installing.


---

Comment by mvngu created at 2010-03-01 01:53:02

Resolution: fixed


---

Comment by mvngu created at 2010-03-01 01:53:02

Close as fixed by #8163.
