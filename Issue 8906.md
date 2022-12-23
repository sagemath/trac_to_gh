# Issue 8906: Optional package for gap3

Issue created by migration from https://trac.sagemath.org/ticket/8906

Original creator: mrobado

Original creation time: 2010-05-06 14:07:54

Assignee: tbd

CC:  burcin andrew.mathas

Keywords: gap3

Here is an spkg wich contains a patched version of gap3 that compiles on linux/x86 and macosx/x86.

[http://thales.math.uqam.ca/~robado/gap3-0.3.spkg](http://thales.math.uqam.ca/~robado/gap3-0.3.spkg)


---

Comment by burcin created at 2010-05-06 16:27:32

Changing status from new to needs_work.


---

Comment by burcin created at 2010-05-06 16:27:32

Thanks a lot for the package, and a good example of how to write `spkg-install` in Python.

Here are a few comments:
 * Version numbers for the GAP4 package are of the form gap-4.4.10.p17, so we should name this gap.3.4.4.p0 and keep increasing the "patch level" at the end for updates.
 * The package has a single mercurial repository at the top, which contains spkg-install, SPKG.txt, etc. and the GAP3 source files. The convention is to keep two separate repositories, one with only "packaging" material, spkg-install and so on, another one to track changes to the upstream sources.
 * Does GAP3 have a test suite? Can we add an spkg-check which runs this? Another option is to copy the spkg-check which just tries to start GAP from the spkg mentioned in comment:9:ticket:8380.
 * SPKG.txt should be based on the template here: http://wiki.sagemath.org/spkgTemplate
  In particular:
   * the changelog should have an entry conforming to the standard
   * TODO list (in the file TODO) should be moved in the SPKG.txt
   * There should be an explanation of what changes were made to the upstream sources, even though they are already documented in the mercurial repository log.
   * SPKG.txt should note that src/bin/gap.sh hardcodes version `gap3r4p4` in the `GAP_DIR` variable
 * I don't see why these lines at the end of `spkg-install` are necessary:
 {{{
 if not os.path.exists(gap3_base):
     os.makedirs(gap3_base)
 }}}


---

Comment by mrobado created at 2010-05-06 21:26:16

Changing status from needs_work to needs_review.


---

Comment by mrobado created at 2010-05-06 21:26:16

I uploaded a new version of the package with the issues fixed at this address [http://thales.math.uqam.ca/~robado/gap-3.4.4.p0.spkg](http://thales.math.uqam.ca/~robado/gap-3.4.4.p0.spkg) . Maybe we should merge this package with the one posted on #8380.


---

Comment by burcin created at 2010-05-06 21:39:01

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-05-06 21:39:01

I don't know what the exact requirements for an optional package are. Especially the difference between an optional and an experimental package is not clear to me. I can't find them anywhere in the documentation either.

The package at http://thales.math.uqam.ca/~robado/gap-3.4.4.p0.spkg looks good to me, switching to positive review. :)


---

Comment by mvngu created at 2010-05-08 22:43:34

Some problems with gap-3.4.4.p0.spkg:

 1. All changes have not been checked in:
 {{{#!sh
[mvngu`@`sage gap-3.4.4.p0]$ hg status
M SPKG.txt
? spkg-check
 }}}
 You must check in all changes.
 1. The license file `COPYING` needs to go under the directory `src/`.
 1. The directory `src/` contains one package within another:
 {{{#!sh
[mvngu`@`sage src]$ pwd
/home/mvngu/spkg/optional/gap/gap-3.4.4.p0/src
[mvngu`@`sage src]$ ls
bin            description12  description4  description8  grp  sml  tom
description1   description13  description5  description9  htm  src  tst
description10  description2   description6  doc           lib  tbl  two
description11  description3   description7  etc           pkg  thr  utl
[mvngu`@`sage src]$ ls src
agcollec.c     description12  function.c     pcpresen.c  record.h    tietze.h
agcollec.h     description13  function.h     pcpresen.h  scanner.c   tom
aggroup.c      description2   gap.c          permutat.c  scanner.h   tst
aggroup.h      description3   gasman.c       permutat.h  set.c       two
bin            description4   gasman.h       pkg         set.h       unknown.c
blister.c      description5   grp            plist.c     sml         unknown.h
blister.h      description6   htm            plist.h     src         utl
coding.c       description7   idents.c       polynom.c   statemen.c  vecffe.c
coding.h       description8   idents.h       polynom.h   statemen.h  vecffe.h
costab.c       description9   integer.c      range.c     string.c    vector.c
costab.h       doc            integer.h      range.h     string.h    vector.h
cyclotom.c     etc            lib            rational.c  system.c    word.c
cyclotom.h     eval.c         list.c         rational.h  system.h    word.h
description1   eval.h         list.h         read.c      tbl
description10  finfield.c     Makefile       read.h      thr
description11  finfield.h     Makefile.orig  record.c    tietze.c
 }}}
 1. You don't have any patches on top of the upstream GAP 3 package, so you need to start the spkg numbering at `gap-3.4.4.spkg`, not at `gap-3.4.4.p0.spkg`. The name `gap-3.4.4.p0.spkg` implies that you have a patch to be applied on top of the upstream GAP 3 package. See this chapter [Producing New Sage Packages](http://www.sagemath.org/doc/developer/producing_spkgs.html) and chapter [Patching a Sage Package](http://www.sagemath.org/doc/developer/patching_spkgs.html) of the Developer's Guide.


---

Comment by mvngu created at 2010-05-08 22:43:34

Changing status from positive_review to needs_work.


---

Comment by burcin created at 2010-05-08 23:03:21

Hi Minh,

Replying to [comment:4 mvngu]:
> Some problems with gap-3.4.4.p0.spkg:
> 
>  1. All changes have not been checked in:
>  {{{
> #!sh
> [mvngu`@`sage gap-3.4.4.p0]$ hg status
> M SPKG.txt
> ? spkg-check
>  }}}
>  You must check in all changes.
>  1. The license file `COPYING` needs to go under the directory `src/`.

Fair enough, I didn't check these again myself. Note that the COPYING file doesn't exist in the original gap3 distribution. We decided to make one after it took us a while to discover the license has a non-commercial use restriction.

>  1. The directory `src/` contains one package within another:

This is just how the gap3 source is laid out. There are gap library files, and gap packages in the other directories. I don't see why this is a problem.

>  1. You don't have any patches on top of the upstream GAP 3 package, so you need to start the spkg numbering at `gap-3.4.4.spkg`, not at `gap-3.4.4.p0.spkg`. The name `gap-3.4.4.p0.spkg` implies that you have a patch to be applied on top of the upstream GAP 3 package.

What is in the spkg is very far from the original gap3 distribution. The changes couldn't be tracked with patches, so there is a mercurial repository in the src directory. Marco did a tremendous job creating a GAP package which actually compiles and works on different platforms, and includes the latest versions of various GAP packages still being maintained.


I agree with your points 1 and 2, but IMHO 3 and 4 are not problems that need to be addressed before this is accepted.

Thanks. 

Burcin


---

Comment by mvngu created at 2010-05-08 23:11:47

Replying to [comment:5 burcin]:
> Note that the COPYING file doesn't exist in the original gap3 distribution. We decided to make one after it took us a while to discover the license has a non-commercial use restriction.

Could you document that in the file `SPKG.txt`? Future reviewers/maintainers might not know about this.




> >  1. The directory `src/` contains one package within another:
> 
> This is just how the gap3 source is laid out. There are gap library files, and gap packages in the other directories. I don't see why this is a problem.

Could you document that in the file `SPKG.txt`? Future reviewers/maintainers might not know about this.





> What is in the spkg is very far from the original gap3 distribution. The changes couldn't be tracked with patches, so there is a mercurial repository in the src directory. 

Could you document that in the file `SPKG.txt`? Future reviewers/maintainers might not know about this.



As you can tell, I raised the above objections because the file `SPKG.txt` did not document the reasons why the spkg was structured as given.


---

Comment by nthiery created at 2010-06-17 21:19:31

Hi!

Thanks Marco for your work!

With Jean-Michel, we have merged Marco's changes into our original spkg (with the changes to the sources upstreamed in Jean's distribution). We will upload the result shortly here.

About the spkg name. Since the gap3 spkg is completely different from the gap4 one, and is supposed to cohabit with it, I would argue for calling the spkg gap3-???? to make a clear distinction. It is further based on Jean's gap3 distribution. So, would you recommend:
calling it `gap3-jm2.spkg` or `gap3-3.4.4-jm2.spkg` ?

Jean would prefer the first option, since anyway gap3's version has not changed since 1997, and won't ever change again.


---

Comment by nthiery created at 2010-06-22 21:24:55

Hi!

I just obtained the following with gap3 on winxp1 (win XP + cygwin host in the Sage build farm):


```
gap> W := CoxeterGroup("E",8);
CoxeterGroup("E",8)
gap> Size(W);                
696729600
```


For the record: I did not have Sage installed, so I did not try directly the spkg. Instead, I built and ran it by hand, using something like:


```
tar xvf gap3-jm2.spkg
cd gap3-jm2/src/src
make ibm-i386-linux-gcc
cd ..
cp src/gap.exe bin
<EDIT bin/gap.sh>
bin/gap.sh
```


In bin/gap.sh, I set GAP_PRG=gap.exe, and downgraded GAP_MEM=512m to GAP_MEM=64m (otherwise I was getting an error Gasman: can not get memory for the initial workspace).

So I assume that it should be easy to adapt the spkg to also work on windows+cygwin once sage will be more publicly available there (windows 7 still to be tested).


---

Comment by saliola created at 2011-08-24 17:10:35

What is the status of this spkg? I've used this with several versions of sage with Ubuntu and MacOSX (pre-Lion), and I have had no problems. I would be great if this appeared in the optional spkg list.

[Aside: the trac preview claims I deleted the dependencies, but I did not.]


---

Comment by saliola created at 2011-08-24 17:10:35

Changing status from needs_work to needs_info.


---

Comment by roed created at 2015-05-14 02:37:20

Is anyone still working on this spkg?  I'm interested in being able to use CHEVIE from Sage....


---

Comment by saliola created at 2015-05-15 01:22:15

It would be great to make this an official package!

I tried the spkg quickly on two machines and it didn't work on either:

- I tried `sage -i http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg` on Mac OSX and got an error

```
imac: sage --version
Sage Version 6.2, Release Date: 2014-05-06

imac: sage -i http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg
Attempting to download package gap3-jm2
>>> Trying to download http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg
[............................................................]
gap3-jm2
====================================================
Extracting package /Users/saliola/Applications/sage/upstream/gap3-jm2.spkg
-rw-r--r--  1 saliola  staff  12234482 May 14 21:16 /Users/saliola/Applications/sage/upstream/gap3-jm2.spkg
Finished extraction
****************************************************
Host system:
Darwin imac.local 14.3.0 Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64 x86_64
****************************************************
C compiler: gcc
C compiler version:
Using built-in specs.
COLLECT_GCC=/Users/saliola/Applications/sage/local/bin/gcc
COLLECT_LTO_WRAPPER=/Users/saliola/Applications/sage/local/libexec/gcc/x86_64-apple-darwin12.5.0/4.7.3/lto-wrapper
Target: x86_64-apple-darwin12.5.0
Configured with: ../src/configure --prefix=/Users/saliola/Applications/sage/local --with-local-prefix=/Users/saliola/Applications/sage/local --with-gmp=/Users/saliola/Applications/sage/local --with-mpfr=/Users/saliola/Applications/sage/local --with-mpc=/Users/saliola/Applications/sage/local --with-system-zlib --disable-multilib --disable-nls  
Thread model: posix
gcc version 4.7.3 (GCC) 
****************************************************
dyld: Symbol not found: _sqlite3_intarray_bind
  Referenced from: /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
  Expected in: /Users/saliola/Applications/sage/local/lib/libsqlite3.dylib
 in /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
make: error: unable to locate xcodebuild, please make sure the path to the Xcode folder is set correctly!
make: error: You can set the path to the Xcode folder using /usr/bin/xcode-select -switch
Compiling target macosx-gcc-686-optimized
18176
Error compiling Gap3
```


- I tried `sage -i http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg` with on Ubuntu 14.04 and got an error

```
T7600: sage --version
Executing: /home/saliola/Applications/sage/sage
SageMath Version 6.7.beta2, Release Date: 2015-04-21

T7600: sage -i http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg
Executing: /home/saliola/Applications/sage/sage
Attempting to download package gap3-jm2
>>> Trying to download http://sage.math.washington.edu/home/nthiery/gap3-jm2.spkg
[............................................................]
gap3-jm2
====================================================
Extracting package /home/saliola/Applications/sage/upstream/gap3-jm2.spkg
-rw-rw-r-- 1 saliola saliola 12234482 May 14 21:14 /home/saliola/Applications/sage/upstream/gap3-jm2.spkg
Finished extraction
****************************************************
Host system:
Linux T7600 3.13.0-45-generic #74-Ubuntu SMP Tue Jan 13 19:36:28 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
****************************************************
C compiler: gcc
C compiler version:
Using built-in specs.
COLLECT_GCC=/usr/bin/gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/4.8/lto-wrapper
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu 4.8.2-19ubuntu1' --with-bugurl=file:///usr/share/doc/gcc-4.8/README.Bugs --enable-languages=c,c++,java,go,d,fortran,objc,obj-c++ --prefix=/usr --program-suffix=-4.8 --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --with-gxx-include-dir=/usr/include/c++/4.8 --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --enable-gnu-unique-object --disable-libmudflap --enable-plugin --with-system-zlib --disable-browser-plugin --enable-java-awt=gtk --enable-gtk-cairo --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-4.8-amd64/jre --enable-java-home --with-jvm-root-dir=/usr/lib/jvm/java-1.5.0-gcj-4.8-amd64 --with-jvm-jar-dir=/usr/lib/jvm-exports/java-1.5.0-gcj-4.8-amd64 --with-arch-directory=amd64 --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --enable-objc-gc --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) 
****************************************************
make[1]: Entering directory `/home/saliola/Applications/sage/local/var/tmp/sage/build/gap3-jm2/src/src'
gcc -m32 -O3 -fomit-frame-pointer -pipe -fno-strength-reduce -march=i686 -DCPU=686 -g -O2 -DSYS_IS_USG -DSYS_HAS_TIME_PROTO -DSYS_HAS_SIGNAL_PROTO -DSYS_HAS_IOCTL_PROTO   -c -o system.o system.c
In file included from /usr/include/features.h:398:0,
                 from /usr/include/ctype.h:25,
                 from system.h:241,
                 from system.c:157:
/usr/include/x86_64-linux-gnu/gnu/stubs.h:7:27: fatal error: gnu/stubs-32.h: No such file or directory
 # include <gnu/stubs-32.h>
                           ^
compilation terminated.
make[1]: *** [system.o] Error 1
make[1]: Leaving directory `/home/saliola/Applications/sage/local/var/tmp/sage/build/gap3-jm2/src/src'
make: *** [ibm-i386-linux-gcc-optimized] Error 2
Compiling target ibm-i386-linux-gcc-optimized
512
Error compiling Gap3

```



---

Comment by saliola created at 2015-05-15 01:22:15

Changing status from needs_info to needs_work.


---

Comment by saliola created at 2015-05-15 01:27:00

It may very well be that the problems with the above are related to unmet system-wide dependencies / configurations, but we should figure them out and update the installation instructions appropriately since I can compile Sage on these systems.


---

Comment by saliola created at 2015-05-15 01:29:31

Replying to [comment:15 roed]:
> Is anyone still working on this spkg?  I'm interested in being able to use CHEVIE from Sage....

To get yourself up and running quickly without waiting for this spkg to be finalized, just install GAP3 system-wide using one of the following options and you should be good to go.

- http://www.math.rwth-aachen.de/~Frank.Luebeck/gap/GAP3

- http://people.math.jussieu.fr/~jmichel/chevie/chevie.html


---

Comment by stumpc5 created at 2015-06-18 19:36:42

Franco and Nicolas, do you plan to make the aim of this ticket happen? It would be great to have for #11187 which I would like to have finished soon.

Thanks, Christian


---

Comment by saliola created at 2015-06-18 19:49:38

Nicolas, what do you think? Should we package this? If so, which version (Luebeck's or Michel's)?

Also, what would be required to maintain this over time? Test it with every stable release of Sage? It would be good to have a plan going forward on maintaining this package.


---

Comment by stumpc5 created at 2015-06-18 19:57:57

I'd vote for Jean Michel's last version since I regularly send him bug reports in the `chevie` code (found through the code now in #11187, and usually in dark corners of complex reflection group computations) and which he then very quickly fixes and provides on his webside.


---

Comment by nthiery created at 2015-06-20 12:27:52

I agree it would be good to have. Alas I don't have the manpower to work on this.

I would go for Jean Michel's version indeed. I believe the main stopgap is to make this compile reasonably robustly. The compilation error in comment:16 on Ubuntu is a missing dependency: since gap3 is 32bit it needs to be compiled with the 32bits C library headers. See
e.g. http://www.cyberciti.biz/tips/compile-32bit-application-using-gcc-64-bit-linux.html for details.


---

Comment by stumpc5 created at 2015-06-20 16:17:24

I could try doing it, but I'd be glad if you were taking that over, Franco... Christian


---

Comment by saliola created at 2015-06-23 01:51:09

From what I gather from [Frank Leubeck's site](http://www.math.rwth-aachen.de/~Frank.Luebeck/gap/GAP3/index.html):
* Frank Leubeck's package includes some optimizations and is statically linked;
* Jean Michel's version has a newer version of CHEVIE;
* Andrew Mathas provided a Makefile target to compile GAP3 on Mac OSX machines.

I guess these should all be combined at some point?

I'm adding Andrew Mathas to the CC list. Andrew, what is your opinion on this?


---

Comment by stumpc5 created at 2015-07-20 12:02:22

So Franco -- are we going to do something here?


---

Comment by saliola created at 2015-07-25 03:45:49

OK, so besides the fact that I don't know what I am doing, I think this is ready for review.

Here is what you have to do to test this.

1. Checkout this branch: use your favourite method; for instance, with git-trac,

```
git trac checkout 8906
```


2. Download the upstream tarball http://webusers.imj-prg.fr/~jean.michel/gap3/gap3-jm5.tar.gz and copy it into `SAGE_ROOT/upstream`; or just run the following commands:

```
cd $(sage --root)/upstream
curl -O http://webusers.imj-prg.fr/~jean.michel/gap3/gap3-jm5.tar.gz
```


3. Install the spkg:

```
sage -i gap3
```


*Question:* where do I put the upstream tarball so that people don't have to do step 2?

----
New commits:


---

Comment by saliola created at 2015-07-25 03:45:49

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2015-07-25 15:54:12

So is that tarball the official release and the one you want mirrored once this ticket is merged? If so, then please add it to the ticket description. The release manager will add it to the tarball mirror list so a user will only have to do `sage -i gap3` once this is merged.


---

Comment by stumpc5 created at 2015-07-26 22:06:13

I am certainly not the right one to do a review since I don't know either whether everything is correct here. Nevertheless, it seems to work like a charm, thanks for preparing it!

Do you know why the first call of `gap3` doesn't appear to work properly?


```
┌────────────────────────────────────────────────────────────────────┐
│ SageMath Version 6.8.rc1, Release Date: 2015-07-22                 │
│ Type "notebook()" for the browser-based notebook interface.        │
│ Type "help()" for help.                                            │
└────────────────────────────────────────────────────────────────────┘
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Warning: this is a prerelease version, and it may be unstable.     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
sage: gap3
Gap3
sage: gap3.execute("1+1")
''
sage: gap3.execute("1+1")
'2'
sage: 
```



---

Comment by chapoton created at 2015-07-30 12:07:06

As this is confusing the only running patchbot, I temporarily put this into 'needs_info'


---

Comment by chapoton created at 2015-07-30 12:07:06

Changing status from needs_review to needs_info.


---

Comment by saliola created at 2015-07-30 22:14:22

Replying to [comment:29 stumpc5]:
> I am certainly not the right one to do a review since I don't know either whether everything is correct here. Nevertheless, it seems to work like a charm, thanks for preparing it!
> 
> Do you know why the first call of `gap3` doesn't appear to work properly?
> 
> {{{
> ┌────────────────────────────────────────────────────────────────────┐
> │ [SageMath](SageMath) Version 6.8.rc1, Release Date: 2015-07-22                 │
> │ Type "notebook()" for the browser-based notebook interface.        │
> │ Type "help()" for help.                                            │
> └────────────────────────────────────────────────────────────────────┘
> ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
> ┃ Warning: this is a prerelease version, and it may be unstable.     ┃
> ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
> sage: gap3
> Gap3
> sage: gap3.execute("1+1")
> ''
> sage: gap3.execute("1+1")
> '2'
> sage: 
> }}}

This is not an issue with the proposed SPKG. In fact, it is a problem even with the first proposed SPKG from Marco Robado.

So this should be a separate ticket.

Edit: I created a ticket: #18971.


---

Comment by saliola created at 2015-07-30 22:20:55

Replying to [comment:30 chapoton]:
> As this is confusing the only running patchbot, I temporarily put this into 'needs_info'

OK, but this still "needs review". :-)


---

Comment by saliola created at 2015-07-30 22:26:29

Replying to [comment:28 tscrim]:
> So is that tarball the official release and the one you want mirrored once this ticket is merged? If so, then please add it to the ticket description. The release manager will add it to the tarball mirror list so a user will only have to do `sage -i gap3` once this is merged.

Thanks, Travis. I'll modify the description.


---

Comment by stumpc5 created at 2015-08-24 09:55:55

> Replying to [comment:28 tscrim]: Thanks, Travis. I'll modify the description.

Hi there -- is anything missing here (except a positive review) in order to get this merged? tscrim, would you be able to do the review if necessary? Thanks, Christian


---

Comment by chapoton created at 2015-08-31 15:29:29

Changing status from needs_info to needs_review.


---

Comment by chapoton created at 2015-08-31 15:29:29

please someone put this into positive review


---

Comment by stumpc5 created at 2015-09-01 19:15:15

It seems to work as it is supposed to. Also, the files and their content are as described to be at http://doc.sagemath.org/html/en/developer/packaging.html#directory-structure.

I think it is ready to go!


---

Comment by stumpc5 created at 2015-09-01 19:15:15

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-09-02 17:25:36

Resolution: fixed


---

Comment by dimpase created at 2015-09-08 18:36:32

there is a lot of crud left in bin/ subdir.


---

Comment by dimpase created at 2015-09-08 18:43:44

this is scary. This package distributes executables. IMHO it should have never been accepted this way.


---

Comment by dimpase created at 2015-09-08 18:52:02

Having said that, I can also point out that some packages included only contain executables for x86_64, while they are advertised to be included regardless of the platform.


---

Comment by ncohen created at 2015-09-09 21:54:49

(this was reverted in #19164)


---

Comment by nthiery created at 2017-06-06 21:08:20

Replying to [comment:31 saliola]:
> Replying to [comment:29 stumpc5]:
> > I am certainly not the right one to do a review since I don't know either whether everything is correct here. Nevertheless, it seems to work like a charm, thanks for preparing it!
> > 
> > Do you know why the first call of `gap3` doesn't appear to work properly?
> > 
> > {{{
> > ┌────────────────────────────────────────────────────────────────────┐
> > │ [SageMath](SageMath) Version 6.8.rc1, Release Date: 2015-07-22                 │
> > │ Type "notebook()" for the browser-based notebook interface.        │
> > │ Type "help()" for help.                                            │
> > └────────────────────────────────────────────────────────────────────┘
> > ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
> > ┃ Warning: this is a prerelease version, and it may be unstable.     ┃
> > ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
> > sage: gap3
> > Gap3
> > sage: gap3.execute("1+1")
> > ''
> > sage: gap3.execute("1+1")
> > '2'
> > sage: 
> > }}}
> 
> This is not an issue with the proposed SPKG. In fact, it is a problem even with the first proposed SPKG from Marco Robado.
> 
> So this should be a separate ticket.
> 
> Edit: I created a ticket: #18971.

Fixed in #23142.
