# Issue 7031: singular believes the Sun C++ compiler is broken.

archive/issues_007031.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  dimpase\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used  (#7021)\n\nCC was set to the Sun C compler, and CXX to the Sun C++ compiler. The singular configure script does not believe the Sun C++ compiler can create executables. This is the same sort of error as seen in quaddouble-2.2.p9 #7030. \n\nThis time the problem is easy to diagnose. The test is used adds the option -fPIC when trying to test the C++ compiler. But -fPIC is a GNU-specific option - it is not acceptable to the Sun C++ compiler. Instead  -xcode=pic32, -KPIC or -PIC would work, but not -fPIC. \n\nIt's clearly dumb to send a GNU specific option to test a C++ compiler unless you are 100% sure the C++ compiler is the GNU C++ compiler. \n\n\n```\nchecking for c++... /opt/xxxsunstudio12.1/bin/CC\nchecking whether the C++ compiler (/opt/xxxsunstudio12.1/bin/CC  -O3 -g -fPIC ) works... no\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7031\n\n",
    "created_at": "2009-09-27T14:14:02Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "singular believes the Sun C++ compiler is broken.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7031",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  dimpase

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used  (#7021)

CC was set to the Sun C compler, and CXX to the Sun C++ compiler. The singular configure script does not believe the Sun C++ compiler can create executables. This is the same sort of error as seen in quaddouble-2.2.p9 #7030. 

This time the problem is easy to diagnose. The test is used adds the option -fPIC when trying to test the C++ compiler. But -fPIC is a GNU-specific option - it is not acceptable to the Sun C++ compiler. Instead  -xcode=pic32, -KPIC or -PIC would work, but not -fPIC. 

It's clearly dumb to send a GNU specific option to test a C++ compiler unless you are 100% sure the C++ compiler is the GNU C++ compiler. 


```
checking for c++... /opt/xxxsunstudio12.1/bin/CC
checking whether the C++ compiler (/opt/xxxsunstudio12.1/bin/CC  -O3 -g -fPIC ) works... no
```




Issue created by migration from https://trac.sagemath.org/ticket/7031





---

archive/issue_comments_058230.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7031#issuecomment-58230",
    "user": "mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_058231.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7031#issuecomment-58231",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058232.json:
```json
{
    "body": "The goal of these tickets is laudable, but:\n\n* We need at least one user who is able to test.\n* The package/OS information on this ticket is outdated beyond usefulness.\n* Upstream is a better place to report portability issues these days.",
    "created_at": "2020-07-12T20:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7031#issuecomment-58232",
    "user": "mjo"
}
```

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.



---

archive/issue_comments_058233.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-12T20:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7031#issuecomment-58233",
    "user": "mjo"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058234.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7031#issuecomment-58234",
    "user": "chapoton"
}
```

Resolution: invalid



---

archive/issue_comments_058235.json:
```json
{
    "body": "Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7031#issuecomment-58235",
    "user": "chapoton"
}
```

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.
