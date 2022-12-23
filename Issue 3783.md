# Issue 3783: cached_method could use some improvements

Issue created by migration from https://trac.sagemath.org/ticket/3783

Original creator: mhansen

Original creation time: 2008-08-06 23:31:20

Assignee: mhansen

CC:  ncalexan simonking

The cached_method decorator from #3781 could use some improvements:


```
<mhansen> Does anyone feel up for reviewing #3781 for me?
<ncalexan> I'll look at it, one moment.  I've wanted this for a while.
<mhansen> Awesome.  It doesn't work on C extension types though since they don't have a __dict__.  This could be done by storing the cache in the decorator object with a weakref though.
<ncalexan> The problem is much more complicated than this.
<ncalexan> Okay, there are other problems too, like un-hashable arguments will break it.
<mhansen> Yep
<ncalexan> And there is no way to clear the cache...
<ncalexan> And the tests don't actually demonstrate that the cache is workin.
<ncalexan> (One could touch the cache with an incorrect answer, then verify it is "correctly" returning that value)
<ncalexan> For what it is, though, it's fine.  It will hurt nothing -- shall I review positive?
<mhansen> If you could, that'd be great.  I do know it's limitations, but there are some big patches going in that depend on it.  I'll make a ticket with your comments for improvement.
```



---

Comment by SimonKing created at 2012-06-25 09:06:37

The description isn't very clear. What exactly is requested? What part of it isn't fixed yet?


---

Comment by mmezzarobba created at 2015-04-13 16:39:18

Have all the issues mentioned in the description been fixed?


---

Comment by mmezzarobba created at 2015-04-13 16:39:18

Changing status from new to needs_review.


---

Comment by SimonKing created at 2015-04-13 18:43:10

Replying to [comment:8 mmezzarobba]:
> Have all the issues mentioned in the description been fixed?

- It does work on C extension types, provided they inherit from `Parent`.
- If I am not mistaken, it is now possible to define a function that does some preprocessing on the key. Thus, unhashable arguments should be fine, but certainly not out of the box.
- There is a way to clear the cache. It is a method of the cached method.
- I think the tests do demonstrate that the cache is working.


---

Comment by vdelecroix created at 2015-04-24 21:21:58

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-04-26 01:45:39

Resolution: fixed
