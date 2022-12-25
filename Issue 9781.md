# Issue 9781: Enhanced fans fail for complicated cases

archive/issues_009781.json:
```json
{
    "body": "Assignee: @novoselt\n\nCC:  @novoselt\n\nFans of toric varieties do not work correctly, for example see the following:\n\n```\nsage: f = Fan([(0, 2, 4), (0, 4, 5), (0, 3, 5), (0, 1, 3), (0, 1, 2), (2, 4, 6), (4, 5, 6), (3, 5, 6), (1, 3, 6), (1, 2, 6)], [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 2), (0, 1, 3), (1, 0, 4)])\nsage: f.is_complete()\nTrue\nsage: X = ToricVariety(f)\nsage: X.fan().is_complete()\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/home/vbraun/opt/sage-4.5.2/devel/sage-main/<ipython console> in <module>()\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan.pyc in is_complete(self)\n   1742         # Then boundary cones are (d-1)-dimensional.\n   1743         for cone in self(codim=1):\n-> 1744             if len(cone.star_generator_indices()) != 2:\n   1745                 self._is_complete = False\n   1746                 return False\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan.pyc in __call__(self, dim, codim)\n    816         else:\n    817             return self.cones(dim, codim)\n--> 818 \n    819     def __cmp__(self, right):\n    820         r\"\"\"\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan.pyc in cones(self, dim, codim)\n   1547                 if len(top_cones) == self.ngenerating_cones():\n   1548                     top_cones.sort(key=lambda cone:\n-> 1549                                             cone.star_generator_indices()[0])\n   1550                 levels[-1] = top_cones\n   1551             if len(levels) >= 2: # We have rays\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan.pyc in <lambda>(cone)\n   1548                     top_cones.sort(key=lambda cone:\n   1549                                             cone.star_generator_indices()[0])\n-> 1550                 levels[-1] = top_cones\n   1551             if len(levels) >= 2: # We have rays\n   1552                 rays = list(levels[1])\n\nIndexError: tuple index out of range\n```\n\nI'm pretty sure it is a bug in Andrey's switch to enhanced cones for toric varieties (`trac_9470_toric_variety_fans.patch`). If I back out that patch it works fine. Unfortunately we didn't catch that in our doctests, we should add tests for complicated toric varieties and mark them as `# long time`\n\nIssue created by migration from https://trac.sagemath.org/ticket/9782\n\n",
    "created_at": "2010-08-22T21:20:49Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Enhanced fans fail for complicated cases",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9781",
    "user": "https://github.com/vbraun"
}
```
Assignee: @novoselt

CC:  @novoselt

Fans of toric varieties do not work correctly, for example see the following:

```
sage: f = Fan([(0, 2, 4), (0, 4, 5), (0, 3, 5), (0, 1, 3), (0, 1, 2), (2, 4, 6), (4, 5, 6), (3, 5, 6), (1, 3, 6), (1, 2, 6)], [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 2), (0, 1, 3), (1, 0, 4)])
sage: f.is_complete()
True
sage: X = ToricVariety(f)
sage: X.fan().is_complete()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/vbraun/opt/sage-4.5.2/devel/sage-main/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan.pyc in is_complete(self)
   1742         # Then boundary cones are (d-1)-dimensional.
   1743         for cone in self(codim=1):
-> 1744             if len(cone.star_generator_indices()) != 2:
   1745                 self._is_complete = False
   1746                 return False

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan.pyc in __call__(self, dim, codim)
    816         else:
    817             return self.cones(dim, codim)
--> 818 
    819     def __cmp__(self, right):
    820         r"""

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan.pyc in cones(self, dim, codim)
   1547                 if len(top_cones) == self.ngenerating_cones():
   1548                     top_cones.sort(key=lambda cone:
-> 1549                                             cone.star_generator_indices()[0])
   1550                 levels[-1] = top_cones
   1551             if len(levels) >= 2: # We have rays

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan.pyc in <lambda>(cone)
   1548                     top_cones.sort(key=lambda cone:
   1549                                             cone.star_generator_indices()[0])
-> 1550                 levels[-1] = top_cones
   1551             if len(levels) >= 2: # We have rays
   1552                 rays = list(levels[1])

IndexError: tuple index out of range
```

I'm pretty sure it is a bug in Andrey's switch to enhanced cones for toric varieties (`trac_9470_toric_variety_fans.patch`). If I back out that patch it works fine. Unfortunately we didn't catch that in our doctests, we should add tests for complicated toric varieties and mark them as `# long time`

Issue created by migration from https://trac.sagemath.org/ticket/9782





---

archive/issue_comments_095858.json:
```json
{
    "body": "Working on it!",
    "created_at": "2010-08-22T22:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9781#issuecomment-95858",
    "user": "https://github.com/novoselt"
}
```

Working on it!



---

archive/issue_comments_095859.json:
```json
{
    "body": "Attachment [trac_9782_bug_in_computing_star_generators.patch](tarball://root/attachments/some-uuid/ticket9782/trac_9782_bug_in_computing_star_generators.patch) by @novoselt created at 2010-08-23 00:12:11",
    "created_at": "2010-08-23T00:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9781#issuecomment-95859",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9782_bug_in_computing_star_generators.patch](tarball://root/attachments/some-uuid/ticket9782/trac_9782_bug_in_computing_star_generators.patch) by @novoselt created at 2010-08-23 00:12:11



---

archive/issue_comments_095860.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-23T00:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9781#issuecomment-95860",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095861.json:
```json
{
    "body": "It was a silly typo in generic fans (I confused the number of rays with the number of cones). We definitely need more doctests, but so far adding new functionality serves as one of the sources ;-) I have added your example from this ticket to documentation of the function which had the error. It adds about 2 seconds to the test time so I put it in without #long so far - checking completeness uses quite a few functions, so it is a nice one to have.\n\nAnyway - the patch is \"one-worder\" plus doctest, ready for review!",
    "created_at": "2010-08-23T00:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9781#issuecomment-95861",
    "user": "https://github.com/novoselt"
}
```

It was a silly typo in generic fans (I confused the number of rays with the number of cones). We definitely need more doctests, but so far adding new functionality serves as one of the sources ;-) I have added your example from this ticket to documentation of the function which had the error. It adds about 2 seconds to the test time so I put it in without #long so far - checking completeness uses quite a few functions, so it is a nice one to have.

Anyway - the patch is "one-worder" plus doctest, ready for review!



---

archive/issue_comments_095862.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-23T11:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9781#issuecomment-95862",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095863.json:
```json
{
    "body": "Thanks, this fixes it and explains why it hasn't surfaced earlier: Tests usually use toric surfaces where the number of rays equals the number of number of generators. But that only holds for 2D complete fans.",
    "created_at": "2010-08-23T11:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9781#issuecomment-95863",
    "user": "https://github.com/vbraun"
}
```

Thanks, this fixes it and explains why it hasn't surfaced earlier: Tests usually use toric surfaces where the number of rays equals the number of number of generators. But that only holds for 2D complete fans.



---

archive/issue_comments_095864.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T09:56:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9781#issuecomment-95864",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
