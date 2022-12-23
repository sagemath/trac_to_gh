# Issue 5895: Limit number of worksheet snapshots

archive/issues_005895.json:
```json
{
    "body": "Assignee: rbeezer\n\nCC:  tornaria\n\nThis is an attempt to reduce the unlimited growth of snapshots of worksheets when using the notebook.  See related #5880 as well.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5895\n\n",
    "created_at": "2009-04-25T17:31:46Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Limit number of worksheet snapshots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5895",
    "user": "rbeezer"
}
```
Assignee: rbeezer

CC:  tornaria

This is an attempt to reduce the unlimited growth of snapshots of worksheets when using the notebook.  See related #5880 as well.

Issue created by migration from https://trac.sagemath.org/ticket/5895





---

archive/issue_comments_046608.json:
```json
{
    "body": "Attached patch is a simple approach to limiting the number of snapshots of a worksheet.  But it presents a bit of a dilemma.\n\n(a)  My first version removed any older snapshots necessary to get the total down to 30.  If added to Sage this would have potentially removed many files the first time a user closed up the notebook.  Presumably some folks might want lots of backups, and wouldn't appreciate having many of them deleted.\n\n(b)  The version included here will delete the single oldest snapshot immediately after creation of the 31-st snapshot.  So any huge collection of snapshots will not be touched, and small collections will not grow past 30.  However, if the maximum number is later changed to something smaller, care will be needed to be sure exisiting collections of snapshots don't revert back to growing uncontrollably.\n\nComments on the above greatly appreciated, and because of this, I don't consider this patch ready for formal review yet.\n\nObviously, setting `max_snaps = 30` should be user-configurable.  Is it easy to add a new option in `user_conf.py` which could then be reset from the Sage command-line on an instance of the notebook?  Or does this require an \"upgrade\" of the data structures for a user's record in {{{nb.sobj}} (and therefore becomes much more complicated)?",
    "created_at": "2009-04-25T17:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5895#issuecomment-46608",
    "user": "rbeezer"
}
```

Attached patch is a simple approach to limiting the number of snapshots of a worksheet.  But it presents a bit of a dilemma.

(a)  My first version removed any older snapshots necessary to get the total down to 30.  If added to Sage this would have potentially removed many files the first time a user closed up the notebook.  Presumably some folks might want lots of backups, and wouldn't appreciate having many of them deleted.

(b)  The version included here will delete the single oldest snapshot immediately after creation of the 31-st snapshot.  So any huge collection of snapshots will not be touched, and small collections will not grow past 30.  However, if the maximum number is later changed to something smaller, care will be needed to be sure exisiting collections of snapshots don't revert back to growing uncontrollably.

Comments on the above greatly appreciated, and because of this, I don't consider this patch ready for formal review yet.

Obviously, setting `max_snaps = 30` should be user-configurable.  Is it easy to add a new option in `user_conf.py` which could then be reset from the Sage command-line on an instance of the notebook?  Or does this require an "upgrade" of the data structures for a user's record in {{{nb.sobj}} (and therefore becomes much more complicated)?



---

archive/issue_comments_046609.json:
```json
{
    "body": "Attachment\n\nYou *MUST* change this code:\n\n```\n \t1945\t        path = self.snapshot_directory() \n \t1946\t        snapshots = os.listdir(path) \n \t1947\t        snapshots.sort() \n \t1948\t        if len(snapshots) == (max_snaps + 1): \n \t1949\t            os.remove(os.path.join(path, snapshots[0]))\n```\n\n\nChange the line \"if len(snapshots) == (max_snaps + 1):\" to \n\n```\nwhile len(snapshots) > max_snaps:\n```\n\nIt reads better, will work, *and* will avoid subtle race conditions.  The way you have stuff setup in this patch, if there is ever a situation where two snapshots are made, but this function isn't called (e.g., due to some weird race conditions), then one goes back to having potentially thousands of snapshots.\n\nAlso, I see no reason to not delete snapshots from old worksheets too.  In fact, I very much hope that when I apply this patch, then directories with tons of snapshots on sagenb.org and my laptop will have their excessive snapshots deleted, at least if the corresponding worksheets are used.\n\n\nWilliam",
    "created_at": "2009-04-26T01:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5895#issuecomment-46609",
    "user": "was"
}
```

Attachment

You *MUST* change this code:

```
 	1945	        path = self.snapshot_directory() 
 	1946	        snapshots = os.listdir(path) 
 	1947	        snapshots.sort() 
 	1948	        if len(snapshots) == (max_snaps + 1): 
 	1949	            os.remove(os.path.join(path, snapshots[0]))
```


Change the line "if len(snapshots) == (max_snaps + 1):" to 

```
while len(snapshots) > max_snaps:
```

It reads better, will work, *and* will avoid subtle race conditions.  The way you have stuff setup in this patch, if there is ever a situation where two snapshots are made, but this function isn't called (e.g., due to some weird race conditions), then one goes back to having potentially thousands of snapshots.

Also, I see no reason to not delete snapshots from old worksheets too.  In fact, I very much hope that when I apply this patch, then directories with tons of snapshots on sagenb.org and my laptop will have their excessive snapshots deleted, at least if the corresponding worksheets are used.


William



---

archive/issue_comments_046610.json:
```json
{
    "body": "Replying to [comment:2 was]:\n> It reads better, will work, *and* will avoid subtle race conditions.  \n\nYes, that was basically my first version.\n\n>The way you have stuff setup in this patch, if there is ever a situation where two snapshots are made, but this function isn't called (e.g., due to some weird race conditions), then one goes back to having potentially thousands of snapshots.\n\nOr if the value of `max_snaps` is configurable and is decreased at some future time.\n\n> Also, I see no reason to not delete snapshots from old worksheets too.\n\nI guess I worry that it is not very courteous to trash anything in someone's home directory without warning.  ;-)  Other than a note on sage-devel with the announcement of a new version, are there any good ways to put out the word to more \"casual\" users?\n\n> In fact, I very much hope that when I apply this patch, then directories with tons of snapshots on sagenb.org and my laptop will have their excessive snapshots deleted, at least if the corresponding worksheets are used.\n\nI believe that will be the case.  On a personal setup, on shutting down a server, it seems *every* worksheet is examined for a save, but I think there would need to be an edit of the worksheet to get to this new routine.  If this routine was called sooner in `save_worksheet()` then there might be a wholesale purge the first time the server is shut down (though in the long-run the routine would be called many times when it was unnecessary).\n\nThanks for the comments - I'll be back to it tomorrow.",
    "created_at": "2009-04-26T05:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5895#issuecomment-46610",
    "user": "rbeezer"
}
```

Replying to [comment:2 was]:
> It reads better, will work, *and* will avoid subtle race conditions.  

Yes, that was basically my first version.

>The way you have stuff setup in this patch, if there is ever a situation where two snapshots are made, but this function isn't called (e.g., due to some weird race conditions), then one goes back to having potentially thousands of snapshots.

Or if the value of `max_snaps` is configurable and is decreased at some future time.

> Also, I see no reason to not delete snapshots from old worksheets too.

I guess I worry that it is not very courteous to trash anything in someone's home directory without warning.  ;-)  Other than a note on sage-devel with the announcement of a new version, are there any good ways to put out the word to more "casual" users?

> In fact, I very much hope that when I apply this patch, then directories with tons of snapshots on sagenb.org and my laptop will have their excessive snapshots deleted, at least if the corresponding worksheets are used.

I believe that will be the case.  On a personal setup, on shutting down a server, it seems *every* worksheet is examined for a save, but I think there would need to be an edit of the worksheet to get to this new routine.  If this routine was called sooner in `save_worksheet()` then there might be a wholesale purge the first time the server is shut down (though in the long-run the routine would be called many times when it was unnecessary).

Thanks for the comments - I'll be back to it tomorrow.



---

archive/issue_comments_046611.json:
```json
{
    "body": "A compromise would be to not delete anything older than April 28, 2009 (say).  \n\n -- William",
    "created_at": "2009-04-26T05:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5895#issuecomment-46611",
    "user": "was"
}
```

A compromise would be to not delete anything older than April 28, 2009 (say).  

 -- William



---

archive/issue_comments_046612.json:
```json
{
    "body": "New version of patch examines the snapshot directory on each new snapshot added.  A snapshot is deleted if (a) it is not one of the 30 newest, and (b) it was created after May 1, 2009.  So snapshots existing about now have \"amnesty\" and won't get trashed.\n\nAt #5880 tornaria has added a bash script to remove duplicate snapshots (a condition that happened prior to 3.1.4).  I wonder if the script could be extended/modified to delete old snapshots by two other criteria - a maximum number per directory, and perhaps by age (ie delete everything created before a certain date).  This would allow those running server installations to take more drastic action on their own.",
    "created_at": "2009-04-26T20:44:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5895#issuecomment-46612",
    "user": "rbeezer"
}
```

New version of patch examines the snapshot directory on each new snapshot added.  A snapshot is deleted if (a) it is not one of the 30 newest, and (b) it was created after May 1, 2009.  So snapshots existing about now have "amnesty" and won't get trashed.

At #5880 tornaria has added a bash script to remove duplicate snapshots (a condition that happened prior to 3.1.4).  I wonder if the script could be extended/modified to delete old snapshots by two other criteria - a maximum number per directory, and perhaps by age (ie delete everything created before a certain date).  This would allow those running server installations to take more drastic action on their own.



---

archive/issue_comments_046613.json:
```json
{
    "body": "The code in the attached patch is this:\n\n```\n \t1948\t        if len(snapshots) == (max_snaps + 1): \n \t1949\t            os.remove(os.path.join(path, snapshots[0])) \n```\n\n\nIt will not do what you claim: \"A snapshot is deleted if (a) it is not one of the 30 newest, and (b) it was created after May 1, 2009\".  I think perhaps you attached the wrong patch.\n\n> I guess I worry that it is not very courteous to trash anything in \n> someone's home directory without warning. ;-) \n\nI'm discovering that it is also evidently not very courteous to create\n500,000 files in a users home directory :-).\n\nWilliam",
    "created_at": "2009-04-27T12:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5895#issuecomment-46613",
    "user": "was"
}
```

The code in the attached patch is this:

```
 	1948	        if len(snapshots) == (max_snaps + 1): 
 	1949	            os.remove(os.path.join(path, snapshots[0])) 
```


It will not do what you claim: "A snapshot is deleted if (a) it is not one of the 30 newest, and (b) it was created after May 1, 2009".  I think perhaps you attached the wrong patch.

> I guess I worry that it is not very courteous to trash anything in 
> someone's home directory without warning. ;-) 

I'm discovering that it is also evidently not very courteous to create
500,000 files in a users home directory :-).

William



---

archive/issue_comments_046614.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-27T13:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5895#issuecomment-46614",
    "user": "rbeezer"
}
```

Attachment



---

archive/issue_comments_046615.json:
```json
{
    "body": "Replying to [comment:7 was]:\n\n> I think perhaps you attached the wrong patch.\n\nNot the wrong patch - just forgot to attach the new one at all.  The underscore-2 version should be the new one.  Sorry for the trouble.\n\nRob",
    "created_at": "2009-04-27T13:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5895#issuecomment-46615",
    "user": "rbeezer"
}
```

Replying to [comment:7 was]:

> I think perhaps you attached the wrong patch.

Not the wrong patch - just forgot to attach the new one at all.  The underscore-2 version should be the new one.  Sorry for the trouble.

Rob



---

archive/issue_comments_046616.json:
```json
{
    "body": "Replying to [comment:7 was]:\n> I'm discovering that it is also evidently not very courteous to create\n> 500,000 files in a users home directory :-).\n\nPoint taken.  ;-)",
    "created_at": "2009-04-27T17:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5895#issuecomment-46616",
    "user": "rbeezer"
}
```

Replying to [comment:7 was]:
> I'm discovering that it is also evidently not very courteous to create
> 500,000 files in a users home directory :-).

Point taken.  ;-)



---

archive/issue_comments_046617.json:
```json
{
    "body": "I applied this against 4.0.rc2, and it performs as advertised (and doesn't break any doctests in sage/server). I run on a slow filesystem, so I could really use this and some of the related patches. Positive review.",
    "created_at": "2009-05-31T00:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5895#issuecomment-46617",
    "user": "kedlaya"
}
```

I applied this against 4.0.rc2, and it performs as advertised (and doesn't break any doctests in sage/server). I run on a slow filesystem, so I could really use this and some of the related patches. Positive review.



---

archive/issue_comments_046618.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T06:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5895#issuecomment-46618",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_046619.json:
```json
{
    "body": "Merged trac_5895_limit_snapshots_2.patch in 4.0.1.alpha0.",
    "created_at": "2009-06-01T06:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5895#issuecomment-46619",
    "user": "mhansen"
}
```

Merged trac_5895_limit_snapshots_2.patch in 4.0.1.alpha0.
