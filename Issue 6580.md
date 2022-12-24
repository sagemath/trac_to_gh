# Issue 6580: ratpoints -- this must be fixed to build with gcc-3.4.x

archive/issues_006580.json:
```json
{
    "body": "Assignee: rlmillster\n\nWe let ratpoints get in, and nobody thought to check that it actually builds with gcc-3.4.x.  Well, it doesn't.  This needs to get fixed. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6580\n\n",
    "created_at": "2009-07-21T16:40:22Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "ratpoints -- this must be fixed to build with gcc-3.4.x",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6580",
    "user": "was"
}
```
Assignee: rlmillster

We let ratpoints get in, and nobody thought to check that it actually builds with gcc-3.4.x.  Well, it doesn't.  This needs to get fixed. 

Issue created by migration from https://trac.sagemath.org/ticket/6580





---

archive/issue_comments_053717.json:
```json
{
    "body": "If someone would like to point me to a machine with gcc-3.4.x, I'd gladly troubleshoot this.",
    "created_at": "2009-07-21T20:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6580#issuecomment-53717",
    "user": "rlm"
}
```

If someone would like to point me to a machine with gcc-3.4.x, I'd gladly troubleshoot this.



---

archive/issue_comments_053718.json:
```json
{
    "body": "Changing assignee from rlmillster to rlm.",
    "created_at": "2009-07-21T20:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6580#issuecomment-53718",
    "user": "rlm"
}
```

Changing assignee from rlmillster to rlm.



---

archive/issue_comments_053719.json:
```json
{
    "body": "I want to start using ratpoints in some elliptic curve code as it is so efficient.  Should I wait until it compiles on these other machines?\n\nIn the meantime the interface to ratpoints which rlm wrote can be enhanced in various ways, (e.g. to list only integral points) and that need not wait.",
    "created_at": "2009-08-16T20:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6580#issuecomment-53719",
    "user": "cremona"
}
```

I want to start using ratpoints in some elliptic curve code as it is so efficient.  Should I wait until it compiles on these other machines?

In the meantime the interface to ratpoints which rlm wrote can be enhanced in various ways, (e.g. to list only integral points) and that need not wait.



---

archive/issue_comments_053720.json:
```json
{
    "body": "At #7021, drkirkby updates prereq to 0.4 and writes \"If gcc is used as the C compiler, the configure script checks it is at least gcc 4.0.1.\" Does this updated spkg invalidate this ticket? Here's a conversation on IRC:\n\n```\n23:14 < mvngu> williamstein: At #7021, I see drkirkby's note \"If gcc is used as \n               the C compiler, the configure script checks it is at least gcc \n               4.0.1\". This makes me wonder about the GCC 3.4.x requirement at \n               #6580.\n23:14 < williamstein> good point.\n23:15 < williamstein> maybe we should just move ahead and forget about \n                      supporting gcc-3.4.\n23:15 < williamstein> I would be ok with that.\n23:15 < williamstein> in which case 6580 could be invalidated.\n23:15 < mvngu> williamstein: I don't know of any machine using GCC 3.4.x.\n23:15 < williamstein> yep\n23:15 < williamstein> that's why we didn't notice until after the release.\n```\n",
    "created_at": "2009-09-27T06:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6580#issuecomment-53720",
    "user": "mvngu"
}
```

At #7021, drkirkby updates prereq to 0.4 and writes "If gcc is used as the C compiler, the configure script checks it is at least gcc 4.0.1." Does this updated spkg invalidate this ticket? Here's a conversation on IRC:

```
23:14 < mvngu> williamstein: At #7021, I see drkirkby's note "If gcc is used as 
               the C compiler, the configure script checks it is at least gcc 
               4.0.1". This makes me wonder about the GCC 3.4.x requirement at 
               #6580.
23:14 < williamstein> good point.
23:15 < williamstein> maybe we should just move ahead and forget about 
                      supporting gcc-3.4.
23:15 < williamstein> I would be ok with that.
23:15 < williamstein> in which case 6580 could be invalidated.
23:15 < mvngu> williamstein: I don't know of any machine using GCC 3.4.x.
23:15 < williamstein> yep
23:15 < williamstein> that's why we didn't notice until after the release.
```




---

archive/issue_comments_053721.json:
```json
{
    "body": "If anyone wants to find a machine with gcc 3.4.x, then 't2' has it. Just make sure that the GNU compilers at /usr/sfw/bin/ are first in your path, as specifying CC and CXX will not work, as numerous packages ignore CC and CXX.\n\nDave",
    "created_at": "2009-09-28T10:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6580#issuecomment-53721",
    "user": "drkirkby"
}
```

If anyone wants to find a machine with gcc 3.4.x, then 't2' has it. Just make sure that the GNU compilers at /usr/sfw/bin/ are first in your path, as specifying CC and CXX will not work, as numerous packages ignore CC and CXX.

Dave



---

archive/issue_comments_053722.json:
```json
{
    "body": "Given that this is three years old and Sage does now build on Solaris and that Sage even builds its own GCC if we have too old of a GCC (in fact, even for newer ones than 4.0.1), this ticket should probably be closed.",
    "created_at": "2012-06-01T19:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6580#issuecomment-53722",
    "user": "kcrisman"
}
```

Given that this is three years old and Sage does now build on Solaris and that Sage even builds its own GCC if we have too old of a GCC (in fact, even for newer ones than 4.0.1), this ticket should probably be closed.



---

archive/issue_comments_053723.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-01T19:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6580#issuecomment-53723",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053724.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-01T19:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6580#issuecomment-53724",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053725.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2012-06-02T12:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6580#issuecomment-53725",
    "user": "jdemeyer"
}
```

Resolution: wontfix
