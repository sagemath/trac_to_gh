# Issue 8181: cannot coerce residue field back to p-adic ring

archive/issues_008181.json:
```json
{
    "body": "Assignee: @roed314\n\nCC:  @roed314 @orlitzky\n\nI should be able to coerce elements of the residue field of a p-adic ring back into the ring, but I can't:\n\n\n```\nsage: R.<z> = Zq(9)\nsage: F = R.residue_class_field()\nsage: F\nFinite Field in z0 of size 3^2\nsage: a = F.gen()\nsage: R(a)\n---------------------------------------------------------------------------\nTypeError\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8181\n\n",
    "created_at": "2010-02-03T23:35:50Z",
    "labels": [
        "component: padics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.2",
    "title": "cannot coerce residue field back to p-adic ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8181",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @roed314

CC:  @roed314 @orlitzky

I should be able to coerce elements of the residue field of a p-adic ring back into the ring, but I can't:


```
sage: R.<z> = Zq(9)
sage: F = R.residue_class_field()
sage: F
Finite Field in z0 of size 3^2
sage: a = F.gen()
sage: R(a)
---------------------------------------------------------------------------
TypeError
```



Issue created by migration from https://trac.sagemath.org/ticket/8181





---

archive/issue_comments_071974.json:
```json
{
    "body": "see also the thread:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/ce14b31005ec053a",
    "created_at": "2010-02-03T23:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71974",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

see also the thread:

http://groups.google.com/group/sage-support/browse_thread/thread/ce14b31005ec053a



---

archive/issue_comments_071975.json:
```json
{
    "body": "This works now:\n\n\n```\nsage: R.<z> = Zq(9)\nsage: F = R.residue_class_field()\nsage: F\nFinite Field in z0 of size 3^2\nsage: a = F.gen()\nsage: R(a)\nz + O(3)\n```\n\n\nI can create a patch with a doctest, but I don't know if the result is correct. Does it look about right?",
    "created_at": "2012-01-13T19:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71975",
    "user": "https://github.com/orlitzky"
}
```

This works now:


```
sage: R.<z> = Zq(9)
sage: F = R.residue_class_field()
sage: F
Finite Field in z0 of size 3^2
sage: a = F.gen()
sage: R(a)
z + O(3)
```


I can create a patch with a doctest, but I don't know if the result is correct. Does it look about right?



---

archive/issue_comments_071976.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-03-20T20:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71976",
    "user": "https://github.com/saraedum"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071977.json:
```json
{
    "body": "It was fixed in the meantime. A added a standard test for it.",
    "created_at": "2016-03-20T20:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71977",
    "user": "https://github.com/saraedum"
}
```

It was fixed in the meantime. A added a standard test for it.



---

archive/issue_comments_071978.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-03-20T20:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71978",
    "user": "https://github.com/saraedum"
}
```

New commits:



---

archive/issue_comments_071979.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-03-21T15:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71979",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071980.json:
```json
{
    "body": "Looks good.",
    "created_at": "2016-03-21T15:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71980",
    "user": "https://github.com/adeines"
}
```

Looks good.



---

archive/issue_comments_071981.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd71\".",
    "created_at": "2016-03-23T15:25:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71981",
    "user": "https://github.com/adeines"
}
```

Changing keywords from "" to "sd71".



---

archive/issue_comments_071982.json:
```json
{
    "body": "Changing keywords from \"sd71\" to \"days71\".",
    "created_at": "2016-03-23T17:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71982",
    "user": "https://github.com/adeines"
}
```

Changing keywords from "sd71" to "days71".



---

archive/issue_comments_071983.json:
```json
{
    "body": "Doesn't apply according to the patchbot.",
    "created_at": "2016-04-04T16:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71983",
    "user": "https://github.com/jdemeyer"
}
```

Doesn't apply according to the patchbot.



---

archive/issue_comments_071984.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2016-04-04T16:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71984",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071985.json:
```json
{
    "body": "Fixed the merge problem.\n----\nNew commits:",
    "created_at": "2016-11-20T01:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71985",
    "user": "https://github.com/roed314"
}
```

Fixed the merge problem.
----
New commits:



---

archive/issue_comments_071986.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-11-20T01:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71986",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071987.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-11-30T01:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71987",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071988.json:
```json
{
    "body": "The increase in startup reported by the patchbot is just noise.",
    "created_at": "2016-11-30T01:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71988",
    "user": "https://github.com/saraedum"
}
```

The increase in startup reported by the patchbot is just noise.



---

archive/issue_comments_071989.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-12-01T22:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-71989",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
