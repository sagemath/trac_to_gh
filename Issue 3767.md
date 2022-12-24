# Issue 3767: move jquery into its own spkg

archive/issues_003767.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  wstein itolkov\n\nWe should move jquery into its own standard spkg (and figure out how to merge the two different copies of it in sage in the process).  \n\nIssue created by migration from https://trac.sagemath.org/ticket/3767\n\n",
    "created_at": "2008-08-03T19:27:58Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "title": "move jquery into its own spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3767",
    "user": "tabbott"
}
```
Assignee: mabshoff

CC:  wstein itolkov

We should move jquery into its own standard spkg (and figure out how to merge the two different copies of it in sage in the process).  

Issue created by migration from https://trac.sagemath.org/ticket/3767





---

archive/issue_comments_026795.json:
```json
{
    "body": "I could only find one copy of jquery in Sage, in data/extcode/notebook/javascript/jquery.  Where is the other copy?",
    "created_at": "2008-10-10T04:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26795",
    "user": "jason"
}
```

I could only find one copy of jquery in Sage, in data/extcode/notebook/javascript/jquery.  Where is the other copy?



---

archive/issue_comments_026796.json:
```json
{
    "body": "Okay, a jquery spkg (that's also been updated to the latest release, which has some really nice performance improvements), is here:\n\nhttp://sage.math.washington.edu/home/jason/jquery-1.2.6.spkg",
    "created_at": "2008-10-10T04:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26796",
    "user": "jason"
}
```

Okay, a jquery spkg (that's also been updated to the latest release, which has some really nice performance improvements), is here:

http://sage.math.washington.edu/home/jason/jquery-1.2.6.spkg



---

archive/issue_comments_026797.json:
```json
{
    "body": "Attachment [remove-jquery.patch](tarball://root/attachments/some-uuid/ticket3767/remove-jquery.patch) by jason created at 2008-10-10 04:37:26\n\nOkay, apply the patch to the extcode repository, then install the spkg, and you should have an updated jquery.",
    "created_at": "2008-10-10T04:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26797",
    "user": "jason"
}
```

Attachment [remove-jquery.patch](tarball://root/attachments/some-uuid/ticket3767/remove-jquery.patch) by jason created at 2008-10-10 04:37:26

Okay, apply the patch to the extcode repository, then install the spkg, and you should have an updated jquery.



---

archive/issue_comments_026798.json:
```json
{
    "body": "itolkov, wstein, tabbot, or mabshoff, do you want to review this?",
    "created_at": "2008-10-10T04:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26798",
    "user": "jason"
}
```

itolkov, wstein, tabbot, or mabshoff, do you want to review this?



---

archive/issue_comments_026799.json:
```json
{
    "body": "I just found the other copy of jquery; it's in the jqueryui folder.  jqueryui should also be an spkg...",
    "created_at": "2008-10-10T04:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26799",
    "user": "jason"
}
```

I just found the other copy of jquery; it's in the jqueryui folder.  jqueryui should also be an spkg...



---

archive/issue_comments_026800.json:
```json
{
    "body": "Don't review this just yet; I'm fixing it so that it doesn't install in extcode.",
    "created_at": "2008-10-10T05:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26800",
    "user": "jason"
}
```

Don't review this just yet; I'm fixing it so that it doesn't install in extcode.



---

archive/issue_comments_026801.json:
```json
{
    "body": "Also, incorporate the jeditable and extendedclicks plugins, if the licenses allow.",
    "created_at": "2008-10-10T23:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26801",
    "user": "jason"
}
```

Also, incorporate the jeditable and extendedclicks plugins, if the licenses allow.



---

archive/issue_comments_026802.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-18T04:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26802",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026803.json:
```json
{
    "body": "Changing assignee from mabshoff to jason.",
    "created_at": "2008-10-18T04:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26803",
    "user": "jason"
}
```

Changing assignee from mabshoff to jason.



---

archive/issue_comments_026804.json:
```json
{
    "body": "This is done at #4267.",
    "created_at": "2008-10-18T04:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26804",
    "user": "jason"
}
```

This is done at #4267.



---

archive/issue_comments_026805.json:
```json
{
    "body": "Ignore any patches of spkgs here.  See #4267 instead.",
    "created_at": "2008-10-18T04:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26805",
    "user": "jason"
}
```

Ignore any patches of spkgs here.  See #4267 instead.



---

archive/issue_comments_026806.json:
```json
{
    "body": "Attachment [jquery-and-friends-spkg.patch](tarball://root/attachments/some-uuid/ticket3767/jquery-and-friends-spkg.patch) by jason created at 2008-12-05 10:15:26\n\nuse instead of any previous patches",
    "created_at": "2008-12-05T10:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26806",
    "user": "jason"
}
```

Attachment [jquery-and-friends-spkg.patch](tarball://root/attachments/some-uuid/ticket3767/jquery-and-friends-spkg.patch) by jason created at 2008-12-05 10:15:26

use instead of any previous patches



---

archive/issue_comments_026807.json:
```json
{
    "body": "This depends on #4674.\n\nIgnore any previous comments.  Apply jquery-and-friends-spkg.patch.  The spkgs are here:\n\nhttp://sage.math.washington.edu/home/jason/notebook/jquery-1.2.6.spkg\n\nhttp://sage.math.washington.edu/home/jason/notebook/jqueryui-1.6r807svn.spkg\n\nEventually, we need to also delete the obsolete directories in the extcode repository.",
    "created_at": "2008-12-05T10:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26807",
    "user": "jason"
}
```

This depends on #4674.

Ignore any previous comments.  Apply jquery-and-friends-spkg.patch.  The spkgs are here:

http://sage.math.washington.edu/home/jason/notebook/jquery-1.2.6.spkg

http://sage.math.washington.edu/home/jason/notebook/jqueryui-1.6r807svn.spkg

Eventually, we need to also delete the obsolete directories in the extcode repository.



---

archive/issue_comments_026808.json:
```json
{
    "body": "When this ticket is closed, close #4184.",
    "created_at": "2008-12-05T10:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26808",
    "user": "jason"
}
```

When this ticket is closed, close #4184.



---

archive/issue_comments_026809.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2008-12-05T10:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26809",
    "user": "jason"
}
```

Changing priority from minor to major.



---

archive/issue_comments_026810.json:
```json
{
    "body": "Attachment [jquery-and-friends-spkg.2.patch](tarball://root/attachments/some-uuid/ticket3767/jquery-and-friends-spkg.2.patch) by jason created at 2008-12-20 21:56:53\n\nApply tclemans  jquery-and-friends-spkg.2.patch patch instead of mine.",
    "created_at": "2008-12-20T21:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26810",
    "user": "jason"
}
```

Attachment [jquery-and-friends-spkg.2.patch](tarball://root/attachments/some-uuid/ticket3767/jquery-and-friends-spkg.2.patch) by jason created at 2008-12-20 21:56:53

Apply tclemans  jquery-and-friends-spkg.2.patch patch instead of mine.



---

archive/issue_comments_026811.json:
```json
{
    "body": "Positive review due to #4705.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T06:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26811",
    "user": "mabshoff"
}
```

Positive review due to #4705.

Cheers,

Michael



---

archive/issue_comments_026812.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T08:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26812",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026813.json:
```json
{
    "body": "Merged jquery-and-friends-spkg.2.patch, jquery-1.2.6.spkg and jqueryui-1.6r807svn.spkg in Sage 3.3.alpha0",
    "created_at": "2009-01-19T08:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3767#issuecomment-26813",
    "user": "mabshoff"
}
```

Merged jquery-and-friends-spkg.2.patch, jquery-1.2.6.spkg and jqueryui-1.6r807svn.spkg in Sage 3.3.alpha0
