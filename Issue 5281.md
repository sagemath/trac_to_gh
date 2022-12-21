# Issue 5281: Update tachyon to Version 0.98.1 (latest upstream)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-16 04:41:49

Assignee: mabshoff

CC:  drkirkby mhampton vbraun

In Sage we are currently shipping some 0.98.beta release of tachyon. Update to the official upstream release 0.98.1.

This will require cleaning up SPKG.txt


---

Comment by aginiewicz created at 2009-04-21 18:03:03

good news - the 0.98.1 don't need the "-fno-crossjumping -fno-reorder-blocks" GCC 4.2/4.3 fix


---

Comment by aginiewicz created at 2009-04-23 18:35:20

New version is out, 0.98.2 had compilation error on non-threaded builds and 0.98.1 also had similar problem as #3710 (but not in architectures used by Sage, just linux-thr-ogl), so it's kind of recommended to skip straight to 0.98.3


---

Comment by leif created at 2010-08-26 19:34:35

The whole spkg really needs clean-up. (And Sage's *beta* version is out of date since at least 19 month; by now, the current one is [still] 0.98.9 - as in the ticket's title, last updated by Mariah.)

I have absolutely no idea why `spkg-install` does the following on Linux:

```sh
    make linux-thr
    if [ $? -ne 0 ]; then
        echo "Maybe your system is 64-bit; trying again."
        if [ `uname -m` = "ia64" ]; then
          echo "ia64"
          make linux-ia64-thr
        else
          echo "64-bit arch"
          make linux-64-thr
        fi
    fi
```

This might even "fail" (building just a 32-bit version on 64-bit Linuces) when the required (multi-arch/32-bit) libraries are present. And if the 32-bit build fails for some reason on a real 32-bit system, it doesn't make sense to attempt a 64-bit build.


---

Comment by leif created at 2010-08-26 19:42:36

Remove assignee mabshoff.


---

Comment by leif created at 2010-08-26 20:30:37

Dave, sadly enough, this ticket is still "new".

I think you've already fixed the Solaris issues, but if Tachyon ever gets updated in Sage, you should probably take a look at the new spkg, making sure it will still work on Solaris.


---

Comment by drkirkby created at 2010-08-26 21:04:05

Replying to [comment:6 leif]:
> Dave, sadly enough, this ticket is still "new".
> 
> I think you've already fixed the Solaris issues, but if Tachyon ever gets updated in Sage, you should probably take a look at the new spkg, making sure it will still work on Solaris.
Thank you Leif, 

personally I'm not going to look at updating this. I just hope whoever updates it does check it on Solaris. The code you showed is clearly dumb, though fortunately will not bother Solaris or any real Unix system. 

Unfortunately, having an f***ing clue what you are doing when it comes to writing software is not a perquisite to contributing to Sage's source code, or to reviewing the changes made by others with a similar lack of skill. 

Michael Abshoff should also be deleted as the package maintainer. Perhaps even William too, as he does not appear to be maintaining it. 

Dave


---

Comment by mhampton created at 2010-09-03 12:55:56

Set assignee to mhampton.


---

Comment by mhampton created at 2010-09-03 12:56:45

I'll try to give this a shot.  It looks like there are lots of important upstream improvements.


---

Comment by leif created at 2010-09-03 22:50:38

Also, the `dist/` (Debian) directory should be removed, cf. #5903.


---

Comment by mhampton created at 2010-09-03 23:10:10

An attempt at a new package is here:

http://sage.math.washington.edu/home/mhampton/tachyon-0.98.9.spkg

This installs fine on a mac (10.5), 64-bit linux, and seems OK on t2 (Solaris).  My t2 build isn't completely working so I did not actually check it on the notebook on that system.

I removed the dist directory, and tried to improve the SPKG.txt somewhat as well.


---

Comment by mhampton created at 2010-09-03 23:10:10

Changing status from new to needs_review.


---

Comment by leif created at 2010-09-04 01:42:02

Replying to [comment:11 mhampton]:
> An attempt at a new package is here:
> 
> http://sage.math.washington.edu/home/mhampton/tachyon-0.98.9.spkg

Hmmm, you somehow omitted / deleted the Mercurial repository.

I'll though give it a try...


---

Comment by leif created at 2010-09-04 01:42:02

Changing type from defect to enhancement.


---

Comment by leif created at 2010-09-04 02:11:36

`spkg-install` still needs work. (I could do that as soon as there's a repository...)

Should we add some (simple) `spkg-check`?

Also, there are some upstream files I think we could delete. (I'll have to take a closer look.)


---

Comment by leif created at 2010-09-04 02:20:07

We should also "install" (copy) the copyright notice somewhere into the Sage tree, at least for binary Sage distributions (e.g. `SAGE_LOCAL/bin/Copyright.Tachyon`).


---

Comment by mhampton created at 2010-09-04 20:42:41

OK, I added the mercurial repository back in and updated it.  I also did as you suggested and copied the tachyon copyright notice into SAGE_LOCAL/bin/ as "Tachyon-Copyright".  
Thanks for looking at it!
I'm not sure how to write a good spkg-check.  The doctests for Tachyon should catch most problems I think.


---

Comment by kcrisman created at 2010-09-21 18:31:27

This installed fine on OS X 10.4 PPC and `interfaces/tachyon.py` passed all tests.


---

Comment by leif created at 2010-09-21 20:25:48

The last change to `spkg-install` isn't committed.

But please let us (me?) clean-up `spkg-install` further...

(If us=me it'll perhaps take until Monday; but I don't mind doing it.)


---

Comment by drkirkby created at 2010-09-21 20:50:47

I just tried it on 32-bit OpenSolaris and it worked ok. It will clearly need checking on Solaris 10 on SPARC too, as that's a supported OS. 

There are some directories:


```
tachyon-0.98.9/src/msvc/
tachyon-0.98.9/src/msvc/CVS/
tachyon-0.98.9/src/msvc/CVS/Entries
tachyon-0.98.9/src/msvc/CVS/Repository
```


I think in a case like this, it would be worth deleting the Microsoft Visual C stuff. That could be added to the `Special Update/Build Instructions` Since Leif intends overhauling the package, he might consider that. 

I guess given it's been open 19 months, waiting until Monday should not be a major problem! 

Dave


---

Comment by leif created at 2010-09-21 21:08:44

Yes.

```sh
leif`@`quadriga:~/Sage/spkgs/tachyon-0.98.9$ du -h src
16K	src/src/CVS
680K	src/src
16K	src/msvc/CVS
16K	src/msvc/tachyon/libtachyon/CVS
4.0K	src/msvc/tachyon/libtachyon/Debug
1.4M	src/msvc/tachyon/libtachyon/Release
1.5M	src/msvc/tachyon/libtachyon
16K	src/msvc/tachyon/CVS
16K	src/msvc/tachyon/tachyon/CVS
4.0K	src/msvc/tachyon/tachyon/Debug
840K	src/msvc/tachyon/tachyon/Release
892K	src/msvc/tachyon/tachyon
4.0K	src/msvc/tachyon/Debug
16K	src/msvc/tachyon/tachyon_ogl/CVS
4.0K	src/msvc/tachyon/tachyon_ogl/Debug
4.0K	src/msvc/tachyon/tachyon_ogl/Release
36K	src/msvc/tachyon/tachyon_ogl
4.0K	src/msvc/tachyon/Release
2.8M	src/msvc/tachyon
2.8M	src/msvc
4.0K	src/compile
16K	src/unix/CVS
308K	src/unix
16K	src/docs/CVS
232K	src/docs/tachyon
808K	src/docs
16K	src/librtvi/CVS
44K	src/librtvi
16K	src/demosrc/CVS
248K	src/demosrc
4.9M	src
```



---

Comment by mhampton created at 2010-09-24 13:25:32

Leif - are you going to work on this?  I'd like to keep it rolling along with #9855 (which I need to work on a little more).  I agree that the msvc folder can be deleted as long as we put a note in the SPKG.txt about it.


---

Comment by mhampton created at 2010-09-24 13:25:42

Changing status from needs_review to needs_work.


---

Comment by mhampton created at 2010-09-24 13:32:01

I over-wrote my spkg at [http://sage.math.washington.edu/home/mhampton/tachyon-0.98.9.spkg](http://sage.math.washington.edu/home/mhampton/tachyon-0.98.9.spkg) with a version with the msvc folder deleted.  That saves quite a bit of space.


---

Comment by leif created at 2010-09-24 13:42:03

Replying to [comment:20 mhampton]:
> Leif - are you going to work on this?

I think over the weekend (unless alpha2 gets released ;-) ) or at least within the next days.

Otherwise I'll open a follow-up.

> I'd like to keep it rolling along with #9855 (which I need to work on a little more).

Doesn't look as if #9855 depended on the new Tachyon, but did you test it with the new one?

> I agree that the msvc folder can be deleted as long as we put a note in the SPKG.txt about it.

Yes. It's also IMHO compatible with the copyright, though I'm not a lawyer.


---

Comment by leif created at 2010-09-24 13:43:21

Dave, are you attempting to make it build on AIX?


---

Comment by leif created at 2010-09-24 13:45:50

Replying to [comment:24 leif]:
> Dave, are you attempting to make it build on AIX?

(If it doesn't, I think you only tested the old one. Also, I think it's just Sage that does not even try to build Tachyon on AIX.)


---

Comment by drkirkby created at 2010-09-24 15:26:50

Replying to [comment:25 leif]:
> Replying to [comment:24 leif]:
> > Dave, are you attempting to make it build on AIX?
> 
> (If it doesn't, I think you only tested the old one. Also, I think it's just Sage that does not even try to build Tachyon on AIX.) 

Leif, 

I've just looked - this will *not* build on AIX with gcc for two reasons. 
 * There's nothing in `spkg-install` to handle AIX
 * The AIX targets in `src/unix/Make-arch`, which are `aix-thr`, `aix-64-thr`, `aix-mpi` and `aix` all assume an IBM compiler is used. 

The same situation exists with HP-UX - the file `src/unix/Make-arch` assumes the use of the HP compiler for all the HP-UX targets. 

I will create two new targets for the file `patches/Make-arch`, which I will call

 * `aix-generic`
 * `hpux-generic`

which will use $CC as a compiler, and not assume a propriety compiler with any special flags. Hopefully that will work with gcc and any reasonable set of flags. 

Since you intend cleaning up the ticket, if I attach that as a unified diff patch, can you make sure that the target `aix-generic` is used on AIX (where $UNAME = AIX) and `hpux-generic` is used on HP-UX (where $UNAME=HP-UX)? 

I might as well do the HP-UX targets at the same time as the AIX ones, though building on AIX looks a lot easier than building on HP-UX - at least with the hardware I own. 

Note there are already several targets been added various platforms, including, but not limited to Solaris. 

Let me know how you want to proceed. We might as well do AIX and HP-UX at the same time. 

Dave


---

Comment by leif created at 2010-09-24 15:33:58

Replying to [comment:26 drkirkby]:
> Since you intend cleaning up the ticket, if I attach that as a unified diff patch, can you make sure that the target `aix-generic` is used on AIX (where $UNAME = AIX) and `hpux-generic` is used on HP-UX (where $UNAME=HP-UX)? 

Sure. If the HP-UX and / or AIX builds do not fully work, we can still open a follow-up for these platforms.


---

Attachment

Patch to add AIX and HP-UX support.


---

Comment by drkirkby created at 2010-09-25 11:44:05

As noted at #9997, Tachyon did not even attempt to build on AIX. Looking at the code, I realise the exact same thing would happen on HP-UX too. I decided to correct both AIX and HP-UX issues at the same time. 

I've added 

http://boxen.math.washington.edu/home/kirkby/patches/tachyon-0.98.9.spkg

`md5=501a1f9667a7bdedcb8f0d3c361b39fb`

which has 4 new targets: 

    * `aix-generic`
    * `aix-generic-thr`
    * `hpux-generic`
    * `hpux-generic-thr`

The targets ending in `-thr` are threaded versions and build OK on both AIX and HP-UX. But following the convention of the `src/unix/Make-arch` file, I've created both threaded and unthreaded targets. 

Since William seems intent on moving disk storage from enterprise grade SCSI disks on a machine with an uptime over over 600 days, to a 2 TB consumer grade external USB disk on a machine with an average uptime of about a month, I thought it wise to make a backup copy at the following site, which will be *much* slower due to my more limited Internet bandwidth!

http://www.althorne.org/tachyon-0.98.9.spkg

As Leif intends cleaning this up, there's little point in me making any significant changes to spkg-install, as Leif and I differ widely on how we write scripts! 

But I've done sufficient in `spkg-install` to check Tachyon at least builds with gcc on both AIX and HP-UX. Since I can't run any doctests on those platforms, I can't say how they work, but at least they build. As Leif says, if there are any issues on AIX, we can open another ticket. The same is true for HP-UX of course. 

Leif might want to change the compiler options for when SAGE_DEBUG=yes. If so, feel free. But -O2 -g should be safe, which is what I've set the calls to the AIX and HP-UX targets to in `spkg-install`.

I hope this is a step in the right direction. It's been open 20 months, so lets hope it can be cleared up soon. 

Dave


---

Comment by mhampton created at 2010-09-25 23:35:55

I think you might have confused me (Marshall Hampton, mhampton) with Mike Hansen (mhansen).


---

Comment by vbraun created at 2010-09-26 14:46:22

While we are at it, can we add the patch to build a shared library? Debian and Fedora both patch tachyon to produce a shared library. This would then enable us to write a reasonable previewer in cython without pushing temporary files around. Realtime raytracing is the future, they say :-)


---

Attachment

Debian shared library patch for reference


---

Comment by leif created at 2010-09-26 15:04:27

Replying to [comment:31 vbraun]:
> While we are at it, can we add the patch to build a shared library? Debian and Fedora both patch tachyon to produce a shared library. This would then enable us to write a reasonable previewer in cython without pushing temporary files around. Realtime raytracing is the future, they say :-)

Certainly we could, but IMHO out of the scope of _this_ ticket. I think we should first provide an spkg with just the current upstream (stand-alone) version, which has to be tested as well.

The patch needs to be tested on various systems; it e.g. calls `make` instead of `$(MAKE)` inside the Makefile, which one should never do.


---

Comment by leif created at 2010-09-26 15:09:31

... and `-soname` works with the GNU linker, but e.g. not Sun's.


---

Comment by drkirkby created at 2010-09-26 18:30:05

The method used to determine the target in `spkg-install` seems crazy to me. First it tries  using the the target `linux`, which specifically forces a 32-bit build, with the `-m32` flag. 

To me at least, on `sage.math`, I can compile with `-m32` and create a 32-bit binary:


```
kirkby`@`sage:~$ cat test.c
#include <stdio.h>

int main() {
printf("ddd");
}
kirkby`@`sage:~$ gcc test.c
kirkby`@`sage:~$ file a.out
a.out: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), for GNU/Linux 2.6.8, dynamically linked (uses shared libs), not stripped
kirkby`@`sage:~$ gcc -m32 test.c
kirkby`@`sage:~$ file a.out
a.out: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), for GNU/Linux 2.6.8, dynamically linked (uses shared libs), not stripped
```


So I would expect this to build 32-bit in most cases on Linux. 

Only if the 32-bit build fails does it try a 64-bit build!! 

Note for AIX and HP-UX, I did not bother with any such flags, but just let it read CFLAGS, where one could add `-m64` or whatever flag one needs.


---

Comment by leif created at 2010-09-26 18:39:55

Replying to [comment:35 drkirkby]:
> The method used to determine the target in `spkg-install` seems crazy to me. First it tries  using the the target `linux`, which specifically forces a 32-bit build, with the `-m32` flag. 
> 
> To me at least, on `sage.math`, I can compile with `-m32` and create a 32-bit binary.
> [...]
> So I would expect this to build 32-bit in most cases on Linux.

No. The necessary 32-bit libraries are rarely installed on 64-bit Linux systems.
 
> Only if the 32-bit build fails does it try a 64-bit build!! 

See [comment:4 this comment above]; that's what definitely has to be cleaned up (i.e., removed).


---

Comment by leif created at 2010-09-26 18:50:32

This is the "typical" behavior:

```sh
$ echo "int main(){return 0;}" > foo.c && gcc -m32 foo.c
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-linux-gnu/4.4.3/libgcc.a when searching for -lgcc
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-linux-gnu/4.4.3/libgcc.a when searching for -lgcc
/usr/bin/ld: cannot find -lgcc
collect2: ld returned 1 exit status
```



---

Comment by leif created at 2010-09-26 19:09:28

It should simply be:

```sh
    ...
    case "`uname -m`" in
      i?86)
        $MAKE linux-thr;;
      ia64)
        $MAKE linux-ia64-thr;;
      *)
        $MAKE linux-64-thr
    esac
    ...
```



---

Comment by leif created at 2010-09-26 19:12:39

(At least if we don't support Linux on SPARC, PPC etc.)


---

Comment by drkirkby created at 2010-09-26 19:49:21

Replying to [comment:37 leif]:
> This is the "typical" behavior:
> {{{
> #!sh
> $ echo "int main(){return 0;}" > foo.c && gcc -m32 foo.c
> /usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-linux-gnu/4.4.3/libgcc.a when searching for -lgcc
> /usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-linux-gnu/4.4.3/libgcc.a when searching for -lgcc
> /usr/bin/ld: cannot find -lgcc
> collect2: ld returned 1 exit status
> }}}

Well,
I don't know how _typical_ that is, but it's certainly not the case on sage.math, which run Ubunta. 


```
kirkby`@`sage:~$  echo "int main(){return 0;}" > foo.c && gcc -m32 foo.c
kirkby`@`sage:~$ file a.out
a.out: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), for GNU/Linux 2.6.8, dynamically linked (uses shared libs), not stripped
kirkby`@`sage:~$ 
```


I can see in some cases trying to build more than once might be sensible, but clearly what currently exists is absurd.


---

Comment by leif created at 2010-09-26 20:17:43

Replying to [comment:40 drkirkby]:
> Well,
> I don't know how _typical_ that is, but it's certainly not the case on sage.math, which run Ubunta

So what? Some people configure GCC with multi-lib support, and some install the necessary 32-bit libraries. On such systems, the current scheme "fails" in that it builds a slower 32-bit executable instead of a 64-bit one, as I noted in one of my first comments here.

But I'm not aware of any Linux distribution (at least of the "major" ones) that ships with / installs these by default. So the "typical" scenario on 64-bit Linuces is that the 32-bit build fails and a 64-bit build is tried. Although that's odd by itself, it's irrelevant, since the scheme fails on other systems, like sage.math (or some of my machines). That's why I'd change it to what I've posted.


---

Comment by leif created at 2010-09-26 20:45:30

By the way, if you build a dynamically linked (which is the default) 32-bit executable on sage.math (e.g. when preparing a Sage binary distribution), this won't run on 64-bit Linuces without the necessary libs.


---

Comment by drkirkby created at 2010-09-26 20:54:18

Replying to [comment:39 leif]:
> (At least if we don't support Linux on SPARC, PPC etc.)
According to the Sage installation guide:

http://www.sagemath.com/doc/installation/source.html

_As of this writing, Sage is known to work on Linux (32-bit x86, 64-bit x86-64, IA64, or 32-bit PPC)_

http://wiki.sagemath.org/SupportedPlatforms

says Sage is supported on 32-bit PPC too. There are pages on 64-bit PPC and MIPS ports too, though I'm not aware of anyone working on them. So if there are targets, it would be worth considering adding them. But I would forget about Linux on SPARC - I can't imagine anyone wanting to port Sage to SPARC Linux. 

Dave


---

Comment by leif created at 2010-09-26 21:19:59

Replying to [comment:43 drkirkby]:
> http://wiki.sagemath.org/SupportedPlatforms
> 
> says Sage is supported on 32-bit PPC too. There are pages on 64-bit PPC and MIPS ports too, though I'm not aware of anyone working on them. So if there are targets, it would be worth considering adding them.

Yeah, there's even support for Linux on Playstation 2 and DEC Alpha. (And PPC, but only 32-bit I think.)

Does anyone port Sage to the PS2?


---

Comment by drkirkby created at 2010-09-26 23:33:58

Replying to [comment:44 leif]:
> Replying to [comment:43 drkirkby]:
> > http://wiki.sagemath.org/SupportedPlatforms
> > 
> > says Sage is supported on 32-bit PPC too. There are pages on 64-bit PPC and MIPS ports too, though I'm not aware of anyone working on them. So if there are targets, it would be worth considering adding them.
> 
> Yeah, there's even support for Linux on Playstation 2 and DEC Alpha. (And PPC, but only 32-bit I think.)

But the point is the Installation Guide does say Sage is supported on PPC. So IMHO, if there's a PPC target, we should try to call it. I'm not suggesting creating one if there is not already one there. 

> Does anyone port Sage to the PS2?

Not to my knowledge, though nothing would surprise me. Some code I wrote, which is part of NetBSD, has binaries for the Playstation. So nothing would totally surprise me. 

Dave


---

Comment by leif created at 2010-09-26 23:51:48

Replying to [comment:45 drkirkby]:
> Replying to [comment:44 leif]:
> > Yeah, there's even support for Linux on Playstation 2 and DEC Alpha. (And PPC, but only 32-bit I think.)
> 
> But the point is the Installation Guide does say Sage is supported on PPC. So IMHO, if there's a PPC target, we should try to call it.

Sure. There is one, so we can support it:

```sh
    ...
    # Linux
    case "`uname -m`" in
      i?86)
        $MAKE linux-thr;;
      ia64)
        $MAKE linux-ia64-thr;;
      amd64|x86_64)
        $MAKE linux-64-thr;;
      ppc)
        $MAKE linux-ppc;;
      *) # e.g. ppc64
        echo "Sorry, your platform isn't supported by Tachyon and/or Sage. Exiting..."
        exit 1
    esac
    ...
```


Although I doubt the Sage documentation is current, as always...


---

Comment by drkirkby created at 2010-09-28 23:51:54

Replying to [comment:46 leif]:
> Replying to [comment:45 drkirkby]:
> > Replying to [comment:44 leif]:
> > > Yeah, there's even support for Linux on Playstation 2 and DEC Alpha. (And PPC, but only 32-bit I think.)
> > 
> > But the point is the Installation Guide does say Sage is supported on PPC. So IMHO, if there's a PPC target, we should try to call it.
> 
> Sure. There is one, so we can support it:
> {{{
> #!sh
>     ...
>     # Linux
>     case "`uname -m`" in
>       i?86)
>         $MAKE linux-thr;;
>       ia64)
>         $MAKE linux-ia64-thr;;
>       amd64|x86_64)
>         $MAKE linux-64-thr;;
>       ppc)
>         $MAKE linux-ppc;;
>       *) # e.g. ppc64
>         echo "Sorry, your platform isn't supported by Tachyon and/or Sage. Exiting..."
>         exit 1
>     esac
>     ...
> }}}
> 
> Although I doubt the Sage documentation is current, as always...

I doubt you will find any two Sage lists of "supported platforms" which agree with each other.


---

Comment by vbraun created at 2011-01-11 10:10:20

I've slightly modified modified Dave's spkg from comment:28:

  * `Make-config.patch` is now a unified diff (-u)
  * For all GNU compiler targets, I removed overrides for `$CC`, `$AR`, and `$RANLIB` in the `Make-arch` file. These variables are already provided by the Sage environment, and it would be unwise to override them. They were in no case set to any useful value in the original `Make-arch`. In fact, it turned out to be harmful in #9379.
  * do not copy Copyright into `$SAGE_LOCAL/bin/Tachyon-Copyright` (??)
  * `SPKG.txt` has been updated.
  * Used leif's case statement from comment:46 for the `spkg-install`.
  * Use `$MAKE` instead of `make` everywhere.
  * don't strip on Itanium as that does not work on iras

Updated spkg is at

http://www.stp.dias.ie/~vbraun/Sage/spkg/tachyon-0.98.9.spkg

The following tickets are superseded by this ticket can be closed:
  * #9997: Tachyon does not even try to build on AIX
  * #9379: ia64-Linux binary fails "devel/sage/sage/plot/plot3d/tachyon.py"


---

Comment by vbraun created at 2011-01-11 10:10:20

Changing status from needs_work to needs_review.


---

Attachment

Diff of Make-arch for review purposes


---

Comment by vbraun created at 2011-01-11 10:11:12

Diff of Make-config for review purposes


---

Attachment

Great, I will review this today.


---

Comment by mhampton created at 2011-01-11 23:47:59

Looks good; I tested on OS X 10.5 and 10.6 and linux (64 bit).  Volker has tested this on the skynet machines as well.

I made one little change, adding Volker to the SPKG.txt.  Apart from that tiny addition I can give this a positive review.  My version is at:

[http://sage.math.washington.edu/home/mhampton/tachyon-0.98.9.spkg](http://sage.math.washington.edu/home/mhampton/tachyon-0.98.9.spkg)


---

Comment by mhampton created at 2011-01-11 23:47:59

Changing status from needs_review to positive_review.


---

Comment by wjp created at 2011-01-13 00:52:32

FYI, I've just created a `.p1` based on this package to #10609, fixing a bug in filetype detection in tachyon that broke the Sage tachyon interface on some machines.


---

Comment by jdemeyer created at 2011-01-19 22:19:10

Resolution: fixed


---

Comment by drkirkby created at 2011-02-06 06:22:46

Since the updated spkg calls the correct target on IBM's AIX operating system, #9997 can be closed as fixed. 

Dave
