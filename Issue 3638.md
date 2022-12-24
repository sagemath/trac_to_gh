# Issue 3638: Vector equality coercion problems

archive/issues_003638.json:
```json
{
    "body": "Assignee: tbd\n\nI think this bit of code should not produce an exception.  The vectors should both be coerced to belong to Z8!^3 and compared.\n\n```\nsage: Z8=IntegerModRing(8)\nsage: vector(ZZ,[1,2,11])==vector(Z8,[1,2,3])\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n...\nAttributeError: 'FreeModule_ambient' object has no attribute 'ambient_vector_space'\n```\n\n\nNote that a similar thing seems to work in other cases (because 7 is prime and Z7 is a field?).\n\n```\nsage: Z7=IntegerModRing(7)\nsage: vector(ZZ,[1,2,10])==vector(Z7,[1,2,3])\nTrue\n```\n\n\n\nThis may or may not be related, but combining QQ and Z7 produces some wrong results:\n\n```\nsage: Z7=IntegerModRing(7)\nsage: vector(Z7,[1,2,3])==vector(QQ,[1,2,3])\nFalse\n```\n\nThat those vectors are not equal is truly disturbing.  This should either raise an exception about not having compatible parents or should be True.  I'll let the coercion guru's argue about that. :)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3638\n\n",
    "created_at": "2008-07-11T02:08:47Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Vector equality coercion problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3638",
    "user": "jbmohler"
}
```
Assignee: tbd

I think this bit of code should not produce an exception.  The vectors should both be coerced to belong to Z8!^3 and compared.

```
sage: Z8=IntegerModRing(8)
sage: vector(ZZ,[1,2,11])==vector(Z8,[1,2,3])
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
...
AttributeError: 'FreeModule_ambient' object has no attribute 'ambient_vector_space'
```


Note that a similar thing seems to work in other cases (because 7 is prime and Z7 is a field?).

```
sage: Z7=IntegerModRing(7)
sage: vector(ZZ,[1,2,10])==vector(Z7,[1,2,3])
True
```



This may or may not be related, but combining QQ and Z7 produces some wrong results:

```
sage: Z7=IntegerModRing(7)
sage: vector(Z7,[1,2,3])==vector(QQ,[1,2,3])
False
```

That those vectors are not equal is truly disturbing.  This should either raise an exception about not having compatible parents or should be True.  I'll let the coercion guru's argue about that. :)

Issue created by migration from https://trac.sagemath.org/ticket/3638





---

archive/issue_comments_025731.json:
```json
{
    "body": "Changing assignee from tbd to malb.",
    "created_at": "2009-01-25T19:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3638#issuecomment-25731",
    "user": "malb"
}
```

Changing assignee from tbd to malb.



---

archive/issue_comments_025732.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-25T19:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3638#issuecomment-25732",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025733.json:
```json
{
    "body": "Attachment [3638-free-module-coerce.patch](tarball://root/attachments/some-uuid/ticket3638/3638-free-module-coerce.patch) by robertwb created at 2010-01-17 09:43:06\n\nFixed the Z/8Z case. As for Z/7Z and Q, they are incomparable, which by convention means == returns False. (If it gave an error,we would have to re-think nonsense like `\"some string\" != random_matrix(ZZ, 3)` returning False).",
    "created_at": "2010-01-17T09:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3638#issuecomment-25733",
    "user": "robertwb"
}
```

Attachment [3638-free-module-coerce.patch](tarball://root/attachments/some-uuid/ticket3638/3638-free-module-coerce.patch) by robertwb created at 2010-01-17 09:43:06

Fixed the Z/8Z case. As for Z/7Z and Q, they are incomparable, which by convention means == returns False. (If it gave an error,we would have to re-think nonsense like `"some string" != random_matrix(ZZ, 3)` returning False).



---

archive/issue_comments_025734.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T09:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3638#issuecomment-25734",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_025735.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-01-19T01:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3638#issuecomment-25735",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_025736.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T01:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3638#issuecomment-25736",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025737.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T05:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3638#issuecomment-25737",
    "user": "rlm"
}
```

Resolution: fixed
