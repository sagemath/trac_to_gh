# Issue 9523: Arch linux build fails because our readline spkg is too old

Issue created by migration from https://trac.sagemath.org/ticket/9523

Original creator: cwitty

Original creation time: 2010-07-17 04:43:30

Assignee: tbd

CC:  timdumol

Under Arch linux, Sage fails to build, giving this error message:

```
bash: symbol lookup error: bash: undefined symbol: rl_filename_rewrite_hook
```

in the middle of the sqlite build (the next package built after readline).

This is a new symbol that was added in readline 6.1; so I'm pretty sure the problem is because our readline 6.0 is missing that symbol, so trying to run Arch's /bin/bash with our LD_LIBRARY_PATH will fail.

We should upgrade our readline spkg to 6.1; I bet that would fix the problem.


---

Comment by gostrc created at 2010-07-17 05:22:51

Hello, I'm the maintainer of sage-mathematics in the AUR. I think I have worked around this issue with 4.5-2 by not building sage's libreadline, and as a result, using the system's readline :)

BTW, this error is supposedly worked around by sage, by checking if uname -r | grep ARCH returns anything. Which means that people with custom kernels are likely to be experiencing this problem.


---

Comment by gostrc created at 2010-07-17 05:24:11

Oh ya, +1 from me to upgrade sage's libreadline to 6.1 so it can get rid of the internal workarounds and the workaround in my PKGBUILD :P


---

Comment by hivert created at 2010-07-19 14:45:28

Just to let you now ! The very same problem occurs with the new openSuSE 11.3...

Florent


---

Comment by mpatel created at 2010-09-15 21:36:52

Replying to [comment:3 hivert]:
> Just to let you now ! The very same problem occurs with the new openSuSE 11.3...

Indeed, there's [a recent thread about readline and openSUSE](http://groups.google.com/group/sage-support/browse_thread/thread/973316c62d190197) on sage-support.


---

Comment by mpatel created at 2010-09-18 09:38:05

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-09-18 09:38:05

Replying to [comment:4 mpatel]:
> Replying to [comment:3 hivert]:
> > Just to let you now ! The very same problem occurs with the new openSuSE 11.3...
> 
> Indeed, there's [a recent thread about readline and openSUSE](http://groups.google.com/group/sage-support/browse_thread/thread/973316c62d190197) on sage-support.

[Another](http://groups.google.com/group/sage-support/browse_thread/thread/8757b2515155ab42#).

We should try to fix this in 4.6 or 4.6.1.


---

Comment by leif created at 2010-09-18 15:40:32

Note that this wouldn't happen with proper shared library versioning... :|


---

Comment by mpatel created at 2010-09-19 06:36:41

Replying to [comment:7 mpatel]:
> Replying to [comment:4 mpatel]:
> > Replying to [comment:3 hivert]:
> > > Just to let you now ! The very same problem occurs with the new openSuSE 11.3...
> > 
> > Indeed, there's [a recent thread about readline and openSUSE](http://groups.google.com/group/sage-support/browse_thread/thread/973316c62d190197) on sage-support.
> 
> [Another](http://groups.google.com/group/sage-support/browse_thread/thread/8757b2515155ab42#).

And at [AskSage](http://ask.sagemath.org/question/135/trying-to-install-sage-to-suse-113).


---

Comment by drkirkby created at 2010-09-23 21:23:20

Somewhat related is #9987 

Readline can definitely be built on AIX -  see for example 

http://www.perzl.org/aix/index.php?n=Main.Readline

so something is wrong in how Sage is using readline. 

Dave


---

Comment by drkirkby created at 2010-10-24 10:21:45

I've updated the source code, and cleaned up the package a bit. If others want to clean it up further, feel free, but I don't want to spend a lot of time on this. It is not even causing any problems on any systems I'm using. The .spkg can be found here.

http://boxen.math.washington.edu/home/kirkby/patches/readline-6.1.spkg

I've checked the new .spkg actually builds on the following systems
 * AIX 5.3 (my own RS/6000 7025 F50 'aixbox') I did *not* try to resolve #9987
 * HP-UX 11.11B (my own HP C3600 'hpbox')
 * Linux (sage.math)
 * OpenSolaris 06/2009 (my own Sun Ultra 27 'hawk' which is a Sage buildbot slave.)
 * OS X (bsd.math)
 * Solaris 10 SPARC ('mark' on skynet, which is a Sun Blade 2500)
 
I've checked that the whole of Sage builds, and passes all doctests 


```
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 1740.4 seconds
drkirkby@hawk:~/sage-4.6.rc0$ 
```


with the updated .spkg on only the following system. 

 * OpenSolaris (my own Sun Ultra 27 'hawk' which is a Sage buildbot slave)

I've *not* checked this on any of the systems which have been known to cause issues with readline (FreeBSD, ArchLinux, OpenSUSE etc). 


Dave


---

Comment by drkirkby created at 2010-10-24 10:21:45

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-10-24 10:26:53

I just noticed I had not made all the necessary changes to a patch that was included in the .spkg. The patch would not apply cleanly to the update version of the source, so I had to do it manually, but it looks like I forgot a couple of bits. 

Leave it with me.


---

Comment by drkirkby created at 2010-10-24 10:26:53

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-10-24 10:59:53

Mercurial patch - adds a rather useless spkg-check file, cleans the package a little.


---

Attachment

This now needs review. 

Please test, especially on platforms where there has been problems with readline, which appear to be many!

I've now added an `spkg-check` file and run `make check` as there is a `check` target, but it does not actually do anything useful at this time. Hopefully the readline developers will add some self-tests. 

The package can be found at http://boxen.math.washington.edu/home/kirkby/patches/readline-6.1.spkg

Dave


---

Comment by drkirkby created at 2010-10-24 11:09:52

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-10-24 13:26:46

Hi David !

Replying to [comment:15 drkirkby]:
> This now needs review. 
> 
> Please test, especially on platforms where there has been problems with readline, which appear to be many!

Thanks for taking care of that. I'm trying to compile sage 4.6.rc0 with your
readline spkg on a 64 bits openSuSE 11.3. It seems to work ! My machine is now
compiling ATLAS and the "undefined symbol" vanished. However, as I posted on
[sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/bb636656e2153332?hl=en_US), it seems that there is another problem on this architecture. So I don't think I'll get a working sage.


---

Comment by leif created at 2010-10-24 16:25:32

A few comments:

 * The way `CFLAGS` (and `CXXFLAGS`) are set overrides user-specified settings (`-O2`, `-Wall`).
 * The handling of `SAGE_DEBUG` is inconsistent (and does not disable optimization):

```sh
# If SAGE_DEBUG is set either unset (the default), or set to  'yes'
# then add debugging information.
# Since both the Sun and GNU compilers accept -g to give debugging information,
# there is no need to do anything specific to one compiler or the other.

if [ "x$SAGE_DEBUG" = "x" ] || [ "x$SAGE_DEBUG" = "xyes" ] ; then
   echo "Code will be built with debugging information present. Set 'SAGE_DEBUG' to 'no' if you don't want that."
   # Actually anything other than 'yes' or '1' will cause
   # no debugging information to be added.
   CFLAGS="$CFLAGS -g "
   CXXFLAGS="$CXXFLAGS -g "
else
   echo "No debugging information will be used during the build of this package."
   echo "Unset SAGE_DEBUG if you want debugging information present (-g added)."
fi
```

   I would add debugging symbols by default anyway.
 * `make` is used instead of `$MAKE`. I don't know why we do the build and install in one call.
 * The following is most probably wrong for readline 6.1:

```sh
elif [ "$UNAME" = "OpenBSD" ]; then
  DYLIB_NAME="$SAGE_LOCAL"/lib/libreadline.so.6.0
```

 * The following should simply be `if grep -q ... ; then ...`:

```sh
    if [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` -eq 0 ]; then
```

   (or at least `if grep ... >/dev/null; then ...`). The preceding `test -f` is also superfluous, but I agree makes it perhaps more readable.
 * The use of `set +/-e` is quite confusing and error-prone, and its use is *definitely wrong here*, since we don't get the exit status of "copying patches" and, worse, `build()`:

```sh
...
set -e
...
cp patches/shobj-conf src/support/
if [ $? -ne 0 ]; then
    echo "Error copying patch over."
    exit 1
fi

cd src/

build()
{
    ./configure --prefix="$SAGE_LOCAL" $CONF_FLAGS
    make install
}

build
set +e
if [ $? -ne 0 ]; then
    echo "Error building and installing readline."
    exit 1
fi
set -e
...
```

 * It is safer to quote (all instances of) `$UNAME`.
 * The `build()` functions is almost useless, and in fact does `make install` (see above).

I originally wanted to set this to "needs info" (w.r.t. OpenBSD), but now I think at least _some of_ the above really needs to be fixed, therefore "needs work".


---

Comment by leif created at 2010-10-24 16:25:32

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-10-24 16:28:45

P.S.: Do we at all still need to use the system's readline on OpenSuSE 11.1?


---

Comment by drkirkby created at 2010-10-24 17:38:13

Leif, 

I'd agree the OpenBSD code is probably wrong, though with nobody at all working on an OpenBSD port to my knowledge, I don't know how we are going to find out. But I'm willing to change that. To my knowledge, only FreeBSD is being worked on by Peter, with nobody working on NetBSD, OpenBSD or any other *BSD. 

With the possible exception of that, I don't believe my changes have introduced any new problems. I simply don't have time to go though another ticket like #9603, where there were endless changes to `spkg-install` which took 6 weeks. 

Many of those proposed will need extensive testing, which I don't have time for. As I remarked above:

_If others want to clean it up further, feel free, but I don't want to spend a lot of time on this. It is not even causing any problems on any systems I'm using._ 

I'd rather concentrate my time on sorting out #9040 and #9840. I suggest you create another ticket to clean this up if you feel it needs it. Sorry, but I just don't want another ticket like #9603! 

I've got no idea of the situation with OpenSUSE

Dave


---

Comment by leif created at 2010-10-24 18:16:14

Replying to [comment:19 drkirkby]:
> I don't believe my changes have introduced any new problems.

I didn't say you introduced them, doesn't make a difference to me though.

> I simply don't have time to go though another ticket like #9603, where there were endless changes to `spkg-install` which took 6 weeks.

That had a couple of reasons. All my suggestions are above, and as I said _some_ of them are minor, but at the same time most of them trivial to fix without risk.

(Cf. the Cython upgrade, where I just "cleaned up" the `spkg-install` by moving `cd src`, and Robert at the same time - with the original spkg - ran into exactly the potential error to make by copying the patches at the wrong point of the script, which one would not even have noticed when installing the spkg.)
 
> Many of those proposed will need extensive testing, 

I don't agree; also, the handling of `SAGE_DEBUG` e.g. and the use of `set -e` is simply wrong *as it is now*.

> _If others want to clean it up further, feel free, but I don't want to spend a lot of time on this. It is not even causing any problems on any systems I'm using._ 
> 

Nathann, is it you? ;-)

> I'd rather concentrate my time on sorting out #9040 and #9840. I suggest you create another ticket to clean this up if you feel it needs it.

It doesn't make sense to me to keep definite flaws in it, and postpone fixing them to yet another ticket. And I don't have time for such either, not to mention every new ticket needs new review and testing again.

It's currently a blocker, but meanwhile one for 4.6*.1*.

> I've got no idea of the situation with OpenSUSE

Me either, but the reason for upgrading readline was OpenSuSE!


---

Comment by hivert created at 2010-10-24 18:28:55

> I've got no idea of the situation with OpenSUSE

I'm using openSuSE 11.3 (the latest) on a 64 bits machine and I've the following behavior:

 - The openSuSE binary for 4.5.2, 4.5.3 *doesn't start* unless the following files are removed from sage install:

```
libreadline.a  libreadline.so  libreadline.so.6  libreadline.so.6.0
```

It seems to works perfectly of those are removed (I got all tests passed with 4.5.2). 

 - The 4.5.2 and 4.5.3 source doesn't compile either. I got it compile and work with the patch on #9530 (all test passed on 4.5.3)

 - The 4.6rc0 seem to compile correctly using David's spkg, however for a probably different reason it doesn't start, failing with the error

```
ImportError: No module named sagenb.misc.sphinxify
```


I've no idea how to fix this last error and as I said previously I asked for
help on sage-release.


Also, if needed I have access on a older openSuSE 11.1 system but I haven't
upgraded sage on it recently.

Cheers,

Florent


---

Comment by drkirkby created at 2010-10-24 19:46:29

Leif, 

I'll make *some* of the changes you suggest. I will change `make` to `$MAKE`, but that will need *extensive* testing, as parallel builds tends to break on many packages. I'll test it 100 times on my reasonably quick (quad core 3.33 GHz) Sun Ultra 27, but I don't have time to test it extensively on every system.


---

Comment by leif created at 2010-10-24 20:10:11

Replying to [comment:21 hivert]:
>  - The 4.6rc0 seem to compile correctly using David's spkg, however for a probably different reason it doesn't start, failing with the error

```
ImportError: No module named sagenb.misc.sphinxify
```

> 
> I've no idea how to fix this last error and as I said previously I asked for
> help on sage-release.
> 
> 
> Also, if needed I have access on a older openSuSE 11.1 system but I haven't
> upgraded sage on it recently.

It would be helpful if you could try to build Sage 4.6.rc0 on that, too (upgrading from a - perhaps copied - working Sage version should also work), to see if the same error occurs as on OpenSuSE 11.3.


---

Comment by drkirkby created at 2010-10-24 20:25:49

Mercurial patch to clean up the package a bit more


---

Attachment

I've attached to clean this up a bit more. If a reviewer wants further changes, please make a reviewer patch, as I have more pressing things to do. I've done most of the changes suggested. 

I've set this to build in parallel. It does not make a huge difference to the install time, changing from 14 seconds to 6 seconds on my machine. Shaving off 8 seconds is not a huge gain, 

http://boxen.math.washington.edu/home/kirkby/patches/readline-6.1.spkg

I've tested the parallel builds 100 times on OpenSolaris, but not on any other platform. 

Dave


---

Comment by drkirkby created at 2010-10-24 20:30:08

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-10-24 20:32:26

Replying to [comment:22 drkirkby]:
> I'll make *some* of the changes you suggest. I will change `make` to `$MAKE`, but that will need *extensive* testing, as parallel builds tends to break on many packages. I'll test it 100 times on my reasonably quick (quad core 3.33 GHz) Sun Ultra 27, but I don't have time to test it extensively on every system.

Well, I would consider changing `make` to `$MAKE` less important for the moment, as - as you say - _that_ requires more testing, in contrast to the other changes.

Note that e.g.

```sh
$ env MAKE="make -j" ./sage -i readline-6.1.spkg
```

(or copying the spkg to `spkg/standard/` and running `env MAKE="make -j" make`) would currently attempt a parallel build / install anyway, even though you call `make` in `spkg-install`.

----

It's quite funny to enable `-Wall` in a script and at the same time keep blocks of unreachable code in the script itself.

----

Btw, `ptestlong` passed with 4.6.rc0 on Ubuntu 10.04 x86_64 both with just that spkg as well as all dependent packages [re]built.


---

Comment by drkirkby created at 2010-10-24 20:43:22

As I said, I don't wish to spend too long on this. I thought it would be a relatively quick fix to just update the source code, but are very keen to let the ticket drag on. 

I was not aware there were blocks of unreachable code, but feel free to remove them with a reviewer patch.


---

Comment by drkirkby created at 2010-10-24 20:46:25

Sage now has a buildbot set up. See

http://build.sagemath.org/sage/waterfall

The machine on the far right 'hawk' is my own machine, and seems to manage being a buildbot slave despite this is only on a home ADSL network, and not a professionally managed data centre. If someone has an !OpenSUSE machine they can keep on 24/7, and permit access via the buildbot, then perhaps Mitesh will add it as a slave. That would drastically reduce the chances of a Sage build breaking on !OpenSUSE, as a failure would be detected very quickly. 

Dave


---

Comment by leif created at 2010-10-24 20:49:57

The newly attached patch looks good (you changed even things I did not mention :) ), except for you now add `$OPTIMZATION_FLAGS` twice (if `SAGE_DEBUG!="yes"`), the second time again overriding user settings, and also `-Wall` is *ap*pended to `CFLAGS` s.t. it can't be disabled by the user.

As far as I can see, `$CONF_FLAGS` passed to `./configure` aren't set anywhere, so we could drop that. (Otherwise a value from the global environment might unintentionally be used.)


---

Comment by leif created at 2010-10-24 20:52:56

Replying to [comment:26 drkirkby]:
> I was not aware there were blocks of unreachable code, but feel free to remove them with a reviewer patch. 

Removing `set -e` solved that.


---

Comment by leif created at 2010-10-24 22:52:42

Replying to [comment:25 leif]:
> Btw, `ptestlong` passed with 4.6.rc0 on Ubuntu 10.04 x86_64 both with just that spkg as well as all dependent packages [re]built.

I've successfully reinstalled / rebuilt the updated spkg and all dependent packages* (with 32 jobs); `ptestlong` again passed.


----

* To achieve this, one can (since rc0) `export SAGE_UPGRADING=yes` and run `make` after copying the new spkg to `spkg/standard/` and deleting `spkg/installed/readline-6.1`.


---

Comment by drkirkby created at 2010-10-25 07:42:34

Are there any more changes needed for this to get a positive review, or is it only further testing? 

Longer term there are a few things I'd like to sort out in this package. Currently it assumes if the compiler is not the Sun compiler, then it is gcc, but that overlooks the possibility of other compilers such as those from IBM and HP. There is now a small script that can determine what C compiler is in use `$SAGE_LOCAL/bin/testcc.sh`. Longer term I'd like to sort that out, but that's not important in the short or medium term. 

I tested my previous version actually built on AIX, HP-UX, Linux, OpenSolaris, OS X and Solaris. I found all tests passed on OpenSolaris. Leif has found all tests pass for this version on Linux. 

I just this minute started a build and test on OpenSolaris, but I wont know the result for a couple of hours, as it takes an hour to build and test and I will not be in the house at that point - I leave in 35 minute or so. 

Given we now have the buildbot, I would have thought this a fairly low-risk patch to put in sage-4.6.rc1, as any problems should be easily spotted. 

Dave


---

Comment by drkirkby created at 2010-10-25 12:34:40

I build Sage from scratch with the updated .spkg on a Sun Ultra 27 running OpenSolaris. This was a parallel build, and parallel doctests. Two doctests failed

```
The following tests failed:

        sage -t  -long -force_lib devel/sage/sage/interfaces/psage.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/algebras/quatalg/quaternion_algebra_element.pyx # 0 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1675.4 seconds
```


But when I run those two tests individually they both passed. I can only assume this is the usual problem - the doctesting framework is partially broken for parallel testing. 


```
drkirkby@hawk:~/sage-4.6.rc0$ ./sage -t  -long -force_lib devel/sage/sage/interfaces/psage.py
sage -t -long -force_lib "devel/sage/sage/interfaces/psage.py"
         [24.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 25.4 seconds
drkirkby@hawk:~/sage-4.6.rc0$ ./sage -t  -long -force_lib devel/sage/sage/algebras/quatalg/quaternion_algebra_element.pyx
sage -t -long -force_lib "devel/sage/sage/algebras/quatalg/quaternion_algebra_element.pyx"
         [13.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 13.0 seconds
drkirkby@hawk:~/sage-4.6.rc0$ 
```


As such, Sage has been build from scratch using this package, and has passed all tests on both Linux and OpenSolaris. 

Dave


---

Comment by drkirkby created at 2010-10-27 10:23:54

Replying to [comment:17 leif]:
> A few comments:

>  * The following should simply be `if grep -q ... ; then ...`:

Using `grep -q` would cause a problem on Solaris, since the default `grep` in most peoples path is not POSIX compatible. 

This is still awaiting review though. 

Dave


---

Comment by jdemeyer created at 2010-11-05 10:48:53

Complete spkg patch for reference


---

Attachment

"presidence" sould be "precedence"

Why is `patches/shobj-conf` under revision control?  I believe it is sufficient for the patch file to be under revision control (but putting the _patched_ files also under revision control might be the usual Sage practice).

I don't like `"$CC" -flags > /dev/null 2>&1` (`spkg-install` line 43) for various reasons:
 * I don't think $CC is supposed to be quoted because people might do things like CC="gcc -m64"
 * You should redirect stdin from `/dev/null` in case $CC wants to read from stdin.
 * Instead of checking for Sun's compiler, why not check explicitly for `gcc` using

```
$CC </dev/null >/dev/null 2>/dev/null --version |grep >/dev/null gcc
```



---

Comment by drkirkby created at 2010-11-05 12:38:25

Replying to [comment:35 jdemeyer]:
> "presidence" sould be "precedence"
> 
> Why is `patches/shobj-conf` under revision control?  I believe it is sufficient for the patch file to be under revision control (but putting the _patched_ files also under revision control might be the usual Sage practice).

It is practice to put both. The argument I've heard for doing this is that if the only the patch file is under revision control, if a package gets updated, then the patch is against a version of the source not in the package. So you need to download the old version. 

I'm not totally convinced of the logic myself, but it is standard practice. (I'd personally rather just see a patch file, and use 'patch' rather than 'cp', but that is not permitted). 

> I don't like `"$CC" -flags > /dev/null 2>&1` (`spkg-install` line 43) for various reasons:
>  * I don't think $CC is supposed to be quoted because people might do things like CC="gcc -m64"

That would not change the results of the test. I can assure you that works with and without -m64. 

>  * You should redirect stdin from `/dev/null` in case $CC wants to read from stdin.

I'm unaware of any problems with the current code. 

>  * Instead of checking for Sun's compiler, why not check explicitly for `gcc` using
> {{{
> $CC </dev/null >/dev/null 2>/dev/null --version |grep >/dev/null gcc
> }}}

I forget why, but there was some reason that I did not use the obvious 'gcc --version'. Several compilers act like gcc, but are not actually gcc. I believe the Intel compiler takes the gcc options, so for practical purposes is gcc, but wont output gcc. In any case, I think one can change that string when gcc is built to whatever you want. 

However, if someone wants to change the test, then the most sensible thing to do is use the script $SAGE_LOCAL/bin/testcc.sh, as that will return one of 

 * GCC
 * Sun_Studio
 * HP_on_Tru64
 * IBM_on_AIX
 * HP_on_Alpha_Linux
 * Unknown

That tests what gets defined when (!__SUNPRO_C in the case of the Sun compiler, !__GNUC!__ in the case of gcc etc). 

There are bugs that I'm aware of, that are causing serious problems - #9040 and #9840 are two I would love to solve. I'm reluctant to make a change, which itself has a finite risk of introducing a bug, to "solve" a problem that has never been observed. That bit of code has remained unchanged for a long time, and has never caused any problem on any platform. 

Dave


---

Comment by jdemeyer created at 2010-11-05 12:56:13

Replying to [comment:36 drkirkby]:
> >  * I don't think $CC is supposed to be quoted because people might do things like CC="gcc -m64"
> 
> That would not change the results of the test. I can assure you that works with and without -m64. 

Really?  With `GNU bash, version 4.0.35(1)-release (x86_64-pc-linux-gnu)`, I get

```
$ CC="gcc -m64"
$ "$CC" --version
bash: gcc -m64: command not found
```


> >  * You should redirect stdin from `/dev/null` in case $CC wants to read from stdin.
> 
> I'm unaware of any problems with the current code.
Me neither, but I think redirecting stdin from `/dev/null` does no harm and is safer.


---

Comment by jdemeyer created at 2010-11-05 13:10:01

For the record: GNU autoconf uses `$CC` without quoting and redirects stdin from `/dev/null` (for the whole `configure` script using `exec`).


---

Comment by jdemeyer created at 2010-11-05 13:11:59

By the way: I think the quoting of `$CC` really is a bug, I care less about the other issues.


---

Comment by jdemeyer created at 2010-11-05 13:11:59

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-11-05 13:51:06

Replying to [comment:36 drkirkby]:
> Replying to [comment:35 jdemeyer]:
> > Why is `patches/shobj-conf` under revision control?  I believe it is sufficient for the patch file to be under revision control (but putting the _patched_ files also under revision control might be the usual Sage practice).
> 
> It is practice to put both. The argument I've heard for doing this is that if the only the patch file is under revision control, if a package gets updated, then the patch is against a version of the source not in the package. So you need to download the old version.

Well, that's of course b*llsh*t, since the old source code is in the old spkg you're going to upgrade. But it is long and current practice, as Dave says.

A more convincing reason is that it is safer to put both under revision control, since some people might update just the patch and not the patched file which is copied over. This is easy to see with `hg log`, though one would also notice that by just looking at the file modification times.

> I'm not totally convinced of the logic myself, but it is standard practice. (I'd personally rather just see a patch file, and use 'patch' rather than 'cp', but that is not permitted).

In the light of 1 MB `configure.in` etc. in `patches/` and the Mercurial repository, I'd also rather have just the patches (diffs) there, i.e. omitting pre-patched files at all.

This would either require (explicitly) making `patch` a prerequisite (which is IMHO not a problem), or - perhaps in addition - providing `ed` patches, with isn't very nice (and complicates reviewing).

> > I don't like `"$CC" -flags > /dev/null 2>&1` (`spkg-install` line 43) for various reasons:
> >  * I don't think $CC is supposed to be quoted because people might do things like CC="gcc -m64"
> 
> That would not change the results of the test. I can assure you that works with and without -m64.

As Jeroen noted, this _does_ make a difference. I do not even get an error message:

```sh
$ "gcc -m64" --version ; echo $?     # equivalent to gcc\ -m64 --version
127
$ gcc -m64 --version ; echo $?
gcc (Ubuntu 4.4.3-4ubuntu5) 4.4.3
Copyright (C) 2009 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

0
```


I wanted to make a reviewer patch anyway, since we need to also patch the `pkg-config` file created by freetype to avoid potential trouble with Sage relocation. (Btw, the term "migration" would be less ambiguous, though it is used in other contexts as well, but certainly not within Sage.)


---

Comment by drkirkby created at 2010-11-05 16:03:32

None of this is causing a problem with the package:


```
export CC="gcc -m64"

<snip>

readline-6.1/src/rlwinsize.h
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -m64 -v
Using built-in specs.
COLLECT_GCC=/usr/local/gcc-4.5.0/bin/gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/libexec/gcc/i386-pc-solaris2.10/4.5.0/lto-wrapper
Target: i386-pc-solaris2.10
Configured with: ../gcc-4.5.0/configure --prefix=/usr/local/gcc-4.5.0 --build=i386-pc-solaris2.10 --enable-languages=c,c++,fortran --with-gmp=/usr/local/gcc-4.5.0 --with-mpfr=/usr/local/gcc-4.5.0 --disable-nls --enable-checking=release --enable-werror=no --enable-multilib -with-system-zlib --enable-bootstrap --with-gnu-as --with-as=/usr/local/binutils-2.20/bin/as --without-gnu-ld --with-ld=/usr/ccs/bin/ld
Thread model: posix
gcc version 4.5.0 (GCC) 
****************************************************
Building a 64-bit version of Readline
Using CC=gcc -m64
The following environment variables will be exported.
Using CFLAGS=-O2  -m64 -g -O2 -Wall
Using CPPFLAGS=
Using LDFLAGS= -m64
```


but I'm happy to change it. 

I long ago created a package for 'patch'

http://boxen.math.washington.edu/home/kirkby/patches/patch-2.6.1.spkg

I think William finally agreed to make it part of sage, since many wanted it. But then after that others had convinced him there were better ways do it with Mercurial, so I gave up the idea. 

Leif, what has the pkg-config file for freetype got to do with this readline package? 

Do you want to create a reviewer patch, or shall I unquote CC? 

Dave


---

Comment by leif created at 2010-11-05 16:31:29

Replying to [comment:41 drkirkby]:
> None of this is causing a problem with the package:
> but I'm happy to change it.

Of course it incidentally "works" _there_, because we are not looking for `gcc`. If you define `CC="suncc -whatever"` it won't work, i.e. not recognize Sun's `cc`.


> I long ago created a package for 'patch'
> 
> http://boxen.math.washington.edu/home/kirkby/patches/patch-2.6.1.spkg
> 
> I think William finally agreed to make it part of sage, since many wanted it. But then after that others had convinced him there were better ways do it with Mercurial, so I gave up the idea.

I think we don't have to provide a (standard) package to make `patch` a prerequisite.

Note that Mercurial depends on Python, so unless we make one of these a prerequisite, using Mercurial instead (which I wouldn't like) isn't an option.


> Leif, what has the pkg-config file for freetype got to do with this readline package?

Good question... ;-) Apparently wrong ticket... (Confused that because updating the readline spkg _triggered_ the `pkg-config` problems with freetype.)

> Do you want to create a reviewer patch, or shall I unquote CC?

I can do that, as I've suggested some other minor changes [comment:28 above].


---

Comment by leif created at 2010-11-05 17:01:15

Grrr, I just noticed we still have to include the changes from #9530 as well, so either we provide two additional patches, or it will take a bit longer.

I think I'll first upload a reviewer patch without the changes from there.


---

Attachment

SPKG reviewer patch. Removes quotes from `$CC`etc. Apply on top of Dave's "further clean-up" patch.


---

Comment by leif created at 2010-11-05 17:18:12

Replying to [comment:43 leif]:
> I think I'll first upload a reviewer patch without the changes from there.

Did so.


---

Comment by drkirkby created at 2010-11-11 19:45:47

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-11-11 19:45:47

I had difficulty merging the changes made on this ticket to the changes made in readline-6.0.p4.spkg (see #9530). There were a lot of rejects and I was less confident of sorting them out, then doing the changes manually. 

As such, I've taken the readline-6.0.p4.spkg, and manually made the changes originally made here. It's not totally impossible I've missed one, but I think they are ok. 

So I'm attaching a new patch, `9523-brand-new-patch-based-on-readline-6.0.p4.patch` which should have all the changes need to sort out the update, and clean the package somewhat. 

The updated package can be found at 

http://boxen.math.washington.edu/home/kirkby/readline-6.1.spkg 

(if you want to look at my previous attempt, see http://boxen.math.washington.edu/home/kirkby/patches/readline-6.1.spkg)

Dave


---

Attachment

Mercurial patch with all (well hopefully all) the changes needed to update to 6.1 and clean up.


---

Comment by jdemeyer created at 2010-11-19 07:56:18

Changing priority from blocker to major.


---

Comment by jdemeyer created at 2010-12-05 09:53:41

Changing priority from major to blocker.


---

Comment by Koen created at 2010-12-13 12:09:31

FYI, for OpenSUSE 11.0 and 11.1, Sage should not try to use the system readline, because it will be a .5 version. It will only build if the special OpenSUSE handling is _not_ there. See also http://groups.google.com/group/sage-devel/browse_thread/thread/71d3a99910e11b01


---

Comment by leif created at 2010-12-13 14:33:15

Replying to [comment:49 Koen]:
> FYI, for OpenSUSE 11.0 and 11.1, Sage should not try to use the system readline, because it will be a .5 version. It will only build if the special OpenSUSE handling is _not_ there. See also http://groups.google.com/group/sage-devel/browse_thread/thread/71d3a99910e11b01

Thanks. Then I'd say *needs work*...

Maybe we should compare the versions and always use the newer one?
But this causes trouble in case the interface changes, but not its "official" version (which should IMHO never happen though).


---

Comment by jdemeyer created at 2010-12-13 14:41:32

Why do we need to special-case OpenSUSE in the first place?  I thought the whole point of this ticket was *not* to have any special cases any more.


---

Comment by leif created at 2010-12-13 15:00:27

`CFLAGS` still (or again) get overwritten even if `SAGE_DEBUG` is not "yes".


---

Comment by leif created at 2010-12-13 15:07:25

Replying to [comment:51 jdemeyer]:
> Why do we need to special-case OpenSUSE in the first place?  I thought the whole point of this ticket was *not* to have any special cases any more.

:D If you convince the openSUSE and ArchLinux developers to never make `bash` depend on a newer libreadline than Sage ships...

Otherwise the problem remains or rearises with future releases of these OSs.


---

Comment by leif created at 2010-12-13 15:31:07

We could just always build Sage's readline and - *before* installing it - test if it works with `/bin/bash` by e.g.

```sh
if env LD_LIBRARY_PATH="." bash -c "echo 'Bash works with this version of readline.'"; then
    $MAKE install
    ...
else
    echo "Bash doesn't work with Sage's version of readline - using the system's one."
    # Can this cause trouble with *older* system libreadlines?
    # We still need a *development* version of readline btw.
    exit 0
fi
```



---

Comment by jdemeyer created at 2010-12-13 15:53:27

Replying to [comment:53 leif]:
> Replying to [comment:51 jdemeyer]:
> > Why do we need to special-case OpenSUSE in the first place?  I thought the whole point of this ticket was *not* to have any special cases any more.
> 
> :D If you convince the openSUSE and ArchLinux developers to never make `bash` depend on a newer libreadline than Sage ships...
> 
> Otherwise the problem remains or rearises with future releases of these OSs.
True, but this problem is not specific to these OSs and applies to every OS.


---

Comment by jdemeyer created at 2010-12-13 15:53:27

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-12-13 16:41:43

Replying to [comment:55 jdemeyer]:
> Replying to [comment:53 leif]:
> > Replying to [comment:51 jdemeyer]:
> > > Why do we need to special-case OpenSUSE in the first place?  I thought the whole point of this ticket was *not* to have any special cases any more.
> > 
> > :D If you convince the openSUSE and ArchLinux developers to never make `bash` depend on a newer libreadline than Sage ships...
> > 
> > Otherwise the problem remains or rearises with future releases of these OSs.
> True, but this problem is not specific to these OSs and applies to every OS.

Not really. Others work fine, so I consider testing if `bash` works with our readline also an (implicit) special case.

Would you be happy with that?

(I think at least it doesn't hurt doing so, i.e. testing `bash` against Sage's readline before installing it. Better to give a concise error message than risking other weird build errors.)


---

Comment by drkirkby created at 2010-12-13 18:41:29

Replying to [comment:55 jdemeyer]:
> Replying to [comment:53 leif]:
> > :D If you convince the openSUSE and ArchLinux developers to never make `bash` depend on a newer libreadline than Sage ships...
> > 
> > Otherwise the problem remains or rearises with future releases of these OSs.
> True, but this problem is not specific to these OSs and applies to every OS.

It seems to be specific to these two Linux distributions - though perhaps there are others, as one Linux distro tends to be based on another. Mint is based on Ubuntu, which is itself based on Debian. 

Most other distros don't ship with a bash that is dynamically linked to readline. It's never been a problem on Solaris or OS X either. Although I've never built Sage fully on either AIX or HP-UX, I'm not aware of any bash/readline issues on those operating systems either. 

Unless someone is willing to set up an OpenSUSE system for people to test on, I can't really see how we can support the latest release. 

http://wiki.sagemath.org/SupportedPlatforms#Linux

says 11.1 is supported, and 11.2 and 11.3 are known to be broken. 

I simply don't have access to the hardware/software to test this. 

William posted a few weeks ago he was wanting people to administer virtual machines. Unless someone is going to do this for the latest OpenSUSE, then I can't see how we can support it. I already admin two machines myself which are buildbot slavs (_hawk_ and _t2_). 

Dave


---

Comment by leif created at 2010-12-13 18:59:23

Replying to [comment:57 drkirkby]:
> Unless someone is willing to set up an OpenSUSE system for people to test on, I can't really see how we can support the latest release. 
> 
> http://wiki.sagemath.org/SupportedPlatforms#Linux
> 
> says 11.1 is supported, and 11.2 and 11.3 are known to be broken. 
> 
> I simply don't have access to the hardware/software to test this.

Just provide an spkg and let the others test (and review) it... ;-)

(until we get more build slaves, running these distros.)


 
> William posted a few weeks ago he was wanting people to administer virtual machines. Unless someone is going to do this for the latest OpenSUSE, then I can't see how we can support it. I already admin two machines myself which are buildbot slavs (_hawk_ and _t2_). 

----

As mentioned on sage-devel, a work-around for a Bash broken by Sage's readline is to set its `RPATH` or `RUNPATH` (with `chrpath`). We could give a hint to that in an error (or warning) message in case we detect installing our readline would break `bash` (but don't know for sure using the system's libreadline will work for us).


---

Comment by jdemeyer created at 2010-12-13 20:07:11

Replying to [comment:56 leif]:
> Not really. Others work fine, so I consider testing if `bash` works with our readline also an (implicit) special case.
> 
> Would you be happy with that?
Well, I don't care too much about this, but if it's possible to test whether `bash` works, that certainly is a better solution.


---

Comment by leif created at 2010-12-13 20:43:08

Replying to [comment:58 leif]:
> As mentioned on sage-devel, a work-around for a Bash broken by Sage's readline is to set its `RPATH` or `RUNPATH` (with `chrpath`). We could give a hint to that in an error (or warning) message in case we detect installing our readline would break `bash` (but don't know for sure using the system's libreadline will work for us).

s/set its `RPATH`/change an existing `RPATH` or `RUNPATH`/

or use `patchelf`, which also supports *creating* / adding such tags.


Another work-around is to set up a `bash` wrapper that (re)sets `LD_LIBRARY_PATH`... ;-)


---

Comment by Koen created at 2010-12-13 23:08:42

Replying to [comment:57 drkirkby]:
> Unless someone is willing to set up an OpenSUSE system for people to test on, I can't really see how we can support the latest release. 
> 
> http://wiki.sagemath.org/SupportedPlatforms#Linux
> 
> says 11.1 is supported, and 11.2 and 11.3 are known to be broken. 
> 
> I simply don't have access to the hardware/software to test this. 

I've been testing openSUSE lately - and theory and practice are completely reversed. Sage does not build on 11.1 due to readline 5.x being the default there. Whereas on openSUSE 11.2 and 11.3, Sage builds properly (a recent 4.6.1.rc0 snapshot).
However, I'm not sure how to test if my final Sage 'works' w.r.t. the readline/bash problem, so I will only claim that it builds and sage starts properly.


---

Comment by Koen created at 2010-12-13 23:12:47

Note: it might be reasonable to drop support for openSUSE 11.1, because it will stop receiving security updates after December 31st, 2010 (the release is 2 years old now).


---

Comment by leif created at 2010-12-14 00:41:56

Replying to [comment:62 Koen]:
> Note: it might be reasonable to drop support for openSUSE 11.1, because it will stop receiving security updates after December 31st, 2010 (the release is 2 years old now).

We shouldn't have to drop support for that, installing / using our 6.1 package should work there as well.

(Bash would still use the system's 5.x version.)

We just have to fix / remove the old copying stuff... (and I would add the mentioned sanity check).


---

Comment by drkirkby created at 2010-12-14 01:36:47

Replying to [comment:62 Koen]:
> Note: it might be reasonable to drop support for openSUSE 11.1, because it will stop receiving security updates after December 31st, 2010 (the release is 2 years old now).

It's a shame that support is dropped so soon in the Linux world - this contrasts widely with professional Unix systems like Solaris. Solaris 8 was released in February 2000 and will be supported until March 2012 (i.e. supported for 12 years). Similar patterns will be seen on AIX and HP-UX I expect. 

Not everyone runs the latest version of the operating system. For many people, they don't update the OS until they buy a new computer. I consider myself pretty IT literate, but looking at my computers, many don't have the latest releases. I grew out of the habit of updating the OS because a new one came out. 

Dave


---

Comment by drkirkby created at 2010-12-14 02:06:38

Replying to [comment:58 leif]:
> Replying to [comment:57 drkirkby]:
> > Unless someone is willing to set up an OpenSUSE system for people to test on, I can't really see how we can support the latest release. 
> > 
> > http://wiki.sagemath.org/SupportedPlatforms#Linux
> > 
> > says 11.1 is supported, and 11.2 and 11.3 are known to be broken. 
> > 
> > I simply don't have access to the hardware/software to test this.
> 
> Just provide an spkg and let the others test (and review) it... ;-)
> 
> (until we get more build slaves, running these distros.)

I've done that. I created the package. It's now marked as "needs work" but it is going to need to be worked on by someone else. 

In general, I very much like the approach taken by `autoconf`, where instead of having a huge lookup table detailing what version of what OS supports this function or that function, it actually *tests* the functionality. Overall that seems a far more logical approach to me, and seems to be what Jeroen is proposing. If we can *test* the functionality of bash, rather than having code that attempts to find a specific Linux release, then testing seems a better way forward. 

Dave


---

Comment by leif created at 2010-12-14 03:10:34

Replying to [comment:65 drkirkby]:
> I've done that. I created the package. It's now marked as "needs work" but it is going to need to be worked on by someone else.

Ok. If you're not going to change it further, I can do that in the next days.


 
> In general, I very much like the approach taken by `autoconf`, where instead of having a huge lookup table detailing what version of what OS supports this function or that function, it actually *tests* the functionality. Overall that seems a far more logical approach to me, and seems to be what Jeroen is proposing. If we can *test* the functionality of bash, rather than having code that attempts to find a specific Linux release, then testing seems a better way forward.

Well, autotools, or the scripts their files are built from, have a lot of knowledge coded into them (like chess programs, or e.g. `gcc`, too), i.e. they also - at least partially - detect the system and make the choices based on that.

(And packages using autotools still have `configure` options like `--with-package-xy=/path/to/package-xy`, `--with-included-package-xy` and `--with-system-package-xy`, and lots of `--disable-*` and `--enable-*` one sometimes _has to_ specify manually. Try e.g. building a "customized" version of a recent GCC, with dozens of settings also for GMP, MPFR, MPC, PPL and CLooG, probably other packages like gettext and zlib as well. Also, GCC does drop support of older platforms, OSs and architectures, due to a lack of developer resources.)


Feel free to extend Sage's `configure` (which really could do much more, setting appropriate environment variables [like your famous `CFLAG64`] etc.)...

But Sage is (also) a distro with many "foreign" packages, not just a program, and to make things work together, we have to make choices normally a user would make - manually - for each of Sage's packages.

The user can still fake Sage's readline was already installed such that Sage will use the system's one, but that requires some more reading and typing than just issuing `make` (or double-clicking the Makefile). ;-)

Same for other packages.


---

Comment by jdemeyer created at 2010-12-16 09:07:52

Thanks for the work on this ticket.  Do you think it is realistic to fix this spkg in the next days?  If not, I will unmerge this spkg and release Sage 4.6.1 with the old readline spkg (which also has problems).


---

Comment by jdemeyer created at 2010-12-16 09:12:02

Additional note: I don't mind merging a partially-fixed readline 6.1 (with some issues remaining) if there is a clear improvement over the old readline 6.0.p4 spkg.  In that case, we should try to converge on a 6.1 spkg which can get positive_review and leave further changes to a different ticket.


---

Comment by drkirkby created at 2010-12-16 17:33:50

Replying to [comment:61 Koen]:
> Replying to [comment:57 drkirkby]:
> > Unless someone is willing to set up an OpenSUSE system for people to test on, I can't really see how we can support the latest release. 
> > 
> > http://wiki.sagemath.org/SupportedPlatforms#Linux
> > 
> > says 11.1 is supported, and 11.2 and 11.3 are known to be broken. 
> > 
> > I simply don't have access to the hardware/software to test this. 
> 
> I've been testing openSUSE lately - and theory and practice are completely reversed. Sage does not build on 11.1 due to readline 5.x being the default there. Whereas on openSUSE 11.2 and 11.3, Sage builds properly (a recent 4.6.1.rc0 snapshot).
> However, I'm not sure how to test if my final Sage 'works' w.r.t. the readline/bash problem, so I will only claim that it builds and sage starts properly.

This is a can of worms. Sage certainly was built on 11.1 on 21<sup>st</sup> October. 

http://build.sagemath.org/sage/builders/openSUSE%2011.1-64%20%28menas%29

I'll leave others to judge if my package is better or worst than the present one. Obviously if someone can improve the readline package soon, it would be good to get an improved version in Sage. But if nobody has the time/resources to do so, then perhaps merging my 6.1 will be preferable to leaving the old one. 

Dave


---

Comment by jdemeyer created at 2010-12-19 12:59:15

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-12-19 12:59:15

Replying to [comment:69 drkirkby]:
> But if nobody has the time/resources to do so, then perhaps merging my 6.1 will be preferable to leaving the old one. 

With these words, I propose the _current_ spkg http://boxen.math.washington.edu/home/kirkby/readline-6.1.spkg] for review.


---

Comment by vbraun created at 2011-01-08 00:40:43

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2011-01-08 00:40:43

This ticket certainly illustrates why screwing with LD_PRELOAD / LD_LIBRARY_PATH is considered bad practice for any nontrivial project. The imho only correct fix is to explicitly set the RPATH/RUNPATH in all of Sage's binaries, and not set LD_LIBRARY_PATH. But then, thats for another ticket...

As far as readline is concerned, I think the current state is a definite improvement. Since there is really no remaining issue that can be fixed easy, I give this a positive review so that we can go ahead with releasing Sage-4.6.1.


---

Comment by jdemeyer created at 2011-01-09 18:59:44

Resolution: fixed
