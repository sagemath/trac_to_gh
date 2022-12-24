# Issue 9121: sage-4.4.3.alpha1: set.py doctest failure

archive/issues_009121.json:
```json
{
    "body": "Assignee: tbd\n\nThis test now fails, since it really just compares types and as sage grows types get loaded into different places in memory:\n\n```\n            sage: Primes() < Set(QQ)\n            True\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9121\n\n",
    "created_at": "2010-06-03T03:23:06Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "sage-4.4.3.alpha1: set.py doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9121",
    "user": "was"
}
```
Assignee: tbd

This test now fails, since it really just compares types and as sage grows types get loaded into different places in memory:

```
            sage: Primes() < Set(QQ)
            True
```


Issue created by migration from https://trac.sagemath.org/ticket/9121





---

archive/issue_comments_084830.json:
```json
{
    "body": "I noticed a bug while looking at the relevant code in __cmp__:\n\n```\n        if not isinstance(right, Set_object):\n            return cmp(type(right), type(Set_object))\n        return cmp(self.__object, right.__object)\n```\n\nNotice that the first compare is totally backwards!   Interestingly, fixing this does fix the above bug.  Patch attached.",
    "created_at": "2010-06-03T03:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9121#issuecomment-84830",
    "user": "was"
}
```

I noticed a bug while looking at the relevant code in __cmp__:

```
        if not isinstance(right, Set_object):
            return cmp(type(right), type(Set_object))
        return cmp(self.__object, right.__object)
```

Notice that the first compare is totally backwards!   Interestingly, fixing this does fix the above bug.  Patch attached.



---

archive/issue_comments_084831.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-03T03:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9121#issuecomment-84831",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084832.json:
```json
{
    "body": "Attachment [trac_9121.patch](tarball://root/attachments/some-uuid/ticket9121/trac_9121.patch) by was created at 2010-06-03 03:29:06",
    "created_at": "2010-06-03T03:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9121#issuecomment-84832",
    "user": "was"
}
```

Attachment [trac_9121.patch](tarball://root/attachments/some-uuid/ticket9121/trac_9121.patch) by was created at 2010-06-03 03:29:06



---

archive/issue_comments_084833.json:
```json
{
    "body": "I actually reported [http://trac.sagemath.org/sage_trac/ticket/9004](http://trac.sagemath.org/sage_trac/ticket/9004)\non that expression - the test has failed for a long time on sage-on-gentoo.\nI didn't notice the backwardness and did something slightly different,\nbut the backwardness explain a lot of things.\nI think you should have a look at it and mark one of them a duplicate.",
    "created_at": "2010-06-03T09:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9121#issuecomment-84833",
    "user": "fbissey"
}
```

I actually reported [http://trac.sagemath.org/sage_trac/ticket/9004](http://trac.sagemath.org/sage_trac/ticket/9004)
on that expression - the test has failed for a long time on sage-on-gentoo.
I didn't notice the backwardness and did something slightly different,
but the backwardness explain a lot of things.
I think you should have a look at it and mark one of them a duplicate.



---

archive/issue_comments_084834.json:
```json
{
    "body": "Attachment [trac_9121-part2.patch](tarball://root/attachments/some-uuid/ticket9121/trac_9121-part2.patch) by was created at 2010-06-03 16:00:16",
    "created_at": "2010-06-03T16:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9121#issuecomment-84834",
    "user": "was"
}
```

Attachment [trac_9121-part2.patch](tarball://root/attachments/some-uuid/ticket9121/trac_9121-part2.patch) by was created at 2010-06-03 16:00:16



---

archive/issue_comments_084835.json:
```json
{
    "body": "fbissey -- you're right.  Both of our patches are wrong, but together they are right.  \n\nNote that I'm marking this test random, since it is a comparison of types, which is architecture and sage-version dependent.",
    "created_at": "2010-06-03T16:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9121#issuecomment-84835",
    "user": "was"
}
```

fbissey -- you're right.  Both of our patches are wrong, but together they are right.  

Note that I'm marking this test random, since it is a comparison of types, which is architecture and sage-version dependent.



---

archive/issue_comments_084836.json:
```json
{
    "body": "Replying to [comment:4 was]:\n> fbissey -- you're right.  Both of our patches are wrong, but together they are right.  \n> \n> Note that I'm marking this test random, since it is a comparison of types, which is architecture and sage-version dependent. \n\nNote : trac_9121.patch was already merged in sage-4.4.3.alpha1 only trac_9121-part2.patch needs to be merged... The patch looks good to me I'm waiting for the tests to finish.",
    "created_at": "2010-06-03T16:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9121#issuecomment-84836",
    "user": "hivert"
}
```

Replying to [comment:4 was]:
> fbissey -- you're right.  Both of our patches are wrong, but together they are right.  
> 
> Note that I'm marking this test random, since it is a comparison of types, which is architecture and sage-version dependent. 

Note : trac_9121.patch was already merged in sage-4.4.3.alpha1 only trac_9121-part2.patch needs to be merged... The patch looks good to me I'm waiting for the tests to finish.



---

archive/issue_comments_084837.json:
```json
{
    "body": "Changing keywords from \"\" to \"Sets comparison\".",
    "created_at": "2010-06-03T17:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9121#issuecomment-84837",
    "user": "hivert"
}
```

Changing keywords from "" to "Sets comparison".



---

archive/issue_comments_084838.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-03T17:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9121#issuecomment-84838",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084839.json:
```json
{
    "body": "All tests passed!",
    "created_at": "2010-06-03T17:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9121#issuecomment-84839",
    "user": "hivert"
}
```

All tests passed!



---

archive/issue_comments_084840.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-04T15:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9121#issuecomment-84840",
    "user": "was"
}
```

Resolution: fixed
