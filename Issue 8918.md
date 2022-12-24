# Issue 8918: Strange behavior for Permutation()

archive/issues_008918.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  jbandlow\n\nSee these examples:\n\n\n```\nsage: Permutation([1,2,3])\n[1, 2, 3]\nsage: Permutation([1,2,3,1])\n[1, 2, 3, 1]\nsage: [1,2,3] in Permutations()\nTrue\nsage: [1,2,3,1] in Permutations()\nFalse\nsage: Permutation([1,2,3,1]) in Permutations()\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8918\n\n",
    "created_at": "2010-05-07T16:48:02Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Strange behavior for Permutation()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8918",
    "user": "lvendramin"
}
```
Assignee: sage-combinat

CC:  jbandlow

See these examples:


```
sage: Permutation([1,2,3])
[1, 2, 3]
sage: Permutation([1,2,3,1])
[1, 2, 3, 1]
sage: [1,2,3] in Permutations()
True
sage: [1,2,3,1] in Permutations()
False
sage: Permutation([1,2,3,1]) in Permutations()
True
```


Issue created by migration from https://trac.sagemath.org/ticket/8918





---

archive/issue_comments_082136.json:
```json
{
    "body": "Yes, this is an error\n\n[1,2,3,1] dos not define a permutation, so the method should raise an error. See also #9831",
    "created_at": "2010-09-08T13:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8918#issuecomment-82136",
    "user": "lftabera"
}
```

Yes, this is an error

[1,2,3,1] dos not define a permutation, so the method should raise an error. See also #9831



---

archive/issue_comments_082137.json:
```json
{
    "body": "I think, this in fact can be closed as a duplicate of the ticket you mention (#9831).\n\nReplying to [comment:1 lftabera]:\n> Yes, this is an error\n> \n> [1,2,3,1] dos not define a permutation, so the method should raise an error. See also #9831",
    "created_at": "2013-01-27T00:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8918#issuecomment-82137",
    "user": "knsam"
}
```

I think, this in fact can be closed as a duplicate of the ticket you mention (#9831).

Replying to [comment:1 lftabera]:
> Yes, this is an error
> 
> [1,2,3,1] dos not define a permutation, so the method should raise an error. See also #9831



---

archive/issue_comments_082138.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-29T19:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8918#issuecomment-82138",
    "user": "tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082139.json:
```json
{
    "body": "One of a few tickets like this. Bonus points if you can find them all.\n\nAlso, don't forget to set this to needs_review. Thanks.",
    "created_at": "2013-01-29T19:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8918#issuecomment-82139",
    "user": "tscrim"
}
```

One of a few tickets like this. Bonus points if you can find them all.

Also, don't forget to set this to needs_review. Thanks.



---

archive/issue_comments_082140.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-29T19:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8918#issuecomment-82140",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082141.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-01-31T20:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8918#issuecomment-82141",
    "user": "jdemeyer"
}
```

Resolution: duplicate
