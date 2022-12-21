# Issue 7344: New libjpeg package

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-10-29 04:24:27

Assignee: mabshoff

CC:  david.kirkby@onetel.net kcrisman leif

This is used by PIL (c.f. #7273). Inclusion as an optional or even as a standard package would be helpful.

The package is here: http://sage.math.washington.edu/home/timdumol/libjpeg-7.p0.spkg


---

Comment by timdumol created at 2009-11-01 02:16:22

Changing status from new to needs_review.


---

Comment by mhampton created at 2009-11-17 15:41:01

There is an extra file, SPKG.txt~, in the package.

I don't know if this should block its inclusion (I think this should go in as an optional package ASAP so it gets wider testing) but the show function doesn't work on my intel mac, 10.4.11, opening a TIFF file:


```
sage: import Image
sage: im = Image.open("/Users/mh/Pictures/psym.tiff")
sage: print im.format, im.size, im.mode
TIFF (455, 495) 1
sage: im.show()
sage: dyld: Symbol not found: __cg_jpeg_resync_to_restart
  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /Volumes/E/sage-4.2.1/local/lib//libJPEG.dylib
```



---

Comment by mhampton created at 2009-11-17 15:42:16

Oops that was a TIFF example, but it happens with jpegs too:

```
sage: im = Image.open("/Users/mh/Pictures/v2shot.jpg")
sage: im.show()
sage: dyld: Symbol not found: __cg_jpeg_resync_to_restart
  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /Volumes/E/sage-4.2.1/local/lib//libJPEG.dylib
```



---

Comment by timdumol created at 2009-11-18 15:50:51

The error seems to be an issue with having multiple versions of libjpeg in OS X. Refer to: http://old.nabble.com/dyld:-Symbol-not-found:-__cg_jpeg_resync_to_restart-to9949988.html. I am unsure as to how to fix that problem (I haven ever used a Mac).


---

Comment by timdumol created at 2009-11-18 15:53:36

A new version without SPKG.txt~ is up at http://sage.math.washington.edu/home/timdumol/libjpeg-7.p1.spkg.


---

Comment by drkirkby created at 2009-12-03 05:01:06

This needs checking on Solaris


---

Comment by jhpalmieri created at 2009-12-22 06:13:40

When I try an example like mhampton's above (`im = Image.open(...), im.show()`, I get the message

```
ImportError: The _imaging C module is not installed
```

(This is on OS X 10.6.)  Is this an issue?


---

Comment by drkirkby created at 2010-01-10 04:12:47

Sorry, I did not  set up email notifications until recently, so cc'ing me did not help. I only stumbled across this when looking for tickets to review. I will check it on Solaris. 

Dave


---

Comment by drkirkby created at 2010-01-10 05:13:39

A few points looking at spkg-install, which is overly complicated following recent updates to sage-env. 

 * The recent changes to sage-env (#7818) will mean a *lot* of spkg-install can be removed. In particular most, if not all the SAGE64 stuff, as sage-env will automatically add the right flags to CFLAGS, CXFLAGS etc for a 64-bit build. It will not do this (yet) for LDFLAGS so it *may* be necessary to add that, but I'm not convinced it will be necessary. It needs testing on bsd.math without the LD flags set. If it builds, then forgot it all. If it needs LDFLAGS to have -m64, replace -m64 with 

```
if [ "x$SAGE64" = xyes ] ; then
  LDFLAGS="$LDFLAGS $CFLAG64" 
  export $LDFLAGS
fi
```

then it will work irrespective of the flag needed to generate 64-bit binaries. (Not all compilers need -m64, as others use -q64 and other flags). I'm not totally convinced LDFLAGS ever needs -m64, as I believe LDFLAGS gets passed to the linker. No linker I am aware of has the -m64 option (check GNU binutils manual if you wish). But I'm not 100% sure it is never needed. I think the right flag if needed is -64 for the GNU linker, but it is rarely needed, as normally the linker can work out whether a 32 or 64 bit binary is needed, based on the object files. The exception is when creasting shared libraries from archives, where the linker may not be able to determine this.
 * Remove the checks for the Sun compiler and adding -Wall with gcc. The updates to sage-env will add the -Wall for you with gcc. 
 * Remove the checks to see if there is a mix of Sun and GNU compilers - that is taken care of elsewhere now. 

 * Unless there is good reason, remove the 


```
: ${CP=cp}; CP="$CP -f"; export CP
: ${MV=mv}; MV="$MV -f"; export MV
: ${RM=rm}; RM="$RM -f"; export RM
```

as it was agreed recently (see sage-devel) that there is no need for there to be variables for very basic commands. However, if the source code makes use of $CP etc, then they might have to stay. But if possible, just use mv, cp etc. 

 * Someting called 'CC' is used here. I'm not sure what that is, but be aware the Sun C++ compiler is called 'CC' so there might be a name clash. Make sure the absolute path to CC is specified if it's not already done, otherwise it may break if the Sun C++ compiler is in the path. 

 * Give me a day or so, and I'll put on sage-devel a *considerably* simpler skeleton spkg-install which will remove 95% of this. 

It does actually build on Solaris, but the spkg-install could be reduced considerably in size, as most of these checks are now done in once place. 

I'll help you do this. 

Dave


---

Comment by drkirkby created at 2010-01-10 05:13:39

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2010-01-10 05:48:35

Replying to [comment:9 drkirkby]:
> [...]
>  * Give me a day or so, and I'll put on sage-devel a *considerably* simpler skeleton spkg-install which will remove 95% of this. 
> 
> It does actually build on Solaris, but the spkg-install could be reduced considerably in size, as most of these checks are now done in once place. 
> 
> I'll help you do this. 
> 
> Dave 
> 
>  

Perfect, thanks. The libjpeg makefile actually uses $CP, $RM and $MV, so that section can't be removed.


---

Attachment


---

Comment by drkirkby created at 2010-01-11 20:16:19

I've looked at this, and have attached a revised spkg-install, which is a lot simpler. However, there are some odd things about this. 

 * Why is the package called libjpeg-7.p1, rather than libjpeg-7 ? The .p0 is appended when a patch is applied, .p1 is used when a second patch is applied. This would therefore imply it's been patched twice, whereas in fact it has not. 
 * There is no need for a patches directory when there are no patches.
 * What is the purpose of this code 


```
: ${CP=cp}; CP="$CP -f"; export CP
: ${MV=mv}; MV="$MV -f"; export MV
: ${RM=rm}; RM="$RM -f"; export RM
```


I just took the libjpeg source code, then built it with:

```
$ ./configure --prefix=/tmp
$ make 
$ make install
```

and it all went ok, without me having to override 'cp', 'mv' or 'rm'. 

 * You would need to get William or someone else to look over the license. I know there is one requirement there, which is not a requirement of the GPL. That is, if you use their code, you must acknowledge them. Having had some GPL'ed code of mine ripped off without acknowledgment, I was a bit annoyed, but I've been told there is no requirement to acknowledge anyone if you use their GPL code. I am not a lawyer are more interested in the technical aspects than license conditions, but someone would need to verify this license is compatible. 

In the attacked in spkg-install I've left all the overriding of cp, but I don't feel it should be necessary. 

Dave


---

Comment by kcrisman created at 2010-08-02 17:59:33

See also [here](http://groups.google.com/group/sage-devel/browse_frm/thread/48f720062cc4e38b/ff817dfb819e5ce).


---

Comment by timdumol created at 2010-08-17 18:17:23

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-08-17 18:17:23

New package version here: http://sage.math.washington.edu/home/timdumol/libjpeg-7.p2.spkg

As stated in #7818, some makefiles depend on $RM being unset or set to "rm -f". The above code overrides any $RM setting, which otherwise causes compilation failure (at least for me).

I am unsure of the GPL compatibility of libjpeg's licensing, but this message on: http://www.mail-archive.com/mozilla-license`@`mozilla.org/msg00143.html seems to suggest that it is widely considered GPL compatible. Otherwise, we may want to consider libjpeg-turbo (http://sourceforge.net/projects/libjpeg-turbo/) and patch PIL to use that.

Regarding review of this package:

The package may be reviewed by using the PIL package, as above:


```
sage: import Image
sage: im = Image.open("<your-jpeg-file-here>")
sage: im.resize((im.size[0]/2,im.size[1]/2))
sage: print im.format, im.size, im.mode
TIFF (455, 495) 1
sage: im.show()
sage: im.save("wherever.jpg")
```



---

Comment by leif created at 2010-09-03 21:59:19

(I could have deleted Dave from the cc-list, but just added the missing trailing "t"...)


---

Comment by drkirkby created at 2011-04-08 08:11:12

Replying to [comment:13 timdumol]:
> New package version here: http://sage.math.washington.edu/home/timdumol/libjpeg-7.p2.spkg
> 
> As stated in #7818, some makefiles depend on $RM being unset or set to "rm -f". The above code overrides any $RM setting, which otherwise causes compilation failure (at least for me).

There's a much simpler way to unset RM than use


```
: ${RM=rm}; RM="$RM -f"; export RM
```


one can use:


```
unset RM
```


If a Makefile needs RM set, I feel it would be better to fix the Makefile and report that upstream. Likewise if a Makefile needs `rm -f`, it should use `rm -f`


---

Comment by mariah created at 2011-05-13 13:20:01

Changing status from needs_review to needs_work.


---

Comment by mariah created at 2011-05-13 13:20:01

If this package causes compilation failure, then it needs work, not
review.


---

Comment by timdumol created at 2011-08-02 18:29:37

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2011-08-02 18:29:37

.p1 gave compilation failure. .p2 fixes it.


---

Comment by timdumol created at 2011-08-02 21:58:11

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2011-08-02 21:58:11

It seems that libjpeg's license is not compatible with GPL, according to: http://www.thomasalspaugh.org/pub/osl-sps/libjpeg8c.html. Also, libjpeg-turbo seems to be significantly faster than libjpeg, while being licensed under GPL. I'm making a package for that now.


---

Comment by timdumol created at 2011-08-02 22:21:17

Here is the new libjpeg-turbo package: http://sage.math.washington.edu/home/timdumol/libjpeg_turbo-1.1.1.spkg


---

Comment by timdumol created at 2011-08-02 22:21:17

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2011-08-02 22:22:42

Review instructions are as above. This definitely needs testing on a Mac, as I am unsure as to whether the patches that were included in the libjpeg package are required for libjpeg-turbo. This version does not include those patches.


---

Comment by jhpalmieri created at 2011-08-02 23:51:35

This fails to build on my OS X box. Here is the tail end of the log:

```
checking whether to use version script when building libjpeg-turbo... yes
checking whether to include arithmetic encoding support... yes
checking whether to include arithmetic decoding support... yes
checking if we have SIMD optimisations for cpu type... yes (i386)
checking for nasm... nasm
checking for object file format of host system... Mach-O
checking for object file format specifier (NAFLAGS) ... -fmacho -DMACHO
checking whether the assembler (nasm -fmacho -DMACHO) works... yes
checking whether the linker accepts assembler output... no
configure: error: configuration problem: maybe object file format mismatch.
Failed to configure libjpeg ... exiting
```



---

Comment by jhpalmieri created at 2011-08-02 23:51:35

Changing status from needs_review to needs_work.


---

Comment by leif created at 2011-08-03 00:37:01

Replying to [comment:21 jhpalmieri]:
> This fails to build on my OS X box. Here is the tail end of the log:

Haven't looked at the spkg yet, but perhaps attach your `config.log`; I'm not sure if (i.e., rather doubt that) we intend to use `nasm` at all, which probably requires some additional `configure` option (if `nasm` is installed) or perhaps setting `AS`.


---

Comment by jhpalmieri created at 2011-08-03 03:29:02

Replying to [comment:22 leif]:
> Replying to [comment:21 jhpalmieri]:
> > This fails to build on my OS X box. Here is the tail end of the log:
> 
> Haven't looked at the spkg yet, but perhaps attach your `config.log`

I've posted it here: [http://sage.math.washington.edu/home/palmieri/misc/config.log](http://sage.math.washington.edu/home/palmieri/misc/config.log).


---

Comment by leif created at 2011-08-03 05:01:56

Replying to [comment:23 jhpalmieri]:
> I've posted it here: [http://sage.math.washington.edu/home/palmieri/misc/config.log](http://sage.math.washington.edu/home/palmieri/misc/config.log).

Hmmm, the error is just that `nasm` doesn't produce 64-bit object files by default. (`configure` should notice that, and use `-fmacho64` instead of `-fmacho`.)

John, did you set `SAGE64=yes`?

Haven't yet looked if there are further `configure` options (`./configure --help` doesn't show appropriate ones), or what happens if `nasm` isn't installed. (Guess it then just defaults to C implementations rather than using GCC with inline assembly; MacOS X / XCode doesn't have a `gas` IIRC.)

----

Btw., there's crap in the spkg, and I can't read the Mercurial files:

```sh
$ ls -a
.   .hg        .hgignore~     spkg-install       SPKG.txt       src
..  .hgignore  .hgignore.swp  .spkg-install.swp  .SPKG.txt.swp
$ hg log ; hg status
abort: requirement 'dotencode' not supported!
abort: requirement 'dotencode' not supported!
```


Also, unfortunately Tim has deleted the old "patches" that were applied on MacOS X

```sh
# This was needed for libjpeg. Is this needed for libjpeg-turbo?
#if [ -n "`uname -s | grep Darwin`" ]; then
#   $CP ../patches/config.sub .
#   $CP ../patches/config.guess .
#   # Required for Mac OS (http://jetfar.com/libjpeg-and-python-imaging-pil-on-snow-leopard/)
#   ./configure --enable-shared --enable-static --prefix="$SAGE_LOCAL"
#else
./configure --prefix="$SAGE_LOCAL"
#fi
```

though that's not necessarily the problem.


---

Comment by jhpalmieri created at 2011-08-03 05:35:18

> John, did you set SAGE64=yes?

I hadn't, because with OS X 10.6 on 64-bit machines, it shouldn't be necessary.  I just tried it anyway, and got the same result.

The file BUILDING.txt in the src directory says this:

```
-- NASM
   * 0.98, or 2.01 or later is required for a 32-bit build
   * NASM 2.00 or later is required for a 64-bit build
   * NASM 2.07 or later is required for a 64-bit build on OS X.  This can be
     obtained from MacPorts (http://www.macports.org/).
```

The default version of nasm seems to be 0.98.40, or at least that's what I have installed.  The same file also says this; perhaps this is the way to go:

```
32-bit Library Build on 64-bit OS X
-----------------------------------

Add

  CFLAGS='-O3 -m32' LDFLAGS=-m32

to the configure command line.
```

If I configure with those options, it seems to succeed.  That is, I ran "sage -sh", then changed to the directory `sage/spkg/build/libjpeg_turbo-1.1.1/src` and ran

```
CFLAGS='-O3 -m32' LDFLAGS=-m32 ./configure --prefix=/Applications/sage/local
```

Then `make` succeeded.  I haven't tried `make install` or testing it inside of Sage.


---

Comment by jhpalmieri created at 2011-08-03 05:41:10

> perhaps this is the way to go

Or maybe not; either I did something wrong or I can't use the 32-bit library in the 64-bit Sage build, but it doesn't seem to work in Sage: it keeps telling me "IOError: decoder jpeg not available".  Maybe we should require nasm as a prerequisite on 64-bit OS X.  (That could be another spkg.)


---

Comment by leif created at 2011-08-03 06:05:55

Replying to [comment:26 jhpalmieri]:
> Or maybe not; either I did something wrong or I can't use the 32-bit library in the 64-bit Sage build

Yeah, you cannot use both 32- and 64-bit libraries or modules within / from the same executable.

> Maybe we should require nasm as a prerequisite on 64-bit OS X.  (That could be another spkg.)

I wonder if it builds (on MacOS X) without assembly parts (perhaps with `--without-simd` passed to `configure`), as I mentioned above.

(You could also try temporarily "removing" `nasm` by renaming it to something obscure and then run `./configure`.)

If `libjpeg` stays an optional package, we could of course also add an optional `nasm` package (if the licence allows this), but I won't add more (binary?) standard spkgs just to accomplish prerequisites. Fortran is IMHO bad enough.

Or we have to resort to some other (upstream) `libjpeg` package.


---

Comment by leif created at 2011-08-03 06:23:59

Replying to [comment:27 leif]:
> I wonder if it builds (on MacOS X) without assembly parts (perhaps with `--without-simd` passed to `configure`), as I mentioned above.

Yep, configuring with `--without-simd` should work, as the only assembler source files are all in `src/simd/`.


---

Comment by timdumol created at 2011-08-03 09:21:24

Replying to [comment:24 leif]:
> Replying to [comment:23 jhpalmieri]:
> > I've posted it here: [http://sage.math.washington.edu/home/palmieri/misc/config.log](http://sage.math.washington.edu/home/palmieri/misc/config.log).
> 
> Hmmm, the error is just that `nasm` doesn't produce 64-bit object files by default. (`configure` should notice that, and use `-fmacho64` instead of `-fmacho`.)
> 
> John, did you set `SAGE64=yes`?
> 
> Haven't yet looked if there are further `configure` options (`./configure --help` doesn't show appropriate ones), or what happens if `nasm` isn't installed. (Guess it then just defaults to C implementations rather than using GCC with inline assembly; MacOS X / XCode doesn't have a `gas` IIRC.)
> 
> ----
> 
> Btw., there's crap in the spkg, and I can't read the Mercurial files:
> {{{
> #!sh
> $ ls -a
> .   .hg        .hgignore~     spkg-install       SPKG.txt       src
> ..  .hgignore  .hgignore.swp  .spkg-install.swp  .SPKG.txt.swp
> $ hg log ; hg status
> abort: requirement 'dotencode' not supported!
> abort: requirement 'dotencode' not supported!
> }}}

Sorry, I used a pretty recent version of Mercurial to create the repository, and it seems that it is backwards incompatible. I'll use `sage -hg` instead. I'll delete the trash files.

> 
> Also, unfortunately Tim has deleted the old "patches" that were applied on MacOS X
> {{{
> #!sh
> # This was needed for libjpeg. Is this needed for libjpeg-turbo?
> #if [ -n "`uname -s | grep Darwin`" ]; then
> #   $CP ../patches/config.sub .
> #   $CP ../patches/config.guess .
> #   # Required for Mac OS (http://jetfar.com/libjpeg-and-python-imaging-pil-on-snow-leopard/)
> #   ./configure --enable-shared --enable-static --prefix="$SAGE_LOCAL"
> #else
> ./configure --prefix="$SAGE_LOCAL"
> #fi
> }}}
> though that's not necessarily the problem.


---

Comment by timdumol created at 2011-08-03 09:26:10

Replying to [comment:26 jhpalmieri]:
> > perhaps this is the way to go
> 
> Or maybe not; either I did something wrong or I can't use the 32-bit library in the 64-bit Sage build, but it doesn't seem to work in Sage: it keeps telling me "IOError: decoder jpeg not available".  Maybe we should require nasm as a prerequisite on 64-bit OS X.  (That could be another spkg.)

I am uncertain, but I believe that you need to reinstall PIL (sage -f pil) in order to enable JPEG capabilities.


---

Comment by leif created at 2011-08-03 11:01:52

I think we should simply check whether `nasm` is installed (`command -v nasm >/dev/null`), and if so, its version (`nasm -v`), and then -- depending on the operating system (especially 32-bit vs. 64-bit on Darwin) -- decide whether we configure with `--without-simd` or not.

This should work on all platforms, and this way machines having (at least) the required version installed won't suffer from not using faster implementations.

If `SAGE_FAT_BINARY=yes`, we should perhaps disable it too.

According to the docs, it might also be necessary to either pass `--build=...` or update the *very old* `config.guess`, at least on / for 64-bit Darwin (MacOS X >=10.6, or 10.5 if `SAGE64=yes`). Maybe setting `ABI` accordingly also works.


---

Comment by jhpalmieri created at 2011-08-03 15:50:46

Building with `--without-simd` and then reinstalling PIL allows me to execute the code above (although `im.format` is `None`).


---

Comment by jhpalmieri created at 2011-08-03 22:17:09

As with the spkg at #7345, you should also provide a patch to the scripts repo, adding the appropriate files to .hgignore there.


---

Comment by leif created at 2011-08-04 11:51:37

Replying to [comment:33 jhpalmieri]:
> As with the spkg at #7345, you should also provide a patch to the scripts repo, adding the appropriate files to .hgignore there.

... if we really want to install any executables as well.

Using them from Sage would certainly be inefficient, and `local/bin/` is already filled up with a lot of .... useful tools.


---

Comment by was created at 2011-08-24 23:46:26

Changing keywords from "" to "sd32".


---

Comment by was created at 2011-11-14 16:31:26

Replying to [comment:18 timdumol]:
> It seems that libjpeg's license is not compatible with GPL, 
> according to: http://www.thomasalspaugh.org/pub/osl-sps/libjpeg8c.html. 
> Also, libjpeg-turbo seems to be significantly faster than libjpeg, while being 
> licensed under GPL. I'm making a package for that now.

There is a discussion of the libjpeg-turbo license by the main developer (I think) here: http://sourceforge.net/projects/libjpeg-turbo/forums/forum/1086868/topic/4519797

It's definitely "licensed under GPL".   However, it seems to be licensed under a subset of LGPL, which would definitely be GPL compatible.


---

Comment by was created at 2011-11-14 16:34:36

I tried building libjpeg_turbo-1.1.1.spkg on OS X 10.7 (Lion) with XCode 4.2.x and it fails during the ./configure stage:

```
...
checking whether the assembler (nasm -fmacho -DMACHO) works... yes
checking whether the linker accepts assembler output... no
configure: error: configuration problem: maybe object file format mismatch.
Failed to configure libjpeg ... exiting

real	0m14.878s
```



---

Comment by jdemeyer created at 2014-11-13 14:03:54

Changing component from packages: standard to packages: optional.


---

Comment by mkoeppe created at 2021-08-26 02:40:52

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2021-08-26 02:40:52

outdated, should close


---

Comment by jhpalmieri created at 2021-08-26 03:49:59

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2021-09-01 06:17:10

Resolution: invalid
