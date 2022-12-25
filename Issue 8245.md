# Issue 8245: tutorial: typo in section "Euler’s Method for Systems of Differential Equations"

archive/issues_008245.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @kcrisman\n\nFrom [sage-support](http://groups.google.com/group/sage-support/browse_frm/thread/437ae27f84e3a05):\n\n```\nIn the section, \"A Guided Tour\"->\"Basic Algebra and Calculus\"-\n>\"Euler\u2019s Method for Systems of Differential Equations\", I found that\n\nthe answer of the example is z(1)\u22480.75, which seems to be wrong.\n\nThe calculation is\n------------------------------------------------------------------------\nsage: t,x,y = PolynomialRing(RealField(10),3,\"txy\").gens()\nsage: f = y; g = -x - y * t\nsage: eulers_method_2x2(f,g, 0, 1, 0, 1/4, 1)\n      t                x            h*f(t,x,y)                y\nh*g(t,x,y)\n      0                1                  0.00\n0           -0.25\n    1/4              1.0                -0.062\n-0.25           -0.23\n    1/2             0.94                 -0.12\n-0.48           -0.17\n    3/4             0.82                 -0.16\n-0.66          -0.081\n      1             0.65                 -0.18\n-0.74           0.02\n------------------------------------------------------------------------\n\nSo I think the right answer should be z(1)\u22480.65 \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8245\n\n",
    "created_at": "2010-02-12T03:51:50Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "tutorial: typo in section \"Euler\u2019s Method for Systems of Differential Equations\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @kcrisman

From [sage-support](http://groups.google.com/group/sage-support/browse_frm/thread/437ae27f84e3a05):

```
In the section, "A Guided Tour"->"Basic Algebra and Calculus"-
>"Euler’s Method for Systems of Differential Equations", I found that

the answer of the example is z(1)≈0.75, which seems to be wrong.

The calculation is
------------------------------------------------------------------------
sage: t,x,y = PolynomialRing(RealField(10),3,"txy").gens()
sage: f = y; g = -x - y * t
sage: eulers_method_2x2(f,g, 0, 1, 0, 1/4, 1)
      t                x            h*f(t,x,y)                y
h*g(t,x,y)
      0                1                  0.00
0           -0.25
    1/4              1.0                -0.062
-0.25           -0.23
    1/2             0.94                 -0.12
-0.48           -0.17
    3/4             0.82                 -0.16
-0.66          -0.081
      1             0.65                 -0.18
-0.74           0.02
------------------------------------------------------------------------

So I think the right answer should be z(1)≈0.65 
```


Issue created by migration from https://trac.sagemath.org/ticket/8245





---

archive/issue_comments_072799.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-05-26T15:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8245#issuecomment-72799",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_072800.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-11T21:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8245#issuecomment-72800",
    "user": "https://trac.sagemath.org/admin/accounts/users/ksmith"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072801.json:
```json
{
    "body": "Attachment [trac_8245_Euler_Guided_Tour.patch](tarball://root/attachments/some-uuid/ticket8245/trac_8245_Euler_Guided_Tour.patch) by ksmith created at 2012-01-11 21:27:38\n\nI just made that one change making the 7 a 6.",
    "created_at": "2012-01-11T21:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8245#issuecomment-72801",
    "user": "https://trac.sagemath.org/admin/accounts/users/ksmith"
}
```

Attachment [trac_8245_Euler_Guided_Tour.patch](tarball://root/attachments/some-uuid/ticket8245/trac_8245_Euler_Guided_Tour.patch) by ksmith created at 2012-01-11 21:27:38

I just made that one change making the 7 a 6.



---

archive/issue_comments_072802.json:
```json
{
    "body": "Changing keywords from \"beginner\" to \"beginner sd35.5\".",
    "created_at": "2012-01-11T22:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8245#issuecomment-72802",
    "user": "https://trac.sagemath.org/admin/accounts/users/ksmith"
}
```

Changing keywords from "beginner" to "beginner sd35.5".



---

archive/issue_comments_072803.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-11T22:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8245#issuecomment-72803",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072804.json:
```json
{
    "body": "And the math turns out to be right.  The example itself is somewhat elliptically expressed, but this is fine.  \n\nCurious as to why we have both `:math:` and the backticks... but anyway, that would be a general overhaul of the tutorial.",
    "created_at": "2012-01-11T22:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8245#issuecomment-72804",
    "user": "https://github.com/kcrisman"
}
```

And the math turns out to be right.  The example itself is somewhat elliptically expressed, but this is fine.  

Curious as to why we have both `:math:` and the backticks... but anyway, that would be a general overhaul of the tutorial.



---

archive/issue_comments_072805.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> Curious as to why we have both `:math:` and the backticks... but anyway, that would be a general overhaul of the tutorial.\n\nWithin Sage, ``foo`` is equivalent to `:math:`foo``.  In general ReST code, this is not true.",
    "created_at": "2012-01-12T08:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8245#issuecomment-72805",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:6 kcrisman]:
> Curious as to why we have both `:math:` and the backticks... but anyway, that would be a general overhaul of the tutorial.

Within Sage, ``foo`` is equivalent to `:math:`foo``.  In general ReST code, this is not true.



---

archive/issue_comments_072806.json:
```json
{
    "body": "> > Curious as to why we have both `:math:` and the backticks... but anyway, that would be a general overhaul of the tutorial.\n> \n> Within Sage, ``foo`` is equivalent to `:math:`foo``.  In general ReST code, this is not true.\nAh, so it's historical in that sense.  Thanks for the clarification.",
    "created_at": "2012-01-12T14:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8245#issuecomment-72806",
    "user": "https://github.com/kcrisman"
}
```

> > Curious as to why we have both `:math:` and the backticks... but anyway, that would be a general overhaul of the tutorial.
> 
> Within Sage, ``foo`` is equivalent to `:math:`foo``.  In general ReST code, this is not true.
Ah, so it's historical in that sense.  Thanks for the clarification.



---

archive/issue_events_008446.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-01-13T23:07:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8245",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8245#event-8446"
}
```



---

archive/issue_comments_072807.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-01-13T23:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8245#issuecomment-72807",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
