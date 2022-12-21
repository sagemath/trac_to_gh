# Issue 5091: find_root should call fast_float

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-01-24 22:05:03

Assignee: burcin

CC:  jason


```
sage: f(x) = sin(x)-cos(x)
sage: g = f._fast_float_()

sage: timeit("find_root(f, 0, pi)")
625 loops, best of 3: 154 µs per loop

sage: timeit("find_root(g, 0, pi)")
625 loops, best of 3: 24 µs per loop
```


See also http://groups.google.com/group/sage-devel/browse_thread/thread/927319a4fa61ae3b/9fc80aa9c114e041


---

Comment by mabshoff created at 2009-02-06 23:00:05

3.4 is for ReST tickets only.

Cheers,

Michael


---

Comment by wcauchois created at 2009-07-29 16:10:22

Incorporating the time it takes to call fast_float, the speedup is not that radical:

```
sage: var('x')
x
sage: from sage.ext.fast_eval import fast_float
sage: timeit("find_root(sin(x)-cos(x), 0, pi)")
625 loops, best of 3: 441 µs per loop
sage: timeit("find_root(fast_float(sin(x)-cos(x), x), 0, pi)")
625 loops, best of 3: 393 µs per loop
```

Its better for clients to call fast_float themselves, if they're using find_root inside a loop.


---

Comment by jason created at 2010-01-17 09:15:17

There is a small speedup here, so why not call it?


---

Comment by robertwb created at 2010-01-17 10:08:09

The point is that there should be a big speedup--I'm going to try and track down why construction is so expensive.


---

Comment by rws created at 2016-12-07 08:28:00

Changing status from new to needs_review.


---

Comment by rws created at 2016-12-07 08:28:00

Actually the speedup is 13x here (Sage 7.5beta5) only if the fast float already exists.

```
sage: timeit("find_root(f, 0, pi)")
625 loops, best of 3: 131 µs per loop
sage: timeit("find_root(g, 0, pi)")
625 loops, best of 3: 10.2 µs per loop
sage: timeit("find_root(sin(x)-cos(x), 0, pi)")
625 loops, best of 3: 170 µs per loop
sage: timeit("find_root(fast_float(sin(x)-cos(x), x), 0, pi)")
625 loops, best of 3: 161 µs per loop

sage: timeit('_ = sin(x)-cos(x)')
625 loops, best of 3: 9.3 µs per loop
sage: timeit("_ = fast_float(sin(x)-cos(x), x)")
625 loops, best of 3: 140 µs per loop
```

The creation of `sin(x)-cos(x)` takes 10µs, `find_root` of a fast float takes also 10µs. What is slow is creation of the fast float (130µs) and `find_root` of the normal expression (120µs). So there is no gain converting to fast float because conversion eats it all.

Therefore I propose to close this ticket.


---

Comment by kcrisman created at 2017-07-11 14:55:34

Sounds reasonable to me.  Nice hunting.


---

Comment by chapoton created at 2017-12-05 14:40:24

Changing status from needs_review to positive_review.


---

Comment by embray created at 2017-12-12 08:23:33

Resolution: wontfix
