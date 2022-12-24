# Issue 9919: Ease SageNB development by providing hg commands, and extracting packages to /devel

archive/issues_009919.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  jason kcrisman\n\nJason Grout commented on #9822 about the relative difficulty/inconvenience of developing and applying patches for SageNB as compared to Sage. This ticket should fix it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9920\n\n",
    "created_at": "2010-09-16T15:48:08Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Ease SageNB development by providing hg commands, and extracting packages to /devel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9919",
    "user": "timdumol"
}
```
Assignee: jason, was

CC:  jason kcrisman

Jason Grout commented on #9822 about the relative difficulty/inconvenience of developing and applying patches for SageNB as compared to Sage. This ticket should fix it.

Issue created by migration from https://trac.sagemath.org/ticket/9920





---

archive/issue_comments_098710.json:
```json
{
    "body": "Attachment [trac_9920-sagenb-package-extraction.patch](tarball://root/attachments/some-uuid/ticket9920/trac_9920-sagenb-package-extraction.patch) by timdumol created at 2010-09-16 16:57:37\n\nSageNB package. Extracts SageNB to $SAGE_ROOT/devel/ for ease of use.",
    "created_at": "2010-09-16T16:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98710",
    "user": "timdumol"
}
```

Attachment [trac_9920-sagenb-package-extraction.patch](tarball://root/attachments/some-uuid/ticket9920/trac_9920-sagenb-package-extraction.patch) by timdumol created at 2010-09-16 16:57:37

SageNB package. Extracts SageNB to $SAGE_ROOT/devel/ for ease of use.



---

archive/issue_comments_098711.json:
```json
{
    "body": "Attachment [trac_9920-sagelib-hg.patch](tarball://root/attachments/some-uuid/ticket9920/trac_9920-sagelib-hg.patch) by timdumol created at 2010-09-16 16:58:24\n\nSage main library. Adds hg_sagenb.",
    "created_at": "2010-09-16T16:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98711",
    "user": "timdumol"
}
```

Attachment [trac_9920-sagelib-hg.patch](tarball://root/attachments/some-uuid/ticket9920/trac_9920-sagelib-hg.patch) by timdumol created at 2010-09-16 16:58:24

Sage main library. Adds hg_sagenb.



---

archive/issue_comments_098712.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-16T16:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98712",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098713.json:
```json
{
    "body": "Patches attached.",
    "created_at": "2010-09-16T16:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98713",
    "user": "timdumol"
}
```

Patches attached.



---

archive/issue_comments_098714.json:
```json
{
    "body": "Does this mean that I should be using spkg-dist to make the spkg, instead of sage -spkg?\n\nAlso, does this set things up so that changes are reflected in the running notebook server?  It seems that the spkg-dist just copies the hg repository there, but the notebook install is completely different.",
    "created_at": "2010-09-24T00:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98714",
    "user": "jason"
}
```

Does this mean that I should be using spkg-dist to make the spkg, instead of sage -spkg?

Also, does this set things up so that changes are reflected in the running notebook server?  It seems that the spkg-dist just copies the hg repository there, but the notebook install is completely different.



---

archive/issue_comments_098715.json:
```json
{
    "body": "Attachment [trac_9920-sagenb-package-extraction.2.patch](tarball://root/attachments/some-uuid/ticket9920/trac_9920-sagenb-package-extraction.2.patch) by timdumol created at 2010-09-24 06:57:24\n\nPuts the \"$SAGE_ROOT/devel/sagenb\" in `develop` mode.",
    "created_at": "2010-09-24T06:57:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98715",
    "user": "timdumol"
}
```

Attachment [trac_9920-sagenb-package-extraction.2.patch](tarball://root/attachments/some-uuid/ticket9920/trac_9920-sagenb-package-extraction.2.patch) by timdumol created at 2010-09-24 06:57:24

Puts the "$SAGE_ROOT/devel/sagenb" in `develop` mode.



---

archive/issue_comments_098716.json:
```json
{
    "body": "Replying to [comment:2 jason]:\n> Does this mean that I should be using spkg-dist to make the spkg, instead of sage -spkg?\n> \n\nYes. That has been the case for a long time (c.f. SPKG.txt)\n\n> Also, does this set things up so that changes are reflected in the running notebook server?  It seems that the spkg-dist just copies the hg repository there, but the notebook install is completely different.\n\nI neglected to add that. Thanks for the notification. This new patch should fix it.",
    "created_at": "2010-09-24T07:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98716",
    "user": "timdumol"
}
```

Replying to [comment:2 jason]:
> Does this mean that I should be using spkg-dist to make the spkg, instead of sage -spkg?
> 

Yes. That has been the case for a long time (c.f. SPKG.txt)

> Also, does this set things up so that changes are reflected in the running notebook server?  It seems that the spkg-dist just copies the hg repository there, but the notebook install is completely different.

I neglected to add that. Thanks for the notification. This new patch should fix it.



---

archive/issue_comments_098717.json:
```json
{
    "body": "Very nice!  This seems to work well.",
    "created_at": "2010-09-28T19:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98717",
    "user": "jason"
}
```

Very nice!  This seems to work well.



---

archive/issue_comments_098718.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-28T19:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98718",
    "user": "jason"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098719.json:
```json
{
    "body": "I'll start reviewing more notebook patches when this spkg is incorporated into sage!",
    "created_at": "2010-09-28T19:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98719",
    "user": "jason"
}
```

I'll start reviewing more notebook patches when this spkg is incorporated into sage!



---

archive/issue_comments_098720.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2010-10-03T10:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98720",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_098721.json:
```json
{
    "body": "The extcode, sage_scripts, and sage packages use Mercurial in their `spkg-install`s to merge changes into an existing repository.  This could be more efficient than copying every file every time.  Can we do that here?\n\nDoes the new `spkg-install` now install SageNB two places, under `site-packages` and `devel`?  Is it practical to do just the latter?",
    "created_at": "2010-10-03T10:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98721",
    "user": "mpatel"
}
```

The extcode, sage_scripts, and sage packages use Mercurial in their `spkg-install`s to merge changes into an existing repository.  This could be more efficient than copying every file every time.  Can we do that here?

Does the new `spkg-install` now install SageNB two places, under `site-packages` and `devel`?  Is it practical to do just the latter?



---

archive/issue_comments_098722.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n> The extcode, sage_scripts, and sage packages use Mercurial in their `spkg-install`s to merge changes into an existing repository.  This could be more efficient than copying every file every time.  Can we do that here?\n\nCan we make a new ticket for that?\n\nIn fact, I like this approach better (backup and copy), since it plays nicely with patch queues.  The merge approach messes everything up if you forgot to pop all of your patches off.\n\n> \n> Does the new `spkg-install` now install SageNB two places, under `site-packages` and `devel`?  Is it practical to do just the latter?\n\n\nNo, I don't think it installs twice (you can check the files to make sure).  The setup.py develop installs under $SAGE_ROOT/devel/ and changes the site-packages folder to refer to that location.",
    "created_at": "2010-10-04T11:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98722",
    "user": "jason"
}
```

Replying to [comment:6 mpatel]:
> The extcode, sage_scripts, and sage packages use Mercurial in their `spkg-install`s to merge changes into an existing repository.  This could be more efficient than copying every file every time.  Can we do that here?

Can we make a new ticket for that?

In fact, I like this approach better (backup and copy), since it plays nicely with patch queues.  The merge approach messes everything up if you forgot to pop all of your patches off.

> 
> Does the new `spkg-install` now install SageNB two places, under `site-packages` and `devel`?  Is it practical to do just the latter?


No, I don't think it installs twice (you can check the files to make sure).  The setup.py develop installs under $SAGE_ROOT/devel/ and changes the site-packages folder to refer to that location.



---

archive/issue_comments_098723.json:
```json
{
    "body": "Replying to [comment:7 jason]:\n> Replying to [comment:6 mpatel]:\n> > The extcode, sage_scripts, and sage packages use Mercurial in their `spkg-install`s to merge changes into an existing repository.  This could be more efficient than copying every file every time.  Can we do that here?\n> \n> Can we make a new ticket for that?\n> \n> In fact, I like this approach better (backup and copy), since it plays nicely with patch queues.  The merge approach messes everything up if you forgot to pop all of your patches off.\n\nI agree with Jason.\n\n> \n> > \n> > Does the new `spkg-install` now install SageNB two places, under `site-packages` and `devel`?  Is it practical to do just the latter?\n> \n> \n> No, I don't think it installs twice (you can check the files to make sure).  The setup.py develop installs under $SAGE_ROOT/devel/ and changes the site-packages folder to refer to that location.\n\nActually, it does, but doing so is needed for the docs to show (static docs). We can make another ticket for that.",
    "created_at": "2010-10-04T13:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98723",
    "user": "timdumol"
}
```

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

archive/issue_comments_098724.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-10-05T02:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98724",
    "user": "jason"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_098725.json:
```json
{
    "body": "I think both questions were answered, so I'm setting this back to positive review.  It would be **fantastic** if it were included in the sagenb package for the next release.",
    "created_at": "2010-10-05T02:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98725",
    "user": "jason"
}
```

I think both questions were answered, so I'm setting this back to positive review.  It would be **fantastic** if it were included in the sagenb package for the next release.



---

archive/issue_comments_098726.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-05T02:24:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98726",
    "user": "jason"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098727.json:
```json
{
    "body": "By the way, another issue for another ticket: updating [the developer's guide](http://sagemath.org/doc/developer/producing_patches.html#using-mercurial-with-other-sage-repositories) to include sagenb in the list of Mercurial repositories.",
    "created_at": "2010-10-05T03:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98727",
    "user": "jhpalmieri"
}
```

By the way, another issue for another ticket: updating [the developer's guide](http://sagemath.org/doc/developer/producing_patches.html#using-mercurial-with-other-sage-repositories) to include sagenb in the list of Mercurial repositories.



---

archive/issue_comments_098728.json:
```json
{
    "body": "Sounds good.  Thanks for the information.  I'll add this to SageNB 0.8.4 at #10036.",
    "created_at": "2010-10-05T03:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98728",
    "user": "mpatel"
}
```

Sounds good.  Thanks for the information.  I'll add this to SageNB 0.8.4 at #10036.



---

archive/issue_comments_098729.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-06T03:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98729",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_098730.json:
```json
{
    "body": "There's a problem with compiling from scratch, because `$SAGE_ROOT/devel` does not exist when `sagenb-*.spkg` is installed.  I think doing `mkdir -p` will be enough.\n\nCan someone add a new patch to fix this?",
    "created_at": "2010-10-07T10:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98730",
    "user": "mpatel"
}
```

There's a problem with compiling from scratch, because `$SAGE_ROOT/devel` does not exist when `sagenb-*.spkg` is installed.  I think doing `mkdir -p` will be enough.

Can someone add a new patch to fix this?



---

archive/issue_comments_098731.json:
```json
{
    "body": "Make `$SAGE_ROOT/devel` on install, if necessary.  Apply on top of package extraction patch.",
    "created_at": "2010-10-07T11:30:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98731",
    "user": "mpatel"
}
```

Make `$SAGE_ROOT/devel` on install, if necessary.  Apply on top of package extraction patch.



---

archive/issue_comments_098732.json:
```json
{
    "body": "Attachment [trac_9920-devel_dir_fix.patch](tarball://root/attachments/some-uuid/ticket9920/trac_9920-devel_dir_fix.patch) by mpatel created at 2010-10-07 11:38:11\n\nI've added a patch that I'm testing now.",
    "created_at": "2010-10-07T11:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98732",
    "user": "mpatel"
}
```

Attachment [trac_9920-devel_dir_fix.patch](tarball://root/attachments/some-uuid/ticket9920/trac_9920-devel_dir_fix.patch) by mpatel created at 2010-10-07 11:38:11

I've added a patch that I'm testing now.



---

archive/issue_comments_098733.json:
```json
{
    "body": "Replying to [comment:17 mpatel]:\n> I've added a patch that I'm testing now.\n\nIt works.",
    "created_at": "2010-10-07T12:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98733",
    "user": "mpatel"
}
```

Replying to [comment:17 mpatel]:
> I've added a patch that I'm testing now.

It works.



---

archive/issue_comments_098734.json:
```json
{
    "body": "I think we'll need to open a new ticket for making this link\n\n```\nln -sf \"$SAGE_ROOT/devel/sagenb-main\" \"$SAGE_ROOT/devel/sagenb\" \n```\n\nrelative.  Otherwise, Sage won't start after I move/rename the root directory.",
    "created_at": "2010-10-07T12:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98734",
    "user": "mpatel"
}
```

I think we'll need to open a new ticket for making this link

```
ln -sf "$SAGE_ROOT/devel/sagenb-main" "$SAGE_ROOT/devel/sagenb" 
```

relative.  Otherwise, Sage won't start after I move/rename the root directory.



---

archive/issue_comments_098735.json:
```json
{
    "body": "And maybe also add `python setup.py develop` to `SAGE_LOCAL/bin/sage-location`?",
    "created_at": "2010-10-07T12:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98735",
    "user": "mpatel"
}
```

And maybe also add `python setup.py develop` to `SAGE_LOCAL/bin/sage-location`?



---

archive/issue_comments_098736.json:
```json
{
    "body": "Replying to [comment:20 mpatel]:\n> And maybe also add `python setup.py develop` to `SAGE_LOCAL/bin/sage-location`?\n\nSee #10097.",
    "created_at": "2010-10-07T22:03:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9919#issuecomment-98736",
    "user": "mpatel"
}
```

Replying to [comment:20 mpatel]:
> And maybe also add `python setup.py develop` to `SAGE_LOCAL/bin/sage-location`?

See #10097.
