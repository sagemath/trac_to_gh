# Issue 8611: speed up cached_function and cached_method

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-03-26 03:48:06

Assignee: tbd

CC:  novoselt was

There are a number of inefficiencies in the critical path (i.e., the code path when values have already been cached) that are addressed in this patch.


---

Attachment

BEFORE PATCH:


```
sage: def g(i=15):
...       return sum(range(2**i))
...
sage: `@`cached_function
sage: def cached_g(i=15):
...       return sum(range(2**i))
...
sage: class A:
...       `@`cached_method
...       def decorator_cache(self, i=15):
...           return sum(range(2**i))
...       def fast_cache(self, i=15):
...           try:
...               return self._fast_cache
...           except AttributeError:
...               self._fast_cache=sum(range(2**i))
...               return self._fast_cache
sage: timeit('g()')
125 loops, best of 3: 2.02 ms per loop
sage: timeit('cached_g()')
625 loops, best of 3: 37.9 µs per loop
sage: timeit('cached_g()')
625 loops, best of 3: 41.8 µs per loop
sage: c=A()
sage: timeit('c.decorator_cache()')
625 loops, best of 3: 64.8 µs per loop
sage: timeit('c.fast_cache()')
625 loops, best of 3: 1.06 µs per loop
```



AFTER PATCH


```

sage: def g(i=15):
...       return sum(range(2**i))
...
sage: `@`cached_function
sage: def cached_g(i=15):
...       return sum(range(2**i))
...
sage: class A:
...       `@`cached_method
...       def decorator_cache(self, i=15):
...           return sum(range(2**i))
...       def fast_cache(self, i=15):
...           try:
...               return self._fast_cache
...           except AttributeError:
...               self._fast_cache=sum(range(2**i))
...               return self._fast_cache
sage: timeit('g()')
125 loops, best of 3: 2.94 ms per loop
sage: timeit('cached_g()')
625 loops, best of 3: 1.64 µs per loop
sage: c=A()
sage: timeit('c.decorator_cache()')
625 loops, best of 3: 22 µs per loop
sage: timeit('c.fast_cache()')
625 loops, best of 3: 678 ns per loop
```



---

Comment by jason created at 2010-03-26 03:57:47

A few doctests don't pass, including one troubling one that seems to indicate that `@`cached_method isn't computing the right values in a simple case.  In the cases in the timings above, the right values are calculated.


---

Comment by davidloeffler created at 2010-03-26 16:36:10

Might it not be better for `@`cached_method to store its cache as an attribute of the instance object, rather than having a single cache which stores the values for all instances of that class?

E.g. the following code works for methods with no arguments:


```
def fast_cached_method(func):
    def fast_func(some_instance):
        try:
            return getattr(some_instance, '_cache_' + func.__name__)
        except AttributeError:
            result = func(some_instance)
            foo_instance.__dict__['_cache_' + func.__name__] = result
            return result
    return fast_func
```


I tested this and it's only about 1.5 times slower than doing the caching "by hand", while your speeded-up version above is still about 40 times slower.

David


---

Comment by SimonKing created at 2011-01-07 14:00:30

Changing status from new to needs_work.


---

Comment by SimonKing created at 2011-01-07 14:00:30

I just noticed that the patch does not apply anymore. I am trying to work on cached_function and cached_method anyway, so, I hope that I can soon submit a new patch.


---

Comment by SimonKing created at 2011-01-09 09:52:26

Hi Jason,

Note also that your patch would break the cache in the case of default/named arguments. Namely, when you have a function `def f(n=3): return n^2` then the values of `f()`, `f(3)` and `f(n=3)` should be identical, but they aren't when you have a special case for `f()`.

The patch that I am now preparing is quite thorough, attacking several spots that created overhead. It can now nearly compete with manual caching. I am currently adding more doctests and hope that I will be able to provide a patch later today.

Best regards,

Simon


---

Comment by SimonKing created at 2011-01-09 20:55:20

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-01-09 20:55:20

Replying to [comment:4 davidloeffler]:
> Might it not be better for `@`cached_method to store its cache as an attribute of the instance object, rather than having a single cache which stores the values for all instances of that class?

It was not the case that there was a single cache for all instances (the cache was in the instance for `cached_method` resp. in the parent of the instance for `cached_in_parent_method`). However, a part of the overhead came from the fact that the cached method _itself_ has not been an attribute of the instance but of its class.

I just attached a new patch that goes far beyond Jason's approach.

These examples show how the cached method performance is
improved by my patch:

*__Using instance attributes__*

Polynomial ideals have a cached method `groebner_basis`. Without
my patch, asking for `I.groebner_basis` would return a
`CachedMethodCaller` - always a _new instance_ whenever the cached
method is requested. Of course, that's a waste of time. Therefore,
I store the cached method caller as an attribute of the instance,
which is done when the attribute is first requested:


```
sage: R.<x, y, z> = PolynomialRing(QQ, 3)
sage: I = R*(x^3 + y^3 + z^3,x^4-y^4)
sage: I.__dict__.has_key('groebner_basis')
False
sage: I.groebner_basis
Cached version of <function groebner_basis at 0x15a0668>
sage: I.__dict__['groebner_basis']
Cached version of <function groebner_basis at 0x15a0668>
sage: I.groebner_basis is I.groebner_basis # False without my patch
True
```


This already yields a considerable speedup. However, pickling posed
a problem: Since the cached method caller is in the instance's
dictionary, it would be attempted to pickle it when the instance is
pickled. But functions can not be pickled.

The solution is "creative" (I hope you don't find it crazy - at least
it works!):

 * `CachedMethodCaller` has a `__reduce__` method, that
   creates a pickle - but when unpickling it, something else is created,
   namely an instance of the new class `CachedMethodPickle`. It only knows
   the name of the original cached method, and it knows the instance to
   which it belongs.

 * Now, after unpickling, one wants to work with the cached method.
   Working means: Requesting attributes (like `__call__`). `CachedMethodPickle`
   has a `__getattr__` method, which first removes the entry of the
   instance's dictionary pointing to it; so, it effectively commits suicide.

 * Since the `CachedMethodPickle` has been removed, the original cached
   method is again available from the class of the instance.

Here is an example:

```
sage: I.groebner_basis()
[y^5*z^3 - 1/4*x^2*z^6 + 1/2*x*y*z^6 + 1/4*y^2*z^6, x^2*y*z^3 - x*y^2*z^3 + 2*y^3*z^3 + z^6, x*y^3 + y^4 + x*z^3, x^3 + y^3 + z^3]
```

We now pickle and unpickle the ideal. The cached method
`groebner_basis` is replaced by a placeholder::

```
sage: J = loads(dumps(I))
sage: J.groebner_basis
Pickle of the cached method "groebner_basis"
```


But as soon as any other attribute is requested from the
placeholder, it replaces itself by the cached method, and
the entries of the cache are actually preserved::

```
sage: J.groebner_basis.is_in_cache()
True
sage: J.groebner_basis
Cached version of <function groebner_basis at 0x...>
sage: J.groebner_basis() == I.groebner_basis()
True
```


*__Creating the cache key__*

1. I found that most of the overhead comes from the computation
of the cache key. It relies on `sage.misc.function_mangling.ArgumentFixer`.
Internally, it works on lists and has some loops. So, I thought
it would benefit from Cython - and indeed it does!

Moreover, I made a shortpath in the method `fix_to_pos`: If there
are no named arguments then the result is essentially the list of
positional arguments plus the list of arguments with default value.

2. Some more cache key improvements take place inside `sage.misc.cachefunc`.
Originally, the key was obtained by a method `get_key`, which was then
calling `_get_instance_key`. In order to reduce the overhead of calling
two methods, I directly inserted the code of `_get_instance_key` and
removed that method.

3. I also use Jason's idea of creating a shortpath for the common case
of an empty argument list. However, if the argument list is empty,
there might still be arguments with a default value. But we want
that explicitly providing these default values yields the same cache
key - hence, the following would not work with Jason's patch (continuing
the example above):

```
sage: I.groebner_basis(algorithm='') is I.groebner_basis()
True
```


The solution is to compute the cache key for an empty argument list
_once_, and store the result for later. That's another reason why it
is good to have one `CachedMethodCaller` permanently attached to an
instance (rather than always creating a new one), since otherwise
caching of the default key would be difficult.

*__Accessing the cache__*

Originally, a method `get_cache` was used to get the cache dictionary.
In some cases, that method used to call another one, `_get_instance_cache`.
Hence, again, there was an overhead of calling two methods.

By my patch, the cache is _always_ available as an attribute of
the `CachedMethodCaller` instance - hence, access is superfast. There is
almost no memory problem, since it is simply a new pointer to a
dictionary that is an attribute of the instance (resp. of its parent):

```
sage: I.groebner_basis.cache is I._cache__groebner_basis
True
```


There is an additional benefit of this approach: If the instance has
no `__dict__` and does not accept an attribute to be set, it is still
possible to cache the method. Similarly, if the parent of the instance
does not accept attributes to be set, `cached_in_parent_method` would
still result in a cached method (but it would be cached in the instance,
not in its parent).

*__Documentation__*

I extended the documentation - but I did not cover `ClearCacheOnPickle`,
which my patch does not change. Apart from that, the doctest coverage
of `sage.misc.cachefunc` is complete. For `sage.misc.function_mangling`,
the coverage script complains "Please add a `TestSuite(s).run()` doctest."
I don't know were that comes from.

Of course, all doctests pass for me. I did not test whether the documentation
looks nice in html.

*__Performance__*

Last but not least, what the ticket is about: Performance!

Here is the setting:

```
sage: class Foo:
....:     def __init__(self,P=None):
....:         if P is None:
....:             self._parent=self
....:         else:
....:             self._parent=P
....:     `@`cached_method
....:     def bar(self,m,n=3):
....:         return m^n
....:     `@`cached_in_parent_method
....:     def barP(self,m,n=3):
....:         return m^n
....:     def parent(self):
....:         return self._parent
....:
sage: F = Foo()
sage: F_ZZ = Foo(ZZ)
```


__Without my patch__

```
# cache in F:
sage: F.bar(2,3) is F.bar(2) is F.bar(2,n=3) is F.bar(n=3,m=2)
True
sage: timeit('F.bar(2)', number=10000)
10000 loops, best of 3: 18 Âµs per loop
sage: timeit('F.bar(2,3)', number=10000)
10000 loops, best of 3: 18.2 Âµs per loop
sage: timeit('F.bar(2,n=3)', number=10000)
10000 loops, best of 3: 20.2 Âµs per loop
sage: timeit('F.bar(n=3,m=2)', number=10000)
10000 loops, best of 3: 20.2 Âµs per loop
```


```
# cache in F as a parent of itself:
sage: F.barP(2,3) is F.barP(2)  # BUG!
False
sage: F.barP.get_key(2,3)
((<__main__.Foo instance at 0x4570d88>, 2, 3), ())
sage: F.barP.get_key(2)
((<__main__.Foo instance at 0x4570d88>, 2), ())
sage: timeit('F.barP(2)', number=10000)
10000 loops, best of 3: 21.9 Âµs per loop
sage: timeit('F.barP(2,3)', number=10000)
10000 loops, best of 3: 22.4 Âµs per loop
sage: timeit('F.barP(2,n=3)', number=10000)
10000 loops, best of 3: 23.8 Âµs per loop
sage: timeit('F.barP(n=3,m=2)', number=10000)
10000 loops, best of 3: 24.5 Âµs per loop
```


```
# cache in ZZ, which does not allow attribute assignment
sage: F_ZZ.barP(2)
Traceback (most recent call last):
...
AttributeError: 'dictproxy' object has no attribute 'setdefault'
```


__With my patch__

```
# cache in F:
sage: F.bar(2,3) is F.bar(2) is F.bar(2,n=3) is F.bar(n=3,m=2)
True
sage: timeit('F.bar(2)', number=10000)
10000 loops, best of 3: 3.27 Âµs per loop
sage: timeit('F.bar(2,3)', number=10000)
10000 loops, best of 3: 3.26 Âµs per loop
sage: timeit('F.bar(2,n=3)', number=10000)
10000 loops, best of 3: 3.63 Âµs per loop
sage: timeit('F.bar(n=3,m=2)', number=10000)
10000 loops, best of 3: 3.69 Âµs per loop
```


```
# cache in F as parent of itself:
# The bug has disappeared
sage: F.barP(2,3) is F.barP(2) is F.barP(2,n=3) is F.barP(n=3,m=2)
True
sage: timeit('F.barP(2)', number=10000)
10000 loops, best of 3: 6.09 Âµs per loop
sage: timeit('F.barP(2,3)', number=10000)
10000 loops, best of 3: 5.5 Âµs per loop
sage: timeit('F.barP(2,n=3)', number=10000)
10000 loops, best of 3: 5.86 Âµs per loop
sage: timeit('F.barP(n=3,m=2)', number=10000)
10000 loops, best of 3: 6.03 Âµs per loop
```


```
# cache in ZZ, which does not allow attribute assignment.
# It works, since the cache is now automatically moved
# to F_ZZ, as a last resort
sage: F_ZZ.barP(2,3) is F_ZZ.barP(2) is F_ZZ.barP(2,n=3) is F_ZZ.barP(n=3,m=2)
True
sage: timeit('F_ZZ.barP(2)', number=10000)
10000 loops, best of 3: 5.6 Âµs per loop
sage: timeit('F_ZZ.barP(2,3)', number=10000)
10000 loops, best of 3: 5.56 Âµs per loop
sage: timeit('F_ZZ.barP(2,n=3)', number=10000)
10000 loops, best of 3: 5.86 Âµs per loop
sage: timeit('F_ZZ.barP(n=3,m=3)', number=10000)
10000 loops, best of 3: 6.1 Âµs per loop
```


Here is the effect of using a shortpath:

```
sage: class BAR:
....:     `@`cached_method
....:     def bar(self,m=2,n=3):
....:         return m^n
....:
sage: B = BAR()
sage: B.bar() is B.bar(2,3)
True
```


Without my patch:

```
sage: timeit('B.bar(n=2,m=3)', number=10000)
10000 loops, best of 3: 20.4 Âµs per loop
sage: timeit('B.bar()', number=10000)
10000 loops, best of 3: 17.1 Âµs per loop
```


With my patch:

```
sage: timeit('B.bar(n=2,m=3)', number=10000)
10000 loops, best of 3: 3.73 Âµs per loop
sage: timeit('B.bar()', number=10000)
10000 loops, best of 3: 1.95 Âµs per loop
```



---

Comment by SimonKing created at 2011-01-09 20:55:20

Changing keywords from "" to "cached method".


---

Comment by SimonKing created at 2011-01-09 20:56:37

For the patchbot:

Apply trac8611_cached_method_overhaul.patch


---

Comment by SimonKing created at 2011-01-09 21:28:48

I forgot to provide a comparison against an explicitly coded cache:

```
sage: class Foo:
....:     `@`cached_method
....:     def decorator_bar(self, n=15):
....:         return sum(range(2**n))
....:     def manual_bar(self, n=15):
....:         try:
....:             D = self._my_cache
....:         except AttributeError:
....:             D = self._my_cache = {}
....:             D[n] = sum(range(2**n))
....:         return D[n]
....:
sage: F = Foo()
sage: F.decorator_bar() is F.decorator_bar()
True
sage: F.decorator_bar() == F.manual_bar()
True
sage: F.manual_bar() is F.manual_bar()
True
sage: timeit('F.manual_bar()', number=10000)
10000 loops, best of 3: 1.02 Âµs per loop
sage: timeit('F.decorator_bar()', number=10000)
10000 loops, best of 3: 1.71 Âµs per loop
sage: timeit('F.decorator_bar(15)', number=10000)
10000 loops, best of 3: 3.05 Âµs per loop
```


Hence, the new version of cached methods can almost compete with an explicitly coded cache, but is of course much more comfortable for the programmer.


---

Comment by SimonKing created at 2011-01-10 07:07:57

I forgot to mention another bug fix (that is also doctested). It is about the comparison of representations of symmetric groups:

```
sage: spc = SymmetricGroupRepresentation([3])
sage: spc.important_info = 'Sage rules'
sage: spc == SymmetricGroupRepresentation([3]) # this used to return False!
True
```


The ticket description states that the improvements concern the _critical_ path (i.e., the value is already caught). Here is one more comparison, that also shows what happens in the non-critical path.

Setting:

```
sage: class A:
....:     `@`cached_method
....:     def bar(self,x):
....:         return x
....:     `@`cached_in_parent_method
....:     def barP(self,x):
....:         return x
....:     def parent(self):
....:         return self
....:     
sage: a = A()
```


Without my patch:

```
# The non-critical path:
sage: time for x in range(10^6): b=a.bar(x)
CPU times: user 24.97 s, sys: 0.16 s, total: 25.13 s
Wall time: 25.13 s
sage: time for x in range(10^6): b=a.barP(x)
CPU times: user 41.03 s, sys: 0.13 s, total: 41.16 s
Wall time: 41.17 s

# The critical path (now the values are cached):
sage: time for x in range(10^6): b=a.bar(x)
CPU times: user 16.45 s, sys: 0.02 s, total: 16.47 s
Wall time: 16.47 s
sage: time for x in range(10^6): b=a.barP(x)
CPU times: user 20.47 s, sys: 0.02 s, total: 20.50 s
Wall time: 20.50 s
```


With my patch:

```
# The non-critical path:
sage: time for x in range(10^6): b=a.bar(x)
CPU times: user 11.40 s, sys: 0.08 s, total: 11.48 s
Wall time: 11.48 s
sage: time for x in range(10^6): b=a.barP(x)
CPU times: user 27.89 s, sys: 0.12 s, total: 28.01 s
Wall time: 28.02 s

# The critical path (now the values are cached):
sage: time for x in range(10^6): b=a.bar(x)
CPU times: user 3.09 s, sys: 0.01 s, total: 3.10 s
Wall time: 3.10 s
sage: time for x in range(10^6): b=a.barP(x)
CPU times: user 5.25 s, sys: 0.02 s, total: 5.26 s
Wall time: 5.26 s
```


Hence, the patch improves all cases.


---

Comment by SimonKing created at 2011-01-10 09:51:38

In the patch version that I've just attached, I also inserted the documentation of `sage.misc.cachedfunc` and (after cleaning the documentation) of `sage.misc.function_mangling` into the reference manual. I think the documentation looks nice, but perhaps the referee can have a look on it as well.


---

Comment by SimonKing created at 2011-01-12 17:09:47

Improved performance for cached methods; add documentation to reference manual; cache is_subcateory. Replaces Jason's patch


---

Attachment

I slightly changed the patch. But the small change has in fact a big impact:

The method `sage.categories.category.Category.is_subcategory` is used to test whether something is an object of a given category. Due to the omnipresence of categories in Sage, this test occurs very often. So, it should be optimised!

I suggest that `is_subcategory` should be cached. I.e., the new patch version differs from the old one only in the line "`@`cached_method" in front of that method.

I believe that the additional memory consumption is affordable: When starting Sage, there are precisely 55 categories, so, in the worst case, caching `is_subcategory` adds 55 cache dictionaries with 55 entries.

The impact on the overall performance is obvious:
On my machine, `sage -tp 4 sage` takes 1721.2 seconds without my patch, but 1643.8 seconds with my patch.

Hence, the average improvement is about 4.5%.


---

Comment by davidloeffler created at 2011-01-16 16:03:07

Apply trac8611_cached_method_overhaul.patch

(for the patchbot)


---

Comment by SimonKing created at 2011-01-16 17:52:57

Replying to [comment:14 davidloeffler]:
> Apply trac8611_cached_method_overhaul.patch
> 
> (for the patchbot)

There already was such message for the patchbot.

But one question: On sage-devel, Robert Bradshaw reported that I need to rebase the patch. But the patchbot - at least in one attempt - succeeded. So, what is the status?

Unfortunately, I seriously screwed up my Sage installations. Currently, my two ol installations are broken, and sadly I was unablee to build either sage-4.6.1 or sage-4.6.2.alpha0/1.

Cheers,

Simon


---

Comment by davidloeffler created at 2011-01-16 20:27:38

Replying to [comment:15 SimonKing]:
> Replying to [comment:14 davidloeffler]:
> > Apply trac8611_cached_method_overhaul.patch
> > 
> > (for the patchbot)
> 
> There already was such message for the patchbot.

Patchbot's a bit pedantic about formatting of such messages. If you look at the records of the test runs it's done, you'll see that prior to today it was trying to apply both patches at once, and thus failing, and after I prodded it earlier, it did a new run which passed.

I've got a working 4.6.2.alpha0 build, so I can test it against that tomorrow morning.


---

Comment by davidloeffler created at 2011-01-17 11:30:55

Applies fine and passes doctests both using 4.6.2.alpha0 on my system, and using 4.6.1 with patchbot. I ran some tests and in the case of a method with no arguments it's something like 15 times faster than the old code and only a tiny bit slower than a hand-rolled cache. Code looks fine by eye, and it's great that you added these modules to the ref manual as well. Positive review.

I'm looking forward to using %prun in future sage versions and not finding that 20% of the execution time has been spent in "fix_to_pos", which is frequently the case at the moment...


---

Comment by davidloeffler created at 2011-01-17 11:30:55

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-23 13:34:55

Please use line breaks in the commit message if it is so long.  Make sure the first line is a short description of the patch with the ticket number.  Following lines can contain a longer description.


---

Comment by jdemeyer created at 2011-01-23 13:34:55

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2011-01-23 15:16:30

Apply only this patch


---

Attachment

Done.


---

Comment by davidloeffler created at 2011-01-23 15:17:01

Changing status from needs_work to positive_review.


---

Comment by SimonKing created at 2011-01-23 16:28:11

Replying to [comment:19 davidloeffler]:
> Done.

Thank you!


---

Comment by jdemeyer created at 2011-01-25 08:14:05

Resolution: fixed


---

Comment by nthiery created at 2011-01-28 10:34:01

For the record, a related thread:

 - http://groups.google.com/group/sage-devel/browse_thread/thread/6607a3919c619345
