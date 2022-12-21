# Issue 8229: gap_packages-4.4.12 updated

Issue created by migration from Trac.

Original creator: dimpase

Original creation time: 2010-02-10 14:31:01

Assignee: tbd

Keywords: GAP, GAP packages

I created and tested, together with the 
updated GAP to 4.4.12 --- see tickets #8150 and #8076 ---
gap_packages-4.4.12_2.spkg, that is available at 
http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
along with  http://boxen.math.washington.edu/home/dima/packages/database_gap-4.4.12.spkg and
http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg

please test these (already tested OK on x86, x86_64, ia64, and OSX PPC 10.5)
together, not forgetting to apply the patch 
track-8150 available at #8150, 
but ignoring the other (obsolete) patches there and at #8076.

This ticket is issued in addition to #8150 and #8076


---

Comment by dimpase created at 2010-02-10 14:31:15

Changing status from new to needs_review.


---

Comment by wdj created at 2010-02-10 15:42:17

The patch 13702 from  #8076 failed to apply to 4.3.2.rc0. Is there a reason why? SHould I try 4.3.2 instead?


---

Comment by dimpase created at 2010-02-10 16:18:55

Replying to [comment:2 wdj]:
> The patch 13702 from  #8076 failed to apply to 4.3.2.rc0. Is there a reason why? SHould I try 4.3.2 instead?

There is only one patch to apply, namely the one named trac-8150.
The other patches, named 13*..., are obsolete - I mention this somewhere
(unfortunately I can't just delete these files from trac)


---

Comment by wdj created at 2010-02-10 16:33:43

Replying to [comment:3 dimpase]:
> Replying to [comment:2 wdj]:
> > The patch 13702 from  #8076 failed to apply to 4.3.2.rc0. Is there a reason why? SHould I try 4.3.2 instead?
> 
> There is only one patch to apply, namely the one named trac-8150.
> The other patches, named 13*..., are obsolete - I mention this somewhere
> (unfortunately I can't just delete these files from trac)

Thank you. Yes, you explained it and I misread what you wrote.

I installed the patch and then gap-4.4.12 on sage-4.3.2.rc0, mac 10.6.2. This went fine.

Installing the GAP packages was a different matter:


```
jeeves:sage-4.3.2.rc0 wdj$ ./sage -i http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg 
Installing http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
Calling sage-spkg on http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
Warning: Attempted to overwrite SAGE_ROOT environment variable
gap_packages-4.4.12_2
Machine:
Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
Deleting directories from past builds of previous/current versions of gap_packages-4.4.12_2
/Users/wdj/sagefiles/sage-4.3.2.rc0/local/bin/sage-spkg: file gap_packages-4.4.12_2 does not exist
Attempting to download it.
http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg --> gap_packages-4.4.12_2.spkg
[..................................................]
Extracting package /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg ...
-rw-r--r--  1 wdj  staff  18318369 Feb 10 11:29 /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg
Finished extraction
****************************************************
Host system
uname -a:
Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i686-apple-darwin10
Configured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10
Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5646) (dot 1)
****************************************************
gap-4.4.10.p13
********************************************************************
Installing optional GAP packages, which may not be open source.
Installing GAP gap-4.4.10 packages to /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2/.. 
Please see SPKG.txt for license details.
********************************************************************
mkdir: /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10: No such file or directory
cp: directory /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10/pkg does not exist
Error copying SPKG.txt

real    0m0.074s
user    0m0.008s
sys     0m0.022s
sage: An error occurred while installing gap_packages-4.4.12_2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/wdj/sagefiles/sage-4.3.2.rc0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2' && '/Users/wdj/sagefiles/sage-4.3.2.rc0/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
```


Do you see what the problem is?


---

Comment by dimpase created at 2010-02-10 17:09:03

Replying to [comment:4 wdj]:
 
> Do you see what the problem is?

I think you should do 
sage -f foo.spkg, 
and not 
sage -i foo.spkg

it could  be that you installed gap-4.4.12.p2.spkg  using -i, and not -f,
and this led to this problem --- the package gap did not change the version...


---

Comment by wdj created at 2010-02-10 17:23:57

I tried sage -f as well before posting the above message but didn't post the log since it was similar.
However, since you asked for it, here it is!



```
jeeves:sage-4.3.2.rc0 wdj$ ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg 
Force installing http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
Calling sage-spkg on http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
Warning: Attempted to overwrite SAGE_ROOT environment variable
gap_packages-4.4.12_2
Machine:
Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
Deleting directories from past builds of previous/current versions of gap_packages-4.4.12_2
Extracting package /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg ...
-rw-r--r--  1 wdj  staff  18318369 Feb 10 11:29 /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg
Finished extraction
****************************************************
Host system
uname -a:
Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i686-apple-darwin10
Configured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10
Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5646) (dot 1)
****************************************************
gap-4.4.10.p13
********************************************************************
Installing optional GAP packages, which may not be open source.
Installing GAP gap-4.4.10 packages to /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2/.. 
Please see SPKG.txt for license details.
********************************************************************
mkdir: /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10: No such file or directory
cp: directory /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10/pkg does not exist
Error copying SPKG.txt

real    0m0.027s
user    0m0.008s
sys     0m0.019s
sage: An error occurred while installing gap_packages-4.4.12_2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/wdj/sagefiles/sage-4.3.2.rc0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2' && '/Users/wdj/sagefiles/sage-4.3.2.rc0/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
```



---

Comment by dimpase created at 2010-02-10 22:54:18

Replying to [comment:6 wdj]:
> I tried sage -f as well before posting the above message but didn't post the log since it was similar.
> However, since you asked for it, here it is!
> 
before this, you should also do
sage -f gap-4.4.12.p2.spkg    

the problem is that the version of gap package did not change, an this must be done during the installation of gap, not
during the installation of gap_packages


---

Comment by wdj created at 2010-02-10 23:36:24

This seems reasonable. But when I did

```
 ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg
```

followed by

```
./sage -b
```

and then

```
./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg 
```

I got the same error as posted above:


```
jeeves:sage-4.3.2.rc0 wdj$ ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg 
Force installing http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
Calling sage-spkg on http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
Warning: Attempted to overwrite SAGE_ROOT environment variable
gap_packages-4.4.12_2
Machine:
Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
Deleting directories from past builds of previous/current versions of gap_packages-4.4.12_2
Extracting package /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg ...
-rw-r--r--  1 wdj  staff  18318369 Feb 10 11:29 /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg
Finished extraction
****************************************************
Host system
uname -a:
Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i686-apple-darwin10
Configured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10
Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5646) (dot 1)
****************************************************
gap-4.4.10.p13
********************************************************************
Installing optional GAP packages, which may not be open source.
Installing GAP gap-4.4.10 packages to /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2/.. 
Please see SPKG.txt for license details.
********************************************************************
mkdir: /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10: No such file or directory
cp: directory /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10/pkg does not exist
Error copying SPKG.txt

real    0m0.032s
user    0m0.008s
sys     0m0.020s
sage: An error occurred while installing gap_packages-4.4.12_2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/wdj/sagefiles/sage-4.3.2.rc0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2' && '/Users/wdj/sagefiles/sage-4.3.2.rc0/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
```


Moreover,


```
jeeves:sage-4.3.2.rc0 wdj$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: 6229-gap
sage: gap_version()
'4.4.12'
```

so sage thinks it is running gap-4.4.12.


---

Comment by dimpase created at 2010-02-11 00:48:39

Replying to [comment:8 wdj]:
> This seems reasonable. But when I did
> {{{
>  ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg
> }}}
> followed by
> {{{
> ./sage -b
> }}}
> and then
> {{{
> ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg 
> }}}
> I got the same error as posted above:
> 
> {{{
> jeeves:sage-4.3.2.rc0 wdj$ ./sage -f http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg 
> Force installing http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
> Calling sage-spkg on http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg
> Warning: Attempted to overwrite SAGE_ROOT environment variable
> gap_packages-4.4.12_2
> Machine:
> Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
> Deleting directories from past builds of previous/current versions of gap_packages-4.4.12_2
> Extracting package /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg ...
> -rw-r--r--  1 wdj  staff  18318369 Feb 10 11:29 /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/optional/gap_packages-4.4.12_2.spkg
> Finished extraction
> ****************************************************
> Host system
> uname -a:
> Darwin jeeves.home 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386
> ****************************************************
> ****************************************************
> CC Version
> gcc -v
> Using built-in specs.
> Target: i686-apple-darwin10
> Configured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/<sup>[cg][</sup>.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10
> Thread model: posix
> gcc version 4.2.1 (Apple Inc. build 5646) (dot 1)
> ****************************************************
> gap-4.4.10.p13
> ********************************************************************
> Installing optional GAP packages, which may not be open source.
> Installing GAP gap-4.4.10 packages to /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2/.. 
> Please see SPKG.txt for license details.
> ********************************************************************
> mkdir: /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10: No such file or directory
> cp: directory /Users/wdj/sagefiles/sage-4.3.2.rc0/local/lib/gap-4.4.10/pkg does not exist
> Error copying SPKG.txt
> 
> real    0m0.032s
> user    0m0.008s
> sys     0m0.020s
> sage: An error occurred while installing gap_packages-4.4.12_2
> Please email sage-devel http://groups.google.com/group/sage-devel
> explaining the problem and send the relevant part of
> of /Users/wdj/sagefiles/sage-4.3.2.rc0/install.log.  Describe your computer, operating system, etc.
> If you want to try to fix the problem yourself, *don't* just cd to
> /Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2 and type 'make check' or whatever is appropriate.
> Instead, the following commands setup all environment variables
> correctly and load a subshell for you to debug the error:
> (cd '/Users/wdj/sagefiles/sage-4.3.2.rc0/spkg/build/gap_packages-4.4.12_2' && '/Users/wdj/sagefiles/sage-4.3.2.rc0/sage' -sh)
> When you are done debugging, you can type "exit" to leave the
> subshell.
> }}}
> 
> Moreover,
> 
> {{{
> jeeves:sage-4.3.2.rc0 wdj$ ./sage
> ----------------------------------------------------------------------
> | Sage Version 4.3.2.rc0, Release Date: 2010-02-03                   |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> **********************************************************************
> *                                                                    *
> * Warning: this is a prerelease version, and it may be unstable.     *
> *                                                                    *
> **********************************************************************
> Loading Sage library. Current Mercurial branch is: 6229-gap
> sage: gap_version()
> '4.4.12'
> }}}
> so sage thinks it is running gap-4.4.12.

I am unable reproduce this. 
Could you please  install a fresh sage-4.3.2  from source and then 
do the above?
This worked on 5 different machines (well, not on OSX 10.6 Intel, but, in particular, on OSX 10.5 PPC).


---

Comment by dimpase created at 2010-02-11 01:20:31

Replying to [comment:8 wdj]:

I insist on a clean install, in another directory, as it seems that you have different instances of Sage lying around in the same directory, one clone of another, one still with gap-4.4.10, another "updated" to 4.4.12, and they appear to interfere with each other in some way.


---

Comment by wdj created at 2010-02-11 02:27:06

I did it again on a fresh install. Same problem.


---

Comment by dimpase created at 2010-02-11 02:40:43

Replying to [comment:11 wdj]:
> I did it again on a fresh install. Same problem.
omg...

rename all files gap*4.4.10*.spkg in spkg/standard to something that is not recognised as spkg
(I normally just erase them, so perhaps this might be the root of the problem for you)

then redo all the package installs:
sage -f gap*...

it can also be that you have  scripts in, say, /usr/local/bin pointing out to wrong installation of sage

Failing all this, you can rebuild the whole sage from scratch with right spkgs corresponding to 4.4.12.


---

Comment by wdj created at 2010-02-11 02:46:29

Changing status from needs_review to needs_work.


---

Comment by wdj created at 2010-02-11 02:46:29

Replying to [comment:12 dimpase]:
> Replying to [comment:11 wdj]:
> > I did it again on a fresh install. Same problem.
> omg...
> 
> rename all files gap*4.4.10*.spkg in spkg/standard to something that is not recognised as spkg
> (I normally just erase them, so perhaps this might be the root of the problem for you)


???!!!!
This is not the correct way to build a package!


> 
> then redo all the package installs:
> sage -f gap*...
> 
> it can also be that you have  scripts in, say, /usr/local/bin pointing out to wrong installation of sage
> 
> Failing all this, you can rebuild the whole sage from scratch with right spkgs corresponding to 4.4.12.
> 


I have tried your instructions on two different macs (both running 4.3.2 and 10.6.2) and a linux machine (running ubuntu 9.10).
Same error on all machines. There is something wrong with

(1) make clone
(2) apply trac-8150
(3) sage -f gap-4.4.12
(4) sage -f gap_packages.

The last step is where the error occurs on every machine.

As far as I know, this is the way it is *supposed* to work. 

To be as clear as I can, you are *not* supposed to ask people to delete gap-4.4.10 manually at any stage of the install. Maybe if this is not clear, it should be moved to sage-support or sage-devel?

I am marking this as needs work.


---

Comment by dimpase created at 2010-02-11 02:53:06

Replying to [comment:13 wdj]:


I do not know what happens to the 
> Replying to [comment:12 dimpase]:
> > Replying to [comment:11 wdj]:
> > > I did it again on a fresh install. Same problem.
> > omg...
> > 
> > rename all files gap*4.4.10*.spkg in spkg/standard to something that is not recognised as spkg
> > (I normally just erase them, so perhaps this might be the root of the problem for you)
> 
> 
> ???!!!!
> This is not the correct way to build a package!
> 
> 
> > 
> > then redo all the package installs:
> > sage -f gap*...
> > 
> > it can also be that you have  scripts in, say, /usr/local/bin pointing out to wrong installation of sage
> > 
> > Failing all this, you can rebuild the whole sage from scratch with right spkgs corresponding to 4.4.12.
> > 
> 
> 
> I have tried your instructions on two different macs (both running 4.3.2 and 10.6.2) and a linux machine (running ubuntu 9.10).
> Same error on all machines. There is something wrong with
> 
> (1) make clone

Sorry, but I asked you to do it on a *clean install*, not on a clone...

> (2) apply trac-8150
> (3) sage -f gap-4.4.12
> (4) sage -f gap_packages.
> 
> The last step is where the error occurs on every machine.
> 
> As far as I know, this is the way it is *supposed* to work. 
> 
> To be as clear as I can, you are *not* supposed to ask people to delete gap-4.4.10 manually at any stage of the install. Maybe if this is not clear, it should be moved to sage-support or sage-devel?
> 
> I am marking this as needs work.


---

Comment by dimpase created at 2010-02-11 04:40:38

Replying to [comment:13 wdj]:

OK, I can reproduce your problem. Namely, I see this behaviour if I try to upgrade
a binary distribution of 4.3.2 (just tried it on boxen, and saw exactly the same thing as you did). But, I swear, it does work on a distribution built from source,
even if I compile gap 4.4.10 and its packages in, and then do the regular upgrade
with -f, without removing old spkgs, it all goes smoothly.

But this is not a problem of our new packages, IMHO. At worst it would mean that 4.4.12 will not be compatible with older sage releases.


> Replying to [comment:12 dimpase]:
> > Replying to [comment:11 wdj]:
> > > I did it again on a fresh install. Same problem.
> > omg...
> > 
> > rename all files gap*4.4.10*.spkg in spkg/standard to something that is not recognised as spkg
> > (I normally just erase them, so perhaps this might be the root of the problem for you)
> 
> 
> ???!!!!
> This is not the correct way to build a package!

Well, we were debugging a problem, OK? :-)

We need to understand how you get that 4.4.10 gets back at you
on a binary distro.

When I said "a fresh install" I really meant it, not a clone...
(cp -a <your-sageroot> <newsageroot> will do the job, but sage -clone won't !)
May I humbly request that you create a really new 4.3.2 install,
from source (a binary download would NOT work --- I do not know why, but this is not the place fix this bug or feature --- I'll ask on sage-devel), 
and try the packages there.
Thanks in advance. 
 
> 
> 
> > 
> > then redo all the package installs:
> > sage -f gap*...
> > 
> > it can also be that you have  scripts in, say, /usr/local/bin pointing out to wrong installation of sage
> > 
> > Failing all this, you can rebuild the whole sage from scratch with right spkgs corresponding to 4.4.12.
> > 
> 
> 
> I have tried your instructions on two different macs (both running 4.3.2 and 10.6.2) and a linux machine (running ubuntu 9.10).
> Same error on all machines. There is something wrong with
> 
> (1) make clone
> (2) apply trac-8150
> (3) sage -f gap-4.4.12
> (4) sage -f gap_packages.
> 
> The last step is where the error occurs on every machine.


> 
> As far as I know, this is the way it is *supposed* to work. 
> 
> To be as clear as I can, you are *not* supposed to ask people to delete gap-4.4.10 manually at any stage of the install. Maybe if this is not clear, it should be moved to sage-support or sage-devel?
> 
> I am marking this as needs work.


---

Comment by dimpase created at 2010-02-11 04:40:38

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2010-02-11 05:19:43

Replying to [comment:15 dimpase]:
I found where the problem lies: when you upgrade gap_packages,
the file gap-4.4.12.p2.spkg must be physically present in spkg/standard

If it is there, I can do sage -f gap_packages-...spkg
just fine.
The file names are used by the script  spkg/standard/newest_version
to get the version of the installed package.

This script is called in spkg-install of gap_packages spkg.

So it would not work if you do 
spkg -f http://....gap-4.4.12.p2.spkg
instead.

This is not our bug, I think. (spkg/standard/newest_version is a standard thing...)


---

Comment by wdj created at 2010-02-11 17:04:57

Okay, modulo the sage -f bug reported in http://trac.sagemath.org/sage_trac/ticket/8236, here is what I have done.

On a mac 10.6.2 machine running sage 4.3.2, I applied trac-8150, then sage -f gap-4.4.12, then sage -f gap_packages, then sage -f database_gap, as indicated in the instructions above. All went fine and sage -testall passes. I then ran sage -testall --optional. I could see only one related failure and it might or might not be minor. Apparently when the new gap_packages skpg was built, it was not set to compile and install the guava C code written by J Leon. This caused 2 failures. When I compiled the code (the traceback tells you how), that test passed. I tested the packages with some random GAP commands and everything else seems to be installed and working fine.

If this trac ticket is to judge only gap-4.4.12, then I give it a positive review. If it is to also include gap_packages then maybe I have some reservations (database_gap seems fine though). Since gap_packages is in the title of the ticket, I am hesitant to give this a positive review yet. I don't know if Leon's code is so old that it will not compile on some machines, in which case this is not a problem for this ticket. So, I am marking this as needs info.


---

Comment by wdj created at 2010-02-11 17:04:57

Changing status from needs_review to needs_info.


---

Comment by dimpase created at 2010-02-12 10:54:12

Replying to [comment:18 wdj]:

Thanks!

could you please meanwhile give the positive review to 
#8076 - i.e. to the ticket on the gap-4.4.12 spkg?

I suppose Leon's code is also in 4.4.10, so there should be no problem
with also compiling it on 4.4.12. I'll add this to spkg-install later today...

database_gap is just a copy you your latest 4.4.12 spkg, unless I forgot
something... As far as I recall, no updates were necessary.




> Okay, modulo the sage -f bug reported in http://trac.sagemath.org/sage_trac/ticket/8236, here is what I have done.
> 
> On a mac 10.6.2 machine running sage 4.3.2, I applied trac-8150, then sage -f gap-4.4.12, then sage -f gap_packages, then sage -f database_gap, as indicated in the instructions above. All went fine and sage -testall passes. I then ran sage -testall --optional. I could see only one related failure and it might or might not be minor. Apparently when the new gap_packages skpg was built, it was not set to compile and install the guava C code written by J Leon. This caused 2 failures. When I compiled the code (the traceback tells you how), that test passed. I tested the packages with some random GAP commands and everything else seems to be installed and working fine.
> 
> If this trac ticket is to judge only gap-4.4.12, then I give it a positive review. If it is to also include gap_packages then maybe I have some reservations (database_gap seems fine though). Since gap_packages is in the title of the ticket, I am hesitant to give this a positive review yet. I don't know if Leon's code is so old that it will not compile on some machines, in which case this is not a problem for this ticket. So, I am marking this as needs info.
> 
> 
>


---

Comment by dimpase created at 2010-02-14 04:22:55

Replying to [comment:19 dimpase]:
 
> I suppose Leon's code is also in 4.4.10, so there should be no problem
> with also compiling it on 4.4.12. I'll add this to spkg-install later today...
> 

In 4.4.10 Leon's code was compiled in gap spkg, not in gap_packages spkg.
So, when you created 1st versions of 4.4.12-spkg's, you (rightly) took out this compilation from gap spkg, but did not add it in  gap_packages spkg.
That's why it's missing at the moment.
I will add it to gap_packages spkg.


---

Comment by dimpase created at 2010-02-14 06:13:53

Changing status from needs_info to needs_review.


---

Comment by dimpase created at 2010-02-14 06:13:53

Replying to [comment:18 wdj]:

There was a trivial typo in spkg-install that prevented all 
of guava from being compiled.
I fixed it, and put the new version of the spkg here
[http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg)
Please reinstall and test the relevant part.
I tested on Linux that -t -optional passes on sage/coding/ after this fix.
Thanks,
Dima


> Okay, modulo the sage -f bug reported in http://trac.sagemath.org/sage_trac/ticket/8236, here is what I have done.
> 
> On a mac 10.6.2 machine running sage 4.3.2, I applied trac-8150, then sage -f gap-4.4.12, then sage -f gap_packages, then sage -f database_gap, as indicated in the instructions above. All went fine and sage -testall passes. I then ran sage -testall --optional. I could see only one related failure and it might or might not be minor. Apparently when the new gap_packages skpg was built, it was not set to compile and install the guava C code written by J Leon. This caused 2 failures. When I compiled the code (the traceback tells you how), that test passed. I tested the packages with some random GAP commands and everything else seems to be installed and working fine.
> 
> If this trac ticket is to judge only gap-4.4.12, then I give it a positive review. If it is to also include gap_packages then maybe I have some reservations (database_gap seems fine though). Since gap_packages is in the title of the ticket, I am hesitant to give this a positive review yet. I don't know if Leon's code is so old that it will not compile on some machines, in which case this is not a problem for this ticket. So, I am marking this as needs info.
> 
> 
>


---

Comment by wdj created at 2010-02-14 12:46:05

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2010-02-14 12:46:05

The binary from Leon's code did not compile for me the first time (installing via the internet). Then I downloaded the spkg and installed using sage -f and it worked. The sage -t --optional from last time passes now.

I'm a little bit curious as to why I had to install it twice, though I think this should get a positive review since it seems that the package is fine but the internet installation method is not working as I expected. (BTW, my mac asks me before opening a file downloaded from the internet - I wonder if that is an issue?)

Still, thanks very much Dima.


---

Comment by mvngu created at 2010-02-17 05:18:59

Changing component from packages to optional packages.


---

Comment by mvngu created at 2010-02-17 21:23:40

Merged [gap_packages-4.4.12_2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg) in the optional spkg repository. See

http://www.sagemath.org/packages/optional/


---

Comment by mvngu created at 2010-02-17 21:23:40

Resolution: fixed
