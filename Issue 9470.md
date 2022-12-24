# Issue 9470: Switch toric varieties to enhanced fans

archive/issues_009470.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @vbraun\n\nAs indicated in #9326, it is desirable for fans and cones associated to toric varieties to know these toric varieties. The framework for such an association was already designed (with a view towards morphisms), this patch puts it to work.\n\nI have written it on top of #9245, which is the last patch in the chain with positive review.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9470\n\n",
    "created_at": "2010-07-10T05:52:15Z",
    "labels": [
        "algebraic geometry",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Switch toric varieties to enhanced fans",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9470",
    "user": "@novoselt"
}
```
Assignee: @aghitza

CC:  @vbraun

As indicated in #9326, it is desirable for fans and cones associated to toric varieties to know these toric varieties. The framework for such an association was already designed (with a view towards morphisms), this patch puts it to work.

I have written it on top of #9245, which is the last patch in the chain with positive review.

Issue created by migration from https://trac.sagemath.org/ticket/9470





---

archive/issue_comments_090843.json:
```json
{
    "body": "Hi Volker,\n\nThis patch should let you to easily add cohomology methods to cones and have everything together in the `toric_variety` module.\n\nI have modified the code of `EnhancedCone` a little with the idea that if you have a chain of enhanced fans\n\nFan ---> EFan1 ---> EFan2\n\nand, say, intersect two cones belonging to `EFan2`, then three cones will be created replicating the same chain\n\nCone ---> ECone1 ---> ECone2\n\nI am not completely sure if this is necessary, but it will be consistent in the sense that \"base cone\" of ECone2 will belong to \"base fan\" of its fan.\n\nThank you,\nAndrey",
    "created_at": "2010-07-10T06:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9470#issuecomment-90843",
    "user": "@novoselt"
}
```

Hi Volker,

This patch should let you to easily add cohomology methods to cones and have everything together in the `toric_variety` module.

I have modified the code of `EnhancedCone` a little with the idea that if you have a chain of enhanced fans

Fan ---> EFan1 ---> EFan2

and, say, intersect two cones belonging to `EFan2`, then three cones will be created replicating the same chain

Cone ---> ECone1 ---> ECone2

I am not completely sure if this is necessary, but it will be consistent in the sense that "base cone" of ECone2 will belong to "base fan" of its fan.

Thank you,
Andrey



---

archive/issue_comments_090844.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-10T06:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9470#issuecomment-90844",
    "user": "@novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090845.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-23T20:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9470#issuecomment-90845",
    "user": "@vbraun"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090846.json:
```json
{
    "body": "The `cone_containing` method of a `Fan_of_toric_variety` should also return a `Cone_of_toric_variety`, but right now:\n\n```\nsage: P2=toric_varieties.P2()\nsage: fan=P2.fan()\nsage: [ type(c) for c in fan ]\n[<class 'sage.schemes.generic.toric_variety.Cone_of_toric_variety'>, <class 'sage.schemes.generic.toric_variety.Cone_of_toric_variety'>, <class 'sage.schemes.generic.toric_variety.Cone_of_toric_variety'>]\nsage: N=fan.lattice()\nsage: c = fan.cone_containing( N(0,1) ); c\n1-d cone in 2-d lattice N\nsage: type(c)\n<class 'sage.geometry.cone.ConvexRationalPolyhedralCone'>\nsage: c.ambient()\n1-d cone in 2-d lattice N\n```\n",
    "created_at": "2010-07-23T20:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9470#issuecomment-90846",
    "user": "@vbraun"
}
```

The `cone_containing` method of a `Fan_of_toric_variety` should also return a `Cone_of_toric_variety`, but right now:

```
sage: P2=toric_varieties.P2()
sage: fan=P2.fan()
sage: [ type(c) for c in fan ]
[<class 'sage.schemes.generic.toric_variety.Cone_of_toric_variety'>, <class 'sage.schemes.generic.toric_variety.Cone_of_toric_variety'>, <class 'sage.schemes.generic.toric_variety.Cone_of_toric_variety'>]
sage: N=fan.lattice()
sage: c = fan.cone_containing( N(0,1) ); c
1-d cone in 2-d lattice N
sage: type(c)
<class 'sage.geometry.cone.ConvexRationalPolyhedralCone'>
sage: c.ambient()
1-d cone in 2-d lattice N
```




---

archive/issue_comments_090847.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-24T07:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9470#issuecomment-90847",
    "user": "@novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090848.json:
```json
{
    "body": "Attachment [trac_9470_toric_variety_fans.patch](tarball://root/attachments/some-uuid/ticket9470/trac_9470_toric_variety_fans.patch) by @novoselt created at 2010-07-24 07:28:44\n\nChanged line 2232 in `fan` (I missed explicit setting of the ambient fan). I have added a doctest for the above case into `Fan_of_toric_variety.__init__`.",
    "created_at": "2010-07-24T07:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9470#issuecomment-90848",
    "user": "@novoselt"
}
```

Attachment [trac_9470_toric_variety_fans.patch](tarball://root/attachments/some-uuid/ticket9470/trac_9470_toric_variety_fans.patch) by @novoselt created at 2010-07-24 07:28:44

Changed line 2232 in `fan` (I missed explicit setting of the ambient fan). I have added a doctest for the above case into `Fan_of_toric_variety.__init__`.



---

archive/issue_comments_090849.json:
```json
{
    "body": "Looks good now!",
    "created_at": "2010-07-27T16:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9470#issuecomment-90849",
    "user": "@vbraun"
}
```

Looks good now!



---

archive/issue_comments_090850.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-27T16:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9470#issuecomment-90850",
    "user": "@vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090851.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9470#issuecomment-90851",
    "user": "@qed777"
}
```

Resolution: fixed
