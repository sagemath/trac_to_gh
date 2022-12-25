# Issue 9999: GSL libary fails to install on AIX 5.3

archive/issues_009999.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @kiwifb\n\n## Hardware and Software\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* DDS-4 tape drive \n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* sage-4.6.alpha1\n\n == The problem ==\n\n```\ngsl-1.14/src/\ngsl-1.14/src/multimin/\n\"gsl-1.14.log\" 2326 lines, 99663 characters\nmv -f .deps/print.Tpo .deps/print.Plo\n/bin/sh ../libtool --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I. -I.. -I..    -g -O2 -MT make_rep.lo -MD -MP -MF .deps/make_rep.Tpo\n -c -o make_rep.lo make_rep.c\nlibtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I.. -g -O2 -MT make_rep.lo -MD -MP -MF .deps/make_rep.Tpo -c make_rep.c  -DPIC -o .lib\ns/make_rep.o\nmv -f .deps/make_rep.Tpo .deps/make_rep.Plo\n/bin/sh ../libtool --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I. -I.. -I..    -g -O2 -MT env.lo -MD -MP -MF .deps/env.Tpo -c -o env\n.lo env.c\nlibtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I.. -g -O2 -MT env.lo -MD -MP -MF .deps/env.Tpo -c env.c  -DPIC -o .libs/env.o\nmv -f .deps/env.Tpo .deps/env.Plo\n/bin/sh ../libtool --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I. -I.. -I..    -g -O2 -MT fp.lo -MD -MP -MF .deps/fp.Tpo -c -o fp.lo\n fp.c\nlibtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I.. -g -O2 -MT fp.lo -MD -MP -MF .deps/fp.Tpo -c fp.c  -DPIC -o .libs/fp.o\nIn file included from fp.c:22:\nfp-aix.c: In function 'gsl_ieee_set_mode':\nfp-aix.c:30: error: 'fprnd_t' undeclared (first use in this function)\nfp-aix.c:30: error: (Each undeclared identifier is reported only once\nfp-aix.c:30: error: for each function it appears in.)\nfp-aix.c:30: error: expected ';' before 'rnd'\nfp-aix.c:55: error: 'rnd' undeclared (first use in this function)\nfp-aix.c:55: error: 'FP_RND_RN' undeclared (first use in this function)\nfp-aix.c:59: error: 'FP_RND_RM' undeclared (first use in this function)\nfp-aix.c:63: error: 'FP_RND_RP' undeclared (first use in this function)\nfp-aix.c:67: error: 'FP_RND_RZ' undeclared (first use in this function)\nmake[2]: *** [fp.lo] Error 1\nmake[2]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gsl-1.14/src/ieee-utils'\nmake[1]: *** [all-recursive] Error 1\nmake[1]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gsl-1.14/src'\nmake: *** [all] Error 2\nError building GSL\n\nreal    7m59.053s\nuser    5m41.085s\nsys     0m49.623s\nsage: An error occurred while installing gsl-1.14\n```\n\n\n == Possible Solution ==\nThe same problem has been reported before against AIX 5.2\n\nhttp://osdir.com/ml/lib.gsl.bugs/2006-06/msg00006.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/10000\n\n",
    "created_at": "2010-09-24T02:40:44Z",
    "labels": [
        "component: porting: aix or hp-ux",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "GSL libary fails to install on AIX 5.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9999",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @kiwifb

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

Issue created by migration from https://trac.sagemath.org/ticket/10000





---

archive/issue_comments_100292.json:
```json
{
    "body": "Attachment [gsl-1.14.log](tarball://root/attachments/some-uuid/ticket10000/gsl-1.14.log) by drkirkby created at 2010-09-24 02:42:29",
    "created_at": "2010-09-24T02:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100292",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [gsl-1.14.log](tarball://root/attachments/some-uuid/ticket10000/gsl-1.14.log) by drkirkby created at 2010-09-24 02:42:29



---

archive/issue_comments_100293.json:
```json
{
    "body": "**Congratulations to ticket number 10000... ;-)**\n\nAre all HP-UX / AIX tickets yet \"major\"?",
    "created_at": "2010-09-24T02:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100293",
    "user": "https://github.com/nexttime"
}
```

**Congratulations to ticket number 10000... ;-)**

Are all HP-UX / AIX tickets yet "major"?



---

archive/issue_comments_100294.json:
```json
{
    "body": "Replying to [comment:2 leif]:\n> Are all HP-UX / AIX tickets yet \"major\"?\n\nOk, not all are.",
    "created_at": "2010-09-24T02:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100294",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:2 leif]:
> Are all HP-UX / AIX tickets yet "major"?

Ok, not all are.



---

archive/issue_comments_100295.json:
```json
{
    "body": "The gsl INSTALL file has this to say:\n\n```\nIf compiling with GCC the following error\n\n  fp-aix.c: In function `gsl_ieee_set_mode':\n  fp-aix.c:30: error: `fprnd_t' undeclared (first use in this function)\n\ncan occur if /usr/includes/float.h is not used, and instead the\nfloat.h of the installed gcc is picked up instead -- it may be missing\nthe necessary structs.  To work around it copy the missing parts\n(between #ifdef _ALL_SOURCE and its #endif) from /usr/includes/float.h\ninto a new header file and #include that in fp-aix.c\n```\n",
    "created_at": "2010-09-24T11:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100295",
    "user": "https://github.com/vbraun"
}
```

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

archive/issue_comments_100296.json:
```json
{
    "body": "Replying to [comment:4 vbraun]:\n> The gsl INSTALL file has this to say:\n\n```\n[...] To work around it copy the missing parts (between #ifdef _ALL_SOURCE and its #endif)\nfrom /usr/includes/float.h into a new header file and #include that in fp-aix.c\n```\n\n\nIt shouldn't be impossible to do that conditionally in GSL's `spkg-install`.",
    "created_at": "2010-09-24T11:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100296",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:4 vbraun]:
> The gsl INSTALL file has this to say:

```
[...] To work around it copy the missing parts (between #ifdef _ALL_SOURCE and its #endif)
from /usr/includes/float.h into a new header file and #include that in fp-aix.c
```


It shouldn't be impossible to do that conditionally in GSL's `spkg-install`.



---

archive/issue_comments_100297.json:
```json
{
    "body": "Replying to [comment:4 vbraun]:\n> The gsl INSTALL file has this to say:\n> {{{\n> If compiling with GCC the following error\n> \n>   fp-aix.c: In function `gsl_ieee_set_mode':\n>   fp-aix.c:30: error: `fprnd_t' undeclared (first use in this function)\n> \n> can occur if /usr/includes/float.h is not used, and instead the\n> float.h of the installed gcc is picked up instead -- it may be missing\n> the necessary structs.  To work around it copy the missing parts\n> (between #ifdef _ALL_SOURCE and its #endif) from /usr/includes/float.h\n> into a new header file and #include that in fp-aix.c\n> }}}\n\nThank you. That is most helpful. \n\nDave",
    "created_at": "2010-09-24T12:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100297",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

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

archive/issue_comments_100298.json:
```json
{
    "body": "Replying to [comment:5 leif]:\n> Replying to [comment:4 vbraun]:\n> > The gsl INSTALL file has this to say:\n> {{{\n> [...] To work around it copy the missing parts (between #ifdef _ALL_SOURCE and its #endif)\n> from /usr/includes/float.h into a new header file and #include that in fp-aix.c\n> }}}\n> \n> It shouldn't be impossible to do that conditionally in GSL's `spkg-install`.\n\nTrue, that is very easy to do. \n\nBut one has to wonder why it's not taken care of in the GSL source code. It would be easy for the GSL developers to check if `fprnd_t` is defined or not in the configure script. I guess if there are a large number of things that might be undefined, then it would get a bit of a headache. \n\nI think Sage gets a lot harder to maintain, and a lot easier for bugs to get missed on one platform or another with so many conditional bits of code. \n\n* We apply readline on some linux versions but not on all OpenSUSE versions\n* We use iconv on Solaris, HP-UX and Cygwin but not Linux or OS X. \n* We patch `paripriv.h` on OS X and Solaris, but in different ways. \n* etc etc etc. \n\nI prefer the `autoconf` approach of actually **testing** what is defined or not, rather than us making exceptions for this platform or that platform. \n\nLet's say I put code like:\n\n\n```\n   if[ \"x$UNAME = xAIX ] ; then\n      cp patches/fp-aix.c src/fp-aix.c # or wherever the file needs to go. \n   fi\n```\n\n\nthen I've no idea if that is necessary on anything other than AIX 5.3. I might be able to find someone to test it on the next release of AIX which is 6.1. (IBM never released a 5.4 or 6.0, so their version numbering is even stranger than Sage's, which is saying something !!)  \n\nMy 32-bit machine is too old to run AIX 6.1, which only has a 64-bit kernel. AIX 5.3 is still officially supported by IBM and will be for a couple of years. Earlier verisons of AIX are no longer supported by IBM, so it is probably not worth worrying about earlier releases. But one should consider AIX 6.1, and the soon to be released AIX 7.0. \n\nDave",
    "created_at": "2010-09-24T12:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100298",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

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

I prefer the `autoconf` approach of actually **testing** what is defined or not, rather than us making exceptions for this platform or that platform. 

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

archive/issue_comments_100299.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> But one has to wonder why it's not taken care of in the GSL source code. It would be easy for the GSL developers to check if `fprnd_t` is defined or not in the configure script.\n\nTrue.\n\n>  * We apply readline on some linux versions but not on all OpenSUSE versions\n\nThat's because they decided to **dynamically** link `/bin/sh` (or `/bin/bash`) against `libreadline`, which is a bad idea. So the shell might break in case a less capable version is found (first) in e.g. `LD_LIBRARY_PATH`. (Proper versioning would also avoid this.)\n\n>  * We use iconv on Solaris, HP-UX and Cygwin but not Linux or OS X. \n\nBecause the assumption is that `iconv` is either broken or missing on those platforms.\n\n>  * We patch `paripriv.h` on OS X and Solaris, but in different ways. \n\nNot true. Same patched file, just avoids a name clash with `ECHO` on those two systems. Not an upstream problem, since as the name suggests it's not intended to be installed / used outside the PARI sources.\n\n>  * etc etc etc. \n\nTrue. ;-) (There are packages I think could and should be made prerequisites, which would avoid some trouble.)\n \n> I prefer the `autoconf` approach of actually **testing** what is defined or not, rather than us making exceptions for this platform or that platform. \n\nYes, but in general work-arounds made in Sage should be obsoleted by later upstream releases. (This is of course not always the case, and as seen above, some changes aren't upstream problems.)\n\n> [...] I've no idea if that is necessary on anything other than AIX 5.3.\n\nThe snippet from GSL's `INSTALL` suggests it's not an AIX problem, but rather one of GCC.",
    "created_at": "2010-09-24T13:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100299",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:7 drkirkby]:
> But one has to wonder why it's not taken care of in the GSL source code. It would be easy for the GSL developers to check if `fprnd_t` is defined or not in the configure script.

True.

>  * We apply readline on some linux versions but not on all OpenSUSE versions

That's because they decided to **dynamically** link `/bin/sh` (or `/bin/bash`) against `libreadline`, which is a bad idea. So the shell might break in case a less capable version is found (first) in e.g. `LD_LIBRARY_PATH`. (Proper versioning would also avoid this.)

>  * We use iconv on Solaris, HP-UX and Cygwin but not Linux or OS X. 

Because the assumption is that `iconv` is either broken or missing on those platforms.

>  * We patch `paripriv.h` on OS X and Solaris, but in different ways. 

Not true. Same patched file, just avoids a name clash with `ECHO` on those two systems. Not an upstream problem, since as the name suggests it's not intended to be installed / used outside the PARI sources.

>  * etc etc etc. 

True. ;-) (There are packages I think could and should be made prerequisites, which would avoid some trouble.)
 
> I prefer the `autoconf` approach of actually **testing** what is defined or not, rather than us making exceptions for this platform or that platform. 

Yes, but in general work-arounds made in Sage should be obsoleted by later upstream releases. (This is of course not always the case, and as seen above, some changes aren't upstream problems.)

> [...] I've no idea if that is necessary on anything other than AIX 5.3.

The snippet from GSL's `INSTALL` suggests it's not an AIX problem, but rather one of GCC.



---

archive/issue_comments_100300.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> Replying to [comment:7 drkirkby]:\n \n> >  * We use iconv on Solaris, HP-UX and Cygwin but not Linux or OS X. \n> \n> Because the assumption is that `iconv` is either broken or missing on those platforms.\n\n\nBut it's more complex than that, since if you include iconv on **some** Linux distributions it breaks the build of Sage. Otherwise we could just install it everywhere. \n\n> >  * We patch `paripriv.h` on OS X and Solaris, but in different ways. \n> \n> Not true. Same patched file, just avoids a name clash with `ECHO` on those two systems. Not an upstream problem, since as the name suggests it's not intended to be installed / used outside the PARI sources.\n\nEm, there used to be two different patches, but perhaps that has changed. The patches needed on Solaris were a lot less than needed on OS X. \n \n> >  * etc etc etc. \n> \n> True. ;-) (There are packages I think could and should be made prerequisites, which would avoid some trouble.)\n> > [...] I've no idea if that is necessary on anything other than AIX 5.3.\n> \n> The snippet from GSL's `INSTALL` suggests it's not an AIX problem, but rather one of GCC.\n\nAll the more reason for this to be handled by autoconf. Since AIX is the only platform where this problem has been observed, it might be sensible to just make an AIX specific patch. \n\nI guess the GSL developers are quite within their rights to refuse to work around compiler bugs. I know the MPFR developers will not work around compiler bugs. \n\nI really wish I had a copy of the C standard, so knew exactly what should be defined and where. \n\nDave",
    "created_at": "2010-09-24T15:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100300",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:8 leif]:
> Replying to [comment:7 drkirkby]:
 
> >  * We use iconv on Solaris, HP-UX and Cygwin but not Linux or OS X. 
> 
> Because the assumption is that `iconv` is either broken or missing on those platforms.


But it's more complex than that, since if you include iconv on **some** Linux distributions it breaks the build of Sage. Otherwise we could just install it everywhere. 

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

archive/issue_comments_100301.json:
```json
{
    "body": "Brian Gough agrees this should be handled by autoconf. He sent me an email, in which he said:\n\n*I agree, if you can make a patch that handles this without breaking anything else I will add it.  As I don't use AIX I was not in a position to do that.*\n\nIt's not high on my priority list, but I might look at this. \n\nDave",
    "created_at": "2010-09-26T21:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100301",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Brian Gough agrees this should be handled by autoconf. He sent me an email, in which he said:

*I agree, if you can make a patch that handles this without breaking anything else I will add it.  As I don't use AIX I was not in a position to do that.*

It's not high on my priority list, but I might look at this. 

Dave



---

archive/issue_comments_100302.json:
```json
{
    "body": "Attachment [float.h](tarball://root/attachments/some-uuid/ticket10000/float.h) by drkirkby created at 2010-09-27 12:46:26\n\n/usr/include/float.h from an RS/6000 7025 F50 running AIX 5.3 (This is a 32-bit PowerPC server)",
    "created_at": "2010-09-27T12:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100302",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [float.h](tarball://root/attachments/some-uuid/ticket10000/float.h) by drkirkby created at 2010-09-27 12:46:26

/usr/include/float.h from an RS/6000 7025 F50 running AIX 5.3 (This is a 32-bit PowerPC server)



---

archive/issue_comments_100303.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n\n> The snippet from GSL's `INSTALL` suggests it's not an AIX problem, but rather one of GCC.\n\nYes, I think that is correct. If one uses grep one can see `fprnd_t` is defined in IBM's `/usr/include/float.h` but it is defined in the headers created by gcc. \n\nI posted this problem to the gcc-help mailing list\n\nhttp://gcc.gnu.org/ml/gcc-help/2010-10/msg00327.html\n\nI was asked by  Ian Lance Taylor (who I suspect is one of the GCC developers) to post this as a bug on the gcc bug database. So I have now done that. \n\nThis is now the following GCC bug:\n\nhttp://gcc.gnu.org/bugzilla/show_bug.cgi?id=46155",
    "created_at": "2010-10-24T04:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100303",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:8 leif]:

> The snippet from GSL's `INSTALL` suggests it's not an AIX problem, but rather one of GCC.

Yes, I think that is correct. If one uses grep one can see `fprnd_t` is defined in IBM's `/usr/include/float.h` but it is defined in the headers created by gcc. 

I posted this problem to the gcc-help mailing list

http://gcc.gnu.org/ml/gcc-help/2010-10/msg00327.html

I was asked by  Ian Lance Taylor (who I suspect is one of the GCC developers) to post this as a bug on the gcc bug database. So I have now done that. 

This is now the following GCC bug:

http://gcc.gnu.org/bugzilla/show_bug.cgi?id=46155



---

archive/issue_comments_100304.json:
```json
{
    "body": "Changing keywords from \"\" to \"gcc-bug\".",
    "created_at": "2010-10-24T04:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100304",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing keywords from "" to "gcc-bug".



---

archive/issue_comments_100305.json:
```json
{
    "body": "Replying to [comment:11 drkirkby]:\n>  If one uses grep one can see `fprnd_t` is defined in IBM's `/usr/include/float.h` but it is defined in the headers created by gcc. \n\nI meant to say `fprnd_t` is defined in IBM's `/usr/include/float.h` but is **not** defined in any of the three `float.h` header files created by gcc. \n\n\n\nDave",
    "created_at": "2010-10-24T07:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100305",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:11 drkirkby]:
>  If one uses grep one can see `fprnd_t` is defined in IBM's `/usr/include/float.h` but it is defined in the headers created by gcc. 

I meant to say `fprnd_t` is defined in IBM's `/usr/include/float.h` but is **not** defined in any of the three `float.h` header files created by gcc. 



Dave



---

archive/issue_comments_100306.json:
```json
{
    "body": "I'm still of the opinion this is a gcc bug, but getting the gcc developers to fix it will be difficult. \n\nI's submitted two patches to the GSL team, which I've attached here. These are **not** in Mercurial format, so for the moment at least I don't intend patching the GSL package in Sage. However, they have been accepted upstream. I got an email today from Brian Gough, a GSL developer saying:\n\n*Thanks for the patches, I've applied them.*\n\nSo the next version of GSL should not have these issues on AIX. \n\nDave",
    "created_at": "2010-11-06T15:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100306",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm still of the opinion this is a gcc bug, but getting the gcc developers to fix it will be difficult. 

I's submitted two patches to the GSL team, which I've attached here. These are **not** in Mercurial format, so for the moment at least I don't intend patching the GSL package in Sage. However, they have been accepted upstream. I got an email today from Brian Gough, a GSL developer saying:

*Thanks for the patches, I've applied them.*

So the next version of GSL should not have these issues on AIX. 

Dave



---

archive/issue_comments_100307.json:
```json
{
    "body": "Unified diff patch for configure.ac, which upstram developers have commited, so will be in the next GSL relese",
    "created_at": "2010-11-06T15:42:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100307",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Unified diff patch for configure.ac, which upstram developers have commited, so will be in the next GSL relese



---

archive/issue_comments_100308.json:
```json
{
    "body": "Attachment [configure.ac.patch](tarball://root/attachments/some-uuid/ticket10000/configure.ac.patch) by drkirkby created at 2010-11-06 15:43:21\n\nUnified diff patch for fp-aix.c, which upstram developers have commited, so will be in the next GSL relese",
    "created_at": "2010-11-06T15:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100308",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [configure.ac.patch](tarball://root/attachments/some-uuid/ticket10000/configure.ac.patch) by drkirkby created at 2010-11-06 15:43:21

Unified diff patch for fp-aix.c, which upstram developers have commited, so will be in the next GSL relese



---

archive/issue_comments_100309.json:
```json
{
    "body": "Attachment [fp-aix.c.patch](tarball://root/attachments/some-uuid/ticket10000/fp-aix.c.patch) by @kiwifb created at 2011-03-17 01:33:57",
    "created_at": "2011-03-17T01:33:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100309",
    "user": "https://github.com/kiwifb"
}
```

Attachment [fp-aix.c.patch](tarball://root/attachments/some-uuid/ticket10000/fp-aix.c.patch) by @kiwifb created at 2011-03-17 01:33:57



---

archive/issue_comments_100310.json:
```json
{
    "body": "Attachment [gsl-fixes-for-AIX.patch](tarball://root/attachments/some-uuid/ticket10000/gsl-fixes-for-AIX.patch) by drkirkby created at 2011-03-23 23:13:59\n\nMercurial patch that includes 1) Two patches which are applied by GNU patch 2) Changes to spkg-install to apply the patches. 3) A new 'configure' script. The latter makes this patch large",
    "created_at": "2011-03-23T23:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100310",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [gsl-fixes-for-AIX.patch](tarball://root/attachments/some-uuid/ticket10000/gsl-fixes-for-AIX.patch) by drkirkby created at 2011-03-23 23:13:59

Mercurial patch that includes 1) Two patches which are applied by GNU patch 2) Changes to spkg-install to apply the patches. 3) A new 'configure' script. The latter makes this patch large



---

archive/issue_comments_100311.json:
```json
{
    "body": "I finally have a complete solution for the GSL problem on AIX, which not only means this now builds, but it pases all the tests too. The log file ends with:\n\n\n```\nThe self-tests of GSL were successfully passed\n```\n\n\nThe changes, which are only applied on AIX, consist of:\n\n* A revised configure.ac which checks for fprnd_t\n* Changes to an AIX-specific file fp-aix.c to define 'fprnd_t' 'FP_RND_RN','FP_RND_RM', 'FP_RND_RP' and 'FP_RND_RZ' if any of them are undefined. All definition were taken from the IBM header file float.h. \n* Changes to spkg-install to apply the two patches. This uses GNU 'patch' (now part of Sage) to apply the patches. \n* A new `configure` script that was generated for the updated `configure.ac`\n* A change to spkg-install to disable debug information when building on AIX. This is necessary since some Technology Levels or Service packs for AIX cause a problem when linking. \n\n\n```\nld: 0711-593 SEVERE ERROR: Symbol C_BSTAT (entry 635) in object siman_tsp.o:\n        The symbol refers to a csect with symbol number 0, which was not\n        found. The new symbol cannot be associated with a csect and\n        is being ignored.\n```\n\nSee http://www.ibm.com/developerworks/forums/thread.jspa?threadID=348558 and http://gcc.gnu.org/bugzilla/show_bug.cgi?id=46072 for information about this GCC bug, which is affecting many pieces of software - not just GSL. \n\n**Note** All changes to spkg-install are inside sections which have\n\n\n```\nIf [ \"x$UNAME~\" = xAIX ] ; then\n   # some changes\nfi\n```\n\n\nso although these changes would not cause problems on any platform, for extra security they are only applied on AIX. \n\nThis now needs review. Sorry for the size of the Mercurial patch, but this is because there's a new configure script that's auto-generated. That is quite large.",
    "created_at": "2011-03-23T23:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100311",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

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

**Note** All changes to spkg-install are inside sections which have


```
If [ "x$UNAME~" = xAIX ] ; then
   # some changes
fi
```


so although these changes would not cause problems on any platform, for extra security they are only applied on AIX. 

This now needs review. Sorry for the size of the Mercurial patch, but this is because there's a new configure script that's auto-generated. That is quite large.



---

archive/issue_comments_100312.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-23T23:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100312",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100313.json:
```json
{
    "body": "Replying to [comment:15 drkirkby]:\n\n> **Note** All changes to spkg-install are inside sections which have\n> \n> {{{\n> If [ \"x$UNAME~\" = xAIX ] ; then\n>    # some changes\n> fi\n> }}}\n\nOops, there's a syntax error in what I just wrote in the trac, though the update .spkg file is fine.  I should have stated all changes to spkg-install are inside sections which have\n \n\n```\nIf [ \"x$UNAME\" = xAIX ] ; then\n   # some changes\nfi\n\n```\n",
    "created_at": "2011-03-23T23:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100313",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:15 drkirkby]:

> **Note** All changes to spkg-install are inside sections which have
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

archive/issue_comments_100314.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-25T13:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100314",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_100315.json:
```json
{
    "body": "This has been fixed upstream in version 1.15 of GSL. The bug will be fixed in Sage when #11357 is merged, which updates the version of GSL in Sage from 1.14 to 1.15.  \n\nDave",
    "created_at": "2011-05-26T05:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100315",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This has been fixed upstream in version 1.15 of GSL. The bug will be fixed in Sage when #11357 is merged, which updates the version of GSL in Sage from 1.14 to 1.15.  

Dave



---

archive/issue_events_010123.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-31T09:48:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9999#event-10123"
}
```



---

archive/issue_comments_100316.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-05-31T09:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9999#issuecomment-100316",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
