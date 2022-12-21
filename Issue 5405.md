# Issue 5405: [with patch, needs review] create a decorator for adding default keyword arguments to a function

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-02-28 23:14:31

Assignee: cwitty

CC:  mhansen jason

The typical usage of this decorator would be to be applied above a
:obj:`cached_method` or :obj:`cached_function` decorator so that
the correct cached object is returned.


---

Attachment

Hi Mike!

I am not so sure about the name, although I can't propose much better than
default_values, or set_default_values.

Could it be generalized to handle both positional and non positional arguments?

I'd suggest to have the doc by starting with what the thing actually does, followed by the typical usage.
Speaking of which: could you add an example of this typical usage? (it was not clear to me).


---

Comment by nthiery created at 2009-04-13 23:28:53

Oops, should have set the subject to needs work. Done.


---

Comment by timdumol created at 2009-10-23 15:54:00

Sorry if I don't get this right, but doesn't functools.partial already fulfill this purpose?


---

Comment by jason created at 2009-10-23 17:22:01

Do you mean something like this?


```
from functools import partial

def partial_dec(*args, **kwds):
    def p(f):
        return partial(f,*args,**kwds)
    return p
    
`@`partial_dec(b=2)
def f(a,b):
    return 10*a+b

f(4)
```



---

Comment by timdumol created at 2009-10-23 21:10:17

Actually I meant something like this:


```
from functools import partial

`@`partial(partial, b=4)
def f(a,b):
    return 10*a + b

f(4)
```



---

Comment by jason created at 2009-10-23 21:14:44

Cute.  Very nice!


---

Comment by jason created at 2009-10-23 21:25:48

So now can you use `@`wraps or something so that g? works correctly below?


```
from functools import partial, wraps

`@`partial(partial, b=4)
def g(a,b):
    """Docs"""
    return 10*a + b

g?
```



---

Comment by timdumol created at 2009-10-23 21:51:35

This works, but it certainly isn't obvious:


```

from functools import partial, wraps

`@`partial(lambda x: wraps(x)(partial(partial, b = 4))(x))
def g(a,b):
    """Docs"""
    return 10*a + b

print(g(5))

g?
```



---

Comment by jason created at 2009-10-23 21:58:59

and at that point, I'd say 


```
`@`default_keywords...
def g...

```


is nicer.  However, one might use partial in the above decorator.  I think our discussion is evidence for the usefulness of the idea on this ticket.


---

Comment by timdumol created at 2009-10-23 22:02:56

Yep. It's certainly much clearer. Using `partial` should deal with the positional and non-positional arguments thing.


---

Comment by jason created at 2009-10-23 22:04:52

So we've agreed that we should create a `partial` decorator that allows something like:


```
from sage.misc.decorators (or wherever) import partial

`@`partial(*args, **kwds) # Same as calling partial(g, *args, **kwds) and wrapping with `@`wraps
def g(a,b):
   ...

```


just works as expected.


---

Comment by timdumol created at 2009-10-23 22:11:05

Perhaps a name of `curry` [1] would be better, since it prevents name collision with functools.partial? Then again, it supersedes functools.partial anyways.

[1] http://en.wikipedia.org/wiki/Currying


---

Comment by nthiery created at 2009-10-23 22:46:18

Thanks much for pointing out functools.partial and functool.wrapper; I have several other use cases for them!

Replying to [comment:14 timdumol]:
> Perhaps a name of `curry` [1] would be better, since it prevents name collision with functools.partial? Then again, it supersedes functools.partial anyways.
> 
> [1] http://en.wikipedia.org/wiki/Currying

I prefer partial, since curry does not really encompass the specialization of named arguments.
It's really functools.partial, but made into a decorator.


---

Comment by timdumol created at 2009-10-24 01:50:41

> I prefer partial, since curry does not really encompass the specialization of named arguments.
> It's really functools.partial, but made into a decorator.

Fair enough -- but just to clarify, `functools.partial` *is* a decorator, just that it doesn't update the documentation string.


---

Attachment

Adds module `sage.misc.decorators` with content `specialize`.


---

Comment by timdumol created at 2009-12-05 09:54:36

Nevermind, `functools.partial` is not a decorator. My apologies.

This patch should do the trick. I named it `specialize` rather than `partial`, since `partial` conflicts with `functools.partial`.


---

Comment by timdumol created at 2009-12-05 09:54:36

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-05-05 19:44:49

Looks good to me.


---

Comment by mhansen created at 2010-05-05 19:44:49

Changing status from needs_review to positive_review.


---

Attachment

same as previous but with username


---

Comment by mvngu created at 2010-05-08 04:07:29

The patch [trac_5405-decorator-partial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5405/trac_5405-decorator-partial.2.patch) is the same as Tim's patch, but with his username.


---

Comment by mvngu created at 2010-05-08 22:05:12

Resolution: fixed


---

Comment by mvngu created at 2010-05-08 22:05:12

Merged [trac_5405-decorator-partial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5405/trac_5405-decorator-partial.2.patch).
