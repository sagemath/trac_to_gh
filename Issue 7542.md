# Issue 7542: Security issues in gnutls-2.2.1

archive/issues_007542.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  david.kirkby@onetel.net\n\nAccording to the Simon Josefsson, there are security issues with version 2.2.1. \n\n*\"Unless you back-port security fixes to 2.2.x, you want to use the 2.8.x release to get proper security fixes.\"*\n\nThere are two other issues with 2.2.1 I am aware of. \n* #7387 gnutls not building on OpenSolaris (x86)\n* #7511 gnutls-2.2.1 fails to build on HP-UX \n\nI do not know exactly what the bug is, but I'm told there are security issues with this release.\n\nI tried to create a .spkg from the latest release, but that failed to build on Solaris 10 (SPARC) so was worst than the older release, though the developers tell me it should be ok. \n\ndave \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7542\n\n",
    "created_at": "2009-11-27T14:11:52Z",
    "labels": [
        "component: cryptography",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Security issues in gnutls-2.2.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7542",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: mvngu

CC:  david.kirkby@onetel.net

According to the Simon Josefsson, there are security issues with version 2.2.1. 

*"Unless you back-port security fixes to 2.2.x, you want to use the 2.8.x release to get proper security fixes."*

There are two other issues with 2.2.1 I am aware of. 
* #7387 gnutls not building on OpenSolaris (x86)
* #7511 gnutls-2.2.1 fails to build on HP-UX 

I do not know exactly what the bug is, but I'm told there are security issues with this release.

I tried to create a .spkg from the latest release, but that failed to build on Solaris 10 (SPARC) so was worst than the older release, though the developers tell me it should be ok. 

dave 


Issue created by migration from https://trac.sagemath.org/ticket/7542





---

archive/issue_comments_063881.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-10-05T09:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7542#issuecomment-63881",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_comments_063882.json:
```json
{
    "body": "GNUTLS is no longer part of Sage.",
    "created_at": "2012-10-05T09:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7542#issuecomment-63882",
    "user": "https://github.com/jdemeyer"
}
```

GNUTLS is no longer part of Sage.



---

archive/issue_events_007772.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-10-05T09:13:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7542",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7542#event-7772"
}
```
