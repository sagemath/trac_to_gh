# Issue 9160: Singular - change timestamp of file and sort out SAGE64 isssue.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-06-06 13:13:55

Assignee: GeorgSWeber

CC:  wjp leif mpatel alexanderdreyer polybori malb

## The problems

There were three things wrong with the Singular package, the last of which can cause build failures. 

 * The ability to build 64-bit was restricted to the OS X operating system, as the -m64 flag was only added if both SAGE64 was set to "yes" and the operating system was OS X with the following line of code.
 * The package version was unconventional, with people sometimes updating a date, rather than incrementing the patch level as is standard Sage practice - see the developers guide at http://www.sagemath.org/doc/developer/patching_spkgs.html#overview-of-patching-spkg-s 
 * The time stamp of the file `src/Singular/libparse.cc` was one second older than the file it was supposed to be created from ( `src/Singular/libparse.l`), so the build process was trying to use 'flex' to update `src/Singular/libparse.cc`, which fails if flex is not available. 

```
make install in Singular
make[4]: Entering directory `/export/home/drkirkby/32/sage-4.4.3/spkg/build/singular-3-1-0-4-20100214/src/Singular'
sh flexer.sh -I -Pyylp -t libparse.l >libparse.cc.lmp
flexer.sh: flex: not found
flexer.sh: test: argument expected
make[4]: *** [libparse.cc] Error 1 
```

 See http://groups.google.co.uk/group/sage-devel/browse_thread/thread/fbf5b7f781c3f523?hl=en for a discussion of this. 

 == The solutions ==
Three very minor changes are made. 
 * The following


```
   if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
```


 was changed to 


```
   if [ "x$SAGE64" = xyes ]; then
```


 to enable 64-bit builds on any platform when SAGE64 is set to "yes".

 * The time stamp of the file `src/Singular/libparse.cc` made the current time with:

```
touch src/Singular/libparse.cc
}}} 

 * The package name was set in according with the Sage Developers Guide. Had this been done properly, it would be patch level 6, so the package was named singular-3.1.0.4.p6. 

 == Why a blocker ? ==
The incorrect time stamp has caused build failures on Solaris and could cause them on other platforms too.


---

Comment by drkirkby created at 2010-06-06 13:16:58

Mercurial patch which resolves all 3 problems


---

Comment by drkirkby created at 2010-06-06 13:33:51

Changing status from new to needs_review.


---

Attachment

An updated .spkg may be found here

http://boxen.math.washington.edu/home/kirkby/patches/singular-3.1.0.4.p6.spkg

Dave


---

Comment by leif created at 2010-06-06 19:32:03

Funny, on Linux the Singular (sub-)packages are configured with `--without-lex --without-bison` (though I have flex and bison, with aliases "lex" and "yacc", installed).
And `install.log` contains

```
configure: warning: building without lex -- make might fail
checking for bison... (cached) bison
```


The patches look ok to me, I'll test them and the new spkg soon - but only on a Linux box...


---

Comment by leif created at 2010-06-06 19:39:39

Nice, too:

```
...
make install in factory
make[4]: Entering directory '/home/leif/sage-4.4.3.rc0/spkg/build/singular-3-1-0-4-20100214/src/factory'
WARNING: You need to rerun autoconf. I am proceeding, for now.
touch configure
./config.status --recheck
running /bin/sh ./configure  --prefix=/home/leif/sage-4.4.3.rc0/local --exec-prefix=/home/leif/sage-4.4.3.rc0/local --bindir=/home/leif/sage-4.4.3.rc0/local/bin --libdir=/home/leif/sage-4.4.3.rc0/local/lib --libexecdir=/home/leif/sage-4.4.3.rc0/local/lib --with-apint=gmp --with-gmp=/home/leif/sage-4.4.3.rc0/local --with-ntl=/home/leif/sage-4.4.3.rc0/local --with-NTL --without-MP --without-lex --without-bison --without-Boost --enable-gmp=/home/leif/sage-4.4.3.rc0/local --enable-Singular --enable-factory --enable-libfac --enable-IntegerProgramming --disable-doc --with-malloc=system --disable-debug --includedir=/home/leif/sage-4.4.3.rc0/local/include --enable-omalloc --with-external-config_h=/home/leif/sage-4.4.3.rc0/spkg/build/singular-3-1-0-4-20100214/src/Singular/omSingularConfig.h --with-track-custom --enable-Plural --with-factory --with-libfac --with-Singular=yes --cache-file=.././config.cache --srcdir=. --no-create --no-recursion
...
```



---

Comment by drkirkby created at 2010-06-06 22:15:36

Replying to [comment:4 leif]:
> Funny, on Linux the Singular (sub-)packages are configured with `--without-lex --without-bison` (though I have flex and bison, with aliases "lex" and "yacc", installed).
> And `install.log` contains
> {{{
> configure: warning: building without lex -- make might fail
> checking for bison... (cached) bison
> }}}
> 
> The patches look ok to me, I'll test them and the new spkg soon - but only on a Linux box...

The more I look at this, the more I think the Singular package as a whole is seriously screwed up. 

You might notice in SPKG.txt my comment that there are 5-copies of `install-sh` in the package. Clearly someone was not short of disk space! 

As you say, Singular is configured with `-without-lex --without-bison`, but there appears to be no such options to the configure script, as 


```
$ configure --help | grep bison
```


produces no output - same with lex. So I suspect those options are doing nothing at all. 

I've tested the new spkg on a Solaris box which *does* have flex in the path. In which case I see:


```
sh flexer.sh -I -Pyylp -t libparse.l >libparse.cc.lmp
cp libparse.cc.lmp libparse.cc
```


So the revised package works on Solaris 10 SPARC machines both with and without flex in the path. The two machines are:

 * Sun Blade 1000, Solaris 10 03/2005 (the first release of Solaris 10), 2 GB RAM, dual 900 MHz UltraSPARC III+ 64-bit processors, *with flex* in the path.
 * Sun Blade 2000, Solaris 10 10/2009 (the latest update of Solaris 10), 8 GB RAM, dual 1.2 GHz UltraSPARC III+ 64-bit processors, *without flex* in the path.

Hardware wise these machines are quite similar (the motherboards are interchangeable), but one has the oldest and one the latest release of Solaris 10. So I think this is a fair test that the changes are a reasonable hack to get a *very* poor package to work.

I've just downloaded the latest source code (3.1.1) and discovered the Singular code still looks a complete mess 
 * Multiple copies of install-sh etc
 * ` make distclean` clears nothing useful. 
 * ` make check` or ` make test` has no test procedures. 
 * ...etc etc. 

So updating it unlikely to be very productive - just give us another set of problems to resolve. 
(It makes me wonder how much I could trust the results from such code). 

Dave


---

Comment by leif created at 2010-06-07 18:09:25

Replying to [comment:6 drkirkby]:
> I've just downloaded the latest source code (3.1.1) and discovered the Singular code still looks a complete mess 
>  * Multiple copies of install-sh etc
>  * ` make distclean` clears nothing useful. 
>  * ` make check` or ` make test` has no test procedures. 
>  * ...etc etc. 
> 
> So updating it unlikely to be very productive - just give us another set of problems to resolve. 

I think further improvements to the Singular package should be made on another ticket (cf. sage-devel thread ["Is flex needed to build Sage"](http://groups.google.com/group/sage-devel/browse_thread/thread/fbf5b7f781c3f523#)).

Built Sage 4.4.3 with the updated spkg from scratch on a 32-bit Linux; all doctests passed (see sage-release).
I though have some minor changes to `SPKG.txt` (typo) and `spkg-install` I'll upload later (i.e. I haven't prepared a patch yet).

After passing other sanity checks I've not yet done I'll give it a positive review; 4.4.4.alpha0 is out now though, but I hope it will make it into alpha1.

-Leif


---

Comment by leif created at 2010-06-08 00:15:02

Replying to [comment:5 leif]:
> Nice, too:

```
...
make install in factory
make[4]: Entering directory '/home/leif/sage-4.4.3.rc0/spkg/build/singular-3-1-0-4-20100214/src/factory'
WARNING: You need to rerun autoconf. I am proceeding, for now.
touch configure
./config.status --recheck
...
```



```
-rwxr-x--- 1 leif leif  86183 2008-08-20 14:52:31.000000000 +0200 ./src/factory/configure
-rw-r----- 1 leif leif  13990 2008-08-20 14:52:32.000000000 +0200 ./src/factory/configure.in
```

Moreover:

```
-rw-r----- 1 leif leif 112167 2008-11-12 13:51:53.000000000 +0100 ./src/Singular/grammar.cc
-rw-r----- 1 leif leif   2673 2008-03-19 18:51:43.000000000 +0100 ./src/Singular/grammar.h
-rw-r----- 1 leif leif  44955 2009-02-27 18:25:22.000000000 +0100 ./src/Singular/grammar.y
```

(In addition to `libparse.l` which is newer than `libparse.cc` by only _one second_.)


---

Comment by drkirkby created at 2010-06-08 00:33:27

Replying to [comment:7 leif]:

> After passing other sanity checks I've not yet done I'll give it a positive review; 4.4.4.alpha0 is out now though, but I hope it will make it into alpha1.
> 
> -Leif

I could remake it and touch 'factory/configure' but this does not seem be causing any build problems. As you remarked above, other issues with this package need another ticket. 

I get the feeling this release is going to be made quite soon. See Mike Hansen's comment when he announced the alpha0.

_Sage 4.4.4.alpha0 has been released.  With the exception of a few more patches, I think this should be pretty close to final._

so I'd rather not try to solve too much in this Singular package, and let the ticket drag on. You know I feel the complete package needs work. 

Dave


---

Comment by leif created at 2010-06-08 01:25:21

Replying to [comment:9 drkirkby]:
> I could remake it and touch 'factory/configure' but this does not seem be causing any build problems.

*Yes*, just to avoid the annoying message (as mentioned, it actually differs only by one second).

We should get another dumb message if bison is not installed (in contrast to flex, where `--without-lex` in fact only triggers "... make _might_ fail").

> As you remarked above, other issues with this package need another ticket. 
> 
> I get the feeling this release is going to be made quite soon. See Mike Hansen's comment when he announced the alpha0.

:-)
 
> _Sage 4.4.4.alpha0 has been released.  With the exception of a few more patches, I think this should be pretty close to final._

A few more...

I'll try to hurry.

Btw, in `spkg-install`: `s/create create/create/` (the typo I mentioned, *not* in `SPKG.txt`)


---

Comment by leif created at 2010-06-08 01:42:33

And you can substitute

```
  if [ "x$SAGE64" = xyes ]; then
    echo "64-bit of Singular"
    CFLAGS="-O2 -g -m64 "; export CFLAGS
    CXXFLAGS="-O2 -g -m64"; export CXXFLAGS
    CPPFLAGS="-O2 -g -m64"; export CPPFLAGS
    LDFLAGS="-m64 "; export LDFLAGS
    DYNAMIC_KERNEL="--without-dynamic-kernel"; export DYNAMIC_KERNEL
  fi
```

by

```
  if [ "x$SAGE64" = xyes ]; then
    echo "64-bit build of Singular"
    CFLAGS="-O2 -g -m64"
    CXXFLAGS="-O2 -g -m64"
    CPPFLAGS="-O2 -g -m64"
    LDFLAGS="-m64"; export LDFLAGS
    DYNAMIC_KERNEL="--without-dynamic-kernel"; export DYNAMIC_KERNEL
  fi
```

(Add _"build"_ or change it to _"Building 64-bit version of..."_; I dont think 64 bits of Singular would be enough. The other flags are already exported a few lines below.)


---

Comment by leif created at 2010-06-08 01:58:04

Actually by:

```
  if [ "x$SAGE64" = xyes ]; then
    echo "64-bit build of Singular"
    CFLAGS="-O2 -g -m64"
    CXXFLAGS="-O2 -g -m64"
    CPPFLAGS="-O2 -g -m64"
    LDFLAGS="-m64"; export LDFLAGS
    if [ `uname` = "Darwin" ]; then
      DYNAMIC_KERNEL="--without-dynamic-kernel"; export DYNAMIC_KERNEL
    fi
  fi
```


Then I'll give it a positive review... :)


---

Comment by drkirkby created at 2010-06-08 13:50:53

OK, I've made some changes. I hope these are ok with you. 

 * Changed the timestamp on the configure script with 'touch'
 * Moved all the 'export' commands to one place - it seemed a bit pointless exporting LDFLAGS and DYNAMIC_KERNEL from inside the SAGE64 code, whereas others were exported multiple times on other lines. Now all variables are exported once, and only once and done in one place. 
 * Changed $RM to 'rm', $CHMOD to 'chmod' etc. I've done quite a few of these in the past, as it makes the code easier to read. 
 * The 'SAGE64' test was actually inside an 'else' part of `if [ $SAGE_DEBUG = 1 ] ; then ` bit of code, so would have not been executed had someone set SAGE_DEBUG to 1. As such it would have been impossible to debug the code in 64-bit mode on systems where SAGE64 needed to be set. The SAGE64 test is now done irrespective of whether debugging or not. 
 * Ensured $SAGE_LOCAL/include is the first CPPFLAG, so the Sage include files are loaded before others. A failure to do this was causing some old headers on Solaris to be included, instead of the newer ones in Sage. (The same is happening with mathplotlib I believe)
 * Removed "-O2 -g -m64" from CPPFLAGS, as these should not be passed to the pre-processor, but the compiler. They should go into CFLAGS and CXXFLAGS, not CPPFLAGS. 
 * I did *not* change DYNAMIC_KERNEL to be only used on OS X (Darwin), as the Singular documentation specifically says this should be used on Solaris. 

I've tested on Solaris 32-bit (SPARC) on several systems, Linux and OS X - all work fine. It does not work fully on OpenSolaris x64, as the CFLAGS and CXXFLAGS are not getting passed every time the compiler is invoked - there are about 6 cases where the flag does not get passed. This needs to be resolved at a later date. 

Hopefully the package is a bit cleaner now. It's still a mess, but it's a start to a cleaner build system. 

The updated package is in the original place - http://boxen.math.washington.edu/home/kirkby/patches/singular-3.1.0.4.p6.spkg An updated patch file is attached to the ticket.

Test results are below for one Solaris system, one Linux system and one OS X system. 

Dave 

 == On bsd.math (OS X) ==

```
Successfully installed singular-3.1.0.4.p6
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing singular-3.1.0.4.p6.spkg
[kirkby`@`bsd sage-4.4.2]$ uname -a 
Darwin bsd.local 10.3.0 Darwin Kernel Version 10.3.0: Fri Feb 26 11:58:09 PST 2010; root:xnu-1504.3.12~1/RELEASE_I386 i386 i386 MacPro1,
1 Darwin
[kirkby`@`bsd sage-4.4.2]$ 
```


 == On sage.math (Linux) ==

```
Successfully installed singular-3.1.0.4.p6
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing singular-3.1.0.4.p6.spkg
kirkby`@`sage:~/sage-4.4.2$ uname -a
Linux sage.math.washington.edu 2.6.24-26-server #1 SMP Tue Dec 1 18:26:43 UTC 2009 x86_64 GNU/Linux
```


 == On t2.math (Solaris 10 on SPARC) ==

```
sys     4m38.647s
Successfully installed singular-3.1.0.4.p6
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/rootpool2/local/kirkby/sage-4.4.3/spkg/build/singular-3.1.0.4.p6
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing singular-3.1.0.4.p6.spkg
```



---

Comment by leif created at 2010-06-08 21:45:16

The more I look at it, the more things don't make sense to me... :(

I would have been happy if you only fixed the _"Solaris doesn't work with dynamic kernel"_ issue, but see below...

Replying to [comment:13 drkirkby]:
> OK, I've made some changes. I hope these are ok with you.
> 
 
> * Changed the timestamp on the configure script with 'touch'

Ok. (The comment in `SPKG.txt` though mentions `factory/configure`, not `src/factory/configure`.)


>  * Moved all the 'export' commands to one place - it seemed a bit pointless exporting LDFLAGS and DYNAMIC_KERNEL from inside the SAGE64 code, whereas others were exported multiple times on other lines. Now all variables are exported once, and only once and done in one place.

I do not really agree.
 * `DYNAMIC_KERNEL` is *only* used in `spkg-install`, so we actually *don't* have to *export it at all*.
 * There is a difference between _exporting empty_ variables and _not exporting_ them, so in general variables should only be exported when necessary.
 

>  * Changed $RM to 'rm', $CHMOD to 'chmod' etc. I've done quite a few of these in the past, as it makes the code easier to read.

I don't agree either. This inhibits redefining them on ill or ill-configured systems. (Nor can I see it being easier to read.) They are all defined in `sage-env` (if not overridden by the user), so we can rely on them.


>  * The 'SAGE64' test was actually inside an 'else' part of `if [ $SAGE_DEBUG = 1 ] ; then ` bit of code, so would have not been executed had someone set SAGE_DEBUG to 1. As such it would have been impossible to debug the code in 64-bit mode on systems where SAGE64 needed to be set. The SAGE64 test is now done irrespective of whether debugging or not.

Ok, though `SAGE_DEBUG` is set to zero in the same file.


>  * Ensured $SAGE_LOCAL/include is the first CPPFLAG, so the Sage include files are loaded before others. A failure to do this was causing some old headers on Solaris to be included, instead of the newer ones in Sage. (The same is happening with mathplotlib I believe)

Ok. (This should usually be achievable by some `configure` option.)


>  * Removed "-O2 -g -m64" from CPPFLAGS, as these should not be passed to the pre-processor, but the compiler. They should go into CFLAGS and CXXFLAGS, not CPPFLAGS.

In general, at least `-m64` *is required* for the preprocessor, too (optimization flags etc. _might_ as well be used by it).


>  * I did *not* change DYNAMIC_KERNEL to be only used on OS X (Darwin), as the Singular documentation specifically says this should be used on Solaris.

Well, setting it for Darwin was already redundant, so Solaris actually does *not* need it either (and remember it previously worked on e.g. t2.math):

```
# disable the dynamic kernel, except on Linux
if [ "$UNAME" = "Linux" ]; then
     DYNAMIC_KERNEL=""
else
     DYNAMIC_KERNEL="--without-dynamic-kernel"
fi
```

(This otherwise shouldn't depend on `SAGE64`, because it is not directly related.)
Perhaps we should add a comment to `SPKG.txt` that it is currently disabled on *all* systems but Linux, which especially includes MacOS/Darwin and Solaris.


> I've tested on Solaris 32-bit (SPARC) on several systems, Linux and OS X - all work fine. It does not work fully on OpenSolaris x64, as the CFLAGS and CXXFLAGS are not getting passed every time the compiler is invoked - there are about 6 cases where the flag does not get passed. This needs to be resolved at a later date. 
> 
> Hopefully the package is a bit cleaner now. It's still a mess, but it's a start to a cleaner build system. 

> The updated package is in the original place - http://boxen.math.washington.edu/home/kirkby/patches/singular-3.1.0.4.p6.spkg An updated patch file is attached to the ticket.

The second (newer) commit message isn't that nice:

```
changeset:   93:6d0fd18da77b
tag:         tip
user:        kirkby`@`localhost
date:        Tue Jun 08 06:18:30 2010 -0700
summary:     #9160 Singular - change timestamp of file and sort out SAGE64 isssue.

changeset:   92:342850f8fd31
user:        David Kirkby <david.kirkby`@`onetel.net>
date:        Sun Jun 06 14:15:05 2010 +0100
summary:     #9160 Singular - change timestamp of file and sort out SAGE64 isssue.
```


Thanks for all the testing, looking forward to getting rid of this ticket... ;-)

-Leif


---

Comment by leif created at 2010-06-08 22:05:14

Just for the record: ["Ticket #3158 (closed defect: fixed) singular-3-0-4-2-20080405.p1 requires flex"](http://trac.sagemath.org/sage_trac/ticket/3158) :-)


---

Comment by drkirkby created at 2010-06-08 23:26:17

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-06-08 23:26:17

Thanks for all your comments. I'm just in the process of testing this, should be ready in under an hour.


---

Comment by drkirkby created at 2010-06-08 23:44:01

Part 2 of patch - much less changes than previous version.


---

Comment by drkirkby created at 2010-06-09 00:04:59

Changing status from needs_work to needs_review.


---

Attachment

I went back to the first version, and made a few minor changes from that. So forget the version you did not like. I've overwritten the patch file. 

 * Removed the code specific to DYNAMIC_KERNEL on OS X, since as you say, it had already been disabled on all platforms except Linux. 
 * set CPPFLAGS="-I$SAGE_LOCAL/include $CPPFLAGS" (All flags like -m64, -g etc are still there. I've not removed them, though I'm not convinced they are needed myself). 
 * Added required sections to SPKG.txt according to Developers guide. I filled in what I could  - only "PKG Maintainers" is empty. 
 * Documented in the new "Special Update/Build Instructions" section about Solaris and the use of --without-dynamic-kernel option and CONFIG_SHELL. No changes have been made to CONFIG_SHELL or --without-dynamic-kernel. 
 * touched src/factory/configure 
 * moved SAGE64 stuff outside the debugging section. Even though as you say SAGE_DEBUG is set to zero, it still seems illogical to have it in that section, as if someone wanted to chage SAGE_DEBUG, they would disable the possibility of building 64-bit, which would seem rather stupid. 
 * I realised too late my email was not in the commit message, but I don't think that should be a major problem. The subject line is more informative 

```
changeset:   93:0283ade6e1ad
tag:         tip
user:        kirkby`@`localhost
date:        Tue Jun 08 16:34:56 2010 -0700
summary:     #9160. Few code changes, mainly releated to the dynamic kernel, and improved documentation
```


Package is still at http://boxen.math.washington.edu/home/kirkby/patches/singular-3.1.0.4.p6.spkg

The two patches on the ticket need to be applied. 

Dave


---

Comment by drkirkby created at 2010-06-09 00:09:51

Just to clarify, the patches on the ticket do not need to be applied to the package at http://boxen.math.washington.edu/home/kirkby/patches/singular-3.1.0.4.p6.spkg - that package has both patches applied. My wording before may have been ambiguous


---

Comment by leif created at 2010-06-09 00:27:26

Ah thanks, I just was wondering you unapplied the patches...

At first glance looks very good to me.

(Only the _"create create"_ got back in, and as you noticed, there's 
`kirkby`@`localhost` in the commit message. Never mind.)

Now taking a final look at the new spkg...

-Leif

P.S.: `-m32`/`-m64` has a major effect on many preprocessor definitions (e.g. `__i386__` vs. `__x86_64__`, and the whole stuff in `stdint.h` etc., i.e. `SIZEOF_LONG` and the like.).


---

Comment by leif created at 2010-06-09 00:45:01

Oh, and I forgot:

If ever somebody again works on this package, the discrepancy between the bison source file `grammar.y` and the currently _much_ older files generated from it -- I suspect from a previous version -- (`grammar.cc` and `grammar.h`, all in `src/Singular`) should be inspected.


```
/****************************************
*  Computer Algebra System SINGULAR     *
****************************************/
/* $Id: grammar.y,v 1.129 2009/02/27 17:25:22 Singular Exp $ */
/*
* ABSTRACT: SINGULAR shell grammatik
*/
```


```
-rw-r----- 1 leif leif 112167 2008-11-12 13:51:53.000000000 +0100 src/Singular/grammar.cc
-rw-r----- 1 leif leif   2673 2008-03-19 18:51:43.000000000 +0100 src/Singular/grammar.h
-rw-r----- 1 leif leif  44955 2009-02-27 18:25:22.000000000 +0100 src/Singular/grammar.y
```


Perhaps worth another note in `SPKG.txt`.


---

Comment by drkirkby created at 2010-06-09 01:03:24

Hi, 
it's 1:56 am here, so I am going to bed. If you want to add a reviewer patch to make that comment in SPKG.txt, feel free. Otherwise I'll address it if  you feel its necessary. Personally, the whole package is such a mess, it would seem a thankless task listing what is wrong with it. 

Nice one you finding the _fixed_ #3158. Not a very good fix! I've not looked at the ticket, but I assume it was perhaps fixed and someone removed the code - it is too late here now for me to bother to look. 

I never thought about what -m64 would do to the preprocessor and sizeof(long). I can see you have a point there. They say one  learns something every day. 


Dave


---

Comment by leif created at 2010-06-09 02:47:11


```
Successfully installed singular-3.1.0.4.p6
You can safely delete the temporary build directory
/home/leif/sage-4.4.4.alpha0/spkg/build/singular-3.1.0.4.p6
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing singular-3.1.0.4.p6.spkg
leif`@`californication:~/sage-4.4.4.alpha0$ uname -a
Linux californication 2.6.28-19-generic #61-Ubuntu SMP Wed May 26 23:35:15 UTC 2010 i686 GNU/Linux
leif`@`californication:~/sage-4.4.4.alpha0$ ./sage -t -long devel/sage/sage/libs/singular/
sage -t -long "devel/sage/sage/libs/singular/singular-cdefs.pxi"
	 [4.3 s]
sage -t -long "devel/sage/sage/libs/singular/__init__.py"   
	 [0.2 s]
sage -t -long "devel/sage/sage/libs/singular/function.pyx"  
	 [6.6 s]
sage -t -long "devel/sage/sage/libs/singular/ring.pyx"      
	 [4.9 s]
sage -t -long "devel/sage/sage/libs/singular/function_factory.py"
	 [4.3 s]
sage -t -long "devel/sage/sage/libs/singular/groebner_strategy.pyx"
	 [4.5 s]
sage -t -long "devel/sage/sage/libs/singular/singular.pxi"  
	 [0.2 s]
sage -t -long "devel/sage/sage/libs/singular/option.pyx"    
	 [4.9 s]
sage -t -long "devel/sage/sage/libs/singular/polynomial.pyx"
	 [4.4 s]
sage -t -long "devel/sage/sage/libs/singular/singular.pyx"  
	 [4.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 39.2 seconds
```

(Ubuntu 9.04 32-bit/Pentium4, new spkg installed on Sage 4.4.4.alpha0)

I'm currently too tired to upload a reviewer patch adding more comments to `SPKG.txt` and perhaps `spkg-install`; it should perhaps also contain a link to the sage-devel thread ["Is flex needed to build Sage?"](http://groups.google.com/group/sage-devel/browse_thread/thread/fbf5b7f781c3f523#) which has further suggestions.

We could also update the ticket description to briefly reflect the outcome.

----

> [...] A huge amount of effort has gone into Singular, and I greatly
> appreciate that it is open source.  I think the Sage project has a
> very good relationship with the Singular project, and I hope criticism
> of the quality of their work will be constructive and not offensive.
> [...]

> 

> It would be cool if some the ideas you guys have could be added to

> http://wiki.sagemath.org/days23.5 

> which is the joint Sage/Singular meeting this summer.

> 

> -- William
(from the sage-devel thread)


---

Comment by leif created at 2010-06-09 02:47:11

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-06-09 03:46:22

Meanwhile, there's a new Singular package (p7; two simple patches to `SPKG.txt` and `spkg-install`) at http://trac.sagemath.org/sage_trac/ticket/9185#comment:2

[comment:ticket:9185:2 mpatel]:
> I've put a new spkg at
> 
>  * http://sage.math.washington.edu/home/mpatel/trac/9185/singular-3.1.0.4.p7.spkg
> 
> It's based on the package mentioned in [comment:ticket:9160:18 this comment] at #9160.  If there are more changes at that ticket, I can reapply the patch above and make a new spkg.

I.e., the package there is currently up-to-date, based on our latest p6.

And here is a shortcut to the [simple patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9185/trac_9185-singular_makeflags.patch).


---

Comment by mhansen created at 2010-06-09 06:35:22

I've checked and this works on Cygwin as well.


---

Comment by mhansen created at 2010-06-09 06:35:22

Resolution: fixed


---

Attachment

Remove the rebuilding of factory and libfac from spkg-install


---

Comment by fbissey created at 2010-06-12 09:41:54

After all the discussion we had on the mailing list about factory and libfac
I am suggesting the above patch for inclusion.


---

Comment by fbissey created at 2010-06-12 09:50:21

Sorry didn't notice the ticket was closed will open another ticket for this shortly.


---

Comment by AlexanderDreyer created at 2010-08-16 22:07:14

Reported upstream: http://www.singular.uni-kl.de:8002/trac/ticket/252


---

Comment by AlexanderDreyer created at 2010-08-22 21:06:49

While creating the tar file of the sources (from svn), touch Singular/grammar.cc and Singular/scanner.cc will be done.
