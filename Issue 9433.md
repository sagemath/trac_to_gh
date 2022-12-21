# Issue 9433: Put more files under revision control.

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-07-06 00:02:39

Assignee: tbd

CC:  was ddrake kcrisman leif

Put the text files in $SAGE_ROOT, and also the text files in spkg, under revision control.  (See the discussion at the end of #9351.)


---

Comment by jhpalmieri created at 2010-07-06 00:03:54

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-07-06 00:03:54

I'm marking this as "needs review", but consider this patch experimental.


---

Comment by jhpalmieri created at 2010-07-06 00:19:41

A little explanation: this patch creates a directory "other-scripts" in SAGE_ROOT/local/bin.  This new directory contains a brief README.txt and also subdirectories "root" and "spkg".  "root" contains the text files from SAGE_ROOT.  The only one with any changes is README.txt which explains how these files are under revision control.  Similarly, "spkg" contains various text files from SAGE_ROOT/spkg, and the only one with any changes is README.txt.


---

Comment by jhpalmieri created at 2010-07-06 03:27:14

This probably needs to be rebased.  When people are ready to look at it, let me know and I'll see what I can do.


---

Comment by jhpalmieri created at 2010-07-08 15:46:52

rebased against 4.5.alpha4 + #9456


---

Attachment

New approach, after a [discussion on sage-devel](http://groups.google.com/group/sage-devel/t/3ba410046ae641f8): create a new repo at the top level tracking the appropriate files.  I'm attaching a new version of the patch for the scripts repo.  Someone -- the release manager, I guess -- also needs to create the top level repo, because I don't know how to do this in such a way that it can be posted on a ticket.  Here are the instructions:

 - move the attached file "hgignore" to SAGE_ROOT/.hgignore
 - cd $SAGE_ROOT
 - hg init .
 - hg add .hgignore COPYING.txt README.txt makefile sage sage-python
 - cd spkg
 - hg add README.txt gen_html install pipestatus 
 - cd standard
 - hg add README.txt deps libdist_filelist newest_version
 - hg add notes.txt numeric-24.2.txt

(I don't know if we really need these last two files, but this is probably not the ticket for making such decisions.)  Finally, do

 - hg commit

When you run "sage -sdist ..." it should add a tag for the new version of Sage.

This does not create a new spkg for the files in SAGE_ROOT, since those files have to be in place when you unpack the sage tar file.  But it creates the repository so that people can post patches to the trac server, etc.


---

Comment by was created at 2010-07-08 22:25:13

Looking with my eyes, this looks good.  I don't have time to test right now.  The test would be to take a clean Sage, do the above, then do "sage -sdist ..." and make sure that in the sdist the above is all still there.


---

Comment by jhpalmieri created at 2010-07-09 00:43:54

main repo: add "hg_root" command to Sage


---

Attachment

Replying to [comment:5 was]:
> The test would be to take a clean Sage, do the above, then do "sage -sdist ..." and make sure that in the sdist the above is all still there. 

This works for me, but other people should definitely look at it carefully.


---

Comment by jhpalmieri created at 2010-07-22 04:14:06

This probably needs work: how will it work with "sage -upgrade"?


---

Comment by jhpalmieri created at 2010-07-26 20:47:51

Here's a new version of the patch for the scripts repo.  I think this should deal with upgrading: the script "sage-upgrade" now runs "sage --hg branch" from SAGE_ROOT, and if this fails, it assumes that there is no Mercurial repository and creates it.


---

Comment by jhpalmieri created at 2010-07-27 14:49:36

This may need to be changed if #9609 is merged: the directions here, and also the modified "sage-upgrade" script, refer to files which would be deleted by #9609.


---

Comment by jhpalmieri created at 2010-07-28 02:25:03

New version, rebased against #9609.


---

Comment by ddrake created at 2010-07-28 06:24:24

In sage-sdist, where you have `# copy sage root repo over`, why not just clone the repo? That will take care of copying all the necessary files, and if we add or remove files tracked by the repo, we won't need to mess with sage-sdist. I'm thinking that something like

```
cd $SAGE_ROOT 
hg clone --pull . DEST_DIR
```

Using --pull means that it doesn't use hardlinks in the clone; I *think* there would be no problem with using hardlinks, but it's unlikely to make a big difference. The clone will include a hgrc file that points to where it came from: it would look something like this:

```
[paths]
default = /home/foo/sage-whatever
```

We could simply delete the file, or just leave it, since it would not negatively affect anything (except running `hg pull` from SAGE_ROOT, which you wouldn't do anyway).

So, all the `cp -p` lines could be just

```
hg clone --pull . $TMP
rm $TMP/.hg/hgrc
```

and files added or removed to the repo would get copied correctly without changing any scripts.


---

Comment by jhpalmieri created at 2010-07-28 15:05:28

new version, using "hg clone". apply to scripts repo.


---

Attachment

new version, using "hg clone". apply to scripts repo.


---

Attachment

Note that if you use "hg clone ..." to copy the repo, you have to do it earlier in the process: it apparently needs to be done with an empty directory, so in sage-sdist it is now done right after creating $TMP.


---

Comment by mpatel created at 2010-08-07 06:18:27

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2010-08-07 06:18:27

If I

 * Build the forthcoming Sage 4.5.2 (which is just 4.5.2.rc1 + #9226) from source.
 * Follow the steps in the description.
 * `./sage -sdist 4.5.99`

`hg log` in the "root" repo now gives

```
changeset:   1:0fea58e94942
tag:         tip
user:        Mitesh Patel <qed777`@`gmail.com>
date:        Fri Aug 06 21:40:23 2010 -0700
summary:     Added tag 4.5.99 for changeset 4c1f4320f743

changeset:   0:4c1f4320f743
tag:         4.5.99
user:        Mitesh Patel <qed777`@`gmail.com>
date:        Fri Aug 06 21:33:45 2010 -0700
summary:     Initial Sage "root" repository
```


The new 4.5.99 builds successfully from source and passes the long doctests.  But `hg log` in the root repo for 4.5.99 lists just revision 0, and the root repo is missing from a binary distribution made with `./sage -bdist 4.5.99`.


---

Comment by mpatel created at 2010-08-07 07:13:00

I also noticed

 * `SAGE_ROOT/ipython` and `SAGE_ROOT/sage-README-osx.txt` are missing from the new source and binary distributions.
 * An extra `SAGE_ROOT/sage-python` after unpacking `sage-4.5.99.tar`.


---

Comment by jhpalmieri created at 2010-08-08 22:38:42

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-08-08 22:38:42

Replying to [comment:15 mpatel]:
> The new 4.5.99 builds successfully from source and passes the long doctests.  But `hg log` in the root repo for 4.5.99 lists just revision 0, and the root repo is missing from a binary distribution made with `./sage -bdist 4.5.99`.

Right, I didn't do this right.  In the new patch, the root repo is not modified at all by sage-make_devel_packages; instead, sage-sdist clones it, tags it, and commits the new tag, while sage-bdist just clones it.

> I also noticed
>
>  * SAGE_ROOT/ipython and SAGE_ROOT/sage-README-osx.txt are missing from the new source and binary distributions.

The missing ipython directory was an oversight.  I think I've fixed it.  The missing sage-README-osx.txt was intentional: this should only be included for binary distributions on OS X, and its presence there is taken care of by sage-bdist:

```
if [ "$UNAME" = "Darwin" ]; then
    ...
    cp sage/local/bin/sage-README-osx.txt README.txt
    ...
```

Perhaps we can close #6938 if this gets merged?

>  * An extra SAGE_ROOT/sage-python after unpacking sage-4.5.99.tar.

This was intentional.  Before this, the file sage-python was stored in the scripts repo and then unpacked to the top level.  I'm not sure why this was done, but I wanted to keep the end result as close as possible to what it was before.


---

Comment by kcrisman created at 2010-08-09 13:03:12

> > I also noticed
> >
> >  * SAGE_ROOT/ipython and SAGE_ROOT/sage-README-osx.txt are missing from the new source and binary distributions.
> 
> The missing ipython directory was an oversight.  I think I've fixed it.  The missing sage-README-osx.txt was intentional: this should only be included for binary distributions on OS X, and its presence there is taken care of by sage-bdist:
> {{{
> if [ "$UNAME" = "Darwin" ]; then
>     ...
>     cp sage/local/bin/sage-README-osx.txt README.txt
>     ...
> }}}
> Perhaps we can close #6938 if this gets merged?

As one of the people involved on that ticket, that is fine. The problem is that #6938 does not currently have positive review! So I think that would be necessary first, or something else indicating that the solution proposed there is correct. Maybe 'merge' that ticket at the same time as this one, for whatever it's worth.

Sounds like you agree :) In fact, notice that once that is removed, that file will only appear ABOVE the SAGE_ROOT directory, in the place a normal README would occur in a dmg or bundle, so it does work properly (I've tested this numerous times


---

Comment by jhpalmieri created at 2010-08-09 14:33:18

I realized there was another problem with the previous patch: while it would work when upgrading from a Sage build with no root repo, it wouldn't do anything when upgrading a Sage build with an existing root repo.  The new patch constructs a sage_root spkg file, but this file only gets used during upgrading.  So it is installed in the script "sage-upgrade", but it does not appear in spkg/standard/deps.


---

Comment by jhpalmieri created at 2010-08-10 02:57:08

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-08-10 02:57:08

This still doesn't deal with upgrading very well.  I need to think about how to do this and work on it for a while in a place where I have a better internet connection.  I may have something in a few days.  Meanwhile, if anyone has suggestions for how to deal with upgrades, I would like to hear them.  The issues:

 - currently, I don't even know what happens with "sage -upgrade ..." if SAGE_ROOT/makefile is changed, for example.  Does anything happen?

 - does it matter whether we install the new sage_root spkg before or after the sage_scripts spkg?  The patch here affects the sage-upgrade script, but the new version won't get run during an upgrade anyway.

 - is it good enough to just install the new sage_root spkg?  I think it might be, but I might be confused.  Anyway, I think I need time to play with it and test it out.


---

Comment by jhpalmieri created at 2010-08-11 19:31:26

This seems to work for me, with one slight glitch: if I run "sage -upgrade" on a copy of sage which does not yet include the root repo, it lists the spkg's to be upgraded and asks me "do you really want to continue", then it does some stuff, and then it lists just the root_repo spkg and asks me again if I want to continue.  The issue is that, before it has installed some of the upgraded packages, it doesn't know what to do with the root_repo spkg, so it doesn't get installed the first time through.  I don't see any way around this, but it's a one-time problem.


---

Comment by jhpalmieri created at 2010-08-11 19:31:26

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-09-13 08:02:46

Ooops, I once had been aware of this ticket, but forgot to cc me...

Before doing this, can we rename `makefile` to `Makefile`?


---

Comment by jhpalmieri created at 2010-09-13 18:11:42

> Before doing this, can we rename makefile to Makefile?

I have no problems with that.  Are there ever any (good) reasons for using `makefile` instead of `Makefile`?


---

Comment by leif created at 2010-09-13 19:17:01

Should `sage-README-osx.txt` be ignored (i.e. *not* be under revision control)?

Also a candidate for renaming (`README.MacOS_X.txt` or alike).

From the attached `hg_script`:

```sh
...
$hg add .hgignore .hgtags COPYING.txt README.txt makefile sage sage-python
cd ipython
$hg add *.py ipythonrc*
...
```


`sage-python` and `ipython/` should IMHO be in `.hgignore`, since these are not in `$SAGE_ROOT` until Sage is built.


---

Comment by jhpalmieri created at 2010-09-13 19:53:13

Replying to [comment:25 leif]:
> Should `sage-README-osx.txt` be ignored (i.e. *not* be under revision control)?

It shouldn't be present at all, and with the patches here, it isn't.  See #6938 and also [my comment above](http://trac.sagemath.org/sage_trac/ticket/9433?replyto=25#comment:17).  (It should only appear in the *parent* directory of SAGE_ROOT when you make a dmg file on a Mac.)

> `sage-python` and `ipython/` should IMHO be in `.hgignore`, since these are not in `$SAGE_ROOT` until Sage is built.

This is another change on this ticket: these files are now tracked in this repo, not in sage_scripts anymore.  Actually, I don't know if ipython was tracked anywhere, but now it is.  I don't know who chose to include sage-python in the top-level directory, but since it's there, it should be tracked properly.  (It's a simple enough script I don't mind having two copies of it.)  I personally don't see the point of it and think it should be removed, but that should probably happen on another ticket.  Or maybe it should be a link to local/bin/sage-python?


---

Comment by kcrisman created at 2010-09-13 20:20:53

Replying to [comment:26 jhpalmieri]:
> Replying to [comment:25 leif]:
> > Should `sage-README-osx.txt` be ignored (i.e. *not* be under revision control)?
> 
> It shouldn't be present at all, and with the patches here, it isn't.  See #6938 and also [my comment above](http://trac.sagemath.org/sage_trac/ticket/9433?replyto=25#comment:17).  (It should only appear in the *parent* directory of SAGE_ROOT when you make a dmg file on a Mac.)

Correct.


---

Comment by leif created at 2010-09-13 20:27:37

Replying to [comment:26 jhpalmieri]:
> Replying to [comment:25 leif]:
> > Should `sage-README-osx.txt` be ignored (i.e. *not* be under revision control)?
> 
> It shouldn't be present at all, and with the patches here, it isn't.  See #6938 and also [my comment above](http://trac.sagemath.org/sage_trac/ticket/9433?replyto=25#comment:17).  (It should only appear in the *parent* directory of SAGE_ROOT when you make a dmg file on a Mac.)

Missed that.

> > `sage-python` and `ipython/` should IMHO be in `.hgignore`, since these are not in `$SAGE_ROOT` until Sage is built.
> 
> This is another change on this ticket: these files are now tracked in this repo, not in sage_scripts anymore.

That, too... :/

> Actually, I don't know if ipython was tracked anywhere, but now it is.  I don't know who chose to include sage-python in the top-level directory, but since it's there, it should be tracked properly.  (It's a simple enough script I don't mind having two copies of it.)  I personally don't see the point of it and think it should be removed, but that should probably happen on another ticket.  Or maybe it should be a link to local/bin/sage-python?

Perhaps...

Sorry for the noise.


---

Comment by leif created at 2010-09-16 12:34:36

I'd also like to have a `VERSION.txt` in `SAGE_ROOT/`, best containing just the "plain" version number (perhaps only with also the release date added); cf. #9434 (the number is a coincidence!).

What about release notes (in the top-level directory)?


---

Comment by kcrisman created at 2010-09-16 13:09:28

Replying to [comment:29 leif]:
> I'd also like to have a `VERSION.txt` in `SAGE_ROOT/`, best containing just the "plain" version number (perhaps only with also the release date added); cf. #9434 (the number is a coincidence!).
That's a good idea.  Be sure not to hold this one up too long ;)
> What about release notes (in the top-level directory)?
That definitely used to be in this directory, filename `HISTORY.txt`.  Maybe it was getting long?  It certainly got out of date quickly.  It might be an onus on the release manager to create the notes *before* the release is made, though - usually that takes a little time, and then it somehow gets added to the official version at sagemath.org (and a few other places?).  The problem is that this isn't fully automated yet.


---

Comment by leif created at 2010-09-16 13:32:02

Replying to [comment:30 kcrisman]:
> Replying to [comment:29 leif]:
> > I'd also like to have a `VERSION.txt` in `SAGE_ROOT/`, best containing just the "plain" version number (perhaps only with also the release date added); cf. #9434 (the number is a coincidence!).
> That's a good idea.  Be sure not to hold this one up too long ;)

I don't think adding this needs great effort... We already have `devel/sage/sage/version.py`, which looks like this:

```python
"""nodoctests"""
version='4.6.alpha1'; date='2010-09-15'
```


> > What about release notes (in the top-level directory)?
> That definitely used to be in this directory, filename `HISTORY.txt`.  Maybe it was getting long?  It certainly got out of date quickly.  It might be an onus on the release manager to create the notes *before* the release is made, though

Doesn't have to be under revision control (i.e. could be in `.hgignore`); it IMHO shouldn't be too lengthy, perhaps just contain the most recent changes (e.g. tickets merged since last final, with a reference to a complete version elsewhere).

> - usually that takes a little time, and then it somehow gets added to the official version at sagemath.org (and a few other places?).  The problem is that this isn't fully automated yet.

I think the release notes as in the announcements are meanwhile fully automatically generated by a script. I just wonder if these are really "human"-(means user-)readable, if we intend that.


---

Comment by kcrisman created at 2010-09-16 13:42:08

Those ideas seem reasonable, but probably I'm not the one to make the call, since I'm not doing the work.

> > - usually that takes a little time, and then it somehow gets added to the official version at sagemath.org (and a few other places?).  The problem is that this isn't fully automated yet.
> 
> I think the release notes as in the announcements are meanwhile fully automatically generated by a script. I just wonder if these are really "human"-(means user-)readable, if we intend that.

The hard part is, but at least in theory the "known issues" and "new features" sections and things like that are supposed to be human-generated.  mvngu used to make great categorized ones, but likely hasn't had the time lately.  I think they are more human-readable than some I've seen in other programs, though :)


---

Comment by jhpalmieri created at 2010-09-16 15:18:40

I think that for release notes, we could just have a document which says something like "Please see http://sagemath.org/mirror/src/changelogs/sage-$VERSION.txt for a list of recent changes."  Or we could use the link "http://sagemath.org/mirror/src/changelogs/" and then we wouldn't have to update it.  This also provides easy access to older changelogs (which the $VERSION.txt doesn't, and notice it's just a text file -- no links to the parent directory or older changelogs).  Opinions?  We could also add the link "http://wiki.sagemath.org/ReleaseTours/", although this hasn't been updated in a while.

I like the generic option better.  But notice that this file won't be auto-generated by "sage -sdist" or any other script, and it should probably be under revision control.  This is not the right ticket for adding new files to the top directory, or for modifying existing files, so I think this should go elsewhere.

I also agree that a VERSION.txt file is a good idea.  Since we can automatically generate this, and since it shouldn't be under revision control, I think we can do it on this ticket.  It should just require modifying sage-sdist and sage-bdist.  I'll try towork on this some time soon.


---

Comment by leif created at 2010-09-16 15:34:07

As a first step, just add `VERSION.txt` to `.hgignore` (here). ;-)

My intention (perhaps as a developer) regarding "release notes" (whatever the file is called) also was _not_ to have to search trac or some web page(s) (or query Mercurial) just to see which tickets have recently been merged...

For users, of course a more abstract description would be better (bugs fixed, packages newly included or upgraded, new features etc.)


---

Comment by jhpalmieri created at 2010-09-16 21:00:50

I've opened up #9922 for adding release notes.  For VERSION.txt, I think we (meaning me) should do the whole thing on this ticket: add it to `.hgignore`, create it in `sage-sdist`, and make sure it gets copied by `sage-bdist`, or else the whole thing should go on another ticket.  If I don't get to it on this one, then I'll open a ticket describing the steps (including adding it to `.hgignore`) -- I don't really see the point in doing one piece of it here.


---

Comment by mpatel created at 2010-09-16 22:09:15

Should we update `VERSION.txt` after successful upgrades?  Or maybe have separate fields for the original version (and whether it was a binary) and the current version?  Or even keep a brief upgrade history?


---

Comment by jhpalmieri created at 2010-09-17 01:13:58

I've attached a new version of hg_script which rename 'makefile' to 'Makefile' if it hasn't already been done.  (I thought I also had to modify root-spkg-install, but I don't think I do: once the repo has been made via hg_script, it will have 'Makefile' in it, not 'makefile'.)

I also think mpatel has a good point about VERSION.txt.  I think there are possible design decisions to be made about how to create that file, what should go in it, how to modify it, etc., so I think it should go another ticket.  It could piggy-back on #9922, I think.  I'm going to change the description of that ticket to include this.


---

Comment by ddrake created at 2010-09-17 03:42:50

Regarding all this VERSION.txt stuff, I think we should stay on task here. This ticket is about putting existing files under version control. Adding new files "while we're at it" is, IMHO, an unnecessary distraction.

Once SAGE_ROOT is in a Mercurial repo, we can add new files by just creating a ticket, attaching a patch, and getting a positive review. Let's get that repo there first!


---

Comment by jhpalmieri created at 2010-09-24 17:13:20

fixes problems found by mpatel. apply to scripts repo


---

Attachment


---

Comment by leif created at 2010-09-24 17:54:47

A lot of environment variables should be quoted (`$SAGE_ROOT`, `$TMP`, `$OPT` etc. in most commands).

Needs rebasing in case #9896 gets merged... (or the other way around)


---

Comment by leif created at 2010-09-24 18:03:29

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-09-24 18:03:29

`root-spkg-install` also needs work:

```sh
...
    if [ -e makefile ]; then
        cp makefile "$TARGET"/Makefile
    else
        cp Makefile "$TARGET"
    fi
    if [ ! -d "$TARGET/skpg" ]; then
        mkdir "$TARGET/spkg"
    fi
    if [ ! -d "$TARGET/skpg/standard" ]; then
        mkdir "$TARGET/spkg/standard"
...
```

We'd better use `-f` than `-e`, `s/skpg/spkg/g`.


---

Comment by leif created at 2010-09-24 18:07:27

P.S.: Instead of

```sh
if [ ! -d foo ]; then
    mkdir foo
fi
```

you can simply do

```sh
mkdir -p foo
```



---

Comment by jhpalmieri created at 2010-09-24 18:38:27

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-09-24 18:38:27

Okay, I've fixed root-spkg-install, although I could probably just have one line

```
mkdir -p "$TARGET/spkg/standard"
```

instead of two

```
mkdir -p "$TARGET/spkg"
mkdir -p "$TARGET/spkg/standard"
```

I've also quoted every variable in sight in the scripts patch.


---

Comment by leif created at 2010-09-24 19:28:05

Okay, `test -e` shouldn't be a problem with `bash`, only (despite being POSIX) with some Solaris' `/bin/sh`.


---

Comment by leif created at 2010-09-24 19:51:24

You don't have to quote variable expansions in normal assignments like `foo=$BAR` or `echo`s, but never mind.

Also, `test -d foo` is superfluous if you `rm -rf foo`. ("force" also implies not raising an error if the directory doesn't exist.)

I'll have to take a closer look regarding (quoting) `$OPT`; this might be wrong in some cases.


---

Comment by leif created at 2010-09-24 20:13:06

There are some quotes missing at the end of `sage-make_devel_packages` (in the newly included part.)

Quoting `$OPT` *currently* works, since it is

```sh
OPT="pPR"
```

but it is a bad idea to omit the dash(es) in `OPT` and prepend it to the expansion.

I.e., it should be

```sh
OPT="-pPR"

...

cp $OPT ... # NOT quoted

...

cp -L $OPT ... # also NOT quoted
```


And I'd suggest renaming `OPT` to `CP_OPTS`.


---

Comment by jhpalmieri created at 2010-09-24 21:54:17

> There are some quotes missing at the end of sage-make_devel_packages (in the newly included part.)

Oops, I don't know how I missed those.  Anyway, here are new versions.  This changes "OPT" to "CP_OPT" and includes the hyphen.


---

Comment by jhpalmieri created at 2010-09-24 22:20:28

I'm attaching new versions of `root-spkg-install` and `hg_script` which omit the file `SAGE_ROOT/sage-python`.  I asked about this [on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/13b4632773e3122c#) and no one demanded that it be kept.


---

Attachment

script to initialize repository. for use by the release manager.


---

Attachment

the file SAGE_ROOT/spkg/root-spkg-install


---

Comment by leif created at 2010-09-25 01:03:14

Ok, except that `hg_script` won't work if `$SAGE_ROOT` contains spaces, and "sage" should be "Sage" in the messages, the patches and attached files now look fine (with the one exception below).

In my opinion more exit codes should be checked (of `hg`, `tar` and `python`), but most of these omissions have been in before, so it is at least "consistent". ;-) (And some `tar` operations are verbose, while others are not. I also think the release date should be UTC or at least contain the [time and] time zone / UTC offset.)

But `sage-upgrade` should in any case check that

```sh
./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a $SAGE_ROOT/spkg/logs/$ROOT_REPO.log"
```

worked before calling `./install`.

I also wonder if this shouldn't (yet) be

```sh
./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a \"$SAGE_ROOT\"/spkg/logs/$ROOT_REPO.log"
```

(Not tested; the side effects of `pipestatus` are quite weird.)

I haven't yet applied the patches or fully checked the functionality; at least I didn't find errors in the latest attachments. :)

Btw, why aren't base packages subject to upgrading? (I would have expected the root spkg there.)


---

Comment by leif created at 2010-09-25 01:14:37

Replying to [comment:49 leif]:
> I also wonder if this shouldn't (yet) be

```sh
./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a \"$SAGE_ROOT\"/spkg/logs/$ROOT_REPO.log"
```

(Not tested; the side effects of `pipestatus` are quite weird.)

The above doesn't work; it should be

```sh
./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a $$SAGE_ROOT/spkg/logs/$ROOT_REPO.log"
```

(since `SAGE_ROOT` is in the environment anyway).


---

Comment by leif created at 2010-09-25 01:17:40

Ouch. Forget my last comment... (i.e. the "solution") :D


---

Comment by leif created at 2010-09-25 01:32:40

Finally :) it should be:

```sh
./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a '$SAGE_ROOT'/spkg/logs/$ROOT_REPO.log"
```



---

Comment by jhpalmieri created at 2010-09-25 01:33:30

Replying to [comment:49 leif]:
> Ok, except that `hg_script` won't work if `$SAGE_ROOT` contains spaces, 

Since this script only gets run once, by the release manager when this ticket is merged, and since it doesn't get distributed with Sage, I'm not going to worry about it.  When Sage works with spaces in the path, if this hasn't been merged yet, I can fix it then.

> and "sage" should be "Sage" in the messages, 

I'll fix that.  You mean messages like "Error building the sage source code package" or  "Error copying sage root repository", right?

> In my opinion more exit codes should be checked (of `hg`, `tar` and `python`), but most of these omissions have been in before, so it is at least "consistent". ;-) (And some `tar` operations are verbose, while others are not. I also think the release date should be UTC or at least contain the [time and] time zone / UTC offset.)
> 
> But `sage-upgrade` should in any case check that

```sh
./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a $SAGE_ROOT/spkg/logs/$ROOT_REPO.log"
```

> worked before calling `./install`.

You're right, I thought about this before, but didn't do it.

> Btw, why aren't base packages subject to upgrading? (I would have expected the root spkg there.)

I'm not sure what you mean by "base packages".  The `sage-upgrade` script will certainly upgrade the sage-root spkg. Let's see, the sage-update script will download any new spkg, including any sage-root spkg. Then it gets installed in sage-upgrade before the other spkgs, in case it changes deps or spkg/install.

Should I create an upgrade path on sage.math?  I may wait a day or two for the disk situation to settle down...

Re the "pipestatus" command, I'm going to leave it as is and see what happens during testing.  (When I tested a month ago or so, the sage-root spkg got upgraded, and I vaguely remember checking that the log file had the right name, but I'll test again.)


---

Comment by leif created at 2010-09-25 01:50:52

Replying to [comment:53 jhpalmieri]:
> Replying to [comment:49 leif]:
> > Ok, except that `hg_script` won't work if `$SAGE_ROOT` contains spaces, 
> 
> Since this script only gets run once, by the release manager when this ticket is merged, and since it doesn't get distributed with Sage, I'm not going to worry about it.

Yes, this is (and was meant) a non-issue, I only mentioned it for completeness. ;-)

> > and "sage" should be "Sage" in the messages, 
> 
> I'll fix that.  You mean messages like "Error building the sage source code package" or  "Error copying sage root repository", right?

Yes.

> > Btw, why aren't base packages subject to upgrading? (I would have expected the root spkg there.)
> 
> I'm not sure what you mean by "base packages".

The packages /files in `spkg/base`, also referred to by `$(BASE)` in the Makefile (`deps`).

> The `sage-upgrade` script will certainly upgrade the sage-root spkg.

Yes, of course. (`sage-update` currently doesn't attempt to upgrade anything from `spkg/base`.)

> Should I create an upgrade path on sage.math?  I may wait a day or two for the disk situation to settle down...

I have no opinion on that.
 
> Re the "pipestatus" command, I'm going to leave it as is and see what happens during testing.  (When I tested a month ago or so, the sage-root spkg got upgraded, and I vaguely remember checking that the log file had the right name, but I'll test again.)

This again just referred to _spaces in SAGE_ROOT_. (My last suggestions would work with such.)


---

Comment by jhpalmieri created at 2010-09-25 02:17:32

apply to scripts repo


---

Attachment

for reference only: diff between v2 and v3 patches.


---

Attachment

Here are new versions; the only difference with any content (i.e., other than capitalization, I think) is from sage-upgrade:

```diff
-./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a $SAGE_ROOT/spkg/logs/$ROOT_REPO.log"
+./pipestatus "sage-spkg $ROOT_REPO 2>&1" "tee -a '$SAGE_ROOT'/spkg/logs/$ROOT_REPO.log"
+
+if [ $? -ne 0 ]; then
+    echo "Error installing Sage root repository."
+    exit 1
+fi
```


I don't know why base packages don't get upgraded.  That's for another ticket.

> Should I create an upgrade path on sage.math?

I meant so that people could test "sage -upgrade".   I'll do this pretty soon.


---

Attachment

rebased for 4.6.1.alpha0


---

Attachment

rebased for 4.6.1.alpha0


---

Comment by ddrake created at 2010-11-05 11:28:59

I rebased the above two patches. The main Sage repo one is fine, but the scripts patch had rejects on some huge hunks and it took a while to manually put them in. Someone should check over the "-rebased" patch and make sure I did everything correctly.


---

Comment by jhpalmieri created at 2010-11-05 17:51:21

Hi Dan,

Thanks for working on this.  The Sage repo patch looks good.  Skimming the scripts patch, the only issue I see with the rebasing is that I think $PKGDIR should be quoted in the following (this is lines 39-41 in sage-sdist):

```
cp "$SAGE_ROOT"/local/bin/sage-spkg $PKGDIR/base/ 
cp "$SAGE_ROOT"/local/bin/sage-env  $PKGDIR/base/ 
cp "$SAGE_ROOT"/local/bin/sage-make_relative $PKGDIR/base/ 
```

I'll look at this more carefully when I have time.


---

Comment by jhpalmieri created at 2010-11-05 21:52:47

I also found the following corrections to be added to the part of the patch for sage-bdist:

```diff
diff -r fa7bc24587ef sage-bdist
--- a/sage-bdist	Fri Sep 24 19:13:24 2010 -0700
+++ b/sage-bdist	Fri Nov 05 14:45:36 2010 -0700
`@``@` -46,16 +46,15 `@``@`
 if [ $? -ne 0 ]; then
     echo "Error copying Sage root repository."
     exit 1
+fi
 
 rm "$TMP"/.hg/hgrc
 echo "Done copying root repository."
 
-mkdir "$TMP"
-
 cd "$SAGE_ROOT"
 
 echo "Copying files over to tmp directory"
-cp -$CP_OPT examples local data "$TMP"/
+cp $CP_OPT examples local data "$TMP"/
 
 if [ -d devel/sage-main ]; then
    echo "Copying Sage library over"
`@``@` -63,7 +62,6 `@``@`
    cp -L $CP_OPT devel/sagenb-main "$TMP"/devel/sagenb-main
    cp -L $CP_OPT devel/sage-main "$TMP"/devel/sage-main
    cd "$TMP"/devel
-   cd $TMP/devel
    ln -s sage-main sage
    ln -s sagenb-main sagenb
    cd sage
```

I'm posting a "v4" patch including this and the above change in sage-sdist (quoting "$PKGDIR").


---

Attachment

rebased for 4.6.1.alpha0


---

Comment by ddrake created at 2010-11-05 22:16:22

I used my rebased patches and 4.6.1.alpha0 to initialize the root repo; I sdisted that and the resulting thing has the correct root repo and built fine -- so everything here seems to work "going forward"; I haven't tested any upgrading yet.


---

Comment by jhpalmieri created at 2010-11-05 22:28:26

I'm working on providing an upgrade path (or two) for testing.  I'll post here when I have links.


---

Comment by jhpalmieri created at 2010-11-06 00:06:51

Okay for testing upgrading:

```
./sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha0/
```

This first upgrade path is just a vanilla version of 4.6.1.alpha0, plus the new root repo.

```
./sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha1/
```

The second upgrade path contains everything from the first one, plus a change to the top-level README.txt file.  This is so we can test upgrading to a plain root repo, then from there to a modified version.  So upgrading to "...9433.alpha0" followed by "...9433.alpha1" should work, as well as just upgrading straight to "...9433.alpha1".

I think that if you upgrade from a version with a Sage root repo to either of these, you may be asked twice if you want to upgrade.  I mentioned this issue [above](http://trac.sagemath.org/sage_trac/ticket/9433#comment:22).


---

Comment by jhpalmieri created at 2010-11-06 03:49:34

One issue: if you upgrade a version of Sage containing "makefile", then you end up with both "makefile" and "Makefile" when you're done.  We can just delete "$SAGE_ROOT/makefile" when running the root-spkg-install file.  That's easy enough to do; is it the right solution?


---

Comment by leif created at 2010-11-06 04:04:35

Hmmm, this doesn't work for upgrades from older versions (<=4.5), and as you mentioned, behaves strange on newer versions >=4.5.1.

We *have to* download `spkg/install` (and I'd prefer the rest, too) in `sage-update` (the Python script).

What's currently newly made in `sage-upgrade` should be moved to that file, which is in any case the fresh, downloaded one. _There_ we have to make a distinction on if we are upgrading.

If so, `spkg/install` should then install the root repo (preferably without overwriting itself, but the root repo should, i.e. must, contain exactly the same file), since our "real" Makefile `spkg/standard/deps` doesn't (though I don't know why you don't want to put the root spkg there).

Btw, it would be better to also have `sage-spkg` in the root rather than the scripts repo; or download an identical copy (from the scripts repo) along with `install`, `deps` etc.

This way we would always do the whole build with the new one, and not switch the version during the installation (after the new scripts spkg has been installed).

Another reason to keep the repos separate, and not as Robert B. suggested on sage-devel, merge them all into an even larger, monolithic one.

(To avoid trouble with getting overwritten, a script can always clone itself and then `exec` this copy, passing it a parameter such that it knows if it's the clone or the original, similar to `fork()`. We should IMHO do this for a few scripts involved in upgrading and the build process. Therefore, the chain or stack of called rather than `exec`'ed scripts shouldn't be deep.)


---

Comment by leif created at 2010-11-06 04:06:08

Replying to [comment:63 jhpalmieri]:
> One issue: if you upgrade a version of Sage containing "makefile", then you end up with both "makefile" and "Makefile" when you're done.  We can just delete "$SAGE_ROOT/makefile" when running the root-spkg-install file.  That's easy enough to do; is it the right solution?

Rename it to `Makefile.old`?


---

Comment by leif created at 2010-11-06 04:09:07

Replying to [comment:62 jhpalmieri]:
> I think that if you upgrade from a version with a Sage root repo to either of these, you may be asked twice if you want to upgrade.  I mentioned this issue [above](http://trac.sagemath.org/sage_trac/ticket/9433#comment:22).

According to the comment you refer to, this should read _"upgrade from a version *without* a Sage root repo"_.


---

Comment by jhpalmieri created at 2010-11-06 06:11:03

Replying to [comment:64 leif]:
> We *have to* download `spkg/install` (and I'd prefer the rest, too) in `sage-update` (the Python script).

I'm not sure what "the rest" refers to here.

> What's currently newly made in `sage-upgrade` should be moved to that file, which is in any case the fresh, downloaded one. _There_ we have to make a distinction on if we are upgrading.

Okay, I think I can do that.

> If so, `spkg/install` should then install the root repo (preferably without overwriting itself, but the root repo should, i.e. must, contain exactly the same file), since our "real" Makefile `spkg/standard/deps` doesn't (though I don't know why you don't want to put the root spkg there).

I don't want to put it there because in a non-upgrade, it's already installed as part of the download. 
 
> Btw, it would be better to also have `sage-spkg` in the root rather than the scripts repo; or download an identical copy (from the scripts repo) along with `install`, `deps` etc.

That's not a bad idea, but it should go on another ticket.  What about the other scripts in spkg/base, for example sage-env?


Replying to [comment:65 leif]:
> Replying to [comment:63 jhpalmieri]:
> > One issue: if you upgrade a version of Sage containing "makefile", then you end up with both "makefile" and "Makefile" when you're done.  We can just delete "$SAGE_ROOT/makefile" when running the root-spkg-install file.  That's easy enough to do; is it the right solution?
> 
> Rename it to `Makefile.old`?

That sounds good to me. 

Replying to [comment:66 leif]:
> Replying to [comment:62 jhpalmieri]:
> > I think that if you upgrade from a version with a Sage root repo to either of these, you may be asked twice if you want to upgrade.  I mentioned this issue [above](http://trac.sagemath.org/sage_trac/ticket/9433#comment:22).
> 
> According to the comment you refer to, this should read _"upgrade from a version *without* a Sage root repo"_.

Yes, that's what I meant to say.  Sorry for any confusion.


---

Comment by leif created at 2010-11-06 08:40:27

Replying to [comment:67 jhpalmieri]:
> Replying to [comment:64 leif]:
> > We *have to* download `spkg/install` (and I'd prefer the rest, too) in `sage-update` (the Python script).
> 
> I'm not sure what "the rest" refers to here.

Well, the files that were previously downloaded (`deps` and `newest_version`, too). But also downloading `sage-env` (and e.g. `sage-spkg`) is not a bad idea.

(I also plan to download `upgrade-notes.txt` and `pre-upgrade-script.sh` first, such that the user (and we) can make an informed choice.)



> > What's currently newly made in `sage-upgrade` should be moved to that file, which is in any case the fresh, downloaded one. _There_ we have to make a distinction on if we are upgrading.
> 
> Okay, I think I can do that.
> 
> > If so, `spkg/install` should then install the root repo (preferably without overwriting itself, but the root repo should, i.e. must, contain exactly the same file), since our "real" Makefile `spkg/standard/deps` doesn't (though I don't know why you don't want to put the root spkg there).
> 
> I don't want to put it there because in a non-upgrade, it's already installed as part of the download.

Well, then `hg pull` would simply be a no-op. But we should check the exit codes of the commands in `root-spkg-install` (`hg` and `cp`) anyway.

`hg incoming <source repo>` returns 1 if there's nothing to pull, 0 if there are changes to pull, other values on errors, so you could change it to:

```sh
...
if [ -d "$TARGET"/.hg ]; then

    # Merge the repository, rather than overwrite changes that the
    # user may have made.
    cd "$TARGET"
    hg ci  # Don't know if we should check in unconditionally,
           # so perhaps move this below the if-elif-fi.
    # should check for errors here
    
    hg incoming "$CUR"  # perhaps redirect output
    if [ $? -eq 1 ]; then
        # No changes to pull
        exit 0
    elif [ $? -ne 0 ]; then
        # Some error, report...
        exit 1
    fi
    # $? = 0: Changes to pull...
    hg pull "$CUR"
    hg merge tip
    hg ci -m "Check-in during upgrade of Sage."
    hg update
    # Add error checks above, too.

else
    ...
```


(Or you could add a rule to `deps` that tests its presence / the need to pull first, before calling `sage-spkg`. But if we one day generate `deps`, this would be less optimal.)



> > Btw, it would be better to also have `sage-spkg` in the root rather than the scripts repo; or download an identical copy (from the scripts repo) along with `install`, `deps` etc.
> 
> That's not a bad idea, but it should go on another ticket.  What about the other scripts in spkg/base, for example sage-env?

Yes, see above. Once we have this ticket in, it will be easier (or at least safer) to make such changes. :-)


P.S.: I wonder if the presence of `$SAGE_ROOT/.hg` guarantees us a functional Mercurial... ;-)


---

Comment by jhpalmieri created at 2010-11-06 15:33:30

Replying to [comment:68 leif]:

Downloading these various files in sage-update seems to at least partly defeat the purpose of the new repo, but anyway.

> Replying to [comment:67 jhpalmieri]:

> > I don't want to put it [deps] because in a non-upgrade, it's already installed as part of the download.
> 
> Well, then `hg pull` would simply be a no-op. But we should check the exit codes of the commands in `root-spkg-install` (`hg` and `cp`) anyway.

If we put it in deps, I guess it gets installed at the end?  I was tempted to make it part of BASE, but then during an upgrade, any changes to the Sage root repo would mean that everything would be rebuilt, which would be annoying.  The only issue is if there is an upgrade to a script like "pipestatus" which is in the root repo, is used in the upgrade process, and is not downloaded in sage-update.

> P.S.: I wonder if the presence of `$SAGE_ROOT/.hg` guarantees us a functional Mercurial... ;-)

I think I'll switch to running "hg verify".


---

Comment by jhpalmieri created at 2010-11-06 17:52:40

Okay, here's a new scripts patch (with no changes to sage-update or sage-upgrade), along with new "deps" and "install".  I've updated the upgrade paths I listed above; I'm adding them to the ticket description.  I am still building Sage 4.4; when that's done, I'll test upgrading it.


---

Comment by jhpalmieri created at 2010-11-06 17:55:17

the file SAGE_ROOT/spkg/install


---

Attachment

diff between current install and new one; for reference only


---

Attachment

the file SAGE_ROOT/spkg/root-spkg-install


---

Attachment

patch for scripts repo


---

Comment by jhpalmieri created at 2010-11-06 18:47:30

the file SAGE_ROOT/spkg/standard/deps


---

Attachment

diff between current deps and new one; for reference only


---

Attachment

For what it's worth, I've done the following successfully with the current versions:

 - build from scratch ("./sage -sdist ..." produced the tar file [http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha0.tar](http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha0.tar))
 - upgrade from 4.6.1.alpha0, and then upgrade again to the version with a modified root repo
 - same, but started from 4.4

This was all on sage.math.  I also tested 4.6.1.alpha0 on OS X 10.6 with no problems.

I'm testing "./sage -bdist ...", which I forgot to do earlier.  I'm also testing a build from scratch on another platform.


---

Comment by jdemeyer created at 2010-11-07 17:47:23

Is this ticket now really ready for review? (if not, please change status to needs_work).


---

Comment by jdemeyer created at 2010-11-07 17:51:15

Please also add a `root-spkg-install.patch`.  I prefer using the patches, not the patched files.


---

Comment by jdemeyer created at 2010-11-07 17:51:15

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-11-07 17:57:40

Can the people involved in this ticket give their opinion about #10231? (informally, the patch is not yet ready for review)  If you agree with #10231, we need to coordinate this ticket with it.


---

Comment by jhpalmieri created at 2010-11-07 18:52:56

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-11-07 18:52:56

Replying to [comment:75 jdemeyer]:
> Please also add a `root-spkg-install.patch`.  I prefer using the patches, not the patched files.

I'm not sure what you mean: the file "root-spkg-install" is completely new to this ticket, and is not part of any pre-existing repo.  So there's nothing to patch.  I'm flipping this back to "needs review".

Regarding #10231, I'd like to see more discussion on sage-devel about it.  I know that leif disagrees, but I'm also interested in the idea of combining the various non-root repos (scripts, examples, extcode, and the main Sage library) into one.  It seems like the Sage community should decide about both of these issues in sage-devel rather than on a trac ticket.


---

Comment by jdemeyer created at 2010-11-07 20:17:56

Replying to [comment:77 jhpalmieri]:
> Replying to [comment:75 jdemeyer]:
> > Please also add a `root-spkg-install.patch`.  I prefer using the patches, not the patched files.
> 
> I'm not sure what you mean: the file "root-spkg-install" is completely new to this ticket, and is not part of any pre-existing repo.

In that case, sorry for the noise.


---

Comment by jdemeyer created at 2010-11-07 20:26:57

Replying to [comment:77 jhpalmieri]:
> Regarding #10231, I'd like to see more discussion on sage-devel about it.  I know that leif disagrees, but I'm also interested in the idea of combining the various non-root repos (scripts, examples, extcode, and the main Sage library) into one.  It seems like the Sage community should decide about both of these issues in sage-devel rather than on a trac ticket.

Well, there was some discussion at [http://groups.google.com/group/sage-devel/browse_thread/thread/cc30eaf87b283881/c2290991827fec9c?hl=en_US&#c2290991827fec9c](http://groups.google.com/group/sage-devel/browse_thread/thread/cc30eaf87b283881/c2290991827fec9c?hl=en_US&#c2290991827fec9c).

Personally, I simply don't see the need for merging sage, sage_scripts, extcode, examples,... into one big spkg.  So there is some disagreement on this.  But this disagreement should not stop us from doing something to which most people seemed to agree: not repackaging extcode and examples with every new Sage version (which is exactly what I want to accomplish with #10231).


---

Comment by jhpalmieri created at 2010-11-07 23:33:15

Replying to [comment:79 jdemeyer]:
> Well, there was some discussion at [http://groups.google.com/group/sage-devel/browse_thread/thread/cc30eaf87b283881/c2290991827fec9c?hl=en_US&#c2290991827fec9c](http://groups.google.com/group/sage-devel/browse_thread/thread/cc30eaf87b283881/c2290991827fec9c?hl=en_US&#c2290991827fec9c).

Not too much discussion of that proposal.  You suggested it, and a few people liked the idea.  On the other hand, a few people made the counter-proposal to merge all of the repositories.  If we end up merging everything, then doing #10231 first will make more work: whatever is involved in that, and then the merge, as opposed to just the merge.  So I'd like to see more of a consensus about which direction to go before putting much effort into #10231.

This ticket seems like a separate issue, and regardless of everything else, the Sage root repo should remain separate from the others, because it should already be installed when you unpack the Sage tar ball.  Perhaps its role should increase, including files like sage-env and sage-spkg, but that's for another ticket.  I hope this ticket can get a positive review soon, and then if anyone feels like working on #10231 (or on a possible merge of the repos), they can base their work on this ticket and other tickets which touch sage-sdist and related files.


---

Comment by ddrake created at 2010-11-09 01:44:15

Replying to [comment:62 jhpalmieri]:
> Okay for testing upgrading:
> {{{
> ./sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.1.9433.alpha0/
> }}}

I've tried twice with 4.6 using the above command, and despite the upgrade appearing to work, I get this when I start Sage:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_plot3d.py:5: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility
  from implicit_surface import ImplicitSurface
/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/plot/plot3d/implicit_plot3d.py:5: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility
  from implicit_surface import ImplicitSurface
/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/calculus/all.py:20: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility
  from interpolators import polygon_spline, complex_cubic_spline
/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/calculus/all.py:20: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility
  from interpolators import polygon_spline, complex_cubic_spline
/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/stats/hmm/all.py:8: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility
  from hmm  import DiscreteHiddenMarkovModel
/home/drake/s/9433/sage-4.6/local/lib/python2.6/site-packages/sage/stats/hmm/all.py:8: RuntimeWarning: numpy.flatiter size changed, may indicate binary incompatibility
  from hmm  import DiscreteHiddenMarkovModel
sage: 
```



---

Comment by kcrisman created at 2010-11-09 01:47:39

Dan, you have to touch the Cython include file and then do `./sage -b` to build the dependencies - see #9808 for details.  Or you could do `./sage -ba` and wait a long time.


---

Comment by ddrake created at 2010-11-09 02:50:57

Replying to [comment:82 kcrisman]:
> Dan, you have to touch the Cython include file and then do `./sage -b` to build the dependencies - see #9808 for details.  Or you could do `./sage -ba` and wait a long time.

That fixed it! Thanks. The first upgrade works fine now; I'm testing the second.


---

Comment by ddrake created at 2010-11-10 01:27:52

Replying to [comment:62 jhpalmieri]:
> Okay for testing upgrading:

I started with 4.6, and both upgrade paths work fine: first to "9433.alpha0", then to 9433.alpha1, and also directly to 9433.alpha1. I'm currently testing with upgrades from 4.3.5.


---

Comment by ddrake created at 2010-11-10 07:08:19

Replying to [comment:84 ddrake]:
> Replying to [comment:62 jhpalmieri]:
> > Okay for testing upgrading:
> 
> I started with 4.6, and both upgrade paths work fine: first to "9433.alpha0", then to 9433.alpha1, and also directly to 9433.alpha1. I'm currently testing with upgrades from 4.3.5.

Both upgrade paths also work when upgrading from 4.3.5. (I'm using 64-bit Ubuntu 10.04.)


---

Comment by jhpalmieri created at 2010-11-11 21:05:55

I just added "VERSION.txt" to the .hgignore file, for compatibility with #9434.


---

Attachment

Updated spkg/install


---

Comment by vbraun created at 2011-01-13 07:19:18

Updated spkg/standard/deps


---

Comment by vbraun created at 2011-01-13 07:38:33

Changing status from needs_review to positive_review.


---

Attachment

After some rediffing I built it successfully on top of Sage-4.6.1.rc1 (identical to the Sage-4.6.1 release) with the following updated files:

  * `trac_9433-scripts.v5.patch` -> `trac_9433-scripts.v5.2.patch`
  * `install` -> `install.2`
  * `deps` -> `deps.2`

I've changed the main ticket documentation accordingly. 

For reference, here is a list of files in the root repository:

```
[vbraun`@`volker-two sage-4.6.1.vb2]$ hg st --all | grep -v '^I'
C .hgignore
C .hgtags
C COPYING.txt
C Makefile
C README.txt
C ipython/ipy_profile_sh.py
C ipython/ipy_user_conf.py
C ipython/ipythonrc
C ipython/ipythonrc-math
C ipython/ipythonrc-numeric
C ipython/ipythonrc-physics
C ipython/ipythonrc-pysh
C ipython/ipythonrc-scipy
C ipython/ipythonrc-tutorial
C sage
C spkg/README.txt
C spkg/gen_html
C spkg/install
C spkg/pipestatus
C spkg/root-spkg-install
C spkg/standard/README.txt
C spkg/standard/deps
C spkg/standard/libdist_filelist
C spkg/standard/newest_version
```


Really, any kind of root repository would be better than the caveman technology we have in place right now. I read through all the scripts and they do make sense to me. I built my private release using `sage -sdist <version>` and it compiled fine. You guys put a lot of effort into this ticket to make sure that nothing breaks, and I think it really is the time to integrate this with Sage. 

Positive review.

Jeroen, can you plug this into 4.6.2.alpha as soon as possible to give it as much exposure as possible?


---

Comment by jdemeyer created at 2011-01-19 08:58:05

Why do we need a `sage_root.spkg`?  I don't see a reason for a "root repo" to ever exist in tarball form.


---

Comment by jdemeyer created at 2011-01-19 08:58:05

Changing status from positive_review to needs_info.


---

Attachment


---

Comment by jdemeyer created at 2011-01-19 09:06:50

Changing status from needs_info to needs_work.


---

Comment by jdemeyer created at 2011-01-19 09:06:50

If we do this, we really should also take care of the following *duplicate* files (files both in sage_scripts and in another repo):

```
README.txt
spkg/install
spkg/base/sage-spkg
spkg/base/sage-env
spkg/base/sage-make_relative
spkg/base/sage-check-64 (added by the not-yet-merged #10303)
```


Also, I think we should get rid of the `spkg/base` repo and merge it with the new root repo.


---

Comment by vbraun created at 2011-01-19 17:05:23

Replying to [comment:88 jdemeyer]:
> Why do we need a `sage_root.spkg`?  I don't see a reason for a "root repo" to ever exist in tarball form.

The way things are set up right now, if you upgrade an existing sage installation then the updated `SAGE_ROOT_REPO` will merge updates to the `$SAGE_ROOT` repository. As long as we don't have an official online repository to pull changes from I don't see any better way to do the upgrade. Am I missing something?

I agree that we need to disentangle the `sage_root` repository more from `sage_scripts`. Basically, everything that `sage_scripts/spkg-install` manually copies into `$SAGE_ROOT` should be part of the root repo, like `README.txt`. But I think this can wait until we actually do have a `sage_root` repository. Then it'll be easy to write complimentary patches for the two repositories that clean this up.

I'm also totally in favour of merging the spkg/base repo. Since that has only 26 log entries (with the most recent one from July), I think we can live without preserving its history. Right now we don't use this repository during upgrades as far as I know.

If you agree with this then I'll make a followup ticket...


---

Comment by vbraun created at 2011-01-19 17:05:23

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2011-01-19 20:31:53

Replying to [comment:92 vbraun]:
> Replying to [comment:88 jdemeyer]:
> > Why do we need a `sage_root.spkg`?  I don't see a reason for a "root repo" to ever exist in tarball form.
> 
> The way things are set up right now, if you upgrade an existing sage installation then the updated `SAGE_ROOT_REPO` will merge updates to the `$SAGE_ROOT` repository. As long as we don't have an official online repository to pull changes from I don't see any better way to do the upgrade.
I have to admit I know nothing about this.  If you really think we need a `sage_root.spkg` then I believe you...

> I agree that we need to disentangle the `sage_root` repository more from `sage_scripts`. Basically, everything that `sage_scripts/spkg-install` manually copies into `$SAGE_ROOT` should be part of the root repo, like `README.txt`. But I think this can wait until we actually do have a `sage_root` repository. Then it'll be easy to write complimentary patches for the two repositories that clean this up.
Personally, I would rather like to clean this up as part of _this_ ticket.  Keep in mind that adding or changing the working of a SAGE_ROOT repo will require some changes to the process of merging Sage releases.  I would prefer to have to do this only once, not once for this ticket and once for every follow-up ticket.

> I'm also totally in favour of merging the spkg/base repo. Since that has only 26 log entries (with the most recent one from July), I think we can live without preserving its history. Right now we don't use this repository during upgrades as far as I know.
> 
> If you agree with this then I'll make a followup ticket...
Same answer as before: I prefer to do it in _this_ ticket.


---

Comment by jdemeyer created at 2011-01-19 20:31:53

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2011-01-19 20:42:37

Replying to [comment:93 jdemeyer]:
> Replying to [comment:92 vbraun]:
> > Replying to [comment:88 jdemeyer]:
> > > Why do we need a `sage_root.spkg`?  I don't see a reason for a "root repo" to ever exist in tarball form.
> > 
> > The way things are set up right now, if you upgrade an existing sage installation then the updated `SAGE_ROOT_REPO` will merge updates to the `$SAGE_ROOT` repository. As long as we don't have an official online repository to pull changes from I don't see any better way to do the upgrade.
> I have to admit I know nothing about this.  If you really think we need a `sage_root.spkg` then I believe you...

Yes, that's the reason for its existence.

> > I agree that we need to disentangle the `sage_root` repository more from `sage_scripts`. Basically, everything that `sage_scripts/spkg-install` manually copies into `$SAGE_ROOT` should be part of the root repo, like `README.txt`. But I think this can wait until we actually do have a `sage_root` repository. Then it'll be easy to write complimentary patches for the two repositories that clean this up.
> Personally, I would rather like to clean this up as part of _this_ ticket.  Keep in mind that adding or changing the working of a SAGE_ROOT repo will require some changes to the process of merging Sage releases.  I would prefer to have to do this only once, not once for this ticket and once for every follow-up ticket.

I think I don't understand. Once there is a SAGE_ROOT repo, then any follow-up ticket can just have a patch which needs to be applied to that repo, as opposed to manually patching `spkg/install` or `Makefile` or whatever. 

For the particular change you have in mind, it requires modifying various scripts (like spkg-install, but maybe others?) in local/bin, and it could possibly be complicated.  It seems safer to do things incrementally, first setting up the new repo, then on a later ticket making further changes.

(I also have a heavy teaching load right now, so I won't have much time to work on this.  I can try to fix bugs with the current implementation when anyone finds them, but I don't think I can work on any major modifications, like dealing with the spkg/base repo.)


---

Comment by vbraun created at 2011-01-19 20:50:39

I'm with John here: Its easy to generate a patch that adds a new file to the `sage_root` repository. You don't have to do anything else for updates, the change will automatically make it into the next `sage_root` package. No more manually digging around to make a new source distribution :-)


---

Comment by kcrisman created at 2011-01-19 20:53:54

> For the particular change you have in mind, it requires modifying various scripts (like spkg-install, but maybe others?) in local/bin, and it could possibly be complicated.  It seems safer to do things incrementally, first setting up the new repo, then on a later ticket making further changes.
And indeed, this is the Sage way of doing things - perfect being the enemy of things ever happening in the open development, open source model.

I'd also like to put in a plug for sage-README-osx.txt finally being removed from $SAGE_ROOT. Apparently #6938 never got 'merged'...> (I also have a heavy teaching load right now, so I won't have much time to work on this.  I can try to fix bugs with the current implementation when anyone finds them, but I don't think I can work on any major modifications, like dealing with the spkg/base repo.)


---

Comment by jdemeyer created at 2011-01-19 21:08:05

Replying to [comment:96 kcrisman]:
> And indeed, this is the Sage way of doing things - perfect being the enemy of things ever happening in the open development, open source model.

In general, I completely agree with your sentiment: too many times a patch has not been finished because it was not the "optimal" solution.  However, this only applies if the halfway-implemented patch makes the situation better.

For this particular ticket, I feel that having a halfway-implemented sage_root repository is strictly worse than having no sage_root repository at all.  The situation for merging SAGE_ROOT patches is already complicated enough (but I can manage) and I'm afraid the current patch on this ticket will make it only worse.

This is not a ticket I want to "rush" into Sage.


---

Comment by vbraun created at 2011-01-19 21:18:40

Replying to [comment:97 jdemeyer]:
> This is not a ticket I want to "rush" into Sage.

This ticket has been worked on for 7 months and has almost 100 comments ;-)

And every time I want to change something on this ticket I need half a day to rebuild sage, manually make half a dozen changes, test the source distribution. 

I can make the changes you wanted in comment:91 but there are a bunch of other files I want to move to the `sage_root` repository as well. Some of them might need some discussion on sage-devel first. How many more months should we wait until the main makefile is under revision control?


---

Comment by ddrake created at 2011-01-20 04:41:23

Replying to [comment:97 jdemeyer]:
> For this particular ticket, I feel that having a halfway-implemented sage_root repository is strictly worse than having no sage_root repository at all.

In what way is the SAGE_ROOT repo "halfway-implemented"? With these scripts and patches, the repo will exist and work for upgrades and new builds.

> The situation for merging SAGE_ROOT patches is already complicated enough (but I can manage) 

Maybe you can manage -- but there's plenty of evidence that other release managers can't. Changing files in SAGE_ROOT currently takes a long time and is an extremely brittle process; why continue in this way?

And even if there's no trouble actually changing files, we still have no version control for our basic makefile, README, and executable script. The only way to track changes is to download tarballs, unpack them, and compare files. Think about it: neither the basic file with which we build Sage (the makefile) nor the basic file with which one runs Sage (SAGE_ROOT/sage) are under any version control! That is crazy. Imagine if Firefox shipped with their "firefox" script not under version control.

> and I'm afraid the current patch on this ticket will make it only worse.

Right now to change the README:

  * make a backup copy
  * make your changes
  * manually run `diff -u` to produce a patch
  * upload _both_ the new README and the patch to a ticket
  * upon positive review, hope that the release manager replaces the README file correctly and does `sage -sdist` in the right directory

With a SAGE_ROOT repo:

  * use the same procedure that one uses in the Sage library to produce a patch.
  * release manager uses same procedure as for the Sage library to merge the patch.

Perhaps it's only me, but the current situation seems far worse.

Please, let's create the SAGE_ROOT repo and argue about merging repos after they actually exist.


---

Comment by jdemeyer created at 2011-01-20 08:50:23

Replying to [comment:99 ddrake]:
>   * release manager uses same procedure as for the Sage library to merge the patch.

Wrong, because the `README` is actually already in a different repository, namely `sage_scripts`.  This is the issue of duplicate files that I mentioned above.


---

Comment by jhpalmieri created at 2011-01-20 15:36:53

After applying the patches here, README.txt will be in the SAGE_ROOT repo, not the scripts repo.  The full list of files which will be tracked:

 -.hgignore .hgtags COPYING.txt README.txt Makefile sage
 - in the ipython directory: *.py, ipythonrc*
 - in the spkg directory: README.txt gen_html install pipestatus root-spkg-install
 - in the spkg/standard directory: README.txt deps libdist_filelist newest_version


---

Comment by jdemeyer created at 2011-01-20 16:19:28

The `SAGE_ROOT/ipython` directory is *created* during the Sage build process, so I don't think it should be part of the `SAGE_ROOT` repository.


---

Comment by jdemeyer created at 2011-01-20 16:36:52

What's the reason for removing the quoting of `SAGE_ROOT` in `sage-spkg-install`?


---

Comment by jhpalmieri created at 2011-01-20 16:48:29

Replying to [comment:102 jdemeyer]:
> The `SAGE_ROOT/ipython` directory is *created* during the Sage build process, so I don't think it should be part of the `SAGE_ROOT` repository.

It's just copied from whatever was there before.  Why not track those files in a repository?  Otherwise they're not tracked anywhere: what if we want to change any of them?  Also, if you decide to not include them in the repo, then you'll need to work on the scripts patch: put back the parts (in sage-sdist for example) which create those files.

> What's the reason for removing the quoting of SAGE_ROOT in sage-spkg-install?

That was presumably just a mistake.


---

Comment by vbraun created at 2011-01-20 16:50:55

The ipython directory is in the `sage_scripts` repository and `sage_scripts/spkg-install` manually copies it into `$SAGE_ROOT`. The patch on this ticket removes that part from `sage_scripts/spkg-install`, so it will no longer be copied over.

I'm not sure if the removal of the quotes has any deeper meaning. But right-hand-sides of variable assignments need not be quoted in shell script:

```
[vbraun`@`volker-two ~]$ x="a b"
[vbraun`@`volker-two ~]$ y=$x/c
[vbraun`@`volker-two ~]$ echo $y
a b/c
```



---

Comment by jdemeyer created at 2011-01-20 16:55:38

Replying to [comment:106 vbraun]:
> The ipython directory is in the `sage_scripts` repository and `sage_scripts/spkg-install` manually copies it into `$SAGE_ROOT`. The patch on this ticket removes that part from `sage_scripts/spkg-install`, so it will no longer be copied over.
Okay, I see.  I got confused by the renaming of `sage-spkg-install` to `spkg-install`, so I didn't realize what the file `sage-spkg-install` was all about.

> I'm not sure if the removal of the quotes has any deeper meaning. But right-hand-sides of variable assignments need not be quoted in shell script:
> {{{
> [vbraun`@`volker-two ~]$ x="a b"
> [vbraun`@`volker-two ~]$ y=$x/c
> [vbraun`@`volker-two ~]$ echo $y
> a b/c
> }}}
I agree, but I think that having the quotes is clearer anyway.

This is most certainly a bug (in `sage-make_devel_packages`):

```
+if [ ! -f "$PKG/sage_scripts-$SAGE_VERSION.spkg" ]; then
```



---

Comment by vbraun created at 2011-01-20 17:00:14

Upon closer investigation I found that the ipython directory is in the `sage_scripts` spkg, but ignored in the `sage_scripts` mercurial repository. So its even worse :-)


---

Attachment

Updated patch


---

Comment by jdemeyer created at 2011-01-20 17:08:18

Ha, I beat you by 13 seconds! :-)


---

Comment by vbraun created at 2011-01-20 17:11:32

That was probably my typo in rebasing the patch to Sage-4.6.1 ;-)


---

Attachment


---

Attachment

I'm fine with all changes.


---

Comment by vbraun created at 2011-01-20 23:20:37

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-01-21 03:18:26

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-01-21 03:18:26

Upgrading from earlier versions of Sage doesn't work because `spkg/standard/VERSION.txt` is gone:


```
$ ./sage -upgrade http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root/
Downloading packages from 'http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg'.
Reading package lists...  Done!
The following packages will be upgraded:

    examples-4.6.2.sage_root extcode-4.6.2.sage_root
    sage-4.6.2.sage_root sage_root-4.6.2.sage_root
    sage_scripts-4.6.2.sage_root

 ** WARNING: This is a source-based upgrade, which could take hours,
 ** fail, and render your Sage install useless!!

Do you want to continue [y/N]? y
http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/examples-4.6.2.sage_root.spkg --> examples-4.6.2.sage_root.spkg [..................................................]
Deleting old spkg 'examples-4.6.1.spkg'...
http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/extcode-4.6.2.sage_root.spkg --> extcode-4.6.2.sage_root.spkg [..................................................]
Deleting old spkg 'extcode-4.6.1.spkg'...
http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/sage-4.6.2.sage_root.spkg --> sage-4.6.2.sage_root.spkg [..................................................]
Deleting old spkg 'sage-4.6.1.spkg'...
http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/sage_root-4.6.2.sage_root.spkg --> sage_root-4.6.2.sage_root.spkg [..............]
http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/sage_scripts-4.6.2.sage_root.spkg --> sage_scripts-4.6.2.sage_root.spkg [..................................................]
Deleting old spkg 'sage_scripts-4.6.1.spkg'...
http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/VERSION.txt --> VERSION.txt [.]
Failed to download 'http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.2.sage_root/sage-4.6.2.sage_root//spkg/standard/VERSION.txt'.
Abort.
```



---

Comment by jhpalmieri created at 2011-01-21 05:04:23

Replying to [comment:115 jdemeyer]:
> Upgrading from earlier versions of Sage doesn't work because `spkg/standard/VERSION.txt` is gone:

That's because when the scripts patch was rebased, lines like these were removed:

```
# Put VERSION.txt in a directory available for download during the 
# update process.  (See sage-update.) 
cp -p VERSION.txt $TMP/$PKGDIR/$STD/
```

I think that just restoring these lines should fix it .


---

Comment by jhpalmieri created at 2011-01-21 05:31:58

patch for scripts repo


---

Attachment

Here's a new patch for the scripts repo.


---

Comment by jhpalmieri created at 2011-01-21 05:33:47

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2011-01-21 19:16:37

Yes that fixes it!


---

Comment by vbraun created at 2011-01-21 19:16:37

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2011-01-22 04:00:16

For the record: I successfully upgraded a Sage-4.6.1 installation to Sage-4.6.2.alpha1.


---

Attachment

SAGEROOT patch for testing, DO NOT APPLY


---

Comment by jdemeyer created at 2011-01-23 13:15:07

Changing priority from major to blocker.


---

Attachment


---

Comment by jdemeyer created at 2011-02-16 08:59:24

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-02-16 08:59:50

Testing changes to root-spkg-install...


---

Comment by jdemeyer created at 2011-02-16 09:06:40

It seems that the `SAGE_ROOT` repository requires a very recent of Mercurial.  With Mercurial version 1.6.4, I get

```
$ hg --version
Mercurial Distributed SCM (version 1.6.4)

Copyright (C) 2005-2010 Matt Mackall <mpm`@`selenic.com> and others
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
$ hg commit
abort: requirement 'dotencode' not supported!
```


I agree that a sufficiently recent version of Mercurial is shipped with Sage, but unless there is a good reason for this `dotencode` requirement, I would prefer if the root repo worked with Mercurial 1.3.1 like the other repos.


---

Comment by jdemeyer created at 2011-02-16 09:09:09

The file `spkg-install` from the root repo is not under revision control.  Is there a reason for this?


---

Comment by jdemeyer created at 2011-02-16 09:18:30

The file $SAGE_ROOT/spkg/root-spkg-install


---

Attachment

create root repository without dotencode


---

Attachment

I'm pretty sure that the `root-spkg-install` ought to be under revision control. I'm travelling right now, so I can't test it out myself.


---

Comment by jhpalmieri created at 2011-02-16 15:35:10

I don't think there is anything in the repository which should require a new version of Mercurial. According to [this page from the Mercurial wiki](http://mercurial.selenic.com/wiki/RequiresFile), if you create a repo with a newer version and then try to access it with an older version, you can see this message.  So I don't think it's anything specific about the root repo.

I'll try to look into the root-spkg-install file issue.


---

Comment by jhpalmieri created at 2011-02-16 15:38:46

Okay, line 24 in `9433_hg_script.sh` is

```
( cd spkg && hg add README.txt gen_html install pipestatus root-spkg-install )
```

So it looks like root-spkg-install should be tracked. Can you explain why you think it's not?

Also, I see that vbraun has a new version of this script which might avoid the dotencode issue...


---

Comment by vbraun created at 2011-02-16 16:02:47

Yes, I tripped over the dotencode thing before when working with mercurial. We don't really need that, so its ok to switch it off for backward compatibility, at least for the next year or so.


---

Comment by jhpalmieri created at 2011-02-16 21:02:10

the file SAGE_ROOT/.hgignore, now including spkg-install


---

Attachment

Replying to [comment:127 jdemeyer]:
> The file `spkg-install` from the root repo is not under revision control.  Is there a reason for this?

I now realize that you're talking about the file `spkg-install` in the actual spkg file.  This is just a copy of `root-spkg-install` made by `sage-make_devel_packages`, so we don't need to track it.  I'm going to add it to the `.hgignore` file (by adding `^spkg-install$`, so it only matches a file with exactly that name at the top level).  This change requires review.

Meanwhile, I'm giving Volker's change to the hg_script a positive review: for me, it makes any errors about dotencode go away when I use an older version of Mercurial to access the repo.


---

Comment by jhpalmieri created at 2011-02-16 21:06:38

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2011-02-17 19:32:16

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-02-17 19:32:16

About the `dotencode` requirement: the change in the shell script indeed "fixes" the actual root repository.  However, the created `sage-root` spkg still has a mercurial repository which requires `dotencode` (so, after sdist and make, you need a new version of `hg`).  Since none of the other spkgs have this behaviour, I think this still needs work.


---

Comment by jhpalmieri created at 2011-02-18 01:16:17

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-02-18 01:16:17

I don't really understand this complaint.  After all, Sage is distributed with a version of Mercurial, and it is completely reasonable to require that version for repositories which are part of Sage.  It's easy enough to type "sage -hg" instead of "hg", or make an alias, or put the Sage version of hg in your $PATH.  I think this is more a problem with Mercurial -- why is it not backwards compatible?  Who merged this version of Mercurial into Sage?   Did the spkg maintainers or release manager notice or discuss this incompatibility issue?  

Also, if you're going to start inventing rules about how an spkg should be prepared, you might consider putting those rules in the developer's guide, and perhaps discussing them and getting approval for them on sage-devel before imposing them.

We can add `--config format.dotencode=0` at various places in sage-sdist and sage-make_devel_packages, and I'm attaching a new version of the scripts patch to do this, but this is not a viable long-term solution: the version requirements of Mercurial for anyone who wants to make a new spkg for Sage need to be made public, not imposed at anyone's whim.


---

Attachment

patch for scripts repo


---

Comment by jdemeyer created at 2011-02-18 08:15:03

Replying to [comment:134 jhpalmieri]:
> Did the spkg maintainers or release manager notice or discuss this incompatibility issue?  
I didn't know about this until looking at this ticket.

Why not simply avoid `hg clone` in `sage-make_devel_packages`?  If the other spkgs can be made without using `hg clone`, surely the same should work for the `sage_root` spkg?


---

Comment by jdemeyer created at 2011-02-18 08:42:12

Version 1.7.3 of Mercurial was merged in sage-4.6.2.alpha2, ticket #10594.  It can still be unmerged if you think that's a good thing to do.  Then we would fall back to Mercurial 1.6.4.


---

Comment by jhpalmieri created at 2011-02-18 19:32:45

Replying to [comment:136 jdemeyer]:
> Why not simply avoid `hg clone` in `sage-make_devel_packages`?  If the other spkgs can be made without using `hg clone`, surely the same should work for the `sage_root` spkg?

It certainly could be done, but it makes the repo harder to maintain.  Suppose you want to add a new file to the repo.  If you clone, you just run "hg add" (or apply a patch which accomplishes this) and you're done.  If you manually copy everything over, as is done for the other repos, then you also have to modify sage-make_devel_packages, maybe root-spkg-install, maybe sage-sdist.  This is especially true for the root repo, where files need to be dealt with individually: it's not like the Sage repo where except for a handful of files, you just copy over an entire directory (devel/sage/sage/), and it's not like the scripts repo where except for a handful of files, you just copy over everything with a certain name ("sage-*").

Maybe instead it could run "hg manifest" and then manually copy over the listed files.  But this seems really awkward when "hg clone" does exactly what is required.

> Version 1.7.3 of Mercurial was merged in sage-4.6.2.alpha2, ticket #10594. It can still be unmerged if you think that's a good thing to do. Then we would fall back to Mercurial 1.6.4.

I'm really not sure about this.  Perhaps it should be discussed on #10594.  The lack of backwards compatibility seems problematic to me.  I can try to post something there later today.


---

Comment by vbraun created at 2011-02-18 20:39:20

Anything that creates a new mercurial repository will by default require dotencode. In particular, `$SAGE_LOCAL/bin/sage-clone` which is unrelated to this ticket. 

It would be easy to add `--config format.dotencode=0` to all `hg init`, `hg clone` commands. But current distributions already picked up the new mercurial, so I don't see it as particularly pressing issue. Moreover, we have a suitable mercurial in Sage precisely because it is sometimes finky with old versions. I would be in favor of just using dotencode. If it causes a big problem then we can always revert the repository format, you just have to clone with `dotencode=0`.


---

Comment by jdemeyer created at 2011-02-20 15:02:26

Testing distributions:

 1. http://boxen.math.washington.edu/home/release/sage-4.7.alpha0/: sage-4.6.2.rc0 + this ticket
 1. http://boxen.math.washington.edu/home/release/sage-4.7.alpha1/: sage-4.7.alpha0 + some random stuff (#10688 and [attachment:9433_testing.patch])


---

Comment by jdemeyer created at 2011-02-20 15:09:24

Upgrading sage-4.7.alpha0 -> sage-4.7.alpha1 fails because of uncommitted changes: during the install of `sage_root-4.7.alpha1.spkg`, I get an editor with

```
HG: Enter commit message.  Lines beginning with 'HG:' are removed.
HG: Leave message empty to abort commit.
HG: --
HG: user: Jeroen Demeyer <jdemeyer`@`cage.ugent.be>
HG: branch 'default'
HG: changed spkg/install
HG: changed spkg/standard/deps
```


`hg diff` gives:

```
diff -r 1c44cedc9957 spkg/install
--- a/spkg/install      Thu Feb 17 15:54:54 2011 +0000
+++ b/spkg/install      Sun Feb 20 16:06:09 2011 +0100
`@``@` -1,5 +1,7 `@``@`
 #!/usr/bin/env bash

+# TESTING PATCH
+
 ###############################################################################
 # Check if pipestatus already exists, otherwise
 # create it to allow upgrade from Sage <4.5.  This is a temporary fix.
`@``@` -422,9 +424,6 `@``@`
 TERMCAP=`$newest termcap`
 export TERMCAP

-WEAVE=`$newest weave`
-export WEAVE
-
 ZLIB=`$newest zlib`
 export ZLIB

```

and something similar for `spkg/standard/deps`.

It seems that `spkg/install` and `spkg/standard/deps` are changed by the upgrader before the Sage root repository is installed and that this causes trouble.


---

Comment by jdemeyer created at 2011-02-20 15:09:24

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-02-21 10:58:37

John (and/or Volker), do you have time to work on this in the coming week / 2 weeks?  If yes, I would like to merge this in sage-4.7.alpha0.  This ticket might require some more work to get it right, so it would be nice to know whether you have time.  Otherwise we can postpone this to a later Sage release.


---

Comment by vbraun created at 2011-02-21 11:13:14

I'm around and am in favor of merging it asap.


---

Comment by jhpalmieri created at 2011-02-21 15:57:03

I have a fix to this problem which I am testing right now.  It looks good so far, and I'll post it later if it continues to look good.  (The fix is as follows: the script `sage-update` downloads new versions of several files, like `install` and `deps`; I'm now adding a command to commit the Sage root repo after doing this download.)


---

Comment by jhpalmieri created at 2011-02-21 16:45:15

Okay, I have two options; which is better?  In `sage-update`, the files install, deps, and newest_version might get changed.  We could:

 - commit the changes in `sage-update`, and then the changes will get committed again by `root-spkg-install` when the root repo spkg is installed.

 - or in `root-spkg-install`, we can overwrite any changes: do `hg pull ...` to pull from the new repo and then `hg update --clean` to discard any other changes.

The first of these adds a redundant commit message to the log file if the relevant files are changed.  The second discards all changes, including any other ones that the user may have made.  I don't know Mercurial well enough, but perhaps there is a better third choice?


---

Comment by vbraun created at 2011-02-21 18:16:01

I'm in favor of the following third option:

  1. The first thing that `sage-update` should do is to commit any outstanding changes and, in particular, abort if there is a patch queue applied. So you are safe even if you forgot to commit your changes.
  1. Then `sage-update` overwrites some critical files for its operation. 
  1. Finally, the `sage_root` spkg is installed and its `spkg-install` overwrites the remaining non-critical files in the root repository. I'd rather be guaranteed to have a clean slate after update than dying in the middle of the update because the attempted merge fails.

So if you had any uncommitted changes before updating, you'll end up with two commit messages. The more individual commits the better. The only drawback is that if you had made modifications to the root repository that you want to keep and you are not using patch queues, then you now have to extract your changes as a patch from the repository and apply that patch. I think thats acceptable since, I think, most developers use patch queues and I don't expect too frequent edits to the root repository.

If that doesn't convince you, I'd prefer option number 1 as my second choice :-)


---

Comment by jhpalmieri created at 2011-02-21 20:42:12

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-02-21 20:42:12

Here is a new version of the scripts patch.  The only change is in `sage-update`.  I updated the instructions, also: I'm not worrying about making the repo compatible with older versions of Mercurial right now.


---

Comment by jhpalmieri created at 2011-02-21 20:46:22

Oh, also, I created some versions for testing upgrades:

 - http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.2.X0/
 - http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.2.X1/ (spkg/install changed)
 - http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.2.X2/ (Makefile changed)
 - http://sage.math.washington.edu/home/palmieri/misc/9433/sage-4.6.2.X3/ (Makefile and spkg/standard/deps changed)

The first of these is just 4.6.2.rc0 with the patches from this ticket applied.  In each of the other ones, one or two files have been modified, as indicated.  It's also worth testing by updating to the "X0" version, for example, then modifying a file tracked by the root repo (like README.txt) without committing the change, and then trying to update to "X1".  The update should abort.


---

Comment by jhpalmieri created at 2011-02-21 21:12:09

I made a few minor cosmetic changes in the patch, and right now, the upgrade paths I mentioned use the old version, not the new one.  I'll have them updated in a few minutes.


---

Comment by jhpalmieri created at 2011-02-21 21:23:17

Okay, everything's updated now.


---

Comment by jdemeyer created at 2011-02-24 14:01:37

I made new testing releases:

 1. http://boxen.math.washington.edu/home/release/sage-4.7.alpha0/: sage-4.6.2.rc1 + this ticket
 1. http://boxen.math.washington.edu/home/release/sage-4.7.alpha1/: sage-4.7.alpha0 + #10688 + [attachment:9433_testing.patch]

Upgrading sage-4.7.alpha0 -> sage-4.7.alpha1 succeeded this time.


---

Comment by vbraun created at 2011-02-24 20:57:54

I've tried the update and it works beautifully. 

I think there is still one problem: If the user has no .hgrc (like many non-developers trying to upgrade), then mercurial will fail to commit with 

```
[vbraun`@`volker-desktop sage-4.7.alpha0]$ mv ~/.hgrc ~/backup.hgrc
[vbraun`@`volker-desktop sage-4.7.alpha0]$ hg commit -m "test"
abort: no username supplied (see "hg help config")
```

So whenever we commit to the root repo, we should specify a username explicitly. For example,

```
hg commit -u "committed by sage -upgrade" -m "test"
```



---

Comment by jhpalmieri created at 2011-02-25 05:45:24

patch for scripts repo


---

Attachment

The file $SAGE_ROOT/spkg/root-spkg-install


---

Attachment

Replying to [comment:153 vbraun]:
> I think there is still one problem: If the user has no .hgrc (like many non-developers trying to upgrade), then mercurial will fail

I wouldn't have spotted this.  Good catch.  I have new patches which add "-u ..." to various commit commands: in sage-update and in root-spkg-install.  I haven't bothered with sage-sdist or sage-make_devel_packages, since these are done by the release manager who had better have a .hgrc file.  (Besides, there are already other "hg commit" commands in those scripts.)

I've also updated my versions (4.6.2.X0 etc.) for testing upgrades with these changes.


---

Comment by vbraun created at 2011-02-25 17:46:46

I'm happy with it now. I tested upgrades without `~/.hgrc` and everything worked for me.


---

Comment by vbraun created at 2011-02-25 17:46:46

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-02-26 10:40:19

Agreed!  This will get merged in sage-4.7.alpha0.  I still expect breakage here and there, but that's what alpha versions are for.


---

Comment by jdemeyer created at 2011-03-08 21:44:36

Resolution: fixed
