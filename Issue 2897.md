# Issue 2897: [with new spkg] GAP: replace guava 3.4 by new and improved guava 3.4

archive/issues_002897.json:
```json
{
    "body": "Assignee: @rlmill\n\nThere was a small bug in the previous version of guava 3.4 which caused it to fail the (GAP) guava.tst file. This version is fixed. Also, some file permissions were \"wrong\" and those are fixed. The SPKG.txt file was updated. Other than these, the spkg is the same. It has been copied to \nhttp://sage.math.washington.edu/home/wdj/patches/gap-4.4.10.p6.spkg and was\ntested using sage -f. Seems to work fine.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2897\n\n",
    "created_at": "2008-04-12T14:42:49Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with new spkg] GAP: replace guava 3.4 by new and improved guava 3.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2897",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @rlmill

There was a small bug in the previous version of guava 3.4 which caused it to fail the (GAP) guava.tst file. This version is fixed. Also, some file permissions were "wrong" and those are fixed. The SPKG.txt file was updated. Other than these, the spkg is the same. It has been copied to 
http://sage.math.washington.edu/home/wdj/patches/gap-4.4.10.p6.spkg and was
tested using sage -f. Seems to work fine.

Issue created by migration from https://trac.sagemath.org/ticket/2897





---

archive/issue_comments_019898.json:
```json
{
    "body": "Two issue: Somebody is moving back in time. \n\n```\n### gap-4.4.10.p3 (David Joyner, March 30th, 2008)\n * replace guava 3.4 by guava 3.4 with fixed Makefile.in\n\n### gap-4.4.10.p5 (Michael Abshoff, April 1st, 2008)\n * Debianize GAP spkg (Tim Abbott, #2756)\n```\n\nDavid, are you a terminator? ;)\n\nThe other thing is that the changes to SPKG.txt were not checked into the main spkg repo. The slightly updated spkg builds fine and passes doctests for me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-12T16:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2897#issuecomment-19898",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Two issue: Somebody is moving back in time. 

```
### gap-4.4.10.p3 (David Joyner, March 30th, 2008)
 * replace guava 3.4 by guava 3.4 with fixed Makefile.in

### gap-4.4.10.p5 (Michael Abshoff, April 1st, 2008)
 * Debianize GAP spkg (Tim Abbott, #2756)
```

David, are you a terminator? ;)

The other thing is that the changes to SPKG.txt were not checked into the main spkg repo. The slightly updated spkg builds fine and passes doctests for me. Positive review.

Cheers,

Michael



---

archive/issue_comments_019899.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T16:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2897#issuecomment-19899",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019900.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-12T16:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2897#issuecomment-19900",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_events_003095.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-12T16:10:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2897",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2897#event-3095"
}
```
