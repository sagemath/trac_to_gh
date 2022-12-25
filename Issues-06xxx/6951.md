# Issue 6951: [with spkg, positive review] Singular fails to build on t2.math with GCC

archive/issues_006951.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @malb drkirkby\n\nAs the subject says. I have attached an install log of Sage 4.1.2.alpha1, building on t2.math with GCC 4.4.1.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6951\n\n",
    "closed_at": "2009-09-27T04:02:05Z",
    "created_at": "2009-09-17T21:39:42Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with spkg, positive review] Singular fails to build on t2.math with GCC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6951",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mabshoff

CC:  @malb drkirkby

As the subject says. I have attached an install log of Sage 4.1.2.alpha1, building on t2.math with GCC 4.4.1.

Issue created by migration from https://trac.sagemath.org/ticket/6951





---

archive/issue_comments_057376.json:
```json
{
    "body": "Attachment [install-4.1.2.alpha1-t2.math.log.bz2](tarball://root/attachments/some-uuid/ticket6951/install-4.1.2.alpha1-t2.math.log.bz2) by mvngu created at 2009-09-17 21:40:37\n\ninstall log for Sage 4.1.2.alpha1 on t2.math with GCC 4.4.1",
    "created_at": "2009-09-17T21:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6951#issuecomment-57376",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [install-4.1.2.alpha1-t2.math.log.bz2](tarball://root/attachments/some-uuid/ticket6951/install-4.1.2.alpha1-t2.math.log.bz2) by mvngu created at 2009-09-17 21:40:37

install log for Sage 4.1.2.alpha1 on t2.math with GCC 4.4.1



---

archive/issue_comments_057377.json:
```json
{
    "body": "Here is the relevant portion:\n\n```\nfor file in *.h; do \\\n../.././install-sh -c $file /scratch/mvngu/sage-4.1.2.alpha1-6945-readline-cliquer-ecl/local/include/singular; \\\ndone\n/bin/sh: ../.././install-sh: not found\n```\n\nIIRC Dave fixed this before but I must have missed to include his fix (the update was a bit chaotic because quite a few fixed from different people went in). David, would you mind reminding me how to fix this?",
    "created_at": "2009-09-17T21:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6951#issuecomment-57377",
    "user": "https://github.com/malb"
}
```

Here is the relevant portion:

```
for file in *.h; do \
../.././install-sh -c $file /scratch/mvngu/sage-4.1.2.alpha1-6945-readline-cliquer-ecl/local/include/singular; \
done
/bin/sh: ../.././install-sh: not found
```

IIRC Dave fixed this before but I must have missed to include his fix (the update was a bit chaotic because quite a few fixed from different people went in). David, would you mind reminding me how to fix this?



---

archive/issue_comments_057378.json:
```json
{
    "body": "Briefly, we're missing a file \"install-sh\" for Sun, and possibly a switch change from -O2 to -O0 on Itanium; copied from my post at the sage-devel thread:\nHi Minh,\n\nobviously (look at your own trace output), you are talking about\n\"singular-3-1-0-4-20090818.spkg\", not\n\"singular-3-1-0-4-20090723.spkg\".\n\nJust looking at the top entries of the \"SPKG.txt\" file of the old\n(Sage-4.1.1) \"singular-3-1-0-2-20090620.p0.spkg\", and of the current\nSage-4.1.2-alpha \"singular-3-1-0-4-20090818.spkg\", shows what the\nproblem is, that the latter spkg might be broken also on Itanium\n(ia64, see trac #6360 and #6240) i.e. not only on Sun, and what to do\nabout it.\nI can look into building a new spkg with the necessary fixes tomorrow,\nor the day after, if nobody beats me to it.\n\nCheers,\nGeorg",
    "created_at": "2009-09-22T20:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6951#issuecomment-57378",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Briefly, we're missing a file "install-sh" for Sun, and possibly a switch change from -O2 to -O0 on Itanium; copied from my post at the sage-devel thread:
Hi Minh,

obviously (look at your own trace output), you are talking about
"singular-3-1-0-4-20090818.spkg", not
"singular-3-1-0-4-20090723.spkg".

Just looking at the top entries of the "SPKG.txt" file of the old
(Sage-4.1.1) "singular-3-1-0-2-20090620.p0.spkg", and of the current
Sage-4.1.2-alpha "singular-3-1-0-4-20090818.spkg", shows what the
problem is, that the latter spkg might be broken also on Itanium
(ia64, see trac #6360 and #6240) i.e. not only on Sun, and what to do
about it.
I can look into building a new spkg with the necessary fixes tomorrow,
or the day after, if nobody beats me to it.

Cheers,
Georg



---

archive/issue_comments_057379.json:
```json
{
    "body": "New \".p0\" spkg is up at:\n\nhttp://sage.math.washington.edu/home/weberg/spkg/singular-3-1-0-4-20090818.p0.spkg",
    "created_at": "2009-09-24T22:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6951#issuecomment-57379",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

New ".p0" spkg is up at:

http://sage.math.washington.edu/home/weberg/spkg/singular-3-1-0-4-20090818.p0.spkg



---

archive/issue_events_016349.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-27T04:02:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6951",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6951#event-16349"
}
```



---

archive/issue_comments_057380.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-27T04:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6951#issuecomment-57380",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057381.json:
```json
{
    "body": "See my report at #6849. Also builds on t2.math. Now the compilation on t2.math fails when building the package sage-4.1.2.alpha2.spkg. Positive review.",
    "created_at": "2009-09-27T04:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6951#issuecomment-57381",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See my report at #6849. Also builds on t2.math. Now the compilation on t2.math fails when building the package sage-4.1.2.alpha2.spkg. Positive review.



---

archive/issue_comments_057382.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T11:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6951#issuecomment-57382",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
