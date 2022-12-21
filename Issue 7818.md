# Issue 7818: Update sage-env

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-02 11:35:05

Assignee: drkirkby

CC:  was jsp

This is an update to the sage-env file. It should allow a much improved build process, simplifying the code in spkg install files, as much of it will be taken care of. The code will also be more portable. 

 * Little or no need for any SAGE64 rubbish in any spkg-install files. The appropriate flag to build 64-bit code is added if SAGE64 is set to use. 
 * No need to add -Wall or -g, as these are added by default. 
 * GNU specific compiler options can be replaced by variables with similar names to the GNU ones, making substitution a relatively easy task. 
 * Will enable code to be much more portable. 

The changes mainly affect the 3 variables for compiler flags  - CFLAGS, CXXFLAGS and FCFLAGS.  

The user may set CFLAGS, CXXFLAGS and FCFLAGS, but the following will be appended. 

 == General flags ==
 * The -g  option is added to enable debugging unless SAGE_DEBUG is set to "no". 
 * -Wall is added for gcc, g++ and gfortran.

 == 64-bit Flags ==
If SAGE64 is "yes"
 * -m64 is added for GCC
 * -m64 is added for Sun Studio
 * -q64 is added for IBM's compiler on AIX
 * +DA2.OW is added on HP-UX. (This will not work on Itanium processors running on HP-UX. I'll update when I have more information). 
 
A variable CFLAG64 is set to the correct option for building 64-bit binaries with the C compiler. So if -m64 is replaced by $CFLAG64, the code will work on any C compiler. 

(Some compilers may require a different option for C and C++ files. The names CXXFLAG64 and FCFLAG64 are reserved for this, but its not suggested they are used now) 

 == C++ library flags ==
Due to changes in the C++ standard, it is impossible for compiler vendors to distribute a C++ runtime library which is both compatible with the old standard and the new one. Both HP and Sun use the older library by default, and need a switch added to enable the newer libraries, which more closely follow the latest C++ standard. See:

http://developers.sun.com/solaris/articles/cmp_stlport_libCstd.html

http://docs.hp.com/en/14487/faq.htm


Therefore
 * If the compiler is Sun Studio, library=stlport4 is added to CXXFLAGS. 
 * If the Compiler is HP's on HP-UX, the option -AA is added to CXXFLAGS. 

 == Shared Library Flags ==
Five new variables are set in sage-env. These are for building shared libraries and take on names very similar to the GNU names for the flags. 

|           |                |                       |
|-----------|----------------|-----------------------|
|*Flag name*|*Value with GCC*|*Value with Sun Studio*|
|FPIC_FLAG|-fPIC|-xcode=pic32|
|SHARED_FLAG|-shared|-G|
|SONAME_FLAG|-soname|-h|
A reviewer may notice two further variable names used. These options can be linker dependent and will be finalized once some code to detect the linker is in place.


---

Comment by drkirkby created at 2010-01-02 11:37:10

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-02 23:14:11

Just to make the point, -m64 in sage should *not* need to be replaced by 'CLFAG64' in general. In 99% of cases, simply removing all the -m64's that litter Sage will do the trick, as the right option will be added automatically. 

In some cases, it may be necessary to keep such a flag on linking. In those rare cases (ECL is the only example I can think of), then use CFLAG64 instead of -m64. But this will allow 99% of the -m64's to be removed and forgotten about, as they will be added only where necessary.


---

Comment by drkirkby created at 2010-01-02 23:17:10

Oopsn, I mean in rare cases, -m64 might need to be replaced by $CFLAG64.


---

Comment by jhpalmieri created at 2010-01-05 22:59:47

Should line 87 be changed from

```
echo "NAME_OF_ENVIROMENT_VARIABLE value_of_environment_variable"
```

to

```
echo "NAME_OF_ENVIROMENT_VARIABLE=value_of_environment_variable"
```

(adding an equals sign)?

In line 380:

```
# often. I think ECL might need it, to just the option, not
```

change "to" to "so", I think.

As far as a careful review goes, I'm not enough of an expert in the Sage build process to do that.  An expert should take a good look at this.


---

Comment by drkirkby created at 2010-01-05 23:16:35

Thank you for the feedback. I'll make the couple o changes you suggest. I take your point about needing an expert of the build process. William and I wrote this many years ago, but its changed a lot since then. 

If you have some spare time, (and I know building Sage can take some time), could you try a build with the sage-env script? First unpack the sources, then exchange spkg/base/sage-env for this one before trying a build. The build should proceed as normal. You might notice an extra -Wall or -g flag here or there, but there should be no huge changes. 

What it will give is a bunch of variables that can at a later date be used inside files like spkg-install. 

Dave


---

Comment by jhpalmieri created at 2010-01-05 23:26:16

Replying to [comment:6 drkirkby]:
> Thank you for the feedback. I'll make the couple o changes you suggest. I take your point about needing an expert of the build process. William and I wrote this many years ago, but its changed a lot since then. 

One more question: should this also be included in sage-scripts?  That is, should the file `SAGE_ROOT/spkg/base/sage-env` be the same as `SAGE_ROOT/local/bin/sage-env`?  If so, please produce a patch for the scripts repository.
 
> If you have some spare time, (and I know building Sage can take some time), could you try a build with the sage-env script? First unpack the sources, then exchange spkg/base/sage-env for this one before trying a build. The build should proceed as normal. You might notice an extra -Wall or -g flag here or there, but there should be no huge changes. 

Sure, I'll start that right now.


---

Comment by jhpalmieri created at 2010-01-06 18:08:49

It built just fine on my OS X 10.6 machine.  I'm trying on sage.math now (or boxen.math or whatever it is these days).

In case you missed my earlier question:

> should this also be included in sage-scripts? That is, should the file SAGE_ROOT/spkg/base/sage-env be the same as SAGE_ROOT/local/bin/sage-env? If so, please produce a patch for the scripts repository.


---

Comment by drkirkby created at 2010-01-06 19:14:22

Note, there are still some occurrences of ;-a' and '-o' here. I tried not too change too much of the original file, to make the review somewhat easier. So some things I don't feel are perfect,   I have left unchanged. They almost certainly make no difference whatsoever here, but its a good habbit to write scripts in such a way they work reliably, irrespective of what shell someone happens to use. 

Dave


---

Comment by jhpalmieri created at 2010-01-06 20:40:28

The patch applies cleanly to the scripts repository and produces the correct file (that is, SAGE_LOCAL/bin/sage-env and spkg/base/sage-env are the same).  For some reason, the one in local/bin wasn't executable, so I had to fix that manually.

Building with the new sage-env works just fine on sage.math, by the way.


---

Comment by drkirkby created at 2010-01-06 22:20:01

Replying to [comment:12 jhpalmieri]:
> The patch applies cleanly to the scripts repository and produces the correct file (that is, SAGE_LOCAL/bin/sage-env and spkg/base/sage-env are the same).  For some reason, the one in local/bin wasn't executable, so I had to fix that manually.
> 
> Building with the new sage-env works just fine on sage.math, by the way.

It's good to hear it builds fine. I don't envisage anything that it does should screw up the build. It will mean in some packages there will be two -m64's on the command line, but they are harmless. Then hopefully we can remove all the SAGE64 stuff from the files. 

I just re-checked the permissions on the file when I created the ticket and they were executable. I don't know if there was anything I should have done which I did not. 

```
drkirkby`@`hawk:~/sage-4.3.1.alpha1/spkg/standard/sage_scripts-4.3.1.alpha1$ ls -l sage-env
-rwxr-xr-x   1 drkirkby staff      20018 Jan  6 18:53 sage-env
```


Dave


---

Comment by jsp created at 2010-01-07 14:26:56

For historical reasons I suggest you keep the 2005 date in the file!

And maybe stupid where can I find the file testcc.sh?



```
Warning: Attempted to overwrite SAGE_ROOT environment variable
Building Sage on Solaris in 64-bit mode
Creating SAGE_LOCAL/lib/sage-64.txt since it does not exist
Detected SAGE64 flag
Building Sage on Solaris in 64-bit mode
/export/home/jaap/Downloads/sage-4.3/local/bin/sage-env: line 253: /export/home/jaap/Downloads/sage-4.3/local/bin/testcc.sh: No such file or directory
/export/home/jaap/Downloads/sage-4.3/local/bin/sage-env: line 267: /export/home/jaap/Downloads/sage-4.3/local/bin/testcc.sh: No such file or directory
/export/home/jaap/Downloads/sage-4.3/local/bin/sage-env: line 289: /export/home/jaap/Downloads/sage-4.3/local/bin/testcc.sh: No such file or directory
/export/home/jaap/Downloads/sage-4.3/local/bin/sage-env: line 306: /export/home/jaap/Downloads/sage-4.3/local/bin/testcc.sh: No such file or directory
/export/home/jaap/Downloads/sage-4.3/local/bin/sage-env: line 319: /export/home/jaap/Downloads/sage-4.3/local/bin/testcc.sh: No such file or directory
/export/home/jaap/Downloads/sage-4.3/local/bin/sage-env: line 332: /export/home/jaap/Downloads/sage-4.3/local/bin/testcc.sh: No such file or directory



```



Jaap


---

Comment by jsp created at 2010-01-07 15:27:39

Ok, found the testcc.sh and testcxx.sh

This new sage-env does a great job. On my Open Solaris in VirtualBox I could add 
to the spkg/installed after a make -k



```
jaap`@`opensolaris:~/Downloads/sage-4.3$ ls -lt spkg/installed/
total 61
-rw-r--r-- 1 jaap staff 219 2010-01-07 15:59 pil-1.1.6.p2
-rw-r--r-- 1 jaap staff 226 2010-01-07 15:58 flintqs-20070817.p4
-rw-r--r-- 1 jaap staff 218 2010-01-07 15:57 cddlib-094f
-rw-r--r-- 1 jaap staff 229 2010-01-07 15:56 genus2reduction-0.3.p5
-rw-r--r-- 1 jaap staff 222 2010-01-07 15:55 boehm_gc-7.1.p2
-rw-r--r-- 1 jaap staff 227 2010-01-07 15:55 pyprocessing-0.52.p0
-rw-r--r-- 1 jaap staff 225 2010-01-07 15:54 ratpoints-2.1.2.p3
-rw-r--r-- 1 jaap staff 226 2010-01-07 15:54 libm4ri-20091120.p0
-rw-r--r-- 1 jaap staff 226 2010-01-07 15:54 rubiks-20070912.p10
-rw-r--r-- 1 jaap staff 225 2010-01-07 15:53 libfplll-3.0.12.p0
-rw-r--r-- 1 jaap staff 221 2010-01-07 15:51 zodb3-3.7.0.p2
-rw-r--r-- 1 jaap staff 224 2010-01-07 15:50 pycrypto-2.0.1.p4
-rw-r--r-- 1 jaap staff 220 2010-01-07 15:50 mpfr-2.4.1.p0
-rw-r--r-- 1 jaap staff 223 2010-01-07 15:49 givaro-3.2.13rc2
-rw-r--r-- 1 jaap staff 220 2010-01-07 15:48 iml-1.0.1.p11
-rw-r--r-- 1 jaap staff   0 2010-01-07 15:46 eclib-20080310.p7
-rw-r--r-- 1 jaap staff 223 2010-01-04 17:38 twisted-8.2.0.p2
-rw-r--r-- 1 jaap staff 224 2010-01-03 21:51 eclib-20080310.p8

```


I would give it a positive review, but will wait for the other testers.

Jaap


---

Comment by jsp created at 2010-01-07 20:05:03

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-01-07 20:05:03

Ok, positive review!

Jaap


---

Comment by jhpalmieri created at 2010-01-08 16:12:39

Is $RM defined anywhere now?  Or $LN?  Or $MKDIR?  They still seem to be used by the gap spkg, so I can't figure out why that package installs correctly with this version of sage-env.


---

Comment by drkirkby created at 2010-01-08 18:18:19

Replying to [comment:18 jhpalmieri]:
> Is $RM defined anywhere now?  Or $LN?  Or $MKDIR?  They still seem to be used by the gap spkg, so I can't figure out why that package installs correctly with this version of sage-env.
I'm not sure if Or $RM, $LN or $MKDIR are defined elsewhere, or if the bits in gap don't work, but it is not apparent they are not working. But there does seem to be no point in having variables for such basic commands, as agreed here. 

http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot

I left 'cp', as potentially the GNU version of CP has some extra options over some other implementations of CP which might make it useful in some cases, though I'd much prefer any GNUisms were avoided. But there really is no point in having variable for 'ln' or 'mkdir' 

They are all part of POSIX, the 2008 edition of which can be found here

http://www.opengroup.org/onlinepubs/9699919799/

I'm not a great fan of GNU standards and I don't agree with some of it here, but even they agree one can rely on rm, ln and mkdir. 

http://www.gnu.org/prep/standards/standards.html#Utilities-in-Makefiles

I've created a ticket for their removal from 'gap' - see #7873 . I'll fix that very shortly. 

Dave


---

Comment by drkirkby created at 2010-01-08 20:44:20

I fixed any potential gap issue. If someone could review #7873 it would be appreciated. 

Dave


---

Comment by drkirkby created at 2010-01-12 19:00:15

Changing status from positive_review to needs_work.


---

Comment by drkirkby created at 2010-01-12 19:00:15

I'm sticking this to needs work, why I put back definitions such as 


```
if [ "$LN" = "" ]; then
    LN="ln"  && export LN
fi
 
if [ "$MKDIR" = "" ]; then
    MKDIR="mkdir"  && export MKDIR
fi
```


just in case they unsetting these causes any problems in any package. I believe all packages are covered by patches, but if one is not, then this could cause problems. 

Dave


---

Attachment

Updated sage-env, much improved, but added back LN, MKIDR etc, to avoid risk of breakage


---

Comment by drkirkby created at 2010-01-12 19:14:36

Changing status from needs_work to needs_review.


---

Comment by jsp created at 2010-01-13 11:39:50

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-01-13 11:39:50

This changes make sense.



```
[jaap`@`vrede sage-4.3.1.alpha1]$ diff local/bin/sage-env ../sage-env
452a453,456
> if [ "$MV" = "" ]; then
>     MV="mv"  && export MV
> fi
> 
456a461,464
> if [ "$RM" = "" ]; then
>     RM="rm"  && export RM
> fi
>  
460a469,484
> if [ "$LN" = "" ]; then
>     LN="ln"  && export LN
> fi
>  
> if [ "$MKDIR" = "" ]; then
>     MKDIR="mkdir"  && export MKDIR
> fi
>  
> if [ "$CHMOD" = "" ]; then
>     CHMOD="chmod"  && export CHMOD
> fi
>  
> if [ "$TOUCH" = "" ]; then
>     TOUCH="touch"  && export TOUCH
> fi
> 
[jaap`@`vrede sage-4.3.1.alpha1]$ 

```


This will not break any code. I'll test this with reinstalling the affected spkgs mercurial, singular, ntl, gap and pari. 

Ok so far. Positive review.


---

Attachment

Patch file which should hopefully commit, as Robert  Miller said the previous one had a problem.


---

Comment by rlm created at 2010-01-14 01:53:32

Resolution: fixed


---

Comment by rlm created at 2010-01-15 22:31:08

Resolution changed from fixed to 


---

Comment by rlm created at 2010-01-15 22:31:08

Changing status from closed to new.


---

Comment by rlm created at 2010-01-15 22:33:37

Changing status from new to needs_work.


---

Comment by rlm created at 2010-01-15 22:33:37

This patch inadvertently removes the `-fno-strict-aliasing` option from the gcc options that Cython uses to compile the autogenerated C files. This makes all sorts of stuff break all over the place. Also, since that's not obvious from the patch, who knows what else goes wrong? (thanks to Robert Bradshaw for helping me figure this out)


---

Comment by jsp created at 2010-01-15 23:36:11

I'll take my hands off. This is much more trickier than I thought!

Jaap


---

Comment by vbraun created at 2010-01-25 21:38:03

Setting RM="rm" breaks newer libtools, namely the ones in Fedora 12 (libtool 2.2.6, autoconf 2.63, automake 1.11.1). They assume that $RM is either unset or RM="rm -f".

One of the symptoms of this breakage is that configure ends with

```
rm: cannot remove `libtoolT': No such file or directory
```

Compile will break later on...


---

Comment by drkirkby created at 2011-04-02 13:09:41

I think this can be closed as "wontfix" as the issues resolved in this ticket are very complex and I think for the foreseeable future, this will not be resolved.


---

Comment by vbraun created at 2011-04-02 19:34:58

I think we should keep this ticket open and gradually fix spgks. For example the Singular spkg needs to be updated soon for gcc-4.6 so we'll remove any `$RM`s in the process...

Also, is there any other issue except the `-fno-strict-aliasing `? We could fix that...


---

Comment by jdemeyer created at 2013-02-05 19:37:14

Replying to [comment:29 drkirkby]:
> I think this can be closed as "wontfix" as the issues resolved in this ticket are very complex and I think for the foreseeable future, this will not be resolved. 

It is also a typical "fix everything" ticket, which is almost impossible to get merged.


---

Comment by jdemeyer created at 2013-02-05 19:37:14

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-02-08 13:23:32

Resolution: wontfix
