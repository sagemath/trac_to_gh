# Issue 8306: Parallel inter/intra-spkg builds

Issue created by migration from https://trac.sagemath.org/ticket/8306

Original creator: mpatel

Original creation time: 2010-02-19 11:31:16

Assignee: GeorgSWeber

CC:  mhansen mvngu

Along with a primed [ccache](http://ccache.samba.org/), compiling multiple spkgs in parallel may significantly speed up Sage builds on multicore machines.

See [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/4c915ae814dd6514) for some information.


---

Comment by mpatel created at 2010-02-25 11:43:44

See #7943 and #8191 for recent changes to `makefile`, `spkg/install`, and `spkg/standard/deps`.


---

Comment by mpatel created at 2010-02-25 17:36:33

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-02-25 17:36:33

With a "primed" compiler cache, i.e., I've already built Sage at least once, I can build Sage sans docs in about 15-20 minutes on an otherwise mostly idle sage.math --- with `make -j20`.  The long doctests pass (after I've built the docs).


---

Comment by cremona created at 2010-02-25 19:50:04

What is it about eclib which makes this fail?  I would be happy to change it if only I knew -- the "exceptionally clear explanation" you refer to was not quite clear enough for me...  John


---

Comment by mpatel created at 2010-02-26 23:13:45

Oops.  That was an attempt at humor.

I don't know why the build fails.  [Here's a log](http://sage.math.washington.edu/home/mpatel/trac/8306/eclib-20080310.p9.log) from building eclib with `+`.

A possibly related problem is that the top-level make doesn't notice the error.  It keeps going until "Sage build/upgrade complete!".  I'll see what happens if I add `$(INST)/$(ECLIB)` to "all"'s list of dependencies.


---

Comment by mpatel created at 2010-02-27 03:18:47

Replying to [comment:6 mpatel]:
> [...] I'll see what happens if I add `$(INST)/$(ECLIB)` to "all"'s list of dependencies.
Same result.  All of the other spkgs build properly.  But I definitely need to figure out why this happens with eclib and check the other spkgs for similar potential behavior.


---

Comment by mpatel created at 2010-02-27 03:18:47

Changing status from needs_review to needs_work.


---

Attachment

Tweak eclib `Makefile`s so it builds with `+`.  eclib src repo.


---

Comment by mpatel created at 2010-02-27 05:45:55

[attachment:eclib_makefiles.patch This patch] gets eclib to build with `+`.  I noticed that eclib's `spkg-install` contains

```sh
if [ "$MAKE" == gmake ]; then 
   echo "using gmake"
else
   echo "Disabling parallel make for now"
   MAKE=make; export $MAKE
fi
```

Is there a particular reason for this?


---

Comment by mpatel created at 2010-02-27 06:52:16

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-02-27 07:09:13

I've updated the attachments so the usual build behavior is the default.  To tell make it's OK to build multiple spkgs at a time, set `PARALLEL_SPKG_BUILD="yes"` near the top of `spkg/standard/deps`.

The new `deps` "depends" on an eclib spkg with [attachment:eclib_makefiles.patch] (or an equivalent).  Should I make it part of #8357?


---

Comment by mpatel created at 2010-02-27 07:10:59

Replying to [comment:10 mpatel]:
> I've updated the attachments so the usual build behavior is the default.  To tell make it's OK to build multiple spkgs at a time, set `PARALLEL_SPKG_BUILD="yes"` near the top of `spkg/standard/deps`.
That should be "near the top of `spkg/install`."


---

Comment by drkirkby created at 2010-02-27 10:16:34

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-02-27 10:16:34

The idea seems excellent. Ir is such a waste on modern machines to 

I think it would be a lot better if an environment variable SAGE_PARALLEL_BUILD or SAGE_PARALLEL_SPKG_BUILD was set to "yes", rather than require the user to edit the spkg/install. Since virtually all other environement variables are prefixed with SAGE (e.g. SAGE_FORTRAN, SAGE_FORTRAN_LIB, SAGE64 ...) I would do likewise for consistency. 

It would be necessary to test this on different architectures and operating systems. It is quite possible that the time different packages take to build differs vastly by the processor and operating system. It is likely that package X always builds in parallel before package Y on sage.math, but Y would build before X on another system. That could well mean there are dependencies existing that are not apparerent in serial builds. 

For example, ATLAS takes at least 10x as long to build on 't2' as it does on my own SPARC, simply because there are no default tuning parameters for ATLAS on t2, so it is tuned each time. That is an extreme example, but it is well known some machine are faster at some tasks than others, but slower on other tasks. Some packages have assembly language support for certain processors, but not others. Several packages go through some sort of tuning process to determine the optimal build parameters. So the timings could be expected to be different on different operating systems. 

At the very least, this should be tested on t2 and bsd, as they run Solaris and OS X repectively. (When testing on t2, I would suggest using j of 256 or 512. That machine has 128 threads). For t2, one would need to use sage 4.3.0.1. (I think any changes to spkg/install and spkg/standard/deps should minimal between 4.3.0.1 and 4.3.3.  There are probably no changes at all. 

It would be safer to compare the md5 checksums of libraries & binaries built in series and parallel to prove they are indeed the same. It is quite possible that there are failures that just do not get exercised by doctests. However, that may not be fully possible, as perhaps some would have the build time information encoded in some way. But I would at least investigate. 

Overall, I think this is a really *excellent* idea, but it needs further testing before I'd want to give it a positive review. 

Dave


---

Comment by cremona created at 2010-02-27 11:36:33

I didn't write eclib's spkg-install, and I know that several people have changed it in the past -- there's at least one ticket out there specifically about managing eclib's Makefiles.

Next time someone edits it they should change the two occurrences of "cremona" in error messages to "eclib".


---

Comment by mpatel created at 2010-02-27 22:58:18

Replying to [comment:14 cremona]:
> I didn't write eclib's spkg-install, and I know that several people have changed it in the past -- there's at least one ticket out there specifically about managing eclib's Makefiles.
Indeed, the workaround is from #4228.
> Next time someone edits it they should change the two occurrences of "cremona" in error messages to "eclib".
I'll make a new spkg available at #8357.


---

Comment by mpatel created at 2010-02-28 00:25:42

Replying to [comment:15 mpatel]:
> I'll make a new spkg available at #8357.
Done, with a provisional version, at least.


---

Comment by mpatel created at 2010-02-28 01:42:25

Replying to [comment:13 drkirkby]:

> The idea seems excellent. Ir is such a waste on modern machines to

Thanks!  I'll get an account on bsd and try to test on both bsd and t2, as well.

`SAGE_PARALLEL_SPKG_BUILD` looks good.

My motivation for making the new feature optional, for now, is so we can get feedback (via sage-devel) from early testers about a much wider range of build conditions and configurations.  It's likely they'll report problems, and we can attempt to solve them before we make it the default for everyone.


---

Attachment

Make `sage -i foo.spkg` also append to `spkg/logs/foo.spkg`.  *scripts* repo.


---

Comment by mpatel created at 2010-03-01 16:27:50

Again, against 4.3.3 on sage.math, this appears to work well.  With `SAGE_CHECK="yes"`, I get the same known errors

```
     sage: An error occurred while testing sagetex-2.2.3
     sage: An error occurred while testing pyprocessing-0.52.p0
     sage: An error occurred while testing sqlalchemy-0.4.6.p1
```

with and without parallel spkg builds.  All the docs build and the long doctests pass.

Against 4.3.0.1 on t2: It builds and runs --- I used a stand-in atlas spkg that just copies the files from the [existing binary build](http://boxen.math.washington.edu/sage/solaris/index.html).  "Several" doctests still fail or segfault.  With `SAGE_CHECK="yes"`, I get the known testing errors, a known testing error with eclib (see #8357),  and _maybe_ a testing error with R.  I ran out of patience with the latter.  I don't have time to test further on t2 / *Solaris.  It's probably better that someone else test with 4.3.3+ on a capable machine.

If I have time (and an account), I'll run a few tests on `bsd.math`.

Note: With `SAGE_PARALLEL_SPKG_BUILD="yes"`, I find it useful to run one of

```sh
grep "An error occurred" SAGE_ROOT/install.log
ls -l SAGE_ROOT/spkg/installed | wc
```

when I see `"Sage build/upgrade complete!"`.  Maybe we should add a similar check at the end of `install`?

Please test and let us know what happens.  I didn't log detailed statistics, but with a warm compiler cache, I noticed a roughly three-fold speedup.  From a recent run on sage.math:

```
Sage build/upgrade complete!

real    15m44.846s
user    45m55.780s
sys     11m10.470s
```



---

Comment by mpatel created at 2010-03-01 16:30:23

Replying to [comment:19 mpatel]:

> [... ...] with a warm compiler cache, I noticed a roughly three-fold speedup. [... ...]

I should add that this could be very useful to a release manager.


---

Comment by drkirkby created at 2010-03-01 16:33:58

Replying to [comment:20 mpatel]:

> I should add that this could be very useful to a release manager.
What exactly is a "warm compiler cache" ? A Google on the term only shows only references to Sage.


---

Comment by mpatel created at 2010-03-01 16:53:23

Oops.  I just mean that I've set up [ccache](http://ccache.samba.org/) and compiled Sage twice, say.  Stats from t2:

```
mpatel@t2 ~$ ccache -s
cache directory                     /home/mpatel/.ccache
cache hit                          34598
cache miss                         23288
called for link                     5050
multiple source files                 14
compiler produced stdout              10
compile failed                       774
preprocessor error                   465
couldn't find the compiler            39
not a C/C++ file                    3409
autoconf compile/link               7006
unsupported compiler option         2815
no input file                       3107
files in cache                     45248
cache size                           2.3 Gbytes
max cache size                       5.0 Gbytes
```

(I think it'll be faster in `/scratch`, but I don't know by how much.)  From sage.math:

```
mpatel@sage ~$ ccache -s
cache directory                     /scratch/mpatel/.ccache
cache hit                         371602
cache miss                         61435
called for link                    48342
multiple source files                131
compiler produced stdout              78
compile failed                      2635
ccache internal error                  2
preprocessor error                  2433
cache file missing                     4
not a C/C++ file                   15851
autoconf compile/link              39762
unsupported compiler option        21463
no input file                      18871
files in cache                    106837
cache size                           4.6 Gbytes
max cache size                      10.0 Gbytes
```

(Lots of testing with different `X` values.)  I've been using ccache 2.4.  I don't know how 3.0pre0 compares.


---

Comment by mpatel created at 2010-03-02 23:08:43

Reminder: Update #8263, if it's necessary.


---

Comment by mvngu created at 2010-03-04 04:05:19

Ticket #8432 adds iconv to the dependency rule for building gd. So you don't need to implement that rule here.


---

Comment by mpatel created at 2010-03-05 01:02:20

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-03-05 01:02:20

I've attached updates rebased vs. #7943 and #8432.


---

Comment by mpatel created at 2010-03-05 01:06:27

Adding Mike Hansen to the Cc: list.


---

Comment by mpatel created at 2010-03-05 03:53:30

Strange error when building on sage.math with `MAKE="make -j23 -l25"` and `SAGE_PARALLEL_SPKG_BUILD` *not* set:

```
Now install rpy
**************************************************************************
You must compile Sage first using 'make' in the Sage root directory.
(If you have already compiled Sage, you must set the SAGE_ROOT variable in 
the file '/mnt/usb1/scratch/mpatel/tmp/sage-4.3.4.alpha0/sage').
**************************************************************************
Error installing rpy.
```



---

Comment by mpatel created at 2010-03-05 04:29:29

Fixed by appending `SAGE_SCRIPTS` to `BASE`.  I'm putting the updates here:

 * http://sage.math.washington.edu/home/mpatel/trac/8306


---

Comment by mvngu created at 2010-03-07 04:25:45

With Sage 4.3.4.alpha0 on sage.math, I updated "deps" and "install" with [deps](http://sage.math.washington.edu/home/mpatel/trac/8306/deps) and [install](http://sage.math.washington.edu/home/mpatel/trac/8306/install). I exported these environment variables:

```
export SAGE_PARALLEL_SPKG_BUILD="yes"
export MAKE="make -j4"
make 
```

The build failed with 

```
Successfully installed gap-4.4.12.p1
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing gap-4.4.12.p1.spkg
make[1]: Leaving directory `/dev/shm/mvngu/sandbox/sage-4.3.4.alpha0/spkg'

real    45m12.933s
user    105m39.580s
sys     15m46.550s
Error building Sage.
Traceback (most recent call last):
  File "/dev/shm/mvngu/sandbox/sage-4.3.4.alpha0/local/bin/sage-preparse", line 230, in <module>
    do_preparse(f)
  File "/dev/shm/mvngu/sandbox/sage-4.3.4.alpha0/local/bin/sage-preparse", line 118, in do_preparse
    from sage.misc.preparser  import preparse_file
ImportError: No module named sage.misc.preparser
```



---

Comment by mpatel created at 2010-03-07 05:26:00

The eclib and sage packages did not build:

```sh
$ grep "An error occurred" /dev/shm/mvngu/sandbox/sage-4.3.4.alpha0/spkg/logs/*
eclib-20080310.p9.log:sage: An error occurred while installing eclib-20080310.p9
sage-4.3.4.alpha0.log:sage: An error occurred while installing sage-4.3.4.alpha0
```

Ticket #8357's `eclib-*.spkg` should fix this.  I apologize for not mentioning it in "To test the changes".

Questions:

 * If I untar `sage-*.tar`, copy over `install`, etc., and start the build, then at some point, `install` is overwritten with the original version.  Do you know which package or script does this?  For my tests, I've run `chmod u-w install` before `make`.

 * I don't know why the build didn't stop when eclib failed to build.  This seems strange.  The file `installed/eclib*` is missing and according to `deps`, it's required for the `sage` target.  Similarly, `installed/sage*` is a prerequisite for gap.  Does anyone know why this happens?  Can we modify `deps` to avoid it?


---

Comment by mpatel created at 2010-03-07 06:31:15

To install and use ccache, I did this

```sh
wget http://samba.org/ftp/ccache/ccache-2.4.tar.gz
tar zxvf ccache-2.4.tar.gz
cd ccache-2.4
./configure
make
cp ccache ~/bin
```

Because I set

```sh
PATH=".:$HOME/bin:$HOME/apps/sage/local/bin:$PATH"
```

in `~/.profile`, I did

```sh
cd ~/bin
ln -s c++ ccache
ln -s cc ccache
ln -s g++ ccache
ln -s g++-3.4 ccache
ln -s g++-4.2 ccache
ln -s gcc ccache
ln -s gcc-3.4 ccache
ln -s gcc-4.1 ccache
ln -s gcc-4.2 ccache
ln -s x86_64-linux-gnu-g++ ccache
ln -s x86_64-linux-gnu-g++-3.4 ccache
ln -s x86_64-linux-gnu-g++-4.2 ccache
ln -s x86_64-linux-gnu-gcc ccache
ln -s x86_64-linux-gnu-gcc-3.4 ccache
ln -s x86_64-linux-gnu-gcc-4.1 ccache
ln -s x86_64-linux-gnu-gcc-4.2 ccache
ln -s x86_64-linux-gnu-gcj-4.2 ccache
ln -s x86_64-linux-gnu-gfortran ccache
ln -s x86_64-linux-gnu-gfortran-4.1 ccache
ln -s x86_64-linux-gnu-gfortran-4.2 ccache
```

This may be overkill.  In `~/.bashrc`, I've put

```sh
export CCACHE_DIR=/scratch/mpatel/.ccache
```



---

Comment by mpatel created at 2010-03-07 06:35:26

I also set a larger ccache size with `ccache -M 10G`.  To print statistics run `ccache -s`.


---

Comment by mvngu created at 2010-03-07 06:51:52

The patch [trac_8306_scripts-spkg_log_files.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8306/trac_8306_scripts-spkg_log_files.patch) introduces the environment variable

```
SAGE_LOGS="$SAGE_ROOT/spkg/logs"
```

for storing build logs of spkg's. A closely related idea, but for MD5 integrity check files, can be found at #7617. What could be implemented is an environment variable like

```
SAGE_SPKG_MD5="$SAGE_ROOT/spkg/md5"
```

As of Sage 4.3.3, the SageTeX package is the only standard package that has an MD5 file bundled together with the package itself to result in an spkg. Whenever the SageTeX spkg is built, its MD5 file is extracted and lingers under 

```
SAGE_ROOT/spkg/build
```

Perhaps a more appropriate place is to deposit MD5 files of spkg's under

```
SAGE_ROOT/spkg/md5
```

This would nicely solve ticket #329 after more than 3 years.


---

Comment by mpatel created at 2010-03-07 09:32:51

We could do the integrity check and relocation (`mv -f foo.md5 "$SAGE_SPKG_MD5"`) in `spkg-checksum`, say, call this script in `sage-spkg`, test `$?`, print a message, etc.  Or we could just delete `foo.md5`.  How useful is the file outside the archive?


---

Comment by mpatel created at 2010-03-07 14:51:07

Replying to [comment:32 mpatel]:
>  * I don't know why the build didn't stop when eclib failed to build.  This seems strange.  The file `installed/eclib*` is missing and according to `deps`, it's required for the `sage` target.  Similarly, `installed/sage*` is a prerequisite for gap.  Does anyone know why this happens?  Can we modify `deps` to avoid it?

The problem is that the exit status `$?` of

```sh
$(SAGE_SPKG) $(FOO) 2>&1 | tee -a $(SAGE_LOGS)/$(FOO).log
```

is the exit status of `tee`, but we need the exit status of `sage-spkg`.  (I found some other workarounds [here](http://www.unix.com/shell-programming-scripting/92163-command-does-not-return-exit-status-due-tee.html).)  We can get this with `$PIPESTATUS` in `bash`.  We could add a helper script somewhere that runs the pipeline and exits with the status of `sage-spkg`.

Or we could use

```sh
$(SAGE_SPKG) $(FOO) 2>&1 | tee -a $(SAGE_LOGS)/$(FOO).log | grep "sage: An error occurred while"
```

if we test the status of `grep`.  The `sage-spkg` script prints this error string when `spkg-install` or `spkg-check` fails.   We could also print the string in a few other places in `sage-spkg` (search for `exit 1`).

Thoughts?


---

Comment by mpatel created at 2010-03-07 18:56:28

I have a helper script that I'm testing.  So far, it's working well, _if_ I force palp to build serially.  The spkg at #8477 does this.


---

Comment by drkirkby created at 2010-03-08 00:22:22

Replying to [comment:35 mvngu]:

> Perhaps a more appropriate place is to deposit MD5 files of spkg's under
> {{{
> SAGE_ROOT/spkg/md5
> }}}
> This would nicely solve ticket #329 after more than 3 years.

See my comment on #329. The problem with md5 is that there is no standard command for getting the md5 checksum. I've seen

 * md5
 * md5sum
 * digest -a md5 ('digest' is part of OpenSSL, and is what I use on Solaris)

It is not a standard POSIX command. In contrast, 'cksum' is much more portable, as it is defined by POSIX. 

http://www.opengroup.org/onlinepubs/9699919799/utilities/cksum.html

It is a 32-bit bit number, so the probability of an error not being detected is around 2.3 x 10^-10.  

Avoid using 'sum' - that is not portable, as the algorithm is implementation dependent. 

Dave


---

Comment by mpatel created at 2010-03-09 04:28:50

I've updated the description with what seems to work.  With `SAGE_PARALLEL_SPKG_BUILD="yes"`, `make` should now _not_ start building new spkgs if it encounters a fatal error with a package.  It'll just wait for the other processes to stop.

Feel free to find a better place or name for the short `pipestatus` script.


---

Comment by drkirkby created at 2010-03-09 11:16:57

Is the intension to use SAGE_CHECK="ok", rather than SAGE_CHECK="yes". I'm not sure if that's a typo in your revised description.


---

Comment by mpatel created at 2010-03-09 11:48:58

It's just to avoid running some [comment:ticket:8262:2 tests twice].


---

Comment by mpatel created at 2010-03-11 04:03:46

Building spkgs in parallel with 4.3.4.alpha1 per the description:

sage.math: Still works.  Long doctests pass.

bsd: Works, but sometimes palp doesn't build properly.  I think this is a problem with palp's makefiles.  I'll update #8477.  Long doctests pass.

t2: Works with the [stand-in atlas package](http://sage.math.washington.edu/home/mpatel/trac/8306/atlas-3.8.3.p13.spkg) mentioned earlier and modulo a problem with cddlib that happens even with serial builds ([log](http://sage.math.washington.edu/home/mpatel/trac/8306/cddlib-094f.p5.log)).  Long doctests pass, except for `ell_rational_field`, `ell_curve_isogeny`, and `ssmod`, which timed out.  Their short versions pass.


---

Comment by drkirkby created at 2010-03-11 05:21:36

On my Blade 1000 (900 MHz), bought for the US equivalent of about $75, all those tests pass, in the times indicated below: 


```
sage -t  -long "devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py"
         [933.6 s]

sage -t  -long "devel/sage/sage/modular/ssmod/ssmod.py"     
         [1737.7 s]

sage -t  -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
         [1590.4 s]
```


Given my Blade 1000 is faster than 't2', and the default value for SAGE_TIMOUT_LONG is 1800s, it is no surprise these timeout. You will need to increase that variable. I think 10000 s should be safe (actually I rekon 4000 s will be, but I'd play it safe). 

I'm surprised the short ones passed if you used the default 300 s timeout. 

Dave


---

Comment by mpatel created at 2010-03-12 09:33:00

I increased the timeout for the short tests.  I've also increased the timeout for the long tests and rerun the timed-out tests.  They pass.

Also: As far as I can tell, this ticket does not break builds where `SAGE_PARALLEL_SPKG_BUILD != "yes"`.


---

Comment by jhpalmieri created at 2010-04-06 05:50:24

Two comments: 

 - Note that the sage_scripts spkg overwrites the file spkg/install, so a few minutes after you've run "make", that file no longer has the parallel build changes in it.  I assume that this doesn't interfere with the current build (?).  This would be fixed by implementing the changes here and making a source distribution, thereby producing a new sage_scripts spkg.  Is that the only way?  Or at least the best way?

 - Running "make distclean" should delete spkg/logs/*.  Here's a patch.


---

Attachment

new version of SAGE_ROOT/makefile


---

Comment by jhpalmieri created at 2010-04-06 05:51:16

diff of SAGE_ROOT/makefile


---

Attachment

scripts repo: add pipestatus to source distribution


---

Comment by jhpalmieri created at 2010-04-06 22:18:57

Changing status from needs_review to needs_work.


---

Attachment

Running "sage -sdist" with these changes doesn't work because pipestatus doesn't get copied over.  The patch "trac_8306_scripts-pipestatus.patch" fixes this.

I was able to successfully build this on sage.math, but I had problems on my mac (with two cores, using "make -j2").  I think it's with singular; I get lots of lines like

```
sage/libs/singular/singular.cpp:162:21: error: factory.h: No such file or directory
```

It seems to be building singular at the same time as the main Sage spkg; does that sound okay?


---

Comment by jhpalmieri created at 2010-04-06 22:21:34

From spkg/logs/singular-3-1-0-4-20100214.log:

```
make install in omalloc
gcc -O3 -g -fPIC -I. -I/Applications/sage_builds/sage-4.3.5.1/local/include  -I/Applications/sage_builds/sage-4.3.5.1/local/include -DHAVE_CONFIG_H -DOM_GENERATE_INC omTables.c -o omTables
./makeheader om_Alloc.h omalloc.h
makeheader: Include file omTables.h not found
make[4]: *** [omalloc.h] Error 1
make[3]: *** [install] Error 1
make[2]: *** [/Applications/sage_builds/sage-4.3.5.1/local/bin/Singular-3-1-0] Error 2
Unable to build Singular.
```



---

Comment by jhpalmieri created at 2010-04-07 04:27:54

Typo in deps: 

```
$(SAGE_LOGS)/$(FLINGQS).log
```

should say 

```
$(SAGE_LOGS)/$(FLINTQS).log
                   ^
```



---

Comment by jhpalmieri created at 2010-04-07 06:14:55

On my iMac, the following packages failed to build with SAGE_CHECK='1':

 - iconv (failed because spkg-check failed; this should be fixed by the new iconv spkg at #8638)
 - sagetex (failed because spkg-check failed; this is because spkg-check requires the main Sage library, but Sage is not a prerequisite for sagetex in spkg/standard/deps - ought to be fixable, but I'm not sure what the right prerequisites are: sage, maxima, gap?  Perhaps should be done independently of this ticket?)
 - ecl (failed, but I don't know why -- see the log file [here](http://sage.math.washington.edu/home/palmieri/misc/ecl-10.2.1.log))
 - maxima (failed because ecl failed, although I don't know why the build process didn't just stop when ecl failed)
 - singular (failed, but I don't know why -- see the log file [here](http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-4-20100214.log))
 - sage (failed because singular failed)

For both singular and ecl, I was able to build them by turning off parallel building just for them (by hand).  Then after turning off SAGE_CHECK, everything else built successfully.


---

Comment by jhpalmieri created at 2010-04-10 23:50:03

From irc:

```
<_leif> we don't need "pipestatus" either
<_leif> "set -o pipefail;"
<_leif> that will set the exit status of a pipe to the last non-zero one
```

Some random web page says that this was introduced in version 3 of bash and doesn't work on the Mac, but it does work on my Mac running OS X 10.6.  I guess this may not work on OS X 10.4, as that seems to have included version 2.


---

Comment by leif created at 2010-04-11 00:35:20

Replying to [comment:53 jhpalmieri]:
> Some random web page says that this was introduced in version 3 of bash and doesn't work on the Mac, but it does work on my Mac running OS X 10.6.  I guess this may not work on OS X 10.4, as that seems to have included version 2.

The `bash` ChangeLog states it was introduced in version 3.0-alpha.

To avoid side effects, the setting should be done just for a/the subshell, i.e. replacing

```
    cmd1 | cmd2 | ... | cmdN | tee logfile
```

by

```
    (set -o pipefail; cmd1 | cmd2 | ... | cmdN | tee logfile)
```


Sufficiently recent versions of bash should at least be _available_ for all OSs currently supported by Sage (including OS X).


---

Comment by jhpalmieri created at 2010-04-11 01:14:48

Replying to [comment:54 leif]:
> Sufficiently recent versions of bash should at least be _available_ for all OSs currently supported by Sage (including OS X).

Recent versions may be available, but we don't necessarily want to require people to install a newer version of bash just to use Sage.  So (if for example OS X 10.4 is officially supported by Sage) we would have to write a script that tests the version of bash (using `${BASH_VERSINFO[0]`}, I guess), and if less than 3, then do something else.

Or since parallel building is an enhancement, I suppose we could make bash 3 a prerequisite for it.  We would have to write SAGE_ROOT/spkg/standard/deps in a way which works with all versions, though.


---

Comment by leif created at 2010-04-11 05:20:42

Replying to [comment:55 jhpalmieri]:
> Or since parallel building is an enhancement, I suppose we could make bash 3 a prerequisite for it.  We would have to write SAGE_ROOT/spkg/standard/deps in a way which works with all versions, though.

Well, `bash` 3.0 was released nearly six years ago (and there are pre-built binaries of it available), so I'd say it _should_ be OK to make it a prerequisite - it's central and ubiquitous, and I'd call 2.x deprecated.

But that's only _my_ opinion, though in general I'd prefer omitting as much GNUism as possible, trying to stay within POSIX scope (which for example the shell's `trap` mechanism is).

[Sorry, maybe too off-topic.]


---

Comment by drkirkby created at 2010-04-11 08:26:46

I too would rather POSIX was used, and not basisms. The -o option is specified by POSIX

http://www.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#set

but note the comment about "unspecified format". If it's possible to avoid that I would, since even bash could change at a later date.


---

Comment by jhpalmieri created at 2010-04-11 15:19:15

> note the comment about "unspecified format".

I read that comment to be about "set -o" with no further options, not about "set -o OPTION". "pipefail" is documented here, by the way:

 http://www.gnu.org/software/bash/manual/bashref.html#The-Set-Builtin

I don't see anything wrong with bashisms, as long as we have #!/usr/bin/env bash at the top of the file. In any case, I'm happy for *any* solution to the pipe situation here: in a command of the form ($1) | ($2), we want the exit code of ($1).

I'm posting experimental versions of pipestatus and deps which test for the bash version and if at least 3, use pipefail.

By the way, I still can't get singular and ecl to compile on my iMac if SAGE_PARALLEL_SPKG_BUILD is set to "yes". Any help with that issue would be appreciated.


---

Attachment

version of pipestatus using pipefail


---

Comment by mpatel created at 2010-06-03 09:54:26

Replying to [comment:58 jhpalmieri]:
> I'm posting experimental versions of pipestatus and deps which test for the bash version and if at least 3, use pipefail.

It appears that `deps-new` is based on a version of `deps` that predates the [latest] version at

 * http://sage.math.washington.edu/home/mpatel/trac/8306/

(last modified on 8 March).  Is there a particular reason for this?  For example, it turns out that we shouldn't use `$(PLUS)`, which can sometimes force an unwanted parallel build within an spkg (i.e., it's better to leave the decision to `spkg-install`).  The 8 March version also fixes [comment:ticket:8306:29 this problem].  But this version still has the `FLINTQS` typo [comment:ticket:8306:51 mentioned above].

> By the way, I still can't get singular and ecl to compile on my iMac if SAGE_PARALLEL_SPKG_BUILD is set to "yes". Any help with that issue would be appreciated.

I'll try to investigate soon.


---

Comment by mpatel created at 2010-06-08 08:56:14

Allow redirection of stderr and other file descriptors.  Add comp.os.unix FAQ reference.


---

Attachment

Replying to [comment:59 mpatel]:
> > By the way, I still can't get singular and ecl to compile on my iMac if SAGE_PARALLEL_SPKG_BUILD is set to "yes". Any help with that issue would be appreciated.
> 
> I'll try to investigate soon.

I've attached updated versions of `deps`, `install`, and `pipestatus` to accompany the `makefile` and the two `trac_8306_scripts-*` patches.  With these and the forthcoming spkgs at #9185, #9186, and #9187, I can build 4.4.4.alpha0 with SAGE_PARALLEL_SPKG_BUILD="yes"`.


---

Comment by mpatel created at 2010-06-09 03:23:16

Replying to [comment:60 mpatel]:
> I've attached updated versions of `deps`, `install`, and `pipestatus` to accompany the `makefile` and the two `trac_8306_scripts-*` patches.  With these and the forthcoming spkgs at #9185, #9186, and #9187, I can build 4.4.4.alpha0 with SAGE_PARALLEL_SPKG_BUILD="yes"`.

I also need the latest Maxima spkg at #8731.


---

Comment by mpatel created at 2010-06-09 07:51:38

Rebased for 4.4.4.alpha0.  Replaces previous version.


---

Attachment


---

Comment by mpatel created at 2010-06-09 09:40:38

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-06-09 15:52:33

I'm testing this now: I've applied the patches, put the new spkg's in place, etc., and run "sage -sdist ...".  Then I unpacked the new tar file and tried building.  It failed on my mac: I needed to change the line (in "deps") from

```
INSTALL = pipestatus
```

to

```
INSTALL = $(SAGE_ROOT)/spkg/pipestatus
```

After making that change, it's building right now.  I'll report on the outcome when it's done.


---

Comment by jhpalmieri created at 2010-06-09 21:28:58

Things look good.  It's worked successfully on sage.math (took 30 minutes!), a Mac, on the skynet machine "lena" (`x86_64-Linux-k10 (with NVIDIA GeForce GPUs)`).  It's still building on t2, although I cheated a bit: I used a build of atlas from a previous Sage install to save myself 11 hours of build time.  It has a chance to finish in 6 or 8 hours instead of the previous time of 17 hours (sans atlas and docs).

I'll report back when the t2 build is done, but once the small change to "deps" is made, I think this will be done (modulo #8731, #9185, #9186, and #9187).


---

Comment by jhpalmieri created at 2010-06-09 23:05:41

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-06-09 23:05:41

The t2 build has completed successfully, in just over 4 hours -- much better than the 17 hours previously required, and even better than the 6 or 8 that I was predicting.  So if you'll fix deps, I'll give this a positive review.


---

Comment by mpatel created at 2010-06-09 23:39:44

I've updated `deps` and `deps.diff`.  Thanks very much to everyone for their help with patches, typos, builds, testing, and other advice!

Additional data: I've had successful builds on bsd, sage.math, and t2.  The long tests pass, up to those to be fixed at #8731 and a [pre-existing failure](http://groups.google.com/group/sage-devel/browse_thread/thread/26b2aae934131c92/4faf6a32bd792962?q=solaris+bsd.py+group:sage-devel#4faf6a32bd792962) in `BSD.py` on Solaris.  Builds with `SAGE_CHECK` set also succeed, except for R on t2, but this appears to be a separate problem (see a later comment).

Should `$(BASE)` be an (in)direct prerequisite for all non-base packages, including Fortran and Cephes?  So far, I haven't had any problems with these.  Pending reports on sage-devel, we could open a separate ticket about making the dependencies in `deps` more explicit/strict.


---

Comment by mpatel created at 2010-06-09 23:39:44

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-06-10 00:09:53

From R's `make check` on t2:

```
Collecting examples for package ‘stats’
  Extracting from parsed Rd's ..............................
Running examples in package ‘stats’
Error: testing 'stats' failed
Execution halted
make[5]: *** [test-Examples-Base] Error 1
```

Some detail from `src/tests/Examples/stats-Ex.Rout.fail`:

```
> contrasts(ffs) <- contr.sum(5, sparse=TRUE)[,1:2]; contrasts(ffs)
Error in .Diag(levels, sparse = sparse) : 
  contr*(.., sparse=TRUE) needs package "Matrix" correctly installed
Calls: contr.sum -> .Diag
Execution halted
```

According to [this log](http://sage.math.washington.edu/home/mpatel/trac/8306/r-2.10.1.p2.log), R's Matrix package isn't built/installed successfully on t2:

```
Loading required package: Matrix
Error in dyn.load(file, DLLpath = DLLpath, ...) : 
  unable to load shared library '/scratch/mpatel/sage-4.4.4.alpha0-j64-par-chk/spkg/build/r-2.10.1.p2/src/library/Matrix/libs/Matrix.so':
  ld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory
Error : require(Matrix, save = FALSE) is not TRUE
```

An alternative is to compare the output of `ls SAGE_LOCAL/lib/R/library` on non-#8306 sage.math and t2 builds.  I think we're also missing class, mgcv, nnet, rpart, spatial, and survival on t2.

But I think this is independent of this ticket --- see, e.g., `/rootpool2/local/kirkby/sage-4.4.3/install.log` on t2.


---

Comment by jhpalmieri created at 2010-06-10 01:31:33

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-06-10 01:31:33

I agree that the R issue can go on another ticket.  I'm marking this as positive review.

Depends on #8731, #9185, #9186, and #9187.


---

Comment by mpatel created at 2010-06-10 07:50:17

Replying to [comment:68 jhpalmieri]:
> I agree that the R issue can go on another ticket.
I've opened #9201 for this problem.


---

Attachment

`spkg/install`.  Rebased for 4.4.4.


---

Attachment

`spkg/standard/deps`.  Rebased for 4.4.4.


---

Comment by mpatel created at 2010-06-24 07:56:28

I've updated `deps` and `install` (and diffs) for Sage 4.4.4's removal of GHMM.


---

Comment by mpatel created at 2010-06-24 07:58:55

Dependencies: #8645, #9185, #9186, #9264.


---

Comment by jhpalmieri created at 2010-06-24 20:33:18

For what it's worth, I think that your "diff" files for deps and install are backwards, showing the diffs from the new version to the old, rather than from the old to the new.

The deps file is a bit off: first, under the target "all", `$(INST)/$(SAGENB)` is listed, but it's not in the "real" version of deps.  I think this is good, and I think it's a bug in the version of deps distributed with Sage.  Other targets are missing from "all", though:

```
  $(INST)/$(JINJA)
  $(INST)/$(JINJA2)
  $(INST)/$(PYGMENTS)
  $(INST)/$(SPHINX)
  $(INST)/$(SQLALCHEMY)
  $(INST)/$(TWISTED)
  $(INST)/$(TWISTEDWEB2)
}}}  
Also, the following lines are missing:
{{{
$(INST)/$(TWISTEDWEB2): $(INST)/$(TWISTED)
	$(INSTALL) "$(SAGE_SPKG) $(TWISTEDWEB2) 2>&1" "tee -a $(SAGE_LOGS)/$(TWISTEDWEB2).log"
}}}
I'm attaching "deps-new" and "deps-new.diff" to fix this.


---

Comment by jhpalmieri created at 2010-06-24 23:33:29

Okay, now I'm confused.

```
  $(INST)/$(TWISTEDWEB2)
```

What is this package?  It's included in the target "all", and the current version of deps has lines

```
$(INST)/$(TWISTEDWEB2): $(INST)/$(TWISTED)
	$(SAGE_SPKG) $(TWISTEDWEB2) 2>&1
```

but it doesn't look like there's an actual package there.  For instance, there are *no* lines like this in install:

```
TWISTEDWEB2 =`$newest twistedweb2`
export TWISTEDWEB2
```



---

Comment by jhpalmieri created at 2010-06-25 00:10:52

I think twistedweb2 used to be a package but is no longer.  I can't find the relevant ticket, but I'm going to remove references to it from deps.  (See also a comment at #9274.)


---

Comment by jhpalmieri created at 2010-06-25 00:11:55

spkg/standard/deps. Rebased for 4.4.4.


---

Attachment

diff between "deps" in 4.4.4 and "deps-new"


---

Attachment

diff between mpatel's "deps" and "deps-new"


---

Comment by jhpalmieri created at 2010-06-25 15:33:39

I tried this again on t2 yesterday.  With `MAKE="make -j4"`, it worked, building Sage (except for Atlas, which I installed by hand) in 4 hours.  For future tickets, we might want to pursue the following: with `MAKE="make -j36"`, the installation failed on the packages `lapack`, `mpir`, `r`, and `sage`.  (After each failure, I switched to "make -j4" until the problematic package was built, then switched back to "j36".)


---

Comment by rlm created at 2010-06-25 15:40:56

Resolution: fixed


---

Attachment

Diff of `spkg/standard/deps` vs 4.4.4.


---

Comment by mpatel created at 2010-06-26 07:48:32

Diff of `spkg/install` vs 4.4.4.


---

Attachment

Replying to [comment:75 jhpalmieri]:
> I think twistedweb2 used to be a package but is no longer.  I can't find the relevant ticket, but I'm going to remove references to it from deps.  (See also a comment at #9274.)

I mentioned twistedweb2 in an [older version of the description](http://trac.sagemath.org/sage_trac/ticket/8306?action=diff&version=70&old_version=3).

Maybe we should add the missing targets (Sphinx, etc.) at #9274?  It does seem better to be explicit about the dependencies.
