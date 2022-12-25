# Issue 3668: Functionality of "Set"

archive/issues_003668.json:
```json
{
    "body": "Assignee: tba\n\nCC:  sage-combinat\n\nIn the documentation for the function \"Set\" (Reference Manual 11.8) it would be helpful to explicitly point out that Set allows objects of different types, so \n\n```\nsage: Set([Sequence(my_seq),3,QQ])\n{Rational Field, 3, [2, 3]}}}}\n\nis perfectly OK.\n\nAlso, it would be nice if Set allowed one to use lists, so\n\n`Set([[2,3]])`\n\nworked, rather than giving the error message ``TypeError: list objects are unhashable''.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3668\n\n",
    "created_at": "2008-07-16T22:25:58Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.12",
    "title": "Functionality of \"Set\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3668",
    "user": "https://trac.sagemath.org/admin/accounts/users/ljpk"
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

archive/issue_events_008397.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-14T23:03:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "milestone": "sage-3.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3668#event-8397"
}
```



---

archive/issue_comments_025868.json:
```json
{
    "body": "Added documentation that `Set` can take arbitrary hashable objects and raises an exception if one of the objects is not. Also cleaned up some of the documentation. Based on the (one line change) #11366.",
    "created_at": "2012-11-18T04:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25868",
    "user": "https://github.com/tscrim"
}
```

Added documentation that `Set` can take arbitrary hashable objects and raises an exception if one of the objects is not. Also cleaned up some of the documentation. Based on the (one line change) #11366.



---

archive/issue_comments_025869.json:
```json
{
    "body": "Changing keywords from \"\" to \"documentation\".",
    "created_at": "2012-11-18T04:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25869",
    "user": "https://github.com/tscrim"
}
```

Changing keywords from "" to "documentation".



---

archive/issue_comments_025870.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-11-18T04:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25870",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_025871.json:
```json
{
    "body": "Changing assignee from tba to @tscrim.",
    "created_at": "2012-11-26T06:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25871",
    "user": "https://github.com/tscrim"
}
```

Changing assignee from tba to @tscrim.



---

archive/issue_comments_025872.json:
```json
{
    "body": "Good to go !\n\nNathann",
    "created_at": "2013-04-21T19:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25872",
    "user": "https://github.com/nathanncohen"
}
```

Good to go !

Nathann



---

archive/issue_comments_025873.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-21T19:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25873",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025874.json:
```json
{
    "body": "Thanks for the review Nathann.",
    "created_at": "2013-04-21T20:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25874",
    "user": "https://github.com/tscrim"
}
```

Thanks for the review Nathann.



---

archive/issue_comments_025875.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-04-22T05:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25875",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_025876.json:
```json
{
    "body": "What's the point of tests like\n\n```\nsage: hash(s) == hash(s) \nTrue\n```\n\nI prefer to keep the actual hash in this case:\n\n```\nsage: hash(s)\n1234   # 32-bit\n56789  # 64-bit\n```\n\nMinor comment: `#indirect doctest` isn't needed for `_underscored_` methods.",
    "created_at": "2013-04-22T05:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25876",
    "user": "https://github.com/jdemeyer"
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

archive/issue_comments_025877.json:
```json
{
    "body": "Replying to [comment:9 jdemeyer]:\n> What's the point of tests like\n> \n> ```\n> sage: hash(s) == hash(s) \n> True\n> ```\n> \n> I prefer to keep the actual hash in this case:\n> \n> ```\n> sage: hash(s)\n> 1234   # 32-bit\n> 56789  # 64-bit\n> ```\n\n\nThe main reason is so that the output does not change if the hash value of the underlying object changes, but it still tests that it is hashable. (Plus it means we don't need to find a 32 and 64 bit machine to test.) I remember there being a discussion about this, but I don't remember/can't find which ticket this came up in (I believe there was a sage-devel topic on this, but I can't find it either).\n\nHowever I can reset the one doctest back and change the other one to reflect the behavior of the `__hash__()` function.\n\n> Minor comment: `#indirect doctest` isn't needed for `_underscored_` methods.\n\n\nI wrote this before the switch to the new doctesting framework and were needed then if `_underscored_` methods weren't explicity called. I'll remove them on the next version of the patch.",
    "created_at": "2013-04-22T21:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25877",
    "user": "https://github.com/tscrim"
}
```

Replying to [comment:9 jdemeyer]:
> What's the point of tests like
> 
> ```
> sage: hash(s) == hash(s) 
> True
> ```
> 
> I prefer to keep the actual hash in this case:
> 
> ```
> sage: hash(s)
> 1234   # 32-bit
> 56789  # 64-bit
> ```


The main reason is so that the output does not change if the hash value of the underlying object changes, but it still tests that it is hashable. (Plus it means we don't need to find a 32 and 64 bit machine to test.) I remember there being a discussion about this, but I don't remember/can't find which ticket this came up in (I believe there was a sage-devel topic on this, but I can't find it either).

However I can reset the one doctest back and change the other one to reflect the behavior of the `__hash__()` function.

> Minor comment: `#indirect doctest` isn't needed for `_underscored_` methods.


I wrote this before the switch to the new doctesting framework and were needed then if `_underscored_` methods weren't explicity called. I'll remove them on the next version of the patch.



---

archive/issue_comments_025878.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-12T09:41:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25878",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_025879.json:
```json
{
    "body": "Attachment [trac_3668-set_doc_update-ts.patch](tarball://root/attachments/some-uuid/ticket3668/trac_3668-set_doc_update-ts.patch) by @tscrim created at 2013-07-12 09:41:02\n\nNew version which keeps the actual hash and removes now unneeded `#indirect doctests`.",
    "created_at": "2013-07-12T09:41:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25879",
    "user": "https://github.com/tscrim"
}
```

Attachment [trac_3668-set_doc_update-ts.patch](tarball://root/attachments/some-uuid/ticket3668/trac_3668-set_doc_update-ts.patch) by @tscrim created at 2013-07-12 09:41:02

New version which keeps the actual hash and removes now unneeded `#indirect doctests`.



---

archive/issue_comments_025880.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-07-12T10:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25880",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025881.json:
```json
{
    "body": "Wellllllll, then `:-)`\n\nNathann",
    "created_at": "2013-07-12T10:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25881",
    "user": "https://github.com/nathanncohen"
}
```

Wellllllll, then `:-)`

Nathann



---

archive/issue_events_008398.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-07-24T06:36:59Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "milestone": "sage-3.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3668#event-8398"
}
```



---

archive/issue_events_008399.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-07-24T06:36:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3668#event-8399"
}
```



---

archive/issue_comments_025882.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-08-16T21:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3668#issuecomment-25882",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_008400.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-16T21:17:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3668",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3668#event-8400"
}
```
