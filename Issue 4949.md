# Issue 4949: Optionally build spkgs in $SAGE_BUILD_TMPDIR

Issue created by migration from https://trac.sagemath.org/ticket/4949

Original creator: mabshoff

Original creation time: 2009-01-07 05:20:19

Assignee: mabshoff

CC:  drkirkby leif

$HOME can be slow in case it is NFS mounted for example. So using local scratch space or even better a RAM disk should speed up the build by a nice factor. To so so use $SAGE_BUILD_TMPDIR in case it exists instead of $SAGE_ROOT/spkg/build.

Cheers,

Michael


---

Comment by was created at 2009-01-09 17:28:04

As a temporary hack to see how this "feels" you could delete spkg/build, then make it a symlink to /tmp/build/.


---

Comment by jhpalmieri created at 2010-08-06 21:50:30

Changing priority from critical to minor.


---

Comment by jhpalmieri created at 2010-08-06 21:50:30

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-08-06 21:50:30

Here's a patch.  This implements both `SAGE_BUILD_TMPDIR` and `SAGE_KEEP_BUILT_SPKGS` -- see #9444.  (This is an incremental change rather than a complete reworking of the sage-spkg script, which might be called for.)


---

Comment by jhpalmieri created at 2010-08-06 22:02:27

A little explanation: BUILD is defined (as "build") by sage-env, but it was used sporadically in sage-spkg.  With this patch, it is used more consistently.


---

Comment by mpatel created at 2010-08-06 22:37:49

If/when this merges, we should consider closing #6550.  `SAGE_KEEP_BUILT_SPKGS` is a much better name than `SAGE_KEEP_SPKG_BUILD`.


---

Comment by leif created at 2010-08-06 22:41:16

Nice to see progress in the build process... :)

See also http://trac.sagemath.org/sage_trac/ticket/6550#comment:7 .


---

Comment by leif created at 2010-08-06 22:47:59

Should `SAGE_BUILD_TMPDIR` default to `SAGE_TMPDIR`?

(We have btw. lots of - in some cases not very well-named - environment variables.)

Making use of e.g. a RAM disk (or some user-provided directory) for doctesting is also worth doing.


---

Comment by mpatel created at 2010-08-19 21:59:12

Replying to [comment:7 leif]:
> Making use of e.g. a RAM disk (or some user-provided directory) for doctesting is also worth doing.

You can already set `SAGE_TESTDIR` (or `DOT_SAGE`) to do this.  Or maybe I misunderstand?


---

Comment by mariah created at 2011-05-20 14:01:27

Changing status from needs_review to needs_work.


---

Comment by mariah created at 2011-05-20 14:01:27

[attachment: trac_4949-scripts.patch] does not apply:


```
sage: hg_sage.apply("/home/mariah/trac_4949-scripts.patch")
cd "/home/mariah/sage/sage-4.7.rc2-x86_64-Linux-core2-fc/devel/sage" && hg status
cd "/home/mariah/sage/sage-4.7.rc2-x86_64-Linux-core2-fc/devel/sage" && hg status
cd "/home/mariah/sage/sage-4.7.rc2-x86_64-Linux-core2-fc/devel/sage" && hg import   "/home/mariah/trac_4949-scripts.patch"
applying /home/mariah/trac_4949-scripts.patch
unable to find 'sage-spkg' for patching
5 out of 5 hunks FAILED -- saving rejects to file sage-spkg.rej
abort: patch failed to apply
sage: 
```



---

Comment by jhpalmieri created at 2011-05-20 14:40:52

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-05-20 14:40:52

Here's a rebased version of [attachment:trac_4949-scripts.patch].  Note that it's for the scripts repository, so you have to apply it with "hg_scripts.apply(...)" rather than "hg_sage.apply(...)".


---

Comment by mariah created at 2011-05-25 13:35:20

I applied the patch [attachment:trac_4949-scripts.patch], then moved
the modified sage-spkg file to a fresh source directory of sage-4.7.rc4.  I set SAGE_BUILD_TMPDIR and SAGE_KEEP_BUILT_SPKGS, and
did 'make testlong'.  The builds took place in the location SAGE_BUILD_TMPDIR and all tests passed.  I applied the patch [attachment: trac_4949-installation.patch], did 'sage -b', then 'sage -docbuild installation html' and verified that the documentation change was made and makes sense.  Positive review.


---

Comment by mariah created at 2011-05-25 13:35:20

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-05-27 08:07:56

Changing status from positive_review to needs_info.


---

Comment by jdemeyer created at 2011-05-27 08:07:56

I think one should add a note in the documentation about how much disk space this is expected to use.  Are the spkgs first all built and then all deleted or are they built-deleted one by one?


---

Comment by leif created at 2011-08-03 14:09:32

Wouldn't it be sufficient to just (keep the -- perhaps slightly modified -- documentation and the three lines honoring `SAGE_KEEP_BUILT_SPKGS` and) change the variable `BUILD` (bad name btw.) in `sage-env` if `SAGE_BUILD_TMPDIR` is set?

That way this ticket would hardly collide with #11021, which fixes a lot in `sage-spkg` (and a bug in `sage-env` w.r.t. `BUILD`), also using `$BUILD` consistently there.

I also would use `SAGE_BUILD_TMPDIR` "directly", without creating yet another subdirectory (`build`) in it; the spkgs are extracted into their own directories anyway.


---

Comment by leif created at 2011-08-03 14:11:56

Ooops, unfortunately it's not _that_ easy, because `$BUILD` is also just used as a _sub_directory name in `sage-spkg`.


---

Comment by jhpalmieri created at 2011-08-04 15:27:48

Replying to [comment:13 jdemeyer]:
> I think one should add a note in the documentation about how much disk space this is expected to use.  Are the spkgs first all built and then all deleted or are they built-deleted one by one?

I've modified the documentation to try to address this.  I built Sage on various machines (sage.math, David Kirkby's machine hawk, various skynet machines), and found that

 - the single largest subdirectory of "build" can be up to 1165M (building eclib on the skynet machines iras and cleo, ia64 processors).  On all of the other machines, it took at most 880M.  On sage.math, cicero, and my mac, the largest took 320M.

 - the total amount of disk space, if you keep all of the subdirectories can be as large as 5.3G (iras and cleo again) or as small as 2.2G (hawk).

I've put in conservative estimates for these in the documentation.


---

Comment by jhpalmieri created at 2011-08-04 15:27:48

Changing status from needs_info to needs_review.


---

Comment by leif created at 2011-08-04 18:12:55

Replying to [comment:16 jhpalmieri]:
> I've modified the documentation to try to address this.

The usage of `$` is a bit inconsistent: `:file:`$SAGE_ROOT/...`` vs. `:file:`SAGE_BUILD_TMPDIR/...``.

I would add a warning that `SAGE_BUILD_TMPDIR` must not contain spaces, and should be an absolute path (starting with a slash or whatever). Note that none of this is checked in `sage-spkg`; also, a broken `test` might return `true` for an empty string, so I would also `test -n "$SAGE_BUILD_TMPDIR"`.

Also, if `SAGE_BUILD_TMPDIR` is set but the directory does not exist, no warning or error message is printed.




> I built Sage on various machines [...] and found that [...]
> I've put in conservative estimates for these in the documentation.

The actual space required or used does hardly depend on the platform, but the file system characteristics, i.e. the block size.

The worst case space usage is theoretically unlimited when taking into account rebuilds and (re)installations of newer packages, as old build dirs are moved to the `$BUILD/old/` directory if `-s` was specified or `SAGE_KEEP_BUILT_SPKGS=yes`.

(Btw., for some reason the build dirs of the base packages never get deleted. Perhaps that's a side-effect of the "`BUILD` bug", haven't tracked this down.)

I would mention the relationship to the `-s` parameter when installing packages with `sage`; the main reason for the additional environment variable is that there's no other way to achieve what `-s` does when using `make`.


---

Comment by jhpalmieri created at 2011-08-07 20:50:52

Replying to [comment:17 leif]:
> The actual space required or used does hardly depend on the platform, but the file system characteristics, i.e. the block size.

Well, many of the systems on which I tested were on skynet, built in subdirectories of a shared home directory -- all of the skynet machines use the same $HOME.  On some of those machines, building eclib took over 1 gigabyte, while on others, it took under 320 megabytes.  There are certainly differences between the types of libraries produced: .so files on linux, .dylib files on darwin, etc.  I would also guess that the size of the library files might vary depending on the compiler, whether it's 32- or 64-bit, etc.

> The worst case space usage is theoretically unlimited when taking into account rebuilds and (re)installations of newer packages, as old build dirs are moved to the $BUILD/old/ directory if -s was specified or SAGE_KEEP_BUILT_SPKGS=yes.

Right, but the documentation as written is accurate ("After a full build of Sage...") and I think is good enough.  Anyone who sets this variable should be paying attention to the build directory anyway.

> (Btw., for some reason the build dirs of the base packages never get deleted. Perhaps that's a side-effect of the "BUILD bug", haven't tracked this down.)

`prereq` and `bzip` are not installed by sage-spkg but by their own install scripts (`prereq-0.9-install` and `bzip2-1.0.5-install`), which create subdirectories of `build` but don't delete them when they're done.

Adding a comment about the relationship to the `-s` option is a good idea.  I'll try to add some tests for `SAGE_BUILD_TEMPDIR`, too.


---

Comment by jhpalmieri created at 2011-08-08 03:04:25

Here are two new patches.  The scripts patch checks for the existence of SAGE_BUILD_TMPDIR, and it also should correctly delete the build subdirectories afterwards -- I had missed this in the previous patch.


---

Comment by jhpalmieri created at 2011-08-08 03:05:42

scripts repo


---

Attachment

There's a `$` missing in

```
:file:`$SAGE_ROOT/spkg/build` or :file:`SAGE_BUILD_TMPDIR/build`
```


I would clarify that `SAGE_KEEP_BUILT_SPKGS=yes` affects _all_ spkg installations (whether with `./sage [-i|-f]` or `make`, the latter also when _re_building [parts of] Sage), and that the build directory (within the Sage tree or in `$SAGE_BUILD_TMPDIR/`) will definitely grow over time, i.e., whenever new packages get installed or already existing / built packages reinstalled, unless one unsets `SAGE_KEEP_BUILT_SPKGS` at some point (which of course doesn't delete existing subdirectories in the first place).




Your observations regarding the build tree sizes on skynet are interesting; there IMHO shouldn't be such a large difference, at least not when doing "the same thing".

There are differences in object code size between RISC and CISC architectures (on the former usually larger, but _at most_ by a factor of 2 I think) and between 32-bit and 64-bit (mostly on RISC architectures, and also if there's a lot of static data involving e.g. pointers or integers of different size); other differences might be due to debug symbols and _how and what_ we build (e.g. assembly implementations, static or dynamic libraries in addition) on a specific platform.

I would mention the effect of the block size of the file system though (as a note perhaps), since many packages consist of a large number of small files.


---

Attachment

sage repo: update installation guide


---

Comment by jhpalmieri created at 2011-08-08 16:03:14

Replying to [comment:20 leif]:
> I would clarify that `SAGE_KEEP_BUILT_SPKGS=yes` affects _all_ spkg installations.

Done

> and that the build directory will definitely grow over time

I've added some explanation.  It doesn't grow quite as fast as it might, since pre-existing subdirectories are moved to SAGE_ROOT/spkg/build/old/, _overwriting_ copies that were already there.  So just reinstalling Sage over and over again will just use twice as much as space as doing it once.  Upgrading will then take up more space.

> Your observations regarding the build tree sizes on skynet are interesting; there IMHO shouldn't be such a large difference, at least not when doing "the same thing".

"eclib" is the usual culprit.  There are huge differences in the amount of disk space it uses, so on some systems it is by far the largest, and on others, it isn't.  On the skynet machines, "moin" uses a consistent 320 megabytes, whereas eclib ranges from something under that to over 1 gig, depending on the OS and the processor.

> I would mention the effect of the block size of the file system though (as a note perhaps), since many packages consist of a large number of small files.

Done.


---

Comment by mderickx created at 2011-08-24 02:46:18

Changing status from needs_review to positive_review.


---

Comment by mderickx created at 2011-08-24 02:46:18

I've build sage entirely from scratch after applying the patch and replacing the bootstrap version of sage-spkg in SAGE_ROOT/spkg/base and passing all doctest . Both with and without the environment variables set. So I think this one is ready to get merged.


---

Comment by was created at 2011-08-24 23:43:54

Changing keywords from "" to "sd32".


---

Comment by leif created at 2011-08-25 05:16:26

Then all of the changes of #11021 will have to be rebased on this one...

Perhaps easier the other way around. (Note that I still haven't updated the patches there though.)


---

Comment by jhpalmieri created at 2011-09-09 22:15:26

By the way, regarding "After applying, replace the bootstrap version of `sage-spkg` in `$SAGE_ROOT/spkg/base/` with the new version": this is taken care of automatically by the `sage-sdist` script, if one is making a new source distribution.  You just have to make sure that the version in local/bin is up to date.


---

Comment by leif created at 2011-09-09 22:45:25

Replying to [comment:27 jhpalmieri]:
> By the way, regarding "After applying, replace the bootstrap version of `sage-spkg` in `$SAGE_ROOT/spkg/base/` with the new version": this is taken care of automatically by the `sage-sdist` script, if one is making a new source distribution.  You just have to make sure that the version in local/bin is up to date.

Yep.

Hope you don't mind me temporarily moving this to "sage-pending"; I intend to finish #11021 and rebase the patch(es) here on that, the latter presumably much easier than the other way around.

If I don't find the time, I'll set the milestone back to 4.7.2 of course.


---

Comment by jhpalmieri created at 2011-09-10 01:35:39

See also #329 which touches sage-spkg, although not in a very complicated way.


---

Comment by swenson created at 2012-01-22 21:01:57

Is there any update to this?  It has been several months since the last update, and some of us are eagerly anticipating this. :)


---

Comment by jhpalmieri created at 2012-01-23 15:49:28

I've rebased this to Sage 5.0.beta1.  It had a positive review already, so I'm leaving it that way.


---

Attachment

root repo


---

Comment by jdemeyer created at 2012-01-23 16:13:59

Do we *really* want

```
BUILD=build
```

?

I think we have too many variables already.

Also, why introduce a new variable `$BUILD_DIR` instead of using `$SAGE_BUILD_TMPDIR`?


---

Comment by jhpalmieri created at 2012-01-23 18:07:57

Replying to [comment:32 jdemeyer]:
> Do we *really* want
 {{{
 BUILD=build
 }}}
> ?

I don't see a reason for it, it was there before.  Should I create a new patch which removes it?  I think that would fix one or two of the issues from #11021.

> Also, why introduce a new variable `$BUILD_DIR` instead of using `$SAGE_BUILD_TMPDIR`?

The code says, roughly

```
if $SAGE_BUILD_TMPDIR is not empty and points to an existing directory:
    BUILD_DIR=$SAGE_BUILD_TMPDIR
else
    BUILD_DIR=$SAGE_PACKAGES
fi

build Sage in $BUILD_DIR
```



---

Comment by jdemeyer created at 2012-01-23 18:17:01

But why not simplify this to:

```
if $SAGE_BUILD_TMPDIR is not empty:
    sanity check $SAGE_BUILD_TMPDIR but don't change any variables
else
    SAGE_BUILD_TMPDIR=$SAGE_PACKAGES
fi

build Sage in $SAGE_BUILD_TMPDIR
```



---

Comment by jdemeyer created at 2012-01-23 18:17:01

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-01-23 18:18:54

Concerning `$BUILD`: it existed before, but was almost not used.  If the variable serves no purpose and is not meant to be customized, it is cleaner to delete it.


---

Comment by jdemeyer created at 2012-01-23 18:22:41

Something else: do we really want to build in

```
$SAGE_BUILD_TMPDIR/build/atlas-3.8.4.p1/
```


I would find it more natural to build in

```
$SAGE_BUILD_TMPDIR/atlas-3.8.4.p1/
```


And therefore, let $SAGE_BUILD_TMPDIR by default be equal to

```
$SAGE_ROOT/spkg/build/
```


And perhaps drop the requirement for `$SAGE_BUILD_TMPDIR` to be an existing directory: just create it if needed.

(This is just an idea: I don't have strong feelings about this)


---

Comment by jhpalmieri created at 2012-01-23 23:13:18

If you run "sage -i blah"  and "blah" is an optional spkg which needs to be downloaded, would it make more sense to save the spkg in $SAGE_ROOT/spkg/optional/ or in $SAGE_BUILD_TMPDIR/optional? The previous versions of the patch do the second of these, but I think it makes more sense to do the first: downloading spkg files for optional packages is not the same as building, so setting SAGE_BUILD_TMPDIR shouldn't cause the spkg files to end up somewhere nonstandard.  Another way to say it: I don't view downloaded spkg files for optional spkgs as temporary, the way build directories are.

Here's a new patch.  I've removed the variables "BUILD" and "BUILD_DIR", and I've appended "build" to the setting of "$SAGE_BUILD_TMPDIR".  I still check whether `$SAGE_BUILD_TMPDIR` exists, as a safeguard against typos, for example.  Optional spkgs are kept in `$SAGE_PACKAGES/optional` regardless of the setting of `$SAGE_BUILD_TMPDIR.`


---

Comment by jhpalmieri created at 2012-01-23 23:13:18

Changing status from needs_work to needs_review.


---

Attachment

root repo


---

Comment by ohanar created at 2012-02-10 10:29:04

`make clean` does not clean ` $SAGE_BUILD_TMPDIR `...

I would also like ` $SAGE_BUILD_TMPDIR ` to be created if it does not exist, but I can live without.


---

Comment by ohanar created at 2012-02-10 10:29:04

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2012-02-10 22:37:31

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2012-02-10 22:37:31

Okay, here are new patches.  `make clean` and `make distclean` now clean `$SAGE_BUILD_TMPDIR`, and in sage-spkg, if the directory doesn't exist, it is created.  The documentation has been changed to reflect this.  (The "delta" patches are the differences between the old versions and the new ones, for reference.)


---

Comment by jhpalmieri created at 2012-02-10 22:37:59

root repo


---

Attachment

root repo: diff between v2 and v3


---

Attachment

sage repo: update installation guide


---

Attachment

sage repo: diff between original and v2


---

Comment by jdemeyer created at 2012-02-12 12:33:32

Replying to [comment:37 jhpalmieri]:
> Optional spkgs are kept in `$SAGE_PACKAGES/optional` regardless of the setting of `$SAGE_BUILD_TMPDIR.`
I totally agree on this.


---

Comment by jdemeyer created at 2012-02-12 12:35:32

Replying to [comment:37 jhpalmieri]:
> I've appended "build" to the setting of "$SAGE_BUILD_TMPDIR".

I ask you again: why???


---

Comment by jdemeyer created at 2012-02-12 12:35:32

Changing status from needs_review to needs_info.


---

Comment by jhpalmieri created at 2012-02-12 16:03:55

Replying to [comment:41 jdemeyer]:
> Replying to [comment:37 jhpalmieri]:
> > I've appended "build" to the setting of "$SAGE_BUILD_TMPDIR".
> 
> I ask you again: why???

It feels cleaner to me: if I set `$SAGE_BUILD_TMPDIR=/tmp`, then rather than producing many subdirectories of `tmp`, everything will live in `/tmp/build`.  It's easier to clean up by hand, and `make clean` is easier to implement this way; otherwise, I suppose it would have to delete `/tmp/atlas-3.8.4.p1/`, `/tmp/blas-...`, etc.  Or `make clean` could not modify SAGE_BUILD_TMPDIR at all, but the Make manual suggests that `make clean` (and `make distclean`) should "Also delete files in other directories if they are created by this makefile."


---

Comment by jdemeyer created at 2012-02-14 09:33:29

Replying to [comment:42 jhpalmieri]:
> Replying to [comment:41 jdemeyer]:
> > Replying to [comment:37 jhpalmieri]:
> > > I've appended "build" to the setting of "$SAGE_BUILD_TMPDIR".
> > 
> > I ask you again: why???
> 
> It feels cleaner to me: if I set `$SAGE_BUILD_TMPDIR=/tmp`, then rather than producing many subdirectories of `tmp`, everything will live in `/tmp/build`.
My opinion is that the user should set `SAGE_BUILD_TMPDIR=/tmp/build` if that's what he wants.

> Or `make clean` could not modify SAGE_BUILD_TMPDIR at all, but the Make manual suggests that `make clean` (and `make distclean`) should "Also delete files in other directories if they are created by this makefile."  
I think it does make sense if `make clean` would always clean `$SAGE_ROOT/spkg/build` and not `SAGE_BUILD_TMPDIR`.

Anyway: I don't want to fight over this.  I'm happy with whatever the outcome.  The last thing I want is that this ticket gets abandoned.


---

Comment by jdemeyer created at 2012-02-14 09:46:50

One other small thing: I would prefer the directory `build/old` to be created only when needed: replace the line

```
mkdir -p "$SAGE_BUILD_TMPDIR/build/old"
```

by

```
mkdir -p "$SAGE_BUILD_TMPDIR/build"
```

(and change the error message below)

And also replace

```

    mv -f "$PKG_BASE-"* old/  2>/dev/null
```

by

```
    mkdir -p old
    if [ $? -ne 0 ]; then
        echo >&2 "Error creating directory $SAGE_BUILD_TMPDIR/old."
        exit 1
    fi
    mv -f "$PKG_BASE-"* old/
```



---

Comment by jdemeyer created at 2012-02-14 09:46:57

If you really want to go with the "build" subdirectory, I would prefer appending it immediately:

```
if [ -n "$SAGE_BUILD_TMPDIR" ]; then
    SAGE_BUILD_TMPDIR="$SAGE_BUILD_TMPDIR/build"
    if [ ! -d "$SAGE_BUILD_TMPDIR" ]; then
        echo "Creating directory \$SAGE_BUILD_TMPDIR (=$SAGE_BUILD_TMPDIR)."
        mkdir -p "$SAGE_BUILD_TMPDIR"
    fi
    echo "Building in $SAGE_BUILD_TMPDIR."
else
    SAGE_BUILD_TMPDIR="$SAGE_PACKAGES/build"
fi
```

(Actually, the whole `if [ ! -d ] ... fi` block can be removed).


---

Comment by drkirkby created at 2012-02-14 22:58:38

Replying to [comment:42 jhpalmieri]:
> Replying to [comment:41 jdemeyer]:
> > I ask you again: why???
> 
> It feels cleaner to me: if I set `$SAGE_BUILD_TMPDIR=/tmp`, then rather than producing many subdirectories of `tmp`, everything will live in `/tmp/build`.  It's easier to clean up by hand, and `make clean` is easier to implement this way; otherwise, I suppose it would have to delete `/tmp/atlas-3.8.4.p1/`, `/tmp/blas-...`, etc.  Or `make clean` could not modify SAGE_BUILD_TMPDIR at all, but the Make manual suggests that `make clean` (and `make distclean`) should "Also delete files in other directories if they are created by this makefile."  

John, 

how do you avoid a possible race condition if two or more instances of Sage (or some other program), want to use /tmp/build? Perhaps /tmp/$user-sage-$SageVersion.$$ might be better. Someone can then find their own Sage-related files easily (for example 


```
rm -rf /tmp/drkirkby-sage-4.5.6*
```

without risk of their being any race condition. 


Dave


---

Comment by jhpalmieri created at 2012-02-14 23:19:56

Replying to [comment:47 drkirkby]:
> Replying to [comment:42 jhpalmieri]:
> > Replying to [comment:41 jdemeyer]:
> > > I ask you again: why???
> > 
> > It feels cleaner to me: if I set `$SAGE_BUILD_TMPDIR=/tmp`, then rather than producing many subdirectories of `tmp`, everything will live in `/tmp/build`.  It's easier to clean up by hand, and `make clean` is easier to implement this way; otherwise, I suppose it would have to delete `/tmp/atlas-3.8.4.p1/`, `/tmp/blas-...`, etc.  Or `make clean` could not modify SAGE_BUILD_TMPDIR at all, but the Make manual suggests that `make clean` (and `make distclean`) should "Also delete files in other directories if they are created by this makefile."  
> 
> John, 
> 
> how do you avoid a possible race condition if two or more instances of Sage (or some other program), want to use /tmp/build? 

I don't.  If someone wants to set `$SAGE_BUILD_TMPDIR`, then I'm making it their responsibility to make sure that the directory is available and in good shape.  (If someone does `export SAGE_BUILD_TMPDIR=/tmp/sage` and then we mangle the file name somehow, I think that will lead to confusion much more often than it will help.  We could instead build in `SAGE_BUILD_TMPDIR/subdir` where we choose `subdir` to avoid race conditions.  But I'm not going to do that.)

Meanwhile, I have new versions of the patches.  I'm going to give in on the "build" subdirectory: Sage will now build in `SAGE_BUILD_TMPDIR`.  Oh, and I changed the name to `SAGE_BUILD_DIR` instead; I think that name makes more sense.  I also patched bzip2 and prereq so they build in `SAGE_BUILD_DIR` as well — easy to do now that the base repo has been merged with the root repo.  `make clean` no longer touches `SAGE_BUILD_DIR`, nor does `make distclean`.  (Also, `make clean` no longer recreates `spkg/build` or `spkg/archive` — what's that directory for, anyway?).

I updated the documentation accordingly.


---

Comment by jhpalmieri created at 2012-02-14 23:19:56

Changing status from needs_info to needs_review.


---

Comment by jhpalmieri created at 2012-02-14 23:20:28

installation guide: diff between v2 and v3


---

Attachment

sage repo: update installation guide


---

Attachment

root repo: diff between v3 and v4


---

Attachment

root repo


---

Attachment


---

Comment by jdemeyer created at 2012-02-15 08:31:21

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2012-02-15 08:31:21

Lines 210 and 216 of `sage-spkg`: you have twice cd "$SAGE_BUILD_DIR".  Remove the second and move the check (line 219) up, after the first cd.  You probably want to "exit 1" if cd fails.

Line 227 of `sage-spkg`: replace

```
if [ -e "$dir" ]; then
```

by

```
if [ -d "$dir" ]; then
```



---

Comment by jdemeyer created at 2012-02-15 09:32:33

Line 235: why "mv -f" and not simply "mv"?


---

Comment by jhpalmieri created at 2012-02-15 18:08:57

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2012-02-15 18:08:57

Replying to [comment:50 jdemeyer]:
> Lines 210 and 216 of `sage-spkg`: you have twice cd "$SAGE_BUILD_DIR".  Remove the second and move the check (line 219) up, after the first cd.  You probably want to "exit 1" if cd fails.

Well, the old version had a second 'cd' command, justified by the comment

```
# Make triply sure that we are in the build directory before doing  
# a scary "rm -rf"
```

So I left the second one in.  You think I should change this?  In any case, you're right about the "exit 1".

> Line 227 of `sage-spkg`: replace

```
if [ -e "$dir" ]; then
```

> by

```
if [ -d "$dir" ]; then
```


On the off-chance that there is a file (not a directory) in the build directory with the wrong name, shouldn't we move it, too?

Replying to [comment:51 jdemeyer]:
> Line 235: why "mv -f" and not simply "mv"?

Left over from the previous version. I can fix that.


---

Attachment


---

Attachment


---

Attachment


---

Comment by jhpalmieri created at 2012-02-15 21:11:45

The review patch looks okay to me.


---

Comment by jdemeyer created at 2012-02-16 21:20:19

Looks good to me too.


---

Comment by jdemeyer created at 2012-02-16 21:20:19

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-02-22 10:43:54

Resolution: fixed


---

Comment by jhpalmieri created at 2012-03-06 19:39:09

See #12637 for a followup.
