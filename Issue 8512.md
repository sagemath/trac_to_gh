# Issue 8512: database_stein_watkins_mini uses 'cp -v' which fails on Solaris.

archive/issues_008512.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein\n\nThe optional package  \"database_stein_watkins_mini\" fails to install on Solaris 10, as 'cp' uses an illegal option -v, which is not defined by POSIX. \n\nhttp://www.opengroup.org/onlinepubs/9699919799/utilities/cp.html\n\nSince the GNU version of 'cp' only uses the -v option to show what is being done - from the 'cp' man page on Linux:\n\n\n```\n       -v, --verbose\n              explain what is being done\n```\n\n\nThe -v option can simply be removed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8512\n\n",
    "created_at": "2010-03-12T23:48:03Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "database_stein_watkins_mini uses 'cp -v' which fails on Solaris.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8512",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @williamstein

The optional package  "database_stein_watkins_mini" fails to install on Solaris 10, as 'cp' uses an illegal option -v, which is not defined by POSIX. 

http://www.opengroup.org/onlinepubs/9699919799/utilities/cp.html

Since the GNU version of 'cp' only uses the -v option to show what is being done - from the 'cp' man page on Linux:


```
       -v, --verbose
              explain what is being done
```


The -v option can simply be removed.

Issue created by migration from https://trac.sagemath.org/ticket/8512





---

archive/issue_comments_076737.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-13T00:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8512#issuecomment-76737",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076738.json:
```json
{
    "body": "The solution to this GNUism was very easy - just remove the -v option.\n\nI also added a **very incomplete** SPKG.txt file - previously there was no file called SPKG.txt. I leave it up to William or others with more knowledge to fill this in. It does at least document the change I made. \n\nThe database can be found at http://boxen.math.washington.edu/home/kirkby/optional/database_stein_watkins_mini.p0/database_stein_watkins_mini.p0.spkg\n\nAttached are a diff of the spkg-install and the new SPKG.txt\n\n == Note to the release manager. == \n\nThere is no Mercurial repository - I this will have to be integrated manually.",
    "created_at": "2010-03-13T00:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8512#issuecomment-76738",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The solution to this GNUism was very easy - just remove the -v option.

I also added a **very incomplete** SPKG.txt file - previously there was no file called SPKG.txt. I leave it up to William or others with more knowledge to fill this in. It does at least document the change I made. 

The database can be found at http://boxen.math.washington.edu/home/kirkby/optional/database_stein_watkins_mini.p0/database_stein_watkins_mini.p0.spkg

Attached are a diff of the spkg-install and the new SPKG.txt

 == Note to the release manager. == 

There is no Mercurial repository - I this will have to be integrated manually.



---

archive/issue_comments_076739.json:
```json
{
    "body": "Brand new (but mostly incomplete) SPKG.txt",
    "created_at": "2010-03-13T00:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8512#issuecomment-76739",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Brand new (but mostly incomplete) SPKG.txt



---

archive/issue_comments_076740.json:
```json
{
    "body": "Attachment [SPKG.txt](tarball://root/attachments/some-uuid/ticket8512/SPKG.txt) by drkirkby created at 2010-03-13 00:27:01\n\nModified spkg-install, removing the '-v' option to 'cp'",
    "created_at": "2010-03-13T00:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8512#issuecomment-76740",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [SPKG.txt](tarball://root/attachments/some-uuid/ticket8512/SPKG.txt) by drkirkby created at 2010-03-13 00:27:01

Modified spkg-install, removing the '-v' option to 'cp'



---

archive/issue_comments_076741.json:
```json
{
    "body": "Attachment [stein-watkins-ecdb.patch](tarball://root/attachments/some-uuid/ticket8512/stein-watkins-ecdb.patch) by drkirkby created at 2010-03-13 00:30:31",
    "created_at": "2010-03-13T00:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8512#issuecomment-76741",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [stein-watkins-ecdb.patch](tarball://root/attachments/some-uuid/ticket8512/stein-watkins-ecdb.patch) by drkirkby created at 2010-03-13 00:30:31



---

archive/issue_comments_076742.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2010-03-13T23:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8512#issuecomment-76742",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_076743.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-02T22:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8512#issuecomment-76743",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076744.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-07T05:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8512#issuecomment-76744",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_008692.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-07T05:06:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8512",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8512#event-8692"
}
```
