# Issue 8250: Extend ClasscallMetaclass to allow for binding behavior

archive/issues_008250.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat\n\nKeywords: ClassCall, descriptor, __classget__\n\nFrom the documentation:\n\n(using this patch) we show how to implement a nested class Foo.Bar\nwith a binding behavior, as if it was a method of Foo: namely for\n``foo`` an instance of ``Foo``, calling ``foo.Bar()`` is equivalent to\n``Foo.Bar(foo)``::\n\n\n```\n            sage: import functools\n            sage: from sage.misc.classcall_metaclass import ClasscallMetaclass\n            sage: class Foo:\n            ...       class Bar(object):\n            ...           __metaclass__ = ClasscallMetaclass\n            ...           @staticmethod\n            ...           def __classget__(cls, instance, owner):\n            ...               print \"calling __classget__\"\n            ...               if instance is None:\n            ...                   return cls\n            ...               return functools.partial(cls, instance)\n            ...           def __init__(self, instance):\n            ...               self.instance = instance\n            sage: foo = Foo()\n            sage: bar = foo.Bar()\n            calling __classget__\n            sage: bar.instance == foo\n            True\n```\n\n\nThis will be used by the upcoming improvements to the functorial constructions in categories\n\nIssue created by migration from https://trac.sagemath.org/ticket/8250\n\n",
    "created_at": "2010-02-12T15:12:34Z",
    "labels": [
        "categories",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Extend ClasscallMetaclass to allow for binding behavior",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8250",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat

Keywords: ClassCall, descriptor, __classget__

From the documentation:

(using this patch) we show how to implement a nested class Foo.Bar
with a binding behavior, as if it was a method of Foo: namely for
``foo`` an instance of ``Foo``, calling ``foo.Bar()`` is equivalent to
``Foo.Bar(foo)``::


```
            sage: import functools
            sage: from sage.misc.classcall_metaclass import ClasscallMetaclass
            sage: class Foo:
            ...       class Bar(object):
            ...           __metaclass__ = ClasscallMetaclass
            ...           @staticmethod
            ...           def __classget__(cls, instance, owner):
            ...               print "calling __classget__"
            ...               if instance is None:
            ...                   return cls
            ...               return functools.partial(cls, instance)
            ...           def __init__(self, instance):
            ...               self.instance = instance
            sage: foo = Foo()
            sage: bar = foo.Bar()
            calling __classget__
            sage: bar.instance == foo
            True
```


This will be used by the upcoming improvements to the functorial constructions in categories

Issue created by migration from https://trac.sagemath.org/ticket/8250





---

archive/issue_comments_072975.json:
```json
{
    "body": "This is a check to see if CC to sage-combinat-commits is working.\nApologies for the trouble. \n\n\nCheers,\n\nFlorent",
    "created_at": "2010-02-12T16:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72975",
    "user": "hivert"
}
```

This is a check to see if CC to sage-combinat-commits is working.
Apologies for the trouble. 


Cheers,

Florent



---

archive/issue_comments_072976.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-12T16:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72976",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072977.json:
```json
{
    "body": "Hi Nicolas,\n\nThey are a few problem with this patch:\n- it seems that line 119-125 (in the file) does not belongs to there ! They are after a return. Are they a bad copy paste ?\n- I think it would be more natural to add this feature to `NestedClassMetaclass` rather than to `ClasscallMetaclass`\n- It took me half an hour to fully understand what's happening. In particular the doc is wrong in saying that \n\n```\nThis method implements a binding behavior for ``foo.cls`` by delegating it to ``cls.__classget__(foo)``\n```\n\nindeed ``cls.__classget__(foo, Foo)`` is called. Can you confirm this ? \n\nFlorent",
    "created_at": "2010-02-12T19:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72977",
    "user": "hivert"
}
```

Hi Nicolas,

They are a few problem with this patch:
- it seems that line 119-125 (in the file) does not belongs to there ! They are after a return. Are they a bad copy paste ?
- I think it would be more natural to add this feature to `NestedClassMetaclass` rather than to `ClasscallMetaclass`
- It took me half an hour to fully understand what's happening. In particular the doc is wrong in saying that 

```
This method implements a binding behavior for ``foo.cls`` by delegating it to ``cls.__classget__(foo)``
```

indeed ``cls.__classget__(foo, Foo)`` is called. Can you confirm this ? 

Florent



---

archive/issue_comments_072978.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-12T19:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72978",
    "user": "hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072979.json:
```json
{
    "body": "Replying to [comment:3 hivert]:\n> Hi Nicolas,\n> \n> They are a few problem with this patch:\n>  - it seems that line 119-125 (in the file) does not belongs to there ! They are after a return. Are they a bad copy paste ?\n\nThanks for spotting this; that could explain some trouble I was having right now :-)\n\n>  - I think it would be more natural to add this feature to `NestedClassMetaclass` rather than to `ClasscallMetaclass`\n\nLet's discuss this over the phone.\n\n>  - It took me half an hour to fully understand what's happening. In particular the doc is wrong in saying that \n> {{{\n> This method implements a binding behavior for ``foo.cls`` by delegating it to ``cls.__classget__(foo)``\n> }}}\n> indeed ``cls.__classget__(foo, Foo)`` is called. Can you confirm this ? \n\nOops right. It calls __classget__ as per the descriptor protocol (which includes a 3rd argument).\n\nPlease let me know if you already made a patch on top on this one in the queue.",
    "created_at": "2010-02-12T21:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72979",
    "user": "nthiery"
}
```

Replying to [comment:3 hivert]:
> Hi Nicolas,
> 
> They are a few problem with this patch:
>  - it seems that line 119-125 (in the file) does not belongs to there ! They are after a return. Are they a bad copy paste ?

Thanks for spotting this; that could explain some trouble I was having right now :-)

>  - I think it would be more natural to add this feature to `NestedClassMetaclass` rather than to `ClasscallMetaclass`

Let's discuss this over the phone.

>  - It took me half an hour to fully understand what's happening. In particular the doc is wrong in saying that 
> {{{
> This method implements a binding behavior for ``foo.cls`` by delegating it to ``cls.__classget__(foo)``
> }}}
> indeed ``cls.__classget__(foo, Foo)`` is called. Can you confirm this ? 

Oops right. It calls __classget__ as per the descriptor protocol (which includes a 3rd argument).

Please let me know if you already made a patch on top on this one in the queue.



---

archive/issue_comments_072980.json:
```json
{
    "body": "Replying to [comment:5 nthiery]:\n> >  - I think it would be more natural to add this feature to `NestedClassMetaclass` rather than to `ClasscallMetaclass`\n> \n> Let's discuss this over the phone.\n\nOk.\n\n> Please let me know if you already made a patch on top on this one in the queue.\n\nplease see `trac_8250-classcall-classget-review-fh.patch` in combinat's queue. I'll upload it there as soon as we decided to move to `NestedClassMetaclass` or not.",
    "created_at": "2010-02-13T09:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72980",
    "user": "hivert"
}
```

Replying to [comment:5 nthiery]:
> >  - I think it would be more natural to add this feature to `NestedClassMetaclass` rather than to `ClasscallMetaclass`
> 
> Let's discuss this over the phone.

Ok.

> Please let me know if you already made a patch on top on this one in the queue.

please see `trac_8250-classcall-classget-review-fh.patch` in combinat's queue. I'll upload it there as soon as we decided to move to `NestedClassMetaclass` or not.



---

archive/issue_comments_072981.json:
```json
{
    "body": "Attachment [trac_8250-classcall-classget.patch](tarball://root/attachments/some-uuid/ticket8250/trac_8250-classcall-classget.patch) by nthiery created at 2010-02-13 12:34:31\n\nDocumentation improvements after phone discussion with Florent",
    "created_at": "2010-02-13T12:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72981",
    "user": "nthiery"
}
```

Attachment [trac_8250-classcall-classget.patch](tarball://root/attachments/some-uuid/ticket8250/trac_8250-classcall-classget.patch) by nthiery created at 2010-02-13 12:34:31

Documentation improvements after phone discussion with Florent



---

archive/issue_comments_072982.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-13T12:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72982",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072983.json:
```json
{
    "body": "There were still a few problems with the documentation:\n- references to methods `__classget__` and `__classcall__` instead of `__get__` and `__call__`; \n- Missing title for the file;\n- Missing use of `NestedClassMetaclass` in the outer class resulting in non standard names for the class. Moreover, the example now demonstrate the correct usage.\n- I also added these two metaclasses to the reference manual. Nicolas: can you confirm that we want it ? \n\nI uploaded a review patch. Please review :-)",
    "created_at": "2010-02-13T14:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72983",
    "user": "hivert"
}
```

There were still a few problems with the documentation:
- references to methods `__classget__` and `__classcall__` instead of `__get__` and `__call__`; 
- Missing title for the file;
- Missing use of `NestedClassMetaclass` in the outer class resulting in non standard names for the class. Moreover, the example now demonstrate the correct usage.
- I also added these two metaclasses to the reference manual. Nicolas: can you confirm that we want it ? 

I uploaded a review patch. Please review :-)



---

archive/issue_comments_072984.json:
```json
{
    "body": "Attachment [trac_8250-classcall-classget-review-2.patch](tarball://root/attachments/some-uuid/ticket8250/trac_8250-classcall-classget-review-2.patch) by hivert created at 2010-02-13 15:39:18\n\nAs we spoke on the phone I added a comment and corrected a typo.\nReady for review. I'm ok with your patch and if you are ok with mine you can put positive review.",
    "created_at": "2010-02-13T15:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72984",
    "user": "hivert"
}
```

Attachment [trac_8250-classcall-classget-review-2.patch](tarball://root/attachments/some-uuid/ticket8250/trac_8250-classcall-classget-review-2.patch) by hivert created at 2010-02-13 15:39:18

As we spoke on the phone I added a comment and corrected a typo.
Ready for review. I'm ok with your patch and if you are ok with mine you can put positive review.



---

archive/issue_comments_072985.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-13T16:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72985",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072986.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-15T03:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72986",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_072987.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8250-classcall-classget.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8250/trac_8250-classcall-classget.patch)\n2. [trac_8250-classcall-classget-review-2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8250/trac_8250-classcall-classget-review-2.patch)",
    "created_at": "2010-02-15T03:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8250#issuecomment-72987",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_8250-classcall-classget.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8250/trac_8250-classcall-classget.patch)
2. [trac_8250-classcall-classget-review-2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8250/trac_8250-classcall-classget-review-2.patch)
