# Issue 7851: libz igoresSAGE64 other than on OS X

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-05 19:04:56

Assignee: drkirkby

CC:  jsp

The spkg-install of libz zlib-1.2.3.p5 has this:


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   CFLAGS=" -m64 $CFLAGS -fPIC -g -I\"$SAGE_LOCAL/include\""
   cp ../patches/configure-OSX-64 configure
else
   CFLAGS="$CFLAGS -fPIC -g -I\"$SAGE_LOCAL/include\""
fi
export CFLAGS
```


so is almost doomed to a 64-bit build unless one sets CFLAGS externally. 


---

Comment by drkirkby created at 2010-01-12 05:53:23

Changing status from new to needs_review.


---

Attachment

With the recent updates to sage-env, this will actually build in 64-bit mode, as that will set CFLAGS appropriately. But there were some other issues with this package, so the following have been addressed. 

 * Move -I $SAGE_LOCAL/include to CPPFLAGS, not CFLAGS
   There's no reason it should go there. 
 * Removed most of the SAGE64 related stuff. The only bit 
   remaining is to apply a patch on OS X in 64-bit mode. 
 * Removed -Wall and -g from CFLAGS - the new sage-eve 
   will add these automatically for gcc. Since they are 
   GNU specific flags, they would break with other compilers. 
 * Substituted -fPIC for $FPIC_FLAG as -fPIC is a GNU specfic 
   option and sage-env defines FPIC_FLAG to be -fPIC for 
   gcc, but other things for Sun Studio and other compilers from
   HP and IBM. 

An updated spkg can be found at 

http://boxen.math.washington.edu/home/kirkby/portability/zlib-1.2.3.p6/zlib-1.2.3.p6.spkg

other relevant files in http://boxen.math.washington.edu/home/kirkby/portability/zlib-1.2.3.p6/

Dave


---

Comment by drkirkby created at 2010-01-12 17:17:49

I'm not 100% happy with this. I'm returning it to 'needs work.'


---

Comment by drkirkby created at 2010-01-12 17:17:49

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-01-28 12:35:22

This problem is not as simple as I first thought. Using the zlib source code, without any CFLAGS, but with the --shared option, we get the message the shared library is built. 


```
drkirkby`@`swan:[~/sage-4.3.1.alpha1/spkg/standard/zlib-1.2.3.p5/src] $  ./configure --shared
Checking for shared library support...
Building shared library libz.so.1.2.3 with /usr/local/gcc-4.4.1-sun-linker/bin/gcc.
Checking for unistd.h... Yes.
Checking whether to use vs[n]printf() or s[n]printf()... using vs[n]printf()
Checking for vsnprintf() in stdio.h... Yes.
Checking for return value of vsnprintf()... Yes.
Checking for errno.h... Yes.
Checking for mmap support... Yes.
```


Trying to build in 64-bit mode, the shared library is not built. 


```
drkirkby`@`swan:[~/sage-4.3.1.alpha1/spkg/standard/zlib-1.2.3.p5/src] $ CFLAGS=-m64  ./configure --shared
Checking for shared library support...
No shared library support; try without defining CC and CFLAGS
Building static library libz.a version 1.2.3 with /usr/local/gcc-4.4.1-sun-linker/bin/gcc.
Checking for unistd.h... Yes.
Checking whether to use vs[n]printf() or s[n]printf()... using vs[n]printf()
Checking for vsnprintf() in stdio.h... Yes.
Checking for return value of vsnprintf()... Yes.
Checking for errno.h... Yes.
Checking for mmap support... Yes.
```


I've reported this issue to the email address zlib at gzip.org and are awaiting feedback.  I don't think it will be easy to progress on this until that point. 

Dave


---

Comment by drkirkby created at 2010-01-28 12:35:22

Changing status from needs_work to needs_info.


---

Comment by jsp created at 2010-02-05 20:51:09

Changing status from needs_info to needs_work.


---

Comment by jsp created at 2010-02-05 20:51:09

I found out the problem is in src/configure. This file is very old!
Has entries for QNX os, remember those days.

This file needs a patch!!!

Jaap


---

Comment by dimpase created at 2020-08-24 18:08:16

Changing status from needs_work to positive_review.


---

Comment by dimpase created at 2020-08-24 18:08:16

this is obsolete.


---

Comment by chapoton created at 2020-09-10 08:01:55

Resolution: invalid
