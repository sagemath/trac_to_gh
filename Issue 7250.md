# Issue 7250: cached_function broken for builtin functions

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-10-19 21:43:40

Assignee: cwitty

CC:  craigcitro boothby rlm

Keywords: cached function

This used to work before #6937:

```
    sage: f = cached_function(sage.structure.element.is_RingElement)
    sage: f(1)
    True
```


That's used at one spot in the category code (but we can disable it temporarily)


---

Comment by nbruin created at 2013-01-09 21:03:02

On 5.6b1 I get

```
sage: f = cached_function(sage.structure.element.is_RingElement)
sage: f(1)
True
sage: f(False)
False
sage: f(True)
True
sage: f(x)
True
sage: f(0)
False
sage: f.get_cache()
{((1,), ()): True, ((x,), ()): True, ((False,), ()): False}
```

so it seems to work well enough now. Of course, `f(0)` and `f(True)` give funny answers because this the computed value is not a function on equality classes of the inputs (i.e., `0==False` and `1==True`, but `is_RingElement` doesn't have the same value on them).

The documentation of `cached_function` could do a better job of pointing out this gotcha (it mentions arguments should be hashable, but not that different but equal arguments will trigger cache use).

Anyway, I guess this ticket can be closed or be used to improve the documentation.


---

Comment by mhansen created at 2013-07-23 15:41:21

I would say that it can be closed.


---

Comment by mhansen created at 2013-07-23 15:41:21

Resolution: invalid
