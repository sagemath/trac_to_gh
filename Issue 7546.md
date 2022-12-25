# Issue 7546: Update Mac OS X app and icon

archive/issues_007546.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein @mwhansen\n\nKeywords: icon, launcher\n\nThere are new icons created Harald Schilly, so I thought I would take this opportunity to update the OS X launcher to use them and also make it easier to update in the future.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7546\n\n",
    "created_at": "2009-11-27T20:43:23Z",
    "labels": [
        "component: user interface",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Update Mac OS X app and icon",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7546",
    "user": "https://github.com/gvol"
}
```
Assignee: @williamstein

CC:  @williamstein @mwhansen

Keywords: icon, launcher

There are new icons created Harald Schilly, so I thought I would take this opportunity to update the OS X launcher to use them and also make it easier to update in the future.

Issue created by migration from https://trac.sagemath.org/ticket/7546





---

archive/issue_comments_063963.json:
```json
{
    "body": "Attachment [app-bundle-7546.patch](tarball://root/attachments/some-uuid/ticket7546/app-bundle-7546.patch) by @gvol created at 2009-11-27 20:48:20\n\nchange the tar file for an app bundle",
    "created_at": "2009-11-27T20:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63963",
    "user": "https://github.com/gvol"
}
```

Attachment [app-bundle-7546.patch](tarball://root/attachments/some-uuid/ticket7546/app-bundle-7546.patch) by @gvol created at 2009-11-27 20:48:20

change the tar file for an app bundle



---

archive/issue_comments_063964.json:
```json
{
    "body": "In the app-bundle patch I accidentally added a .DS_Store file, but then I removed it.  I hope that doesn't cause any problems with history.",
    "created_at": "2009-11-27T20:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63964",
    "user": "https://github.com/gvol"
}
```

In the app-bundle patch I accidentally added a .DS_Store file, but then I removed it.  I hope that doesn't cause any problems with history.



---

archive/issue_comments_063965.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-27T20:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63965",
    "user": "https://github.com/gvol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063966.json:
```json
{
    "body": "Is it possible to fix #5261 in here as well (somehow detecting Intel vs. PPC, for instance)?",
    "created_at": "2009-11-28T04:24:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63966",
    "user": "https://github.com/kcrisman"
}
```

Is it possible to fix #5261 in here as well (somehow detecting Intel vs. PPC, for instance)?



---

archive/issue_comments_063967.json:
```json
{
    "body": "I haven't added anything to detect Intel/PPC, but I think I have fixed the rest of #5261.  I think detection should be a separate ticket.",
    "created_at": "2009-11-28T09:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63967",
    "user": "https://github.com/gvol"
}
```

I haven't added anything to detect Intel/PPC, but I think I have fixed the rest of #5261.  I think detection should be a separate ticket.



---

archive/issue_comments_063968.json:
```json
{
    "body": "I like the bdist patch, except for some reason it doesn't look like the sage-bdist at [http://hg.sagemath.org/scripts-main](http://hg.sagemath.org/scripts-main).    Does this depend on some other patch (perhaps one in 4.3.alpha0)?",
    "created_at": "2009-12-04T16:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63968",
    "user": "https://github.com/kcrisman"
}
```

I like the bdist patch, except for some reason it doesn't look like the sage-bdist at [http://hg.sagemath.org/scripts-main](http://hg.sagemath.org/scripts-main).    Does this depend on some other patch (perhaps one in 4.3.alpha0)?



---

archive/issue_comments_063969.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-12-04T16:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63969",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_063970.json:
```json
{
    "body": "Oops, very sorry about that.  I had some local changes committed when upgrading.  I have updated the patch to work against 4.3.alpha1, and have started using mercurial queues to prevent this sort of mistake in the future.",
    "created_at": "2009-12-06T21:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63970",
    "user": "https://github.com/gvol"
}
```

Oops, very sorry about that.  I had some local changes committed when upgrading.  I have updated the patch to work against 4.3.alpha1, and have started using mercurial queues to prevent this sort of mistake in the future.



---

archive/issue_comments_063971.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-12-06T21:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63971",
    "user": "https://github.com/gvol"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_063972.json:
```json
{
    "body": "There is a syntax error with else and fi on consecutive lines.  Maybe this is intended?\n\n```\n        # Rename it with the version number\n        mv Sage.app \"Sage-$SAGE_VERSION.app\"\n    else\n        echo 'If you wish to create an app bundle please set'\n        echo 'SAGE_APP_BUNDLE=yes'\n    fi\n\n    # Go back to the right directory for later copying\n    cd \"$CUR\"/tmp/\n    if [ \"$SAGE_APP_DMG\" = \"yes\" ]; then\n        echo \"Creating dmg\"\n        DYLD_LIBRARY_PATH=$SAGE_ORIG_DYLD_LIBRARY_PATH; export DYLD_LIBRARY_PATH\n        hdiutil create -srcfolder \"$TARGET\" -format UDBZ \"$TARGET\".dmg\n    else\n        echo 'If you wish to create a disk image please set'\n        echo 'SAGE_APP_DMG=yes'\n    fi\n```\n\nI did this and am now testing on Macintel 10.5, hope to do MacPPC 10.4 as well if it doesn't take forever to build.",
    "created_at": "2009-12-07T17:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63972",
    "user": "https://github.com/kcrisman"
}
```

There is a syntax error with else and fi on consecutive lines.  Maybe this is intended?

```
        # Rename it with the version number
        mv Sage.app "Sage-$SAGE_VERSION.app"
    else
        echo 'If you wish to create an app bundle please set'
        echo 'SAGE_APP_BUNDLE=yes'
    fi

    # Go back to the right directory for later copying
    cd "$CUR"/tmp/
    if [ "$SAGE_APP_DMG" = "yes" ]; then
        echo "Creating dmg"
        DYLD_LIBRARY_PATH=$SAGE_ORIG_DYLD_LIBRARY_PATH; export DYLD_LIBRARY_PATH
        hdiutil create -srcfolder "$TARGET" -format UDBZ "$TARGET".dmg
    else
        echo 'If you wish to create a disk image please set'
        echo 'SAGE_APP_DMG=yes'
    fi
```

I did this and am now testing on Macintel 10.5, hope to do MacPPC 10.4 as well if it doesn't take forever to build.



---

archive/issue_comments_063973.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-07T17:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63973",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063974.json:
```json
{
    "body": "I'm really sorry, I think I screwed something up... how do I apply the change of the tar file?  I get \n\n```\ncp: /Users/.../sage-4.3.alpha1/data/extcode/sage/ext/mac-app/Sage.app: No such file or directory\nsed: ./Sage.app/Contents/Info.plist: No such file or directory\nmv: rename sage to ./Sage.app/Contents/Resources/: No such file or directory\nmv: rename Sage.app to Sage-sample.app: No such file or directory\n```\n\nSo obviously hg_sage.import... didn't actually import these files.  Should I put them in manually?  That is difficult given the current patch state, since the various icon files etc. are just binary data on trac.",
    "created_at": "2009-12-07T17:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63974",
    "user": "https://github.com/kcrisman"
}
```

I'm really sorry, I think I screwed something up... how do I apply the change of the tar file?  I get 

```
cp: /Users/.../sage-4.3.alpha1/data/extcode/sage/ext/mac-app/Sage.app: No such file or directory
sed: ./Sage.app/Contents/Info.plist: No such file or directory
mv: rename sage to ./Sage.app/Contents/Resources/: No such file or directory
mv: rename Sage.app to Sage-sample.app: No such file or directory
```

So obviously hg_sage.import... didn't actually import these files.  Should I put them in manually?  That is difficult given the current patch state, since the various icon files etc. are just binary data on trac.



---

archive/issue_comments_063975.json:
```json
{
    "body": "Ack!  That's exactly what I meant.  That's what I get for not waiting the incredible amount of time it takes to build before posting a patch.  I have uploaded a patch that I actually tested this time :)\n\nAs for the other, try (from the top level sage directory)\n\ncd data/extcode\ncurl http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7546/app-bundle-7546.patch | sage -hg import -\n\nthat seems to have worked for me.  I tried to use hg_sage.import_patch(...) but it put it in the wrong place.  I'm no expert in that part of sage so I probably did something wrong.",
    "created_at": "2009-12-07T22:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63975",
    "user": "https://github.com/gvol"
}
```

Ack!  That's exactly what I meant.  That's what I get for not waiting the incredible amount of time it takes to build before posting a patch.  I have uploaded a patch that I actually tested this time :)

As for the other, try (from the top level sage directory)

cd data/extcode
curl http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7546/app-bundle-7546.patch | sage -hg import -

that seems to have worked for me.  I tried to use hg_sage.import_patch(...) but it put it in the wrong place.  I'm no expert in that part of sage so I probably did something wrong.



---

archive/issue_comments_063976.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-07T22:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63976",
    "user": "https://github.com/gvol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063977.json:
```json
{
    "body": "Attachment [bdist-7546.patch](tarball://root/attachments/some-uuid/ticket7546/bdist-7546.patch) by @gvol created at 2009-12-07 22:17:32",
    "created_at": "2009-12-07T22:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63977",
    "user": "https://github.com/gvol"
}
```

Attachment [bdist-7546.patch](tarball://root/attachments/some-uuid/ticket7546/bdist-7546.patch) by @gvol created at 2009-12-07 22:17:32



---

archive/issue_comments_063978.json:
```json
{
    "body": "Man, Unix commands... I really appreciate it.  I had actually downloaded it, so file:///path worked as an argument to curl.\n\nOkay, this now seems to work on my Macintel 10.5!  It takes a looong time (multiple minutes) to verify the .dmg when I click on it, and then a few more minutes (!) to copy the app bundle.  Is that just because it's well over one gigabyte?\n\nWhen my PPC finishes building (sometime tomorrow) I will check there too.   If I'm really ambitious I will also try #5261, as well as actually moving it from the Intel to PPC (over the network, so probably very slowly).  I don't know if I'll be done in time for 4.3, but certainly for 4.3.1.  Thanks for all the work on this!",
    "created_at": "2009-12-08T04:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63978",
    "user": "https://github.com/kcrisman"
}
```

Man, Unix commands... I really appreciate it.  I had actually downloaded it, so file:///path worked as an argument to curl.

Okay, this now seems to work on my Macintel 10.5!  It takes a looong time (multiple minutes) to verify the .dmg when I click on it, and then a few more minutes (!) to copy the app bundle.  Is that just because it's well over one gigabyte?

When my PPC finishes building (sometime tomorrow) I will check there too.   If I'm really ambitious I will also try #5261, as well as actually moving it from the Intel to PPC (over the network, so probably very slowly).  I don't know if I'll be done in time for 4.3, but certainly for 4.3.1.  Thanks for all the work on this!



---

archive/issue_comments_063979.json:
```json
{
    "body": "> So obviously hg_sage.import... didn't actually import these files.\n\nIt's a patch to the extcode repo, so you have to use `hg_extcode.import`...",
    "created_at": "2009-12-08T06:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63979",
    "user": "https://github.com/williamstein"
}
```

> So obviously hg_sage.import... didn't actually import these files.

It's a patch to the extcode repo, so you have to use `hg_extcode.import`...



---

archive/issue_comments_063980.json:
```json
{
    "body": "kcrisman thanks for reviewing it even through all the rockiness, and thanks was for the pointer to hg_extcode.  It makes so much more sense now.",
    "created_at": "2009-12-08T09:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63980",
    "user": "https://github.com/gvol"
}
```

kcrisman thanks for reviewing it even through all the rockiness, and thanks was for the pointer to hg_extcode.  It makes so much more sense now.



---

archive/issue_comments_063981.json:
```json
{
    "body": "Yes, thanks was - I only knew about hg_scripts and hg_sage.  Great!\n\nI should point out that the .DS_Store thing does \n\n```\n1 out of 1 hunks FAILED -- saving rejects to file sage/ext/.DS_Store.rej\nsage/ext/.DS_Store not tracked!\nsage/ext/.DS_Store: No such file or directory\nabort: patch failed to apply\n```\n\n\nbut I think everything actually still works out okay.   I'll change to positive review once I've verified a couple more things, which will depend on how fast sage.math and my own network are.\n\nDo you have any idea why it takes so dang long for the dmg to verify (more than five minutes)?  This could be a real turnoff; I haven't downloaded a binary in a while, so I forget whether that also takes a while to verify.  And then it takes another ten minutes to copy - granted, on an older computer, but this is a long time.  Good thing we have sagenb to try it out!\n\nNaming for PPC/Intel is now #7623.",
    "created_at": "2009-12-08T16:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63981",
    "user": "https://github.com/kcrisman"
}
```

Yes, thanks was - I only knew about hg_scripts and hg_sage.  Great!

I should point out that the .DS_Store thing does 

```
1 out of 1 hunks FAILED -- saving rejects to file sage/ext/.DS_Store.rej
sage/ext/.DS_Store not tracked!
sage/ext/.DS_Store: No such file or directory
abort: patch failed to apply
```


but I think everything actually still works out okay.   I'll change to positive review once I've verified a couple more things, which will depend on how fast sage.math and my own network are.

Do you have any idea why it takes so dang long for the dmg to verify (more than five minutes)?  This could be a real turnoff; I haven't downloaded a binary in a while, so I forget whether that also takes a while to verify.  And then it takes another ten minutes to copy - granted, on an older computer, but this is a long time.  Good thing we have sagenb to try it out!

Naming for PPC/Intel is now #7623.



---

archive/issue_comments_063982.json:
```json
{
    "body": "Okay, the only problem I have found is the following:\n\nIF someone had a previous Sage install with the old notebook, but now downloads and uses this, the script will ask whether they want to migrate their notebooks.  Like this:\n\n```\n********************************************************************************\n*\n* The Sage notebook at\n*\n*      '/Users/karl-dietercrisman/.sage/sage_notebook'\n*\n* will be upgraded to a new format and stored in\n*\n*      '/Users/karl-dietercrisman/.sage/sage_notebook.sagenb'.\n*\n* Your existing notebook will not be modified in any way.\n*\n********************************************************************************\n\nWould like to continue? [YES or no]\n```\n\nOnly, they can't answer the question, because of how the bundle is made, so you have no choice but to quit.  Maybe there should be something which catches this?  I have absolutely no idea how it would be implemented; I'm cc:ing William in on this in case he has an obvious trick.\n\nOtherwise it all seems to work fine.  Positive review!  \n\nCan we still get this in 4.3?  This would be really good.",
    "created_at": "2009-12-08T16:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63982",
    "user": "https://github.com/kcrisman"
}
```

Okay, the only problem I have found is the following:

IF someone had a previous Sage install with the old notebook, but now downloads and uses this, the script will ask whether they want to migrate their notebooks.  Like this:

```
********************************************************************************
*
* The Sage notebook at
*
*      '/Users/karl-dietercrisman/.sage/sage_notebook'
*
* will be upgraded to a new format and stored in
*
*      '/Users/karl-dietercrisman/.sage/sage_notebook.sagenb'.
*
* Your existing notebook will not be modified in any way.
*
********************************************************************************

Would like to continue? [YES or no]
```

Only, they can't answer the question, because of how the bundle is made, so you have no choice but to quit.  Maybe there should be something which catches this?  I have absolutely no idea how it would be implemented; I'm cc:ing William in on this in case he has an obvious trick.

Otherwise it all seems to work fine.  Positive review!  

Can we still get this in 4.3?  This would be really good.



---

archive/issue_comments_063983.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T16:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63983",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063984.json:
```json
{
    "body": "I'm also looking to check what happens when I try to run an Intel bundle on a PPC, but unless the network significantly speeds up, that won't happen today.\n\nThe reason why I still put positive review despite the migration issue is that at this point the sage-bdist doesn't make these by default, and sage-support can easily point to downloading the non-notebook version when that time comes.  I'm putting that on #7622 as well.",
    "created_at": "2009-12-08T16:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63984",
    "user": "https://github.com/kcrisman"
}
```

I'm also looking to check what happens when I try to run an Intel bundle on a PPC, but unless the network significantly speeds up, that won't happen today.

The reason why I still put positive review despite the migration issue is that at this point the sage-bdist doesn't make these by default, and sage-support can easily point to downloading the non-notebook version when that time comes.  I'm putting that on #7622 as well.



---

archive/issue_comments_063985.json:
```json
{
    "body": "Sorry, that is not the right ticket, so I guess I'll leave it here.",
    "created_at": "2009-12-08T16:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63985",
    "user": "https://github.com/kcrisman"
}
```

Sorry, that is not the right ticket, so I guess I'll leave it here.



---

archive/issue_events_007776.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-12-09T02:41:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7546#event-7776"
}
```



---

archive/issue_comments_063986.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T02:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7546#issuecomment-63986",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
