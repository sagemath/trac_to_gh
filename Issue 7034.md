# Issue 7034: Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 

CC was set to the Sun C compiler, and CXX to the Sun C++ compiler,  uses GNU flags with the Sun compiler

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-27 15:00:15

Assignee: tbd

CC:  polybori@mfo.de alexanderdreyer

Keywords: SCons Solaris

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 

CC was set to the Sun C compiler, and CXX to the Sun C++ compiler, 


It would appear that Using PolyBoRi correctly uses the value of CXX as the C++ compiler, but will pass GNU specific options to that compiler. 


```
polybori-0.6.3-20090827/.hgignore
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
mkdir: Failed to make directory "src/boost_1_34_1.cropped"; File exists
Starting build...
Removing old PolyBoRi install...
Done removing old PolyBoRi install.
Running build_polybori...
scons: Reading SConscript files ...
Sun linker detected.
Checking for C header file gd.h... no
Checking for C++ header file unordered_map... no
Checking for C++ header file tr1/unordered_map... no
Checking for C++ header file ext/hash_map... no
Warning: No LaTeX to html converter found, Tutorial will not be installed
Checking for C library m4ri... no
Checking for C header file gd.h... no
Symlinking to M4RI/m4ri ...
no python extension
scons: done reading SConscript files.
scons: Building targets ...
/opt/xxxsunstudio12.1/bin/CC -o polybori/src/BoolePolyRing.o -c -O3 -Wno-long-long -Wreturn-type -g -fPIC -ftemplate-depth-100 -g -fPIC -O3 -Wno-long-long -Wreturn-type -g -fPIC -DNDEBUG -DPACKED -DHAVE_M4RI -DHAVE_IEEE_754 -DBSD -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/polybori-0.6.3-20090827/src/boost_1_34_1.cropped -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/python2.6 -Ipolybori/include -IM4RI -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd polybori/src/BoolePolyRing.cc
CC: Warning: Option -Wno-long-long passed to ld, if ld is invoked, ignored otherwise
CC: Warning: Option -Wreturn-type passed to ld, if ld is invoked, ignored otherwise
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
CC: Warning: Option -ftemplate-depth-100 passed to ld, if ld is invoked, ignored otherwise
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
CC: Warning: Option -Wno-long-long passed to ld, if ld is invoked, ignored otherwise
CC: Warning: Option -Wreturn-type passed to ld, if ld is invoked, ignored otherwise
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
"polybori/include/CDDManager.h", line 103: Warning: Last line in file "polybori/include/cacheopts.h" is not terminated with a newline.
"polybori/include/CCuddZDD.h", line 308: Warning (Anachronism): Formal argument func of type DdNode*(*)(DdManager*,DdNode*,int) in call to polybori::CCuddDDBase<polybori::CCuddZDD>::apply(DdNode*(*)(DdManager*,DdNode*,int), int) const is being passed extern "C" DdNode*(*)(DdManager*,DdNode*,int).
"polybori/include/CCuddZDD.h", line 308: Warning (Anachronism): Formal argument func of type DdNode*(*)(DdManager*,DdNode*,int) in call to polybori::CCuddDDBase<polybori::CCuddZDD>::apply(DdNode*(*)(DdManager*,DdNode*,int), int) const is being passed extern "C" DdNode*(*)(DdManager*,DdNode*,int).
"polybori/include/CCuddZDD.h", line 308: Warning (Anachronism): Formal argument func of type DdNode*(*)(DdManager*,DdNode*,int) in call to polybori::CCuddDDBase<polybori::CCuddZDD>::apply(DdNode*(*)(DdManager*,DdNode*,int), int) const is being passed extern "C" DdNode*(*)(DdManager*,DdNode*,int).
```


PolyBoRi uses SCons, and the use of SCons in Sage seems to cause countless problems.


---

Comment by drkirkby created at 2009-11-27 13:41:46

I emailed this to polybori-discuss at lists.sourceforge.net on 27th November 2009.


---

Comment by PolyBoRi created at 2009-12-03 08:23:32

From polybori-discuss:
In fact, Sage forces PolyBoRi to do so. Sage's spkg contains a custom.py
file, which overwrites PolyBoRi's settings:
Looking at  polybori-0.6.3.r1647-20091028, one can see:

dreyer`@`lts035 [999] (0) [...patches]cat custom.py
import os
import sys

CCFLAGS=["-O3 -Wno-long-long -Wreturn-type -g -fPIC"]
CXXFLAGS=CCFLAGS+["-ftemplate-depth-100 -g -fPIC"]
[...]

The -W options can be dropped without any problems for all platforms.
But the remaining options were set intentionally in Sage, as far as I
know.  (I don't know the reason for -fPIC).
Does PolyBoRi compile with the sun-compiler, if -ftemplate-depth-100 and
-fPIC is dropped, i.e. if the two lines from custom.py read as follows:

CCFLAGS=["-O3 -g"]
CXXFLAGS=[""]
(previous line corrected since polybori-discuss)

In addition (see
http://developers.sun.com/solaris/articles/cmp_stlport_libCstd.html)
in order to have C++98 available, one has to build with  -library=stlport4 .

But there are still some lines of code (related to default template parameters), which do not compile using the solaris compiler. I'll try to sort this out.

Regards,
  Alexander


---

Comment by AlexanderDreyer created at 2012-06-01 19:38:29

Changing status from new to needs_info.


---

Comment by AlexanderDreyer created at 2012-06-01 19:38:29

The issue was discussed in polybori-discuss and the flags were corrected upstream in the meantime. I have no knowledge whether recent spkgs were tested w.r.t. sun's compiler.


---

Comment by jdemeyer created at 2015-09-08 14:48:05

Changing status from needs_info to positive_review.


---

Comment by jdemeyer created at 2015-09-08 14:48:05

Let's assume this is fixed by the new `brial` package.


---

Comment by vbraun created at 2015-09-12 13:57:55

Resolution: fixed
