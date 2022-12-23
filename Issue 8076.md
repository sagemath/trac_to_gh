# Issue 8076: gap-4.4.12.p2 - please test

Issue created by migration from https://trac.sagemath.org/ticket/8076

Original creator: dimpase

Original creation time: 2010-01-26 11:54:24

Assignee: tbd

Keywords: gap

Please test [http://www1.spms.ntu.edu.sg/~dima/tmp/gap-4.4.12.p2.spkg](http://www1.spms.ntu.edu.sg/~dima/tmp/gap-4.4.12.p2.spkg), in particular on "exotic" platforms: ia64 (Itanium Linux), Intel MacOSX, Solaris(?).
So far I have done some tests on Linux x86 (stable Debian) and
PPC MacOSX.
It incorporates a long-awaited upstream GAP patches for Itanium.

It can be combined with 
[http://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.12_1.spkg](http://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.12_1.spkg) (I am updating this currently, but for the time being
it should be OK) and
[http://sage.math.washington.edu/home/wdj/patches/database_gap-4.4.12.spkg](http://sage.math.washington.edu/home/wdj/patches/database_gap-4.4.12.spkg)


---

Comment by was created at 2010-01-26 16:09:29

It builds fine, and Gap seems to work.   The major workspaces issue seems gone.    Bravo!  Thanks to Steve Linton and dimpase!

The repo needs to have its changed checked in:

```
wstein@iras:~/screen/iras/sage-4.3.1/gap-4.4.12.p2> ../sage -hg status
M .hgignore
M SPKG.txt
? patches/saveload.patch
wstein@iras:~/screen/iras/sage-4.3.1/gap-4.4.12.p2>
```


This needs an `hg ci`.

The changes to the spkg look fine.  I'm guess I'm OK with the comment "(not using the usual patches/* procedure, as this is an upstream patch.)", though I would personally never do things that way -- to me src/ should be pristine.    

I give this a positive review, subject to the other doctests in the core Sage library being fixed to reflect the new package update, e.g., things like

```
wstein@iras:~/screen/iras/sage-4.3.1> ./sage -t devel/sage/sage/interfaces/gap.py 
sage -t  "devel/sage/sage/interfaces/gap.py"                                      
**********************************************************************
File "/home/wstein/screen/iras/sage-4.3.1/devel/sage/sage/interfaces/gap.py", line 821:
    sage: gap.version()
Expected:
    '4.4.10'
Got:
    '4.4.12'
```




 -- William


---

Comment by was created at 2010-01-26 16:09:36

Changing status from new to needs_review.


---

Attachment

changing GAP version to 4.4.12


---

Comment by dimpase created at 2010-01-27 03:38:56

attached a patch to bump up version in interfaces/gap.py

updated the gap-4.4.12 spkg at the URL above to fix the repo issue (hopefully) 

Please check these. Thanks!


---

Comment by wdj created at 2010-01-27 11:15:01

Is there a patch that also fixes all the ordering issues that were discussed (the conjugacy classes, etc)?


---

Comment by dimpase created at 2010-01-31 06:25:03

working on the latter. 
Will use TESTS:: instead of EXAMPLES::, and whenever necessary, mark EXAMPLES:: as "not tested"


---

Comment by mvngu created at 2010-02-02 07:37:44

Ticket #6348 is a duplicate of this.


---

Comment by dimpase created at 2010-02-02 09:03:45

Replying to [comment:6 mvngu]:
> Ticket #6348 is a duplicate of this.
it could be, but this is a new version of the spkg's in question, that
in particular incorporated a new patch by Steve Linton and fixed the stopper problem (crashes on Linux ia64 that occured with
previous spkg vesrions)

I am about to open up a new trac ticket with a grand patch fixing the doctrings
affected.


---

Comment by dimpase created at 2010-02-02 09:12:44

Replying to [comment:4 wdj]:
> Is there a patch that also fixes all the ordering issues that were discussed (the conjugacy classes, etc)?

please see trac ticket

#8150

for this patch (at least it fixes all the -t -long sage/groups/ docstring problems)


---

Comment by dimpase created at 2010-02-05 16:30:22

Replying to [comment:4 wdj]:
> Is there a patch that also fixes all the ordering issues that were discussed (the conjugacy classes, etc)?

as #8150 is done, could you please review this ticket, too, too, to have it all set, formally speaking? Thanks!


---

Comment by wdj created at 2010-02-13 00:39:56

Tested on a mac 10.6.2 and ubuntu 9.10. 

Positive review from me too (see also William Stein's review above).


---

Comment by wdj created at 2010-02-13 00:39:56

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-13 06:30:07

Something is wrong with the package [gap-4.4.12.p2.spkg](http://www1.spms.ntu.edu.sg/~dima/tmp/gap-4.4.12.p2.spkg). First, all changes are not checked in:

```
[mvngu@sage gap-4.4.12.p2]$ hg st
M .hgignore
M SPKG.txt
```

Second, the directory `patches/` must be under revision control, so the file `.hgignore` must not contain the line `patches/`:

```
[mvngu@sage gap-4.4.12.p2]$ cat .hgignore 
src/
patches/
```

Third, I can't check anything in:

```
[mvngu@sage gap-4.4.12.p2]$ hg ci
<enter-commit-message>
abort: data/.hgignore.i@bc8f0f49e4a4: no node!
```

Am I using the correct version of the spkg to be updated?


---

Comment by dimpase created at 2010-02-13 14:10:20

Replying to [comment:12 mvngu]:

The question is which version is "right". Gap 4.4.12 was never a part of Sage,
so perhaps the proper package name is
gap-4.4.12.spkg ?

If yes, can I just wipe out .hg directory there and re-initialise hg ?

It's better to use the files located at
http://boxen.math.washington.edu/home/dima/packages/
rather than at http://www1.spms.ntu.edu.sg/~dima/tmp/
(the connection is not always stable, etc. http://boxen.math.washington.edu/home/dima/packages/
contains copies of spkg's on http://www1.spms.ntu.edu.sg/~dima/tmp/)


> Something is wrong with the package [gap-4.4.12.p2.spkg](http://www1.spms.ntu.edu.sg/~dima/tmp/gap-4.4.12.p2.spkg). First, all changes are not checked in:
> {{{
> [mvngu`@`sage gap-4.4.12.p2]$ hg st
> M .hgignore
> M SPKG.txt
> }}}
> Second, the directory `patches/` must be under revision control, so the file `.hgignore` must not contain the line `patches/`:
> {{{
> [mvngu`@`sage gap-4.4.12.p2]$ cat .hgignore 
> src/
> patches/
> }}}
> Third, I can't check anything in:
> {{{
> [mvngu`@`sage gap-4.4.12.p2]$ hg ci
> <enter-commit-message>
> abort: data/.hgignore.i`@`bc8f0f49e4a4: no node!
> }}}
> Am I using the correct version of the spkg to be updated?


---

Comment by dimpase created at 2010-02-14 07:14:32

Replying to [comment:12 mvngu]:

I have fixed the hg issues and uploaded the revised version to
[http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg)

apparently, editing .hgignore at the wrong time wreaks havoc in .hg...

> Something is wrong with the package [gap-4.4.12.p2.spkg](http://www1.spms.ntu.edu.sg/~dima/tmp/gap-4.4.12.p2.spkg). First, all changes are not checked in:
> {{{
> [mvngu`@`sage gap-4.4.12.p2]$ hg st
> M .hgignore
> M SPKG.txt
> }}}
> Second, the directory `patches/` must be under revision control, so the file `.hgignore` must not contain the line `patches/`:
> {{{
> [mvngu`@`sage gap-4.4.12.p2]$ cat .hgignore 
> src/
> patches/
> }}}
> Third, I can't check anything in:
> {{{
> [mvngu`@`sage gap-4.4.12.p2]$ hg ci
> <enter-commit-message>
> abort: data/.hgignore.i`@`bc8f0f49e4a4: no node!
> }}}
> Am I using the correct version of the spkg to be updated?


---

Comment by wdj created at 2010-02-14 12:19:04

If all you did was change the hg-related files then I don't think this needs retesting. If this is wrong, please correct me.


---

Comment by dimpase created at 2010-02-14 13:46:08

Replying to [comment:16 wdj]:
> If all you did was change the hg-related files then I don't think this needs retesting. If this is wrong, please correct me.

That's correct, I just changed the hg-related files, and updated the trac ticket descriptions. 

I changed URLs there, so now they point to the files on boxen in my
account there, rather than to anything else. But this is just administration, the code did not change. I imagine there would be more testing done when they go into a Sage pre-release, and you have already tested the updated gap_packages spkg.
(and certainly I did some testing of the updated gap spkg-file)


---

Comment by mvngu created at 2010-02-15 04:43:15

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-02-15 04:43:15

Here are some issues with the latest updated spkg:

 * It wiped out the entire commit history of all versions of the GAP spkg prior to 4.4.12.
 * The changelog `SPKG.txt` does not conform to the requirements as documented in the [Developer's Guide](http://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt).


---

Comment by mvngu created at 2010-02-15 04:45:23

What happened to `gap-4.4.12.spkg`, `gap-4.4.12.p0.spkg`, and `gap-4.4.12.p1.spkg`?


---

Comment by dimpase created at 2010-02-15 04:55:18

Replying to [comment:19 mvngu]:
> What happened to `gap-4.4.12.spkg`, `gap-4.4.12.p0.spkg`, and `gap-4.4.12.p1.spkg`?

I picked up the package made by wdj and did a bit of fixing.
None of p0, p1 ever made it to Sage.
That's why I ask whether we should really be calling it p2, and not just 
gap-4.4.12.spkg


---

Comment by dimpase created at 2010-02-15 05:52:48

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2010-02-15 05:52:48

Replying to [comment:18 mvngu]:
> Here are some issues with the latest updated spkg:
> 
>  * It wiped out the entire commit history of all versions of the GAP spkg prior to 4.4.12.

Well, the .hg/ broke down, as you have noticed.
So I wiped it out. 
Now I copied .hg/ from gap-4.4.10.p13.spkg
and merged the changes there. Please check the updated spkg file.

>  * The changelog `SPKG.txt` does not conform to the requirements as documented in the [Developer's Guide](http://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt).

Fixed. Please check the updated spkg file.


---

Comment by wdj created at 2010-02-15 12:15:04

If you have not changed the code and only the hg stuff, then I think I can leave the review to Minh, who knows mercurial much better than I do. If you changed the code so that the package needs testing, please let me know.


---

Comment by dimpase created at 2010-02-15 12:21:14

Replying to [comment:22 wdj]:
> If you have not changed the code and only the hg stuff, then I think I can leave the review to Minh, who knows mercurial much better than I do. If you changed the code so that the package needs testing, please let me know.

I changed $CP to cp, $RM to rm, etc., in spkg-install.
That was all, as far as code goes. The rest was hg stuff and documentation.


---

Comment by wdj created at 2010-02-15 20:53:23

This seems to apply fine and pass the same tests as before. at least on a mac 10.6.2. Again, I guess I leave this to Minh to give a positive review.


---

Comment by mvngu created at 2010-02-17 06:12:22

I assume that I don't need to apply [13702.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8076/13702.patch) since it's already covered by #8150.


---

Comment by dimpase created at 2010-02-17 06:27:24

Replying to [comment:25 mvngu]:
> I assume that I don't need to apply [13702.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8076/13702.patch) since it's already covered by #8150.

that's correct.


---

Comment by mvngu created at 2010-02-17 15:13:23

Someone reading the changelog of the GAP spkg would come across this snippet:

```
### gap-4.4.12.p2 (Dima Pasechnik, 2010-1-25)

 * Added .hgignore.
 *  Applied Steve Linton's Itanium patch to GAP_ROOT/src/saveload.c
   (not using the usual patches/* procedure, as this is
   an upstream patch.)
 *  Removed a stray binary file "patch" at the top level.
 *  Replaced $LN, $MKDIR, etc as done in gap-4.4.10.p13 (see below)

### gap-4.4.12.p0 (David Joyner, 2009-6-17)

Upgraded to gap-4.4.12. Removed guava compilation. From the source
GAP tarball, removed tomlib, small, prim, trans.
```

and wonder what happened to `gap-4.4.12.p1`. The updated spkg is OK by me, but I have changed its name to `gap-4.4.12.p1` and its changelog now reads:

```
### gap-4.4.12.p1 (Dima Pasechnik, 2010-1-25)
 * See ticket #8076 for full details.
 * Added .hgignore.
 * Applied Steve Linton's Itanium patch to GAP_ROOT/src/saveload.c
   (not using the usual patches/* procedure, as this is
   an upstream patch.)
 *  Removed a stray binary file "patch" at the top level.
 *  Replaced $LN, $MKDIR, etc as done in gap-4.4.10.p13 (see below)

### gap-4.4.12.p0 (David Joyner, 2009-6-17)
 * Upgraded to gap-4.4.12. Removed guava compilation. From the source
   GAP tarball, removed tomlib, small, prim, trans.
```

Remember to reference the ticket number, both in the commit message and in the changelog. The updated spkg with the above name and changelog changes is up at

http://sage.math.washington.edu/home/mvngu/spkg/standard/gap/gap-4.4.12.p1.spkg


---

Comment by mvngu created at 2010-02-17 15:13:23

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-17 20:49:35

Resolution: fixed


---

Comment by mvngu created at 2010-02-17 20:49:35

Merged [gap-4.4.12.p1.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/gap/gap-4.4.12.p1.spkg) in the standard spkg repository.
