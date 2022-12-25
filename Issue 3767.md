# Issue 3767: move jquery into its own spkg

archive/issues_003767.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  wstein @itolkov\n\nWe should move jquery into its own standard spkg (and figure out how to merge the two different copies of it in sage in the process).  \n\nIssue created by migration from https://trac.sagemath.org/ticket/3767\n\n",
    "created_at": "2008-08-03T19:27:58Z",
    "labels": [
        "component: packages: standard",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "move jquery into its own spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3767",
    "user": "https://github.com/timabbott"
}
```
Assignee: mabshoff

CC:  wstein @itolkov

We should move jquery into its own standard spkg (and figure out how to merge the two different copies of it in sage in the process).  

Issue created by migration from https://trac.sagemath.org/ticket/3767





---

archive/issue_comments_026738.json:
```json
{
    "body": "I could only find one copy of jquery in Sage, in data/extcode/notebook/javascript/jquery.  Where is the other copy?",
    "created_at": "2008-10-10T04:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26738",
    "user": "https://github.com/jasongrout"
}
```

I could only find one copy of jquery in Sage, in data/extcode/notebook/javascript/jquery.  Where is the other copy?



---

archive/issue_comments_026739.json:
```json
{
    "body": "Okay, a jquery spkg (that's also been updated to the latest release, which has some really nice performance improvements), is here:\n\nhttp://sage.math.washington.edu/home/jason/jquery-1.2.6.spkg",
    "created_at": "2008-10-10T04:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26739",
    "user": "https://github.com/jasongrout"
}
```

Okay, a jquery spkg (that's also been updated to the latest release, which has some really nice performance improvements), is here:

http://sage.math.washington.edu/home/jason/jquery-1.2.6.spkg



---

archive/issue_comments_026740.json:
```json
{
    "body": "Attachment [remove-jquery.patch](tarball://root/attachments/some-uuid/ticket3767/remove-jquery.patch) by @jasongrout created at 2008-10-10 04:37:26\n\nOkay, apply the patch to the extcode repository, then install the spkg, and you should have an updated jquery.",
    "created_at": "2008-10-10T04:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26740",
    "user": "https://github.com/jasongrout"
}
```

Attachment [remove-jquery.patch](tarball://root/attachments/some-uuid/ticket3767/remove-jquery.patch) by @jasongrout created at 2008-10-10 04:37:26

Okay, apply the patch to the extcode repository, then install the spkg, and you should have an updated jquery.



---

archive/issue_comments_026741.json:
```json
{
    "body": "itolkov, wstein, tabbot, or mabshoff, do you want to review this?",
    "created_at": "2008-10-10T04:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26741",
    "user": "https://github.com/jasongrout"
}
```

itolkov, wstein, tabbot, or mabshoff, do you want to review this?



---

archive/issue_comments_026742.json:
```json
{
    "body": "I just found the other copy of jquery; it's in the jqueryui folder.  jqueryui should also be an spkg...",
    "created_at": "2008-10-10T04:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26742",
    "user": "https://github.com/jasongrout"
}
```

I just found the other copy of jquery; it's in the jqueryui folder.  jqueryui should also be an spkg...



---

archive/issue_comments_026743.json:
```json
{
    "body": "Don't review this just yet; I'm fixing it so that it doesn't install in extcode.",
    "created_at": "2008-10-10T05:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26743",
    "user": "https://github.com/jasongrout"
}
```

Don't review this just yet; I'm fixing it so that it doesn't install in extcode.



---

archive/issue_comments_026744.json:
```json
{
    "body": "Also, incorporate the jeditable and extendedclicks plugins, if the licenses allow.",
    "created_at": "2008-10-10T23:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26744",
    "user": "https://github.com/jasongrout"
}
```

Also, incorporate the jeditable and extendedclicks plugins, if the licenses allow.



---

archive/issue_comments_026745.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-18T04:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26745",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026746.json:
```json
{
    "body": "Changing assignee from mabshoff to @jasongrout.",
    "created_at": "2008-10-18T04:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26746",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from mabshoff to @jasongrout.



---

archive/issue_comments_026747.json:
```json
{
    "body": "This is done at #4267.",
    "created_at": "2008-10-18T04:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26747",
    "user": "https://github.com/jasongrout"
}
```

This is done at #4267.



---

archive/issue_comments_026748.json:
```json
{
    "body": "Ignore any patches of spkgs here.  See #4267 instead.",
    "created_at": "2008-10-18T04:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26748",
    "user": "https://github.com/jasongrout"
}
```

Ignore any patches of spkgs here.  See #4267 instead.



---

archive/issue_comments_026749.json:
```json
{
    "body": "Attachment [jquery-and-friends-spkg.patch](tarball://root/attachments/some-uuid/ticket3767/jquery-and-friends-spkg.patch) by @jasongrout created at 2008-12-05 10:15:26\n\nuse instead of any previous patches",
    "created_at": "2008-12-05T10:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26749",
    "user": "https://github.com/jasongrout"
}
```

Attachment [jquery-and-friends-spkg.patch](tarball://root/attachments/some-uuid/ticket3767/jquery-and-friends-spkg.patch) by @jasongrout created at 2008-12-05 10:15:26

use instead of any previous patches



---

archive/issue_comments_026750.json:
```json
{
    "body": "This depends on #4674.\n\nIgnore any previous comments.  Apply jquery-and-friends-spkg.patch.  The spkgs are here:\n\nhttp://sage.math.washington.edu/home/jason/notebook/jquery-1.2.6.spkg\n\nhttp://sage.math.washington.edu/home/jason/notebook/jqueryui-1.6r807svn.spkg\n\nEventually, we need to also delete the obsolete directories in the extcode repository.",
    "created_at": "2008-12-05T10:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26750",
    "user": "https://github.com/jasongrout"
}
```

This depends on #4674.

Ignore any previous comments.  Apply jquery-and-friends-spkg.patch.  The spkgs are here:

http://sage.math.washington.edu/home/jason/notebook/jquery-1.2.6.spkg

http://sage.math.washington.edu/home/jason/notebook/jqueryui-1.6r807svn.spkg

Eventually, we need to also delete the obsolete directories in the extcode repository.



---

archive/issue_comments_026751.json:
```json
{
    "body": "When this ticket is closed, close #4184.",
    "created_at": "2008-12-05T10:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26751",
    "user": "https://github.com/jasongrout"
}
```

When this ticket is closed, close #4184.



---

archive/issue_comments_026752.json:
```json
{
    "body": "Attachment [jquery-and-friends-spkg.2.patch](tarball://root/attachments/some-uuid/ticket3767/jquery-and-friends-spkg.2.patch) by @jasongrout created at 2008-12-20 21:56:53\n\nApply tclemans  jquery-and-friends-spkg.2.patch patch instead of mine.",
    "created_at": "2008-12-20T21:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26752",
    "user": "https://github.com/jasongrout"
}
```

Attachment [jquery-and-friends-spkg.2.patch](tarball://root/attachments/some-uuid/ticket3767/jquery-and-friends-spkg.2.patch) by @jasongrout created at 2008-12-20 21:56:53

Apply tclemans  jquery-and-friends-spkg.2.patch patch instead of mine.



---

archive/issue_comments_026753.json:
```json
{
    "body": "Positive review due to #4705.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T06:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26753",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review due to #4705.

Cheers,

Michael



---

archive/issue_events_003989.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-19T08:06:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3767#event-3989"
}
```



---

archive/issue_comments_026754.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T08:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26754",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026755.json:
```json
{
    "body": "Merged jquery-and-friends-spkg.2.patch, jquery-1.2.6.spkg and jqueryui-1.6r807svn.spkg in Sage 3.3.alpha0",
    "created_at": "2009-01-19T08:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26755",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged jquery-and-friends-spkg.2.patch, jquery-1.2.6.spkg and jqueryui-1.6r807svn.spkg in Sage 3.3.alpha0
