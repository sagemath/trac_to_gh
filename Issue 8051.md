# Issue 8051: SageNB 0.7

archive/issues_008051.json:
```json
{
    "body": "Assignee: @williamstein\n\nNew spkg.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8051\n\n",
    "created_at": "2010-01-24T18:53:29Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "SageNB 0.7",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8051",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

New spkg.

Issue created by migration from https://trac.sagemath.org/ticket/8051





---

archive/issue_comments_070276.json:
```json
{
    "body": "If it's possible, I'd like to get into 0.7.1 as many of the now remaining \"needs review\" tickets as we can.  I'm rebasing these now.",
    "created_at": "2010-01-25T04:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70276",
    "user": "https://github.com/qed777"
}
```

If it's possible, I'd like to get into 0.7.1 as many of the now remaining "needs review" tickets as we can.  I'm rebasing these now.



---

archive/issue_comments_070277.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T04:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70277",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070278.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> If it's possible, I'd like to get into 0.7.1 as many of the now remaining \"needs review\" tickets as we can.  I'm rebasing these now.\nHere's a possible queue:\n\n```\ntrac_7784-hgignore_update.patch\ntrac_5712-interrupt-notification.5.patch\ntrac_6069-missing_pub_ws.2.patch\ntrac_8038-email_plus_addressing_v2.patch\ntrac_7506-notebook_object-documentation.2.patch\ntrac_693-spawn_notebook.3.patch\ntrac_5177-delete-cell-dirs.3.patch\n```\n",
    "created_at": "2010-01-25T07:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70278",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:2 mpatel]:
> If it's possible, I'd like to get into 0.7.1 as many of the now remaining "needs review" tickets as we can.  I'm rebasing these now.
Here's a possible queue:

```
trac_7784-hgignore_update.patch
trac_5712-interrupt-notification.5.patch
trac_6069-missing_pub_ws.2.patch
trac_8038-email_plus_addressing_v2.patch
trac_7506-notebook_object-documentation.2.patch
trac_693-spawn_notebook.3.patch
trac_5177-delete-cell-dirs.3.patch
```




---

archive/issue_comments_070279.json:
```json
{
    "body": "Changing assignee from @williamstein to @qed777.",
    "created_at": "2010-01-27T05:40:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70279",
    "user": "https://github.com/qed777"
}
```

Changing assignee from @williamstein to @qed777.



---

archive/issue_comments_070280.json:
```json
{
    "body": "I just noticed that long `'eval'` docstrings are truncated.  I'll add a reviewer patch to #3083.",
    "created_at": "2010-01-30T05:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70280",
    "user": "https://github.com/qed777"
}
```

I just noticed that long `'eval'` docstrings are truncated.  I'll add a reviewer patch to #3083.



---

archive/issue_comments_070281.json:
```json
{
    "body": "All tickets got positive review and have been merged. So what should be reviewed in this ticket?\n\nI installed the spkg, seems to work fine (but I did not test everything), is this enough to give positive review?\n\nbtw: the link from description \"says\" http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.2.spkg but it points to http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.1.spkg",
    "created_at": "2010-01-31T20:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70281",
    "user": "https://github.com/robert-marik"
}
```

All tickets got positive review and have been merged. So what should be reviewed in this ticket?

I installed the spkg, seems to work fine (but I did not test everything), is this enough to give positive review?

btw: the link from description "says" http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.2.spkg but it points to http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.1.spkg



---

archive/issue_comments_070282.json:
```json
{
    "body": "Replying to [comment:9 robert.marik]:\n> All tickets got positive review and have been merged. So what should be reviewed in this ticket?\n\nYou need to make sure that you can successfully install the updated spkg.\n\n\n\n\n\n> I installed the spkg, seems to work fine (but I did not test everything), is this enough to give positive review?\n\nI would say, all doctests must pass as well. In any case, if you can't run all doctests after installing the updated spkg, I can do that. A correct link to the updated spkg is\n\nhttp://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.2.spkg",
    "created_at": "2010-01-31T23:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70282",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:9 robert.marik]:
> All tickets got positive review and have been merged. So what should be reviewed in this ticket?

You need to make sure that you can successfully install the updated spkg.





> I installed the spkg, seems to work fine (but I did not test everything), is this enough to give positive review?

I would say, all doctests must pass as well. In any case, if you can't run all doctests after installing the updated spkg, I can do that. A correct link to the updated spkg is

http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.2.spkg



---

archive/issue_comments_070283.json:
```json
{
    "body": "I don't understand why the spkg is not managed by Mercurial:\n\n```\n[mvngu@mod sagenb-0.7.2]$ hg st\nabort: There is no Mercurial repository here (.hg not found)!\n```\n\nThe file `spkg-install` should have its executable bits on:\n\n```\n[mvngu@mod sagenb-0.7.2]$ ls -g spkg-install\n-rw-r--r-- 1 mvngu 348 2010-01-30 16:37 spkg-install\n```\n\nAnd `SPKG.txt` is very sketchy about update details.",
    "created_at": "2010-01-31T23:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70283",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I don't understand why the spkg is not managed by Mercurial:

```
[mvngu@mod sagenb-0.7.2]$ hg st
abort: There is no Mercurial repository here (.hg not found)!
```

The file `spkg-install` should have its executable bits on:

```
[mvngu@mod sagenb-0.7.2]$ ls -g spkg-install
-rw-r--r-- 1 mvngu 348 2010-01-30 16:37 spkg-install
```

And `SPKG.txt` is very sketchy about update details.



---

archive/issue_comments_070284.json:
```json
{
    "body": "I suggest\n\n* Checking that the package installs and the notebook runs.\n* Checking the repo for unchecked-in changes, queued patches, etc.\n* Checking that the claimed merged tickets appear in `hg log`.\n* Running the doctests: `sage -t -sagenb`.\n\nIdeally, you should run the SageNB Selenium tests, too.  But they require special extra setup.  I'll make simplifying that setup a separate ticket.\n\nThanks for pointing out the link error.  I've updated it.",
    "created_at": "2010-01-31T23:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70284",
    "user": "https://github.com/qed777"
}
```

I suggest

* Checking that the package installs and the notebook runs.
* Checking the repo for unchecked-in changes, queued patches, etc.
* Checking that the claimed merged tickets appear in `hg log`.
* Running the doctests: `sage -t -sagenb`.

Ideally, you should run the SageNB Selenium tests, too.  But they require special extra setup.  I'll make simplifying that setup a separate ticket.

Thanks for pointing out the link error.  I've updated it.



---

archive/issue_comments_070285.json:
```json
{
    "body": "The repository is in `sagenb-0.7.2/src/sagenb`.  We auto-generate the package with `sagenb-0.7.2/src/sagenb/spkg-dist`.\n\nI suggest that I make a separate ticket to update SPKG.txt.\n\nSee #7784 about\n\n```\n$ hg stat\n? release_notes.txt\n? setup.cfg\n```\n",
    "created_at": "2010-01-31T23:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70285",
    "user": "https://github.com/qed777"
}
```

The repository is in `sagenb-0.7.2/src/sagenb`.  We auto-generate the package with `sagenb-0.7.2/src/sagenb/spkg-dist`.

I suggest that I make a separate ticket to update SPKG.txt.

See #7784 about

```
$ hg stat
? release_notes.txt
? setup.cfg
```




---

archive/issue_comments_070286.json:
```json
{
    "body": "Replying to [comment:13 mpatel]:\n> I suggest that I make a separate ticket to update SPKG.txt.\n\nOr I can do this here later today.",
    "created_at": "2010-01-31T23:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70286",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:13 mpatel]:
> I suggest that I make a separate ticket to update SPKG.txt.

Or I can do this here later today.



---

archive/issue_comments_070287.json:
```json
{
    "body": "I'll fix the `spkg-install` problem, too.",
    "created_at": "2010-01-31T23:39:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70287",
    "user": "https://github.com/qed777"
}
```

I'll fix the `spkg-install` problem, too.



---

archive/issue_comments_070288.json:
```json
{
    "body": "Please see #7784 for the changes.  If/when that ticket gets a positive review, I'll create SageNB 0.7.3 and post it here.",
    "created_at": "2010-02-01T03:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70288",
    "user": "https://github.com/qed777"
}
```

Please see #7784 for the changes.  If/when that ticket gets a positive review, I'll create SageNB 0.7.3 and post it here.



---

archive/issue_comments_070289.json:
```json
{
    "body": "By the way, it seems that for the near future, I may be the only very active SageNB developer.  I'd be *very* happy to be proved (proven?) wrong!  There are many tasks to complete --- there are several cool new notebook features to implement.  It's not possible for me to cover them all, and I'd like to avoid stalling ongoing development.\n\nTo this end, I'll try to make it easier for Sage developers to review notebook tickets or make other contributions.  Please let me know what would help.  For example, I can make experimental spkgs that contain the latest patches in the queue.  Those who wish just to test the cumulative changes can install the package with `sage -f sagenb-*.spkg`.  But reviewers can also open the spkg, pop / push patches, and comment on specific ticket(s).  In either case, we'll get useful information about how the notebook behaves in a wider gamut of browser-OS combinations.  We'll also get more end user feedback.",
    "created_at": "2010-02-01T04:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70289",
    "user": "https://github.com/qed777"
}
```

By the way, it seems that for the near future, I may be the only very active SageNB developer.  I'd be *very* happy to be proved (proven?) wrong!  There are many tasks to complete --- there are several cool new notebook features to implement.  It's not possible for me to cover them all, and I'd like to avoid stalling ongoing development.

To this end, I'll try to make it easier for Sage developers to review notebook tickets or make other contributions.  Please let me know what would help.  For example, I can make experimental spkgs that contain the latest patches in the queue.  Those who wish just to test the cumulative changes can install the package with `sage -f sagenb-*.spkg`.  But reviewers can also open the spkg, pop / push patches, and comment on specific ticket(s).  In either case, we'll get useful information about how the notebook behaves in a wider gamut of browser-OS combinations.  We'll also get more end user feedback.



---

archive/issue_comments_070290.json:
```json
{
    "body": "Experimental spkgs would be good.  I think the best way to get more testing/review would be a good guide to applying patches, testing spkgs, etc.\n\nIs there a mailing list or wiki page for coordinating development effort?",
    "created_at": "2010-02-01T05:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70290",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Experimental spkgs would be good.  I think the best way to get more testing/review would be a good guide to applying patches, testing spkgs, etc.

Is there a mailing list or wiki page for coordinating development effort?



---

archive/issue_comments_070291.json:
```json
{
    "body": "Replying to [comment:18 acleone]:\n> Is there a mailing list or wiki page for coordinating development effort?\n\nA relevant mailing is [sage-devel](http://groups.google.com/group/sage-devel). Most of the time, that list receives high volume traffic on development discussion. For coordinating release effort, the [sage-release](http://groups.google.com/group/sage-release) mailing list is appropriate. Some effort is underway to expand the Sage documentation with information to help beginners getting started with Sage development. The relevant tickets are:\n\n1. #8108: Expand the Sage Developer Guide for newcomers\n2. #6987: reorganize section on producing patches with Mercurial\n3. #8079: Better documentation for patching spgk's\n4. #8104: developer's guide for making spkgs should specify that patches need to be version controlled\n5. #3882: explain in the programming guide why spkg source patches should be applied by copying entire files\n6. #7944: update Developers' Guide to reflect new process for working on tickets",
    "created_at": "2010-02-01T05:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70291",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:18 acleone]:
> Is there a mailing list or wiki page for coordinating development effort?

A relevant mailing is [sage-devel](http://groups.google.com/group/sage-devel). Most of the time, that list receives high volume traffic on development discussion. For coordinating release effort, the [sage-release](http://groups.google.com/group/sage-release) mailing list is appropriate. Some effort is underway to expand the Sage documentation with information to help beginners getting started with Sage development. The relevant tickets are:

1. #8108: Expand the Sage Developer Guide for newcomers
2. #6987: reorganize section on producing patches with Mercurial
3. #8079: Better documentation for patching spgk's
4. #8104: developer's guide for making spkgs should specify that patches need to be version controlled
5. #3882: explain in the programming guide why spkg source patches should be applied by copying entire files
6. #7944: update Developers' Guide to reflect new process for working on tickets



---

archive/issue_comments_070292.json:
```json
{
    "body": "Both [sage-devel](http://groups.google.com/group/sage-devel) and [sage-notebook](http://groups.google.com/group/sage-notebook) are good places.  I suppose we should move this discussion to sage-notebook.\n\nOne source for ideas is [SageTasks](http://wiki.sagemath.org/devel/SageTasks), but it may be getting old.\n\nAddendum: Of course, we should also try to attract energetic developers who'd contribute fresh ideas, techniques, etc., to the SageNB project.",
    "created_at": "2010-02-01T05:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70292",
    "user": "https://github.com/qed777"
}
```

Both [sage-devel](http://groups.google.com/group/sage-devel) and [sage-notebook](http://groups.google.com/group/sage-notebook) are good places.  I suppose we should move this discussion to sage-notebook.

One source for ideas is [SageTasks](http://wiki.sagemath.org/devel/SageTasks), but it may be getting old.

Addendum: Of course, we should also try to attract energetic developers who'd contribute fresh ideas, techniques, etc., to the SageNB project.



---

archive/issue_comments_070293.json:
```json
{
    "body": "While I'm here, I'd also like to suggest using `alpha.sagenb.org` or creating `ouch.sagenb.org` to test a bleeding-edge SageNB.  This could be a notebook with all positively reviewed patches applied or, more interestingly, an experimental spkg.\n\nWe could also set up a corresponding repository, different from http://boxen.math.washington.edu:8100/, to which to push experimental features and from which to backport what works.  A potential problem here is that Mercurial changesets are immutable.  But we might not care about keeping the history of this repository clean.\n\nJust some thoughts.",
    "created_at": "2010-02-01T06:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70293",
    "user": "https://github.com/qed777"
}
```

While I'm here, I'd also like to suggest using `alpha.sagenb.org` or creating `ouch.sagenb.org` to test a bleeding-edge SageNB.  This could be a notebook with all positively reviewed patches applied or, more interestingly, an experimental spkg.

We could also set up a corresponding repository, different from http://boxen.math.washington.edu:8100/, to which to push experimental features and from which to backport what works.  A potential problem here is that Mercurial changesets are immutable.  But we might not care about keeping the history of this repository clean.

Just some thoughts.



---

archive/issue_comments_070294.json:
```json
{
    "body": "Installs fine, works fine with jsmath image fonts, tests paseed, cannot check the rest, since I have probably old hg in my Debian Linux\n\n```\nsage@um-bc107:~/sagenb-0.7.2/src/sagenb$ hg log\nabort: requirement 'fncache' not supported!\nsage@um-bc107:~/sagenb-0.7.2/src/sagenb$ hg status\nabort: requirement 'fncache' not supported!\n```\n\n\nCan someone finish testing? I think that this is very important ticket and nice sage notebook is important to attract new users (and new developers). Thank you for working on it.",
    "created_at": "2010-02-02T18:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70294",
    "user": "https://github.com/robert-marik"
}
```

Installs fine, works fine with jsmath image fonts, tests paseed, cannot check the rest, since I have probably old hg in my Debian Linux

```
sage@um-bc107:~/sagenb-0.7.2/src/sagenb$ hg log
abort: requirement 'fncache' not supported!
sage@um-bc107:~/sagenb-0.7.2/src/sagenb$ hg status
abort: requirement 'fncache' not supported!
```


Can someone finish testing? I think that this is very important ticket and nice sage notebook is important to attract new users (and new developers). Thank you for working on it.



---

archive/issue_comments_070295.json:
```json
{
    "body": "If you have a spare moment, please review #7784, which is \"blocking\" this ticket.\n\nYou can use `sage -hg` instead of `hg`.",
    "created_at": "2010-02-02T22:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70295",
    "user": "https://github.com/qed777"
}
```

If you have a spare moment, please review #7784, which is "blocking" this ticket.

You can use `sage -hg` instead of `hg`.



---

archive/issue_comments_070296.json:
```json
{
    "body": "Minh -- Even with #8036, it's very likely the PDF reference manual won't build with this spkg, owing to #7249's Unicode doctests.  I'm not sure what we should do about this.",
    "created_at": "2010-02-03T02:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70296",
    "user": "https://github.com/qed777"
}
```

Minh -- Even with #8036, it's very likely the PDF reference manual won't build with this spkg, owing to #7249's Unicode doctests.  I'm not sure what we should do about this.



---

archive/issue_comments_070297.json:
```json
{
    "body": "Replying to [comment:24 mpatel]:\n> Minh -- Even with #8036, it's very likely the PDF reference manual won't build with this spkg, owing to #7249's Unicode doctests.  I'm not sure what we should do about this.\n\nThe release deadline for Sage 4.3.2 is Saturday 06th February 2010, which means there's not much time for sorting out failures when building the PDF version of the reference manual. I think [sagenb-0.7.3.spkg](http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.3.spkg) needs to wait for after Sage 4.3.2 is done.",
    "created_at": "2010-02-03T02:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70297",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:24 mpatel]:
> Minh -- Even with #8036, it's very likely the PDF reference manual won't build with this spkg, owing to #7249's Unicode doctests.  I'm not sure what we should do about this.

The release deadline for Sage 4.3.2 is Saturday 06th February 2010, which means there's not much time for sorting out failures when building the PDF version of the reference manual. I think [sagenb-0.7.3.spkg](http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.3.spkg) needs to wait for after Sage 4.3.2 is done.



---

archive/issue_comments_070298.json:
```json
{
    "body": "Please see #8167.  If/when that ticket gets a positive review, I'll make 0.7.4...",
    "created_at": "2010-02-03T09:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70298",
    "user": "https://github.com/qed777"
}
```

Please see #8167.  If/when that ticket gets a positive review, I'll make 0.7.4...



---

archive/issue_comments_070299.json:
```json
{
    "body": "I've posted SageNB 0.7.4 for review.",
    "created_at": "2010-02-05T00:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70299",
    "user": "https://github.com/qed777"
}
```

I've posted SageNB 0.7.4 for review.



---

archive/issue_comments_070300.json:
```json
{
    "body": "Thanks for the update. But now I have too many sage notebooks\n\n```\n[marik@um-bc107 ../lib/python/site-packages]$ pwd\n/opt/sage/local/lib/python/site-packages\n[marik@um-bc107 ../lib/python/site-packages]$ ls -ld sagenb*\ndrwxr-xr-x 4 marik marik 4096  1.\u00a0\u00fano 17.16 sagenb-0.6-py2.6.egg\ndrwxr-xr-x 4 marik marik 4096  2.\u00a0\u00fano 19.33 sagenb-0.7.2-py2.6.egg\ndrwxr-xr-x 4 marik marik 4096  5.\u00a0\u00fano 09.13 sagenb-0.7.4-py2.6.egg\n```\n\n\nHow do I know, which one is actually used? Jsmath image fonts failed to install intro correct directory. Should the old sage notebook be removed, first? Should this be tested on fresh install only?",
    "created_at": "2010-02-05T08:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70300",
    "user": "https://github.com/robert-marik"
}
```

Thanks for the update. But now I have too many sage notebooks

```
[marik@um-bc107 ../lib/python/site-packages]$ pwd
/opt/sage/local/lib/python/site-packages
[marik@um-bc107 ../lib/python/site-packages]$ ls -ld sagenb*
drwxr-xr-x 4 marik marik 4096  1. úno 17.16 sagenb-0.6-py2.6.egg
drwxr-xr-x 4 marik marik 4096  2. úno 19.33 sagenb-0.7.2-py2.6.egg
drwxr-xr-x 4 marik marik 4096  5. úno 09.13 sagenb-0.7.4-py2.6.egg
```


How do I know, which one is actually used? Jsmath image fonts failed to install intro correct directory. Should the old sage notebook be removed, first? Should this be tested on fresh install only?



---

archive/issue_comments_070301.json:
```json
{
    "body": "We install the sagenb package with [setuptools](http://peak.telecommunity.com/DevCenter/setuptools) ([PyPI](http://pypi.python.org/pypi/setuptools)), which updates `SAGE_LOCAL/lib/python/site-packages/easy-install.pth`.  This file contains paths prepended to `sys.path` on startup.\n\nYou can query the installed version with\n\n\n```python\nsage: from sagenb.misc.misc import SAGENB_VERSION\nsage: SAGENB_VERSION\n```\n\nwhich is essentially\n\n\n```python\nsage: from pkg_resources import Requirement, working_set\nsage: w = working_set.find(Requirement.parse('sagenb'))\nsage: w.version\n```\n\nMoreover, `w.location` gives the install directory.\n\nI'm checking the fonts now...",
    "created_at": "2010-02-05T09:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70301",
    "user": "https://github.com/qed777"
}
```

We install the sagenb package with [setuptools](http://peak.telecommunity.com/DevCenter/setuptools) ([PyPI](http://pypi.python.org/pypi/setuptools)), which updates `SAGE_LOCAL/lib/python/site-packages/easy-install.pth`.  This file contains paths prepended to `sys.path` on startup.

You can query the installed version with


```python
sage: from sagenb.misc.misc import SAGENB_VERSION
sage: SAGENB_VERSION
```

which is essentially


```python
sage: from pkg_resources import Requirement, working_set
sage: w = working_set.find(Requirement.parse('sagenb'))
sage: w.version
```

Moreover, `w.location` gives the install directory.

I'm checking the fonts now...



---

archive/issue_comments_070302.json:
```json
{
    "body": "sagenb 0.7.4 installed correctly for me.  All doc and selenium tests passed.  Still problems building the PDF docs but Ihaven't applied any of the unicode patches (using vanilla sage-4.3.2.alpha1).",
    "created_at": "2010-02-05T09:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70302",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

sagenb 0.7.4 installed correctly for me.  All doc and selenium tests passed.  Still problems building the PDF docs but Ihaven't applied any of the unicode patches (using vanilla sage-4.3.2.alpha1).



---

archive/issue_comments_070303.json:
```json
{
    "body": "On the fonts: What is the output of\n\n```sh\negrep \"Copying jsMath image\"\\|\"Installed.*sagenb\" $SAGE_ROOT/install.log \n```\n\n?",
    "created_at": "2010-02-05T09:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70303",
    "user": "https://github.com/qed777"
}
```

On the fonts: What is the output of

```sh
egrep "Copying jsMath image"\|"Installed.*sagenb" $SAGE_ROOT/install.log 
```

?



---

archive/issue_comments_070304.json:
```json
{
    "body": "Replying to [comment:30 acleone]:\n> sagenb 0.7.4 installed correctly for me.  All doc and selenium tests passed.  Still problems building the PDF docs but Ihaven't applied any of the unicode patches (using vanilla sage-4.3.2.alpha1).\nPositive review?",
    "created_at": "2010-02-05T10:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70304",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:30 acleone]:
> sagenb 0.7.4 installed correctly for me.  All doc and selenium tests passed.  Still problems building the PDF docs but Ihaven't applied any of the unicode patches (using vanilla sage-4.3.2.alpha1).
Positive review?



---

archive/issue_comments_070305.json:
```json
{
    "body": "\n```\n$ egrep \"Copying jsMath image\"\\|\"Installed.*sagenb\" ~/sage-dev/sage-4.3.2.alpha1/install.log\nInstalled /home/alex/sage-dev/sage-4.3.2.alpha1/local/lib/python2.6/site-packages/sagenb-0.6-py2.6.egg\n```\n\nStrange.\n\n\n```\nsage: from sagenb.misc.misc import SAGENB_VERSION\nsage: SAGENB_VERSION\n'0.7.4'\n```\n\n\nHere's how I installed: \n\n1. `make` on an unmodified 4.3.2.alpha1 \n\n2. \n\n```\n$ tar -jxvf sagenb-0.7.4.spkg\n$ cd sagenb-0.7.4/src/sagenb/\n$ sage -python setup.py develop\n```\n\n3. Tested with `sage -t -sagenb` \n\n4. Selenium tests with `sage -python sagenb/testing/run_tests.py` \n\n5. Checking the PDF build with `sage -docbuild all pdf`",
    "created_at": "2010-02-05T12:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70305",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```


```
$ egrep "Copying jsMath image"\|"Installed.*sagenb" ~/sage-dev/sage-4.3.2.alpha1/install.log
Installed /home/alex/sage-dev/sage-4.3.2.alpha1/local/lib/python2.6/site-packages/sagenb-0.6-py2.6.egg
```

Strange.


```
sage: from sagenb.misc.misc import SAGENB_VERSION
sage: SAGENB_VERSION
'0.7.4'
```


Here's how I installed: 

1. `make` on an unmodified 4.3.2.alpha1 

2. 

```
$ tar -jxvf sagenb-0.7.4.spkg
$ cd sagenb-0.7.4/src/sagenb/
$ sage -python setup.py develop
```

3. Tested with `sage -t -sagenb` 

4. Selenium tests with `sage -python sagenb/testing/run_tests.py` 

5. Checking the PDF build with `sage -docbuild all pdf`



---

archive/issue_comments_070306.json:
```json
{
    "body": "I think this is OK, because the `SAGE_LOCAL/bin/sage-spkg` script invoked by `sage -f` updates `SAGE_ROOT/install.log` but the `sage -python setup.py` commands do not.",
    "created_at": "2010-02-05T13:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70306",
    "user": "https://github.com/qed777"
}
```

I think this is OK, because the `SAGE_LOCAL/bin/sage-spkg` script invoked by `sage -f` updates `SAGE_ROOT/install.log` but the `sage -python setup.py` commands do not.



---

archive/issue_comments_070307.json:
```json
{
    "body": "The \"Use image fonts\" option is disabled (greyed out) in jsMath - is this a problem?\n\n`jsMath v3.6c (Unicode fonts)`",
    "created_at": "2010-02-05T13:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70307",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

The "Use image fonts" option is disabled (greyed out) in jsMath - is this a problem?

`jsMath v3.6c (Unicode fonts)`



---

archive/issue_comments_070308.json:
```json
{
    "body": "Are the image fonts installed?  In `twist.py`, we set the boolean\n\n```python\njsmath_image_fonts = is_package_installed(\"jsmath-image-fonts\")\n```\n\nwhich propagates to `jsmath.js`.  This should enable the option if the spkg is installed.  But the fonts need to be installed in the right place...",
    "created_at": "2010-02-05T13:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70308",
    "user": "https://github.com/qed777"
}
```

Are the image fonts installed?  In `twist.py`, we set the boolean

```python
jsmath_image_fonts = is_package_installed("jsmath-image-fonts")
```

which propagates to `jsmath.js`.  This should enable the option if the spkg is installed.  But the fonts need to be installed in the right place...



---

archive/issue_comments_070309.json:
```json
{
    "body": "Ok then, LGTM.",
    "created_at": "2010-02-05T13:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70309",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Ok then, LGTM.



---

archive/issue_comments_070310.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-05T13:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70310",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070311.json:
```json
{
    "body": "I decided to try something random to see if I was running the right notebook.  So I tried #3154 first, and it appears that it is *NOT* fixed by this notebook upgrade.  Other things I tried are fixed though.",
    "created_at": "2010-02-06T18:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70311",
    "user": "https://github.com/williamstein"
}
```

I decided to try something random to see if I was running the right notebook.  So I tried #3154 first, and it appears that it is *NOT* fixed by this notebook upgrade.  Other things I tried are fixed though.



---

archive/issue_comments_070312.json:
```json
{
    "body": "Remove assignee @qed777.",
    "created_at": "2010-02-06T18:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70312",
    "user": "https://github.com/williamstein"
}
```

Remove assignee @qed777.



---

archive/issue_comments_070313.json:
```json
{
    "body": "It turns out that I merged #4217, not #3154, into SageNB 0.7.  I didn't notice that #4217's commit string was copied from #3154 by mistake.  I used `hg log` to make the list of merged tickets in the description.",
    "created_at": "2010-02-06T19:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70313",
    "user": "https://github.com/qed777"
}
```

It turns out that I merged #4217, not #3154, into SageNB 0.7.  I didn't notice that #4217's commit string was copied from #3154 by mistake.  I used `hg log` to make the list of merged tickets in the description.



---

archive/issue_events_008260.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-10T09:34:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8051#event-8260"
}
```



---

archive/issue_comments_070314.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-10T09:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8051#issuecomment-70314",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
