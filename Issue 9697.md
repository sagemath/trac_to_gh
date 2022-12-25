# Issue 9697: DS_Store garbage in flint spkg

archive/issues_009697.json:
```json
{
    "body": "Assignee: pdehaye\n\nNew **spkg**: [http://boxen.math.washington.edu/home/pdehaye/spkg/flint-1.5.2.p2.spkg](http://boxen.math.washington.edu/home/pdehaye/spkg/flint-1.5.2.p2.spkg)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9697\n\n",
    "closed_at": "2012-10-17T20:52:18Z",
    "created_at": "2010-08-06T17:33:52Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.4",
    "title": "DS_Store garbage in flint spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9697",
    "user": "https://github.com/rlmill"
}
```
Assignee: pdehaye

New **spkg**: [http://boxen.math.washington.edu/home/pdehaye/spkg/flint-1.5.2.p2.spkg](http://boxen.math.washington.edu/home/pdehaye/spkg/flint-1.5.2.p2.spkg)

Issue created by migration from https://trac.sagemath.org/ticket/9697





---

archive/issue_comments_094090.json:
```json
{
    "body": "I have reported a similar error about flint-1.5.2.p1.spkg at https://groups.google.com/d/topic/sage-release/52Hz8-G3TWA/discussion",
    "created_at": "2012-10-15T21:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9697#issuecomment-94090",
    "user": "https://trac.sagemath.org/admin/accounts/users/pdehaye"
}
```

I have reported a similar error about flint-1.5.2.p1.spkg at https://groups.google.com/d/topic/sage-release/52Hz8-G3TWA/discussion



---

archive/issue_events_024228.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/pdehaye",
    "created_at": "2012-10-15T21:47:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "milestone": "sage-5.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9697#event-24228"
}
```



---

archive/issue_comments_094091.json:
```json
{
    "body": "Changing assignee from tbd to pdehaye.",
    "created_at": "2012-10-15T21:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9697#issuecomment-94091",
    "user": "https://trac.sagemath.org/admin/accounts/users/pdehaye"
}
```

Changing assignee from tbd to pdehaye.



---

archive/issue_comments_094092.json:
```json
{
    "body": "Suggested fix: http://boxen.math.washington.edu/home/pdehaye/spkg/flint-1.5.2.p2.spkg\n\nBeware, this is my first spkg. I removed the offending file, modified SPKG.txt, and the mercurial log. I then made the spkg using sage _5.0_ as this is the last version I have running on my system. It looks like sage-spkg has not been changed since, so that should not be a problem.",
    "created_at": "2012-10-15T21:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9697#issuecomment-94092",
    "user": "https://trac.sagemath.org/admin/accounts/users/pdehaye"
}
```

Suggested fix: http://boxen.math.washington.edu/home/pdehaye/spkg/flint-1.5.2.p2.spkg

Beware, this is my first spkg. I removed the offending file, modified SPKG.txt, and the mercurial log. I then made the spkg using sage _5.0_ as this is the last version I have running on my system. It looks like sage-spkg has not been changed since, so that should not be a problem.



---

archive/issue_comments_094093.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-10-15T21:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9697#issuecomment-94093",
    "user": "https://trac.sagemath.org/admin/accounts/users/pdehaye"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094094.json:
```json
{
    "body": "The spkg was created correctly, as far as I can tell.  You even added the tag!\n\nThis just needs formal testing on a couple machines to make sure something weird didn't accidentally happen, but looks good.",
    "created_at": "2012-10-16T00:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9697#issuecomment-94094",
    "user": "https://github.com/kcrisman"
}
```

The spkg was created correctly, as far as I can tell.  You even added the tag!

This just needs formal testing on a couple machines to make sure something weird didn't accidentally happen, but looks good.



---

archive/issue_comments_094095.json:
```json
{
    "body": "Seems fine on sage.math, passes relevant tests.",
    "created_at": "2012-10-16T01:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9697#issuecomment-94095",
    "user": "https://github.com/kcrisman"
}
```

Seems fine on sage.math, passes relevant tests.



---

archive/issue_comments_094096.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-10-16T01:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9697#issuecomment-94096",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094097.json:
```json
{
    "body": "Same on Mac OS X.  I think this is ok...",
    "created_at": "2012-10-16T01:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9697#issuecomment-94097",
    "user": "https://github.com/kcrisman"
}
```

Same on Mac OS X.  I think this is ok...



---

archive/issue_comments_094098.json:
```json
{
    "body": "FWIW, the `.svn/` folders should get removed from the source tree anyway.  [Haven't looked at the new spkg.]",
    "created_at": "2012-10-16T10:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9697#issuecomment-94098",
    "user": "https://github.com/nexttime"
}
```

FWIW, the `.svn/` folders should get removed from the source tree anyway.  [Haven't looked at the new spkg.]



---

archive/issue_comments_094099.json:
```json
{
    "body": "`@`leif: There are actually two issues: some .DS_Store are in the spkg, all having to do with bernoulli. One of those files sits inside a .svn folder, and was originally reported in this ticket. The others are in regular src/ folders, and might have been introduced when preparing the spkg.",
    "created_at": "2012-10-16T12:01:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9697#issuecomment-94099",
    "user": "https://trac.sagemath.org/admin/accounts/users/pdehaye"
}
```

`@`leif: There are actually two issues: some .DS_Store are in the spkg, all having to do with bernoulli. One of those files sits inside a .svn folder, and was originally reported in this ticket. The others are in regular src/ folders, and might have been introduced when preparing the spkg.



---

archive/issue_events_024229.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-10-17T20:52:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9697#event-24229"
}
```



---

archive/issue_comments_094100.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-10-17T20:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9697#issuecomment-94100",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
