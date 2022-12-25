# Issue 6955: update simon denis pari-scripts

archive/issues_006955.json:
```json
{
    "body": "Assignee: @loefflerd\n\nKeywords: two descent,\n\nI found out that sage comes with old versions of the files ell.gp,  ellQ.gp,  qfsolve.gp. This should be updated. The newest version can be found at http://www.math.unicaen.fr/~simon/ .\n\nIssue created by migration from https://trac.sagemath.org/ticket/6955\n\n",
    "created_at": "2009-09-18T11:03:40Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "update simon denis pari-scripts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6955",
    "user": "https://github.com/categorie"
}
```
Assignee: @loefflerd

Keywords: two descent,

I found out that sage comes with old versions of the files ell.gp,  ellQ.gp,  qfsolve.gp. This should be updated. The newest version can be found at http://www.math.unicaen.fr/~simon/ .

Issue created by migration from https://trac.sagemath.org/ticket/6955





---

archive/issue_comments_057406.json:
```json
{
    "body": "This should be very easy to do, but I don't know how to submit a patch for this. Sorry.",
    "created_at": "2009-09-18T11:04:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57406",
    "user": "https://github.com/categorie"
}
```

This should be very easy to do, but I don't know how to submit a patch for this. Sorry.



---

archive/issue_comments_057407.json:
```json
{
    "body": "Remove assignee @loefflerd.",
    "created_at": "2009-10-09T09:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57407",
    "user": "https://github.com/loefflerd"
}
```

Remove assignee @loefflerd.



---

archive/issue_comments_057408.json:
```json
{
    "body": "See also #5153.  We'll need to check that the version on Denis's home page is at least as up-to-date as the one he sent me which apparently fixed the bug I sent him.  I'll also try to find that email correspondence and add it to one of these tickets.",
    "created_at": "2009-12-14T17:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57408",
    "user": "https://github.com/JohnCremona"
}
```

See also #5153.  We'll need to check that the version on Denis's home page is at least as up-to-date as the one he sent me which apparently fixed the bug I sent him.  I'll also try to find that email correspondence and add it to one of these tickets.



---

archive/issue_comments_057409.json:
```json
{
    "body": "I have updated the scripts (attached to the ticket) to the ones on DS's home page on 3 April 2010, which are dated as follows:\n- ell.gp (v. 2009-03-25)\n- ellQ.gp (v. 2008-04-29)\n- qfsolve.gp (v. 2008-02-26)\nThe patch (to appear) applies to 4.3.5 and fixes some small things:  Simon's variable DEBUGLEVEL has been renamed DEBUGLEVEL_ell, and some of the verbose output changes a little.  ALso, some \"generators\" appear in a different order or are otherwise (mathematically) trivially different.\n\nThis does not fix other issues with these scripts, as in #5153.",
    "created_at": "2010-04-03T16:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57409",
    "user": "https://github.com/JohnCremona"
}
```

I have updated the scripts (attached to the ticket) to the ones on DS's home page on 3 April 2010, which are dated as follows:
- ell.gp (v. 2009-03-25)
- ellQ.gp (v. 2008-04-29)
- qfsolve.gp (v. 2008-02-26)
The patch (to appear) applies to 4.3.5 and fixes some small things:  Simon's variable DEBUGLEVEL has been renamed DEBUGLEVEL_ell, and some of the verbose output changes a little.  ALso, some "generators" appear in a different order or are otherwise (mathematically) trivially different.

This does not fix other issues with these scripts, as in #5153.



---

archive/issue_comments_057410.json:
```json
{
    "body": "Attachment [ellQ.gp](tarball://root/attachments/some-uuid/ticket6955/ellQ.gp) by @JohnCremona created at 2010-04-03 16:37:19",
    "created_at": "2010-04-03T16:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57410",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [ellQ.gp](tarball://root/attachments/some-uuid/ticket6955/ellQ.gp) by @JohnCremona created at 2010-04-03 16:37:19



---

archive/issue_comments_057411.json:
```json
{
    "body": "Attachment [trac_6955-simon-update.patch](tarball://root/attachments/some-uuid/ticket6955/trac_6955-simon-update.patch) by @JohnCremona created at 2010-04-03 16:42:29\n\nApplies to 4.3.5",
    "created_at": "2010-04-03T16:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57411",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_6955-simon-update.patch](tarball://root/attachments/some-uuid/ticket6955/trac_6955-simon-update.patch) by @JohnCremona created at 2010-04-03 16:42:29

Applies to 4.3.5



---

archive/issue_comments_057412.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-03T16:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57412",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057413.json:
```json
{
    "body": "The three scripts should replace those in SAGE_ROOT/data/extcode/pari/simon/",
    "created_at": "2010-04-03T16:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57413",
    "user": "https://github.com/JohnCremona"
}
```

The three scripts should replace those in SAGE_ROOT/data/extcode/pari/simon/



---

archive/issue_comments_057414.json:
```json
{
    "body": "Apply in SAGE_ROOT/data/extcode before other patch",
    "created_at": "2010-04-03T18:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57414",
    "user": "https://github.com/JohnCremona"
}
```

Apply in SAGE_ROOT/data/extcode before other patch



---

archive/issue_comments_057415.json:
```json
{
    "body": "Attachment [trac_6955-simon-update-extcode.patch](tarball://root/attachments/some-uuid/ticket6955/trac_6955-simon-update-extcode.patch) by @JohnCremona created at 2010-04-03 18:35:21\n\nThe patch trac_6955-simon-update-extcode.patch should be applied in the directory SAGE_ROOT/data/extcode in addition to the usual patch for sage-main.  The gp files on the ticket are just for reference.",
    "created_at": "2010-04-03T18:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57415",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_6955-simon-update-extcode.patch](tarball://root/attachments/some-uuid/ticket6955/trac_6955-simon-update-extcode.patch) by @JohnCremona created at 2010-04-03 18:35:21

The patch trac_6955-simon-update-extcode.patch should be applied in the directory SAGE_ROOT/data/extcode in addition to the usual patch for sage-main.  The gp files on the ticket are just for reference.



---

archive/issue_comments_057416.json:
```json
{
    "body": "Sorry, John, I am a newbie to anything that is outside the devel-tree. Can you tell me exactly what I have to do (if you want me to review it) ?\n\nChris.",
    "created_at": "2010-04-08T13:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57416",
    "user": "https://github.com/categorie"
}
```

Sorry, John, I am a newbie to anything that is outside the devel-tree. Can you tell me exactly what I have to do (if you want me to review it) ?

Chris.



---

archive/issue_comments_057417.json:
```json
{
    "body": "Replying to [comment:7 wuthrich]:\n> Sorry, John, I am a newbie to anything that is outside the devel-tree.\n\nSo was I before I did this!\n\n> Can you tell me exactly what I have to do (if you want me to review it) ?\n>\n\nOK.  You need to be careful, since you will be changing files outside $SAGE_ROOT/devel, which are therefore not covered by the cloning system, so you have to work a bit harder both to apply the patches and to unapply them.  I will assume that you will use mercurial queues (but it would be possible without).\n\nFirst make a clone in the usual way, say called simon, so you have created $SAGE_ROOT/devel/sage-simon as a copy of $SAGE_ROOT/devel/sage-main.\n\nNow apply the patch to the extcode:\n\n```\ncd SAGE_ROOT/data/extcode  \nhg qseries      # test that queues have been initialised here;  if not, do hg qinit first\nhg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6955/trac_6955-simon-update-extcode.patch\nhg qpush\n```\n\nNow apply the ordinary patch:\n\n```\ncd ../../devel/sage-simon\nhg qinit  # if not already done\nhg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6955/trac_6955-simon-update.patch\nhg qpush\nsage -b\n```\n\n\nThat's it applied.  Run, test, as much as you like.  To reverse the changes:\n\n```\n# in devel/sage-simon\nhg qpop\ncd ../../data/extcode\nhg qpop\nsage -b\n```\n\n\n \n> Chris.",
    "created_at": "2010-04-08T15:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57417",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:7 wuthrich]:
> Sorry, John, I am a newbie to anything that is outside the devel-tree.

So was I before I did this!

> Can you tell me exactly what I have to do (if you want me to review it) ?
>

OK.  You need to be careful, since you will be changing files outside $SAGE_ROOT/devel, which are therefore not covered by the cloning system, so you have to work a bit harder both to apply the patches and to unapply them.  I will assume that you will use mercurial queues (but it would be possible without).

First make a clone in the usual way, say called simon, so you have created $SAGE_ROOT/devel/sage-simon as a copy of $SAGE_ROOT/devel/sage-main.

Now apply the patch to the extcode:

```
cd SAGE_ROOT/data/extcode  
hg qseries      # test that queues have been initialised here;  if not, do hg qinit first
hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6955/trac_6955-simon-update-extcode.patch
hg qpush
```

Now apply the ordinary patch:

```
cd ../../devel/sage-simon
hg qinit  # if not already done
hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6955/trac_6955-simon-update.patch
hg qpush
sage -b
```


That's it applied.  Run, test, as much as you like.  To reverse the changes:

```
# in devel/sage-simon
hg qpop
cd ../../data/extcode
hg qpop
sage -b
```


 
> Chris.



---

archive/issue_comments_057418.json:
```json
{
    "body": "Thanks a lot for the very helpful comments. I assume the next time I would be able to make a patch myself for this.\n\nAll tests passed after having deleted the first change in the patch (it added a space at the start of the file.)\n\nThe modified patch corrects this.",
    "created_at": "2010-04-09T17:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57418",
    "user": "https://github.com/categorie"
}
```

Thanks a lot for the very helpful comments. I assume the next time I would be able to make a patch myself for this.

All tests passed after having deleted the first change in the patch (it added a space at the start of the file.)

The modified patch corrects this.



---

archive/issue_comments_057419.json:
```json
{
    "body": "Attachment [trac_6955-simon-update_reviewer.patch](tarball://root/attachments/some-uuid/ticket6955/trac_6955-simon-update_reviewer.patch) by @categorie created at 2010-04-09 17:17:37\n\nreplaces the previous patch of this name",
    "created_at": "2010-04-09T17:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57419",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_6955-simon-update_reviewer.patch](tarball://root/attachments/some-uuid/ticket6955/trac_6955-simon-update_reviewer.patch) by @categorie created at 2010-04-09 17:17:37

replaces the previous patch of this name



---

archive/issue_comments_057420.json:
```json
{
    "body": "So I give a positive review. The two patches trac_6955-simon-update_reviewer.patch and trac_6955-simon-update-extcode.patch have to be applied as described by John.",
    "created_at": "2010-04-09T17:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57420",
    "user": "https://github.com/categorie"
}
```

So I give a positive review. The two patches trac_6955-simon-update_reviewer.patch and trac_6955-simon-update-extcode.patch have to be applied as described by John.



---

archive/issue_comments_057421.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-09T17:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57421",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057422.json:
```json
{
    "body": "Thanks -- sorry about that space, which I thought I had put in before making the patch and not after!  It has been bugging me ever since.",
    "created_at": "2010-04-09T18:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57422",
    "user": "https://github.com/JohnCremona"
}
```

Thanks -- sorry about that space, which I thought I had put in before making the patch and not after!  It has been bugging me ever since.



---

archive/issue_comments_057423.json:
```json
{
    "body": "The reviewer patch doesn't apply cleanly.  Is it okay to just delete the portion of the patch for the file sage/schemes/elliptic_curves/gp_simon.py?",
    "created_at": "2010-04-15T22:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57423",
    "user": "https://github.com/jhpalmieri"
}
```

The reviewer patch doesn't apply cleanly.  Is it okay to just delete the portion of the patch for the file sage/schemes/elliptic_curves/gp_simon.py?



---

archive/issue_comments_057424.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-15T22:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57424",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_057425.json:
```json
{
    "body": "Replying to [comment:12 jhpalmieri]:\n> The reviewer patch doesn't apply cleanly.  Is it okay to just delete the portion of the patch for the file sage/schemes/elliptic_curves/gp_simon.py? \n\nNo, that part is crucial.  Did you see that the review patch is instead of my patch called trac_6955-simon-update.patch, and not a second one to b applied after it?  The only difference between them is that my patch wrongly inserts a space in the first line of the file ell_number_field.py, and Chris's patch removes that bit of my patch,",
    "created_at": "2010-04-16T08:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57425",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:12 jhpalmieri]:
> The reviewer patch doesn't apply cleanly.  Is it okay to just delete the portion of the patch for the file sage/schemes/elliptic_curves/gp_simon.py? 

No, that part is crucial.  Did you see that the review patch is instead of my patch called trac_6955-simon-update.patch, and not a second one to b applied after it?  The only difference between them is that my patch wrongly inserts a space in the first line of the file ell_number_field.py, and Chris's patch removes that bit of my patch,



---

archive/issue_comments_057426.json:
```json
{
    "body": "Replying to [comment:13 cremona]:\n> Did you see that the review patch is instead of my patch called trac_6955-simon-update.patch, and not a second one to b applied after it?  \n\nAh, no, I'd missed that.  Sorry.",
    "created_at": "2010-04-16T17:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57426",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:13 cremona]:
> Did you see that the review patch is instead of my patch called trac_6955-simon-update.patch, and not a second one to b applied after it?  

Ah, no, I'd missed that.  Sorry.



---

archive/issue_comments_057427.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-16T17:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57427",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057428.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-16T17:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57428",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007179.json:
```json
{
    "actor": "@jhpalmieri",
    "created_at": "2010-04-16T18:58:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6955#event-7179"
}
```



---

archive/issue_comments_057429.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n- trac_6955-simon-update-extcode.patch\n- trac_6955-simon-update_reviewer.patch",
    "created_at": "2010-04-16T18:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57429",
    "user": "https://github.com/jhpalmieri"
}
```

Merged in 4.4.alpha0:
- trac_6955-simon-update-extcode.patch
- trac_6955-simon-update_reviewer.patch



---

archive/issue_comments_057430.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57430",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_057431.json:
```json
{
    "body": "Many thanks, jhp -- seems that you are release manager, and busy!",
    "created_at": "2010-04-16T19:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6955#issuecomment-57431",
    "user": "https://github.com/JohnCremona"
}
```

Many thanks, jhp -- seems that you are release manager, and busy!
