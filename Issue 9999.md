# Issue 9999: GSL libary fails to install on AIX 5.3

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-09-24 02:40:44

Assignee: drkirkby

CC:  fbissey

## Hardware and Software
 * IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
 * 4 x 332 MHz 32-bit PowerPC CPUs
 * 3 GB RAM
 * A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
 * DDS-4 tape drive 
 * AIX 5.3 (A POSIX certified operating system)
 * gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
 * sage-4.6.alpha1

 == The problem ==

```
gsl-1.14/src/
gsl-1.14/src/multimin/
"gsl-1.14.log" 2326 lines, 99663 characters
mv -f .deps/print.Tpo .deps/print.Plo
/bin/sh ../libtool --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I. -I.. -I..    -g -O2 -MT make_rep.lo -MD -MP -MF .deps/make_rep.Tpo
 -c -o make_rep.lo make_rep.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I.. -g -O2 -MT make_rep.lo -MD -MP -MF .deps/make_rep.Tpo -c make_rep.c  -DPIC -o .lib
s/make_rep.o
mv -f .deps/make_rep.Tpo .deps/make_rep.Plo
/bin/sh ../libtool --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I. -I.. -I..    -g -O2 -MT env.lo -MD -MP -MF .deps/env.Tpo -c -o env
.lo env.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I.. -g -O2 -MT env.lo -MD -MP -MF .deps/env.Tpo -c env.c  -DPIC -o .libs/env.o
mv -f .deps/env.Tpo .deps/env.Plo
/bin/sh ../libtool --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I. -I.. -I..    -g -O2 -MT fp.lo -MD -MP -MF .deps/fp.Tpo -c -o fp.lo
 fp.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I.. -g -O2 -MT fp.lo -MD -MP -MF .deps/fp.Tpo -c fp.c  -DPIC -o .libs/fp.o
In file included from fp.c:22:
fp-aix.c: In function 'gsl_ieee_set_mode':
fp-aix.c:30: error: 'fprnd_t' undeclared (first use in this function)
fp-aix.c:30: error: (Each undeclared identifier is reported only once
fp-aix.c:30: error: for each function it appears in.)
fp-aix.c:30: error: expected ';' before 'rnd'
fp-aix.c:55: error: 'rnd' undeclared (first use in this function)
fp-aix.c:55: error: 'FP_RND_RN' undeclared (first use in this function)
fp-aix.c:59: error: 'FP_RND_RM' undeclared (first use in this function)
fp-aix.c:63: error: 'FP_RND_RP' undeclared (first use in this function)
fp-aix.c:67: error: 'FP_RND_RZ' undeclared (first use in this function)
make[2]: *** [fp.lo] Error 1
make[2]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gsl-1.14/src/ieee-utils'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gsl-1.14/src'
make: *** [all] Error 2
Error building GSL

real    7m59.053s
user    5m41.085s
sys     0m49.623s
sage: An error occurred while installing gsl-1.14
```


 == Possible Solution ==
The same problem has been reported before against AIX 5.2

http://osdir.com/ml/lib.gsl.bugs/2006-06/msg00006.html


---

Attachment


---

Comment by leif created at 2010-09-24 02:45:14

*Congratulations to ticket number 10000... ;-)*

Are all HP-UX / AIX tickets yet "major"?


---

Comment by leif created at 2010-09-24 02:53:35

Replying to [comment:2 leif]:
> Are all HP-UX / AIX tickets yet "major"?

Ok, not all are.


---

Comment by vbraun created at 2010-09-24 11:29:06

The gsl INSTALL file has this to say:

```
If compiling with GCC the following error

  fp-aix.c: In function `gsl_ieee_set_mode':
  fp-aix.c:30: error: `fprnd_t' undeclared (first use in this function)

can occur if /usr/includes/float.h is not used, and instead the
float.h of the installed gcc is picked up instead -- it may be missing
the necessary structs.  To work around it copy the missing parts
(between #ifdef _ALL_SOURCE and its #endif) from /usr/includes/float.h
into a new header file and #include that in fp-aix.c
```



---

Comment by leif created at 2010-09-24 11:59:37

Replying to [comment:4 vbraun]:
> The gsl INSTALL file has this to say:

```
[...] To work around it copy the missing parts (between #ifdef _ALL_SOURCE and its #endif)
from /usr/includes/float.h into a new header file and #include that in fp-aix.c
```


It shouldn't be impossible to do that conditionally in GSL's `spkg-install`.


---

Comment by drkirkby created at 2010-09-24 12:08:29

Replying to [comment:4 vbraun]:
> The gsl INSTALL file has this to say:
> {{{
> If compiling with GCC the following error
> 
>   fp-aix.c: In function `gsl_ieee_set_mode':
>   fp-aix.c:30: error: `fprnd_t' undeclared (first use in this function)
> 
> can occur if /usr/includes/float.h is not used, and instead the
> float.h of the installed gcc is picked up instead -- it may be missing
> the necessary structs.  To work around it copy the missing parts
> (between #ifdef _ALL_SOURCE and its #endif) from /usr/includes/float.h
> into a new header file and #include that in fp-aix.c
> }}}

Thank you. That is most helpful. 

Dave


---

Comment by drkirkby created at 2010-09-24 12:33:52

Replying to [comment:5 leif]:
> Replying to [comment:4 vbraun]:
> > The gsl INSTALL file has this to say:
> {{{
> [...] To work around it copy the missing parts (between #ifdef _ALL_SOURCE and its #endif)
> from /usr/includes/float.h into a new header file and #include that in fp-aix.c
> }}}
> 
> It shouldn't be impossible to do that conditionally in GSL's `spkg-install`.

True, that is very easy to do. 

But one has to wonder why it's not taken care of in the GSL source code. It would be easy for the GSL developers to check if `fprnd_t` is defined or not in the configure script. I guess if there are a large number of things that might be undefined, then it would get a bit of a headache. 

I think Sage gets a lot harder to maintain, and a lot easier for bugs to get missed on one platform or another with so many conditional bits of code. 

 * We apply readline on some linux versions but not on all OpenSUSE versions
 * We use iconv on Solaris, HP-UX and Cygwin but not Linux or OS X. 
 * We patch `paripriv.h` on OS X and Solaris, but in different ways. 
 * etc etc etc. 

I prefer the `autoconf` approach of actually *testing* what is defined or not, rather than us making exceptions for this platform or that platform. 

Let's say I put code like:


```
   if[ "x$UNAME = xAIX ] ; then
      cp patches/fp-aix.c src/fp-aix.c # or wherever the file needs to go. 
   fi
```


then I've no idea if that is necessary on anything other than AIX 5.3. I might be able to find someone to test it on the next release of AIX which is 6.1. (IBM never released a 5.4 or 6.0, so their version numbering is even stranger than Sage's, which is saying something !!)  

My 32-bit machine is too old to run AIX 6.1, which only has a 64-bit kernel. AIX 5.3 is still officially supported by IBM and will be for a couple of years. Earlier verisons of AIX are no longer supported by IBM, so it is probably not worth worrying about earlier releases. But one should consider AIX 6.1, and the soon to be released AIX 7.0. 

Dave


---

Comment by leif created at 2010-09-24 13:12:37

Replying to [comment:7 drkirkby]:
> But one has to wonder why it's not taken care of in the GSL source code. It would be easy for the GSL developers to check if `fprnd_t` is defined or not in the configure script.

True.

>  * We apply readline on some linux versions but not on all OpenSUSE versions

That's because they decided to *dynamically* link `/bin/sh` (or `/bin/bash`) against `libreadline`, which is a bad idea. So the shell might break in case a less capable version is found (first) in e.g. `LD_LIBRARY_PATH`. (Proper versioning would also avoid this.)

>  * We use iconv on Solaris, HP-UX and Cygwin but not Linux or OS X. 

Because the assumption is that `iconv` is either broken or missing on those platforms.

>  * We patch `paripriv.h` on OS X and Solaris, but in different ways. 

Not true. Same patched file, just avoids a name clash with `ECHO` on those two systems. Not an upstream problem, since as the name suggests it's not intended to be installed / used outside the PARI sources.

>  * etc etc etc. 

True. ;-) (There are packages I think could and should be made prerequisites, which would avoid some trouble.)
 
> I prefer the `autoconf` approach of actually *testing* what is defined or not, rather than us making exceptions for this platform or that platform. 

Yes, but in general work-arounds made in Sage should be obsoleted by later upstream releases. (This is of course not always the case, and as seen above, some changes aren't upstream problems.)

> [...] I've no idea if that is necessary on anything other than AIX 5.3.

The snippet from GSL's `INSTALL` suggests it's not an AIX problem, but rather one of GCC.


---

Comment by drkirkby created at 2010-09-24 15:37:58

Replying to [comment:8 leif]:
> Replying to [comment:7 drkirkby]:
 
> >  * We use iconv on Solaris, HP-UX and Cygwin but not Linux or OS X. 
> 
> Because the assumption is that `iconv` is either broken or missing on those platforms.


But it's more complex than that, since if you include iconv on *some* Linux distributions it breaks the build of Sage. Otherwise we could just install it everywhere. 

> >  * We patch `paripriv.h` on OS X and Solaris, but in different ways. 
> 
> Not true. Same patched file, just avoids a name clash with `ECHO` on those two systems. Not an upstream problem, since as the name suggests it's not intended to be installed / used outside the PARI sources.

Em, there used to be two different patches, but perhaps that has changed. The patches needed on Solaris were a lot less than needed on OS X. 
 
> >  * etc etc etc. 
> 
> True. ;-) (There are packages I think could and should be made prerequisites, which would avoid some trouble.)
> > [...] I've no idea if that is necessary on anything other than AIX 5.3.
> 
> The snippet from GSL's `INSTALL` suggests it's not an AIX problem, but rather one of GCC.

All the more reason for this to be handled by autoconf. Since AIX is the only platform where this problem has been observed, it might be sensible to just make an AIX specific patch. 

I guess the GSL developers are quite within their rights to refuse to work around compiler bugs. I know the MPFR developers will not work around compiler bugs. 

I really wish I had a copy of the C standard, so knew exactly what should be defined and where. 

Dave


---

Comment by drkirkby created at 2010-09-26 21:25:51

Brian Gough agrees this should be handled by autoconf. He sent me an email, in which he said:

_I agree, if you can make a patch that handles this without breaking anything else I will add it.  As I don't use AIX I was not in a position to do that._

It's not high on my priority list, but I might look at this. 

Dave


---

Attachment

/usr/include/float.h from an RS/6000 7025 F50 running AIX 5.3 (This is a 32-bit PowerPC server)


---

Comment by drkirkby created at 2010-10-24 04:43:32

Replying to [comment:8 leif]:

> The snippet from GSL's `INSTALL` suggests it's not an AIX problem, but rather one of GCC.

Yes, I think that is correct. If one uses grep one can see `fprnd_t` is defined in IBM's `/usr/include/float.h` but it is defined in the headers created by gcc. 

I posted this problem to the gcc-help mailing list

http://gcc.gnu.org/ml/gcc-help/2010-10/msg00327.html

I was asked by  Ian Lance Taylor (who I suspect is one of the GCC developers) to post this as a bug on the gcc bug database. So I have now done that. 

This is now the following GCC bug:

http://gcc.gnu.org/bugzilla/show_bug.cgi?id=46155


---

Comment by drkirkby created at 2010-10-24 04:43:32

Changing keywords from "" to "gcc-bug".


---

Comment by drkirkby created at 2010-10-24 07:05:42

Replying to [comment:11 drkirkby]:
>  If one uses grep one can see `fprnd_t` is defined in IBM's `/usr/include/float.h` but it is defined in the headers created by gcc. 

I meant to say `fprnd_t` is defined in IBM's `/usr/include/float.h` but is *not* defined in any of the three `float.h` header files created by gcc. 



Dave


---

Comment by drkirkby created at 2010-11-06 15:39:46

I'm still of the opinion this is a gcc bug, but getting the gcc developers to fix it will be difficult. 

I's submitted two patches to the GSL team, which I've attached here. These are *not* in Mercurial format, so for the moment at least I don't intend patching the GSL package in Sage. However, they have been accepted upstream. I got an email today from Brian Gough, a GSL developer saying:

_Thanks for the patches, I've applied them._

So the next version of GSL should not have these issues on AIX. 

Dave


---

Comment by drkirkby created at 2010-11-06 15:42:28

Unified diff patch for configure.ac, which upstram developers have commited, so will be in the next GSL relese


---

Attachment

Unified diff patch for fp-aix.c, which upstram developers have commited, so will be in the next GSL relese


---

Attachment


---

Attachment

Mercurial patch that includes 1) Two patches which are applied by GNU patch 2) Changes to spkg-install to apply the patches. 3) A new 'configure' script. The latter makes this patch large


---

Comment by drkirkby created at 2011-03-23 23:52:10

I finally have a complete solution for the GSL problem on AIX, which not only means this now builds, but it pases all the tests too. The log file ends with:


```
The self-tests of GSL were successfully passed
```


The changes, which are only applied on AIX, consist of:

 * A revised configure.ac which checks for fprnd_t
 * Changes to an AIX-specific file fp-aix.c to define 'fprnd_t' 'FP_RND_RN','FP_RND_RM', 'FP_RND_RP' and 'FP_RND_RZ' if any of them are undefined. All definition were taken from the IBM header file float.h. 
 * Changes to spkg-install to apply the two patches. This uses GNU 'patch' (now part of Sage) to apply the patches. 
 * A new `configure` script that was generated for the updated `configure.ac`
 * A change to spkg-install to disable debug information when building on AIX. This is necessary since some Technology Levels or Service packs for AIX cause a problem when linking. 


```
ld: 0711-593 SEVERE ERROR: Symbol C_BSTAT (entry 635) in object siman_tsp.o:
        The symbol refers to a csect with symbol number 0, which was not
        found. The new symbol cannot be associated with a csect and
        is being ignored.
```

See http://www.ibm.com/developerworks/forums/thread.jspa?threadID=348558 and http://gcc.gnu.org/bugzilla/show_bug.cgi?id=46072 for information about this GCC bug, which is affecting many pieces of software - not just GSL. 

*Note* All changes to spkg-install are inside sections which have


```
If [ "x$UNAME~" = xAIX ] ; then
   # some changes
fi
```


so although these changes would not cause problems on any platform, for extra security they are only applied on AIX. 

This now needs review. Sorry for the size of the Mercurial patch, but this is because there's a new configure script that's auto-generated. That is quite large.


---

Comment by drkirkby created at 2011-03-23 23:52:10

Changing status from new to needs_review.


---

Comment by drkirkby created at 2011-03-23 23:58:58

Replying to [comment:15 drkirkby]:

> *Note* All changes to spkg-install are inside sections which have
> 
> {{{
> If [ "x$UNAME~" = xAIX ] ; then
>    # some changes
> fi
> }}}

Oops, there's a syntax error in what I just wrote in the trac, though the update .spkg file is fine.  I should have stated all changes to spkg-install are inside sections which have
 

```
If [ "x$UNAME" = xAIX ] ; then
   # some changes
fi

```



---

Comment by jdemeyer created at 2011-05-25 13:00:49

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2011-05-26 05:42:15

This has been fixed upstream in version 1.15 of GSL. The bug will be fixed in Sage when #11357 is merged, which updates the version of GSL in Sage from 1.14 to 1.15.  

Dave


---

Comment by jdemeyer created at 2011-05-31 09:48:16

Resolution: duplicate
