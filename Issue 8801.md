# Issue 8801: implement the projective dual of a plane curve

archive/issues_008801.json:
```json
{
    "body": "Assignee: @aghitza\n\nThis was requested by Ursula Whitcher on sage-support.  She adds:\n\n\n```\n  I'm playing with a family of plane curves with rational coefficients in \n  the complex projective plane.  So rational or complex numbers would be \n  enough for me to test examples.  In a perfect world I'd be able to \n  specify a family using rational functions of arbitrary constants \n  (something like a x^2 + b/(a-1) y^2), and compute the projective dual in \n  terms of those constants.\n```\n\n\nA good place to start in implementing this could be http://www.emilvolcheck.com/dual.ps\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8801\n\n",
    "created_at": "2010-04-28T14:24:54Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.1",
    "title": "implement the projective dual of a plane curve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8801",
    "user": "https://github.com/aghitza"
}
```
Assignee: @aghitza

This was requested by Ursula Whitcher on sage-support.  She adds:


```
  I'm playing with a family of plane curves with rational coefficients in 
  the complex projective plane.  So rational or complex numbers would be 
  enough for me to test examples.  In a perfect world I'd be able to 
  specify a family using rational functions of arbitrary constants 
  (something like a x^2 + b/(a-1) y^2), and compute the projective dual in 
  terms of those constants.
```


A good place to start in implementing this could be http://www.emilvolcheck.com/dual.ps


Issue created by migration from https://trac.sagemath.org/ticket/8801





---

archive/issue_comments_080601.json:
```json
{
    "body": "The attached patch implements this for (reduced and irreducible) hypersurfaces over the rationals. I intend to generalize this.\n\nI use Grobner bases and elimination. Resultants might be faster so I might switch to that approach.\n\nIf you plug in a variety I think the dual should be reduced. I'm not sure exactly what the scheme structure of the output is at the moment.\n\nSomething related to think about for the general case: given a subscheme X of projective space, what should the dual of X be?\n\nI will look at the approach described in the attached paper. When the dual is a hypersurface and has smaller degree than \"expected\", that approach seems to be better than the one used at the moment.",
    "created_at": "2012-05-26T01:45:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80601",
    "user": "https://trac.sagemath.org/admin/accounts/users/davideklund"
}
```

The attached patch implements this for (reduced and irreducible) hypersurfaces over the rationals. I intend to generalize this.

I use Grobner bases and elimination. Resultants might be faster so I might switch to that approach.

If you plug in a variety I think the dual should be reduced. I'm not sure exactly what the scheme structure of the output is at the moment.

Something related to think about for the general case: given a subscheme X of projective space, what should the dual of X be?

I will look at the approach described in the attached paper. When the dual is a hypersurface and has smaller degree than "expected", that approach seems to be better than the one used at the moment.



---

archive/issue_comments_080602.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-05-26T02:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80602",
    "user": "https://trac.sagemath.org/admin/accounts/users/davideklund"
}
```

Changing priority from major to minor.



---

archive/issue_comments_080603.json:
```json
{
    "body": "Attachment [trac_8801_projective_duals.patch](tarball://root/attachments/some-uuid/ticket8801/trac_8801_projective_duals.patch) by davideklund created at 2012-08-24 17:20:59\n\nThe patch implements duals of projective hypersurfaces. Patch rebased on top of Sage 5.2.",
    "created_at": "2012-08-24T17:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80603",
    "user": "https://trac.sagemath.org/admin/accounts/users/davideklund"
}
```

Attachment [trac_8801_projective_duals.patch](tarball://root/attachments/some-uuid/ticket8801/trac_8801_projective_duals.patch) by davideklund created at 2012-08-24 17:20:59

The patch implements duals of projective hypersurfaces. Patch rebased on top of Sage 5.2.



---

archive/issue_comments_080604.json:
```json
{
    "body": "Patch rebased on top of Sage 5.2.",
    "created_at": "2012-08-24T17:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80604",
    "user": "https://trac.sagemath.org/admin/accounts/users/davideklund"
}
```

Patch rebased on top of Sage 5.2.



---

archive/issue_comments_080605.json:
```json
{
    "body": "Here is a git branch. Maybe this could be considered as need review ?\n----\nNew commits:",
    "created_at": "2014-03-06T13:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80605",
    "user": "https://github.com/fchapoton"
}
```

Here is a git branch. Maybe this could be considered as need review ?
----
New commits:



---

archive/issue_comments_080606.json:
```json
{
    "body": "I guess it could be reviewed. It could be useful as it is. I had some plans to do something better but someone stole all my time... There is no particular reason to stick to hypersurfaces, it was just meant as an initial simplification.",
    "created_at": "2014-03-06T18:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80606",
    "user": "https://trac.sagemath.org/admin/accounts/users/davideklund"
}
```

I guess it could be reviewed. It could be useful as it is. I had some plans to do something better but someone stole all my time... There is no particular reason to stick to hypersurfaces, it was just meant as an initial simplification.



---

archive/issue_comments_080607.json:
```json
{
    "body": "Nor is there any particular reason to stick to varieties over Q.",
    "created_at": "2014-03-06T18:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80607",
    "user": "https://trac.sagemath.org/admin/accounts/users/davideklund"
}
```

Nor is there any particular reason to stick to varieties over Q.



---

archive/issue_comments_080608.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-01-27T20:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80608",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_080609.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-01-27T20:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80609",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080610.json:
```json
{
    "body": "turning that into `needs review` to require feedback:\n\nwhat is the class of rings over which this can currently work ?",
    "created_at": "2015-01-27T20:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80610",
    "user": "https://github.com/fchapoton"
}
```

turning that into `needs review` to require feedback:

what is the class of rings over which this can currently work ?



---

archive/issue_comments_080611.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-02-27T09:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80611",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_021461.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-04-29T12:47:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "milestone": "sage-6.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8801#event-21461"
}
```



---

archive/issue_comments_080612.json:
```json
{
    "body": "Changing keywords from \"\" to \"projective duality\".",
    "created_at": "2015-05-28T13:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80612",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "projective duality".



---

archive/issue_events_021462.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-05-28T13:36:33Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "milestone": "sage-6.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8801#event-21462"
}
```



---

archive/issue_events_021463.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-05-28T13:36:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "milestone": "sage-6.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8801#event-21463"
}
```



---

archive/issue_events_021464.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-08-09T09:04:41Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "milestone": "sage-6.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8801#event-21464"
}
```



---

archive/issue_events_021465.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-08-09T09:04:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "milestone": "sage-6.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8801#event-21465"
}
```



---

archive/issue_comments_080613.json:
```json
{
    "body": "nobody interested by this ticket ?",
    "created_at": "2015-10-18T19:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80613",
    "user": "https://github.com/fchapoton"
}
```

nobody interested by this ticket ?



---

archive/issue_events_021466.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-10-18T19:50:26Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "milestone": "sage-6.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8801#event-21466"
}
```



---

archive/issue_events_021467.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-10-18T19:50:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "milestone": "sage-6.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8801#event-21467"
}
```



---

archive/issue_events_021468.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2016-01-06T20:06:42Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "milestone": "sage-6.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8801#event-21468"
}
```



---

archive/issue_events_021469.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2016-01-06T20:06:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "milestone": "sage-7.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8801#event-21469"
}
```



---

archive/issue_comments_080614.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-18T13:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80614",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_021470.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2016-01-21T20:24:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "milestone": "sage-7.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8801#event-21470"
}
```



---

archive/issue_events_021471.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2016-01-21T20:24:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "milestone": "sage-7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8801#event-21471"
}
```



---

archive/issue_comments_080615.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-02-23T22:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80615",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080616.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-02-24T19:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80616",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_021472.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-02-24T19:35:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8801#event-21472"
}
```
