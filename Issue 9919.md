# Issue 9919: Ease SageNB development by providing hg commands, and extracting packages to /devel

Issue created by migration from https://trac.sagemath.org/ticket/9920

Original creator: timdumol

Original creation time: 2010-09-16 15:48:08

Assignee: jason, was

CC:  jason kcrisman

Jason Grout commented on #9822 about the relative difficulty/inconvenience of developing and applying patches for SageNB as compared to Sage. This ticket should fix it.


---

Attachment

SageNB package. Extracts SageNB to $SAGE_ROOT/devel/ for ease of use.


---

Attachment

Sage main library. Adds hg_sagenb.


---

Comment by timdumol created at 2010-09-16 16:59:56

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-09-16 16:59:56

Patches attached.


---

Comment by jason created at 2010-09-24 00:32:09

Does this mean that I should be using spkg-dist to make the spkg, instead of sage -spkg?

Also, does this set things up so that changes are reflected in the running notebook server?  It seems that the spkg-dist just copies the hg repository there, but the notebook install is completely different.


---

Attachment

Puts the "$SAGE_ROOT/devel/sagenb" in `develop` mode.


---

Comment by timdumol created at 2010-09-24 07:03:49

Replying to [comment:2 jason]:
> Does this mean that I should be using spkg-dist to make the spkg, instead of sage -spkg?
> 

Yes. That has been the case for a long time (c.f. SPKG.txt)

> Also, does this set things up so that changes are reflected in the running notebook server?  It seems that the spkg-dist just copies the hg repository there, but the notebook install is completely different.

I neglected to add that. Thanks for the notification. This new patch should fix it.


---

Comment by jason created at 2010-09-28 19:15:46

Very nice!  This seems to work well.


---

Comment by jason created at 2010-09-28 19:15:46

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-09-28 19:16:12

I'll start reviewing more notebook patches when this spkg is incorporated into sage!


---

Comment by mpatel created at 2010-10-03 10:41:17

Changing status from positive_review to needs_info.


---

Comment by mpatel created at 2010-10-03 10:41:17

The extcode, sage_scripts, and sage packages use Mercurial in their `spkg-install`s to merge changes into an existing repository.  This could be more efficient than copying every file every time.  Can we do that here?

Does the new `spkg-install` now install SageNB two places, under `site-packages` and `devel`?  Is it practical to do just the latter?


---

Comment by jason created at 2010-10-04 11:50:40

Replying to [comment:6 mpatel]:
> The extcode, sage_scripts, and sage packages use Mercurial in their `spkg-install`s to merge changes into an existing repository.  This could be more efficient than copying every file every time.  Can we do that here?

Can we make a new ticket for that?

In fact, I like this approach better (backup and copy), since it plays nicely with patch queues.  The merge approach messes everything up if you forgot to pop all of your patches off.

> 
> Does the new `spkg-install` now install SageNB two places, under `site-packages` and `devel`?  Is it practical to do just the latter?


No, I don't think it installs twice (you can check the files to make sure).  The setup.py develop installs under $SAGE_ROOT/devel/ and changes the site-packages folder to refer to that location.


---

Comment by timdumol created at 2010-10-04 13:34:11

Replying to [comment:7 jason]:
> Replying to [comment:6 mpatel]:
> > The extcode, sage_scripts, and sage packages use Mercurial in their `spkg-install`s to merge changes into an existing repository.  This could be more efficient than copying every file every time.  Can we do that here?
> 
> Can we make a new ticket for that?
> 
> In fact, I like this approach better (backup and copy), since it plays nicely with patch queues.  The merge approach messes everything up if you forgot to pop all of your patches off.

I agree with Jason.

> 
> > 
> > Does the new `spkg-install` now install SageNB two places, under `site-packages` and `devel`?  Is it practical to do just the latter?
> 
> 
> No, I don't think it installs twice (you can check the files to make sure).  The setup.py develop installs under $SAGE_ROOT/devel/ and changes the site-packages folder to refer to that location.

Actually, it does, but doing so is needed for the docs to show (static docs). We can make another ticket for that.


---

Comment by jason created at 2010-10-05 02:24:04

Changing status from needs_info to needs_review.


---

Comment by jason created at 2010-10-05 02:24:04

I think both questions were answered, so I'm setting this back to positive review.  It would be *fantastic* if it were included in the sagenb package for the next release.


---

Comment by jason created at 2010-10-05 02:24:16

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-10-05 03:17:25

By the way, another issue for another ticket: updating [the developer's guide](http://sagemath.org/doc/developer/producing_patches.html#using-mercurial-with-other-sage-repositories) to include sagenb in the list of Mercurial repositories.


---

Comment by mpatel created at 2010-10-05 03:44:50

Sounds good.  Thanks for the information.  I'll add this to SageNB 0.8.4 at #10036.


---

Comment by mpatel created at 2010-10-06 03:33:58

Resolution: fixed


---

Comment by mpatel created at 2010-10-07 10:52:33

There's a problem with compiling from scratch, because `$SAGE_ROOT/devel` does not exist when `sagenb-*.spkg` is installed.  I think doing `mkdir -p` will be enough.

Can someone add a new patch to fix this?


---

Comment by mpatel created at 2010-10-07 11:30:43

Make `$SAGE_ROOT/devel` on install, if necessary.  Apply on top of package extraction patch.


---

Attachment

I've added a patch that I'm testing now.


---

Comment by mpatel created at 2010-10-07 12:29:52

Replying to [comment:17 mpatel]:
> I've added a patch that I'm testing now.

It works.


---

Comment by mpatel created at 2010-10-07 12:51:15

I think we'll need to open a new ticket for making this link

```
ln -sf "$SAGE_ROOT/devel/sagenb-main" "$SAGE_ROOT/devel/sagenb" 
```

relative.  Otherwise, Sage won't start after I move/rename the root directory.


---

Comment by mpatel created at 2010-10-07 12:53:46

And maybe also add `python setup.py develop` to `SAGE_LOCAL/bin/sage-location`?


---

Comment by mpatel created at 2010-10-07 22:03:53

Replying to [comment:20 mpatel]:
> And maybe also add `python setup.py develop` to `SAGE_LOCAL/bin/sage-location`?

See #10097.
