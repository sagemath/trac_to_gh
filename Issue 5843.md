# Issue 5843: race condition in cached_method (should not be shared between instances)

archive/issues_005843.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat @mwhansen\n\nKeywords: race condition, cached_method, cache\n\nConsider the following class (simplified from a real life example, after 3 hours of heisenbug debugging):\n\n```\nclass bla:\n    def __init__(self, value):\n        self.value = value\n    #\n    @cached_method\n    def f(self, x):\n        return self.value\n```\n\nThe method f ignores its input, and should return self.value:\n\n```\nsage: x = bla(1)\nsage: y = bla(2)\nsage: x.f(None)\n1\nsage: y.f(None)\n2\n```\n\nThen, y.f(x.f) should ignore the inner x.f and return 2. It does not:\n\n```\nsage: sage: y.f(x.f)\n1\n```\n\nThe reason is that x.f and y.f, and all other instances of bla share the same cached_method object.\n\n```\nsage: x.f is y.f\nTrue\nsage: x.f is x.__class__.f\nTrue\n```\n\nand the _instance field is set to the latest instance for which this method has been queried:\n\n```\nsage: yf = y.f\nsage: yf._instance is y\nTrue\nsage: x.f\nCached version of <function f at 0xb532d84>\nsage: yf._instance is y\nFalse\nsage: yf._instance is x\nTrue\n```\n\nMost of the time things work well, but there can be race conditions, as in the example above.\n\nNicolas and Florent\n\nIssue created by migration from https://trac.sagemath.org/ticket/5843\n\n",
    "closed_at": "2010-01-24T02:09:07Z",
    "created_at": "2009-04-21T08:43:49Z",
    "labels": [
        "component: misc",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "race condition in cached_method (should not be shared between instances)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5843",
    "user": "https://github.com/nthiery"
}
```
Assignee: @mwhansen

CC:  sage-combinat @mwhansen

Keywords: race condition, cached_method, cache

Consider the following class (simplified from a real life example, after 3 hours of heisenbug debugging):

```
class bla:
    def __init__(self, value):
        self.value = value
    #
    @cached_method
    def f(self, x):
        return self.value
```

The method f ignores its input, and should return self.value:

```
sage: x = bla(1)
sage: y = bla(2)
sage: x.f(None)
1
sage: y.f(None)
2
```

Then, y.f(x.f) should ignore the inner x.f and return 2. It does not:

```
sage: sage: y.f(x.f)
1
```

The reason is that x.f and y.f, and all other instances of bla share the same cached_method object.

```
sage: x.f is y.f
True
sage: x.f is x.__class__.f
True
```

and the _instance field is set to the latest instance for which this method has been queried:

```
sage: yf = y.f
sage: yf._instance is y
True
sage: x.f
Cached version of <function f at 0xb532d84>
sage: yf._instance is y
False
sage: yf._instance is x
True
```

Most of the time things work well, but there can be race conditions, as in the example above.

Nicolas and Florent

Issue created by migration from https://trac.sagemath.org/ticket/5843





---

archive/issue_comments_045853.json:
```json
{
    "body": "Possible correct implementation:\n   cached_method could return a closure instead of function object. Upon assignment to the\n   class, this closure would become just a usual unbound method, removing the need to handle\n   by hand the instance binding.",
    "created_at": "2009-04-21T08:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45853",
    "user": "https://github.com/nthiery"
}
```

Possible correct implementation:
   cached_method could return a closure instead of function object. Upon assignment to the
   class, this closure would become just a usual unbound method, removing the need to handle
   by hand the instance binding.



---

archive/issue_comments_045854.json:
```json
{
    "body": "Attachment [5843_CachedMethodCaller.patch](tarball://root/attachments/some-uuid/ticket5843/5843_CachedMethodCaller.patch) by @wjp created at 2010-01-18 22:52:38",
    "created_at": "2010-01-18T22:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45854",
    "user": "https://github.com/wjp"
}
```

Attachment [5843_CachedMethodCaller.patch](tarball://root/attachments/some-uuid/ticket5843/5843_CachedMethodCaller.patch) by @wjp created at 2010-01-18 22:52:38



---

archive/issue_comments_045855.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T23:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45855",
    "user": "https://github.com/wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_045856.json:
```json
{
    "body": "I added a patch that returns a (newly created) `CachedMethodCaller` object from `CachedMethod.__get__` that stores the instance on which the `CachedMethod` was called.\n\nAdditionally this object has a `__get__` of its own that does the same to handle stored copies of `CachedMethodCaller`s, which is something that categories seem to do.\n\nUsing a function/closure would also handle the caching (and I added a comment in the patch on how to do it exactly), but you would lose the ability to call methods like `is_in_cache()` which are used in some places in sage.",
    "created_at": "2010-01-18T23:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45856",
    "user": "https://github.com/wjp"
}
```

I added a patch that returns a (newly created) `CachedMethodCaller` object from `CachedMethod.__get__` that stores the instance on which the `CachedMethod` was called.

Additionally this object has a `__get__` of its own that does the same to handle stored copies of `CachedMethodCaller`s, which is something that categories seem to do.

Using a function/closure would also handle the caching (and I added a comment in the patch on how to do it exactly), but you would lose the ability to call methods like `is_in_cache()` which are used in some places in sage.



---

archive/issue_comments_045857.json:
```json
{
    "body": "Excellent patch (I couldn't figure out how to fix this, glad you did), but there doesn't seem to be a test for the main problem:\n\n```\nclass bla:\n    def __init__(self, value):\n        self.value = value\n    #\n    @cached_method\n    def f(self, x):\n        return self.value\n```\n\nThe method f ignores its input, and should return self.value:\n\n```\nsage: x = bla(1)\nsage: y = bla(2)\nsage: x.f(None)\n1\nsage: y.f(None)\n2\n```\n\nThen, y.f(x.f) should ignore the inner x.f and return 2. It does not:\n\n```\nsage: sage: y.f(x.f)\n1\n```",
    "created_at": "2010-01-20T11:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45857",
    "user": "https://github.com/TimDumol"
}
```

Excellent patch (I couldn't figure out how to fix this, glad you did), but there doesn't seem to be a test for the main problem:

```
class bla:
    def __init__(self, value):
        self.value = value
    #
    @cached_method
    def f(self, x):
        return self.value
```

The method f ignores its input, and should return self.value:

```
sage: x = bla(1)
sage: y = bla(2)
sage: x.f(None)
1
sage: y.f(None)
2
```

Then, y.f(x.f) should ignore the inner x.f and return 2. It does not:

```
sage: sage: y.f(x.f)
1
```



---

archive/issue_comments_045858.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T11:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45858",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_045859.json:
```json
{
    "body": "Attachment [5843_doctests.patch](tarball://root/attachments/some-uuid/ticket5843/5843_doctests.patch) by @wjp created at 2010-01-20 19:06:51\n\nGood point. I replaced the doctest patch with one that adds a more direct test for this ticket.",
    "created_at": "2010-01-20T19:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45859",
    "user": "https://github.com/wjp"
}
```

Attachment [5843_doctests.patch](tarball://root/attachments/some-uuid/ticket5843/5843_doctests.patch) by @wjp created at 2010-01-20 19:06:51

Good point. I replaced the doctest patch with one that adds a more direct test for this ticket.



---

archive/issue_comments_045860.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T19:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45860",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_045861.json:
```json
{
    "body": "Nice. I'm giving this a positive review, but I've attached a little patch that transfers some of the documentation from the `__init__` method to the the class itself, and adds some more documentation. It would be great for you to review it.",
    "created_at": "2010-01-20T20:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45861",
    "user": "https://github.com/TimDumol"
}
```

Nice. I'm giving this a positive review, but I've attached a little patch that transfers some of the documentation from the `__init__` method to the the class itself, and adds some more documentation. It would be great for you to review it.



---

archive/issue_comments_045862.json:
```json
{
    "body": "Attachment [trac_5843-doctests-ref.patch](tarball://root/attachments/some-uuid/ticket5843/trac_5843-doctests-ref.patch) by @TimDumol created at 2010-01-20 20:18:31\n\nAdds a little bit more documentation to CachedMethod.",
    "created_at": "2010-01-20T20:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45862",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_5843-doctests-ref.patch](tarball://root/attachments/some-uuid/ticket5843/trac_5843-doctests-ref.patch) by @TimDumol created at 2010-01-20 20:18:31

Adds a little bit more documentation to CachedMethod.



---

archive/issue_comments_045863.json:
```json
{
    "body": "Attachment [trac_5843-doctests-ref.2.patch](tarball://root/attachments/some-uuid/ticket5843/trac_5843-doctests-ref.2.patch) by @TimDumol created at 2010-01-20 21:54:07\n\nChanges the doctest to use `print` instead of `sleep`",
    "created_at": "2010-01-20T21:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45863",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_5843-doctests-ref.2.patch](tarball://root/attachments/some-uuid/ticket5843/trac_5843-doctests-ref.2.patch) by @TimDumol created at 2010-01-20 21:54:07

Changes the doctest to use `print` instead of `sleep`



---

archive/issue_comments_045864.json:
```json
{
    "body": "Looks good. Thanks!\n\n\nPatches to apply, in order:\n5843_CachedMethodCaller.patch\n5843_doctests.patch\ntrac_5843-doctests-ref.2.patch",
    "created_at": "2010-01-20T21:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45864",
    "user": "https://github.com/wjp"
}
```

Looks good. Thanks!


Patches to apply, in order:
5843_CachedMethodCaller.patch
5843_doctests.patch
trac_5843-doctests-ref.2.patch



---

archive/issue_comments_045865.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T21:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45865",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_045866.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-24T02:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45866",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_013744.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-24T02:09:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5843#event-13744"
}
```



---

archive/issue_comments_045867.json:
```json
{
    "body": "Merged patches in this order:\n\n1. [5843_CachedMethodCaller.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5843/5843_CachedMethodCaller.patch)\n2. [5843_doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5843/5843_doctests.patch)\n3. [trac_5843-doctests-ref.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5843/trac_5843-doctests-ref.2.patch) --- timdumol: please remember to put your username in your patch. I have committed this patch in your name.",
    "created_at": "2010-01-24T02:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45867",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged patches in this order:

1. [5843_CachedMethodCaller.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5843/5843_CachedMethodCaller.patch)
2. [5843_doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5843/5843_doctests.patch)
3. [trac_5843-doctests-ref.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5843/trac_5843-doctests-ref.2.patch) --- timdumol: please remember to put your username in your patch. I have committed this patch in your name.



---

archive/issue_comments_045868.json:
```json
{
    "body": "Willem, Tim: thanks so much for fixing this!",
    "created_at": "2010-01-24T21:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45868",
    "user": "https://github.com/nthiery"
}
```

Willem, Tim: thanks so much for fixing this!



---

archive/issue_comments_045869.json:
```json
{
    "body": "Btw: #383 plays similar trick. Maybe Sage (actually Python) should have a standard tool for method wrappers as there already is for functions (see functools.wrapper).",
    "created_at": "2010-01-24T21:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5843#issuecomment-45869",
    "user": "https://github.com/nthiery"
}
```

Btw: #383 plays similar trick. Maybe Sage (actually Python) should have a standard tool for method wrappers as there already is for functions (see functools.wrapper).
