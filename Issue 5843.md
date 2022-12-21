# Issue 5843: race condition in cached_method (should not be shared between instances)

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-04-21 08:43:49

Assignee: mhansen

CC:  sage-combinat mhansen

Keywords: race condition, cached_method, cache

Consider the following class (simplified from a real life example, after 3 hours of heisenbug debugging):

```
class bla:
    def __init__(self, value):
        self.value = value
    #
    `@`cached_method
    def f(self, x):
        return self.value
```


The method f ignores its input, and should return self.value:

```
sage: x = bla(1)
sage: y = bla(2)
sage: x.f(None)
1
sage: y.f(None)
2
```


Then, y.f(x.f) should ignore the inner x.f and return 2. It does not:

```
sage: sage: y.f(x.f)
1
```


The reason is that x.f and y.f, and all other instances of bla share the same cached_method object.

```
sage: x.f is y.f
True
sage: x.f is x.__class__.f
True
```


and the _instance field is set to the latest instance for which this method has been queried:

```
sage: yf = y.f
sage: yf._instance is y
True
sage: x.f
Cached version of <function f at 0xb532d84>
sage: yf._instance is y
False
sage: yf._instance is x
True
```


Most of the time things work well, but there can be race conditions, as in the example above.

Nicolas and Florent


---

Comment by nthiery created at 2009-04-21 08:59:06

Possible correct implementation:
   cached_method could return a closure instead of function object. Upon assignment to the
   class, this closure would become just a usual unbound method, removing the need to handle
   by hand the instance binding.


---

Attachment


---

Comment by wjp created at 2010-01-18 23:52:39

Changing status from new to needs_review.


---

Comment by wjp created at 2010-01-18 23:52:39

I added a patch that returns a (newly created) `CachedMethodCaller` object from `CachedMethod.__get__` that stores the instance on which the `CachedMethod` was called.

Additionally this object has a `__get__` of its own that does the same to handle stored copies of `CachedMethodCaller`s, which is something that categories seem to do.

Using a function/closure would also handle the caching (and I added a comment in the patch on how to do it exactly), but you would lose the ability to call methods like `is_in_cache()` which are used in some places in sage.


---

Comment by timdumol created at 2010-01-20 11:00:45

Excellent patch (I couldn't figure out how to fix this, glad you did), but there doesn't seem to be a test for the main problem:


```
class bla:
    def __init__(self, value):
        self.value = value
    #
    `@`cached_method
    def f(self, x):
        return self.value
```


The method f ignores its input, and should return self.value:

```
sage: x = bla(1)
sage: y = bla(2)
sage: x.f(None)
1
sage: y.f(None)
2
```


Then, y.f(x.f) should ignore the inner x.f and return 2. It does not:

```
sage: sage: y.f(x.f)
1
```



---

Comment by timdumol created at 2010-01-20 11:00:45

Changing status from needs_review to needs_work.


---

Attachment

Good point. I replaced the doctest patch with one that adds a more direct test for this ticket.


---

Comment by wjp created at 2010-01-20 19:06:51

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-01-20 20:11:09

Nice. I'm giving this a positive review, but I've attached a little patch that transfers some of the documentation from the `__init__` method to the the class itself, and adds some more documentation. It would be great for you to review it.


---

Attachment

Adds a little bit more documentation to CachedMethod.


---

Attachment

Changes the doctest to use `print` instead of `sleep`


---

Comment by wjp created at 2010-01-20 21:58:56

Looks good. Thanks!


Patches to apply, in order:
5843_CachedMethodCaller.patch
5843_doctests.patch
trac_5843-doctests-ref.2.patch


---

Comment by wjp created at 2010-01-20 21:58:56

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-24 02:09:07

Resolution: fixed


---

Comment by mvngu created at 2010-01-24 02:09:07

Merged patches in this order:

 1. [5843_CachedMethodCaller.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5843/5843_CachedMethodCaller.patch)
 1. [5843_doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5843/5843_doctests.patch)
 1. [trac_5843-doctests-ref.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5843/trac_5843-doctests-ref.2.patch) --- timdumol: please remember to put your username in your patch. I have committed this patch in your name.


---

Comment by nthiery created at 2010-01-24 21:38:04

Willem, Tim: thanks so much for fixing this!


---

Comment by nthiery created at 2010-01-24 21:41:52

Btw: #383 plays similar trick. Maybe Sage (actually Python) should have a standard tool for method wrappers as there already is for functions (see functools.wrapper).
