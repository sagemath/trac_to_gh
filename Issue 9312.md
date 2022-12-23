# Issue 9312: Fix GLPK spkg for SAGE64

Issue created by migration from https://trac.sagemath.org/ticket/9312

Original creator: rlm

Original creation time: 2010-06-22 15:39:15

Assignee: tbd

CC:  ncohen mpatel

From the discussion at

http://groups.google.com/group/sage-devel/browse_thread/thread/b9429bcb929cda7

The GLPK spkg ignores the SAGE64 variable.


---

Comment by drkirkby created at 2010-06-22 16:50:06

Is there any way to test this package? There's no spkg-check. 

Whoever put this package together has their own unique style, with each line ending in '&&'. 

I'll try to sort out the SAGE64 stuff. 

Dave


---

Comment by drkirkby created at 2010-06-22 17:18:51

I'm not in a position to check this quickly, as I need to go out soon. It needs a bit of work. But the spkg-install makes little sense to me. 

 * There's no spkg-check to we are once again trusting things work. 
 * I've no idea what all this 'make prefix' is about. 
 * I've no idea why so many lines end in &&
 * Since MV, CP, etc are not universally used, it would seem better to just unset these, rather than try to add -f to them. It just seems to be overly complicating things. 
 
It would be better if the person that put it together looked over some other spkg-install files and the Sage Developers Guide. 


```
if [ "$SAGE_LOCAL" = "" ]; then
   echo "SAGE_LOCAL undefined ... exiting";
   echo "Maybe run 'sage -sh'?"
   exit 1
fi

# The version of libtool in this glpk package requires that
# RM/MV/CP if they are set include the -f option
# See for example the discussion at:
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=523750

: ${CP=cp}; CP="$CP -f"; export CP
: ${MV=mv}; MV="$MV -f"; export MV
: ${RM=rm}; RM="$RM -f"; export RM

cd src &&
LIBS=-ldl ./configure --prefix=$SAGE_LOCAL &&
make prefix=$SAGE_LOCAL &&
make install && 
cd .. && 
python setup.py install &&
echo "********************************************************************************" && 
echo "" &&
echo "    ATTENTION: YOU HAVE TO REBUILD THE SAGE LIBRARY TO GET THIS TO WORK" &&
echo "    exit any running sage instances and call \"sage -b\"" &&
echo "" &&
echo "********************************************************************************"
```



---

Comment by drkirkby created at 2010-06-22 18:02:42

Is there any good reason to use version 4.42, when the latest is 4.44? 

Would it be more sensible if I created a completely fresh package, then some others test that? 

I feel it would be simpler to start this from scratch. 

I'll be travelling later, and will not have access to any SPARC systems, but I can get somewhere with this on my OpenSolaris laptop. 

Dave


---

Comment by drkirkby created at 2010-06-22 18:02:42

Changing status from new to needs_info.


---

Comment by drkirkby created at 2010-06-23 01:35:58

Be aware this is GPL version 3. I was under the impression GPL 3 code was not permitted as standard - only optional or experimental. 

Dave


---

Comment by rlm created at 2010-06-23 03:00:27

Replying to [comment:4 drkirkby]:
> Be aware this is GPL version 3. I was under the impression GPL 3 code was not permitted as standard - only optional or experimental. 
> 
> Dave 

I was under the same impression, but apparently that has changed. I don't think this is relevant here, since this ticket isn't even about making GLPK standard anyway! I'd mention this on sage-devel instead.


---

Comment by drkirkby created at 2010-06-23 18:30:00

Heres a patch. Will post a new package after dinner - wife calling!


---

Attachment

Mercurial patch which fixes the SAGE64 issue and tons more beside


---

Comment by drkirkby created at 2010-06-23 19:49:12

I've updated this package somewhat

http://boxen.math.washington.edu/home/kirkby/patches/glpk-4.44.spkg

to fix what were quite a number of problems with how the package was put together. I've not tested this as a library. Someone more knowledgeable can test this properly. I've only tested it on Solaris and OpenSolaris to see that it builds ok and passes the self-tests in the source code.

I've not changed any of the python stuff, so it should be unchanged. The major change was to disable building of the static libraries, which I doubt Python needs. 

## Changes made

 * Updated to the latest upstream code, version 4.44.
 * Added code to allow a 64-bit build on any platform.
   If SAGE64 is set to "yes", the compiler flag -m64 is added
   by default. That flag works with GCC and SunStudio, but not
   all compilers - IBM's compiler for AIX and HP's for HP-UX
   both use different flags to create a 64-bit build.
   If the compiler does not use -m64 for 64-bit builds, then
   the environment variable CFLAG64 can be set to indicate what
   flag gets added.
 * Added a file spkg-check so the self-test code is built.
   This includes code which will add the appropriate flag
   for 64-bit builds if the test procedures need code to be
   compiled. (Sometimes running 'make test' actually needs
   the compiler flags set properly, so I do it just in case.
   It appears to be unnecessary with this version of GLPK,
   but might with later releases.
 * Added the configure option --with-gmp which will speed up
   processing of large integers (see src/INSTALL)
 * Added the configure option --disable-static since there is
   no need to build static libraries. (see src/INSTALL)
 * Added the configure option --with-zlib. Adding this allows
   GLPK API routines and the stand-alone solver to read and
   write compressed data files performing compression and
   decompression "on the fly" (see src/INSTALL)
 * Removed linking of the 'ld' library in spkg-install, as the
   reason for it being added was not clear.
 * Corrected SPKG.txt to indicate this code is GPL 3.
   (see src/COPYING)
 * Added the ChangeLog section to the SPKG.txt file
 * Added zlib, python and mpir as dependencies in SPKG.txt
 * Checked that the configure script actually does configure
   properly, if not exits.
 * Checked that 'make' does build the code properly, if not exits.
 * Checked that 'make install' does actually install the library
 * Checked that running 'python setup.py install' does actually work.
   If this is not done, code can appear to install properly as it
   passes 'configure', 'make' and 'make install'. So unusually there
   are 4 cases where spkg-install can fail.

 == Desirable changes not made ==
 * There is a "patch" directory which I did not remove, as there is one file referenced there. It should be called "patches" and I believe from discussions on sage-devel it can perhaps be removed. 
 * setup.py has no comments. 
 * setup.py has lots of ../../../.. in directory entires and does not refer to $SAGE_ROOT or $SAGE_LOCAL. Since I'm not a good Python programmer, I've not attempted to fix this. 
As you can see, if SAGE_CHECK is set to "yes", this passes the one self test that there is (pretty dismal IMHO)

## Test system #1 (others MUST test on other hardware and test properly)
 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)
 * SEAGATE-ST3146807FC 2 Gbit/s 15,000 rpm fiber channel disk (FCAL)
 * UFS (not ZFS) local file system.
 * Sage 4.4.4.alpha1
 * GLPK 4.44 source code integrated. 


```
Removing /export/home/drkirkby/sage-4.4.4.alpha1/local/lib/python2.6/site-packages/UNKNOWN-0.0.0-py2.6.egg-info
Writing /export/home/drkirkby/sage-4.4.4.alpha1/local/lib/python2.6/site-packages/UNKNOWN-0.0.0-py2.6.egg-info

real	3m13.451s
user	2m41.607s
sys	0m28.154s
Successfully installed glpk-4.44
Running the test suite.
GLPK will now be tested
Making check in include
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/glpk-4.44/src/include'
make[1]: Nothing to be done for `check'.
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/glpk-4.44/src/include'
Making check in src
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/glpk-4.44/src/src'
make[1]: Nothing to be done for `check'.
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/glpk-4.44/src/src'
Making check in examples
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/glpk-4.44/src/examples'
./glpsol --version
GLPSOL: GLPK LP/MIP Solver, v4.44

Copyright (C) 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
2009, 2010 Andrew Makhorin, Department for Applied Informatics, Moscow
Aviation Institute, Moscow, Russia. All rights reserved.

This program has ABSOLUTELY NO WARRANTY.

This program is free software; you may re-distribute it under the terms
of the GNU General Public License version 3 or later.
./glpsol --mps ./plan.mps
GLPSOL: GLPK LP/MIP Solver, v4.44
Parameter(s) specified in the command line:
 --mps ./plan.mps
Reading problem data from `./plan.mps'...
Problem: PLAN
Objective: VALUE
8 rows, 7 columns, 48 non-zeros
54 records were read
GLPK Simplex Optimizer, v4.44
8 rows, 7 columns, 48 non-zeros
Preprocessing...
7 rows, 7 columns, 41 non-zeros
Scaling...
 A: min|aij| =  1.000e-02  max|aij| =  1.000e+00  ratio =  1.000e+02
GM: min|aij| =  2.534e-01  max|aij| =  3.946e+00  ratio =  1.557e+01
EQ: min|aij| =  6.422e-02  max|aij| =  1.000e+00  ratio =  1.557e+01
Constructing initial basis...
Size of triangular part = 7
      0: obj =   6.500000000e+02  infeas =  3.788e+03 (0)
*     2: obj =   4.376770833e+02  infeas =  0.000e+00 (0)
*    10: obj =   2.962166065e+02  infeas =  0.000e+00 (0)
OPTIMAL SOLUTION FOUND
Time used:   0.0 secs
Memory used: 0.0 Mb (51150 bytes)
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/glpk-4.44/src/examples'
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/glpk-4.44/src'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/glpk-4.44/src'
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/glpk-4.44
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing glpk-4.44.spkg
```



---

Comment by ncohen created at 2010-06-23 20:09:17

Nothing wrong to report on my laptop (debian).

Nathann


---

Comment by drkirkby created at 2010-06-23 20:21:31

Replying to [comment:8 ncohen]:
> Nothing wrong to report on my laptop (debian).
> 
> Nathann
You should put more information than just "Debian laptop". Things like version of Debian, processor, RAM, gcc version etc can all be useful. Note what I put above about my SPARC system. The only really unnecessary info was the disks and file systems, as I'd cut-n-pasted that from a ticket where it was relevant, and forgot to remove it. 

Dave


---

Comment by ncohen created at 2010-06-23 20:24:27

Hmmmm... Do you know how I could get these informations ? :-)

Nathann


---

Comment by drkirkby created at 2010-06-23 20:38:32

Replying to [comment:10 ncohen]:
> Hmmmm... Do you know how I could get these informations ? :-)
> 
> Nathann

Google should come to your rescue.


---

Comment by rlm created at 2010-06-24 17:20:58

Replying to [comment:7 drkirkby]:

## Test system #2
* MacBook
* 2.4 GHz Intel Core 2 Duo
* 2 GB 667 MHz DDR2 SDRAM
* OS X 10.6.3
* Sage 4.4.4.alpha1

Build succeeded and all tests pass.


---

Comment by drkirkby created at 2010-07-03 23:29:44

I'm attaching an *very briefly tested* `spkg/standard/deps` file. It is based on the deps file at #9351, so if this is merged, #9351 can be closed too. 

I've not tried building Sage from scratch using this deps file - just tried that


```
drkirkby@hawk:~/SAGE-4.5.alpha1$ ./sage -f glpk-4.44
Force installing glpk-4.44
Calling sage-spkg on glpk-4.44
Warning: Attempted to overwrite SAGE_ROOT environment variable
Building Sage on Solaris in 64-bit mode
Creating SAGE_LOCAL/lib/sage-64.txt since it does not exist
Detected SAGE64 flag
Building Sage on Solaris in 64-bit mode
glpk-4.44
Machine:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
Deleting directories from past builds of previous/current versions of glpk-4.44
Extracting package /export/home/drkirkby/SAGE-4.5.alpha1/spkg/standard/glpk-4.44.spkg ...
-rw-r--r--   1 drkirkby staff    2937482 Jun 23 20:24 /export/home/drkirkby/SAGE-4.5.alpha1/spkg/standard/glpk-4.44.spkg
glpk-4.44/
glpk-4.44/patch/

<SNIP>

patch/mipGlpk.cpp:857: warning: dereferencing pointer '__pyx_t_3' does break strict-aliasing rules
patch/mipGlpk.cpp:857: warning: dereferencing pointer '__pyx_t_3' does break strict-aliasing rules
patch/mipGlpk.cpp:853: note: initialized from here
creating build/lib.solaris-2.11-i86pc-2.6
creating build/lib.solaris-2.11-i86pc-2.6/sage
creating build/lib.solaris-2.11-i86pc-2.6/sage/numerical
g++ -m64 -shared -L/export/home/drkirkby/SAGE-4.5.alpha1/local/lib -m64 -m64 -I /export/home/drkirkby/SAGE-4.5.alpha1/local/include -m64 build/temp.solaris-2.11-i86pc-2.6/patch/mipGlpk.o -L/export/home/drkirkby/SAGE-4.5.alpha1/local/lib -lcsage -lstdc++ -lglpk -lpython2.6 -o build/lib.solaris-2.11-i86pc-2.6/sage/numerical/mipGlpk.so
running install_lib
copying build/lib.solaris-2.11-i86pc-2.6/sage/numerical/mipGlpk.so -> /export/home/drkirkby/SAGE-4.5.alpha1/local/lib/python2.6/site-packages/sage/numerical
running install_egg_info
Removing /export/home/drkirkby/SAGE-4.5.alpha1/local/lib/python2.6/site-packages/UNKNOWN-0.0.0-py2.6.egg-info
Writing /export/home/drkirkby/SAGE-4.5.alpha1/local/lib/python2.6/site-packages/UNKNOWN-0.0.0-py2.6.egg-info

real	0m13.830s
user	0m9.231s
sys	0m3.341s
Successfully installed glpk-4.44
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/SAGE-4.5.alpha1/spkg/build/glpk-4.44
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing glpk-4.44.spkg
```


worked. 

I've not attached a diff. Not sure if that should be a mercurial one or not. I'll sort that out after I've had some sleep. 

Dave


---

Comment by drkirkby created at 2010-07-04 14:46:25

I've attached a new spkg/standard/deps file (MD5 checksum a49d9c910e8b10148f7aaf025e05cc69), which ensures that 
 * GLPK builds
 * GLPB builds before Sage

I've also attached a unified diff between this and the deps file on #9351. 

However, I am aware of ticket #9274, which rightly points out that the deps file is broken for parallel builds. In particular, almost everything actually depends on 'BASE', but very little is shown to depend on BASE. I have made 'GLPK' depend on 'BASE' here, but really the whole file is broken. 

Unfortunately, #9274 does not have positive review, and I'm unable to give it positive review, so don't feel I should add the dependencies, even though I believe they should be added. (I don't want to over complicate this ticket). Robert may or may not feel differently. I'm happy to go along with either. In fact, I'd rather add BASE as a dependency to everything where I believe it should be. 

Dave


---

Attachment

Untested $SAGE_ROOT/spkg/install file, which adds GLPK


---

Attachment

Untested $SAGE_ROOT/spkg/install file diff file. Relative to to 'install' in sage-4.5.alpha1


---

Comment by drkirkby created at 2010-07-05 17:22:23

I'm going to upload revised versions of 'deps' and 'deps.diff'. This removes the dependency of GLPK on Python, so GLPK can be built before Python, or in parallel with Python - it does not need to wait for Python. 

This should improve the parallel build process. I made it a dependency on Python before, since there was a call to python in spkg-install, but since Nathann has removed that, so the dependency can be removed. 

Here's the MD5 checksums of the two files. I'm just going to overwrite these on the ticket. 


```
drkirkby@hawk:~$ digest -a md5 deps deps.diff
(deps) = 8ddc6b0fcc9445ba566fa647451d871c
(deps.diff) = 5e9a409b2ec49f00039802b20a28d7cd
```



---

Attachment

$SAGE_ROOT/spkg/standard/deps


---

Attachment

Diff file for $SAGE_ROOT/spkg/standard/deps


---

Comment by rlm created at 2010-07-05 20:37:22

Changing type from defect to enhancement.


---

Comment by rlm created at 2010-07-05 20:37:22

Changing status from needs_info to needs_review.


---

Comment by rlm created at 2010-07-05 20:37:22

Changing component from optional packages to packages.


---

Comment by drkirkby created at 2010-07-05 20:52:43

I'm attaching a deps.better, which you may or may not prefer to merge. The difference is that it makes everything depend on the 4 base packages. That means building in parallel is more relieable, as no standard packages will get built before the base packages do. 

Robert can decide whether he merges it or not. 

I've also attached a diff from the deps in this package - you can see the changes are minor. 

I've cc'ed Mitesh Patel as the making everything depend on BASE is his idea. I've put him as an author too, but Robert can remove that if he would rather use the less changed deps file

Dave


---

Comment by drkirkby created at 2010-07-05 20:53:35

A better version of deps, which ensures things depend on the 4 base packages - better for parallel building.


---

Attachment

Changes between the deps file here, and what I think is a better version - more relieable


---

Attachment

same file, but with a .txt extension, as I could not see it in my browser. Hopefully .txt should be easy for comparision of the two files


---

Attachment


---

Comment by drkirkby created at 2010-07-05 21:13:55

Changing assignee from tbd to drkirkby.


---

Comment by rlm created at 2010-07-05 21:20:47

Replying to [comment:17 drkirkby]:
> Robert can decide whether he merges it or not. 

Nope. This is part of #9274, and belongs there.


---

Attachment

A new patch to remove the #optional GLPK from Sage's code.

I know 2 or 3 are still missing in other files, which I will remove later in another patch to simplify - now useless - code. I leave them here for the moment as touching it would conflict with other patches already written.

Nathann


---

Comment by rlm created at 2010-07-05 22:32:02

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-05 22:32:02

FINALLY!


---

Comment by ncohen created at 2010-07-05 22:33:03

Yeahhhhhhhhhhhhhhhhhhhhhhhhhhhhhh !! :-D

Nathann


---

Comment by rlm created at 2010-07-05 22:35:30

Resolution: fixed


---

Comment by jhpalmieri created at 2010-07-06 00:06:41

It looks to me as though cython should be a prerequisite for glpk in spkg/standard/deps.  From setup.py:

```
from Cython.Distutils import build_ext
```

When I tried to build Sage on sage.math (using parallel spkg building), it bombed when it got to glpk because of this issue.


---

Comment by jhpalmieri created at 2010-07-06 00:08:20

If I'm right about deps, can we deal with it in #9274?


---

Comment by rlm created at 2010-07-06 00:10:16

Replying to [comment:25 jhpalmieri]:
> If I'm right about deps, can we deal with it in #9274?

Yes, and sage-4.5.alpha4 will be a very short release, so that people can actually test GLPK.


---

Comment by ncohen created at 2010-07-06 06:19:28

O_o

There should not be any setup.py file anymore in the GLPK spkg O_o

Nathann


---

Comment by rlm created at 2010-07-06 07:04:27

Replying to [comment:27 ncohen]:
> O_o
> 
> There should not be any setup.py file anymore in the GLPK spkg O_o

Nathann,

What are you talking about? I don't see one anywhere in the GLPK spkg that was merged into sage-4.5.alpha3.


---

Comment by ncohen created at 2010-07-06 07:18:37

> What are you talking about? I don't see one anywhere in the GLPK spkg that was merged into sage-4.5.alpha3.

That's what I mean ! There is no setup.py in the glpk SPKG embedded in alpha 3, and so no reason at all to make it dependent on Cython !

Nathann


---

Comment by drkirkby created at 2010-07-06 09:57:44

Nathann is saying there is no setup.py, so there should be no need for Cython. I agree with this. 

As Robert knows, I did a quick hack of a 'deps' file to 

 * Add Cython as a dependency of GLPK
 * Sort out the parallel building stuff. 

which I posted a link to (much to Roberts dislike). Sage built ok with that. 

Having seen Nathann's comments, I hacked this file again and removed the Cython dependency, so now the GLPK entry says:


```
$(INST)/$(GLPK): $(BASE) $(INST)/$(MPIR) $(INST)/$(ZLIB)
        $(INSTALL) "$(SAGE_SPKG) $(GLPK) 2>&1" "tee -a $(SAGE_LOGS)/$(GLPK).log"
```


i.e. it was back to what I had before. Sage still built ok. So I agree with Nathann, there seems no need for Cython to be a dependency of GLPK. Whatever the reasons for the failed build by someone, it was not a lack of Cython. 

I think until a release is made with all the parallel issues resolved, building will be unrelieable in parallel, and may throw up some 'red herrings'. What appears to be due to X, might in fact be due to Y. 

Dave
