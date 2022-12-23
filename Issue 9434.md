# Issue 9434: Stop greping for a non-existent sage-banner

Issue created by migration from https://trac.sagemath.org/ticket/9434

Original creator: drkirkby

Original creation time: 2010-07-06 06:50:04

Assignee: GeorgSWeber

CC:  jhpalmieri

In install.log, we often see:


```
drkirkby@hawk:~/f/sage-4.5.alpha3$ grep sage-banner install.log
grep: can't open /export/home/drkirkby/f/sage-4.5.alpha3/local/bin/sage-banner
grep: can't open /export/home/drkirkby/f/sage-4.5.alpha3/local/bin/sage-banner
grep: can't open /export/home/drkirkby/f/sage-4.5.alpha3/local/bin/sage-banner
grep: can't open /export/home/drkirkby/f/sage-4.5.alpha3/local/bin/sage-banner
sage_scripts-4.5.alpha3/.hg/store/data/sage-banner.i
sage_scripts-4.5.alpha3/sage-banner
drkirkby@hawk:~/f/sage-4.5.alpha3$ 
```


I think this is probably due to some code in sage-sage


```
if [ "$1" = '-v' -o "$1" = '-version' -o "$1" = '--version' ]; then
    cat "$SAGE_LOCAL/bin/sage-banner" | grep -i "version" | sed "s/\| //" | sed "s/ *\|//"
    exit $?
fi
```


This will obviously fail if sage-banner does not exist. 

Also
 * There is an useless use of 'cat'. Perhaps the author was hoping to get a [Useless Use of Cat Award](http://partmaps.org/era/unix/award.html) (Well worth a read - it's both funny and educational.) 
 * There is an an unnecessary use of double-quotes around 'version'. 

The following will save a few bytes of disk space and a few CPU cycles, as it will invoke one less process. 


```
    grep -i version "$SAGE_LOCAL/bin/sage-banner" | sed "s/\| //" | sed "s/ *\|//"
```


More importantly, we should check that sage-banner exists before doing this, so it does not produce potentially confusing error messages. 

Dave 


---

Comment by leif created at 2010-07-06 11:38:39

Well, reading carefully, your error messages can't come from `sage-sage`... (I know you haven't had much sleep... ;-) )

Btw, there are more superfluous quotes.

If you want to save another "redundant" process invocation (there are in general many), at the expense of losing some parallelism, substitute

```
... | sed "s/\| //" | sed "s/ *\|//"
```

by

```
... | sed -e "s/\| //" -e "s/ *\|//"
```


(The whole line could be replaced by a single invocation of `sed`.)


---

Comment by leif created at 2010-07-10 05:47:35

Just for the record:

```sh
grep -c "^grep:" install.log
```

gives me zero for both sequential and parallel builds of Sage 4.5.alpha4 (Ubuntu 9.04).


---

Comment by drkirkby created at 2010-07-10 06:45:20

Changing assignee from GeorgSWeber to drkirkby.


---

Comment by drkirkby created at 2010-07-10 06:45:20

Hi leif
 * I was not aware of that shorter sed sequence. I just found the 'cat' a bit amuzing. 
 * Yes, there are loads of unneeded quotes in this bit of Sage. 
 * Interesting that you don't see this error message - I'm not the only one that gets it. I forget who posted the log with this, and commented on it, but someone did. 

I'll have to look at this, but its not exactly the most serious Sage bug. 

Dave


---

Comment by leif created at 2010-07-10 09:14:39

Replying to [comment:3 drkirkby]:
>  * I was not aware of that shorter sed sequence. I just found the 'cat' a bit amuzing.

Yes, though I love cats. One of my favorites is:

```sh
sed -n "/[Vv]ersion/s/ *| *//gp" $SAGE_LOCAL/bin/sage-banner
```

(Spaces in `$SAGE_LOCAL` are forbidden, otherwise we'd need quotes there.)

Note that the original version gives two lines for non-finals; it does *not* remove the vertical bars (nor the whitespace) because the pipe symbol is "superfluously" escaped: :)

```sh
leif64@portland:~/Sage/sage-4.5.alpha4-serial$ ./sage -v
* Warning: this is a prerelease version, and it may be unstable.     *
```

| Sage Version 4.5.alpha4, Release Date: 2010-07-06                  |
More important, the discussion is still somewhat off-topic or off-ticket, since - as mentioned - the error messages do not originate from `sage-sage`, so the issue has to be fixed elsewhere.

> I'll have to look at this, but its not exactly the most serious Sage bug.

Obviously, I agree.


---

Comment by leif created at 2010-07-12 23:10:56

I think I've found the _real_ culprit:

```sh
    # Mark that the new package has been installed. 
    # This file will eventually be a certificate like in OS X.
    echo "PACKAGE NAME: $PKG_NAME" > "$PKG_NAME"
    echo "INSTALL DATE: `date`" >> "$PKG_NAME"
    echo "UNAME: `uname -a`" >> "$PKG_NAME"
    echo "Sage VERSION: `grep Sage $SAGE_LOCAL/bin/sage-banner`" >> "$PKG_NAME"
    echo "Successfully installed $PKG_NAME"
```

(This is from `sage-spkg`.)


---

Comment by drkirkby created at 2010-07-12 23:24:53

Replying to [comment:5 leif]:
> I think I've found the _real_ culprit:
> {{{
> #!sh
>     # Mark that the new package has been installed. 
>     # This file will eventually be a certificate like in OS X.
>     echo "PACKAGE NAME: $PKG_NAME" > "$PKG_NAME"
>     echo "INSTALL DATE: `date`" >> "$PKG_NAME"
>     echo "UNAME: `uname -a`" >> "$PKG_NAME"
>     echo "Sage VERSION: `grep Sage $SAGE_LOCAL/bin/sage-banner`" >> "$PKG_NAME"
>     echo "Successfully installed $PKG_NAME"
> }}}
> (This is from `sage-spkg`.)


Yes, it looks like you have. It seems the author was not trying to win a [Useless Use of Cat Award](http://partmaps.org/era/unix/award.html). 

Do you have any idea why some people do not see this error message? If you can produce a patch, I can test it. 

Dave


---

Comment by jhpalmieri created at 2010-07-12 23:38:43

Since sage-spkg is in spkg/base and in sage_scripts, while sage-banner is only in sage_scripts, you should see this message for any spkgs installed before sage-scripts.  In the most recent version of Sage, deps should install sage_scripts right at the beginning:

```
BASE = $(INST)/$(PREREQ) $(INST)/$(DIR) $(INST)/$(SAGE_BZIP2)

# Also install scripts before we continue with other spkgs
BASE += $(INST)/$(SAGE_SCRIPTS)
```

So I hope this problem has already been taken care of.  Installing sage_scripts itself looks like the only possible problem.


---

Comment by leif created at 2010-07-12 23:58:23

Replying to [comment:6 drkirkby]:
> If you can produce a patch, I can test it.

Milestone: Sage 5.0 ;-)

I think a file containing (just) the Sage version number should be in `$SAGE_ROOT` anyhow; then we could `cat` that. (Testing for the existence of files is though not a bad idea...)


---

Comment by jhpalmieri created at 2010-09-29 21:03:36

Here's an attempt at fixing this.  Three comments: 

 - It stores the current Sage version in SAGE_ROOT/VERSION.txt, as suggested by Leif -- see #9922.
 - Right now, upgrading just adds the new version to the top, with "Updated from" and then the old version, so if you've somehow managed to update 6 times, the file will have 7 lines in it, recording the full update history.
 - It uses cat.  Sorry, Dave.


---

Comment by jhpalmieri created at 2010-09-29 21:03:36

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-09-29 21:08:31

To be more precise: with the patch, in a non-upgrade, the file SAGE_ROOT/VERSION.txt will look like this:

```
Sage version: 4.6.alpha2, Release date: 2010-09-29
```

I haven't tested the upgrade script yet, but it should produce

```
Sage version: 4.6.alpha2, Release date: 2010-09-29
Upgraded from Sage version: 4.6.alpha1, Release date: 2010-09-18
Upgraded from ...
```



---

Comment by leif created at 2010-09-29 21:27:16

Hmmm, besides I don't like the date format string (which is _local_ time), I don't think `$SAGE_RELEASE_DATE` is available (i.e. set) in `sage-upgrade`.

Do you intentionally export `OLD_VERSION`?

A non-existing `$SAGE_ROOT/VERSION.txt` could be handled as well.

I'd prefer having _"Sage version: ... [Last] Upgraded from: ..."_ on a single line (at least in the log).


---

Comment by leif created at 2010-09-29 21:37:59

You could use

```sh
    ...
    if [ -f "$SAGE_ROOT/VERSION.txt" ]; then
        sed -i -e "1iSage version: $SAGE_VERSION, Release date: $SAGE_RELEASE_DATE\nUpdated from $OLD_VERSION"
    else
        ...
```

to avoid `cat` ... ;-)

(Perhaps omit the newline, i.e. replace it by e.g. two spaces.)


---

Comment by leif created at 2010-09-29 21:42:08

And we'd have to make sure the version file doesn't get overwritten later once we have the root repo.


---

Comment by jhpalmieri created at 2010-09-29 22:09:28

Replying to [comment:11 leif]:
> Hmmm, besides I don't like the date format string (which is _local_ time), I don't think `$SAGE_RELEASE_DATE` is available (i.e. set) in `sage-upgrade`.
> 
> Do you intentionally export `OLD_VERSION`?

Right, I'll fix these.

> A non-existing `$SAGE_ROOT/VERSION.txt` could be handled as well.
> 
> I'd prefer having _"Sage version: ... [Last] Upgraded from: ..."_ on a single line (at least in the log).

Note that the Sage version doesn't appear in the log: it should only appear in the files in spkg/installed/.  But maybe a single line is cleaner.

> And we'd have to make sure the version file doesn't get overwritten later once we have the root repo.

We can add VERSION.txt to .hgignore; I think that should do it.


---

Comment by jhpalmieri created at 2010-09-29 22:11:31

scripts repo


---

Attachment

The new patch also modifies sage-make_devel_packages: when preparing the scripts package, it no longer indiscriminately copies all *.txt files from SAGE_ROOT into the scripts spkg, it just copies COPYING.txt and README.txt.  (Thus it won't copy VERSION.txt.)


---

Comment by leif created at 2010-09-29 23:38:51

I wouldn't call `sage` in `sage-upgrade`. Also, `sage-spkg` is run before `sage-upgrade` updates `VERSION.txt`, so (just) the old version would be logged. (I consider the files in `spkg/installed/` also logs, though they have no `.log` extension.)

Rather than omitting `VERSION.txt` from the `sage_scripts` spkg, I would put the code to update (or better: not overwrite) an existing `VERSION.txt` in its `spkg-install`.

As noted, the version file should be updated _before_ `spkg/install` is called (and that's also before a new scripts spkg gets installed).

We'd have to extract the new version from some newly downloaded file. (This only works for later Sage versions anyway, unless we handle it in `spkg/install`, too.)

----

_"While you're at it"_<sup>TM</sup>, would you mind quoting more instances of `$SAGE_ROOT` etc.?


---

Comment by leif created at 2010-09-29 23:49:28

P.S.: See also #9905 (for the date format).


---

Comment by drkirkby created at 2010-09-30 05:17:15

Replying to [comment:12 leif]:
> You could use
> {{{
> #!sh
>     ...
>     if [ -f "$SAGE_ROOT/VERSION.txt" ]; then
>         sed -i -e "1iSage version: $SAGE_VERSION, Release date: $SAGE_RELEASE_DATE\nUpdated from $OLD_VERSION"
>     else
>         ...
> }}}
> to avoid `cat` ... ;-)
> 
> (Perhaps omit the newline, i.e. replace it by e.g. two spaces.)
> 

But that would be an even bigger mistake than to use an unnecessary cat, as you are making use of non-POSIX options to `sed` - see [POSIX specifiction of sed](http://www.opengroup.org/onlinepubs/009695399/utilities/sed.html) I can guarantee that will fail on Solaris and AIX and probably other Unix systems too. 

Dave


---

Comment by jhpalmieri created at 2010-09-30 05:46:49

Replying to [comment:17 leif]:
> I wouldn't call `sage` in `sage-upgrade`. 

I can see from your other reasons that we need to update the version number earlier so my solution won't work, but I see no reason, a priori, not to call `sage` in `sage-upgrade`, after the upgrade process has completed, apparently successfully.  It actually tests further whether the upgrade succeeded.

> Also, `sage-spkg` is run before `sage-upgrade` updates `VERSION.txt`, so (just) the old version would be logged. (I consider the files in `spkg/installed/` also logs, though they have no `.log` extension.)

That makes sense.

> Rather than omitting `VERSION.txt` from the `sage_scripts` spkg, I would put the code to update (or better: not overwrite) an existing `VERSION.txt` in its `spkg-install`.

Why?  In general, copying over all *.txt files is a little dangerous, and is part of the reason that the file sage-README-osx.txt appears in the wrong places and isn't currently tracked in any repo.  I think if we want to include a file, it should be tracked.  If it's automatically generated, I don't see any reason to include it in a repo.  If #9433 ever gets reviewed and merged, then all of the *.txt files in SAGE_ROOT will be taken out of the scripts repo in any case.

> As noted, the version file should be updated _before_ `spkg/install` is called (and that's also before a new scripts spkg gets installed).

Right.

> We'd have to extract the new version from some newly downloaded file. (This only works for later Sage versions anyway, unless we handle it in `spkg/install`, too.)

How about extracting it from VERSION.txt?  I'm attaching a patch which does this, perhaps not in the optimal way, but I think it should work.

> _"While you're at it"_<sup>TM</sup>, would you mind quoting more instances of `$SAGE_ROOT` etc.?

I don't have time to do this now.


---

Comment by jhpalmieri created at 2010-09-30 05:49:53

I also didn't change the date format.  I wasn't sure exactly what you meant; if you're not happy with the date format in a line like 

```
INSTALL DATE: Tue Sep 21 12:48:53 PDT 2010
```

from a file in spkg/installed, I didn't touch any of that code, and I don't have time to deal with it now.  I think for a release date, we don't need anything more precise than `2010-09-29`: no hours, minutes, second, or time zone.


---

Comment by leif created at 2010-09-30 06:36:08

Replying to [comment:21 jhpalmieri]:
> I also didn't change the date format.  I wasn't sure exactly what you meant; if you're not happy with the date format in a line like 
> {{{
> INSTALL DATE: Tue Sep 21 12:48:53 PDT 2010
> }}}
> from a file in spkg/installed, I didn't touch any of that code,

I didn't mean that. (At least not for this ticket, since #9905 addresses this.)

> I think for a release date, we don't need anything more precise than `2010-09-29`: no hours, minutes, second, or time zone.

It should simply be UTC. (`date -u +"%Y-%m-%d"` or better `date -u +"%Y-%m-%d %Z"` to include "UTC". One could also print the UTC verbatim, without `%Z`...)


---

Comment by leif created at 2010-09-30 06:59:43

Replying to [comment:20 jhpalmieri]:
> Replying to [comment:17 leif]:
> > I wouldn't call `sage` in `sage-upgrade`. 
> 
> I can see from your other reasons that we need to update the version number earlier so my solution won't work, but I see no reason, a priori, not to call `sage` in `sage-upgrade`,

`sage-upgrade` isn't "the end" of the upgrade process (it's called by `sage-sage`),
and calling the "new" Sage there can potentially cause more trouble than we want. So since it's not necessary, I would leave it.

> after the upgrade process has completed, apparently successfully.  It actually tests further whether the upgrade succeeded.

This is done later, and finally calling the new Sage should be up to the user, e.g. indirectly by building the documentation.

> > Rather than omitting `VERSION.txt` from the `sage_scripts` spkg, I would put the code to update (or better: not overwrite) an existing `VERSION.txt` in its `spkg-install`.
> 
> Why?  In general, copying over all *.txt files is a little dangerous, and is part of the reason that the file sage-README-osx.txt appears in the wrong places and isn't currently tracked in any repo.

I didn't say copy `*.txt` (otherwise checking the presence of an existing `$SAGE_ROOT/VERSION.txt` wouldn't make much sense). But having it there (_not_ in the repo, i.e., in `.hgignore`) we can easily extract it before that spkg gets installed, because a new scripts repo is always there, is relatively small and gets created by `sage -sdist` anyway, where the new version and release date are known.
 
> I think if we want to include a file, it should be tracked.  If it's automatically generated, I don't see any reason to include it in a repo.

See above.

> If #9433 ever gets reviewed and merged, then all of the *.txt files in SAGE_ROOT will be taken out of the scripts repo in any case.

Well, `VERSION.txt` shouldn't be under revision control.
 
> > As noted, the version file should be updated _before_ `spkg/install` is called (and that's also before a new scripts spkg gets installed).
> 
> Right.
> 
> > We'd have to extract the new version from some newly downloaded file. (This only works for later Sage versions anyway, unless we handle it in `spkg/install`, too.)
> 
> How about extracting it from VERSION.txt?

Extracting the file from the file itself? You misunderstood me. I meant we could extract `VERSION.txt` e.g. from the scripts repo, with `tar`.

> I'm attaching a patch which does this, perhaps not in the optimal way, but I think it should work.

I'll take a look at it.


---

Comment by drkirkby created at 2010-09-30 07:06:16

Although I'm aware of the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) date format, for humans to read, having the month (Jan, Feb etc) and day (Mon, Tue etc) is useful. It's obvious that 2001 is the year, but things like 2010-05-06 are not so good for human readability. Is that the the 5th of June or the 6th of May? It's more confusing, as different parts of the world use different order for the month and day. 

One other thing, that I'll mention though this is perhaps not the best ticket for it, is  #8447, which was a suggestion of mine to detect when the Sage version is old. Having the release date stored as seconds since the Epoch (in addition to a human friendly way), would enable us to detect when Sage is old. So I suggest anywhere one adds a release date, we bear that in mind. 

BTW John, I've nothing against the use of `cat` as sometimes it is needed, but things like 

`cat filename | grep foobar`

are a bit silly when 

`grep foobar filename`

will work, is shorter, and does not create an extra process. 

I've got to submit a job application today, so doing lots with Sage is not on my priority list today. Hence I wont be reviewing things for the rest of the day. 

dave


---

Comment by leif created at 2010-09-30 07:20:44

Replying to [comment:23 leif]:
> Replying to [comment:20 jhpalmieri]:
> > I'm attaching a patch which does this, perhaps not in the optimal way, but I think it should work.
> 
> I'll take a look at it.

Ok, if we supply a separate file in the upgrade path. The code is a _bit_ complicated though.


---

Comment by leif created at 2010-09-30 07:42:06

Replying to [comment:24 drkirkby]:
> Although I'm aware of the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) date format, for humans to read, having the month (Jan, Feb etc) and day (Mon, Tue etc) is useful.

That depends on the locale and isn't easily sortable or grepable. (I thought you had to deal with airlines; you know every date is always UTC there, regardless of any daylight saving or whatever.)

> It's obvious that 2001 is the year, but things like 2010-05-06 are not so good for human readability. Is that the the 5th of June or the 6th of May?

I'm aware there are some <censored> people writing 2010/28/02, but with slashes, not dashes.


> One other thing, that I'll mention though this is perhaps not the best ticket for it, is  #8447, which was a suggestion of mine to detect when the Sage version is old. Having the release date stored as seconds since the Epoch (in addition to a human friendly way), would enable us to detect when Sage is old. So I suggest anywhere one adds a release date, we bear that in mind.

Detecting such is easier with the date format we have. ;-)

But I'm strongly against nagging or annoying users, especially since the default is to print the Sage banner when Sage starts up, which shows the release date.


---

Comment by drkirkby created at 2010-09-30 07:59:14

Replying to [comment:26 leif]:

> > One other thing, that I'll mention though this is perhaps not the best ticket for it, is  #8447, which was a suggestion of mine to detect when the Sage version is old. Having the release date stored as seconds since the Epoch (in addition to a human friendly way), would enable us to detect when Sage is old. So I suggest anywhere one adds a release date, we bear that in mind.
> 
> Detecting such is easier with the date format we have. ;-)
> 
> But I'm strongly against nagging or annoying users, especially since the default is to print the Sage banner when Sage starts up, which shows the release date. 
>  

If we nagged users their version of Sage was very old, we would not have the problems there are with the Debian distribution, and some other distributions of Sage. I think more than a year old and you do seriously need to nag them! 

Dave


---

Comment by jhpalmieri created at 2010-09-30 15:10:58

Replying to [comment:23 leif]:
> Replying to [comment:20 jhpalmieri]:
> > Replying to [comment:17 leif]:
> > > I wouldn't call `sage` in `sage-upgrade`. 
> > 
> > I can see from your other reasons that we need to update the version number earlier so my solution won't work, but I see no reason, a priori, not to call `sage` in `sage-upgrade`,
> 
> `sage-upgrade` isn't "the end" of the upgrade process (it's called by `sage-sage`),
> and calling the "new" Sage there can potentially cause more trouble than we want. So since it's not necessary, I would leave it.
> 
> > after the upgrade process has completed, apparently successfully.  It actually tests further whether the upgrade succeeded.
> 
> This is done later

Where?  sage-upgrade gets called twice in sage-sage, but that's basically all that happens when you run "sage -upgrade", isn't it?  I guess running it twice means that VERSION.txt may end up being wrong; I'll have to fix that.

> , and finally calling the new Sage should be up to the user, e.g. indirectly by building the documentation.
> 
> > > Rather than omitting `VERSION.txt` from the `sage_scripts` spkg, I would put the code to update (or better: not overwrite) an existing `VERSION.txt` in its `spkg-install`.
> > 
> > Why?  In general, copying over all *.txt files is a little dangerous, and is part of the reason that the file sage-README-osx.txt appears in the wrong places and isn't currently tracked in any repo.
> 
> I didn't say copy `*.txt` (otherwise checking the presence of an existing `$SAGE_ROOT/VERSION.txt` wouldn't make much sense). But having it there (_not_ in the repo, i.e., in `.hgignore`) we can easily extract it before that spkg gets installed, because a new scripts repo is always there, is relatively small and gets created by `sage -sdist` anyway, where the new version and release date are known.

VERSION.txt is written to SAGE_ROOT by sage-sdist, so it's present in the Sage tarball.  It will therefore also be available in the upgrade path.

> > I think if we want to include a file, it should be tracked.  If it's automatically generated, I don't see any reason to include it in a repo.
> 
> See above.
> 
> > If #9433 ever gets reviewed and merged, then all of the *.txt files in SAGE_ROOT will be taken out of the scripts repo in any case.
> 
> Well, `VERSION.txt` shouldn't be under revision control.
>  
> > > As noted, the version file should be updated _before_ `spkg/install` is called (and that's also before a new scripts spkg gets installed).
> > 
> > Right.
> > 
> > > We'd have to extract the new version from some newly downloaded file. (This only works for later Sage versions anyway, unless we handle it in `spkg/install`, too.)
> > 
> > How about extracting it from VERSION.txt?
> 
> Extracting the file from the file itself? You misunderstood me. I meant we could extract `VERSION.txt` e.g. from the scripts repo, with `tar`.

Although we can't get the release date from it, we could also use the _file name_ for the main Sage repo, for example.

> > I'm attaching a patch which does this, perhaps not in the optimal way, but I think it should work.
> 
> I'll take a look at it.

Replying to [comment:25 leif]:
> Ok, if we supply a separate file in the upgrade path. 

(See above: the file VERSION.txt gets written to SAGE_ROOT by sage-sdist, so it will be there.)

> The code is a _bit_ complicated though.

It's straightforward, but long: first you extract the old version from VERSION.txt, then you download the new VERSION.txt and extract the new version, then you produce the updated VERSION.txt.  I need to check whether the new version matches the beginning of the old version, in case this is the second time sage-upgrade is run.  

Finally, I think having "UTC" at the end of the date looks a little silly when it's just a date, no time, but I've included it.

Here's a new patch.


---

Comment by jdemeyer created at 2010-11-11 20:21:41

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-11-11 20:21:41

This needs to be rebased (and perhaps coordinated with #9433?):

```
patching file sage-make_devel_packages
patching file sage-sdist
patching file sage-spkg
patching file sage-update
Hunk #1 succeeded at 344 (offset 35 lines).
Hunk #2 FAILED at 380.
1 out of 2 hunks FAILED -- saving rejects to file sage-update.rej
patching file sage-upgrade
Hunk #1 succeeded at 35 (offset 4 lines).
```



---

Attachment

version 2: replaces earlier patch. scripts repo


---

Comment by jhpalmieri created at 2010-11-11 21:03:41

Here's a rebased version.  As far as coordinating with #9433, some rebasing may be required, and I can add "VERSION.txt" to the .hgignore file in the new Sage repo.  I'll make the change to .hgignore now, but I'm going to wait for any rebasing until one or the other ticket has at least a positive review.


---

Comment by jhpalmieri created at 2010-11-11 21:03:41

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-11-26 12:35:29

Replying to [comment:28 jhpalmieri]:
> Finally, I think having "UTC" at the end of the date looks a little silly when it's just a date, no time.

I agree, this should be removed.  This just looks so strange:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage:
```

| Sage Version 4.6.1.alpha3, Release Date: 2010-11-26 UTC            |
| Type notebook() for the GUI, and license() for information.        |
The patch looks okay to me (apart from this minor UTC issue).  I will do some more testing (also upgrade).


---

Attachment

Reviewer scripts patch, apply on top of previous


---

Comment by jdemeyer created at 2010-11-26 22:43:41

Changing keywords from "" to "scripts VERSION.txt".


---

Comment by jdemeyer created at 2010-11-26 22:43:41

positive_review to everything except for my patch.


---

Comment by drkirkby created at 2010-11-27 00:19:41

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-11-27 00:19:41

Replying to [comment:32 jdemeyer]:
> positive_review to everything except for my patch.

I'm giving a positive review to your patch, and so setting this to positive review.


---

Comment by jdemeyer created at 2010-12-02 16:09:12

Resolution: fixed


---

Comment by mpatel created at 2010-12-08 17:17:17

I've reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/461c1eeb61cc6f45/56108269d1090223?#56108269d1090223) a _possible_ problem involving `VERSION.txt` and failed upgrades.


---

Comment by mpatel created at 2010-12-14 04:16:55

Replying to [comment:35 mpatel]:
> I've reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/461c1eeb61cc6f45/56108269d1090223?#56108269d1090223) a _possible_ problem involving `VERSION.txt` and failed upgrades.

Does `download_file("VERSION.txt")` attempt to download a non-existent file, e.g.,

 http://sage.math.washington.edu/home/release/sage-4.6.1.alpha3/sage-4.6.1.alpha3/spkg/VERSION.txt

?  The successful upgrades I've done from 4.6 to 4.6.1.alpha3 somehow avoid this problem --- after the upgrade, `SAGE_ROOT` does not contain a `VERSION.txt`.  But upgrades that failed I cannot resume:

```
$ ./sage -upgrade http://sage.math.washington.edu/home/release/sage-4.6.1.alpha3/sage-4.6.1.alpha3
[...]
http://sage.math.washington.edu/home/release/sage-4.6.1.alpha3/sage-4.6.1.alpha3/spkg/VERSION.txt --> VERSION.txt [.]
Failed to download 'http://sage.math.washington.edu/home/release/sage-4.6.1.alpha3/sage-4.6.1.alpha3/spkg/VERSION.txt'.
Abort.
$ 
```



---

Comment by jhpalmieri created at 2010-12-14 06:53:57

> Does download_file("VERSION.txt") attempt to download a non-existent file

I think that might be the problem.  I thought we tested this with upgrades, but obviously not well enough.  How about a patch like this:

```diff
diff -r 6e07658dbbd6 -r b35cea7f82c9 sage-sdist
--- a/sage-sdist
+++ b/sage-sdist
@@ -58,6 +58,9 @@ cp -LRp Makefile *.txt *.sage sage ipyth
 STD=standard
 mkdir $TMP/$PKGDIR
 mkdir $TMP/$PKGDIR/$STD
+# Put VERSION.txt in a directory available for download during the
+# update process.  (See sage-update.)
+cp VERSION.txt $TMP/$PKGDIR/$STD/.VERSION.txt
 cp -p $PKGDIR/$STD/deps $TMP/$PKGDIR/$STD/
 cp -p $PKGDIR/$STD/libdist_filelist $TMP/$PKGDIR/$STD/
 cp -p $PKGDIR/$STD/newest_version $TMP/$PKGDIR/$STD/
diff -r 6e07658dbbd6 -r b35cea7f82c9 sage-update
--- a/sage-update
+++ b/sage-update
@@ -351,11 +351,16 @@ def do_update():
         version_file.close()
     else:
         old_version = ""
-    download_file("VERSION.txt")
-    version_file = open("VERSION.txt")
+    download_file("standard/.VERSION.txt")
+    version_file = open(".VERSION.txt")
     new_version = version_file.read()
     new_version = new_version.strip()  # remove trailing newline
     version_file.close()
+    try:
+        os.remove(os.path.join(SPKG_ROOT, "standard", ".VERSION.txt"))
+    except OSError:
+        pass
+    os.rename(".VERSION.txt", os.path.join(SPKG_ROOT, "standard", ".VERSION.txt"))
     # sage-upgrade, hence sage-update, gets run twice during the
     # upgrade process.  If old_version starts with new_version, then
     # this should be the second time through, so don't update the
```

(The "try ... except" block is probably not necessary except on Windows, but it feels safer this way, and who knows, we might eventually support Windows.)

I've created two upgrade paths which include this (one, version "V0", to test upgrading from anything else to this, and then the second, version "V1", to try upgrading from version "V0"):

 - [http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V0/](http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V0/)
 - [http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V1/](http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V1/)

We can open up a new ticket with a formally attached patch if this seems like the right approach.  I won't have much time to work on this, though: I have to focus on grading exams and getting ready for next quarter's classes.


---

Comment by jhpalmieri created at 2010-12-14 06:54:34

(This patch is to be applied on top of 4.6.1.alpha3.)


---

Comment by jdemeyer created at 2010-12-14 08:13:07

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2010-12-14 08:13:07

Changing status from closed to new.


---

Comment by jdemeyer created at 2010-12-14 08:13:07

Reopening this because of the issue mentioned.


---

Comment by jdemeyer created at 2010-12-14 08:13:07

Changing priority from minor to blocker.


---

Comment by mpatel created at 2010-12-14 15:25:07

Using `download_file("../VERSION.txt")` may also work (I've tested this only once).

For me, the upgrades that failed were parallel spkg builds.  But some parallel spkg upgrades did "succeed," i.e., modulo SageNB not being upgraded.  (Were there any other packages not upgraded?)
All purely serial and parallel-only-within-spkg upgrades "succeeded."

Could when the new `sage_scripts` package is installed matter for either the `VERSION.txt` discrepancy or the apparently separate SageNB problem?


---

Comment by jdemeyer created at 2010-12-14 16:05:11

Replying to [comment:40 mpatel]:
> Using `download_file("../VERSION.txt")` may also work (I've tested this only once).

If that's true, it's probably a better solution (but it needs to be tested properly).


---

Comment by jhpalmieri created at 2010-12-14 18:50:10

Replying to [comment:40 mpatel]:
> Using `download_file("../VERSION.txt")` may also work (I've tested this only once).

I would expect it to work from an upgrade path like the one I provided, or like the ones provided by release managers for alpha releases.  But if I try to download from a URL like "http://boxen.math.washington.edu/sage/spkg/../COPYING.txt", the file is not found.  I think the same would be true of VERSION.txt: I don't think the top-level directory is available on the official Sage mirrors.


---

Comment by jdemeyer created at 2010-12-14 19:15:15

Replying to [comment:42 jhpalmieri]:
> Replying to [comment:40 mpatel]:
> > Using `download_file("../VERSION.txt")` may also work (I've tested this only once).
> 
> I would expect it to work from an upgrade path like the one I provided, or like the ones provided by release managers for alpha releases.  But if I try to download from a URL like "http://boxen.math.washington.edu/sage/spkg/../COPYING.txt", the file is not found.

Well, the file is not found because it doesn't actually exist.  So your comment doesn't really prove anything.


---

Comment by jdemeyer created at 2010-12-14 19:27:18

I don't see any reason why [http://boxen.math.washington.edu/sage/spkg/../COPYING.txt](http://boxen.math.washington.edu/sage/spkg/../COPYING.txt) shouldn't work while John's URL works.


---

Comment by jdemeyer created at 2010-12-14 19:27:18

Changing status from new to needs_work.


---

Comment by jhpalmieri created at 2010-12-14 19:54:51

Replying to [comment:44 jdemeyer]:
> I don't see any reason why [http://boxen.math.washington.edu/sage/spkg/../COPYING.txt](http://boxen.math.washington.edu/sage/spkg/../COPYING.txt) shouldn't work while John's URL works.

I think that on the official Sage mirrors, none of the top-level files (makefile or Makefile, COPYING.txt, etc.) are available for download via the URLs in the sage-update script.  So if we have VERSION.txt only in the top-level, it won't be available for download (unless the scripts which make the official release available are rewritten). That is, after Sage 4.6.1 is released, running "sage -upgrade" with no arguments will fail to download VERSION.txt because that file won't be anywhere on the server.

I could be wrong, though.  Does anyone know for sure what files are mirrored on the official servers?  Browsing around the /home/sagemath directory on sage.math, for example the www-files subdirectory, I don't see 'makefile' anywhere...


---

Comment by jhpalmieri created at 2010-12-14 19:59:34

Here is the patch quoted above.  I think this will work, and I don't think that downloading "../VERSION.txt" will.  I'm marking it as needing review, but if anyone wants to try a different approach, please go ahead.


---

Comment by jhpalmieri created at 2010-12-14 19:59:34

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-12-14 20:12:45

Replying to [comment:45 jhpalmieri]:
> I could be wrong, though.  Does anyone know for sure what files are mirrored on the official servers?  Browsing around the /home/sagemath directory on sage.math, for example the www-files subdirectory, I don't see 'makefile' anywhere...

Does this mean that `Makefile` will never get upgraded?  That doesn't sound good, especially given #9799, #10156.


---

Comment by jhpalmieri created at 2010-12-14 23:01:09

Well, I think `Makefile` never gets run during an upgrade, so while it doesn't get upgraded, that doesn't affect the upgrade process.  I suppose if someone ran "sage -upgrade ..." and then did "make clean" and "make", it would use the old version of `Makefile` (or `makefile`), but the spkgs should be up to date.  (This is yet another reason to work on getting #9433 merged...)


---

Comment by leif created at 2010-12-16 03:38:16

Replying to [comment:35 mpatel]:
> I've reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/461c1eeb61cc6f45/56108269d1090223?#56108269d1090223) a _possible_ problem involving `VERSION.txt` and failed upgrades.

Just for the record (from IRC):

```
<kini>
  er... I just ran `sage -upgrade` (from 4.6) to see if it would pull a development version
  - sage told me that everything was already upgraded, and it exited without seeming to do
  anything but now when I load sage it's telling me I have 4.6.rc0
  odd
  curiouser and curiouser
  sage.misc.banner.banner() returns the correct, 4.6 banner
  ... hm
  so apparently `sage -version` just cats a text file,  $SAGE_ROOT/local/bin/sage-banner
  odd, my $SAGE_ROOT/local/bin repository's files are for some reason marked as descended
  from 4.6.rc0
  well, never mind
```


8)


---

Comment by jdemeyer created at 2010-12-16 09:02:22

1) Why not rename/copy the file "SAGE_ROOT/spkg/standard/.VERSION.txt" to "SAGE_ROOT/VERSION.txt" in `spkg-upgrade`?  That way, there will be a top-level `VERSION.txt` just like one would have with a clean build.

2) I would _not_ make the file hidden, I don't think there is a problem with a file `spkg/standard/VERSION.txt`.

3) I would copy using `cp -p`.


---

Comment by jdemeyer created at 2010-12-16 09:02:22

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-12-16 21:25:38

Replying to [comment:50 jdemeyer]:
> 1) Why not rename/copy the file "SAGE_ROOT/spkg/standard/.VERSION.txt" to "SAGE_ROOT/VERSION.txt" in `spkg-upgrade`?  That way, there will be a top-level `VERSION.txt` just like one would have with a clean build.

I agree that the top-level VERSION.txt should be the same as spkg/standard/VERSION.txt, which was not the case in my previous patch.  I've fixed that so that once the top-level file is created, it's copied to spkg/standard.  (The top-level file contains upgrade information, and since upgrade info may be helpful in tracking down problems, we should keep that one rather than the downloaded one.)

> 2) I would _not_ make the file hidden, I don't think there is a problem with a file `spkg/standard/VERSION.txt`.

Okay.
 
> 3) I would copy using `cp -p`.

Good idea.

I'm attaching two patches, one of which just fixes these issues.  The other patch, which could be applied on top of the others, does a little miscellaneous clean-up in sage-update, using `os.path.join(x,y)` instead of `"%s/%s" %(x,y)`.  Feel free to ignore the second patch completely; it is entirely optional right now.


---

Comment by jhpalmieri created at 2010-12-16 21:25:38

Changing status from needs_work to needs_review.


---

Attachment

scripts repo; apply on top of other patches


---

Attachment

scripts repo; this patch is optional, so reviewing it should have lower priority


---

Comment by jdemeyer created at 2010-12-17 14:20:20

The patches look good to me, but I need to do more testing before this can get positive review.


---

Comment by jhpalmieri created at 2010-12-17 16:28:59

I just created new upgrade paths for further testing: I took a vanilla version of 4.6.1.alpha3 and applied "trac_9434-VERSION-update.patch", then did "./sage -sdist 4.6.1.V0" and "./sage -sdist 4.6.1.V1".  Then I applied "trac_9434-os.path.join.patch" and did "./sage -sdist 4.6.1.W0" and "./sage -sdist 4.6.1.W1".  The resulting upgrade paths are

 -  http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V0/
 -  http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.V1/
 -  http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.W0/  (with os.path.join patch)
 -  http://sage.math.washington.edu/home/palmieri/misc/sage-4.6.1.W1/  (with os.path.join patch)


---

Comment by jdemeyer created at 2010-12-18 09:36:22

I'm also testing with the upgrade path [http://sage.math.washington.edu/home/release/sage-4.6.1.rc0/sage-4.6.1.rc0/](http://sage.math.washington.edu/home/release/sage-4.6.1.rc0/sage-4.6.1.rc0/) (including also other tickets such as #10176).

I currently get the following problem (building an "nameless" package), still investigating:

```
/mnt/usb1/scratch/jdemeyer/sage-4.6.1.rc0_upgraded/spkg/pipestatus "sage-spkg ${SAGE_SPKG_OPTS}  2>&1" "tee -a /mnt/usb1/scratch/jdemeyer/sage-4.6.1.rc0_upgraded/spkg/logs/.log"
```



---

Comment by jdemeyer created at 2010-12-19 09:33:33

Looks good to me ("merged" changed to rc0 because there is an additional patch).


---

Comment by jdemeyer created at 2010-12-19 09:33:33

Resolution: fixed
