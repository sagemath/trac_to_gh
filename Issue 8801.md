# Issue 8801: implement the projective dual of a plane curve

archive/issues_008801.json:
```json
{
    "body": "Assignee: @aghitza\n\nThis was requested by Ursula Whitcher on sage-support.  She adds:\n\n\n```\n  I'm playing with a family of plane curves with rational coefficients in \n  the complex projective plane.  So rational or complex numbers would be \n  enough for me to test examples.  In a perfect world I'd be able to \n  specify a family using rational functions of arbitrary constants \n  (something like a x^2 + b/(a-1) y^2), and compute the projective dual in \n  terms of those constants.\n```\n\n\nA good place to start in implementing this could be http://www.emilvolcheck.com/dual.ps\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8801\n\n",
    "created_at": "2010-04-28T14:24:54Z",
    "labels": [
        "algebraic geometry",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.1",
    "title": "implement the projective dual of a plane curve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8801",
    "user": "@aghitza"
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

archive/issue_comments_080733.json:
```json
{
    "body": "The attached patch implements this for (reduced and irreducible) hypersurfaces over the rationals. I intend to generalize this.\n\nI use Grobner bases and elimination. Resultants might be faster so I might switch to that approach.\n\nIf you plug in a variety I think the dual should be reduced. I'm not sure exactly what the scheme structure of the output is at the moment.\n\nSomething related to think about for the general case: given a subscheme X of projective space, what should the dual of X be?\n\nI will look at the approach described in the attached paper. When the dual is a hypersurface and has smaller degree than \"expected\", that approach seems to be better than the one used at the moment.",
    "created_at": "2012-05-26T01:45:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80733",
    "user": "davideklund"
}
```

The attached patch implements this for (reduced and irreducible) hypersurfaces over the rationals. I intend to generalize this.

I use Grobner bases and elimination. Resultants might be faster so I might switch to that approach.

If you plug in a variety I think the dual should be reduced. I'm not sure exactly what the scheme structure of the output is at the moment.

Something related to think about for the general case: given a subscheme X of projective space, what should the dual of X be?

I will look at the approach described in the attached paper. When the dual is a hypersurface and has smaller degree than "expected", that approach seems to be better than the one used at the moment.



---

archive/issue_comments_080734.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-05-26T02:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80734",
    "user": "davideklund"
}
```

Changing priority from major to minor.



---

archive/issue_comments_080735.json:
```json
{
    "body": "Attachment [trac_8801_projective_duals.patch](tarball://root/attachments/some-uuid/ticket8801/trac_8801_projective_duals.patch) by davideklund created at 2012-08-24 17:20:59\n\nThe patch implements duals of projective hypersurfaces. Patch rebased on top of Sage 5.2.",
    "created_at": "2012-08-24T17:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80735",
    "user": "davideklund"
}
```

Attachment [trac_8801_projective_duals.patch](tarball://root/attachments/some-uuid/ticket8801/trac_8801_projective_duals.patch) by davideklund created at 2012-08-24 17:20:59

The patch implements duals of projective hypersurfaces. Patch rebased on top of Sage 5.2.



---

archive/issue_comments_080736.json:
```json
{
    "body": "Patch rebased on top of Sage 5.2.",
    "created_at": "2012-08-24T17:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80736",
    "user": "davideklund"
}
```

Patch rebased on top of Sage 5.2.



---

archive/issue_comments_080737.json:
```json
{
    "body": "Here is a git branch. Maybe this could be considered as need review ?\n----\nNew commits:",
    "created_at": "2014-03-06T13:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80737",
    "user": "@fchapoton"
}
```

Here is a git branch. Maybe this could be considered as need review ?
----
New commits:



---

archive/issue_comments_080738.json:
```json
{
    "body": "I guess it could be reviewed. It could be useful as it is. I had some plans to do something better but someone stole all my time... There is no particular reason to stick to hypersurfaces, it was just meant as an initial simplification.",
    "created_at": "2014-03-06T18:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80738",
    "user": "davideklund"
}
```

I guess it could be reviewed. It could be useful as it is. I had some plans to do something better but someone stole all my time... There is no particular reason to stick to hypersurfaces, it was just meant as an initial simplification.



---

archive/issue_comments_080739.json:
```json
{
    "body": "Nor is there any particular reason to stick to varieties over Q.",
    "created_at": "2014-03-06T18:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80739",
    "user": "davideklund"
}
```

Nor is there any particular reason to stick to varieties over Q.



---

archive/issue_comments_080740.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-01-27T20:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80740",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_080741.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-01-27T20:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80741",
    "user": "@fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080742.json:
```json
{
    "body": "turning that into `needs review` to require feedback:\n\nwhat is the class of rings over which this can currently work ?",
    "created_at": "2015-01-27T20:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80742",
    "user": "@fchapoton"
}
```

turning that into `needs review` to require feedback:

what is the class of rings over which this can currently work ?



---

archive/issue_comments_080743.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-02-27T09:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80743",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_080744.json:
```json
{
    "body": "Changing keywords from \"\" to \"projective duality\".",
    "created_at": "2015-05-28T13:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80744",
    "user": "@fchapoton"
}
```

Changing keywords from "" to "projective duality".



---

archive/issue_comments_080745.json:
```json
{
    "body": "nobody interested by this ticket ?",
    "created_at": "2015-10-18T19:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80745",
    "user": "@fchapoton"
}
```

nobody interested by this ticket ?



---

archive/issue_comments_080746.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-18T13:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80746",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_080747.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-02-23T22:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80747",
    "user": "@vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080748.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-02-24T19:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8801#issuecomment-80748",
    "user": "@vbraun"
}
```

Resolution: fixed
