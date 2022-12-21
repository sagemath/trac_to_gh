# Issue 7115: building cliquer Cython extension fails on OS X 10.4 PPC (with cliquer-1.2.p0.spkg)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-04 17:34:39

Assignee: tbd

CC:  georgsweber kcrisman


```
building 'sage.graphs.cliquer' extension
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/home/wstein/screen/varro/build/sage-4.1.2.rc
1.alpha1/local//include -I/home/wstein/screen/varro/build/sage-4.1.2.rc1.alpha1/local//include/csage -I/home/wstein/screen
/varro/build/sage-4.1.2.rc1.alpha1/devel//sage/sage/ext -I/home/wstein/screen/varro/build/sage-4.1.2.rc1.alpha1/local/incl
ude/python2.6 -c sage/graphs/cliquer.c -o build/temp.macosx-10.3-ppc-2.6/sage/graphs/cliquer.o -w
gcc -L/home/wstein/screen/varro/build/sage-4.1.2.rc1.alpha1/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-
10.3-ppc-2.6/sage/graphs/cliquer.o -L/home/wstein/screen/varro/build/sage-4.1.2.rc1.alpha1/local//lib -lcsage -lcliquer -l
stdc++ -lntl -o build/lib.macosx-10.3-ppc-2.6/sage/graphs/cliquer.so
/usr/libexec/gcc/powerpc-apple-darwin8/4.0.1/ld: can't locate file for: -lcliquer
collect2: ld returned 1 exit status
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.

ERROR installing SAGE

real    32m56.224s
user    27m12.748s
sys     2m58.301s
sage: An error occurred while installing sage-4.1.2.rc1.alpha1


varro:~/screen/varro/build/sage-4.1.2.rc1.alpha1 wstein$ ls spkg/installed/*cliq*
spkg/installed/cliquer-1.2.p0
```





---

Comment by GeorgSWeber created at 2009-10-05 10:54:12

That will most likely fail on MacIntel OS X 10.4, too (what about OS X 10.5, 10.6 ?!?).


---

Comment by GeorgSWeber created at 2009-10-05 21:13:39

On my MacIntel with OS X 10.4, some "libcliquer.so" is built by the "cliquer-1.2.p0.spkg" introduced by #6681, instead of a "libcliquer.dylib". 
Duh.


---

Comment by GeorgSWeber created at 2009-10-05 21:43:52

I'm pretty stunned. In the Makefile we explicitly have:

```
cl: cl.o cliquer.o graph.o reorder.o
	$(CC) $(LDFLAGS) $(SAGESOFLAGS) -o libcliquer.so cl.o cliquer.o graph.o reorder.o
```

so, no .dylib is to built (nor a .dll on Cygwin, if that would matter), but explicitly some file with the .so ending; and the SAGESOFLAGS are set to:

```
elif [ `uname` = "Darwin" ]; then
    SAGESOFLAGS="-shared -dynamiclib"
    export SAGESOFLAGS
```

with which on at least my MacIntel with OS X 10.4 and the newest Xcode to be had for this platform (v2.5), the compiler barfs:

```
gcc  -L/Users/Shared/sage/sage-4.1.2.alpha4/local/lib  -shared -dynamiclib -o libcliquer.so cl.o cliquer.o graph.o reorder.o
i686-apple-darwin8-gcc-4.0.1: unrecognized option '-shared'
```

although it does produce some "libcliquer.so" file, and the makefile seems to exit with 0, pretending everything would be OK.

How could that possibly have worked on Mac OS X 10.6? Probably due to the GCC 4.0.1 --> 4.2.x change, but the latter is not available under Mac OS X 10.4.

Can we back out cliquer-1.2.p0.spkg and revert to cliquer-1.2.spkg (re-opening #6681 as "needs work")?


---

Comment by GeorgSWeber created at 2009-10-05 22:02:11

Strange, even the copy command:

```
cp -f *.h "$SAGE_LOCAL/include/cliquer/"
cp -f libcliquer.so "$SAGE_LOCAL/lib/"
```

explicitly references the .so file, and not some .dylib. At least on my Mac, this results in many errors on startup like:

```
ImportError: dlopen(/Users/Shared/sage/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/graphs/cliquer.so, 2): Library not loaded: libcliquer.dylib
  Referenced from: /Users/Shared/sage/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/graphs/cliquer.so
  Reason: image not found
```

Again, if that ever worked on Mac OS X 10.6 --- then Snow Leopard now accepts .so libraries, not only .dylib libraries (even for dynamic linking at run-time). Beautiful.

I think I now know how to make up a cliquer-1.2.p1.spkg which works on "non-Snow Leopard" Macs, but it's midnight again, and I stop here.


---

Attachment

patch against cliquer-1.2.p0.spkg (root hg repo)


---

Comment by GeorgSWeber created at 2009-10-06 22:24:30

With a bit luck, the attached patch to "spkg-install" already might do the job. But it's totally untested yet, and I can't test it myself on e.g. Mac OS X 10.5 or 10.6 anyway. Could somebody take over?


---

Comment by kcrisman created at 2009-10-07 14:34:00

Okay, here's the results.

```
Finished extraction
****************************************************
Host system
uname -a:
Darwin <snip>-powerbook-g4-110.local 8.11.0 Darwin Kernel Version 8.11.0: Wed Oct 10 18:26:00 PDT 2007; root:xnu-792.24.17~1/RELEASE_PPC Power Macintosh powerpc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: powerpc-apple-darwin8
Configured with: /var/tmp/gcc/gcc-5370~2/src/configure --disable-checking -enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-slibdir=/usr/lib --build=powerpc-apple-darwin8 --host=powerpc-apple-darwin8 --target=powerpc-apple-darwin8
Thread model: posix
gcc version 4.0.1 (Apple Computer, Inc. build 5370)
****************************************************
Code will be built with debugging information present. Set 'SAGE_DEBUG' to 'no' if you don't want that.
No Fortran compiler has been defined. This is not normally a problem.
Using CC=gcc
Using CXX=g++
Using FC=
Using F77=
Using SAGE_FORTRAN=
Using SAGE_FORTRAN_LIB=
The following environment variables will be exported
Using CFLAGS= -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC 
Using CXXFLAGS= -O2  -g  -Wall 
Using FCFLAGS= -O2  -g  -Wall 
Using F77FLAGS= -O2  -g  -Wall 
Using CPPFLAGS= -I/Users/<snip>/Desktop/sage-4.1.2.rc1.alpha3/local/include 
Using LDFLAGS= -L/Users/<snip>/Desktop/sage-4.1.2.rc1.alpha3/local/lib 
Using ABI=
configure scripts and/or makefiles might override these later
 
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/Users/<snip>/Desktop/sage-4.1.2.rc1.alpha3/local/include   -c -o cliquer.o cliquer.c
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/Users/<snip>/Desktop/sage-4.1.2.rc1.alpha3/local/include   -c -o graph.o graph.c
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/Users/<snip>/Desktop/sage-4.1.2.rc1.alpha3/local/include   -c -o reorder.o reorder.c
gcc  -L/Users/<snip>/Desktop/sage-4.1.2.rc1.alpha3/local/lib  -dynamiclib -single_module -flat_namespace -undefined dynamic_lookup -o libcliquer.so cl.o cliquer.o graph.o reorder.o
ld: flag: -undefined dynamic_lookup can't be used with MACOSX_DEPLOYMENT_TARGET environment variable set to: 10.1
/usr/libexec/gcc/powerpc-apple-darwin8/4.0.1/libtool: internal link edit command failed
make[2]: *** [cl] Error 1
Failed to compile cliquer... exiting

real    0m4.676s
user    0m3.687s
sys     0m0.439s
sage: An error occurred while installing cliquer-1.2.p0
```


More specifically:

```
-undefined dynamic_lookup can't be used with MACOSX_DEPLOYMENT_TARGET environment variable set to: 10.1
```


Any ideas?  I think maybe reverting the spkg might be the way to go if the mpfr problem can be resolved.


---

Comment by kcrisman created at 2009-10-07 14:43:46

Turns out this is something one can fix, since the default is "not to create weak links" or something like that.  See e.g. [http://web.mit.edu/darwin/src/modules/cctools/RelNotes/CompilerTools.html](http://web.mit.edu/darwin/src/modules/cctools/RelNotes/CompilerTools.html).   I'm going to try something with that, though I understand very little about build variables.


---

Comment by kcrisman created at 2009-10-07 15:02:18

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-10-07 15:02:18

This change to spkg-install works.  I don't know how to make a patch on something outside the main Sage tree, I'm sorry.

```
# Flags for building a dynamically linked shared object.
SAGESOFLAGS=" "
if [ `uname` = "Linux" ]; then
    SAGESOFLAGS="-shared -Wl,-soname,libcliquer.so"
    export SAGESOFLAGS
elif [ `uname` = "Darwin" ]; then
    MACOSX_DEPLOYMENT_TARGET="10.3"
    export MACOSX_DEPLOYMENT_TARGET
    SAGESOFLAGS="-dynamiclib -single_module -flat_namespace -undefined dynamic_lookup"
    export SAGESOFLAGS
elif [ `uname` = "SunOS" ]; then
    SAGESOFLAGS="-G -Bdynamic"
    export SAGESOFLAGS
else
    # We exit here, since we are possibly on an unsupported platform.
    echo "Cannot determine your platform or it is not supported... exiting"
    exit 1
fi
```

The reason this never came up before is because only Python, of all the spkgs, does anything like this (do a grep to see).  And I guess it didn't come up on cliquer before because of the use of Scons, whatever that is?


---

Attachment

And it goes without saying that the change to the end of the file by gsw was still necessary as well.\


---

Comment by GeorgSWeber created at 2009-10-07 21:18:27

It does feel good to be part of a team!

I created a new spkg (with the adapted "spkg-install" as above, and updated "SPKG.txt" and hg repo), here it is:
http://sage.math.washington.edu/home/weberg/spkg/cliquer-1.2.p1.spkg
Tested successfully on both MacIntel OS X 10.4 and MacPPC OS X 10.4, and also:

```
sage -t -long "devel/sage/sage/graphs/cliquer.pyx"          
         [8.3 s]
 
----------------------------------------------------------------------
All tests passed!
```


Two final remarks. I work often from the command line (more precisely: bash shell), started with "./sage -sh" in the root directory of the Sage version I want to work with. Issuing "hg" then fires up exactly the hg of the respective Sage install. I don't even have a system-wide hg installation. Mercurial repositories are also used in spkg's. Just use "sage -f -s foobar.spkg" to leave the spkg resp. its contents undeleted in spkg/build/foobar/. "cd" there and do "hg export default" to see the latest commit checked in. After doing some changes (and checking with "hg diff" what I would check in ...), I do firstly

```
hg commit -m "fix for trac ticket #12345"
```

and if then, I want to create a patch (and not the spkg as a whole), I do what I do usually for Sage library patches, too:

```
hg export default >> ../../../../patches/trac_12345.patch
```

Secondly, regarding the MACOSX_DEPLOYMENT_TARGET="10.3" thing: I knew that essentially. However, I was not working on my clean-room OS partition, but from my work installation. There I have MACOSX_DEPLOYMENT_TARGET="10.4" in my .bashrc file, because it was so annoying to add it every now and again. So I simply forgot about that, sorry! If you take any "install.log" from a recent Sage install on Mac OS X, and search for "-undefined dynamic_lookup", you'll find tons of occurences. There seems to by another method to tell the compiler that it is OK to use this, by adding this option to the other linker options:

```
 -mmacosx-version-min=10.4
```

Probably that way is the better way in light of cross-compiling Sage (if we ever will get to this anytime soon).


---

Comment by kcrisman created at 2009-10-08 00:31:25

Ironically, I encountered one problem.  At startup when Sage tried to import * from sage.graphs.cliquer, it couldn't find graphs/cliquer.so.  I had to change the end to the following:

```
if [ `uname` = "Darwin" ]; then
    cp -f libcliquer.so "$SAGE_LOCAL/lib/libcliquer.dylib"
fi

cp -f libcliquer.so "$SAGE_LOCAL/lib/"
```

That is, I copied both the dylib and the so files.  And then after sage -f the spkg again, all was well.  But then I rethought it, and tried what I already posted again, and it didn't seem to affect things.  The problem is that I don't understand enough about such things to know whether this is worrisome.

On the 10.3 etc. thing, I agree that the other option is probably better.  I'm just amazed that I found anything useful at all on the Internet about this!

I can try to compile this again with your spkg, I suppose, but I want to point out that it will take the better part of 8 hours.  You might want to email William or someone else who is doing a lot of tests to see if they can check to make sure this compiles fine on e.g. Solaris, Snow Leopard.  Who knows what havoc it might cause?  Though I hope it won't be too bad.

Also, if you know a little about shell script, can you take a look at #7107?  I think it solves the problem, but needs someone who knows something to put it together.


---

Comment by was created at 2009-10-12 04:51:25

Resolution: fixed
