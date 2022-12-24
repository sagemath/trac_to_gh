# Issue 602: sage: (1/2)^(2^100)
serious powering bug / overflow

archive/issues_000602.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\nsage: (1/2)^(2^100)\n1\n```\n\n\nOuch!\n\nIssue created by migration from https://trac.sagemath.org/ticket/602\n\n",
    "created_at": "2007-09-06T19:24:35Z",
    "labels": [
        "basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "sage: (1/2)^(2^100)\nserious powering bug / overflow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/602",
    "user": "was"
}
```
Assignee: boothby


```
sage: (1/2)^(2^100)
1
```


Ouch!

Issue created by migration from https://trac.sagemath.org/ticket/602





---

archive/issue_comments_003105.json:
```json
{
    "body": "The cutoff for the exponent looks to be 2^32.\n\n```\nsage: x = 2^(2^32-1)\nsage: x == 1\nFalse\nsage: x = 2^(2^32)\nsage: x == 1\nTrue\nsage: \n```\n",
    "created_at": "2007-09-06T21:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/602#issuecomment-3105",
    "user": "mhansen"
}
```

The cutoff for the exponent looks to be 2^32.

```
sage: x = 2^(2^32-1)
sage: x == 1
False
sage: x = 2^(2^32)
sage: x == 1
True
sage: 
```




---

archive/issue_comments_003106.json:
```json
{
    "body": "fixed by patch:\n\n[http://sage.math.washington.edu/home/boothby/my_patches/rationals602.hg](http://sage.math.washington.edu/home/boothby/my_patches/rationals602.hg)",
    "created_at": "2007-09-06T22:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/602#issuecomment-3106",
    "user": "boothby"
}
```

fixed by patch:

[http://sage.math.washington.edu/home/boothby/my_patches/rationals602.hg](http://sage.math.washington.edu/home/boothby/my_patches/rationals602.hg)



---

archive/issue_comments_003107.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T01:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/602#issuecomment-3107",
    "user": "was"
}
```

Resolution: fixed
