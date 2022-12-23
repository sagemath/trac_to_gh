# Issue 9622: Check SPKGs more vigorously for common problems

Issue created by migration from https://trac.sagemath.org/ticket/9622

Original creator: mpatel

Original creation time: 2010-07-28 08:42:37

Assignee: tbd

When we build new or updated Sage packages (spkgs), `SAGE_LOCAL/bin/sage-pkg` runs a few checks for common problems.  For example,


```sh
$ sage -pkg foo/
Creating Sage package foo/
Warning: no version number detected

Created package foo.spkg.

    NAME: foo
 VERSION:
    SIZE: 17.8M
 HG REPO: Good
SPKG.txt: Good

Please test this package using
[...]
```


But we could add several new, more detailed tests for `spkg-install`, etc.  Or put them in a `sage-spkg-{check,checker,lint}` script.


---

Comment by mpatel created at 2010-07-28 08:59:12

Possibilities, some of which could simply give warnings or reminders:

 * Check for `spkg-check` and `spkg-install` and that they're executable.
 * Check the first line of scripts for `#!/usr/bin/env` (cf. #9597).
 * Check for an unfinished Mercurial patch queue.
 * Check for the presence of `set -e`.
 * Check for the presence of $MAKE and other important variables.
 * Check for Python scripts and whether Python is a dependency in `spkg/standard/deps` (cf. #9435, #9507).

I'm sure there are others!


---

Comment by leif created at 2010-07-28 12:56:19

Yep, but two comments:

 * I wonder how many people actually use `sage-pkg` to create spkgs (rather than just use `tar`).

 * In a perfect world, the reviewer(s) would do this job (i.e. look at the code e.g., too, not just try to install a new package and then give positive review, or sometimes the other way around).

I was thinking of a good spkg template (`-install`, `-check`, `SPKG.txt`), too. And perhaps some minimalistic shell programming guide targeted at Sage scripts.


---

Comment by leif created at 2010-07-28 18:45:21

I've created a (vaguely) related ticket:

  _Update and extend "SPKG Tracking" Wiki page_, #9626.

(`sage-pkg` could spit out some reminder...)

Comments there welcome.


---

Comment by leif created at 2010-07-28 18:45:21

Changing type from defect to enhancement.


---

Comment by leif created at 2010-07-28 19:08:25

We could also formalize/code some aspects of `SPKG.txt`'s _Special Update/Build Instructions_, e.g. in (a) new (optional) script(s) like `spkg-cleanup-upstream` (deleting parts not needed by Sage, upstream repo files, etc.), contained in the spkg itself, and perhaps run automatically.

Some upstream managers also tend to copy files without preserving mtime, so we could more or less automatically check for files like `configure`, make sure they are newer than their sources, and if not, touch them before preparing the spkg.

The application of patches to the upstream source tree (i.e. currently _copying of patched files_) could also be "normalized", allowing to perform some spkg sanity checks automatically, too, and to simplify `spkg-install`s.


---

Comment by mpatel created at 2010-07-29 07:19:22

Replying to [comment:2 leif]:
>  * I wonder how many people actually use `sage-pkg` to create spkgs (rather than just use `tar`).

Good question.  I usually use `sage -spkg`, an alias of `sage -pkg`.

>  * In a perfect world, the reviewer(s) would do this job (i.e. look at the code e.g., too, not just try to install a new package and then give positive review, or sometimes the other way around).

Just a quick thought:  We could also run the spkg checks, or a subset of them, during installation.


---

Comment by drkirkby created at 2010-07-29 10:43:19

Replying to [comment:1 mpatel]:
> Possibilities, some of which could simply give warnings or reminders:
> 
>  * Check for `spkg-check` and `spkg-install` and that they're executable.

Good idea

>  * Check the first line of scripts for `#!/usr/bin/env` (cf. #9597).

Yes. 

>  * Check for an unfinished Mercurial patch queue.

Yes 

>  * Check for the presence of `set -e`.

William will not have that. He is very against the use of set -e. 

>  * Check for the presence of $MAKE and other important variables.

What's important in one package is not in another. That might be difficult to do. 

>  * Check for Python scripts and whether Python is a dependency in `spkg/standard/deps` (cf. #9435, #9507).
> 
> I'm sure there are others!

If the package is called foobar-x.y.z, then SPKG.txt should have the string foobar.x.y.z somewhere in it. Many times commits get made, with no entry in SPKG.txt

Dave


---

Comment by drkirkby created at 2010-07-29 10:47:39

One other thing, make sure all the required sections from SPKG.txt exist. i.e. none are missing. Even if there are no special build instructions, the section should exist and simply say "none". 

One could also check that entries in SPKG.txt have something in each section. But this could get a lot of work.


---

Comment by jdemeyer created at 2014-10-29 08:17:06

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-10-29 08:17:06

Close because we no longer use spkgs.


---

Comment by jdemeyer created at 2014-10-29 08:17:11

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-10-29 22:10:07

Resolution: invalid
