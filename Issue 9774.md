# Issue 9774: lcalc should make a .dll file on Cygwin instead of .so file

Issue created by migration from https://trac.sagemath.org/ticket/9775

Original creator: mhansen

Original creation time: 2010-08-21 17:57:45

Assignee: tbd

CC:  rishi




---

Comment by mhansen created at 2010-08-21 18:41:42

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-08-21 18:41:42

There is an spkg at http://boxen.math.washington.edu/home/mhansen/lcalc-20100428-1.23.p3.spkg base on the one at #9592.


---

Comment by mhansen created at 2010-08-21 18:44:26

Note that #9592 should be closed or have a positive review before this one does.


---

Comment by mpatel created at 2010-08-21 20:20:44

SPKG patch of Mike's changes.


---

Attachment

There is a small type in SPKG.txt: on line 29, you should replace "lcalc-1.23.p2" by "lcalc-1.23.p3"


---

Comment by leif created at 2010-08-29 15:35:35

Replying to [comment:3 jdemeyer]:
> There is a small type in SPKG.txt: on line 29, you should replace "lcalc-1.23.p2" by "lcalc-1.23.p3"

Also in the top comment of `spkg-install`.


---

Comment by leif created at 2010-08-29 17:36:27

Some comments (on the spkg in general, not the Cygwin changes, with the exception of quoting `$SAGE_LOCAL`):

 * `$CFLAG64` and `$CXXFLAG64` should be quoted.

 * `CXXFLAG64` is exported (?) twice. (It is in fact currently used in the Makefile.)

 * In general, e.g. `-m64` should be added to `CPPFLAGS` as well.

 * In other packages, we disable optimization if `SAGE_DEBUG=yes`, and build *with* debugging symbols (`-g`) unconditionally, i.e. independent of the setting of `SAGE_DEBUG`.

 * `$MAKE` should be used instead of `make`. (Though `make` is called(!) inside the Makefile itself for the default target, `all`, which we build. See below, too.) 

 * `$SAGE_LOCAL` should be quoted, too (for future support of spaces).

 * The following case distinction is superfluous (and the branches are redundant as well):

```sh
if `test -d $SAGE_LOCAL/include/lcalc`; then
    rm -fr $SAGE_LOCAL/include/lcalc
    mkdir $SAGE_LOCAL/include/lcalc
    cp ../include/* $SAGE_LOCAL/include/lcalc
else
    mkdir $SAGE_LOCAL/include/lcalc
    cp ../include/* $SAGE_LOCAL/include/lcalc
fi
```

   It should simply be:

```sh
    rm -fr "$SAGE_LOCAL"/include/lcalc
    mkdir -p "$SAGE_LOCAL"/include/lcalc
    cp ../include/* "$SAGE_LOCAL"/include/lcalc
```


 * I'm not sure if I should like the `success()` function (the messages are quite strange); same for the use of `set -e`.

 * There's no `spkg-check`, but unfortunately the test program has been removed from the sources anyway. Should be addressed in later versions (e.g. add a comment to _"Special Update/Build Instructions"_).

 * These files have been removed without telling Mercurial:

```sh
$ hg status
! patches/lcalc-1.11-constification+solaris.patch
! patches/lcalc-1.11-gcc-4.3-build.patch
! patches/lcalc-1.11-memleak-fixes.patch
```


 * The _patched_ Makefile (`patches/Makefile.sage`, lacking the corresponding diff) isn't much better than the original.
   It also should *not* make Lcalc link against `libmpir.so` (or its static version), but - if at all - `libgmp.so` instead, since we configure MPIR with `--enable-gmpcompat` anyway. As is, it's the *only* package that breaks building with GNU MP, unless one creates a symbolic link from `libmpir.so` to `libgmp.so`.


It would be nice to address at least some (especially the last) of these points _here_, too, since it IMHO doesn't make much sense to frequently open new tickets and create new spkgs just for minor/clean-up changes.


---

Comment by mhansen created at 2010-09-01 22:37:43

I'm going to close this as a duplicate of #9845.  I'll post an spkg there which contains some changes from leif's review.


---

Comment by mhansen created at 2010-09-01 22:37:43

Resolution: duplicate


---

Comment by leif created at 2010-09-03 22:54:26

Also, the `dist/` (Debian) directory should be removed, cf. #5903.
