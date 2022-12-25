# Issue 7138: freetype always builds 32-bit libraries on Solaris, even when SAGE64="yes"

archive/issues_007138.json:
```json
{
    "body": "Assignee: tbd\n\nUsing\n\n* A Sun Blade 2000 running Solaris 10 update 7\n* Sage 4.1.2.rc0\n* gcc 4.4.1\n* SAGE64 exported to \"yes\" \n\nLooking at the directory $SAGE_HOME/local/lib, we can see the *freetype*' libraries are 32-bit, even though SAGE64 was set to \"yes\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/7138\n\n",
    "created_at": "2009-10-06T01:09:25Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "freetype always builds 32-bit libraries on Solaris, even when SAGE64=\"yes\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7138",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Using

* A Sun Blade 2000 running Solaris 10 update 7
* Sage 4.1.2.rc0
* gcc 4.4.1
* SAGE64 exported to "yes" 

Looking at the directory $SAGE_HOME/local/lib, we can see the *freetype*' libraries are 32-bit, even though SAGE64 was set to "yes"

Issue created by migration from https://trac.sagemath.org/ticket/7138





---

archive/issue_comments_059054.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T07:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7138#issuecomment-59054",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059055.json:
```json
{
    "body": "I decided to make only the minimum changes necessary to get this to build 64-bit with gcc. As such, the only change is to spkg-install, so instead of -m64 being added only on Darwin, it is now added whenever SAGE64 is set to yes. \n\nI'll leave a better fix until a later date. See\n\nhttp://boxen.math.washington.edu/home/kirkby/portability/freetype-2.3.5.p2/",
    "created_at": "2010-01-02T07:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7138#issuecomment-59055",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I decided to make only the minimum changes necessary to get this to build 64-bit with gcc. As such, the only change is to spkg-install, so instead of -m64 being added only on Darwin, it is now added whenever SAGE64 is set to yes. 

I'll leave a better fix until a later date. See

http://boxen.math.washington.edu/home/kirkby/portability/freetype-2.3.5.p2/



---

archive/issue_comments_059056.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-02T18:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7138#issuecomment-59056",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059057.json:
```json
{
    "body": "Looks ok for me. Tested on Open Solaris 0906 64 bit and Fedora 12.\n\nI think SPKG.txt needs work, that can be done later by the official maintainer :)\n\nPositive review.\n\nJaap",
    "created_at": "2010-01-02T18:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7138#issuecomment-59057",
    "user": "https://github.com/jaapspies"
}
```

Looks ok for me. Tested on Open Solaris 0906 64 bit and Fedora 12.

I think SPKG.txt needs work, that can be done later by the official maintainer :)

Positive review.

Jaap



---

archive/issue_comments_059058.json:
```json
{
    "body": "I think you mean spkg-install needs further work, not SPKG.txt \n\nBut this will at least allow it to build with gcc on Open Solaris.",
    "created_at": "2010-01-02T18:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7138#issuecomment-59058",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I think you mean spkg-install needs further work, not SPKG.txt 

But this will at least allow it to build with gcc on Open Solaris.



---

archive/issue_comments_059059.json:
```json
{
    "body": "Replying to [comment:6 drkirkby]:\n> I think you mean spkg-install needs further work, not SPKG.txt \n> \n> But this will at least allow it to build with gcc on Open Solaris.\n> \n\nI really mean SPKG.txt as it is not conform the rules!\n\nWilliam is the maintainer so he will make the changes sometime.\n\nspkg-install is ok withe me.\n\nJaap",
    "created_at": "2010-01-02T21:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7138#issuecomment-59059",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:6 drkirkby]:
> I think you mean spkg-install needs further work, not SPKG.txt 
> 
> But this will at least allow it to build with gcc on Open Solaris.
> 

I really mean SPKG.txt as it is not conform the rules!

William is the maintainer so he will make the changes sometime.

spkg-install is ok withe me.

Jaap



---

archive/issue_events_007358.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-01-04T02:01:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7138",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7138#event-7358"
}
```



---

archive/issue_comments_059060.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T02:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7138#issuecomment-59060",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
