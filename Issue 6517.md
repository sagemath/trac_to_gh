# Issue 6517: [with SPKG, needs review] FriCAS 1.0.7

Issue created by migration from https://trac.sagemath.org/ticket/6517

Original creator: awebb

Original creation time: 2009-07-12 11:52:39

Assignee: tbd

CC:  bpage mhansen hemmecke

This is an update to fricas to use ecl and to update to the recent fricas release. The package is based on fricas-1.0.3.p0.spkg. 

The package can be downloaded here: http://www.mediafire.com/file/im5zd201mh0/fricas-1.0.7.p0.spkg

Adam


---

Comment by mvngu created at 2009-07-12 12:08:42

This might depends on or related to ticket #6318.


---

Comment by awebb created at 2009-07-13 06:11:33

Ticket #6318 is related. The patches on that ticket were tested with this package.


---

Comment by jsp created at 2009-07-14 15:45:45


```
79 FriCAS installation finished.

real	46m21.303s
user	34m38.652s
sys	4m30.484s
Successfully installed fricas-1.0.7.p0

```


I tested the patches from #6318 related to fricas.

./sage -t --long --optional devel/sage/sage/interface/fricas.py

alls tests passed.

Positive review.

Jaap


---

Comment by mvngu created at 2009-07-19 16:48:37

Replying to [comment:3 awebb]:
> Ticket #6318 is related. The patches on that ticket were tested with this package.
So what is the order of merging patches here? Is it
 1. merge the patches at #6318;
 1. then merge the spkg on this ticket in the optional spkg repository?
In that case, #6318 must get positive review first. On the other hand, is this ticket and its spkg not at all dependent on #6318?


---

Comment by jsp created at 2009-07-19 16:57:01

Replying to [comment:5 mvngu]:
> Replying to [comment:3 awebb]:
> > Ticket #6318 is related. The patches on that ticket were tested with this package.
> So what is the order of merging patches here? Is it
>  1. merge the patches at #6318;
>  1. then merge the spkg on this ticket in the optional spkg repository?
> In that case, #6318 must get positive review first. On the other hand, is this ticket and its spkg not at all dependent on #6318?


I think it is independent of #6318 in the sense that it updates the fricas optional spkg.

And than it fixes the fricas.py failures mentioned in #6318, Not the axiom issues.

Jaap


---

Comment by mvngu created at 2009-07-19 18:41:01

I've uploaded Adam's FriCAS 1.0.7 spkg to

http://sage.math.washington.edu/home/mvngu/patch/fricas-1.0.7.p0.spkg

I install it as in the following transcript, but received "configure: error: Unable to determine Lisp flavor":

```
[mvngu@sage sage-4.1.1.alpha0]$ ./sage -f /home/mvngu/patch/fricas-1.0.7.p0.spkg
<insall-messages>
axiom_build_bindir = /scratch/mvngu/release/sage-4.1.1.alpha0/spkg/build/fricas-1.0.7.p0/build-dir/build/x86_64-unknown-linux/bin
checking Lisp implementation... ECL (Embeddable Common-Lisp) 9.4.1
Copyright (C) 1984 Taiichi Yuasa and Masami Hagiya
Copyright (C) 1993 Giuseppe Attardi
Copyright (C) 2000 Juan J. Garcia-Ripoll
ECL is free software, and you are welcome to redistribute it
under certain conditions; see file 'Copyright' for details.
Type :h for Help.  Top level.
> 
;;; Loading "/scratch/mvngu/release/sage-4.1.1.alpha0/spkg/build/fricas-1.0.7.p0/src/config.lisp"
Filesystem error with pathname #P"SYS:cmp.NEWEST".
Either
 1) the file does not exist, or
 2) we are not allow to access the file, or
 3) the pathname points to a broken symbolic link.
Broken at SI:BYTECODES.No restarts available.
Broken at SI:BYTECODES. File: #P"/scratch/mvngu/release/sage-4.1.1.alpha0/spkg/build/fricas-1.0.7.p0/src/config.lisp" (Form #1)
>> 
configure: error: Unable to determine Lisp flavor
***********************************************************
Failed to configure FriCAS.
***********************************************************

real	0m0.577s
user	0m0.250s
sys	0m0.340s
sage: An error occurred while installing fricas-1.0.7.p0
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /scratch/mvngu/release/sage-4.1.1.alpha0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/scratch/mvngu/release/sage-4.1.1.alpha0/spkg/build/fricas-1.0.7.p0 and type 'make'.
Instead type "/scratch/mvngu/release/sage-4.1.1.alpha0/sage -sh"
in order to set all environment variables correctly, then cd to
/scratch/mvngu/release/sage-4.1.1.alpha0/spkg/build/fricas-1.0.7.p0
(When you are done debugging, you can type "exit" to leave the
subshell.)
```

Am I doing something wrong or missing something?


---

Comment by awebb created at 2009-07-24 06:42:51

This package depends on #6318 for the fricas interface to work therefore that patch needs to go in first. 

adam


---

Comment by awebb created at 2009-07-24 15:13:58

In previous versions there was an install option for the lisp flavour but according to the fricas mailing list, this is depreciated and fricas is supposed to detect which lisp is used. I have not yet tested with 4.1.1.alpha0 but it worked for me on 4.0 and 4.1.


---

Comment by awebb created at 2009-07-25 08:36:33

update: Tested package with 4.1.1.alpha0 and it worked. This could be sensitive to the lisp install but I am not an expert on this. The long path name might also be a problem but this only speculation.


---

Comment by burcin created at 2009-08-05 08:00:25

Could someone comment on the relation between the two pairs of issues:
 - this one, #6318
 - #4461, #4036 ?

Is the package here built on the one at #4461? Are the changes on #4036 independent of the ones at #6318?

Thanks.

Burcin


---

Comment by awebb created at 2009-08-05 08:32:13

Sorry, 
I think there is a bit of cross-posting of tickets. My bad. I did not see the the earlier ones (#4461 and #4036) and with the new versions of fricas it is not clear to me which is now needed. I agree that the axiom and fricas should be separate interfaces although at the moment the fricas interface is a basically a subclass of the axiom one. They are still very similar but it means that to test axiom.py one needs both axiom and fricas installed. 

Adam


---

Comment by awebb created at 2009-08-09 12:52:37

Just a comment. 
#4461 deals with an issue with clisp which is no longer used. It seems that it could just be closed now. 
#4036 are independent of #6318. (I am not sure what they do.)
#6318 fix some interface issues but perhaps should be added after #4036?

As a guess: 1. apply #4036 to a new version (and rebase), 2. apply #6318 and test, 3. check/make a new fricas spkg. 

Adam

PS I will not have computer access for at least a week but can look at it after that if no one else has.


---

Comment by awebb created at 2009-08-17 15:18:56

Replying to [comment:12 burcin]:
> Could someone comment on the relation between the two pairs of issues:
>  - this one, #6318
>  - #4461, #4036 ?
> 
> Is the package here built on the one at #4461? Are the changes on #4036 independent of the ones at #6318?
> 
> Thanks.
> 
> Burcin

The patches at #4036 are already in and I only added a few fricas tests. I would apply #6318 first, then #4036 (trac_4036-axiom_interface.patch only) and of course axiom and fricas need to be installed to test everything.

Adam


---

Comment by hemmecke created at 2009-10-15 00:18:29

Changing status from needs_work to needs_review.


---

Comment by hemmecke created at 2009-10-15 00:18:29

I've created an spkg builder at http://boxen.math.washington.edu:29792 .
This code is not an spkg itself but rather builds two spkg: fricas-VERSION.spkg and fricasaldor-VERSION.spkg. It requires a checkout of the FriCAS sources from SVN at sourceforge.

On sage.math the following should work.

WARNING, before you start compiling FriCAS, you should read the top of the Makefile, in particular the part connected to an X server. It's unwise to have the X server running on a different machine from where you compile the spkg!!! The X server is not needed for actually installing the .spkg into Sage.

Get the FriCAS sources:

```
svn export https://fricas.svn.sourceforge.net/svnroot/fricas/trunk fricas-sources
```


Use the installed Aldor from my HOME (or install aldor from http://www.aldor.org).

```
export ALDORROOT=/home/hemmecke/aldorroot
export PATH=$ALDORROOT/bin:$PATH
```


Make sure you have ecl 9.8.4.

```
export PATH=$SAGE_ROOT/local/bin:$PATH
export LD_LIBRARY_PATH=$SAGE_ROOT/local/lib:$LD_LIBRARY_PATH
hg clone http://boxen.math.washington.edu:29792 fricas-aldor-spkg
cd fricas-aldor-spkg
make
```


Installing FriCAS inside Sage

```
cp fricas-aldor-spkg/spkg/fricas*.spkg  $SAGE_ROOT/spkg/optional
sage -i fricasaldor-VERSION
```


The VERSION of the spkg will automatically be extracted from FriCAS configure script.
VERSION is appropriate if you use a proper release version, i.e. (should work for a release > 1.0.7)

```
svn export https://fricas.svn.sourceforge.net/svnroot/fricas/releases/1.0.8 fricas-sources
```

and running the fricas-aldor-spkg/Makefile will produce VERSION=1.0.8.

Ralf


---

Comment by hemmecke created at 2009-10-15 00:26:39

Ooops, you should give a pointer to the FriCAS sources...
and you will probably have to download some additional files.

```
hg clone http://boxen.math.washington.edu:29792 fricas-aldor-spkg
cd fricas-aldor-spkg
make spadhelp
make noweb
make FRICAS_SRC=../fricas-sources
```



---

Comment by awebb created at 2009-10-15 06:56:29

Hi,

I tried on sage.math and on my own machine. When doing 

```
make spadhelp
make noweb
```


I get messages like: 

```
grep: /home/awebb/configure.ac: No such file or directory
grep: /home/awebb/configure.ac: No such file or directory
```


So it seems to be looking in the wrong place. I then get the following when I try to make.


```
sage subshell$ make FRICAS_SRC=../fricas-sources
mkdir -p build
touch -t 199901010000 build/.dir
(cd build; /home/awebb/test_fricas/fricas-sources/configure --enable-aldor --with-lisp=ecl)
checking build system type... x86_64-unknown-linux
checking host system type... x86_64-unknown-linux
checking target system type... x86_64-unknown-linux
checking for make... make
checking for gcc... gcc
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables...
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking for a BSD-compatible install... /usr/bin/install -c
checking for touch... touch
checking for mktemp... mktemp
checking for gawk... no
checking for mawk... mawk
checking for gtar... no
checking for tar... tar
checking for ranlib... ranlib
checking for ar... ar
checking for latex... /usr/bin/latex
checking for makeindex... makeindex
checking for notangle... no
checking for noweave... no
configure: error: noweb utils and noweb sources missing
make: *** [build/src/aldor/al/libaxiom.al] Error 1
/home/awebb/test_fricas/fricas-aldor-spkg
sage subshell$ ls
build        Makefile  spkg-install.fricas       SPKG.txt.fricas       zips
gpl-3.0.txt  share     spkg-install.fricasaldor  SPKG.txt.fricasaldor
/home/awebb/test_fricas/fricas-aldor-spkg
sage subshell$ 
```


noweb-2.10a.tgz is in the zips directory. Is the script looking in the fricas-sources instead?

Cheers,
Adam


---

Comment by awebb created at 2009-10-18 10:20:20

Changing status from needs_review to needs_work.


---

Comment by awebb created at 2009-11-14 10:22:27

Hi,

I apologize if I misunderstood. My impression was that work was ongoing and packages would be made available when ready.

When I tried making the packages on sage.math I eventually get to the following. 


```
make[3]: Entering directory `/scratch/awebb/fricas-aldor-spkg/build/src/aldor'
Makefile:259: domains.mk: No such file or directory
echo "domains := \\" > domains.mk
echo ')lisp (dolist (c (|allConstructors|)) (format t "~A \\~%" (|constructor?| c))) (quit)'|(DAASE=/scratch/awebb/fricas-aldor-spkg/build/target/x86_64-unknown-linux /scratch/awebb/fricas-aldor-spkg/build/target/x86_64-unknown-linux/bin/AXIOMsys)|grep '\\'|grep -v '.*- \\'|grep -v NIL|sed -e 's/.*-> //'|sort >> domains.mk
echo >> domains.mk
make[3]: Leaving directory `/scratch/awebb/fricas-aldor-spkg/build/src/aldor'
make[3]: Entering directory `/scratch/awebb/fricas-aldor-spkg/build/src/aldor'
svn cat https://svn.origo.ethz.ch/algebraist/trunk/aldor/lib/libax0/axiom.as > axiom.as
svn: /usr/local/sage/local/lib/libcrypto.so.0.9.8: no version information available (required by /usr/lib/libpq.so.5)
svn: /usr/local/sage/local/lib/libssl.so.0.9.8: no version information available (required by /usr/lib/libpq.so.5)
svn: /usr/local/sage/local/lib/libssl.so.0.9.8: no version information available (required by /usr/lib/libneon.so.27)
svn: /usr/local/sage/local/lib/libcrypto.so.0.9.8: no version information available (required by /usr/lib/libneon.so.27)
svn: relocation error: /usr/lib/libneon.so.27: symbol SSL_CTX_set_client_cert_cb, version OPENSSL_0.9.8 not defined in file libssl.so.0.9.8 with link time reference
make[3]: *** [axiom.as] Error 127
make[3]: Leaving directory `/scratch/awebb/fricas-aldor-spkg/build/src/aldor'
make[2]: *** [all-aldor] Error 2
make[2]: Leaving directory `/scratch/awebb/fricas-aldor-spkg/build/src'
make[1]: *** [all-src] Error 2
make[1]: Leaving directory `/scratch/awebb/fricas-aldor-spkg/build'
make: *** [build/src/aldor/al/libaxiom.al] Error 2

```


I will try again on a local machine although my machine is much slower.

Adam


---

Comment by awebb created at 2009-11-14 12:10:49

I got the same result locally.  ~ Adam


---

Comment by awebb created at 2009-11-14 13:42:42

I am not sure what the trouble was but I tried again and made the package. The package without the aldor interface is at http://sage.math.washington.edu/home/awebb/fricas-1.0.8.spkg. It installs and I can start the console.

Adam


---

Comment by hemmecke created at 2009-11-14 18:54:00

Replying to [comment:22 awebb]:

> I apologize if I misunderstood. My impression was that work was ongoing and packages would be made available when ready.

Yes, that was the plan, and I volunteer to be the maintainer of the spkg-builder.
The fricasaldor stuff is just a question of time.
 
> When I tried making the packages on sage.math I eventually get to the following. 
> {{{
> svn cat https://svn.origo.ethz.ch/algebraist/trunk/aldor/lib/libax0/axiom.as > axiom.as
> svn: /usr/local/sage/local/lib/libcrypto.so.0.9.8: no version information available (required by /usr/lib/libpq.so.5)
> }}}

I also experienced that, but this must be a problem with "sage -sh". One doesn't get such wierd messages when you simply do as I described above. In particular not 'sage -sh' but just

```
export PATH=$SAGE_ROOT/local/bin:$PATH
export LD_LIBRARY_PATH=$SAGE_ROOT/local/lib:$LD_LIBRARY_PATH
```



---

Comment by hemmecke created at 2009-11-14 18:58:04

Replying to [comment:24 awebb]:
> http://sage.math.washington.edu/home/awebb/fricas-1.0.8.spkg. It installs and I can start the console. 
If it works, someone should upload it to http://sagemath.org/packages/optional/ .
What is the workflow to get the package into the "optional" archive?


---

Comment by awebb created at 2009-11-14 19:34:24

Changing status from needs_work to needs_review.


---

Comment by awebb created at 2009-11-14 19:34:24

I think it just needs to be reviewed. If it works then it should be set to 'positive review' and then the current release manager looks at it. If they are happy than they put it in the optional packages. The package works for me and I ran a quick test from inside sage so I would give it a positive review. If the package also works for you than I guess the status can be changed. BTW I used sage 4.2.1.alpha0 for building the package and testing it. This includes ecl 9.10.2.

Adam


---

Comment by was created at 2009-11-17 06:38:06

Replying to [comment:27 awebb]:
> I think it just needs to be reviewed. If it works then it should be set to 'positive review' and then the current release manager looks at it. If they are happy than they put it in the optional packages. The package works for me and I ran a quick test from inside sage so I would give it a positive review. If the package also works for you than I guess the status can be changed. BTW I used sage 4.2.1.alpha0 for building the package and testing it. This includes ecl 9.10.2.
> 
> Adam

Exactly right.


---

Comment by drkirkby created at 2009-11-19 22:22:06

I just tried it on Solaris, and it fails very quickly:



```

fricas-1.0.8/src/src/ChangeLog.bu
fricas-1.0.8/src/confignotes.tex
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/usr/local/gcc-4.4.1-sun-linker/bin/gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: ../gcc-4.4.1/configure --prefix=/usr/local/gcc-4.4.1-sun-linker/ --with-as=/usr/ccs/bin/as --without-gnu-as --with-ld=/usr/ccs/bin/ld --without-gnu-ld --enable-languages=c,c++,fortran --with-mpfr-include=/usr/local/include --with-mpfr-lib=/usr/local/lib --with-gmp-include=/usr/local/include --with-gmp-lib=/usr/local/lib CC=/usr/sfw/bin/gcc CXX=/usr/sfw/bin/g++ LDFLAGS='-R /usr/local/lib -L /usr/local/lib'
Thread model: posix
gcc version 4.4.1 (GCC) 
****************************************************
checking build system type... sparc-sun-solaris2.10
checking host system type... sparc-sun-solaris2.10
checking target system type... sparc-sun-solaris2.10
checking for gmake... make
GNU Make 3.80
checking for gcc... /usr/local/gcc-4.4.1-sun-linker/bin/gcc
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables... 
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether /usr/local/gcc-4.4.1-sun-linker/bin/gcc accepts -g... yes
checking for /usr/local/gcc-4.4.1-sun-linker/bin/gcc option to accept ISO C89... none needed
checking for a BSD-compatible install... /usr/local/bin/ginstall -c
checking for touch... touch
checking for mktemp... mktemp
checking for gawk... no
checking for mawk... no
checking for nawk... nawk
checking for gtar... gtar
checking for ranlib... ranlib
checking for ar... ar
checking for latex... no
checking for makeindex... no
checking for bash... /usr/bin/bash
checking for notangle... no
checking for noweave... no
axiom_build_bindir = /export/home/drkirkby/sage-4.2/spkg/build/fricas-1.0.8/build-dir/build/sparc-sun-solaris2.10/bin
checking Lisp implementation... ../src/configure: line 3955: ecl: command not found
Can't open config_cl.out
configure: error: Unable to determine Lisp flavor
***********************************************************
Failed to configure FriCAS.
***********************************************************

real    0m2.871s
user    0m0.924s
sys     0m1.561s
sage: An error occurred while installing fricas-1.0.8

```



---

Comment by drkirkby created at 2009-11-19 22:28:56

Oops, ignore that comment. I realised I downloaded the package into an incomplete build of Sage. 

Dave


---

Comment by hemmecke created at 2009-11-19 22:37:20

Replying to [comment:29 drkirkby]:
> I just tried it on Solaris, and it fails very quickly:

```
checking Lisp implementation... ../src/configure: line 3955: ecl: command not found
```


The error message says it all. And http://boxen.math.washington.edu:29792/file/25ab4f31480e/SPKG.txt.fricas#l1 also lists ecl as a dependency.

If there were a proper package management in Sage, I would have made ecl a formal dependency, but adding "sage -i ecl-9.8.4" to the install script is also not fool proof, since specifying a version number is bad. Giving no version number is bad as well. I'd rather wish to be able to specify a range of versions that should work for the fricas-1.0.8.
Try 

```
sage -i http://sage.math.washington.edu/home/hemmecke/pub/ecl-9.8.4.spkg
```



---

Comment by mhansen created at 2009-11-20 05:42:08

Resolution: fixed


---

Comment by mhansen created at 2009-11-20 05:42:08

I've merged this into the optional packages.


---

Comment by hemmecke created at 2010-06-17 11:17:20

FriCAS 1.0.9 and FriCAS-Aldor is available from

[http://sage.math.washington.edu/home/hemmecke/pub/fricas-1.0.9.spkg](http://sage.math.washington.edu/home/hemmecke/pub/fricas-1.0.9.spkg)

[http://sage.math.washington.edu/home/hemmecke/pub/fricasaldor-1.0.9.spkg](http://sage.math.washington.edu/home/hemmecke/pub/fricasaldor-1.0.9.spkg)


---

Comment by hemmecke created at 2010-06-17 15:07:01

Changing status from closed to new.


---

Comment by hemmecke created at 2010-06-17 15:07:01

Resolution changed from fixed to 


---

Comment by hemmecke created at 2010-06-17 15:08:11

Changing status from new to needs_review.


---

Comment by awebb created at 2010-06-18 06:56:42

Thanks for the packages. I guess it is mentioned somewhere that installing fricasaldor depends on the source of fricas. This means that the following is needed:

```
sage -i -s fricas-1.0.9.spkg
sage -i fricasaldor-1.0.9.spkg
```

I had a problem with an example for fricasaldor. 

```
(1) -> )co fib.as
   Compiling FriCAS source code from file /home/math/test/fib.as using
      AXIOM-XL compiler and options
-O -Fasy -Fao -Flsp -laxiom -Mno-ALDOR_W_WillObsolete -DAxiom -Y $AXIOM/algebra -I $AXIOM/algebra
      Use the system command )set compiler args to change these
      options.
   Compiling Lisp source code from file fib.lsp
   Issuing )library command for fib
   Reading /home/math/test/fib.asy
(1) -> fib 5

   >> System error:
   Error when using UNREAD-CHAR on stream #<string-input stream from "3(1) ->
```


where fib.as is

```
#include "axiom"
fib(n: Integer): Integer == {
        n < 0 => 0;
	n < 3 => 1;
	fib(n-1) + fib(n-2);
}
```


I get get this with ecl but not with sbcl but I think this is a known problem. Another example with a simple factorial function worked. I did some simple things and the fricas package seemed to work fine.

Adam


---

Comment by awebb created at 2010-06-18 07:14:35

There seems to be an API change. A few tests fail in the Sage interface. This is now ticket #9258. It appears to be a change in the return string. Note that these tests still work for axiom.

Adam


---

Comment by hemmecke created at 2010-06-18 07:46:16

Replying to [comment:37 awebb]:
> Thanks for the packages. I guess it is mentioned somewhere that installing fricasaldor depends on the source of fricas. This means that the following is needed:
> {{{
> sage -i -s fricas-1.0.9.spkg
> sage -i fricasaldor-1.0.9.spkg
> }}}

That is *not* so! As explained [above](http://trac.sagemath.org/sage_trac/ticket/6517#comment:17), the commands are simply:


```
cp fricas-aldor-spkg/spkg/fricas*.spkg  $SAGE_ROOT/spkg/optional
sage -i fricasaldor-X.Y.Z
```


Dependency is included in the package fricasaldor.

> I had a problem with an example for fricasaldor. 
> {{{
> (1) -> )co fib.as
>    Compiling FriCAS source code from file /home/math/test/fib.as using
>       AXIOM-XL compiler and options
> -O -Fasy -Fao -Flsp -laxiom -Mno-ALDOR_W_WillObsolete -DAxiom -Y $AXIOM/algebra -I $AXIOM/algebra
>       Use the system command )set compiler args to change these
>       options.
>    Compiling Lisp source code from file fib.lsp
>    Issuing )library command for fib
>    Reading /home/math/test/fib.asy
> (1) -> fib 5
> 
>    >> System error:
>    Error when using UNREAD-CHAR on stream #<string-input stream from "3(1) ->
> }}}

> I get get this with ecl but not with sbcl but I think this is a known problem.

Yes that seems to be an ecl problem and I have no idea how to track that. So unfortunately, I cannot fix it. I think the link to Aldor is not as stable as it should be. There might also be a problem on 64bit machines with respect to internal hash codes. But since the Aldor sources are not free, it's up to a person who agrees with the Aldor Public License 2.0 to sync with FriCAS.

Ralf


---

Comment by awebb created at 2010-06-18 10:12:54

Replying to [comment:39 hemmecke]:

> 
> That is *not* so! As explained [above](http://trac.sagemath.org/sage_trac/ticket/6517#comment:17), the commands are simply:
> 
> {{{
> cp fricas-aldor-spkg/spkg/fricas*.spkg  $SAGE_ROOT/spkg/optional
> sage -i fricasaldor-X.Y.Z
> }}}
> 
> Dependency is included in the package fricasaldor.

I got the following when installing fricasaldor. The message says that the build directory is missing so I assumed that I had made a mistake. 



```
****************************************************
Installing -s fricas-1.0.9
Calling sage-spkg on fricas-1.0.9
Warning: Attempted to overwrite SAGE_ROOT environment variable
fricas-1.0.9
Machine:
Linux haso220w 2.6.18-92.1.6.el5 #1 SMP Wed Jun 25 12:46:39 EDT 2008 i686 i686 i386 GNU/Linux
sage: /home/math/sage/spkg/build/fricasaldor-1.0.9/fricas-1.0.9 is already installed
grep: /home/math/sage/spkg/build/fricas-1.0.9/spkg-install: No such file or directory
cp: cannot create regular file `/home/math/sage/spkg/build/fricas-1.0.9/build-dir/src/aldor/': No such file or directory
mkdir: cannot create directory `/home/math/sage/spkg/build/fricas-1.0.9/build-dir/src/aldor/al': No such file or directory
cp: cannot create regular file `/home/math/sage/spkg/build/fricas-1.0.9/build-dir/src/aldor/al': No such file or directory
./spkg-install: line 60: cd: /home/math/sage/spkg/build/fricas-1.0.9/build-dir: No such file or directory
./spkg-install: line 61: /home/math/sage/spkg/build/fricas-1.0.9/src/configure: No such file or directory
***********************************************************
Failed to configure FriCAS-Aldor interface.
***********************************************************
```



Adam


---

Comment by awebb created at 2010-06-18 10:13:45

Replying to [comment:39 hemmecke]:

> Yes that seems to be an ecl problem and I have no idea how to track that. So unfortunately, I cannot fix it. I think the link to Aldor is not as stable as it should be. There might also be a problem on 64bit machines with respect to internal hash codes. But since the Aldor sources are not free, it's up to a person who agrees with the Aldor Public License 2.0 to sync with FriCAS.
> 
> Ralf

I agree

Adam


---

Comment by hemmecke created at 2010-06-18 10:27:44

> > Dependency is included in the package fricasaldor.
 
> I got the following when installing fricasaldor. The message says that the build directory is missing so I assumed that I had made a mistake. 

Yes. The whole problem is due to the Aldor Public License 2. :-( That's the only reason why there are two packages. The fricas spkg is mBSD and the fricasaldor spkg is APL2.
The other problem is that Sage does not provide a proper mechanism to deal with dependencies. (People should look at "zc.buildout".)

It's all not so easy since currently fricasaldor needs the build directory of the build of the fricas package. It basically copies copies some files into this directory and then starts the build.

So saying

```
sage -i fricas-X.Y.Z
sage -i fricasaldor-X.Y.Z
```

will not work, because the build directory of fricas is gone. I guess that might be the problem with your error.

The other thing is
> {{{
> ****************************************************
> Installing -s fricas-1.0.9
> Calling sage-spkg on fricas-1.0.9
> Warning: Attempted to overwrite SAGE_ROOT environment variable
> }}}
Do you have an idea who is printing that warning?


---

Comment by awebb created at 2010-06-18 10:56:47

Replying to [comment:42 hemmecke]:

> It's all not so easy since currently fricasaldor needs the build directory of the build of the fricas package. It basically copies copies some files into this directory and then starts the build.
> 
> So saying
> {{{
> sage -i fricas-X.Y.Z
> sage -i fricasaldor-X.Y.Z
> }}}
> will not work, because the build directory of fricas is gone. I guess that might be the problem with your error.

Exactly, 

```
sage -i -s fricas-X.Y.Z
sage -i fricasaldor-X.Y.Z
```


This worked for me since the -s keeps the build directory in the first step. 

> 
> The other thing is
> > {{{
> > ****************************************************
> > Installing -s fricas-1.0.9
> > Calling sage-spkg on fricas-1.0.9
> > Warning: Attempted to overwrite SAGE_ROOT environment variable
> > }}}
> Do you have an idea who is printing that warning?

I think I see it everytime I use sage -i to install something. I assume that it is part of the Sage installing process somewhere. I don't know why the SAGE_ROOT would need to be changed though.


---

Comment by awebb created at 2010-06-19 12:07:56

I am not sure of the procedure of who should give the positive review and in any case several people should look at it. As I have not been very active lately I will just give a comment. This seems to be a simple upgrade of two optional packages and so I don't have any major concerns. I installed the packages on two Linux systems (32 bit SL 5.1, 64 bit Ubuntu 10.04) and ran some tests without severe problems (small issues noted above). I am aware that there are problems with the Sage interface but I think that is a separate issue. Therefore, I would give the packages a positive review.

Adam


---

Comment by mhansen created at 2010-06-27 20:07:46

Resolution: fixed


---

Comment by mhansen created at 2010-06-27 20:07:46

These look good to me.  I've made a new ticket at #9354 -- please don't reopen this ticket once it has been closed.  I'll post a fix to the issues at #9258.
