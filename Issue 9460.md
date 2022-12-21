# Issue 9460: Many Maxima-related doctest failures on sage.math

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-09 04:39:23

Assignee: mvngu

CC:  jhpalmieri rlm was leif

Building Sage 4.5.alphaX with `SAGE_FAT_BINARY="yes"` or `SAGE_PARALLEL_SPKG_BUILD="yes"` on sage.math can cause many Maxima-related test failures.

See [testlong.log](http://sage.math.washington.edu/home/wstein/build/sage-4.5.alpha4/testlong.log) and [comment:ticket:9274:17 this comment] at #9274 for examples.

So far, it seems that reinstalling the Maxima spkg "fixes" the failures.

See [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/1a6359a73d39dac2/4b4aaa26c0e22660#4b4aaa26c0e22660) for some background.


---

Comment by jhpalmieri created at 2010-07-09 04:51:04

I've been unable to replicate this.  I've built Sage 4.5.alpha4 with SAGE_FAT_BINARY and SAGE_PARALLEL_SPKG_BUILD both set to 'yes' and everything has come out fine.  I'll try again and see what happens...


---

Comment by mpatel created at 2010-07-09 04:57:00

Could the problem be building Sage from a script?  I get the failures if I build 4.5.alpha4 with

```sh
#!/bin/bash
X=20
export MAKE="make -j$X"
VER=4.5.alpha4
unset SAGE_CHECK SAGE_PARALLEL_SPKG_BUILD
#export SAGE_CHECK="check"
export SAGE_PARALLEL_SPKG_BUILD="yes"

TAG="-j$X"
[ ! -z "$SAGE_PARALLEL_SPKG_BUILD" ] && TAG="$TAG-par"
[ ! -z "$SAGE_CHECK" ] && TAG="$TAG-chk"

cd $HOME/scratch/tmp
OLDDIR="sage-$VER"
NEWDIR="$OLDDIR$TAG"
rm -rf $OLDDIR $NEWDIR
tar xvf /home/release/sage-$VER/sage-$VER.tar
mv $OLDDIR $NEWDIR
cd $NEWDIR

nice -n 19 time make build
```

but _not_ if I build with

```sh
$ nohup nice -n 19 env MAKE="make -j20" SAGE_PARALLEL_SPKG_BUILD="yes" make build &
```

The same happens even if I _do not_ build with `SAGE_PARALLEL_SPKG_BUILD="yes"`.  The four builds are [here](http://sage.math.washington.edu/home/mpatel/stmp/).


---

Comment by mpatel created at 2010-07-09 05:00:54

Addendum: I called the script in the previous comment `go` and ran it with `nohup go &`.


---

Comment by was created at 2010-07-09 06:00:45

Yes, all my builds of sage that failed were with a script.   I didn't even use nohup, but just screen.
The scri[pt I used is /home/wstein/buildbot. 

I suspect somebody screwed up the maxima spkg, obviously, and removed some workaround for building under a script.


---

Comment by rlm created at 2010-07-09 07:35:03

William,

Can you try the build with the ecl and maxima spkg's replaced with those in sage-4.4.4? I think #8645 might be causing this. If it is we can just reopen the ticket and roll back ecl and maxima.


---

Comment by was created at 2010-07-09 11:59:46

I'm running my whole test cycle here:

   http://sage.math.washington.edu/home/wstein/build/sage-4.5.alphastein1/

but with ecl and maxima rolled back.


---

Comment by jhpalmieri created at 2010-07-09 15:06:52

I've built successfully by running the same script as William: I copied "buildbot" to /scratch/palmieri/new and ran it to build Sage.  I tried it with SAGE64='yes' and that worked, too.  I just tried running screen and then running buildbot, and that worked, too.  I just can't reproduce this.


---

Comment by leif created at 2010-07-09 15:34:31

Replying to [comment:2 mpatel]:
> The four builds are [here](http://sage.math.washington.edu/home/mpatel/stmp/).

Did you compare the build trees?


---

Comment by was created at 2010-07-09 19:01:42

With the old maxima/ecl, everything worked.

The failures could be related to the memory issues we were having.  I've started a fresh build with my script as me here 

http://sage.math.washington.edu/home/wstein/build/sage-4.5.alpha4/

We'll see if it works.

 -- William, in Paris


---

Comment by mpatel created at 2010-07-09 22:43:02

Replying to [comment:9 leif]:
> Replying to [comment:2 mpatel]:
> > The four builds are [here](http://sage.math.washington.edu/home/mpatel/stmp/).
> 
> Did you compare the build trees?
> 
Yes.  As far as I can tell, the non-binary differences are simple path differences.  For example, the output of

```sh
diff -purN sage-4.5.alpha4-j20-env sage-4.5.alpha4-j20 2>&1 | grep -v "Binary files"
```

includes

```diff
--- sage-4.5.alpha4-j20-env/local/bin/maxima    2010-07-08 02:40:13.000000000 -0700
+++ sage-4.5.alpha4-j20/local/bin/maxima        2010-07-08 01:11:55.000000000 -0700
`@``@` -9,10 +9,10 `@``@` setup_vars() {
   if [ -z "$MAXIMA_VERSION" ]; then
     MAXIMA_VERSION=5.20.1
   fi
-  prefix=`unixize "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha4-j20-env/local"`
+  prefix=`unixize "/home/mpatel/scratch/tmp/sage-4.5.alpha4-j20/local"`
   exec_prefix=`unixize "${prefix}"`
   PACKAGE=maxima
-  top_srcdir=`unixize "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.alpha4-j20-env/spkg/build/maxima-5.20.1.p1/src"`
+  top_srcdir=`unixize "/home/mpatel/scratch/tmp/sage-4.5.alpha4-j20/spkg/build/maxima-5.20.1.p1/src"`
   libdir=`unixize "${exec_prefix}/lib"`
   if [ -n "$MAXIMA_LAYOUT_AUTOTOOLS" ]; then
       layout_autotools="$MAXIMA_LAYOUT_AUTOTOOLS"
```

Note: `/home/mpatel/scratch` is a symbolic link to `/scratch/mpatel`, which expands to `/mnt/usb1/scratch/mpatel/`.


---

Comment by mpatel created at 2010-07-09 23:20:08

I changed `cd $HOME/scratch/tmp` to `cd /mnt/usb1/scratch/mpatel/tmp` in `go` and rebuilt `sage-4.5.alpha4-j20-par` as `sage-4.5.alpha4-j20-par-mod`.  The long tests now _pass._  Hmm...


---

Comment by jhpalmieri created at 2010-07-10 00:06:42

David Kirkby has had some suspicions about the way the disk storing the home directories on sage.math is set up.  I wonder if that's causing the problem here.


---

Comment by was created at 2010-07-10 05:04:16

There is definitely a problem.  I tried rebuilding with the new maxima and ecl packages (in sage-4.5.alpha4) and had a huge number of failures.   Building the same sage-4.5.alpha4, but with the older maxima and ecl packages entirely fixes the problem.

> David Kirkby has had some suspicions about the way the disk storing the home directories on 
> sage.math is set up. I wonder if that's causing the problem here.

That could be.  If true, it definitely means that we have a serious bug in Sage -- not our filesystem.    Here's my build setup:

   * I make a symlink:   /home/wstein/build -> /scratch/wstein/build
   * I build in /home/wstein/build.

William


---

Comment by leif created at 2010-07-10 06:20:03

I can only tell I've successfully built Sage 4.5.alpha0, alpha1 and alpha4 with a similar link in my home directory to a different local filesystem, running `make` in the directory which is a symbolic link (Ubuntu 9.04).

I wonder if what Mitesh and William observed is really reproducible, or just a strange coincidence.


---

Comment by was created at 2010-07-10 07:05:46

Replying to [comment:15 leif]:
> I wonder if what Mitesh and William observed is really reproducible, or just a strange coincidence.

It's reproducible since:

  (1) I can systematically reproduce it, and 
  (2) Mitesh independently reproduced it.

That's pretty much the definition of reproducible.

I think we should revert the maxima and ecl spkg's, and release 4.5 without them, then sort this out in 4.5.1.


---

Comment by leif created at 2010-07-10 07:54:54

I mean I cannot see any reasonable cause in Mitesh's script vs. command line procedure; John has successfully built with your `buildbot` script. Reinstalling the packages or even just moving Sage seemed to solve the problems.

It's obviously an ECL/Maxima issue, but I think either related to uncatched or badly handled filesystem errors, or ECL again messing things up in concurrent builds.

So I'm not that sure that it's the package _version_, rather than the _build circumstances_.


---

Comment by leif created at 2010-07-10 08:05:35

Replying to [comment:16 was]:
> Replying to [comment:15 leif]:
> > I wonder if what Mitesh and William observed is really reproducible, or just a strange coincidence.
> 
> It's reproducible since:
> 
>   (1) I can systematically reproduce it, and 
>   (2) Mitesh independently reproduced it.
> 
> That's pretty much the definition of reproducible.

I should have written _deterministic_.


---

Comment by drkirkby created at 2010-07-10 08:26:19

Replying to [comment:14 was]:

> > David Kirkby has had some suspicions about the way the disk storing the home directories on 
> > sage.math is set up. I wonder if that's causing the problem here.
> 
> That could be.  If true, it definitely means that we have a serious bug in Sage -- not our filesystem.    Here's my build setup:
> 
>    * I make a symlink:   /home/wstein/build -> /scratch/wstein/build
>    * I build in /home/wstein/build.
> 
> William

In this case, since William's '/scratch', I would tend to agree the bug is in Sage, not the file system. That said, I am not 100% sure, since you are mounting a local file sysmem on an NFS one. If the NFS one can't be trust, can the file system that's mounted on the NFS one? I would however tend to think it would be OK, but I'm not 100% sure. 

I know for a fact there are issues on 't2' with the NFS file system exported by 'disk - it is clearly logged


```
Jul  6 12:06:06 t2 nfs: [ID 236337 kern.info] NOTICE: [NFS4][Server: disk][Mntpt: /home]NFS op OP_SETATTR got error NFS4ERR_DELAY causing recovery action NR_DELAY.
Jul  6 12:06:06 t2 nfs: [ID 236337 kern.info] NOTICE: [NFS4][Server: disk][Mntpt: /home]NFS op OP_CLOSE got error NFS4ERR_STALE causing recovery action NR_STALE.
Jul  6 12:06:06 t2 nfs: [ID 286389 kern.info] NOTICE: [NFS4][Server: disk][Mntpt: /home]File ./palmieri/t2/sage-4.5.alpha3/local/bin/python2.6 (rnode_pt: 3003cad4018) was closed due to NFS recovery error on server disk(failed to recover from NFS4ERR_STALE NFS4ERR_STALE)
Jul  6 12:06:06 t2 nfs: [ID 941083 kern.info] NOTICE: NFS4 FACT SHEET: 
Jul  6 12:06:06 t2  Action: NR_STALE 
Jul  6 12:06:06 t2  NFS4 error: NFS4ERR_STALE   
Jul  6 13:25:28 t2 nfs: [ID 236337 kern.info] NOTICE: [NFS4][Server: disk][Mntpt: /home]NFS op OP_CLOSE got error NFS4ERR_STALE causing recovery action NR_STALE.
Jul  6 13:25:28 t2 nfs: [ID 286389 kern.info] NOTICE: [NFS4][Server: disk][Mntpt: /home]File ./palmieri/t2/sage-4.5.alpha3/local/lib/gap-4.4.12/bin/gap.sh (rnode_pt: 6004da64c50) was closed due to NFS recovery error on server disk(failed to recover from NFS4ERR_STALE NFS4ERR_STALE)
Jul  6 13:25:28 t2 nfs: [ID 941083 kern.info] NOTICE: NFS4 FACT SHEET: 
Jul  6 13:25:28 t2  Action: NR_STALE 
Jul  6 13:25:28 t2  NFS4 error: NFS4ERR_STALE   
```


I would bet a pound to a penny this is a result of disabling the ZIL Log, which is bad practice - see [Disabling the ZIL (Don't)](http://www.solarisinternals.com/wiki/index.php/ZFS_Evil_Tuning_Guide#Disabling_the_ZIL_.28Don.27t.29)


---

Comment by drkirkby created at 2010-07-10 08:30:22

Replying to [comment:19 drkirkby]:
> I would bet a pound to a penny this is a result of disabling the ZIL Log, which is bad practice - see [Disabling the ZIL (Don't)](http://www.solarisinternals.com/wiki/index.php/ZFS_Evil_Tuning_Guide#Disabling_the_ZIL_.28Don.27t.29)
> 
Just to quote from [Disabling the ZIL (Don't) ](http://www.solarisinternals.com/wiki/index.php/ZFS_Evil_Tuning_Guide#Disabling_the_ZIL_.28Don.27t.29)

"Caution: Disabling the ZIL on an NFS server can lead to client side corruption. The ZFS pool integrity itself is not compromised by this tuning."


---

Comment by drkirkby created at 2010-07-10 09:15:06

I'm attaching a log of 

$ make ptestlong

on sage.math. I did forget, and actually built this in $HOME, not on a scratch disk. However, I did not use a script. 

Ultimately there are 4 failures. 


```
The following tests failed:

	sage -t  -long devel/sage/sage/interfaces/expect.py # 11 doctests failed
	sage -t  -long devel/sage/sage/interfaces/r.py # 184 doctests failed
	sage -t  -long devel/sage/sage/stats/r.py # 1 doctests failed
	sage -t  -long devel/sage/sage/tests/startup.py # 1 doctests failed
----------------------------------------------------------------------
```


All Maxima tests appear to have passed as far as I can see.

One possibility for the changed behavior might be the changes to 'deps'. This is now much better than it was before, with more accurate rules about the order things are built. This could mean that the build order has changed from previous versions of Sage and possibly libraries in Sage are now used when before the system libraries might be used - or visa versa. 

Another useful to track this might be to write a script that
 * Build Sage with the old maxima. Run just the maxima test to reduce the time. 
 * Build Sage with the old ECL. Run just the maxima test to reduce the time. 
 * Build Sage with the old maxima and old ECL. Run just the maxima test to reduce the time. 
 * Build Sage with the new Maxima and new ECL. Run just the maxima test to reduce the time. 

Repeat the above 10 times. Then look at the results, and see if failures are correlated or not. 
 
I see from his comment above William rolled back Maxima, and started a build. That has now finished. All his Maxima tests pass, but he gets this failure - which is new as far as I can see. I've just built Sage on sage.math without this failure. 

http://sage.math.washington.edu/home/wstein/build/sage-4.5.alphastein1/testlong.log

```
----------------------------------------------------------------------
The following tests failed:


	sage -t  -long "devel/sage/sage/schemes/elliptic_curves/lseries_ell.py"
Total time for all tests: 8270.6 seconds
```


Why should changing Maxima make `devel/sage/sage/schemes/elliptic_curves/lseries_ell.py` fail? I suspect the real cause of these problems might not be Maxima at all. There appears to be sporadic problems in this release of Sage (William for example failed to get R to build on OS X, but that works for me). 

This is a shame, as I know Robert has put a lot of effort into this release. I was actually expecting it to be one of the more stable Sage releases - which hopefully it will be, once the problem is resolved. 

Is it possible GPLK is responsible for this? That is a new standard package. I agree it seems unlikely, but I'm not convinced it is just a Maxima issue. Most likely is a build issue, which makes me think 'deps' might be the cause. 

Dave


---

Comment by drkirkby created at 2010-07-10 09:16:34

Tests on sage.math. Built in $HOME, not on /scratch. A script was not used.


---

Attachment

Replying to [comment:17 leif]:

> It's obviously an ECL/Maxima issue, but I think either related to uncatched or badly handled filesystem errors, or ECL again messing things up in concurrent builds.
> 
> So I'm not that sure that it's the package _version_, rather than the _build circumstances_.
> 

I too think this is the build problem. 
 * Why should William now get a failure of `devel/sage/sage/schemes/elliptic_curves/lseries_ell.py` when I assume that worked before? `devel/sage/sage/schemes/elliptic_curves/lseries_ell.py` passed on sage.math when I built it.  
 * Why should Maxima pass all tests for me, and all tests for John, yet fail for Metesh and William? 
 * Why should I get 4 failures when I build on sage.math, which don't share anything in common with the failures observed by William? 

I think one pass with the old Maxima and old ECL does not prove the problem is with ECL and/or Maxima. Since there issues which are not 100% reproducible, I fail to see how one good build by one person proves anything. (And even "good build" is not really true, as there is the elliptic curves test failed). 

IMHO, just changing ECL and Maxima and producing a 4.5 would be unwise until there is more proof there is not another more subtle error. 


I've just run 'dmesg' on sage.math and don't see anything like uncorrected RAM errors. In fact, I don't see any corrected RAM errors, so I doubt it is a memory fault. 

Dave


---

Comment by drkirkby created at 2010-07-10 09:38:53

Given Maxima has a library interface, should Maxima not be built before the Sage library, rather than the other way around? 


```
kirkby`@`sage:~/sage-4.5.alpha4$ ls -lrt spkg/installed | egrep "maxima|sage-4.5.alpha4"
-rw-r--r-- 1 kirkby kirkby 265 2010-07-09 08:41 sage-4.5.alpha4
-rw-r--r-- 1 kirkby kirkby 266 2010-07-09 08:51 maxima-5.20.1.p1
```


I'm going to create a 'deps' file which will ensure Maxima builds before Sage. Give that a try. 

Dave


---

Attachment

Deps file, which 1) Makes Maxima build before Sage 2) Makes SAGETEX depend on BASE. 3) Makes R dependancy on Fortran clearer, though not necessary


---

Comment by drkirkby created at 2010-07-10 09:45:37

Difference from the deps file in sage-4.5.alpha4.


---

Attachment

Replying to [comment:23 drkirkby]:
> Given Maxima has a library interface, should Maxima not be built before the Sage library, rather than the other way around?

In my _sequential_ build, the Sage library was built *before* Maxima, while the other way around in the _parallel_ build.

Both builds passed all doctests (`ptestlong`).


---

Comment by mpatel created at 2010-07-11 09:50:16

I haven't test this extensively, but I have the same problem with the Maxima spkg at #8731.


---

Comment by mpatel created at 2010-07-11 09:52:47

If we do revert ECL and Maxima, which changes from #8645 and #9264 should we backport?


---

Comment by was created at 2010-07-11 10:01:44

Replying to [comment:26 mpatel]:
> If we do revert ECL and Maxima, which changes from #8645 and #9264 should we backport?

I think revert ECL and Maxima is just a *very* temporary reversion so that we can release sage-4.5.   This reversion is just until we can fix whatever bug was introduced in these new packages, and hopefully we'll put them back in for sage-4.5.1.

We really need to get sage-4.5 out the door.


---

Comment by drkirkby created at 2010-07-11 11:39:17

Just reverting ECL will break the build on both Solaris 10 and OpenSolaris, since

 * ECL is leaving files in /tmp which means building on 't2' is unreliable - OK for one person, but stops the next person until root deletes files. Patch at http://trac.sagemath.org/sage_trac/attachment/ticket/8951/clear-ECL-from-tmp.patch
 * ECL includes assembly code on OpenSolaris which stops that building. Patch at http://trac.sagemath.org/sage_trac/attachment/ticket/8089/disable-assembly-code-on-OpenSolaris.patch

I've created #9474 for this. I should have a package ready in 15 minutes or so. 

As a matter of interest, does William have any idea why after reverting ECL and Maxima, his build still failed with `devel/sage/sage/schemes/elliptic_curves/lseries_ell.py`? 


Dave


---

Comment by was created at 2010-07-11 12:09:58

> As a matter of interest, does William have any idea why after reverting ECL and Maxima,
>  his build still failed with devel/sage/sage/schemes/elliptic_curves/lseries_ell.py?

That was caused by memory fragmentation on sage.math -- it has nothing to do with Sage itself.   So no worries at all.

```
sage -t  -long "devel/sage/sage/schemes/elliptic_curves/lseries_ell.py"
  ***   not enough memory
Aborted
  ***   not enough memory
Aborted**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.5.alphastein1/devel/sage/sage/schemes/elliptic_curves/lseries_ell.py", line 226:
    sage: E.lseries().zeros(2)
Expected:
    [0.000000000, 5.00317001]
Got:
    []
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.5.alphastein1/devel/sage/sage/schemes/elliptic_curves/lseries_ell.py", line 230:
    sage: point([(1,x) for x in a])             # graph  (long time)
Exception raised:
 }}}


---

Comment by leif created at 2010-07-11 13:22:21

Is it reproducible that the Maxima failures on sage.math vanish by doing `./sage -f maxima-5.20.1.p1` (i.e. forcing reinstallation)?

Then we could try just building Maxima as the *last* package, after all other packages have been built (or even temporarily force reinstallation as the last build step just to get 4.5 working).

P.S.: Dave has built a [ecl-10.2.1.p0.spkg](http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p0.spkg) (for downgrading ECL to 10.*2*.1) to fix the SunOS/Solaris issues he mentioned above (see #9474).


---

Comment by was created at 2010-07-11 13:49:03

> Then we could try just building Maxima as the last package, after all other packages have been 
> built (or even temporarily force reinstallation as the last build step just to get 4.5 working).

That's a really cool idea (!)


---

Comment by leif created at 2010-07-11 15:02:45

I still suspect ECL for the whole mess, creating lots of `/tmp/ECLINIT??????.?` files. I'm not sure if that happens in a really safe way on a multi-user system (with lots of concurrent builds).

On the other hand, then failing _builds_ would be more likely, rather than "successful" builds with failing doctests, but perhaps not all build failures are catched. And there have been doctest failures completely(?) unrelated to Maxima and ECL, like `pi in RR` evaluating to `False` IIRC.


---

Comment by leif created at 2010-07-11 15:24:10

Replying to [comment:32 leif]:
> ... completely(?) unrelated to Maxima and ECL, like `pi in RR` evaluating to `False` IIRC.

Oh, at least that example _starts_ a Maxima process... :/


---

Comment by leif created at 2010-07-11 15:41:25


```
$ grep warn_unused_result sage-4.5.alpha4/spkg/logs/ecl-10.4.1.log 
.../ecl-10.4.1/src/src/c/num_rand.d:73: warning: ignoring return value of 'fread', declared with attribute warn_unused_result
.../ecl-10.4.1/src/src/c/unixsys.d:421: warning: ignoring return value of 'pipe', declared with attribute warn_unused_result
.../ecl-10.4.1/src/src/c/unixsys.d:437: warning: ignoring return value of 'pipe', declared with attribute warn_unused_result
.../ecl-10.4.1/src/src/c/unixsys.d:470: warning: ignoring return value of 'dup', declared with attribute warn_unused_result
.../ecl-10.4.1/src/src/c/unixsys.d:473: warning: ignoring return value of 'dup', declared with attribute warn_unused_result
.../ecl-10.4.1/src/src/c/unixsys.d:476: warning: ignoring return value of 'dup', declared with attribute warn_unused_result
```



---

Comment by jhpalmieri created at 2010-07-11 16:16:20

Is it possible that those of you who have seen failures have some crap lying around in /tmp which is interfering with your build and/or doctesting?  I'm still trying to understand why some people have problems and others don't.


---

Comment by rlm created at 2010-07-11 19:16:57

Changing priority from blocker to major.


---

Comment by rlm created at 2010-07-11 19:16:57

I've reverted #8645 and #9264 in sage-4.5.rc0.


---

Comment by leif created at 2010-07-12 01:36:29

Just for the record:

I've "cloned" Sage 4.5.alpha4 (with SageNB 0.8.1 and zodb3 3.7.0.p4), then downgraded ECL to 10.2.1*.p0* (Dave's spkg) and Maxima to 5.20.1.p0 by forcing "reinstallation" (`./sage -f ...`).

With that version, all tests passed in `ptestlong`, `ptest` reported "0 doctests failed" in the French tutorial's `index.rst` (where I wouldn't have expected any doctests, btw). Testing just that file gave no errors.

I haven't had any doctest failures on that system with Sage 4.5.alpha4 though, so I can't tell if this is an improvement, but at least there is no regression for me.

(Ubuntu 9.04 x86, gcc 4.3.3, sequential build)


---

Comment by drkirkby created at 2010-07-12 10:43:13

Replying to [comment:35 jhpalmieri]:
> Is it possible that those of you who have seen failures have some crap lying around in /tmp which is interfering with your build and/or doctesting?  I'm still trying to understand why some people have problems and others don't.

If things in /tmp are a problem, then I feel that should be considered a bug. One should be able to write something to /tmp and some other package not read or write the same file. (That's currently happening on t2, which the ECL developer admits is an ECL bug. He assumed temporary file names created by 'mktemp' can't have a dot in their name, but that is not required by POSIX standards, and occasionally on Solaris tmp files have a dot in their name.) But I suspect mktemp on Linux does not use a dot, otherwise the issue would have been noticed before. 

I've seen failures with sage-4.5.alpha4 which are repeatable but go away as soon as I do an rm -r of $HOME/.sage. However, they were unrelated to the Maxima issues. 

This bug sure is weird. It might depend on what way the wind is blowing or the longitude. Has anyone in Europe seen this bug? 

If the system is low on memory, it could mean Sage mis-compiles. It would probably be worth logging the free memory 20 seconds or so, to see if it runs low. There are probably times of the day (i.e. longitude) where the system gets more use and so memory is lower. 

Dave


---

Comment by mpatel created at 2010-07-14 22:05:52

Some more information, which may or may not be useful:

 * In my tests at #9274, I tried making the Sage package depend on Maxima in `deps`, but the problems remained.

 * I have the same problem if I move `~/.bash*`, `~/.inputrc`, and `~/.profile` to another location, log out, log in, and build 4.5.alpha4 with the `go` script mentioned above.

 * I have the same problem (with 4.5.alpha4) on sage.math with William's [buildbot](http://sage.math.washington.edu/home/wstein/buildbot) setup.  I did

```sh
$ cd
$ cp ~wstein/buildbot .
$ mkdir /scratch/mpatel/build
$ ln -s /scratch/mpatel/build .
$ ./buildbot
```

   in a screen session.

 * Removing `/tmp` files owned by me and `~/.sage` also didn't help.


---

Comment by mpatel created at 2010-07-18 10:56:06

But building/testing 4.5.alpha4 in `/dev/shm` on sage.math works for me.  I did

```sh
$ cd
$ mkdir -p /dev/shm/mpatel
$ ln -s /dev/shm/mpatel SHM
$ cd SHM
$ emacs -nw go  # Replace 'cd $HOME/scratch/tmp' with 'cp $HOME/SHM' in "go" script above
$ nohup go &
```



---

Comment by nbruin created at 2010-07-30 06:07:36

Replying to [comment:23 drkirkby]:
> Given Maxima has a library interface, should Maxima not be built before the Sage library, rather than the other way around? 

This should not matter. the "library" maxima.fas is an ECL library that can be loaded into ECL completely dynamically. It is currently not used in sage anyway, but even if it were, maxima.fas does not have to be present at build-time - only at runtime.


---

Comment by drkirkby created at 2010-08-20 15:37:52

Does this still need to be open?


---

Comment by mpatel created at 2010-08-20 21:50:31

Replying to [comment:42 drkirkby]:
> Does this still need to be open? 

I still get the same types of failures with a 4.5.alpha4 I compiled today with the [comment:2 go script above] on sage.math.  Is the ZIL is still disabled on the Sage cluster?  I don't know if the plan is to enable it permanently, but it might help to do it temporarily, if it's practical, and revisit this ticket and #9501.

According to [comment:ticket:8731:40 this comment] at #8731, there's now a newer upstream release of Maxima.  I don't know if it will help here.


---

Comment by drkirkby created at 2010-08-20 23:30:32

Replying to [comment:43 mpatel]:
> Replying to [comment:42 drkirkby]:
> > Does this still need to be open? 
> 
> I still get the same types of failures with a 4.5.alpha4 I compiled today with the [comment:2 go script above] on sage.math.  Is the ZIL is still disabled on the Sage cluster?  I don't know if the plan is to enable it permanently, but it might help to do it temporarily, if it's practical, and revisit this ticket and #9501.

Here's the situation. 

[ZFS](http://en.wikipedia.org/wiki/ZFS) is the file system used on the main server disk.math. The ZFS Intent Log (ZIL) was disabled by William long ago (> 1 year). It speeds up NFS writes considerably, but it risks data corruption on the NFS clients (sage.math, t2.math, boxen.math etc). IMHO, this is a very bad idea. 

William has three choices
 * Leave the ZIL disabled and risk data corruption. 
 * Re-enable the ZIL, get valid data, but at a cost of a dramatic slow down in NFS speed. 
 * Buy a fast solid state disk. Then configure the storage pool so the ZIL is written to the fast solid state disk. The disk does not need to be large (even 100 MB would be sufficient), but it needs to be a good quality enterprise grade disks. Logging to a USB memory stick would not be a good idea. 

I've made William aware of this long ago. What he does is up to him. As far as I'm aware, the ZIL is disabled. Therefore, I would not trust any file in the home directories at all. I would only trust the disks locally mounted on the machines. If the problem goes away when things are built in 

Looking on sage.math, I see `/mnt/usb1/scratch` is locally mounted, so that should not suffer the problems the NFS mounted directories have. (I'm a bit suspicious that `/mnt/usb1 ` might actually be a USB mounted hard drive, which undoubtedly uses a consumer grade disk. The disks on a server like sage.math should not be on USB connectors, which is what that device name implies to me.)

`/scratch` on 't2.math' is a high quality local disk, so I trust that as much as you can trust any single hard drive. It is not backed up and its not mirrored. 

> According to [comment:ticket:8731:40 this comment] at #8731, there's now a newer upstream release of Maxima.  I don't know if it will help here.

I've no idea. 

We did try updating both ECL and Maxima recently, and it all went pear shaped. I don't think that has been resolved. I've rather lost track of what happened over that. 

Dave


---

Comment by kcrisman created at 2013-04-26 01:49:02

Changing status from new to needs_info.


---

Comment by kcrisman created at 2013-04-26 01:49:02

Is this still an issue?


---

Comment by jdemeyer created at 2014-11-21 10:13:32

I'm guessing this ticket is obsolete.


---

Comment by jdemeyer created at 2014-11-21 10:13:32

Changing status from needs_info to positive_review.


---

Comment by kcrisman created at 2014-11-21 13:25:58

Given that that machine is gone... sage.math is dead, long live sage.math!


---

Comment by vbraun created at 2014-11-28 18:38:43

Resolution: wontfix
