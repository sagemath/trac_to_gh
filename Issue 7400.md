# Issue 7400: ElementWrapper does not copy the wrapped values when copied

archive/issues_007400.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nKeywords: copy, ElementWrapper\n\nBefore the patch\n\n```\nsage: o1 = ElementWrapper([1], parent=ZZ)\nsage: o2 = copy(o1)\nsage: o2.value[0] = 3; o2\n[3]\nsage: o1\n[3]\n```\n\nAfter the patch\n\n```\nsage: o1 = ElementWrapper([1], parent=ZZ)\nsage: o2 = copy(o1)\nsage: o2.value[0] = 3; o2\n[3]\nsage: o1\n[1]\n```\n\n\nCheers,\n\nFlorent\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7400\n\n",
    "created_at": "2009-11-06T09:52:42Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "ElementWrapper does not copy the wrapped values when copied",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7400",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  sage-combinat

Keywords: copy, ElementWrapper

Before the patch

```
sage: o1 = ElementWrapper([1], parent=ZZ)
sage: o2 = copy(o1)
sage: o2.value[0] = 3; o2
[3]
sage: o1
[3]
```

After the patch

```
sage: o1 = ElementWrapper([1], parent=ZZ)
sage: o2 = copy(o1)
sage: o2.value[0] = 3; o2
[3]
sage: o1
[1]
```


Cheers,

Florent


Issue created by migration from https://trac.sagemath.org/ticket/7400





---

archive/issue_comments_062104.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-06T10:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62104",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062105.json:
```json
{
    "body": "The solution I give here doesn't work correctly with inheritance... I'm reworking it. \n\nFlorent",
    "created_at": "2009-11-08T17:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62105",
    "user": "https://github.com/hivert"
}
```

The solution I give here doesn't work correctly with inheritance... I'm reworking it. 

Florent



---

archive/issue_comments_062106.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-08T17:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62106",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062107.json:
```json
{
    "body": "Attachment [trac_7400-element_wrapper_copy-fh.patch](tarball://root/attachments/some-uuid/ticket7400/trac_7400-element_wrapper_copy-fh.patch) by @hivert created at 2009-11-08 18:27:46",
    "created_at": "2009-11-08T18:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62107",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7400-element_wrapper_copy-fh.patch](tarball://root/attachments/some-uuid/ticket7400/trac_7400-element_wrapper_copy-fh.patch) by @hivert created at 2009-11-08 18:27:46



---

archive/issue_comments_062108.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-08T18:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62108",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062109.json:
```json
{
    "body": "The new version should do the job ! Please review.\n\nFlorent",
    "created_at": "2009-11-08T18:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62109",
    "user": "https://github.com/hivert"
}
```

The new version should do the job ! Please review.

Florent



---

archive/issue_comments_062110.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-24T12:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62110",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062111.json:
```json
{
    "body": "Replying to [comment:3 hivert]:\n> The new version should do the job ! Please review.\n> \n> Florent\n\nUp to two small comments below, this is looking good:\n\nThe implementation of copy can probably be simplified a bit by using \"super\":\n\n```\nsage: class bla(SageObject):\n....:     pass\n....: \nsage: x = bla(); x.a = []; y = copy(x)\nsage: id(x), id(y), id(x.a), id(y.a)\n(204820300, 205533580, 208011212, 208011212)\nsage: class bla(SageObject):\n   def __copy__(self):\n       res = copy(super(bla, self))\n       res.a = copy(self.a)\n       return res\n....: ....: ....: ....: ....: \nsage: x = bla(); x.a = []; y = copy(x)\nsage: id(x), id(y), id(x.a), id(y.a)\n(204866636, 204866156, 205535372, 204820300)\n```\n\n\nIn the ElementWrapperTester: __repr__ => _repr_",
    "created_at": "2009-11-24T12:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62111",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:3 hivert]:
> The new version should do the job ! Please review.
> 
> Florent

Up to two small comments below, this is looking good:

The implementation of copy can probably be simplified a bit by using "super":

```
sage: class bla(SageObject):
....:     pass
....: 
sage: x = bla(); x.a = []; y = copy(x)
sage: id(x), id(y), id(x.a), id(y.a)
(204820300, 205533580, 208011212, 208011212)
sage: class bla(SageObject):
   def __copy__(self):
       res = copy(super(bla, self))
       res.a = copy(self.a)
       return res
....: ....: ....: ....: ....: 
sage: x = bla(); x.a = []; y = copy(x)
sage: id(x), id(y), id(x.a), id(y.a)
(204866636, 204866156, 205535372, 204820300)
```


In the ElementWrapperTester: __repr__ => _repr_



---

archive/issue_comments_062112.json:
```json
{
    "body": "Replying to [comment:4 nthiery]:\n\n> Up to two small comments below, this is looking good:\n> \n> The implementation of copy can probably be simplified a bit by using \"super\":\n\nThis does not work if you inherits from `Element` rather than from `SageObject`. I consider this as a bug in `Element` but I'm not sure. I'm waiting for answer on  [sage-devel](http://groups.google.fr/group/sage-devel/browse_thread/thread/d13fab1cd0bf79bc)\n\n \n> In the ElementWrapperTester: __repr__ => _repr_\n\nI had to write `__repr__` because `ElementWrapper` also has `__repr__` fixed both...",
    "created_at": "2009-12-02T08:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62112",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:4 nthiery]:

> Up to two small comments below, this is looking good:
> 
> The implementation of copy can probably be simplified a bit by using "super":

This does not work if you inherits from `Element` rather than from `SageObject`. I consider this as a bug in `Element` but I'm not sure. I'm waiting for answer on  [sage-devel](http://groups.google.fr/group/sage-devel/browse_thread/thread/d13fab1cd0bf79bc)

 
> In the ElementWrapperTester: __repr__ => _repr_

I had to write `__repr__` because `ElementWrapper` also has `__repr__` fixed both...



---

archive/issue_comments_062113.json:
```json
{
    "body": "> This does not work if you inherits from `Element` rather than from `SageObject`. I consider this as a bug in `Element` but I'm not sure. I'm waiting for answer on  [sage-devel](http://groups.google.fr/group/sage-devel/browse_thread/thread/d13fab1cd0bf79bc)\n\nThere where no answer on sage devel so that I fixed Element.",
    "created_at": "2009-12-16T09:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62113",
    "user": "https://github.com/hivert"
}
```

> This does not work if you inherits from `Element` rather than from `SageObject`. I consider this as a bug in `Element` but I'm not sure. I'm waiting for answer on  [sage-devel](http://groups.google.fr/group/sage-devel/browse_thread/thread/d13fab1cd0bf79bc)

There where no answer on sage devel so that I fixed Element.



---

archive/issue_comments_062114.json:
```json
{
    "body": "I uploaded a new patch which is ready for review. Please apply only `trac_7400-element_copy_fh.patch`.\n\nFlorent",
    "created_at": "2009-12-16T09:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62114",
    "user": "https://github.com/hivert"
}
```

I uploaded a new patch which is ready for review. Please apply only `trac_7400-element_copy_fh.patch`.

Florent



---

archive/issue_comments_062115.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-16T09:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62115",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062116.json:
```json
{
    "body": "Replying to [comment:8 hivert]:\n> I uploaded a new patch which is ready for review. Please apply only `trac_7400-element_copy_fh.patch`.\n> \n> Florent\n\nIs there a reason not to use  `super(Element, self).__copy__()` in Element.__copy__?",
    "created_at": "2009-12-16T11:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62116",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:8 hivert]:
> I uploaded a new patch which is ready for review. Please apply only `trac_7400-element_copy_fh.patch`.
> 
> Florent

Is there a reason not to use  `super(Element, self).__copy__()` in Element.__copy__?



---

archive/issue_comments_062117.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-12-16T11:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62117",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_062118.json:
```json
{
    "body": "Replying to [comment:9 nthiery]:\n> Replying to [comment:8 hivert]:\n> > I uploaded a new patch which is ready for review. Please apply only `trac_7400-element_copy_fh.patch`.\n> > \n> > Florent\n> \n> Is there a reason not to use  `super(Element, self).__copy__()` in Element.__copy__?\n\nA very good one:\n\n```\n   AttributeError: 'super' object has no attribute '__copy__'\n```\n\n\nFlorent",
    "created_at": "2009-12-16T12:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62118",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:9 nthiery]:
> Replying to [comment:8 hivert]:
> > I uploaded a new patch which is ready for review. Please apply only `trac_7400-element_copy_fh.patch`.
> > 
> > Florent
> 
> Is there a reason not to use  `super(Element, self).__copy__()` in Element.__copy__?

A very good one:

```
   AttributeError: 'super' object has no attribute '__copy__'
```


Florent



---

archive/issue_comments_062119.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-12-16T12:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62119",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_062120.json:
```json
{
    "body": "> > Is there a reason not to use  `super(Element, self).__copy__()` in Element.__copy__?\n> A very good one:\n> {{{\n>    AttributeError: 'super' object has no attribute '__copy__'\n> }}}\n\n:-)\n\nOops, I meant:  copy(super(Element, self)). Btw: does copy(super(Element,self)) work for ElementWrapper? I think I vaguely prefer it if it works.",
    "created_at": "2009-12-16T17:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62120",
    "user": "https://github.com/nthiery"
}
```

> > Is there a reason not to use  `super(Element, self).__copy__()` in Element.__copy__?
> A very good one:
> {{{
>    AttributeError: 'super' object has no attribute '__copy__'
> }}}

:-)

Oops, I meant:  copy(super(Element, self)). Btw: does copy(super(Element,self)) work for ElementWrapper? I think I vaguely prefer it if it works.



---

archive/issue_comments_062121.json:
```json
{
    "body": "Replying to [comment:12 nthiery]:\n> > > Is there a reason not to use  `super(Element, self).__copy__()` in Element.__copy__?\n> > A very good one:\n> > {{{\n> >    AttributeError: 'super' object has no attribute '__copy__'\n> > }}}\n> \n> :-)\n> \n> Oops, I meant:  copy(super(Element, self)). Btw: does copy(super(Element,self)) work for ElementWrapper? I think I vaguely prefer it if it works.\n\nIf you look at the way copy works, you'll realize that there is no chance that this works... And indeed:\n\n```\nFile \"/usr/local/sage/sage-4.2/devel/sage-combinat/sage/structure/element.pyx\", line 322:\n    sage: blo.__dict__ is bla.__dict__\nExpected:\n    False\nGot:\n    True\n```\n\n\nAny more suggestion you don't want to try by yourself ;-)",
    "created_at": "2009-12-17T06:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62121",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:12 nthiery]:
> > > Is there a reason not to use  `super(Element, self).__copy__()` in Element.__copy__?
> > A very good one:
> > {{{
> >    AttributeError: 'super' object has no attribute '__copy__'
> > }}}
> 
> :-)
> 
> Oops, I meant:  copy(super(Element, self)). Btw: does copy(super(Element,self)) work for ElementWrapper? I think I vaguely prefer it if it works.

If you look at the way copy works, you'll realize that there is no chance that this works... And indeed:

```
File "/usr/local/sage/sage-4.2/devel/sage-combinat/sage/structure/element.pyx", line 322:
    sage: blo.__dict__ is bla.__dict__
Expected:
    False
Got:
    True
```


Any more suggestion you don't want to try by yourself ;-)



---

archive/issue_comments_062122.json:
```json
{
    "body": "I just uploaded a hopefully final version...",
    "created_at": "2009-12-17T21:49:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62122",
    "user": "https://github.com/hivert"
}
```

I just uploaded a hopefully final version...



---

archive/issue_comments_062123.json:
```json
{
    "body": "I am happy with the patch.\n\nI just did some minor editing of the doc on the Sage-Combinat patch server. Please double check, and/or adapt, and then you can set a positive review.",
    "created_at": "2009-12-18T22:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62123",
    "user": "https://github.com/nthiery"
}
```

I am happy with the patch.

I just did some minor editing of the doc on the Sage-Combinat patch server. Please double check, and/or adapt, and then you can set a positive review.



---

archive/issue_comments_062124.json:
```json
{
    "body": "Attachment [trac_7400-element_copy_fh.patch](tarball://root/attachments/some-uuid/ticket7400/trac_7400-element_copy_fh.patch) by @hivert created at 2009-12-19 00:32:16",
    "created_at": "2009-12-19T00:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62124",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7400-element_copy_fh.patch](tarball://root/attachments/some-uuid/ticket7400/trac_7400-element_copy_fh.patch) by @hivert created at 2009-12-19 00:32:16



---

archive/issue_comments_062125.json:
```json
{
    "body": "Replying to [comment:15 nthiery]:\n> I am happy with the patch.\n> \n> I just did some minor editing of the doc on the Sage-Combinat patch server. Please double check, and/or adapt, and then you can set a positive review.\n\nYour changes left a typo which prevented the doctests to pass (a remaining `bla`) and some lines in the doc was to long... I corrected the patch, but as a punishment for leaving this, you have to re-review the patch :-)",
    "created_at": "2009-12-19T00:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62125",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:15 nthiery]:
> I am happy with the patch.
> 
> I just did some minor editing of the doc on the Sage-Combinat patch server. Please double check, and/or adapt, and then you can set a positive review.

Your changes left a typo which prevented the doctests to pass (a remaining `bla`) and some lines in the doc was to long... I corrected the patch, but as a punishment for leaving this, you have to re-review the patch :-)



---

archive/issue_comments_062126.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-19T00:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62126",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007623.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-12-19T20:57:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7400#event-7623"
}
```



---

archive/issue_comments_062127.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T20:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7400",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7400#issuecomment-62127",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
