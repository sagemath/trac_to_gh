# Issue 8181: cannot coerce residue field back to p-adic ring

archive/issues_008181.json:
```json
{
    "body": "Assignee: @roed314\n\nCC:  @roed314 @orlitzky\n\nI should be able to coerce elements of the residue field of a p-adic ring back into the ring, but I can't:\n\n\n```\nsage: R.<z> = Zq(9)\nsage: F = R.residue_class_field()\nsage: F\nFinite Field in z0 of size 3^2\nsage: a = F.gen()\nsage: R(a)\n---------------------------------------------------------------------------\nTypeError\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8181\n\n",
    "created_at": "2010-02-03T23:35:50Z",
    "labels": [
        "padics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.2",
    "title": "cannot coerce residue field back to p-adic ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8181",
    "user": "dmharvey"
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

archive/issue_comments_072096.json:
```json
{
    "body": "see also the thread:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/ce14b31005ec053a",
    "created_at": "2010-02-03T23:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72096",
    "user": "dmharvey"
}
```

see also the thread:

http://groups.google.com/group/sage-support/browse_thread/thread/ce14b31005ec053a



---

archive/issue_comments_072097.json:
```json
{
    "body": "This works now:\n\n\n```\nsage: R.<z> = Zq(9)\nsage: F = R.residue_class_field()\nsage: F\nFinite Field in z0 of size 3^2\nsage: a = F.gen()\nsage: R(a)\nz + O(3)\n```\n\n\nI can create a patch with a doctest, but I don't know if the result is correct. Does it look about right?",
    "created_at": "2012-01-13T19:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72097",
    "user": "@orlitzky"
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

archive/issue_comments_072098.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-03-20T20:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72098",
    "user": "@saraedum"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072099.json:
```json
{
    "body": "It was fixed in the meantime. A added a standard test for it.",
    "created_at": "2016-03-20T20:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72099",
    "user": "@saraedum"
}
```

It was fixed in the meantime. A added a standard test for it.



---

archive/issue_comments_072100.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-03-20T20:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72100",
    "user": "@saraedum"
}
```

New commits:



---

archive/issue_comments_072101.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-03-21T15:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72101",
    "user": "@adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072102.json:
```json
{
    "body": "Looks good.",
    "created_at": "2016-03-21T15:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72102",
    "user": "@adeines"
}
```

Looks good.



---

archive/issue_comments_072103.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd71\".",
    "created_at": "2016-03-23T15:25:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72103",
    "user": "@adeines"
}
```

Changing keywords from "" to "sd71".



---

archive/issue_comments_072104.json:
```json
{
    "body": "Changing keywords from \"sd71\" to \"days71\".",
    "created_at": "2016-03-23T17:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72104",
    "user": "@adeines"
}
```

Changing keywords from "sd71" to "days71".



---

archive/issue_comments_072105.json:
```json
{
    "body": "Doesn't apply according to the patchbot.",
    "created_at": "2016-04-04T16:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72105",
    "user": "@jdemeyer"
}
```

Doesn't apply according to the patchbot.



---

archive/issue_comments_072106.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2016-04-04T16:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72106",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_072107.json:
```json
{
    "body": "Fixed the merge problem.\n----\nNew commits:",
    "created_at": "2016-11-20T01:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72107",
    "user": "@roed314"
}
```

Fixed the merge problem.
----
New commits:



---

archive/issue_comments_072108.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-11-20T01:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72108",
    "user": "@roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072109.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-11-30T01:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72109",
    "user": "@saraedum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072110.json:
```json
{
    "body": "The increase in startup reported by the patchbot is just noise.",
    "created_at": "2016-11-30T01:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72110",
    "user": "@saraedum"
}
```

The increase in startup reported by the patchbot is just noise.



---

archive/issue_comments_072111.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-12-01T22:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8181#issuecomment-72111",
    "user": "@vbraun"
}
```

Resolution: fixed
