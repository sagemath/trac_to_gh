# Issue 5291: notebook - Do not save snapshots if nothing has changed

archive/issues_005291.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  timothy.clemans@gmail.com jason-sage@creativetrax.com\n\nThis problem has come up over and over again. Per default Sage saves a snapshot every 3 minutes regardless if anything has changed or not. This can add up to a *lot* of identical snapshots if a computation is left running a long time. And that in turn causes people with quotas to run out of space as reported in \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/8544666b8b18660c#\n\nI am making this a critical issue against 3.3.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5291\n\n",
    "created_at": "2009-02-17T03:44:45Z",
    "labels": [
        "notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "notebook - Do not save snapshots if nothing has changed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5291",
    "user": "mabshoff"
}
```
Assignee: boothby

CC:  timothy.clemans@gmail.com jason-sage@creativetrax.com

This problem has come up over and over again. Per default Sage saves a snapshot every 3 minutes regardless if anything has changed or not. This can add up to a *lot* of identical snapshots if a computation is left running a long time. And that in turn causes people with quotas to run out of space as reported in 

http://groups.google.com/group/sage-devel/browse_thread/thread/8544666b8b18660c#

I am making this a critical issue against 3.3.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5291





---

archive/issue_comments_040659.json:
```json
{
    "body": "Attachment [trac-5291.2.patch](tarball://root/attachments/some-uuid/ticket5291/trac-5291.2.patch) by TimothyClemans created at 2009-02-17 22:03:25",
    "created_at": "2009-02-17T22:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5291#issuecomment-40659",
    "user": "TimothyClemans"
}
```

Attachment [trac-5291.2.patch](tarball://root/attachments/some-uuid/ticket5291/trac-5291.2.patch) by TimothyClemans created at 2009-02-17 22:03:25



---

archive/issue_comments_040660.json:
```json
{
    "body": "I tested it by setting the auto save interval to 10 seconds and clicking undo to see the revisions. Each revision was different.",
    "created_at": "2009-02-17T22:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5291#issuecomment-40660",
    "user": "TimothyClemans"
}
```

I tested it by setting the auto save interval to 10 seconds and clicking undo to see the revisions. Each revision was different.



---

archive/issue_comments_040661.json:
```json
{
    "body": "I'm not sure that this fixes the problem.  Isn't saving to worksheet.txt and saving a snapshot two different things?  If so, then I imagine there will be a time when things are saved to worksheet.txt, and then a snapshot should happen, but wouldn't under this code.",
    "created_at": "2009-02-17T23:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5291#issuecomment-40661",
    "user": "@jasongrout"
}
```

I'm not sure that this fixes the problem.  Isn't saving to worksheet.txt and saving a snapshot two different things?  If so, then I imagine there will be a time when things are saved to worksheet.txt, and then a snapshot should happen, but wouldn't under this code.



---

archive/issue_comments_040662.json:
```json
{
    "body": "save calls save_snapshot which updates worksheet.txt",
    "created_at": "2009-02-17T23:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5291#issuecomment-40662",
    "user": "TimothyClemans"
}
```

save calls save_snapshot which updates worksheet.txt



---

archive/issue_comments_040663.json:
```json
{
    "body": "> save calls save_snapshot which updates worksheet.txt \n\nyep.  Snapshotting *only* ever writes a copy of worksheet.txt. \n\nREVIEW:\n\n* positive review -- but it is not an efficient approach.  \n\nSee Trac #5300 which will be about doing the same thing more efficiently.",
    "created_at": "2009-02-18T00:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5291#issuecomment-40663",
    "user": "@williamstein"
}
```

> save calls save_snapshot which updates worksheet.txt 

yep.  Snapshotting *only* ever writes a copy of worksheet.txt. 

REVIEW:

* positive review -- but it is not an efficient approach.  

See Trac #5300 which will be about doing the same thing more efficiently.



---

archive/issue_comments_040664.json:
```json
{
    "body": "Merged in Sage 3.3.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-18T00:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5291#issuecomment-40664",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc2.

Cheers,

Michael



---

archive/issue_comments_040665.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-18T00:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5291#issuecomment-40665",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040666.json:
```json
{
    "body": "Replying to [comment:7 mabshoff]:\n\nIt appears to me that this code only gets called if (1) there is a worksheet edit, and (2) the time since the last save exceeds the per-user autosave_interval.  If so, checking for a change is always true.  See #5459 for more.",
    "created_at": "2009-03-09T04:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5291#issuecomment-40666",
    "user": "@rbeezer"
}
```

Replying to [comment:7 mabshoff]:

It appears to me that this code only gets called if (1) there is a worksheet edit, and (2) the time since the last save exceeds the per-user autosave_interval.  If so, checking for a change is always true.  See #5459 for more.



---

archive/issue_comments_040667.json:
```json
{
    "body": "Was this even ever merged?  https://github.com/sagemath/sagenb/blob/master/sagenb/notebook/worksheet.py does not have this diff, and I have a version of Sage from 2010 hanging around that does not have it either.  Maybe it was unmerged at some unspecified point...\n\n(Also note that the function in question also has `return` as its first line.)",
    "created_at": "2014-09-18T17:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5291#issuecomment-40667",
    "user": "@kcrisman"
}
```

Was this even ever merged?  https://github.com/sagemath/sagenb/blob/master/sagenb/notebook/worksheet.py does not have this diff, and I have a version of Sage from 2010 hanging around that does not have it either.  Maybe it was unmerged at some unspecified point...

(Also note that the function in question also has `return` as its first line.)
