# Issue 8171: New Cbc spkg with Cplex support

archive/issues_008171.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @malb @haraldschilly\n\nThis new spkg for Cbc includes several new lines in spkg-install to activate CPLEX support in the Coin Library.\n\nIt is to be found at : ~ncohen/cbc-2.3.p2.spkg\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8171\n\n",
    "created_at": "2010-02-03T13:04:07Z",
    "labels": [
        "component: packages: optional"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "New Cbc spkg with Cplex support",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8171",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: tbd

CC:  @malb @haraldschilly

This new spkg for Cbc includes several new lines in spkg-install to activate CPLEX support in the Coin Library.

It is to be found at : ~ncohen/cbc-2.3.p2.spkg

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8171





---

archive/issue_comments_071815.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T13:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71815",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071816.json:
```json
{
    "body": "I just updated the spkg to make it support multithreading through Cbc !\n\nNathann",
    "created_at": "2010-02-26T11:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71816",
    "user": "https://github.com/nathanncohen"
}
```

I just updated the spkg to make it support multithreading through Cbc !

Nathann



---

archive/issue_comments_071817.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-10T23:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71817",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071818.json:
```json
{
    "body": "Since this is new, you need to state whether it is intended to go into experimental or optional. Also, since this is new, you should remove the .p2 from the spkg name and instead call it cbc-2.3.spkg.\n\nIf you update this, before it is committed to Sage, just replace it, or provide a new link. The patch number increments each time a new version is added to Sage - not each time you change your version. \n\nDave",
    "created_at": "2010-03-10T23:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71818",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Since this is new, you need to state whether it is intended to go into experimental or optional. Also, since this is new, you should remove the .p2 from the spkg name and instead call it cbc-2.3.spkg.

If you update this, before it is committed to Sage, just replace it, or provide a new link. The patch number increments each time a new version is added to Sage - not each time you change your version. 

Dave



---

archive/issue_comments_071819.json:
```json
{
    "body": "Sorry, there is some confusion here.\n\nReplying to [comment:3 drkirkby]:\n> Since this is new, you need to state whether it is intended to go into experimental or optional. \n\n\nThe package is intended for optional, because that's where CBC is right now.\n\n> Also, since this is new, you should remove the .p2 from the spkg name and instead \n> call it cbc-2.3.spkg.\n\n\nAs hinted above the SPKG is indeed not new but an update. The CPLEX support in the ticket #8172 is new but *this* ticket only updates the CBC SPKG to work with the new interface. A true update. There is and never will be a CPLEX SPKG because CPLEX is proprietary.\n\nHope that clarifies the situation somewhat.",
    "created_at": "2010-03-10T23:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71819",
    "user": "https://github.com/malb"
}
```

Sorry, there is some confusion here.

Replying to [comment:3 drkirkby]:
> Since this is new, you need to state whether it is intended to go into experimental or optional. 


The package is intended for optional, because that's where CBC is right now.

> Also, since this is new, you should remove the .p2 from the spkg name and instead 
> call it cbc-2.3.spkg.


As hinted above the SPKG is indeed not new but an update. The CPLEX support in the ticket #8172 is new but *this* ticket only updates the CBC SPKG to work with the new interface. A true update. There is and never will be a CPLEX SPKG because CPLEX is proprietary.

Hope that clarifies the situation somewhat.



---

archive/issue_comments_071820.json:
```json
{
    "body": "Yes, it does clarify this. I was under the impression this was a new package, rather than an update to a pre-existing one. \n\nI've stuck it back to needs review. I'm personally unable to review it, as it is outside my level of expertese.",
    "created_at": "2010-03-11T14:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71820",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Yes, it does clarify this. I was under the impression this was a new package, rather than an update to a pre-existing one. 

I've stuck it back to needs review. I'm personally unable to review it, as it is outside my level of expertese.



---

archive/issue_comments_071821.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-11T14:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71821",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071822.json:
```json
{
    "body": "Harald, can you take a look at the SPKG? I tried it and it works but someone needs to check for the basics (hg status, SPKG.txt, etc.) and I'm busy for the next few days.",
    "created_at": "2010-03-11T18:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71822",
    "user": "https://github.com/malb"
}
```

Harald, can you take a look at the SPKG? I tried it and it works but someone needs to check for the basics (hg status, SPKG.txt, etc.) and I'm busy for the next few days.



---

archive/issue_comments_071823.json:
```json
{
    "body": "Finally ..... This package has been tested on t2 (Solaris). It compiles and runs ! :-)\n\nAs soon as this and #8172 are in Sage, it will be possible to work on the inclusion of SCIP !\n\nNathann",
    "created_at": "2010-03-22T23:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71823",
    "user": "https://github.com/nathanncohen"
}
```

Finally ..... This package has been tested on t2 (Solaris). It compiles and runs ! :-)

As soon as this and #8172 are in Sage, it will be possible to work on the inclusion of SCIP !

Nathann



---

archive/issue_comments_071824.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-09T06:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71824",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071825.json:
```json
{
    "body": "Replying to [comment:8 ncohen]:\n> Finally ..... This package has been tested on t2 (Solaris). It compiles and runs ! :-)\n> \n> As soon as this and #8172 are in Sage, it will be possible to work on the inclusion of SCIP !\n> \n> Nathann\n\n\nPositive review, all works, good, but please take care of the update I posted on\n#8172\n\nThanks,\nDima",
    "created_at": "2010-04-09T06:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71825",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:8 ncohen]:
> Finally ..... This package has been tested on t2 (Solaris). It compiles and runs ! :-)
> 
> As soon as this and #8172 are in Sage, it will be possible to work on the inclusion of SCIP !
> 
> Nathann


Positive review, all works, good, but please take care of the update I posted on
#8172

Thanks,
Dima



---

archive/issue_events_019572.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-20T22:55:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8171#event-19572"
}
```



---

archive/issue_comments_071826.json:
```json
{
    "body": "Merged 2010/04/20.",
    "created_at": "2010-04-20T22:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71826",
    "user": "https://github.com/jhpalmieri"
}
```

Merged 2010/04/20.



---

archive/issue_comments_071827.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-20T22:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8171#issuecomment-71827",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
