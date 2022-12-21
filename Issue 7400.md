# Issue 7400: ElementWrapper does not copy the wrapped values when copied

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-11-06 09:52:42

Assignee: hivert

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



---

Comment by hivert created at 2009-11-06 10:02:03

Changing status from new to needs_review.


---

Comment by hivert created at 2009-11-08 17:00:58

The solution I give here doesn't work correctly with inheritance... I'm reworking it. 

Florent


---

Comment by hivert created at 2009-11-08 17:00:58

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by hivert created at 2009-11-08 18:29:20

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2009-11-08 18:29:20

The new version should do the job ! Please review.

Florent


---

Comment by nthiery created at 2009-11-24 12:49:32

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2009-11-24 12:49:32

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

Comment by hivert created at 2009-12-02 08:53:55

Replying to [comment:4 nthiery]:

> Up to two small comments below, this is looking good:
> 
> The implementation of copy can probably be simplified a bit by using "super":

This does not work if you inherits from `Element` rather than from `SageObject`. I consider this as a bug in `Element` but I'm not sure. I'm waiting for answer on  [sage-devel](http://groups.google.fr/group/sage-devel/browse_thread/thread/d13fab1cd0bf79bc)

 
> In the ElementWrapperTester: __repr__ => _repr_

I had to write `__repr__` because `ElementWrapper` also has `__repr__` fixed both...


---

Comment by hivert created at 2009-12-16 09:13:59

> This does not work if you inherits from `Element` rather than from `SageObject`. I consider this as a bug in `Element` but I'm not sure. I'm waiting for answer on  [sage-devel](http://groups.google.fr/group/sage-devel/browse_thread/thread/d13fab1cd0bf79bc)

There where no answer on sage devel so that I fixed Element.


---

Comment by hivert created at 2009-12-16 09:15:48

I uploaded a new patch which is ready for review. Please apply only `trac_7400-element_copy_fh.patch`.

Florent


---

Comment by hivert created at 2009-12-16 09:15:48

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2009-12-16 11:45:24

Replying to [comment:8 hivert]:
> I uploaded a new patch which is ready for review. Please apply only `trac_7400-element_copy_fh.patch`.
> 
> Florent

Is there a reason not to use  `super(Element, self).__copy__()` in Element.__copy__?


---

Comment by nthiery created at 2009-12-16 11:45:24

Changing status from needs_review to needs_info.


---

Comment by hivert created at 2009-12-16 12:49:42

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

Comment by hivert created at 2009-12-16 12:49:59

Changing status from needs_info to needs_review.


---

Comment by nthiery created at 2009-12-16 17:30:57

> > Is there a reason not to use  `super(Element, self).__copy__()` in Element.__copy__?
> A very good one:
> {{{
>    AttributeError: 'super' object has no attribute '__copy__'
> }}}

:-)

Oops, I meant:  copy(super(Element, self)). Btw: does copy(super(Element,self)) work for ElementWrapper? I think I vaguely prefer it if it works.


---

Comment by hivert created at 2009-12-17 06:18:10

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

Comment by hivert created at 2009-12-17 21:49:48

I just uploaded a hopefully final version...


---

Comment by nthiery created at 2009-12-18 22:03:15

I am happy with the patch.

I just did some minor editing of the doc on the Sage-Combinat patch server. Please double check, and/or adapt, and then you can set a positive review.


---

Attachment


---

Comment by hivert created at 2009-12-19 00:36:53

Replying to [comment:15 nthiery]:
> I am happy with the patch.
> 
> I just did some minor editing of the doc on the Sage-Combinat patch server. Please double check, and/or adapt, and then you can set a positive review.

Your changes left a typo which prevented the doctests to pass (a remaining `bla`) and some lines in the doc was to long... I corrected the patch, but as a punishment for leaving this, you have to re-review the patch :-)


---

Comment by nthiery created at 2009-12-19 00:43:38

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 20:57:48

Resolution: fixed
