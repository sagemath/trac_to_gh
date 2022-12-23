# Issue 9718: iconv fails to build on Solaris 10 x86 64-bit - host fulvia

Issue created by migration from https://trac.sagemath.org/ticket/9718

Original creator: drkirkby

Original creation time: 2010-08-10 14:28:27

Assignee: drkirkby

CC:  jsp jhpalmieri leif

Using the host 'fulvia'

 * Dell Optiplex 755
 * 2.4 GHz Quad-Core Intel Core Q6600 
 * 8 GB RAM
 * Solaris 10 x86 (update 5, 5/08)
 * gcc 4.5.1 configured to use the Sun linker and GNU assembler from binutils-2.20.1. 
 * 64-bit build. 

iconv failed to build. See the attached log file. 

An identical issue was seen on disk.math using OpenSolaris, but I assumed that was because the tool set was rather old on disk.math - see #9405.

I've built iconv both 32-bit and 64-bit on several machines OK.

|          |    |           |          |     |      |        |       |
|----------|----|-----------|----------|-----|------|--------|-------|
|*Hardware*|*OS*|*Processor*|*hostname*|*gcc*|*Bits*|*Result*|*Notes*|
|Sun T5240|Solaris 10 update 7 05/2009|SPARC|t2.math|4.4.1|32-bit|OK||
|Sun T5240|Solaris 10 update 7 05/2009|SPARC|t2.math|4.4.1|64-bit|OK||
|Sun Blade 1000|Solaris 10 03/2005|SPARC|redstart (mine)|4.4.4|32-bit|OK||
|Sun Blade 1000|Solaris 10 03/2005|SPARC|redstart (mine)|4.4.4|64-bit|OK||
|Sun Fire X4540|OpenSolaris 11/2008|x86|disk.math|4.3.2|32-bit|??||
|Sun Fire X4540|OpenSolaris 11/2008|x86|disk.math|4.3.2|64-bit|*Fail*|#9405, but old tools|
|Dell Optiplex 755 |Solaris 10 update 5 05/2008|x86|fulvia`@`skynet|4.5.1|32-bit|OK||
|Dell Optiplex 755 |Solaris 10 update 5 05/2008|x86|fulvia`@`skynet|4.5.1|64-bit|*Fail*|This ticket|
|Sun Ultra 27|OpenSolaris 06/2009|x86|hawk (mine)|4.5.1|32-bit|OK||
|Sun Ultra 27|OpenSolaris 06/2009|x86|hawk (mine)|4.5.1|64-bit|OK||
With only two failures, it's to sure of any pattern, though so far. 

 * iconv has only failed to build on x86 processors. Always OK on SPARC.
 * iconv has only failed on 64-bit builds.
 * iconv seems to failed on older versions of Solaris/OpenSolaris and not the more recent versions.


---

Comment by drkirkby created at 2010-08-10 16:22:56

config.log of failed build 64-bit on host 'fulvia' which runs Solaris 10 on a quad core Intel Xeon


---

Attachment

Log file generated when building a 64-bit iconv on host 'fulvia', which runs Solaris 10 on an quad core Intel Xeon


---

Comment by drkirkby created at 2010-08-11 09:35:15

I've not get any feedback from the iconv developers, but Ralf Wildenhues, a libtool developer, was most helpful when I posted this to the libtool mailing list. libtool <at> gnu.org. 

With a few tricks it is possible to iconv to build the library, though it requires hacking of an auto-generated file, and to run modified commands manually, which may be difficult to implement as a Sage patch. 

A failed build log, which was created outside of Sage, can be found at

http://boxen.math.washington.edu/home/kirkby/failed-Solaris-10_x86-build-of-libiconv-1.13.1.tar.bz2

Dave


---

Comment by drkirkby created at 2010-08-29 12:41:19

Ralf Wildenhues, who is a *libtool* developer kindly took a look at this for me - iconv uses libtool. The solution is to use:



```
CC="gcc -m64"
```


rather than have 


```
CC=gcc
CFLAGS=-m64
```


(Of course, gcc and -m64 should not be hardcoded - use $CC and $CFLAG64 in place). But the basic problem is that setting -m64 in CLFAGS does not work for some packages, and iconv is one of them. `Numpy` `Pynac` and `Libfplll` are other packages which will not build properly if only `CFLAGS` is set. 

I will add the necessary changes to #9603, which initially started off as a very small fix to install iconv on HP-UX, but has now generated into an almost complete redesign of the iconv package. 

The solution Ralf found has been posted to the libtool mailing list, but I'll get it put in the iconv one too, so others hopefully don't hit this problem. 

I'm cc'ing Leif, so he knows why the change will need to be made to #9603.

Dave


---

Comment by leif created at 2010-08-29 14:51:46

Replying to [comment:4 drkirkby]:
> The solution is to use:


```
CC="gcc -m64"
```

> rather than have 

```
CC=gcc
CFLAGS=-m64
```


Honestly, that's well-documented in many installation instructions of packages using `autoconf` / `automake` and `libtool`... (`libtool` strips flags from `CFLAGS` et al., but *not* from `CC`.)


---

Comment by drkirkby created at 2010-08-29 14:57:07

Replying to [comment:5 leif]:
> Replying to [comment:4 drkirkby]:
> > The solution is to use:
> 
> {{{
> CC="gcc -m64"
> }}}
> > rather than have 
> {{{
> CC=gcc
> CFLAGS=-m64
> }}}
> 
> Honestly, that's well-documented in many installation instructions of packages using `autoconf` / `automake` and `libtool`... (`libtool` strips flags from `CFLAGS` et al., but *not* from `CC`.)
> 

I have come across the problem before I must admit. Strange thing is though, this works OK on:

 * OS X 64-bit
 * Numerous Solaris systems - see above table. 

I'll create a patch and add it to the HP-UX patch, #9603. 

Dave


---

Comment by drkirkby created at 2010-08-29 15:58:30

I'm attaching a file showing this now building fully on `fulvia` at Skynet  - the machine where `iconv-1.13.1.p2` had failed before. 

Since SAGE_CHECK was set to "yes", the test suite is run. Note there are 3 core dumps, but these are to be expected, and documented in messages printed to the screen. 


```
Running the test suite.
If you see 3 core dumps, do not be too alarmed. See
http://trac.sagemath.org/sage_trac/ticket/8270
This is a Solaris bug and can be safely ignored
http://bugs.opensolaris.org/bugdatabase/view_bug.do?bug_id=6550204
It will probably be fixed in later releases of Solaris 10
It was fixed in build 66 of OpenSolaris.
```


As such, I consider this issue is now resolved. A patch will be attached to #9603.

Dave


---

Comment by drkirkby created at 2010-08-29 15:59:45

iconv now building on 'fulvia' at Skynet


---

Attachment

*This ticket can be closed when #9603 gets merged*, since the relevant patch

  http://trac.sagemath.org/sage_trac/attachment/ticket/9603/9603-move-from-CFLAGS-to-CC.patch

is _there_ (integrated into iconv-1.13.1.p3).


---

Comment by chapoton created at 2020-06-26 18:50:25

Resolution: duplicate
