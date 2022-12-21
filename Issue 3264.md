# Issue 3264: Upgrade PolyBoRi to 0.4 release

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-21 13:19:54

Assignee: mabshoff

CC:  polybori malb

Make sure to revert #3104 in case we do end up using less memory.

Cheers,

Michael


---

Comment by tabbott created at 2008-05-30 06:03:45

This would be quite helpful for getting SAGE into Debian (since the polybori-0.4 package is the first version that satisfies Debian python policy).


---

Comment by tabbott created at 2008-07-11 01:40:24

I've attached a patch to SAGE required to make SAGE build against the polybori 0.5 release candidate.

The corresponding polybori-0.5rc.spkg is available at:

http://sage.math.washington.edu/home/tabbott/polybori-0.5rc.spkg


---

Attachment


---

Comment by mabshoff created at 2008-07-11 02:58:23

Changing keywords from "" to "editor_mabshoff".


---

Comment by mabshoff created at 2008-07-11 02:58:23

Hi Tim,

thanks for doing this, but I am curious about a couple things.

 * The repo is in an inconsitent state:

```
polybori-0.5rc$ hg status
! patches/CCuddCore.h
! patches/CCuddCore.h-diff.patch
! patches/SConstruct
! patches/SConstruct.cygwin
! patches/SConstruct.cygwin.patch
? patches/PyPolyBoRi.py.orig
? patches/PyPolyBori.patch
? patches/SConstruct.orig
? patches/SConstruct.patch
```

 * The workaround at the end of spkg-install should have been removed:

```
# linking dynmic libraries causes segfaults at exit (see #2822)
if [ `uname` = "Darwin" ]; then
    rm -f $SAGE_LOCAL/lib/libpolybori.dylib
    rm -f $SAGE_LOCAL/lib/libpboriCudd.dylib
    rm -f $SAGE_LOCAL/lib/libgroebner.dylib
else
    rm -f $SAGE_LOCAL/lib/libpolybori.so
    rm -f $SAGE_LOCAL/lib/libpboriCudd.so
    rm -f $SAGE_LOCAL/lib/libgroebner.so 
fi
```

 * patches/SConstruct is missing, but in spkg-install you copy it over:

```
cp patches/SConstruct src/${PBDIR}/SConstruct
```

 * There seems to be some inconsitency between between PyPolyBori.patch, ./patches/PyPolyBoRi.py and ./src/polybori-0.5rc/pyroot/polybori/PyPolyBoRi.py
 * You removed an OSX 10.4 workaround (the removed the "-s" from LINKFLAGS below in SConstruct) that breaks compilation there and is a must fix we must have in our tree:

```
opts.Add('LINKFLAGS', "Linker flags", ['-s'], converter = Split)
opts.Add('LIBS', 'custom libraries needed for build', [], converter = Split)
```


Cheers,

Michael


---

Comment by tabbott created at 2008-07-11 03:35:15

I agree on that workaround.  

I'm a bit confused as to what happened to patches/SConstruct (which is supposed to be the OS X 10.4 fix).  It's easy to regenerate from SConstruct.patch and the actual SConstruct file.  I'm a bit puzzled by PyPolyBoRi.py not being what I recall as well.

I'm also confused regarding what happened with the repository.  I've posted a new version in the same place that should have none of these problems.

I think the patch is sage is likely wrong, however; I get

```
ImportError: /usr/lib/python2.5/site-packages/sage/rings/polynomial/pbori.so: undefined symbol: _Z20m4ri_build_all_codesv
```

when I try to run SAGE with this patch in my Debian build (this was masked before by a flint problem).

I observe that devel/sage-main/build/temp.linux-i686-2.5/sage/rings/polynomial/pbori.o contains references to _Z20m4ri_build_all_codesv, but devel/sage/sage/rings/polynomial/pbori.cpp refers to m4ri_build_all_codes (as do the .pyx files).  But this rewriting doesn't happen with the very similar m4ri_build_all_codes and m4ri_destroy_all_codes code in sage/sage/matrix/matrix_mod2_dense.c.

The only clear difference I can see here is that the pbori stuff is c++ based...


---

Comment by mabshoff created at 2008-07-11 03:40:28

Replying to [comment:4 tabbott]:

Hi Tim,

> I agree on that workaround.  


Good.

> I'm a bit confused as to what happened to patches/SConstruct (which is supposed to be the OS X 10.4 fix).  It's easy to regenerate from SConstruct.patch and the actual SConstruct file.  I'm a bit puzzled by PyPolyBoRi.py not being what I recall as well.
> 
> I'm also confused regarding what happened with the repository.  I've posted a new version in the same place that should have none of these problems.

I will take a look in a minute and do some build testing, followed by valgrinding to see if the dynamic lib problem has been fixed.

> I think the patch is sage is likely wrong, however; I get
> {{{
> ImportError: /usr/lib/python2.5/site-packages/sage/rings/polynomial/pbori.so: undefined symbol: _Z20m4ri_build_all_codesv
> }}}
> when I try to run SAGE with this patch in my Debian build (this was masked before by a flint problem).
> 
> I observe that devel/sage-main/build/temp.linux-i686-2.5/sage/rings/polynomial/pbori.o contains references to _Z20m4ri_build_all_codesv, but devel/sage/sage/rings/polynomial/pbori.cpp refers to m4ri_build_all_codes (as do the .pyx files).  But this rewriting doesn't happen with the very similar m4ri_build_all_codes and m4ri_destroy_all_codes code in sage/sage/matrix/matrix_mod2_dense.c.
> 
> The only clear difference I can see here is that the pbori stuff is c++ based...

We upgraded to a new m4ri version recently. IIRC PolyBoRi 0.5 is supposed to switch from its own static m4ri to using a shared one if so configured, so Sage's m4ri might get in the way here. But it might also be a C vs. C++ problem that might be fixed via some extern "C" sprinkled in the m4ri headers in case they are missing.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-11 03:43:28

IIRC correctly Martin is afk the weekend, but we might still catch him. So I added him to CC :)

Cheers,

Michael


---

Comment by malb created at 2008-07-11 09:53:00

This certainly looks like a C vs. C++ issue, that's all I can say for now without actually digging in.


---

Comment by malb created at 2008-07-11 15:14:41

Note that PolyBoRi 0.5 still ships its own M4RI and does not use the default M4RI installed (in Sage or the system). We should sit down with the authors at ISSAC and discuss how to change that :-)


---

Comment by mabshoff created at 2008-07-21 07:05:51

Replying to [comment:8 malb]:
> Note that PolyBoRi 0.5 still ships its own M4RI and does not use the default M4RI installed (in Sage or the system). We should sit down with the authors at ISSAC and discuss how to change that :-)

I am sitting next to Michael B. and he correctly pointed out that the issue is with the extension and not PolyBoRi itself.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-21 07:07:07

Note that #3195 might be resolved by this upgrade.

Cheers,

Michael


---

Comment by malb created at 2008-07-21 19:24:23

> I am sitting next to Michael B. and he correctly pointed out that the issue is with the extension and not PolyBoRi itself.

I don't understand what you mean by "the issue is with the extension".


---

Comment by mabshoff created at 2008-07-22 11:43:49

Hi Tim, Martin, Michael, Alexander,

the problem is that m4ri is now build as a C library in PolyBoRi. This requires that the m4ri header has some extern "C" header guards, which Martin will add in a new point release of m4ri. We will also attempt to make PolyBoRi use Sage's libm4ri instead of using its own copy, but I hope we can get that done in time for the freeze.

Cheers,

Michael


---

Comment by malb created at 2008-07-22 13:01:49

Replying to [comment:12 mabshoff]:
> the problem is that m4ri is now build as a C library in PolyBoRi. This requires that the m4ri header has some extern "C" header guards, which Martin will add in a new point release of m4ri. 

After thinking about this some more time, I came to the conclusion, that
 * future versions of M4RI will have the extern "C" guard in m4ri.h
 * the easiest fix is to add the guard to `pb_wrap.h` in clib.


---

Comment by malb created at 2008-07-22 13:05:58

Since the current spkg for 0.5 is broken, I won't provide the fix just now:

```
malb`@`road:/tmp/polybori-0.5rc$ ./spkg-install
./spkg-install: line 15: [: =: unary operator expected
cp: accessing `src/polybori-0.3/SConstruct': Not a directory
cp: accessing `src/polybori-0.3/pyroot/polybori': Not a directory
cp: accessing `src/polybori-0.3/Cudd/util/cpu_stats.c': Not a directory
Starting build...
Running build_polybori...
./spkg-install: line 38: cd: polybori-0.3: Not a directory

scons: *** No SConstruct file found.
File "/tmp/sage-3.0.4.rc1/local/lib/scons-0.97.0d20071212/SCons/Script/Main.py", line 826, in _main
Error building PolyBoRi.
```


but here is what needs to be added to pb_wrap.h

```
// M4RI
#define PACKED 1
#ifdef __cplusplus
extern "C" {
#include "M4RI/m4ri.h"
}
#else
#include "M4RI/m4ri.h"
#endif
```


which replaces


```
// M4RI
#define PACKED 1
#include "M4RI/packedmatrix.h"
#include "M4RI/grayflex.h"
```


What is the `#define PACKED 1` for btw.?


---

Comment by tabbott created at 2008-07-22 21:23:32

This change does seem to resolve the problems I was having with my Debian build.

The failure you're seeing with polybori-0.5rc.spkg is just a line that needs to be changed from 
"polybori-0.3" to "polybori-0.5rc" in spkg-install (I've posted a new version in my sage.math).

But after I make that change, I get compilation failures trying to build the polybori spkg in a stock 3.0.5 Sage install using gcc-4.3.  So, we're not done yet.


```
gcc -o M4RI/packedmatrix.o -c -std=c99 -O3 -ansi -Wno-long-long -Wreturn-type -g -fPIC -DNDEBUG -DPACKED -DHAVE_M4RI -DHAVE_IEEE_754 -DBSD -I/var/tmp/sage-3.0.5/spkg/build/polybori-0.5rc/src/boost_1_34_1.cropped -I/var/tmp/sage-3.0.5/local/include/python2.5 -Ipolybori/include -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd M4RI/packedmatrix.c
In file included from M4RI/packedmatrix.h:31,
                 from M4RI/packedmatrix.c:21:
M4RI/misc.h:241:8: warning: extra tokens at end of #endif directive
In file included from M4RI/packedmatrix.c:21:
M4RI/packedmatrix.h:135: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'void'
M4RI/packedmatrix.h:153: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'BIT'
M4RI/packedmatrix.h:166: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'void'
M4RI/packedmatrix.h:186: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'void'
M4RI/packedmatrix.h:207: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'void'
M4RI/packedmatrix.h:223: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'word'
In file included from M4RI/packedmatrix.c:21:
M4RI/packedmatrix.h:546:8: warning: extra tokens at end of #endif directive
In file included from M4RI/packedmatrix.c:22:
M4RI/parity.h:52: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'word'
M4RI/parity.h:87: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'word'
M4RI/packedmatrix.c:224: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'packedmatrix'
M4RI/packedmatrix.c:251: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'packedmatrix'
M4RI/packedmatrix.c: In function 'mzd_transpose':
M4RI/packedmatrix.c:298: warning: return makes pointer from integer without a cast
M4RI/packedmatrix.c: In function '_mzd_add_impl':
M4RI/packedmatrix.c:571: error: expected expression before '/' token
M4RI/packedmatrix.c:670:8: warning: extra tokens at end of #endif directive
M4RI/packedmatrix.c:712:8: warning: extra tokens at end of #endif directive
scons: *** [M4RI/packedmatrix.o] Error 1
scons: building terminated because of errors.
Error building PolyBoRi.
```



---

Comment by PolyBoRi created at 2008-07-22 21:42:00

The errors are due to -ansi, which is probably still in the spkg-patches of custom.py and/or SConstruct.

Best regards,
  Alexander


---

Comment by mabshoff created at 2008-08-08 16:06:19


```
Hello everybody,
I've put another release candidate for upcoming polybori 0.5 to sf.net:
http://sourceforge.net/project/showfiles.php?group_id=210499
Direct link:
http://sourceforge.net/project/downloading.php?group_id=210499&use_mirror=osdn&filename=polybori-0.5-2008-08-06.tar.gz&96560043
(A first rc was created for Tim's debianization some weeks ago.)

Please let us know about any issues.

Best regards,
 Alexander
```



---

Comment by malb created at 2008-09-01 13:52:11

updated patch


---

Attachment

Hi there,

I've uploaded an updated SPKG (not based on the rc Alexander pointed us to) here:

  http://sage.math.washington.edu/home/malb/spkgs/polybori-0.5rc.p1.spkg

and updated the attached patch. `sage -t sage/rings/` passes for me. I'v reverted #3104 too btw. and fixed the SPKG.txt.


---

Comment by mabshoff created at 2008-09-01 20:19:40

There are some changes from the polybori-0.3.1.pX spkgs that need to be ported forward:

```
changeset:   16:35ca591c94cd
tag:         tip
user:        mabshoff`@`bsd.local
date:        Tue Aug 19 16:26:33 2008 -0700
summary:     polybori-0.3.1.p5: Add 64 bit OSX support

changeset:   15:fa58118566ad
user:        mabshoff`@`sage.math.washington.edu
date:        Mon Jul 21 14:49:07 2008 -0700
summary:     polybori-0.3.1.p4: Use /usr/bin/env bash as shebang

changeset:   14:181f8b612d1b
user:        mabshoff`@`sage.math.washington.edu
date:        Sun May 18 06:45:23 2008 -0700
summary:     Add diffs for all changed files to the repo
```

I will look into this today.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-07 00:40:46

I have backported the changes into 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc0/polybori-0.5rc.p2.spkg

It passes build tests on 

 * linux x86-64 and Itanium
 * 32 and 64 bit OSX 10.5 (but the 10.4 fix is in the spkg)
 * Solaris

The patch looks good to me and passes doctests. In total: positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-07 00:46:59

Merged in Sage 3.1.2.rc0


---

Comment by mabshoff created at 2008-09-07 00:46:59

Resolution: fixed
