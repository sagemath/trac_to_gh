# Issue 9221: update matplotlib to svn and clean out the patches

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-06-11 21:35:44

Assignee: jason, was

CC:  drkirkby kcrisman

Matplotlib SVN 8415 has some bugfixes and enhancements that are really nice for us.  For example, the configuration variables allow us to eliminate most of our patches to the spkg, and a new path.snap config parameter solves #7808.

The spkg is up at http://sage.math.washington.edu/home/jason/matplotlib-0.99.3-svn8415.spkg, and builds on the spkg in #9202.


---

Comment by jason created at 2010-06-11 21:38:40

The SVN spkg does not compile on Solaris.  See the issues with header files reported at the end of #9202.


---

Comment by jason created at 2010-06-11 21:38:40

Changing status from new to needs_work.


---

Comment by jason created at 2010-06-11 21:38:46

Changing status from needs_work to needs_info.


---

Comment by jason created at 2010-07-07 05:22:01

David, can you check to see if this spkg compiles on Solaris, or if we need to still address the issues at the end of #9202?


---

Comment by jason created at 2010-07-07 05:23:52

See what's new at: http://matplotlib.sourceforge.net/users/whats_new.html


---

Comment by jason created at 2010-07-07 05:35:02

This was in the log, so I think this should compile on Solaris now:


```
2010-07-02 Modified CXX/WrapPython.h to fix "swab bug" on solaris so
           mpl can compile on Solaris with CXX6 in the trunk.  Closes
           tracker bug 3022815 - JDH
```



---

Comment by drkirkby created at 2010-07-07 08:18:45

Changing status from needs_info to needs_work.


---

Comment by drkirkby created at 2010-07-07 08:18:45

Replying to [comment:6 jason]:
> This was in the log, so I think this should compile on Solaris now:
> 
> {{{
> 2010-07-02 Modified CXX/WrapPython.h to fix "swab bug" on solaris so
>            mpl can compile on Solaris with CXX6 in the trunk.  Closes
>            tracker bug 3022815 - JDH
> }}}

No such luck. I've tried on both Solaris 10 on SPARC, and OpenSolaris on x64. It looks like a mix of compilation modes is causing them to get two different definitions for _swab_. 

The bug tracker suggests this was a very recent fix, so may not have made it into 1.0. If if did make it into 1.0, then it failed to solve the problem. 

## Solaris 10 update with Sun UltraSPARC T2+ processors

 * Sun T5240
 * 2 x 8 core, 64-thread UltraSPARC T2+ 1167 MHz
 * 32 GB RAM
 * Solaris 10 update 7 (05/09)
 * t2.math.washtington.edu
 * gcc 4.4.1 configured to use both the Sun linker and assembler. 
 * A build of sage-4.5.alpha4 was used to test matplotlib-1.0.0.spkg
 * MD5 checksum of matplotlib-1.0.0.spkg was cb9f3cb0ec3da550d2d67ea7e8b6094f 
 * 32-bit build (This is the default). The environment variable `SAGE64` was *not* used. 


```
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -Isrc -Iagg24/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include/freetype2 -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/include/python2.6 -c agg24/src/agg_vcgen_dash.cpp -o build/temp.solaris-2.10-sun4v-2.6/agg24/src/agg_vcgen_dash.o
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -Isrc -Iagg24/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include/freetype2 -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/include/python2.6 -c agg24/src/agg_image_filters.cpp -o build/temp.solaris-2.10-sun4v-2.6/agg24/src/agg_image_filters.o
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -Isrc -Iagg24/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/tmp/kirkby/sage-4.5.alpha4/local/include/freetype2 -I/tmp/kirkby/sage-4.5.alpha4/local/include -I. -I/tmp/kirkby/sage-4.5.alpha4/local/include/python2.6 -c src/backend_agg.cpp -o build/temp.solaris-2.10-sun4v-2.6/src/backend_agg.o
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from /tmp/kirkby/sage-4.5.alpha4/local/include/python2.6/Python.h:8,
                 from ./CXX/WrapPython.h:61,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/backend_agg.cpp:10:
/tmp/kirkby/sage-4.5.alpha4/local/include/python2.6/pyconfig.h:1013:1: warning: "_FILE_OFFSET_BITS" redefined
In file included from /usr/include/sys/types.h:18,
                 from /tmp/kirkby/sage-4.5.alpha4/local/include/zconf.h:364,
                 from /tmp/kirkby/sage-4.5.alpha4/local/include/zlib.h:34,
                 from /tmp/kirkby/sage-4.5.alpha4/local/include/png.h:470,
                 from src/backend_agg.cpp:3:
/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/sys/feature_tests.h:197:1: warning: this is the location of the previous definition
In file included from /tmp/kirkby/sage-4.5.alpha4/local/include/python2.6/Python.h:42,
                 from ./CXX/WrapPython.h:61,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/backend_agg.cpp:10:
/usr/include/stdlib.h:144: error: declaration of C function ‘void swab(const char*, char*, ssize_t)’ conflicts with
/usr/include/unistd.h:496: error: previous declaration ‘void swab(const void*, void*, ssize_t)’ here
error: command 'gcc' failed with exit status 1
Error building matplotlib package.

real    3m35.224s
user    3m20.924s
sys     0m9.504s
sage: An error occurred while installing matplotlib-1.0.0
```


## OpenSolaris 2009.06 on x64 hardware

 * Sun Ultra 27 
 * 1 x 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads.
 * 12 GB RAM
 * OpenSolaris 2009.06 snv_134 X86
 * gcc 4.4.4 configured to use the Sun linker and GNU assembler. 
 * A build of sage-4.5.alpha4 was used to test matplotlib-1.0.0.spkg
 * 64-bit build. OpenSolaris defaults to 32-bit, but the environment variable `SAGE64=yes` was used.
 * MD5 checksum of matplotlib-1.0.0.spkg was cb9f3cb0ec3da550d2d67ea7e8b6094f

```
gcc -DNDEBUG -g -O3 -m64 -Wall -Wstrict-prototypes -O2 -g -m64 -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/export/home/drkirkby/sage-4.5.alpha4/local/include -I. -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -Isrc -Iagg24/include -I. -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include -I/export/home/drkirkby/sage-4.5.alpha4/local/include -I. -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include/freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/include/freetype2 -I./freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include/freetype2 -Isrc/freetype2 -Iagg24/include/freetype2 -I./freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/lib/python2.6/site-packages/numpy/core/include/freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/include/freetype2 -I./freetype2 -I/export/home/drkirkby/sage-4.5.alpha4/local/include/python2.6 -c src/backend_agg.cpp -o build/temp.solaris-2.11-i86pc-2.6/src/backend_agg.o
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from /export/home/drkirkby/sage-4.5.alpha4/local/include/python2.6/Python.h:42,
                 from ./CXX/WrapPython.h:61,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/backend_agg.cpp:10:
/usr/include/stdlib.h:159: error: declaration of C function 'void swab(const char*, char*, ssize_t)' conflicts with
/usr/include/unistd.h:513: error: previous declaration 'void swab(const void*, void*, ssize_t)' here
src/backend_agg.cpp: In member function 'Py::Object RendererAgg::draw_markers(const Py::Tuple&)':
src/backend_agg.cpp:727: warning: dereferencing type-punned pointer will break strict-aliasing rules
src/backend_agg.cpp:727: warning: dereferencing type-punned pointer will break strict-aliasing rules
src/backend_agg.cpp:763: warning: dereferencing type-punned pointer will break strict-aliasing rules
src/backend_agg.cpp:763: warning: dereferencing type-punned pointer will break strict-aliasing rules
error: command 'gcc' failed with exit status 1
Error building matplotlib package.

real	0m19.778s
user	0m17.826s
sys	0m1.441s
sage: An error occurred while installing matplotlib-1.0.0
```



---

Comment by jason created at 2010-07-07 14:46:52

Well, the log I posted was from the changelog for 1.0.0, so it certainly look like the fix had made it in.  I'll try looking at this soon.

Also, the spkg I posted above needs:

 * an updated SPKG.txt file
 * long doctests run

before it is officially ready for review.


---

Comment by jason created at 2010-07-07 15:26:37

David,

I verified that the md5 you reported is for the right spkg and contains the fix.  If you have time, could you download the vanilla matplotlib source and try compiling that, just to make sure it isn't a problem with the Sage environment?  The 1.0.0 source is here:

https://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.0/  (I can't test this URL; it isn't loading for me...)

The installation instructions are here:

http://matplotlib.sourceforge.net/users/installing.html

and basically are:


```
cd matplotlib
python setup.py build
python setup.py install
```


I've also posted a report to https://sourceforge.net/mailarchive/forum.php?thread_name=4C349BDE.4020604%40creativetrax.com&forum_name=matplotlib-devel


---

Comment by jason created at 2010-07-18 06:12:44

The patch at #9211 (correcting behavior where vertices in graphs are clipped) depends on this spkg.


---

Comment by jason created at 2010-08-13 17:02:57

The patch needs to be applied so that axes labels come out okay.  Compare the results of

plot(x, (x,-3,3), axes_labels=['x','y'])

before and after to check this.


---

Comment by jason created at 2010-08-14 05:19:55

David,

Could you test compiling the vanilla matplotlib 1.0 source on solaris to see if the issue is in the vanilla upstream package?

Just download from http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.0/matplotlib-1.0.0.tar.gz/download

Then untar and do:


```
cd matplotlib
python setup.py build
python setup.py install
```


(or use `sage -python` if you want to install into a Sage version of python).


---

Comment by jason created at 2010-08-14 05:20:34

For reference, here is the mailing list post where John Hunter discusses the fix that he hoped fixed the bug:  http://www.mail-archive.com/matplotlib-users`@`lists.sourceforge.net/msg17531.html


---

Comment by drkirkby created at 2010-08-14 07:58:02

It's not so easy to test the upstream source code directly, as there are dependencies which are not provided on Solaris. On 't2.math' I get:


```
kirkby`@`t2:32 ~/matplotlib-1.0.0$ python setup.py build
basedirlist is: ['/usr/local']
============================================================================
BUILDING MATPLOTLIB
            matplotlib: 1.0.0
                python: 2.4.4 (#1, Jan 10 2007, 01:25:01) [C]
              platform: sunos5

REQUIRED DEPENDENCIES
                 numpy: no
                        * You must install numpy 1.1 or later to build
                        * matplotlib.
```


But Numpy has a whole list of dependencies of its own, so I don't want to spend a long time setting that lot up. 

But I just retried your .spkg on 't2' using a working copy of the latest `sage-4.5.3.alpha0` and find exactly the same problem. 

I also tried on my OpenSolaris machine inside a slightly modified version of `sage-4.5.3.alpha0`. Again, I get the same problem as before. 

To me this looks like an upstream bug, and not anything introduced in Sage. 

I just checked the source code, and see the code is actually in matplotlib-1.0.0. 


```
// Prevent multiple conflicting definitions of swab from stdlib.h and unistd.h
#if defined(__sun) || defined(sun)
#if defined(_XPG4)
#undef _XPG4
#endif
#if defined(_XPG3)
#undef _XPG3
#endif
#endif
```


It seems a bit of a hack to me. If `_XPG4` or `_XPG3` are defined, there were defined for good reason, and I doubt simply undefining them is the right way to tackle this. I could imagine this could cause a whole lot more problems than it solves. 

According to http://en.wikipedia.org/wiki/X/Open the [Single UNIX Specification](http://en.wikipedia.org/wiki/Single_UNIX_Specification) was based on the XPG4 standard, so I would not be surprised that undefining `_XPG4` will cause problems as the behavior of hundreds of header files will be changed.


---

Comment by drkirkby created at 2010-08-14 08:06:15

BTW, it perfectly possible on Solaris to have both `stdlib.h` and `unistd.h` included in the one source file - here's a "hello world" that does just that. 


```
drkirkby`@`hawk:~$ cat test.c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
   printf("Hello world\n");
   exit(0);
}

drkirkby`@`hawk:~$ gcc -Wall test.c
drkirkby`@`hawk:~$ ./a.out
Hello world
```



---

Attachment

With the patch, all doctests in plot/*.py pass with matplotlib 1.0.


---

Comment by jason created at 2010-08-14 16:02:29

Replying to [comment:16 drkirkby]:
> BTW, it perfectly possible on Solaris to have both `stdlib.h` and `unistd.h` included in the one source file - here's a "hello world" that does just that. 
> 
> {{{
> drkirkby`@`hawk:~$ cat test.c
> #include <stdio.h>
> #include <unistd.h>
> #include <stdlib.h>
> 
> int main() {
>    printf("Hello world\n");
>    exit(0);
> }
> 
> drkirkby`@`hawk:~$ gcc -Wall test.c
> drkirkby`@`hawk:~$ ./a.out
> Hello world
> }}}


Interesting.  In this case, it seems like they want to include Python.h.

By default, which of _XPG4 or _XPG3 is defined in your compiler?  From the code in stdlib.h, it looks like setting _XPG4, but undefining _XPG3, should work.


---

Comment by drkirkby created at 2010-08-14 17:38:37

Replying to [comment:18 jason]:
> Replying to [comment:16 drkirkby]:
> > BTW, it perfectly possible on Solaris to have both `stdlib.h` and `unistd.h` included in the one source file - here's a "hello world" that does just that. 
> > 
> > {{{
> > drkirkby`@`hawk:~$ cat test.c
> > #include <stdio.h>
> > #include <unistd.h>
> > #include <stdlib.h>
> > 
> > int main() {
> >    printf("Hello world\n");
> >    exit(0);
> > }
> > 
> > drkirkby`@`hawk:~$ gcc -Wall test.c
> > drkirkby`@`hawk:~$ ./a.out
> > Hello world
> > }}}
> 
> 
> Interesting.  In this case, it seems like they want to include Python.h.

I've no idea. 

> By default, which of _XPG4 or _XPG3 is defined in your compiler?  

Neither of them. 

One can see what gets defined with any combination of C and header files by pre-processing a file, and using the -dM options. To get the defaults, just use an empty file or /dev/null. This is a very useful trick some times. 


```
drkirkby`@`laptop:~$ gcc -dM -E - </dev/null  
#define __DBL_MIN_EXP__ (-1021)
#define __FLT_MIN__ 1.17549435e-38F
#define __CHAR_BIT__ 8
#define __WCHAR_MAX__ 2147483647
#define __DBL_DENORM_MIN__ 4.9406564584124654e-324
#define __FLT_EVAL_METHOD__ 2

etc etc
```


For the case of a test file where both unistd.h and stdlib.h are defined, we see both `_XOPEN_XPG3` and `_XOPEN_XPG4` get defined, but not `_XPG3` or `_XPG4`. 


```
drkirkby`@`laptop:~$ gcc -dM -E  test.c | grep XPG
#define _XOPEN_XPG3 
#define _XOPEN_XPG4 
```


> From the code in stdlib.h, it looks like setting _XPG4, but undefining _XPG3, should work.

I don't think one should go defining `_XPG3` and `_XPG4`  directly, but if one does do that, then one can induce the error depending on what you define and what header files you include. I leave it for you to prove that to yourself. (Try it on 't2.math') 

I can suggest a few resources that might shed some light on it. 

 * http://www.opengroup.org/forums/
 * gcc-help mailing list. (The mainly Linux crowd are bound to blame Sun, but worth asking anyway.)
 * comp.unix.solaris newsgroup http://groups.google.com/group/comp.unix.solaris
 * comp.lang.c newsgroup http://groups.google.co.uk/group/comp.lang.c 

There's probably a few more. Sorry I don't know the answer, but I doubt it needs on to go around defining `_XPG4` or similar. 


Dave


---

Comment by drkirkby created at 2010-08-24 19:09:40

I'm attaching the standards(1) man page from an OpenSolaris machine. This gives some information on this matter. I've also asked on the newsgroup [solaris.unix.solaris](http://groups.google.com/group/comp.unix.solaris/browse_thread/thread/2f10c2308c0b533d?hl=en#) about this issue.


---

Comment by drkirkby created at 2010-08-24 19:13:40

Oops, the standards's man page is in section 5, not 1.


---

Comment by jason created at 2010-09-07 02:55:58

Can I get an account on a Solaris box and instructions for reproducing this problem?  This is getting hard to debug without access to the hardware.


---

Comment by drkirkby created at 2010-09-08 16:44:15

Replying to [comment:22 jason]:
> Can I get an account on a Solaris box and instructions for reproducing this problem?  This is getting hard to debug without access to the hardware.

Ask William - he can give you an account on t2.math, which is a Solaris 10 SPARC system. 

Dave


---

Comment by jason created at 2010-09-09 18:03:55

I'm trying it out on t2 right now.  I logged into t2, extracted {{{/usr/local/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS.tar.gz}} to /scratch/grout, and then tried (as a control) to install the current matplotlib spkg:


```
./sage -f spkg/standard/matplotlib-0.99.3.spkg
```


gave errors like these:


```

building 'matplotlib.ft2font' extension
creating build/temp.solaris-2.10-sun4v-2.6
creating build/temp.solaris-2.10-sun4v-2.6/src
creating build/temp.solaris-2.10-sun4v-2.6/CXX
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -I/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/python2.6/site-packages/numpy/core/include -I/export/home/drkirkby/sage-4.5.1/local/include/freetype2 -I/export/home/drkirkby/sage-4.5.1/local/include -I/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/include/ -I/usr/local/include -I. -I/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/include/python2.6 -c src/ft2font.cpp -o build/temp.solaris-2.10-sun4v-2.6/src/ft2font.o
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/ext/hash_map:59,
                 from ./CXX/Extensions.hxx:68,
                 from src/ft2font.h:4,
                 from src/ft2font.cpp:1:
/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/backward/backward_warning.h:28:2: warning: #warning This file includes at least one deprecated or antiquated header which may be removed without further notice at a future date. Please use a non-deprecated interface with equivalent functionality instead. For a listing of replacement headers and interfaces, consult the file backward_warning.h. To disable this warning use -Wno-deprecated.
In file included from src/ft2font.h:13,
                 from src/ft2font.cpp:1:
/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/include/ft2build.h:56:38: error: freetype/config/ftheader.h: No such file or directory
In file included from src/ft2font.cpp:1:
src/ft2font.h:14:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:15:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:16:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:17:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:18:10: error: #include expects "FILENAME" or <FILENAME>
In file included from src/ft2font.cpp:1:
src/ft2font.h:31: error: ‘FT_Bitmap’ has not been declared
src/ft2font.h:31: error: ‘FT_Int’ has not been declared
src/ft2font.h:31: error: ‘FT_Int’ has not been declared
src/ft2font.h:77: error: ISO C++ forbids declaration of ‘FT_Face’ with no type
src/ft2font.h:77: error: expected ‘,’ or ‘...’ before ‘&’ token
src/ft2font.h:83: error: ISO C++ forbids declaration of ‘FT_Face’ with no type
src/ft2font.h:83: error: expected ‘,’ or ‘...’ before ‘&’ token
src/ft2font.h:122: error: ‘FT_Face’ does not name a type
src/ft2font.h:123: error: ‘FT_Matrix’ does not name a type
src/ft2font.h:124: error: ‘FT_Vector’ does not name a type
src/ft2font.h:125: error: ‘FT_Error’ does not name a type
src/ft2font.h:126: error: ‘FT_Glyph’ was not declared in this scope
src/ft2font.h:126: error: template argument 1 is invalid
src/ft2font.h:126: error: template argument 2 is invalid
src/ft2font.h:127: error: ‘FT_Vector’ was not declared in this scope
src/ft2font.h:127: error: template argument 1 is invalid
src/ft2font.h:127: error: template argument 2 is invalid
src/ft2font.h:133: error: ‘FT_BBox’ does not name a type
src/ft2font.cpp:45: error: ‘FT_Library’ does not name a type
src/ft2font.cpp:96: error: variable or field ‘draw_bitmap’ declared void
src/ft2font.cpp:96: error: ‘FT_Bitmap’ was not declared in this scope
src/ft2font.cpp:96: error: ‘bitmap’ was not declared in this scope
src/ft2font.cpp:97: error: ‘FT_Int’ was not declared in this scope
src/ft2font.cpp:98: error: ‘FT_Int’ was not declared in this scope
/scratch/grout/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/python2.6/site-packages/numpy/core/include/numpy/__multiarray_api.h:968: warning: ‘int _import_array()’ defined but not used
error: command 'gcc' failed with exit status 1
Error building matplotlib package.

```


Do you know how I can get up to at least installing the current matplotlib spkg on t2?  When I tried my updated 1.0 spkg, I also got these errors.


---

Comment by jason created at 2010-09-09 18:24:08

FYI, I did do the recommended `. /usr/local/gcc-4.4.1-sun-linker/gcc441sun` first.


---

Comment by jason created at 2010-09-09 19:51:45

It appears that the problem is in sage-location.  Note that the local/lib/pkgconfig/freetype2.pc file is

```
prefix=/export/home/drkirkby/sage-4.5.1/local
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include

Name: FreeType 2
Description: A free, high-quality, and portable font engine.
Version: 9.16.3
Requires:
Libs: -L${libdir} -lfreetype -lz 
Cflags: -I${includedir}/freetype2 -I${includedir}
```


which means it points to totally the wrong place once Sage is moved.  This should be fixed over on #9210.


---

Comment by drkirkby created at 2010-09-09 19:58:05

Jason,

I have no idea why this did not work for you. That binary was not built on 't2' but on another machine, with the expectation it would work on any SPARC. However, I am aware moving Sage does not always work. 

I can only suggest you build the latest Sage from source. Just remember to set something like


```
export SAGE_PARALLEL_SPKG_BUILD=yes
export MAKE="make -j8"
```


otherwise it will take ages to build. 

Dave


---

Comment by drkirkby created at 2010-09-09 19:59:38

BTW, there's a binary at 


```
/scratch/sage-4.5.3.rc0-binary.tar
```


you could try extracting that. 

But again, it has been moved, though in that case the binary was built on t2.math. 

Dave


---

Comment by jason created at 2010-09-09 20:17:35

Replying to [comment:27 drkirkby]:
> Jason,
> 
> I have no idea why this did not work for you. That binary was not built on 't2' but on another machine, with the expectation it would work on any SPARC. However, I am aware moving Sage does not always work. 
> 
> I can only suggest you build the latest Sage from source. Just remember to set something like
> 
> {{{
> export SAGE_PARALLEL_SPKG_BUILD=yes
> export MAKE="make -j8"
> }}}
> 
> otherwise it will take ages to build. 
> 

Thanks; I'll do that.  I'm 99% sure my problem is caused by a Sage directory move.


---

Comment by jason created at 2010-09-16 18:06:50

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-09-16 18:06:50

Okay, I've updated the spkg so that it works on t2 (and passes all matplotlib tests):

http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg

Can people try it?  Basically, I just deleted in CXX/WrapPython.h any fudging with the defines, based on drkirkby's idea above that it ought not have to do that.  The new WrapPython.h is:


```
#ifndef __PyCXX_wrap_python_hxx__
#define __PyCXX_wrap_python_hxx__

// On some platforms we have to include time.h to get select defined
#if !defined(__WIN32__) && !defined(WIN32) && !defined(_WIN32) && !defined(_WIN64)
#include <sys/time.h>
#endif

// pull in python definitions
#include <Python.h>

#endif
```


Here it passes the matplotlib test suite:


```
In [1]: import matplotlib
In [2]: matplotlib.__version__
Out[2]: '1.0.0'

In [3]: matplotlib.test()
/scratch/grout/sage-4.5.3/local/lib/python2.6/site-packages/matplotlib/axes.py:2369: UserWarning: Attempting to set identical left==right results
in singular transformations; automatically expanding.
left=730139.0, right=730139.0
  + 'left=%s, right=%s') % (left, right))
----------------------------------------------------------------------
Ran 138 tests in 755.419s

OK (KNOWNFAIL=42)
Out[3]: True
```



---

Comment by kcrisman created at 2010-09-16 18:10:23

Replying to [comment:30 jason]:
> Okay, I've updated the spkg so that it works on t2 (and passes all matplotlib tests):
> 
> http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg
> 
> Can people try it? 

I should be able to try this on OS X 10.4 PPC today or tomorrow.


---

Comment by jason created at 2010-09-16 18:37:48

Okay, I've composed a long message to matplotlib-devel about this issue:

http://sourceforge.net/mailarchive/message.php?msg_name=4C9262A9.5040901%40creativetrax.com


---

Comment by kcrisman created at 2010-09-16 20:33:02

Replying to [comment:31 kcrisman]:
> Replying to [comment:30 jason]:
> > Okay, I've updated the spkg so that it works on t2 (and passes all matplotlib tests):
> > 
> > http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg
> > 
> > Can people try it? 
> 
> I should be able to try this on OS X 10.4 PPC today or tomorrow.

Seems to be working a-ok here, no issues.

By the way, to drkirkby, looks like matplotlib also uses `nose` to run their tests, like scipy and numpy.  I get no indication that `SAGE_CHECK=yes` does anything - or would - because of that.  

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: import mat 
math        matplotlib  
sage: import matplotlib
sage: matplotlib.test()
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
| Sage Version 4.6.prealpha4, Release Date: 2010-09-07               |
| Type notebook() for the GUI, and license() for information.        |
/Users/student/<ipython console> in <module>()

/Users/student/Desktop/sage-4.6.prealpha4/local/lib/python2.6/site-packages/matplotlib/__init__.pyc in test(verbosity)
    922 def test(verbosity=0):
    923     """run the matplotlib test suite"""
--> 924     import nose
    925     import nose.plugins.builtin
    926     from testing.noseclasses import KnownFailure

ImportError: No module named nose
```

If we want to test these automatically, we need nose; just adding the lines to `spkg-check` or `spkg-install` won't help.  Obviously this is a different ticket, but I wanted to point it out.  And I'd support adding this to Sage if it improved things overall.


---

Comment by jason created at 2010-09-16 20:51:36

Sorry; I should have CCd you on this: #9221


---

Comment by kcrisman created at 2010-09-16 21:03:51

> Sorry; I should have CCd you on this: #9221
???  That's this ticket, which I'm obviously already cc:ed on.  Did you mean something else related to nose?


---

Comment by jason created at 2010-09-16 21:13:05

Yes: #9921.  Notice that it's convenient that related tickets have numbers so similar :).


---

Comment by drkirkby created at 2010-09-16 22:10:03

Replying to [comment:33 kcrisman]:
> Replying to [comment:31 kcrisman]:
> > Replying to [comment:30 jason]:
> > > Okay, I've updated the spkg so that it works on t2 (and passes all matplotlib tests):
> > > 
> > > http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg
> > > 
> > > Can people try it? 
> > 
> > I should be able to try this on OS X 10.4 PPC today or tomorrow.
> 
> Seems to be working a-ok here, no issues.
> 
> By the way, to drkirkby, looks like matplotlib also uses `nose` to run their tests, like scipy and numpy.  I get no indication that `SAGE_CHECK=yes` does anything - or would - because of that.  

See 

#9921

where only today I suggested we make 'nose' a *standard* package. 

> If we want to test these automatically, we need nose; just adding the lines to `spkg-check` or `spkg-install` won't help.  Obviously this is a different ticket, but I wanted to point it out.  And I'd support adding this to Sage if it improved things overall.

As far as I can see, adding nose as a stranded package would be very low risk, as nothing would depend on it except during testing. So it can't hardly screw Sage up, as long as nose builds reliably itself. Even if it was totally non-functional, it would not hurt sage. 

What we need is a list of packages that use nose, then request it is added as standard on the basis we can't test otherwise. It might be able to escape the 'experimental' stage. 

Dave


---

Comment by jason created at 2010-09-17 03:20:53

Eric Firing just committed a fix to matplotlib SVN which takes care of these compiling issues on Solaris.  Thanks for David for the tipoff on how to solve these issues (i.e., delete the kludgy defines).

See http://matplotlib.svn.sourceforge.net/viewvc/matplotlib?view=revision&revision=8707 for the commit log upstream.


---

Comment by jason created at 2010-09-17 03:21:37

(so in the next release, we can delete the patch I added to the spkg fixing the Solaris compiling issue).


---

Comment by jason created at 2010-09-21 18:24:05

Ping about a review---can anyone review this?  The new spkg works on solaris (t2).  The new version of matplotlib adds some very nice features and allows us to clean up the spkg quite a bit.


---

Comment by jason created at 2010-09-28 15:04:27

Another friendly ping to people to look at this ticket and review it...


---

Comment by kcrisman created at 2010-09-28 15:16:31

> Another friendly ping to people to look at this ticket and review it...
I'd love to, but there is too much technical shell stuff mentioned in the comments so I don't want to be responsible for breaking something somewhere.


---

Comment by jason created at 2010-09-28 15:29:57

As I see it, the only outstanding problem was that it didn't compile on Solaris.  We fixed that (I compiled it on t2), but it doesn't seem appropriate for me to set the ticket to positive review.  I was hoping for someone to give it one last try on their standard platform.

David, can you confirm that this spkg now works on Solaris?  If not, kcrisman, can you just check that it works on your platform still?


---

Comment by kcrisman created at 2010-09-28 16:23:08

Replying to [comment:43 jason]:
> As I see it, the only outstanding problem was that it didn't compile on Solaris.  We fixed that (I compiled it on t2), but it doesn't seem appropriate for me to set the ticket to positive review.  I was hoping for someone to give it one last try on their standard platform.
> 
> David, can you confirm that this spkg now works on Solaris?  If not, kcrisman, can you just check that it works on your platform still?
Jason, that was the version I tried!

Seems to be working fine on OS X 10.6 right now, tested the live documentation and the output at various spots.  Currently running doctests.


---

Comment by kcrisman created at 2010-09-28 18:20:45

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-09-28 18:20:45

Okay, all is well.  I love some of those plot doc graphics!  One definitely also needs the patch for the axis labels to look right - interesting change in API, though of course it was a switch from 0.x to 1.y!

As long as you are confident enough that t2 working is good (and indeed, drkirkby didn't say boo although he commented after that) then I'll set to positive review.


---

Comment by jason created at 2010-09-28 19:07:58

ptestlong in 4.6.alpha1 passes with the following tickets applied in order: #9221 (and new spkg), #9740, #9746, #4342.


---

Comment by mpatel created at 2010-09-29 08:48:37

Resolution: fixed


---

Comment by mpatel created at 2010-09-29 23:58:39

Has anyone tested the new package with a full build of Sage from scratch?  I'm getting very many doctest errors that appears to stem from missing .ttf files.  I'll investigate further.


---

Comment by jason created at 2010-09-30 01:46:17

I haven't tested that configuration.  Can you post some of these errors here?


---

Comment by mpatel created at 2010-09-30 02:58:06

I made a source distribution from 4.6.alpha1 + #9221 and built it in a directory named `sage-4.6.alpha2-9221`.  The long doctests pass.  I moved the directory to a different place.

I made a source distribution from the latest trial 4.6.alpha2 + #9221 and built it in a directory named `sage-4.6.alpha2pre2`, i.e., it's different from the previous build directory.  Many tests fail with

```
RuntimeError: Could not open facefile /mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha2-9221/local/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf/Vera.ttf; Cannot_Open_Resource
```

The full log is [here](http://sage.math.washington.edu/home/mpatel/trac/9221/ptestlong-4.6.alpha2pre2.log).  I think the problem is that

```sh
$ grep 9221 $HOME/.matplotlib/fontList.cache | grep Vera.ttf
S'/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha2-9221/local/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf/Vera.ttf'
aS'/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha2-9221/local/lib/python/site-packages/matplotlib/mpl-data/fonts/ttf/Vera.ttf'
$ grep 9221 $HOME/.matplotlib/fontList.cache | wc
    128     128   16666
```



---

Comment by mpatel created at 2010-09-30 03:18:15

After moving `$HOME/.matplotlib` to a different place, I've rerun the tests in `sage-4.6.alpha2pre2`.  I see many failures with

```
AttributeError: 'module' object has no attribute 'cbook'
```

See [this log](http://sage.math.washington.edu/home/mpatel/trac/9221/ptestlong-4.6.alpha2pre2-take2.log).  (I stopped the tests early.)

I've started the tests again and now they appear to be passing.


---

Comment by mpatel created at 2010-09-30 03:18:15

Changing status from closed to needs_work.


---

Comment by mpatel created at 2010-09-30 03:20:31

Changing status from needs_work to needs_info.


---

Comment by mpatel created at 2010-09-30 03:48:02

Changing status from needs_info to needs_work.


---

Comment by mpatel created at 2010-09-30 03:48:02

I'm removing this from 4.6.alpha2, but there's still time for it in alpha3.


---

Comment by jason created at 2010-09-30 04:32:45

If you still have the directories around, keep the .matplotlib directory, but delete the fontList.cache file (it's a cache that should be automagically regenerated).


---

Comment by jason created at 2010-09-30 04:39:55

Relevant docs: http://matplotlib.sourceforge.net/faq/troubleshooting_faq.html#matplotlib-directory-location

Maybe Sage should set the MPLCONFIGDIR to point to something inside the Sage tree.


---

Comment by jason created at 2010-09-30 04:41:01

In fact, setting MPLCONFIGDIR is #6235.


---

Comment by jason created at 2010-09-30 05:18:20

When I move things around to try to duplicate the issue, the cache file is automatically updated after plotting something using fonts.  So I'll try to recreate your problem with a fresh source+9221 build.


---

Comment by jason created at 2010-09-30 05:18:20

Changing status from needs_work to needs_info.


---

Comment by jason created at 2010-09-30 05:33:06

Replying to [comment:50 mpatel]:
> I made a source distribution from 4.6.alpha1 + #9221 and built it in a directory named `sage-4.6.alpha2-9221`.  The long doctests pass.  I moved the directory to a different place.
> 
> I made a source distribution from the latest trial 4.6.alpha2 + #9221 and built it in a directory named `sage-4.6.alpha2pre2`, i.e., it's different from the previous build directory.  Many tests fail with


I assume this is on sage.math?  Can you make the latest trial 4.6.alpha2 tarball available somewhere so I can try to reproduce what you did?


---

Comment by mpatel created at 2010-09-30 10:12:11

I built on sage.math.  The latest trial 4.6.alpha2, which is likely final, as the builds appear to be going well, is in http://sage.math.washington.edu/home/release/sage-4.6.alpha2/ .


---

Comment by jason created at 2010-10-01 02:46:44

I'm going to try to reproduce this first on sage.math.  Do I just replace the matplotlib-0.99.3 spkg with my spkg in the source tarball, then build?  Is there something more I need to do?


---

Comment by mpatel created at 2010-10-01 06:54:23

Replying to [comment:60 jason]:
> I'm going to try to reproduce this first on sage.math.  Do I just replace the matplotlib-0.99.3 spkg with my spkg in the source tarball, then build?  Is there something more I need to do?

That should work.  The colormap tests fixed by the patch will fail, but if the errors I saw show up --- i.e., they're not part of the "fog of merge" --- they'll be easy to distinguish.


---

Comment by jason created at 2010-10-01 15:32:19

I've reproduced the problem and emailed the matplotlib mailing list.  I'll also try tracking this down a bit this afternoon.


---

Comment by jason created at 2010-10-01 15:47:14

The reply on matplotlib-users is that this is already fixed in SVN.  I'll get the commit, apply the patch, and update the spkg.


---

Comment by jason created at 2010-10-01 18:01:43

Changing status from needs_info to needs_review.


---

Comment by jason created at 2010-10-01 18:01:43

Okay, I've updated the spkg (at the original address in the description) with the patch from matplotlib SVN that should take care of the problem.  I'm building this momentarily.

I'm putting this as needs review so that one or two others can double-check this.  kcrisman?


---

Comment by kcrisman created at 2010-10-01 19:25:03

> I'm putting this as needs review so that one or two others can double-check this.  kcrisman?
I'll do my best, but might not be able to test it on something you don't have access to already (you have OS X 10.6, and access to sage.math) until after the weekend.


---

Comment by kcrisman created at 2010-10-01 19:47:41

I can at least confirm that this mpl package installs fine with `./sage -i` on a relatively new (but not brand new) build of 4.6.alpha1.  I hope that is helpful; I don't have time to run any tests on this machine now.


---

Comment by jason created at 2010-10-02 02:08:33

mpatel: I just built a fresh copy of 4.6.alpha2 on sage.math with the new spkg (linked above) and ran ptestlong.  I got the two colormap failures that are solved in the patch on this ticket, as well as two other failures that seem totally unrelated to this spkg.

So I think we are good to go.  I feel weird setting this back to positive review, but can you try merging it again and "reviewing" the change to make sure it fixes the error you were seeing?


---

Comment by jhpalmieri created at 2010-10-02 15:53:36

I haven't looked at the code at all, but it builds and passes tests for me on an Intel Mac OS X 10.6 box, skynet machine taurus (linux: x86_64-Linux-nehalem-fc), and skynet machine fulvia (Solaris on x86: x86_64-SunOS-core2). I also deleted my .matplotlib directory and reran the tests on taurus, and they passed again.  I haven't been following this ticket; is this good enough to restore the positive review?


---

Comment by jason created at 2010-10-02 16:05:48

I think so.


---

Comment by jhpalmieri created at 2010-10-02 16:50:31

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-02 23:29:44

There are uncommitted changes

```sh
matplotlib-1.0.0$ hg stat
? patches/WrapPython.h
? patches/WrapPython.h.diff
```

By the way, is this the patch that fixes the font cache problem?


---

Comment by jason created at 2010-10-03 02:42:48

No, that's the previous version of the spkg.  Apparently somehow the new version was not copied to my home directory on sage.math.

The new version is md5 28179fff25e33fc623f1de96a039eecc

I've just double-checked, and it is now the version in my home directory:

http://sage.math.washington.edu/home/jason/matplotlib-1.0.0.spkg

Sorry for the mess-up!  I'm setting it back to needs_review, since apparently people reviewed the old spkg.  mpatel---I think you building on sage.math would be sufficient to review this.


---

Comment by jason created at 2010-10-03 02:42:48

Changing status from positive_review to needs_work.


---

Comment by jason created at 2010-10-03 02:42:57

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-10-03 02:43:29

BTW, WrapPython.h fixes the Solaris problem, and the font_manager.py patch fixes the font cache problem.


---

Comment by jason created at 2010-10-03 02:48:05

I wonder if maybe this happened because of the system maintenance on the home directory???  I don't know.  I might have also made a mistake when I thought I copied the new spkg over.


---

Comment by mpatel created at 2010-10-03 06:35:21

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-03 06:40:34

Thanks, Jason!  The `fontList.cache` is now quietly regenerated and the tests pass on sage.math.


---

Comment by leif created at 2010-10-20 14:57:05

Replying to [comment:74 jason]:
> BTW, WrapPython.h fixes the Solaris problem, and the font_manager.py patch fixes the font cache problem.

Aren't these worth an spkg patch level? This also avoids confusion with previous versions.


---

Comment by jason created at 2010-10-20 15:04:05

Replying to [comment:79 leif]:
> Replying to [comment:74 jason]:
> > BTW, WrapPython.h fixes the Solaris problem, and the font_manager.py patch fixes the font cache problem.
> 
> Aren't these worth an spkg patch level? This also avoids confusion with previous versions.
>  

I viewed this as part of the 1.0.0 spkg (these patches were necessary for the 1.0.0 spkg to be accepted and used).


---

Comment by leif created at 2010-10-20 15:13:54

Replying to [comment:80 jason]:
> Replying to [comment:79 leif]:
> > Replying to [comment:74 jason]:
> > > BTW, WrapPython.h fixes the Solaris problem, and the font_manager.py patch fixes the font cache problem.
> > 
> > Aren't these worth an spkg patch level? This also avoids confusion with previous versions.
> >  
> 
> I viewed this as part of the 1.0.0 spkg (these patches were necessary for the 1.0.0 spkg to be accepted and used).

:-) IMHO every spkg that's not almost vanilla upstream should carry a patch level, since the (Sage) package version (without the patch level) is not a Sage but the upstream version, but this appears to be an endless discussion...


---

Comment by leif created at 2010-10-20 18:44:38

I'm not the release manager, but *IMHO* either this ticket *needs work*, or #6235 / #9210? should be blockers for Sage 4.6, since

 * installing Sage 4.6.alpha3 / matplotlib 1.0.0 breaks other Sage installations (cf. doctest errors in `sage/plot/plot.py` below, which even occur after rebuilding e.g. Sage 4.5.3 from scratch),
 * the current spkg / alpha3 *again* breaks upgrading (cf. #9896) if the original Sage installation has been moved (copied / renamed), which apparently is common user practice.


Unless one e.g. deletes `$HOME/.matplotlib/`, the following happens with *other* Sage installations (and perhaps other software):

```
sage -t -long "devel/sage/sage/plot/plot.py"                
**********************************************************************
File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/devel/sage/sage/plot/plot.py", line 210:
    sage: P    # show the result
Exception raised:
    Traceback (most recent call last):
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[55]>", line 1, in <module>
        P    # show the result###line 210:
    sage: P    # show the result
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/misc/displayhook.py", line 174, in displayhook
        print_obj(sys.stdout, obj)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/misc/displayhook.py", line 142, in print_obj
        print >>out_stream, `obj`
      File "sage_object.pyx", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1370)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/plot/plot.py", line 915, in _repr_
        self.show()
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/plot/plot.py", line 1437, in show
        self.save(DOCTEST_MODE_FILE, **options)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/sage/plot/plot.py", line 1973, in save
        figure.savefig(filename,dpi=dpi,bbox_inches='tight',**options)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/figure.py", line 1032, in savefig
        self.canvas.print_figure(*args, **kwargs)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/backend_bases.py", line 1455, in print_figure
        **kwargs)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 358, in print_png
        FigureCanvasAgg.draw(self)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 314, in draw
        self.figure.draw(self.renderer)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/artist.py", line 46, in draw_wrapper
        draw(artist, renderer, *args, **kwargs)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/figure.py", line 773, in draw
        for a in self.axes: a.draw(renderer)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/artist.py", line 46, in draw_wrapper
        draw(artist, renderer, *args, **kwargs)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/axes.py", line 1735, in draw
        a.draw(renderer)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/text.py", line 518, in draw
        bbox, info = self._get_layout(renderer)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/text.py", line 280, in _get_layout
        clean_line, self._fontproperties, ismath=ismath)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 156, in get_text_width_height_descent
        self.mathtext_parser.parse(s, self.dpi, prop)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/mathtext.py", line 2797, in parse
        font_output = fontset_class(prop, backend)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/mathtext.py", line 658, in __init__
        self._stix_fallback = StixFonts(*args, **kwargs)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/mathtext.py", line 900, in __init__
        fullpath = findfont(name)
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python/site-packages/matplotlib/font_manager.py", line 1306, in findfont
        if not os.path.exists(font):
      File "/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/lib/python2.6/genericpath.py", line 18, in exists
        st = os.stat(path)
    TypeError: coercing to Unicode: need string or buffer, dict found
**********************************************************************
...
[same exception in other examples]
...
**********************************************************************
5 items had failures:
   1 of  71 in __main__.example_0
   1 of   7 in __main__.example_13
   1 of   8 in __main__.example_14
   1 of  45 in __main__.example_30
   1 of  89 in __main__.example_43
***Test Failed*** 5 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_plot.py
```



When trying to upgrade to 4.6.alpha3 in a _renamed_ directory, installing matplotlib 1.0.0 fails with

```
...
running build_ext
building 'matplotlib.ft2font' extension
creating build/temp.linux-x86_64-2.6
creating build/temp.linux-x86_64-2.6/src
creating build/temp.linux-x86_64-2.6/CXX
gcc -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -march=native -O3 -fno-strict-aliasing -fomit-frame-pointer -DHONORS_CFLAGS -march=native -O3 -DHONORS_CPPFLAGS -fPIC -DPY_ARRAY_UNIQUE_SYMBOL=MPL_ARRAY_API -DPYCXX_ISO_CPP_LIB=1 -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/lib/python2.6/site-packages/numpy/core/include -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/include/freetype2 -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-to-rename/local/include -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include -I. -I/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6 -c src/ft2font.cpp -o build/temp.linux-x86_64-2.6/src/ft2font.o
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from /home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6/Python.h:8,
                 from ./CXX/WrapPython.h:47,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/ft2font.cpp:1:
/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6/pyconfig.h:1028:1: warning: "_POSIX_C_SOURCE" redefined
In file included from /usr/include/sys/time.h:23,
                 from ./CXX/WrapPython.h:43,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/ft2font.cpp:1:
/usr/include/features.h:158:1: warning: this is the location of the previous definition
In file included from /home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6/Python.h:8,
                 from ./CXX/WrapPython.h:47,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/ft2font.cpp:1:
/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/python2.6/pyconfig.h:1037:1: warning: "_XOPEN_SOURCE" redefined
In file included from /usr/include/sys/time.h:23,
                 from ./CXX/WrapPython.h:43,
                 from ./CXX/Extensions.hxx:37,
                 from src/ft2font.h:4,
                 from src/ft2font.cpp:1:
/usr/include/features.h:160:1: warning: this is the location of the previous definition
In file included from src/ft2font.h:14,
                 from src/ft2font.cpp:1:
/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/include/ft2build.h:56:38: error: freetype/config/ftheader.h: No such file or directory
In file included from src/ft2font.cpp:1:
src/ft2font.h:15:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:16:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:17:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:18:10: error: #include expects "FILENAME" or <FILENAME>
src/ft2font.h:19:10: error: #include expects "FILENAME" or <FILENAME>
In file included from src/ft2font.cpp:1:
src/ft2font.h:33: error: 'FT_Bitmap' has not been declared
src/ft2font.h:33: error: 'FT_Int' has not been declared
src/ft2font.h:33: error: 'FT_Int' has not been declared
src/ft2font.h:89: error: ISO C++ forbids declaration of 'FT_Face' with no type
src/ft2font.h:89: error: expected ',' or '...' before '&' token
src/ft2font.h:95: error: ISO C++ forbids declaration of 'FT_Face' with no type
src/ft2font.h:95: error: expected ',' or '...' before '&' token
src/ft2font.h:137: error: 'FT_Face' does not name a type
src/ft2font.h:138: error: 'FT_Matrix' does not name a type
src/ft2font.h:139: error: 'FT_Vector' does not name a type
src/ft2font.h:140: error: 'FT_Error' does not name a type
src/ft2font.h:141: error: 'FT_Glyph' was not declared in this scope
src/ft2font.h:141: error: template argument 1 is invalid
src/ft2font.h:141: error: template argument 2 is invalid
src/ft2font.h:142: error: 'FT_Vector' was not declared in this scope
src/ft2font.h:142: error: template argument 1 is invalid
src/ft2font.h:142: error: template argument 2 is invalid
src/ft2font.h:148: error: 'FT_BBox' does not name a type
src/ft2font.cpp:45: error: 'FT_Library' does not name a type
src/ft2font.cpp:108: error: variable or field 'draw_bitmap' declared void
src/ft2font.cpp:108: error: 'FT_Bitmap' was not declared in this scope
src/ft2font.cpp:108: error: 'bitmap' was not declared in this scope
src/ft2font.cpp:109: error: 'FT_Int' was not declared in this scope
src/ft2font.cpp:110: error: 'FT_Int' was not declared in this scope
/home/leif/Sage/sage-4.5.3-for-4.6.alpha3-renamed/local/lib/python2.6/site-packages/numpy/core/include/numpy/__multiarray_api.h:968: warning: 'int _import_array()' defined but not used
error: command 'gcc' failed with exit status 1
Error building matplotlib package.
```



---

Comment by jason created at 2010-10-20 21:17:31

Replying to [comment:82 leif]:
> I'm not the release manager, but *IMHO* either this ticket *needs work*, or #6235 / #9210? should be blockers for Sage 4.6, since
> 
>  * installing Sage 4.6.alpha3 / matplotlib 1.0.0 breaks other Sage installations (cf. doctest errors in `sage/plot/plot.py` below, which even occur after rebuilding e.g. Sage 4.5.3 from scratch),

Are you sure that you have the most recent (i.e., the merged) 1.0.0 spkg from this ticket?  Can you try sage -f just in case (you see that there have been updates to the 1.0.0 spkg on this ticket as time went on)

Or wait.  Are you saying that the font cache file created by the new(est) spkg here is causing problems with older versions of matplotlib?


---

Comment by leif created at 2010-10-20 21:39:37

Replying to [comment:83 jason]:
> Replying to [comment:82 leif]:
> > I'm not the release manager, but *IMHO* either this ticket *needs work*, or #6235 / #9210? should be blockers for Sage 4.6, since
> > 
> >  * installing Sage 4.6.alpha3 / matplotlib 1.0.0 breaks other Sage installations (cf. doctest errors in `sage/plot/plot.py` below, which even occur after rebuilding e.g. Sage 4.5.3 from scratch),
> 
> Are you sure that you have the most recent (i.e., the merged) 1.0.0 spkg from this ticket?  Can you try sage -f just in case (you see that there have been updates to the 1.0.0 spkg on this ticket as time went on)

I only have the current 1.0.0 one, but that doesn't solve the problems older MPL installations have. ;-)
 
> Or wait.  Are you saying that the font cache file created by the new(est) spkg here is causing problems with older versions of matplotlib?

Exactly that. It seems they've changed the format s.t. older MPL versions expecting an older format (without doing any consistency / type / error checking) pass a dictionary to `os.path.exists()`.


---

Comment by mpatel created at 2010-10-20 23:40:03

Leif, do the current patches at #6235 and #9210 fix the problems you've found?


---

Comment by leif created at 2010-10-21 01:23:14

Replying to [comment:85 mpatel]:
> Leif, do the current patches at #6235 and #9210 fix the problems you've found?

I'm pretty sure #6235 fixes (at least Sage's) MPL 1.0.0 breaking older installations.

Modifying `$SAGE_ROOT/local/lib/pkgconfig/freetype2.pc` on Sage relocations perhaps fixes later build errors (including upgrades) of dependent packages like MPL; I haven't looked at nor tested the patch though. (Forcing reinstallation of freetype after moving Sage fixes it; but that's of course just a work-around, cf. #9896.)

At least for freetype, it should be possible to simply set `prefix` to `$SAGE_LOCAL` (unexpanded) rather than a hard-coded absolute path. (Done once, e.g. in its `spkg-install`.)


---

Comment by leif created at 2010-10-21 01:34:50

Replying to [comment:86 leif]:
> At least for freetype, it should be possible to simply set `prefix` to `$SAGE_LOCAL` (unexpanded) rather than a hard-coded absolute path. (Done once, e.g. in its `spkg-install`.)


```
prefix=${SAGE_LOCAL}
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include

Name: FreeType 2
Description: A free, high-quality, and portable font engine.
Version: 9.16.3
Requires:
Libs: -L${libdir} -lfreetype
Cflags: -I${includedir}/freetype2 -I${includedir}
```

works for me. (The curly braces are mandatory.)


---

Comment by leif created at 2010-10-21 04:52:37

Replying to [comment:85 mpatel]:
> Leif, do the current patches at #6235 and #9210 fix the problems you've found?

Obviously #9210 doesn't help with upgrades from older versions, i.e. upgrading *to* 4.6. So for 4.6, it's perhaps better to fix the freetype spkg (though even preparing a fake new spkg would suffice for the moment).

Again hard-coding `SAGE_ROOT` into the `.pc` files is IMHO superfluous btw.


---

Comment by mpatel created at 2010-10-21 07:49:28

Replying to [comment:88 leif]:
> Replying to [comment:85 mpatel]:
> > Leif, do the current patches at #6235 and #9210 fix the problems you've found?
> 
> Obviously #9210 doesn't help with upgrades from older versions, i.e. upgrading *to* 4.6. So for 4.6, it's perhaps better to fix the freetype spkg (though even preparing a fake new spkg would suffice for the moment).

For 4.6, I suggest we just bump up the patch level for freetype.  Could you do this and add a link to the new spkg here?


---

Comment by mpatel created at 2010-10-21 09:58:29

Replying to [comment:89 mpatel]:
> Replying to [comment:88 leif]:
> > Replying to [comment:85 mpatel]:
> > > Leif, do the current patches at #6235 and #9210 fix the problems you've found?
> > 
> > Obviously #9210 doesn't help with upgrades from older versions, i.e. upgrading *to* 4.6. So for 4.6, it's perhaps better to fix the freetype spkg (though even preparing a fake new spkg would suffice for the moment).
> 
> For 4.6, I suggest we just bump up the patch level for freetype.  Could you do this and add a link to the new spkg here?

I've put an "updated" spkg at

 http://sage.math.washington.edu/home/mpatel/trac/9221/freetype-2.3.5.p3.spkg


---

Comment by jason created at 2010-10-21 12:19:11

Replying to [comment:86 leif]:

> At least for freetype, it should be possible to simply set `prefix` to `$SAGE_LOCAL` (unexpanded) rather than a hard-coded absolute path. (Done once, e.g. in its `spkg-install`.)

That's fantastic!  It sounds like we should investigate doing that for the other packages as well (like libpng, etc.)  There are some places in the pkgconfig files where the path is used in places other than the prefix, so doing this trick may not solve everything, but probably would solve a lot of the issues with pkgconfig files.


---

Comment by jason created at 2010-11-02 14:14:54

Replying to [comment:91 jason]:
> Replying to [comment:86 leif]:
> 
> > At least for freetype, it should be possible to simply set `prefix` to `$SAGE_LOCAL` (unexpanded) rather than a hard-coded absolute path. (Done once, e.g. in its `spkg-install`.)
> 
> That's fantastic!  It sounds like we should investigate doing that for the other packages as well (like libpng, etc.)  There are some places in the pkgconfig files where the path is used in places other than the prefix, so doing this trick may not solve everything, but probably would solve a lot of the issues with pkgconfig files.

I've made this idea #10202.  Leif, do you think we can do this at compile time, or do we have to fix up the pkgconfig file after the spkg is installed?  I'm guessing the latter.
