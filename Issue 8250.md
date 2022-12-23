# Issue 8250: Extend ClasscallMetaclass to allow for binding behavior

Issue created by migration from https://trac.sagemath.org/ticket/8250

Original creator: nthiery

Original creation time: 2010-02-12 15:12:34

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


---

Comment by hivert created at 2010-02-12 16:25:27

This is a check to see if CC to sage-combinat-commits is working.
Apologies for the trouble. 


Cheers,

Florent


---

Comment by nthiery created at 2010-02-12 16:26:22

Changing status from new to needs_review.


---

Comment by hivert created at 2010-02-12 19:10:09

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

Comment by hivert created at 2010-02-12 19:18:04

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2010-02-12 21:38:51

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

Comment by hivert created at 2010-02-13 09:38:11

Replying to [comment:5 nthiery]:
> >  - I think it would be more natural to add this feature to `NestedClassMetaclass` rather than to `ClasscallMetaclass`
> 
> Let's discuss this over the phone.

Ok.

> Please let me know if you already made a patch on top on this one in the queue.

please see `trac_8250-classcall-classget-review-fh.patch` in combinat's queue. I'll upload it there as soon as we decided to move to `NestedClassMetaclass` or not.


---

Attachment

Documentation improvements after phone discussion with Florent


---

Comment by nthiery created at 2010-02-13 12:34:42

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-02-13 14:01:14

There were still a few problems with the documentation:
 - references to methods `__classget__` and `__classcall__` instead of `__get__` and `__call__`; 
 - Missing title for the file;
 - Missing use of `NestedClassMetaclass` in the outer class resulting in non standard names for the class. Moreover, the example now demonstrate the correct usage.
 - I also added these two metaclasses to the reference manual. Nicolas: can you confirm that we want it ? 

I uploaded a review patch. Please review :-)


---

Attachment

As we spoke on the phone I added a comment and corrected a typo.
Ready for review. I'm ok with your patch and if you are ok with mine you can put positive review.


---

Comment by nthiery created at 2010-02-13 16:17:13

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-15 03:40:37

Resolution: fixed


---

Comment by mvngu created at 2010-02-15 03:40:37

Merged in this order:

 1. [trac_8250-classcall-classget.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8250/trac_8250-classcall-classget.patch)
 1. [trac_8250-classcall-classget-review-2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8250/trac_8250-classcall-classget-review-2.patch)
