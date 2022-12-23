# Issue 9804: save_session is completely broken in the notebook

Issue created by migration from https://trac.sagemath.org/ticket/9805

Original creator: was

Original creation time: 2010-08-26 03:09:59

Assignee: jason, was

Try

```
save_session('foo')
```

in the notebook.  Boom!

The problem is these lines in misc/session.pyx:

```
    if embedded():
        # Also save D to the data directory if we're using the notebook.
        save(D, '../../data/' + name)
```


When I rewrote the notebook I forgot to change this appropriately.  I'm not sure exactly what the right fix is, but it is to somehow replace '../../data/' by the data
directory (which is defined by the variable DATA in the notebook).


---

Attachment

[attachment:trac_9805.patch Example patch] is provided to inform user of the workaround. I don't see how to get the worksheet directory of the user automatically. The DATA variable seems inaccessible from session.pyx.


---

Comment by ppurka created at 2013-08-09 17:01:06

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-08-15 09:30:51

Actually, this is pretty nice.  It tells of a workaround that is not onerous and should be familiar to people using the notebook.  What do you think, in retrospect?


---

Comment by ppurka created at 2014-08-17 06:27:54

Replying to [comment:6 kcrisman]:
> Actually, this is pretty nice.  It tells of a workaround that is not onerous and should be familiar to people using the notebook.  What do you think, in retrospect?
I don't even remember why I tried to patch this. If you think it is useful, I can create the git branch.


---

Comment by kcrisman created at 2014-10-22 18:53:40

Interestingly, this works even if you _don't_ save the worksheet - the cells that one made new disappear, but the sobj still appears.  This works nicely.

In this one case I am not sure if a doctest is useful - can you think of a viable one?
----
New commits:


---

Comment by kcrisman created at 2014-11-13 19:26:08

I still can't think of one, since although we can test for the creation of the sobj (in fact, it is still created in the cell directory and could be saved!) and we can pretend to be in the notebook, there is no point in testing the message and we can't emulate the data directory without opening a notebook and so forth, not worth that.  In fact, `save_session(DATA)` and so forth works, but once again explicit is probably better than implicit...


---

Comment by kcrisman created at 2014-11-13 19:26:08

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-11-14 21:01:43

Resolution: fixed


---

Comment by kcrisman created at 2014-12-10 17:46:06

This issue is actually fixed (as opposed to being warned against) in #17482 - it turned out to be nearly trivial, as there is a symlink to `DATA` in every cell directory!
