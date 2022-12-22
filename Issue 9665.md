# Issue 9665: Make lcalc accessible as a library on OS X

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-08-01 21:18:40

Assignee: tbd

CC:  fbissey drkirkby georgsweber rishi robertwb was ylchapuy mrubinst@math.uwaterloo.ca kcrisman

Reported by Georg Weber on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/fa2facb36603675a/a19253d8c2f48d2f#a19253d8c2f48d2f):

```
...
building 'sage.libs.lcalc.lcalc_Lfunction' extension
...
g++ -L/Users/Shared/sage/sage-4.5.2.rc0/local/lib -bundle -undefined
dynamic_lookup build/temp.macosx-10.4-i386-2.6/sage/libs/lcalc/
lcalc_Lfunction.o -L/Users/Shared/sage/sage-4.5.2.rc0/local//lib -
lcsage -lm -lntl -lmpfr -lgmp -lgmpxx -lLfunction -lstdc++ -lstdc++ -
lntl -o build/lib.macosx-10.4-i386-2.6/sage/libs/lcalc/
lcalc_Lfunction.so
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-
prototypes -I/Users/Shared/sage/sage-4.5.2.rc0/local//include -I/Users/
Shared/sage/sage-4.5.2.rc0/local//include/csage -I/Users/Shared/sage/
sage-4.5.2.rc0/devel//sage/sage/ext -I/Users/Shared/sage/
sage-4.5.2.rc0/local/include/python2.6 -c sage/libs/pari/gen.c -o
build/temp.macosx-10.4-i386-2.6/sage/libs/pari/gen.o -w
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: can't locate file for: -
lLfunction
collect2: ld returned 1 exit status
error: command 'g++' failed with exit status 1
sage: There was an error installing modified sage library code.
...

It seems that in the Sage library code, the usage of some "Lfunction"
library from the lcalc package was newly introduced. On my Mac, both
the (half-built) Sage-4.5.2 and the older (fuly working) Sage-4.5.1
have under local/lib/ some library "libLfunction.so". But on a Mac
under OS X (OS X 10.4 at least), this would need to be
"libLfunction.dylib" to be usable ... 
```


[Georg continues](http://groups.google.com/group/sage-release/browse_thread/thread/fa2facb36603675a/99b55c2958a197cb#99b55c2958a197cb):

```
for the "Lfunction" issue, the relevant tickets are #5396 resp. #4793.
It seems to be as I thought --- the lcalc spkg (#4793) never built a
correct dynamic (".dylib") library on OS X. But this was not relevant
or did break anything, until the interface between Sage and lcalc was
changed from using pexpect to using this library directly (#5396,
introduced in Sage-4.5.2.alpha1). 
```


Related: #4793, #5396.


---

Comment by mpatel created at 2010-08-01 21:34:21

Sage 4.5.2.rc0 happens to build successfully and pass the long doctests on bsd.math.  In particular,

```sh
$ uname -a
Darwin bsd.local 10.4.0 Darwin Kernel Version 10.4.0: Fri Apr 23 18:28:53 PDT 2010; root:xnu-1504.7.4~1/RELEASE_I386 i386
$ pwd
/Users/mpatel/apps/sage-4.5.2.rc0
$ find . | grep libLfunction
./local/lib/libLfunction.so
$ touch devel/sage-main/sage/libs/lcalc/lcalc_Lfunction.pyx
$ ./sage -b
...
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/mpatel/apps/sage-4.5.2.rc0/local/include/lcalc/ -I/Users/mpatel/apps/sage-4.5.2.rc0/local//include -I/Users/mpatel/apps/sage-4.5.2.rc0/local//include/csage -I/Users/mpatel/apps/sage-4.5.2.rc0/devel//sage/sage/ext -I/Users/mpatel/apps/sage-4.5.2.rc0/local/include/python2.6 -c sage/libs/lcalc/lcalc_Lfunction.cpp -o build/temp.macosx-10.6-i386-2.6/sage/libs/lcalc/lcalc_Lfunction.o -O3 -ffast-math -w
...
g++ -L/Users/mpatel/apps/sage-4.5.2.rc0/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.6-i386-2.6/sage/libs/lcalc/lcalc_Lfunction.o -L/Users/mpatel/apps/sage-4.5.2.rc0/local//lib -lcsage -lm -lntl -lmpfr -lgmp -lgmpxx -lLfunction -lstdc++ -lstdc++ -lntl -o build/lib.macosx-10.6-i386-2.6/sage/libs/lcalc/lcalc_Lfunction.so
...
```

finishes with several warnings but no errors.  Does bsd.math not require a .dylib library?

Disclaimer:  I'm not familiar with OS X.


---

Comment by GeorgSWeber created at 2010-08-02 11:12:12

Replying to [comment:1 mpatel]:
> Sage 4.5.2.rc0 happens to build successfully and pass the long doctests on bsd.math. Does bsd.math not require a .dylib library?
> 
> Disclaimer:  I'm not familiar with OS X.

The "bsd.math" Mac runs with OS X 10.6 using Apples version of GCC 4.2, and obviously this one knows how to handle ".so" dynamic libraries in addition to ".dylib" ones. I suspected so earlier, but since I work almost exclusively with OS X 10.4 (and thus Apples version of GCC 4.0.1), I couldn't tell, or know, for sure. So OS X 10.6 is "out of the game" for the time being.

But how about OS X 10.5 (I think it also still uses GCC 4.0.1)?
Any results on this platform anybody?


---

Comment by rishi created at 2010-08-02 15:11:55

Last time I built on 10.5, it worked fine. I do not have access to 10.4 intel machine. I am building it again, but I do not think anything should change since last time.

Replying to [comment:3 GeorgSWeber]:
> Replying to [comment:1 mpatel]:
> > Sage 4.5.2.rc0 happens to build successfully and pass the long doctests on bsd.math. Does bsd.math not require a .dylib library?
> > 
> > Disclaimer:  I'm not familiar with OS X.
> 
> The "bsd.math" Mac runs with OS X 10.6 using Apples version of GCC 4.2, and obviously this one knows how to handle ".so" dynamic libraries in addition to ".dylib" ones. I suspected so earlier, but since I work almost exclusively with OS X 10.4 (and thus Apples version of GCC 4.0.1), I couldn't tell, or know, for sure. So OS X 10.6 is "out of the game" for the time being.
> 
> But how about OS X 10.5 (I think it also still uses GCC 4.0.1)?
> Any results on this platform anybody?


---

Comment by rishi created at 2010-08-02 16:06:02

It works fine on 10.5 on intel mac. I could not replicate the problem. I am also building on a ppc machine. This should take a long time.


---

Comment by kcrisman created at 2010-08-02 16:13:09

It sounds from gsw that the issue is Tiger, not PPC versus Intel (he has Intel for Tiger).  Does anyone know of an spkg that builds .so files versus .dylib files for these situations? Then one could copy that naively and a non-expert (say, me) with access to Tiger could try it out.

Otherwise, [this](http://osdir.com/ml/bug-libtool-gnu/2010-02/msg00003.html) link seems relevant, though I can't gauge its usefulness for sure.


---

Comment by rishi created at 2010-08-02 19:08:16

Changing status from new to needs_review.


---

Comment by rishi created at 2010-08-02 19:08:16

New spkg should work. It is only needed to compile on 10.4. If you are using a compiled version from 10.5 to run on 10.4 then this spkg update is not needed. 

http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-20100428-1.23.p1.spkg


---

Comment by GeorgSWeber created at 2010-08-02 19:25:48

In the meantime, I had a look on the "p0" spkg build system (makefile and such). All seems fine, except that ".so" is hardcoded as suffix. Usually, one has something like $(SO_SUFFIX), and this defaults to so on Linux, dylib on Mac OS X, and dll under Windows. No surprise that in the spkg-install, it is said that this lcalc spkg does not work under Cygwin ...

But otherwise, OS X is taken care for in the build system, e.g. using "dynamiclib" as an option instead of "shared". So I duplicated under /local/lib/ the file "libLfunction.so" to another file "libLfunction.dylib" and, oh wonder, everything works fine. Sage builds, and the doctest for "devel/sage/sage/libs/lcalc/lcalc_Lfunction.pyx" passes.

Now I just downloaded the "p1" lcalc spkg and check it out. Thanks for the quick work!


---

Comment by kcrisman created at 2010-08-02 19:33:03

Replying to [comment:9 GeorgSWeber]:
> In the meantime, I had a look on the "p0" spkg build system (makefile and such). All seems fine, except that ".so" is hardcoded as suffix. Usually, one has something like $(SO_SUFFIX), and this defaults to so on Linux, dylib on Mac OS X, and dll under Windows. No surprise that in the spkg-install, it is said that this lcalc spkg does not work under Cygwin ...
> 

Does that mean the 'correct' fix is to do this instead, since we eventually want to get Cygwin or whatever to work?  Presumably drkirkby has a comment about this as well :)


---

Comment by GeorgSWeber created at 2010-08-02 20:12:39

Replying to [comment:10 kcrisman]:
> Replying to [comment:9 GeorgSWeber]:
> > In the meantime, I had a look on the "p0" spkg build system (makefile and such). All seems fine, except that ".so" is hardcoded as suffix. Usually, one has something like $(SO_SUFFIX), and this defaults to so on Linux, dylib on Mac OS X, and dll under Windows. No surprise that in the spkg-install, it is said that this lcalc spkg does not work under Cygwin ...
> > 
> 
> Does that mean the 'correct' fix is to do this instead, since we eventually want to get Cygwin or whatever to work?  Presumably drkirkby has a comment about this as well :)

*This* ticket is about OS X 10.4, and although the difference between p0 and p1 is a quick and dirty hack --- it's exactly the one I myself had in mind ...

Let's open up a new ticket for the Cygwin issues (resp. there probably is already one), and close this one. Because I'm giving it a positive review (I just tested it OK).


---

Comment by GeorgSWeber created at 2010-08-02 20:12:39

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-02 23:24:27

Replying to [comment:3 GeorgSWeber]:
> Replying to [comment:1 mpatel]:
> > Sage 4.5.2.rc0 happens to build successfully and pass the long doctests on bsd.math. Does bsd.math not require a .dylib library?
> > 
> > Disclaimer:  I'm not familiar with OS X.
> 
> The "bsd.math" Mac runs with OS X 10.6 using Apples version of GCC 4.2, and obviously this one knows how to handle ".so" dynamic libraries in addition to ".dylib" ones.

Thanks to Georg and [Karl-Dieter](http://groups.google.com/group/sage-release/browse_thread/thread/fa2facb36603675a/570c8fc35ac1014d#570c8fc35ac1014d) for their clarifications!


---

Comment by mpatel created at 2010-08-04 02:11:41

Resolution: fixed


---

Comment by kcrisman created at 2010-08-04 03:02:30

Just to confirm, this worked fine on my PPC OS X 10.4 Mac as well, so it works on Intel and PPC (as it should, having read the hack).  Huzzah!


---

Comment by rishi created at 2010-08-06 19:48:01

>Hi Dave,
>
>the makefile needed some sanity put back into it, especially linker wise. so that was a job that >was needed. I guess my main concern here is:
>
>*lcalc depends on mpfr when it shouldn't.

lcalc as included does not need mpfr. Mike has experimental code which uses mpfr.

>
>The rest is just my ramblings about there being an unused variable in spkg-install - which may >lead people to think it is.

Feel free to clean and put up an spkg for review.

>
>Francois


---

Comment by kcrisman created at 2010-08-06 20:00:57

Replying to [comment:16 rishi]:
> >Hi Dave,
> >
> >the makefile needed some sanity put back into it, especially linker wise. so that was a job that >was needed. I guess my main concern here is:
> >
> >*lcalc depends on mpfr when it shouldn't.
> 
> lcalc as included does not need mpfr. Mike has experimental code which uses mpfr.
> 
> >
> >The rest is just my ramblings about there being an unused variable in spkg-install - which may >lead people to think it is.
> 
> Feel free to clean and put up an spkg for review.
> 

This should probably be on a different ticket, though.


---

Comment by fbissey created at 2010-08-06 22:13:25

OK since I am redirected here.
Yes the lcalc spkg cleaning should happen in another ticket.
But does the lcalc wrapper in sage really need mpfr if lcalc
doesn't? From the new module_list.py:

```
    Extension('sage.libs.lcalc.lcalc_Lfunction',
              sources = ['sage/libs/lcalc/lcalc_Lfunction.pyx'],
              libraries = ['m', 'ntl', 'mpfr', 'gmp', 'gmpxx',
                           'Lfunction', 'stdc++'],
              include_dirs = [SAGE_ROOT + "/local/include/lcalc/"],
              extra_compile_args=["-O3", "-ffast-math"],
              language = 'c++'),
```

As a matter of fact I don't think it depends on gmp and gmpxx either.
Those are added when you use mpfr.
Actually at the moment Lfunction.so is never ever linked against mpfr, gmp,
gmpxx and pari. Only the lcalc executable is. The same could be said for ntl,
which isn't a dependency of lcalc at all.
So unless the wrapper itself needs any of these I suggest they should go.

Francois


---

Comment by rishi created at 2010-08-06 22:46:39

Yes it needs them. If you do not agree, try to remove and compile and see the error message, or better yet, see the code for the pyx file. It has been quite a long time since I wrote the wrapper. I never used NTL, but the wrapper does not compile without without those flags.


---

Comment by mpatel created at 2010-08-13 21:30:26

In case anyone is already working on the lcalc spkg (`spkg-install` changes, dependencies, etc.) for a different ticket:  Ticket #9592 updates the lcalc package so that it's compatible with #9343's PARI upgrade.
