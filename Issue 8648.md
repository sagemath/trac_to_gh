# Issue 8648: Generic __call__ function for parents prevents empty input in constructor

archive/issues_008648.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  sage-combinat\n\nKeywords: element constructor\n\nGeneric __call__ function for parents has a default value for its first argument. This prevents from making a difference between A() and A(0). This causes problems for crystal code, where the typical input is A(2,1,4,3,0,...). For example:\n\n\n```\n    sage: T = CrystalOfTableaux(['B',3], shape=[3])\n    sage: t=T(1,2,0)\n    sage: t\n    [[1, 2, 0]]\n\n    sage: T = CrystalOfTableaux(['B',3], shape=[])\n    sage: t=T()\n    sage: t     # goes boom\n    sage: t._list # this list should be empty\n    [0]\n```\n\n\nSuggestion: self.__call__() could instead call right away self._element_constructor_().\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8648\n\n",
    "created_at": "2010-04-03T15:34:28Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "title": "Generic __call__ function for parents prevents empty input in constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8648",
    "user": "https://github.com/anneschilling"
}
```
Assignee: @robertwb

CC:  sage-combinat

Keywords: element constructor

Generic __call__ function for parents has a default value for its first argument. This prevents from making a difference between A() and A(0). This causes problems for crystal code, where the typical input is A(2,1,4,3,0,...). For example:


```
    sage: T = CrystalOfTableaux(['B',3], shape=[3])
    sage: t=T(1,2,0)
    sage: t
    [[1, 2, 0]]

    sage: T = CrystalOfTableaux(['B',3], shape=[])
    sage: t=T()
    sage: t     # goes boom
    sage: t._list # this list should be empty
    [0]
```


Suggestion: self.__call__() could instead call right away self._element_constructor_().


Issue created by migration from https://trac.sagemath.org/ticket/8648





---

archive/issue_comments_078333.json:
```json
{
    "body": "An alternate suggestion: in CrystalOfTableaux define\n\n\n```\n\n    def __call__(self, x=[], *args, **kwds):\n        return Parent.__call__(self, x, *args, **kwds)\n\n```\n",
    "created_at": "2010-10-16T23:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8648#issuecomment-78333",
    "user": "https://github.com/roed314"
}
```

An alternate suggestion: in CrystalOfTableaux define


```

    def __call__(self, x=[], *args, **kwds):
        return Parent.__call__(self, x, *args, **kwds)

```




---

archive/issue_comments_078334.json:
```json
{
    "body": "Oh, I see.  The issue is that the generic call is constructing a morphism from the parent of x, and so x can't be non-existent.  You may need to just completely override the generic `Parent.__call__`.",
    "created_at": "2010-10-16T23:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8648#issuecomment-78334",
    "user": "https://github.com/roed314"
}
```

Oh, I see.  The issue is that the generic call is constructing a morphism from the parent of x, and so x can't be non-existent.  You may need to just completely override the generic `Parent.__call__`.



---

archive/issue_comments_078335.json:
```json
{
    "body": "Hi David!\n\nThanks for your feedback!\n\nReplying to [comment:2 roed]:\n> Oh, I see.  The issue is that the generic call is constructing a morphism from the parent of x, and so x can't be non-existent.  You may need to just completely override the generic `Parent.__call__`.  \n\nI'd rather not duplicate that rather technical code :-) And still we want to benefit from coercion ... \n\nDo you see an inconvenient to the first approach suggested?",
    "created_at": "2010-10-20T20:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8648#issuecomment-78335",
    "user": "https://github.com/nthiery"
}
```

Hi David!

Thanks for your feedback!

Replying to [comment:2 roed]:
> Oh, I see.  The issue is that the generic call is constructing a morphism from the parent of x, and so x can't be non-existent.  You may need to just completely override the generic `Parent.__call__`.  

I'd rather not duplicate that rather technical code :-) And still we want to benefit from coercion ... 

Do you see an inconvenient to the first approach suggested?



---

archive/issue_comments_078336.json:
```json
{
    "body": "I think the \n\n\n```\n    def __call__(self, x=[], *args, **kwds):\n        return Parent.__call__(self, x, *args, **kwds)\n```\n\n\napproach is probably the best.  I had to do this recently when converting some old code to use the new `Parent.__call__`.",
    "created_at": "2010-10-20T20:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8648#issuecomment-78336",
    "user": "https://github.com/mwhansen"
}
```

I think the 


```
    def __call__(self, x=[], *args, **kwds):
        return Parent.__call__(self, x, *args, **kwds)
```


approach is probably the best.  I had to do this recently when converting some old code to use the new `Parent.__call__`.



---

archive/issue_comments_078337.json:
```json
{
    "body": "My second comment was in error, and as Mike says, my first suggestion should work.",
    "created_at": "2010-10-20T21:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8648#issuecomment-78337",
    "user": "https://github.com/roed314"
}
```

My second comment was in error, and as Mike says, my first suggestion should work.



---

archive/issue_comments_078338.json:
```json
{
    "body": "Isn't this a rather ugly workaround? How about we just default to `x=None` and if it is unchanged we call `_element_constructor_`?",
    "created_at": "2013-12-23T21:13:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8648#issuecomment-78338",
    "user": "https://github.com/vbraun"
}
```

Isn't this a rather ugly workaround? How about we just default to `x=None` and if it is unchanged we call `_element_constructor_`?



---

archive/issue_comments_078339.json:
```json
{
    "body": "I'm not sure why that's much different.  The whole point is that calling with no arguments should be the same as calling with the empty list.",
    "created_at": "2013-12-27T13:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8648#issuecomment-78339",
    "user": "https://github.com/mwhansen"
}
```

I'm not sure why that's much different.  The whole point is that calling with no arguments should be the same as calling with the empty list.
