# Issue 1452: GAP - id120.z file missing (?)

Issue created by migration from https://trac.sagemath.org/ticket/1452

Original creator: rlm

Original creation time: 2007-12-10 19:29:19

Assignee: mhansen

CC:  wdj

Running doctests on permgroup.py complains that file `id120.z` is missing. Indeed it is!


---

Comment by rlm created at 2007-12-11 17:13:40

Related to #950


---

Comment by rlm created at 2007-12-19 06:17:09

NOTE!

I forgot to mention, but this particular code has **HORRIBLE** memory leaks, and so in general it is a **very bad** idea to link this particular code in dynamically. Its executable files should be called directly, so that the leaks are gone as soon as it is finished. So I suppose this needs some more autoconf work...


---

Comment by mabshoff created at 2008-03-22 01:53:28

Resolution: duplicate


---

Comment by mabshoff created at 2008-03-22 01:53:28

This is a dupe of #2641 which also updates Guava to the 3.3 release.

Cheers,

Michael


---

Comment by rlm created at 2008-03-30 18:15:14

Resolution changed from duplicate to 


---

Comment by rlm created at 2008-03-30 18:15:14

Changing component from combinatorics to coding theory.


---

Comment by rlm created at 2008-03-30 18:15:14

Changing status from closed to reopened.


---

Comment by rlm created at 2008-03-30 18:15:14

Actually, #2641 doesn't seem to quite fix the problem. Although the compiler outputs the line:

```
gcc -O2 -o desauto \
	  desauto.o addsgen.o bitmanp.o cdesauto.o chbase.o cmatauto.o \
	  code.o compcrep.o compsg.o copy.o cparstab.o cstborb.o cstrbas.o \
	  errmesg.o essentia.o factor.o field.o inform.o matrix.o new.o \
	  oldcopy.o optsvec.o orbit.o orbrefn.o partn.o permgrp.o permut.o \
	  primes.o ptstbref.o randgrp.o randschr.o readdes.o readgrp.o \
	  readper.o rprique.o storage.o token.o util.o
```

The output must be getting clobbered somewhere. I'm looking for it now...


---

Comment by rlm created at 2008-03-30 18:42:00

If I run `./configure` in the `src` directory, and then `./configure` and `make` in the guava directory, then the appropriate files show up.

(A separate issue I notice is that other programs in Leon's code aren't compiled, such as `setstab`, and none of the `.sh` routines are moved anywhere.)


---

Comment by rlm created at 2008-03-30 18:43:43

Changing status from reopened to new.


---

Comment by rlm created at 2008-03-30 18:43:43

Changing assignee from mhansen to rlm.


---

Comment by rlm created at 2008-03-30 19:25:46

I think two things need to happen.

1. Either Guava should be updated to compile all of Leon, or Leon should be made its own spkg (in non-dynamic mode for now), since maybe some of Leon's functionality isn't specific to coding theory.

2. Either way, the `spkg-install` for gap-4.4.10 needs to be updated to copy the pieces of Leon that do get compiled to the corresponding place in `$SAGE_LOCAL/lib`.


---

Comment by wdj created at 2008-03-30 19:36:20

I'd be happy to make a new version of GUAVA which modifies the configure file so that "all of Leon" is compiled. 
I don't see why this is a defect though. Not trying to argue, just wondering what's the deal?
Also, I'm wondering if there is anything preventing Leon's (compiled) code from being used in SAGE as it is. At one point, there was an argument that the memory leaks barred this. With Brouwer's patch, perhaps this is fixed now?


---

Comment by mabshoff created at 2008-03-30 19:39:05

Why was this reopened? The Guava ticket covers this problem.

Cheers,

Michael


---

Comment by rlm created at 2008-03-30 20:00:29

Because there are substantial parts of Leon's programs missing from the install. Will post spkg later tonight.


---

Comment by rlm created at 2008-03-30 22:40:53

OK, here's the full deal:

1. `Makefile.in` in `gap-4.4.10.p3/src/pkg/guava3.3` lists only the programs `desauto` and `wtdist`, while the `Makefile` in `gap-4.4.10.p3/src/pkg/guava3.3/src/leon/src` contains instructions and dependencies for all the programs, including `setstab` (set stabilizer), `cent` (centralizer and conjugacy), etc.

2. There are a number of `.sh` files in `gap-4.4.10.p3/src/pkg/guava3.3/src/leon/src` which make calling the other programs for more questions easy.

3. The issue of memory leaks prevented Leon being used as a dynamically linked library. Compiling them as they are here is perfectly fine, since the process quits as soon as the computation is done. The only problem is overhead.

4. There are also certain no-no's which I figured out the better way to do when linking Leon in dynamically, but that never made it back to Guava proper. For example, in `Makefile.in`, mentioned above, there is the line `DEFINES = -DINT_SIZE=32`, when obviously the right way to do this is to get configure to tell you.

With David's permission, I'd like to fix all of these up for Guava 3.3.1, or 3.4 or something. In addition, I'd like to fix up the spkg-install to make all of Leon's programs a little more easily accessible from Sage.


---

Comment by rlm created at 2008-03-30 22:45:06

PS - I should mention that originally I wasn't finding desauto or wtdist at all, and they *are* actually put somewhere, but my "spotlight" did not find them. Now I am using Google desktop.......


---

Comment by wdj created at 2008-03-30 22:52:15

Yes, please go ahead and fix all these, but please use 3.4 as the next version
number instead of 3.3.1. Thanks! Let me know where the new tarball is so I can post it to the Guava webpage.


---

Comment by rlm created at 2008-03-31 02:19:33

Latest Guava tarball here:

http://sage.math.washington.edu/home/rlmill/guava3.4.tar

Latest GAP package here:

http://sage.math.washington.edu/home/rlmill/gap-4.4.10.p4.spkg

Within Guava, this ensures that all of Leon's programs are compiled, and makes sure that they are available in `bin/leon`, together with the shell scripts. I have also left the desauto and wtdist execs where they were for backwards compatibility.

The latest GAP package (I checked in David's p3 changes to the hg repo, as well as my own changes) makes sure that all the binaries from Guava are copied to `$SAGE_LOCAL/lib/gap-4.4.10/pkg/guava-3.4/bin`. The guava tarball is not necessary for Sage - its contents are contained in the GAP spkg.


---

Comment by mabshoff created at 2008-03-31 20:21:41

Somebody has been adding crap files to the spkg again:

```
.hg
._.hg
.hgignore
._.hgignore
patches
._patches
._spkg-install
spkg-install
._SPKG.txt
SPKG.txt
src
._src
```

I did skip the 1,200 others. But I will remove all those crap files.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-31 20:30:55

Resolution: fixed


---

Comment by mabshoff created at 2008-03-31 20:30:55

Merged the cleaned up gap.spkg in Sage 3.0.alpha0
