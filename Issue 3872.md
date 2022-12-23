# Issue 3872: calculus -- incorporate ginac into without cln

Issue created by migration from https://trac.sagemath.org/ticket/3872

Original creator: was

Original creation time: 2008-08-15 10:11:17

Assignee: gfurnish

CC:  burcin robertwb

The goal of this ticket:

  1. Remove all dependency of ginac (http://www.ginac.de/) on CLN, so (a) Ginac builds in 2 minutes, (b) Ginac makes use of libraries like MPFR that are better than cln, and (c) in the future ginac will be able to work directly with *any* Sage objects. 

  2. Create a purely optional symbolic arithmetic class that works like this in parallel with the existing sage symbolics, but is far from feature complete:


```
sage: var("x y",ns=1)
(x, y)
sage: type(x)
<type 'sage.symbolic.expression.Expression'>
sage: expand((x^3*tan(x*y^x) + sin(y) - cos(y))^2)
cos(y)^2-2*cos(y)*sin(y)-2*cos(y)*x^3*tan(y^x*x) + x^6*tan(y^x*x)^2 + sin(y)^2 + 2*x^3*sin(y)*tan(y^x*x)
sage: timeit('expand((x^3*tan(x*y^x) + sin(y) - cos(y))^2)')
625 loops, best of 3: 107 µs per loop


sage: var("x y")
(x, y)
sage: timeit('expand((x^3*tan(x*y^x) + sin(y) - cos(y))^2)')
5 loops, best of 3: 24.5 ms per loop
sage: 24.5/(107*(10^(-3)))
228.971962616822


sage: x = sympy.var('x'); y = sympy.var('y')
sage: timeit("((x^3r * sympy.tan(x*y^x) + sympy.sin(y) - sympy.cos(y))^2r).expand()")
625 loops, best of 3: 691 µs per loop
```



The above would go in *before* any of this replaces the existing symbolic framework.


---

Comment by was created at 2008-08-15 10:20:05

Changing assignee from gfurnish to was.


---

Comment by was created at 2008-08-15 10:42:53

NOTE: There is something wrong on Itanium Linux since the library has no .so.  I did

```
  ln -s libginac-1.4.0.0.3 libginac.so
```

in local/lib, and then it built.  Mabshoff says "some autoconf problem".


---

Comment by certik created at 2008-08-19 20:48:07

This is impressive! Great job.

The patches look good to me in general. Just a naive question -- why do you need to call PY_NEW here:

 	82	cdef Expression new_Expression_from_GEx(GEx juice): 
 	83	    cdef Expression nex 
 	84	    nex = <Expression>PY_NEW(Expression) 
 	85	    GEx_construct_ex(&nex._gobj, juice) 
 	86	    nex._parent = ring.NSR 
 	87	    return nex 


? Is it some defficiency in Cython?


---

Comment by certik created at 2008-08-19 20:49:49

Sorry for the formatting, here:

```
 	82	cdef Expression new_Expression_from_GEx(GEx juice): 
 	83	    cdef Expression nex 
 	84	    nex = <Expression>PY_NEW(Expression) 
 	85	    GEx_construct_ex(&nex._gobj, juice) 
 	86	    nex._parent = ring.NSR 
 	87	    return nex 
```



---

Comment by robertwb created at 2008-08-20 02:04:08

PY_NEW is a macro that creates a new object without calling any of the `__init__` methods (it calls the tp_new function pointer directly).


---

Comment by certik created at 2008-08-20 11:06:12

Don't know if I am doing something wrong:

```
g++ -DHAVE_CONFIG_H -I. -I.. -I/home/ondra/ext/sage/local/include/python2.5/ -g -O2 -MT add.lo -MD -MP -MF .deps/add.Tpo -c add.cpp  -fPIC -DPIC -DPIC -o add.o
In file included from expair.h:27,
                 from expairseq.h:32,
                 from add.h:26,
                 from add.cpp:28:
numeric.h:97: error: extra qualification 'GiNaC::Number_T::' on member 'Number_T'
make[2]: *** [add.lo] Error 1
```

I am using Sage 3.1.1. Changing this:

Number_T::~Number_T();

to this:

~Number_T();

in numeric.h fixes the problem for me. Using:

```
$ g++ --version
g++ (Debian 4.3.1-9) 4.3.1
Copyright (C) 2008 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```


Unfortunately then it fails at:

```
g++ -DHAVE_CONFIG_H -I. -I.. -I/home/ondra/ext/sage/local/include/python2.5/ -g -O2 -MT numeric.lo -MD -MP -MF .deps/numeric.Tpo -c numeric.cpp  -fPIC -DPIC -DPIC -o numeric.o
numeric.cpp: In function 'std::ostream& GiNaC::operator<<(std::ostream&, const GiNaC::Number_T&)':
numeric.cpp:231: error: jump to case label
numeric.cpp:222: error:   crosses initialization of 'PyObject* o'
```


I don't have more time to investigate.


---

Attachment

attachment:pynac.2.hg (and also pynac.2.2.hg, thanks to trac) has a clean version of William's bundle, plus two changesets (one trivial).

I give a positive review to William's patch, someone should review mine.

There is also a new package file here:

http://www.risc.jku.at/people/berocal/sage/pynac-0.1.spkg

The only difference is a new SPKG.txt and an environment check on top of spkg-install.

As the ticket description states, these should go in after my changes are reviewed. I'll open new tickets for further additions to the pynac interface.


---

Comment by was created at 2008-09-23 23:39:54

Hi,

I read through Burcin's two patches to my patches, which he wrote when refereeing my code,
and I'm happy with them.

Mhansen, all mentioned to me that "he's read through all of this". 

I also tested building and running all this on the intel atom n270, and it works. 

So --- positive review!  Let's get this in sage.


---

Comment by mabshoff created at 2008-09-23 23:51:56

Replying to [comment:19 was]:

> So --- positive review!  Let's get this in sage.

After ghmm I want to do some wider build testing, especially on Linux Itanium, Solaris as well as Cygwin before merging this.

Cheers,

Michael


---

Comment by robertwb created at 2008-09-23 23:56:51

Trying to install the spkg on OS X 10.4


```
...
Configuration of GiNaC 1.4.3 done. Now type "make".
cd . && /bin/sh /Users/robert/sage/current/spkg/build/pynac-0.1/src/missing --run autoheader
aclocal.m4:17: error: this file was generated for autoconf 2.61.
You have another version of autoconf.  If you want to use that,
you should regenerate the build system entirely.
aclocal.m4:17: the top level
autom4te: /usr/bin/gm4 failed with exit status: 63
autoheader: /usr/bin/autom4te failed with exit status: 63
make: *** [config.h.in] Error 1
Error building ginac.

real    0m20.315s
user    0m6.509s
sys     0m11.412s
```


I could have sworn I tried this out a month ago (perhaps that was on sage.math).


---

Comment by mabshoff created at 2008-09-24 00:07:49

Well, the fix here is to run autoconf and friends with the --missing argument so that files that are linked and/or missing are instead copied into the archive. This will prevent the above problem from happening and also makes the spkg work in absence of autohell tools. If there is no script called autogen.sh we should add one so that rerunning those scripts is automated since one does tend to forget to run them all in the right order with the right parameters :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-27 19:22:37

Since this spkg is known broken at least on OSX 10.4 this needs work.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-30 09:49:50

A couple remarks:

 * pynac runs autoheader:

```
make  all-recursive
make[1]: Entering directory `/scratch/mabshoff/release-cycle/review/pynac-0.1/src'
Making all in ginac
```

 * CPPFLAGS and potentially LDFLAGS need to be set so we pick up Sage's Python:

```
/bin/sh ../libtool    --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. 
-I/scratch/mabshoff/release-cycle/sage-3.1.2.rc5/local/include/python2.5/   
-I/scratch/mabshoff/release-cycle/sage-3.1.2.rc5/local/include/python2.5  
-g -O2 -MT ex.lo -MD -MP -MF .deps/ex.Tpo -c -o ex.lo ex.cpp
```

 * spkg-install needs some cleanup, i.e. delete the PolyBoRi references, switch to #!/usr/bin/env bash, etc
 * SPKG.txt should explain which patches/changes were made to make Ginac work with Python types/remove the CLN dependency. That patch should be somewhere in a repo since at some point we will rebase on upstream
 * Ginac depends on dlopen, so this is a portability issue that needs to be taken into consideration and should be mentioned in SPKG.txt

Cheers,

Michael


---

Attachment

pynac bundle against 3.1.3.alpha2


---

Comment by burcin created at 2008-10-01 17:34:18

The spkg was split into ticket #4221.

attachment:pynac_3.1.3.alpha2.hg contains a new bundle that applies cleanly against 3.1.3.alpha2. There is a small additional patch over pynac.2.hg, which has minor corrections for the library name and coercion model changes.


---

Comment by burcin created at 2008-10-01 17:34:18

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-10-16 12:51:03

Positive review from me on pynac_3.1.3.alpha2.hg. Let's hope it still cleanly applies :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-18 00:01:20

Resolution: fixed


---

Comment by mabshoff created at 2008-10-18 00:01:20

Merged pynac_3.1.3.alpha2.hg in Sage 3.2.alpha0


---

Comment by jason created at 2008-10-18 03:54:24

Can we release alpha0 as soon as possible so that people can play with pynac and try to find bugs?


---

Comment by mabshoff created at 2008-10-18 08:49:09

Replying to [comment:28 jason]:
> Can we release alpha0 as soon as possible so that people can play with pynac and try to find bugs?

Yes, the plan to do so is very soon, i.e. alpha0 today. But we need to have a review for #4243 and #4244 to catch up with the current state of the art here.

Cheers,

Michael
