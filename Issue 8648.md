# Issue 8648: Generic __call__ function for parents prevents empty input in constructor

Issue created by migration from https://trac.sagemath.org/ticket/8648

Original creator: aschilling

Original creation time: 2010-04-03 15:34:28

Assignee: robertwb

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



---

Comment by roed created at 2010-10-16 23:08:25

An alternate suggestion: in CrystalOfTableaux define


```

    def __call__(self, x=[], *args, **kwds):
        return Parent.__call__(self, x, *args, **kwds)

```



---

Comment by roed created at 2010-10-16 23:12:14

Oh, I see.  The issue is that the generic call is constructing a morphism from the parent of x, and so x can't be non-existent.  You may need to just completely override the generic `Parent.__call__`.


---

Comment by nthiery created at 2010-10-20 20:03:02

Hi David!

Thanks for your feedback!

Replying to [comment:2 roed]:
> Oh, I see.  The issue is that the generic call is constructing a morphism from the parent of x, and so x can't be non-existent.  You may need to just completely override the generic `Parent.__call__`.  

I'd rather not duplicate that rather technical code :-) And still we want to benefit from coercion ... 

Do you see an inconvenient to the first approach suggested?


---

Comment by mhansen created at 2010-10-20 20:06:11

I think the 


```
    def __call__(self, x=[], *args, **kwds):
        return Parent.__call__(self, x, *args, **kwds)
```


approach is probably the best.  I had to do this recently when converting some old code to use the new `Parent.__call__`.


---

Comment by roed created at 2010-10-20 21:11:19

My second comment was in error, and as Mike says, my first suggestion should work.


---

Comment by vbraun created at 2013-12-23 21:13:26

Isn't this a rather ugly workaround? How about we just default to `x=None` and if it is unchanged we call `_element_constructor_`?


---

Comment by mhansen created at 2013-12-27 13:47:04

I'm not sure why that's much different.  The whole point is that calling with no arguments should be the same as calling with the empty list.
