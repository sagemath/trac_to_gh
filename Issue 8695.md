# Issue 8695: UniqueRepresentations implements __eq__ but not __ne__

archive/issues_008695.json:
```json
{
    "body": "Assignee: hivert\n\nCC:  sage-combinat\n\nKeywords: UniqueRepresentation, equality\n\nPython manuals says:\n\n    There are no implied relationships among the comparison operators. The truth of x==y does not imply that x!=y is false. Accordingly, when defining __eq__(), one should also define __ne__() so that the operators will behave as expected.\n\nUniqueRepresentation fails to comply with this. As a consequence:\n\n```\nsage: G6 = GL(6, QQ)\nsage: G6 == G6\nTrue\nsage: G6 != G6\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n...\nNotImplementedError: Matrix group over Rational Field not implemented.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8695\n\n",
    "created_at": "2010-04-16T15:13:49Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "UniqueRepresentations implements __eq__ but not __ne__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8695",
    "user": "hivert"
}
```
Assignee: hivert

CC:  sage-combinat

Keywords: UniqueRepresentation, equality

Python manuals says:

    There are no implied relationships among the comparison operators. The truth of x==y does not imply that x!=y is false. Accordingly, when defining __eq__(), one should also define __ne__() so that the operators will behave as expected.

UniqueRepresentation fails to comply with this. As a consequence:

```
sage: G6 = GL(6, QQ)
sage: G6 == G6
True
sage: G6 != G6
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
...
NotImplementedError: Matrix group over Rational Field not implemented.
```


Issue created by migration from https://trac.sagemath.org/ticket/8695





---

archive/issue_comments_079208.json:
```json
{
    "body": "This should be ready for review.",
    "created_at": "2010-04-16T15:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79208",
    "user": "hivert"
}
```

This should be ready for review.



---

archive/issue_comments_079209.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-16T15:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79209",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079210.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-16T16:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79210",
    "user": "nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079211.json:
```json
{
    "body": "apply, tests, doc...\n\nPositive review for this patch.",
    "created_at": "2010-04-16T16:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79211",
    "user": "nborie"
}
```

apply, tests, doc...

Positive review for this patch.



---

archive/issue_comments_079212.json:
```json
{
    "body": "I am just not sure about forcing UniqueRepresentation to inherit from object. Let's discuss this over the phone.",
    "created_at": "2010-04-16T21:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79212",
    "user": "nthiery"
}
```

I am just not sure about forcing UniqueRepresentation to inherit from object. Let's discuss this over the phone.



---

archive/issue_comments_079213.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-16T21:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79213",
    "user": "nthiery"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_079214.json:
```json
{
    "body": "Also, this would have been caught by a _test_eq, which we should implement! See #8697!",
    "created_at": "2010-04-16T21:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79214",
    "user": "nthiery"
}
```

Also, this would have been caught by a _test_eq, which we should implement! See #8697!



---

archive/issue_comments_079215.json:
```json
{
    "body": "Replying to [comment:5 nthiery]:\n> Also, this would have been caught by a _test_eq, which we should implement! See #8697!\n\nActually that exactly how I caught it except that it was with _test_self_equal which is implemented in #8402. I think #8697 should be closed as a duplicate of #8402.",
    "created_at": "2010-04-16T23:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79215",
    "user": "hivert"
}
```

Replying to [comment:5 nthiery]:
> Also, this would have been caught by a _test_eq, which we should implement! See #8697!

Actually that exactly how I caught it except that it was with _test_self_equal which is implemented in #8402. I think #8697 should be closed as a duplicate of #8402.



---

archive/issue_comments_079216.json:
```json
{
    "body": "Replying to [comment:4 nthiery]:\n> I am just not sure about forcing UniqueRepresentation to inherit from object. Let's discuss this over the phone.\n\nThe only thing that inheriting from object does is make it a \"new-style\" class in Python, which is what everything should be now.  In the 3.x series, old-style classes are removed.  http://docs.python.org/reference/datamodel.html",
    "created_at": "2010-04-17T01:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79216",
    "user": "mhansen"
}
```

Replying to [comment:4 nthiery]:
> I am just not sure about forcing UniqueRepresentation to inherit from object. Let's discuss this over the phone.

The only thing that inheriting from object does is make it a "new-style" class in Python, which is what everything should be now.  In the 3.x series, old-style classes are removed.  http://docs.python.org/reference/datamodel.html



---

archive/issue_comments_079217.json:
```json
{
    "body": "Replying to [comment:6 hivert]:\n> Replying to [comment:5 nthiery]:\n> > Also, this would have been caught by a _test_eq, which we should implement! See #8697!\n> \n> Actually that exactly how I caught it except that it was with _test_self_equal which is implemented in #8402. I think #8697 should be closed as a duplicate of #8402.\n\nOops, right. I looked for that one and somehow missed it.",
    "created_at": "2010-04-17T20:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79217",
    "user": "nthiery"
}
```

Replying to [comment:6 hivert]:
> Replying to [comment:5 nthiery]:
> > Also, this would have been caught by a _test_eq, which we should implement! See #8697!
> 
> Actually that exactly how I caught it except that it was with _test_self_equal which is implemented in #8402. I think #8697 should be closed as a duplicate of #8402.

Oops, right. I looked for that one and somehow missed it.



---

archive/issue_comments_079218.json:
```json
{
    "body": "Replying to [comment:7 mhansen]:\n> Replying to [comment:4 nthiery]:\n> > I am just not sure about forcing UniqueRepresentation to inherit from object. Let's discuss this over the phone.\n> \n> The only thing that inheriting from object does is make it a \"new-style\" class in Python, which is what everything should be now.  In the 3.x series, old-style classes are removed.  http://docs.python.org/reference/datamodel.html\n\nYup! So there is particularly no point about forcing it explicitly, since it will be automatically the case later, and in the mean time there is no reason to fix something that ain't broken.\n\nWe discussed with Florent over the phone. He will remove the inheritance from object, reupload the patch, and set a positive review on my behalf.",
    "created_at": "2010-04-17T20:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79218",
    "user": "nthiery"
}
```

Replying to [comment:7 mhansen]:
> Replying to [comment:4 nthiery]:
> > I am just not sure about forcing UniqueRepresentation to inherit from object. Let's discuss this over the phone.
> 
> The only thing that inheriting from object does is make it a "new-style" class in Python, which is what everything should be now.  In the 3.x series, old-style classes are removed.  http://docs.python.org/reference/datamodel.html

Yup! So there is particularly no point about forcing it explicitly, since it will be automatically the case later, and in the mean time there is no reason to fix something that ain't broken.

We discussed with Florent over the phone. He will remove the inheritance from object, reupload the patch, and set a positive review on my behalf.



---

archive/issue_comments_079219.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-17T20:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79219",
    "user": "hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079220.json:
```json
{
    "body": "Attachment\n\n> We discussed with Florent over the phone. He will remove the inheritance from object, reupload the patch, and set a positive review on my behalf.\n\nDone !",
    "created_at": "2010-04-17T20:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79220",
    "user": "hivert"
}
```

Attachment

> We discussed with Florent over the phone. He will remove the inheritance from object, reupload the patch, and set a positive review on my behalf.

Done !



---

archive/issue_comments_079221.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-17T20:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79221",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079222.json:
```json
{
    "body": "Replying to [comment:10 hivert]:\n> > We discussed with Florent over the phone. He will remove the inheritance from object, reupload the patch, and set a positive review on my behalf.\n> \n> Done !\n\nAt put back to positive review.",
    "created_at": "2010-04-17T20:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79222",
    "user": "hivert"
}
```

Replying to [comment:10 hivert]:
> > We discussed with Florent over the phone. He will remove the inheritance from object, reupload the patch, and set a positive review on my behalf.
> 
> Done !

At put back to positive review.



---

archive/issue_comments_079223.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79223",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_079224.json:
```json
{
    "body": "Merged \"trac_8695-uniquerep_missing__ne__-fh.patch\" into 4.4.alpha1.",
    "created_at": "2010-04-19T05:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8695#issuecomment-79224",
    "user": "jhpalmieri"
}
```

Merged "trac_8695-uniquerep_missing__ne__-fh.patch" into 4.4.alpha1.
