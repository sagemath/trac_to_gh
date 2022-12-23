# Issue 7546: Update Mac OS X app and icon

Issue created by migration from https://trac.sagemath.org/ticket/7546

Original creator: iandrus

Original creation time: 2009-11-27 20:43:23

Assignee: was

CC:  was mhansen

Keywords: icon, launcher

There are new icons created Harald Schilly, so I thought I would take this opportunity to update the OS X launcher to use them and also make it easier to update in the future.


---

Attachment

change the tar file for an app bundle


---

Comment by iandrus created at 2009-11-27 20:51:12

In the app-bundle patch I accidentally added a .DS_Store file, but then I removed it.  I hope that doesn't cause any problems with history.


---

Comment by iandrus created at 2009-11-27 20:51:12

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-11-28 04:24:57

Is it possible to fix #5261 in here as well (somehow detecting Intel vs. PPC, for instance)?


---

Comment by iandrus created at 2009-11-28 09:44:00

I haven't added anything to detect Intel/PPC, but I think I have fixed the rest of #5261.  I think detection should be a separate ticket.


---

Comment by kcrisman created at 2009-12-04 16:03:03

I like the bdist patch, except for some reason it doesn't look like the sage-bdist at [http://hg.sagemath.org/scripts-main](http://hg.sagemath.org/scripts-main).    Does this depend on some other patch (perhaps one in 4.3.alpha0)?


---

Comment by kcrisman created at 2009-12-04 16:03:03

Changing status from needs_review to needs_info.


---

Comment by iandrus created at 2009-12-06 21:20:34

Oops, very sorry about that.  I had some local changes committed when upgrading.  I have updated the patch to work against 4.3.alpha1, and have started using mercurial queues to prevent this sort of mistake in the future.


---

Comment by iandrus created at 2009-12-06 21:20:34

Changing status from needs_info to needs_review.


---

Comment by kcrisman created at 2009-12-07 17:31:30

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

Comment by kcrisman created at 2009-12-07 17:31:30

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2009-12-07 17:36:24

I'm really sorry, I think I screwed something up... how do I apply the change of the tar file?  I get 

```
cp: /Users/.../sage-4.3.alpha1/data/extcode/sage/ext/mac-app/Sage.app: No such file or directory
sed: ./Sage.app/Contents/Info.plist: No such file or directory
mv: rename sage to ./Sage.app/Contents/Resources/: No such file or directory
mv: rename Sage.app to Sage-sample.app: No such file or directory
```

So obviously hg_sage.import... didn't actually import these files.  Should I put them in manually?  That is difficult given the current patch state, since the various icon files etc. are just binary data on trac.


---

Comment by iandrus created at 2009-12-07 22:16:43

Ack!  That's exactly what I meant.  That's what I get for not waiting the incredible amount of time it takes to build before posting a patch.  I have uploaded a patch that I actually tested this time :)

As for the other, try (from the top level sage directory)

cd data/extcode
curl http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7546/app-bundle-7546.patch | sage -hg import -

that seems to have worked for me.  I tried to use hg_sage.import_patch(...) but it put it in the wrong place.  I'm no expert in that part of sage so I probably did something wrong.


---

Comment by iandrus created at 2009-12-07 22:16:43

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by kcrisman created at 2009-12-08 04:10:42

Man, Unix commands... I really appreciate it.  I had actually downloaded it, so file:///path worked as an argument to curl.

Okay, this now seems to work on my Macintel 10.5!  It takes a looong time (multiple minutes) to verify the .dmg when I click on it, and then a few more minutes (!) to copy the app bundle.  Is that just because it's well over one gigabyte?

When my PPC finishes building (sometime tomorrow) I will check there too.   If I'm really ambitious I will also try #5261, as well as actually moving it from the Intel to PPC (over the network, so probably very slowly).  I don't know if I'll be done in time for 4.3, but certainly for 4.3.1.  Thanks for all the work on this!


---

Comment by was created at 2009-12-08 06:05:06

> So obviously hg_sage.import... didn't actually import these files.

It's a patch to the extcode repo, so you have to use `hg_extcode.import`...


---

Comment by iandrus created at 2009-12-08 09:28:54

kcrisman thanks for reviewing it even through all the rockiness, and thanks was for the pointer to hg_extcode.  It makes so much more sense now.


---

Comment by kcrisman created at 2009-12-08 16:16:47

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

Comment by kcrisman created at 2009-12-08 16:38:34

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

Comment by kcrisman created at 2009-12-08 16:38:34

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-12-08 16:57:31

I'm also looking to check what happens when I try to run an Intel bundle on a PPC, but unless the network significantly speeds up, that won't happen today.

The reason why I still put positive review despite the migration issue is that at this point the sage-bdist doesn't make these by default, and sage-support can easily point to downloading the non-notebook version when that time comes.  I'm putting that on #7622 as well.


---

Comment by kcrisman created at 2009-12-08 16:58:58

Sorry, that is not the right ticket, so I guess I'll leave it here.


---

Comment by mhansen created at 2009-12-09 02:41:13

Resolution: fixed
