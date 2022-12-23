# Issue 3668: Functionality of "Set"

archive/issues_003668.json:
```json
{
    "body": "Assignee: tba\n\nCC:  sage-combinat\n\nIn the documentation for the function \"Set\" (Reference Manual 11.8) it would be helpful to explicitly point out that Set allows objects of different types, so \n\n\n```\nsage: Set([Sequence(my_seq),3,QQ])\n{Rational Field, 3, [2, 3]}}}}\n\nis perfectly OK.\n\nAlso, it would be nice if Set allowed one to use lists, so\n\n`Set([[2,3]])`\n\nworked, rather than giving the error message ``TypeError: list objects are unhashable''.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3668\n\n",
    "created_at": "2008-07-16T22:25:58Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "Functionality of \"Set\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3668",
    "user": "ljpk"
}
```
Assignee: tba

CC:  sage-combinat

In the documentation for the function "Set" (Reference Manual 11.8) it would be helpful to explicitly point out that Set allows objects of different types, so 


```
sage: Set([Sequence(my_seq),3,QQ])
{Rational Field, 3, [2, 3]}}}}

is perfectly OK.

Also, it would be nice if Set allowed one to use lists, so

`Set([[2,3]])`

worked, rather than giving the error message ``TypeError: list objects are unhashable''.

Issue created by migration from https://trac.sagemath.org/ticket/3668





---

archive/issue_comments_025922.json:
```json
{
    "body": "Added documentation that `Set` can take arbitrary hashable objects and raises an exception if one of the objects is not. Also cleaned up some of the documentation. Based on the (one line change) #11366.",
    "created_at": "2012-11-18T04:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25922",
    "user": "tscrim"
}
```

Added documentation that `Set` can take arbitrary hashable objects and raises an exception if one of the objects is not. Also cleaned up some of the documentation. Based on the (one line change) #11366.



---

archive/issue_comments_025923.json:
```json
{
    "body": "Changing keywords from \"\" to \"documentation\".",
    "created_at": "2012-11-18T04:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25923",
    "user": "tscrim"
}
```

Changing keywords from "" to "documentation".



---

archive/issue_comments_025924.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-11-18T04:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25924",
    "user": "tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_025925.json:
```json
{
    "body": "Changing assignee from tba to tscrim.",
    "created_at": "2012-11-26T06:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25925",
    "user": "tscrim"
}
```

Changing assignee from tba to tscrim.



---

archive/issue_comments_025926.json:
```json
{
    "body": "Good to go !\n\nNathann",
    "created_at": "2013-04-21T19:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25926",
    "user": "ncohen"
}
```

Good to go !

Nathann



---

archive/issue_comments_025927.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-21T19:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25927",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025928.json:
```json
{
    "body": "Thanks for the review Nathann.",
    "created_at": "2013-04-21T20:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25928",
    "user": "tscrim"
}
```

Thanks for the review Nathann.



---

archive/issue_comments_025929.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-04-22T05:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25929",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_025930.json:
```json
{
    "body": "What's the point of tests like\n\n```\nsage: hash(s) == hash(s) \nTrue\n```\n\n\nI prefer to keep the actual hash in this case:\n\n```\nsage: hash(s)\n1234   # 32-bit\n56789  # 64-bit\n```\n\n\nMinor comment: `#indirect doctest` isn't needed for `_underscored_` methods.",
    "created_at": "2013-04-22T05:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25930",
    "user": "jdemeyer"
}
```

What's the point of tests like

```
sage: hash(s) == hash(s) 
True
```


I prefer to keep the actual hash in this case:

```
sage: hash(s)
1234   # 32-bit
56789  # 64-bit
```


Minor comment: `#indirect doctest` isn't needed for `_underscored_` methods.



---

archive/issue_comments_025931.json:
```json
{
    "body": "Replying to [comment:9 jdemeyer]:\n> What's the point of tests like\n> {{{\n> sage: hash(s) == hash(s) \n> True\n> }}}\n> \n> I prefer to keep the actual hash in this case:\n> {{{\n> sage: hash(s)\n> 1234   # 32-bit\n> 56789  # 64-bit\n> }}}\n\nThe main reason is so that the output does not change if the hash value of the underlying object changes, but it still tests that it is hashable. (Plus it means we don't need to find a 32 and 64 bit machine to test.) I remember there being a discussion about this, but I don't remember/can't find which ticket this came up in (I believe there was a sage-devel topic on this, but I can't find it either).\n\nHowever I can reset the one doctest back and change the other one to reflect the behavior of the `__hash__()` function.\n\n> Minor comment: `#indirect doctest` isn't needed for `_underscored_` methods.\n\nI wrote this before the switch to the new doctesting framework and were needed then if `_underscored_` methods weren't explicity called. I'll remove them on the next version of the patch.",
    "created_at": "2013-04-22T21:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25931",
    "user": "tscrim"
}
```

Replying to [comment:9 jdemeyer]:
> What's the point of tests like
> {{{
> sage: hash(s) == hash(s) 
> True
> }}}
> 
> I prefer to keep the actual hash in this case:
> {{{
> sage: hash(s)
> 1234   # 32-bit
> 56789  # 64-bit
> }}}

The main reason is so that the output does not change if the hash value of the underlying object changes, but it still tests that it is hashable. (Plus it means we don't need to find a 32 and 64 bit machine to test.) I remember there being a discussion about this, but I don't remember/can't find which ticket this came up in (I believe there was a sage-devel topic on this, but I can't find it either).

However I can reset the one doctest back and change the other one to reflect the behavior of the `__hash__()` function.

> Minor comment: `#indirect doctest` isn't needed for `_underscored_` methods.

I wrote this before the switch to the new doctesting framework and were needed then if `_underscored_` methods weren't explicity called. I'll remove them on the next version of the patch.



---

archive/issue_comments_025932.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-12T09:41:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25932",
    "user": "tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_025933.json:
```json
{
    "body": "Attachment\n\nNew version which keeps the actual hash and removes now unneeded `#indirect doctests`.",
    "created_at": "2013-07-12T09:41:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25933",
    "user": "tscrim"
}
```

Attachment

New version which keeps the actual hash and removes now unneeded `#indirect doctests`.



---

archive/issue_comments_025934.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-07-12T10:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25934",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025935.json:
```json
{
    "body": "Wellllllll, then `:-)`\n\nNathann",
    "created_at": "2013-07-12T10:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25935",
    "user": "ncohen"
}
```

Wellllllll, then `:-)`

Nathann



---

archive/issue_comments_025936.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-08-16T21:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25936",
    "user": "jdemeyer"
}
```

Resolution: fixed
