# Issue 7894: bzip2 does not always clear up before building

archive/issues_007894.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nI just noticed something odd on Solaris 8. bzip2 built fine, but I started the build after modifying one a file in 'prereq'. Then I get:\n\n```\ncp -f libbz2.a /export/home/drkirkby/sage-4.3/spkg/../local/lib\nchmod a+r /export/home/drkirkby/sage-4.3/spkg/../local/lib/libbz2.a\ncp -f bzgrep /export/home/drkirkby/sage-4.3/spkg/../local/bin/bzgrep\nln -s -f /export/home/drkirkby/sage-4.3/spkg/../local/bin/bzgrep /export/home/drkirkby/sage-4.3/spkg/../local/bin/bzegrep\nln: cannot create /export/home/drkirkby/sage-4.3/spkg/../local/bin/bzegrep: File exists\nmake[2]: *** [install] Error 2\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/bzip2-1.0.5'\nError installing bzip2\nmake[1]: *** [installed/bzip2-1.0.5] Error 1\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg'\n\nreal    0m13.366s\nuser    0m7.790s\nsys     0m3.090s\nError building Sage. \n```\n\nIt actually leaves several files starting with the letters 'bz' in local/bin. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7894\n\n",
    "closed_at": "2014-01-10T08:49:00Z",
    "created_at": "2010-01-11T06:16:45Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bzip2 does not always clear up before building",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7894",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

I just noticed something odd on Solaris 8. bzip2 built fine, but I started the build after modifying one a file in 'prereq'. Then I get:

```
cp -f libbz2.a /export/home/drkirkby/sage-4.3/spkg/../local/lib
chmod a+r /export/home/drkirkby/sage-4.3/spkg/../local/lib/libbz2.a
cp -f bzgrep /export/home/drkirkby/sage-4.3/spkg/../local/bin/bzgrep
ln -s -f /export/home/drkirkby/sage-4.3/spkg/../local/bin/bzgrep /export/home/drkirkby/sage-4.3/spkg/../local/bin/bzegrep
ln: cannot create /export/home/drkirkby/sage-4.3/spkg/../local/bin/bzegrep: File exists
make[2]: *** [install] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/bzip2-1.0.5'
Error installing bzip2
make[1]: *** [installed/bzip2-1.0.5] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg'

real    0m13.366s
user    0m7.790s
sys     0m3.090s
Error building Sage. 
```

It actually leaves several files starting with the letters 'bz' in local/bin. 

Issue created by migration from https://trac.sagemath.org/ticket/7894





---

archive/issue_events_018874.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7894",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7894#event-18874"
}
```



---

archive/issue_comments_068554.json:
```json
{
    "body": "Fixed in #12102",
    "created_at": "2014-01-09T09:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7894#issuecomment-68554",
    "user": "https://github.com/jdemeyer"
}
```

Fixed in #12102



---

archive/issue_events_018875.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-01-09T09:32:56Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7894",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7894#event-18875"
}
```



---

archive/issue_events_018876.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-01-09T09:32:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7894",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7894#event-18876"
}
```



---

archive/issue_comments_068555.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-01-09T09:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7894#issuecomment-68555",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068556.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-01-09T09:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7894#issuecomment-68556",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_018877.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-01-10T08:49:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7894",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7894#event-18877"
}
```



---

archive/issue_comments_068557.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-01-10T08:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7894#issuecomment-68557",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate
