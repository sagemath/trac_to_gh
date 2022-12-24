# Issue 8311: elliptic curve random point hangs when group is trivial

archive/issues_008311.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  schilly\n\nKeywords: random point\n\nAs reported:\n\n```\nE = EllipticCurve(GF(3), [0,0,0,2,2])\nE.random_element()\n```\n\nHangs since\n\n```\nsage: E.rational_points()\n[(0 : 1 : 0)]\n```\n\nso unless the point at infinity is picked (probability 1/(q+1)=1/4) no point will be found.\n\nThis can only happen for q=2,3,4 (try Hasse_bounds(q)) so these cases need separate treatment.\n\nPatch coming up.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8311\n\n",
    "created_at": "2010-02-20T12:06:17Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "elliptic curve random point hangs when group is trivial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8311",
    "user": "cremona"
}
```
Assignee: cremona

CC:  schilly

Keywords: random point

As reported:

```
E = EllipticCurve(GF(3), [0,0,0,2,2])
E.random_element()
```

Hangs since

```
sage: E.rational_points()
[(0 : 1 : 0)]
```

so unless the point at infinity is picked (probability 1/(q+1)=1/4) no point will be found.

This can only happen for q=2,3,4 (try Hasse_bounds(q)) so these cases need separate treatment.

Patch coming up.


Issue created by migration from https://trac.sagemath.org/ticket/8311





---

archive/issue_comments_073712.json:
```json
{
    "body": "Attachment [trac_8311-random-point.patch](tarball://root/attachments/some-uuid/ticket8311/trac_8311-random-point.patch) by cremona created at 2010-02-20 13:48:52\n\napplies to 4.3.3.alpha1",
    "created_at": "2010-02-20T13:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8311#issuecomment-73712",
    "user": "cremona"
}
```

Attachment [trac_8311-random-point.patch](tarball://root/attachments/some-uuid/ticket8311/trac_8311-random-point.patch) by cremona created at 2010-02-20 13:48:52

applies to 4.3.3.alpha1



---

archive/issue_comments_073713.json:
```json
{
    "body": "Patch attached.  I needed to make a few side adjustments to avoid infinite recursions, since enumerating points is sometimes done via first finding the group generators, which in turn uses random points....",
    "created_at": "2010-02-20T13:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8311#issuecomment-73713",
    "user": "cremona"
}
```

Patch attached.  I needed to make a few side adjustments to avoid infinite recursions, since enumerating points is sometimes done via first finding the group generators, which in turn uses random points....



---

archive/issue_comments_073714.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-20T13:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8311#issuecomment-73714",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073715.json:
```json
{
    "body": "thx, tried the patch, works. i'll seek for some feedback from the original reporter.",
    "created_at": "2010-02-20T13:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8311#issuecomment-73715",
    "user": "schilly"
}
```

thx, tried the patch, works. i'll seek for some feedback from the original reporter.



---

archive/issue_comments_073716.json:
```json
{
    "body": "Replaces the previous patch",
    "created_at": "2010-03-05T18:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8311#issuecomment-73716",
    "user": "wuthrich"
}
```

Replaces the previous patch



---

archive/issue_comments_073717.json:
```json
{
    "body": "Attachment [trac_8311_random_point_2.patch](tarball://root/attachments/some-uuid/ticket8311/trac_8311_random_point_2.patch) by wuthrich created at 2010-03-05 18:26:42\n\nI changed a few tabulators to spaces. Other than that the patch is fine. And I started testing now.",
    "created_at": "2010-03-05T18:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8311#issuecomment-73717",
    "user": "wuthrich"
}
```

Attachment [trac_8311_random_point_2.patch](tarball://root/attachments/some-uuid/ticket8311/trac_8311_random_point_2.patch) by wuthrich created at 2010-03-05 18:26:42

I changed a few tabulators to spaces. Other than that the patch is fine. And I started testing now.



---

archive/issue_comments_073718.json:
```json
{
    "body": "Replying to [comment:4 wuthrich]:\n> I changed a few tabulators to spaces. Other than that the patch is fine. And I started testing now.\nThanks, sorry about the tabs.",
    "created_at": "2010-03-08T21:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8311#issuecomment-73718",
    "user": "cremona"
}
```

Replying to [comment:4 wuthrich]:
> I changed a few tabulators to spaces. Other than that the patch is fine. And I started testing now.
Thanks, sorry about the tabs.



---

archive/issue_comments_073719.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-09T19:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8311#issuecomment-73719",
    "user": "wuthrich"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073720.json:
```json
{
    "body": "Sorry about the delay. I still do not know why I can use the trac only from home and not from my office. \n\nThe tests passed (except the once that are reported and present in the current .alpha)",
    "created_at": "2010-03-09T19:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8311#issuecomment-73720",
    "user": "wuthrich"
}
```

Sorry about the delay. I still do not know why I can use the trac only from home and not from my office. 

The tests passed (except the once that are reported and present in the current .alpha)



---

archive/issue_comments_073721.json:
```json
{
    "body": "Merged [trac_8311_random_point_2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8311/trac_8311_random_point_2.patch).",
    "created_at": "2010-03-11T04:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8311#issuecomment-73721",
    "user": "mvngu"
}
```

Merged [trac_8311_random_point_2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8311/trac_8311_random_point_2.patch).



---

archive/issue_comments_073722.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-11T04:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8311#issuecomment-73722",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_073723.json:
```json
{
    "body": "Much better fix at #16951.",
    "created_at": "2014-09-09T15:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8311#issuecomment-73723",
    "user": "jdemeyer"
}
```

Much better fix at #16951.
