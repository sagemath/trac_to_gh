# Issue 8611: speed up cached_function and cached_method

archive/issues_008611.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @novoselt @williamstein\n\nThere are a number of inefficiencies in the critical path (i.e., the code path when values have already been cached) that are addressed in this patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8611\n\n",
    "created_at": "2010-03-26T03:48:06Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "speed up cached_function and cached_method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8611",
    "user": "https://github.com/jasongrout"
}
```
Assignee: tbd

CC:  @novoselt @williamstein

There are a number of inefficiencies in the critical path (i.e., the code path when values have already been cached) that are addressed in this patch.

Issue created by migration from https://trac.sagemath.org/ticket/8611





---

archive/issue_comments_077878.json:
```json
{
    "body": "Attachment [trac-8611-speed-up-cached-decorators.patch](tarball://root/attachments/some-uuid/ticket8611/trac-8611-speed-up-cached-decorators.patch) by @jasongrout created at 2010-03-26 03:54:03\n\nBEFORE PATCH:\n\n\n```\nsage: def g(i=15):\n...       return sum(range(2**i))\n...\nsage: @cached_function\nsage: def cached_g(i=15):\n...       return sum(range(2**i))\n...\nsage: class A:\n...       @cached_method\n...       def decorator_cache(self, i=15):\n...           return sum(range(2**i))\n...       def fast_cache(self, i=15):\n...           try:\n...               return self._fast_cache\n...           except AttributeError:\n...               self._fast_cache=sum(range(2**i))\n...               return self._fast_cache\nsage: timeit('g()')\n125 loops, best of 3: 2.02 ms per loop\nsage: timeit('cached_g()')\n625 loops, best of 3: 37.9 \u00b5s per loop\nsage: timeit('cached_g()')\n625 loops, best of 3: 41.8 \u00b5s per loop\nsage: c=A()\nsage: timeit('c.decorator_cache()')\n625 loops, best of 3: 64.8 \u00b5s per loop\nsage: timeit('c.fast_cache()')\n625 loops, best of 3: 1.06 \u00b5s per loop\n```\n\n\n\nAFTER PATCH\n\n\n```\n\nsage: def g(i=15):\n...       return sum(range(2**i))\n...\nsage: @cached_function\nsage: def cached_g(i=15):\n...       return sum(range(2**i))\n...\nsage: class A:\n...       @cached_method\n...       def decorator_cache(self, i=15):\n...           return sum(range(2**i))\n...       def fast_cache(self, i=15):\n...           try:\n...               return self._fast_cache\n...           except AttributeError:\n...               self._fast_cache=sum(range(2**i))\n...               return self._fast_cache\nsage: timeit('g()')\n125 loops, best of 3: 2.94 ms per loop\nsage: timeit('cached_g()')\n625 loops, best of 3: 1.64 \u00b5s per loop\nsage: c=A()\nsage: timeit('c.decorator_cache()')\n625 loops, best of 3: 22 \u00b5s per loop\nsage: timeit('c.fast_cache()')\n625 loops, best of 3: 678 ns per loop\n```\n",
    "created_at": "2010-03-26T03:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77878",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8611-speed-up-cached-decorators.patch](tarball://root/attachments/some-uuid/ticket8611/trac-8611-speed-up-cached-decorators.patch) by @jasongrout created at 2010-03-26 03:54:03

BEFORE PATCH:


```
sage: def g(i=15):
...       return sum(range(2**i))
...
sage: @cached_function
sage: def cached_g(i=15):
...       return sum(range(2**i))
...
sage: class A:
...       @cached_method
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
sage: @cached_function
sage: def cached_g(i=15):
...       return sum(range(2**i))
...
sage: class A:
...       @cached_method
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

archive/issue_comments_077879.json:
```json
{
    "body": "A few doctests don't pass, including one troubling one that seems to indicate that `@`cached_method isn't computing the right values in a simple case.  In the cases in the timings above, the right values are calculated.",
    "created_at": "2010-03-26T03:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77879",
    "user": "https://github.com/jasongrout"
}
```

A few doctests don't pass, including one troubling one that seems to indicate that `@`cached_method isn't computing the right values in a simple case.  In the cases in the timings above, the right values are calculated.



---

archive/issue_comments_077880.json:
```json
{
    "body": "Might it not be better for `@`cached_method to store its cache as an attribute of the instance object, rather than having a single cache which stores the values for all instances of that class?\n\nE.g. the following code works for methods with no arguments:\n\n\n```\ndef fast_cached_method(func):\n    def fast_func(some_instance):\n        try:\n            return getattr(some_instance, '_cache_' + func.__name__)\n        except AttributeError:\n            result = func(some_instance)\n            foo_instance.__dict__['_cache_' + func.__name__] = result\n            return result\n    return fast_func\n```\n\n\nI tested this and it's only about 1.5 times slower than doing the caching \"by hand\", while your speeded-up version above is still about 40 times slower.\n\nDavid",
    "created_at": "2010-03-26T16:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77880",
    "user": "https://github.com/loefflerd"
}
```

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

archive/issue_comments_077881.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-01-07T14:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77881",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_077882.json:
```json
{
    "body": "I just noticed that the patch does not apply anymore. I am trying to work on cached_function and cached_method anyway, so, I hope that I can soon submit a new patch.",
    "created_at": "2011-01-07T14:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77882",
    "user": "https://github.com/simon-king-jena"
}
```

I just noticed that the patch does not apply anymore. I am trying to work on cached_function and cached_method anyway, so, I hope that I can soon submit a new patch.



---

archive/issue_comments_077883.json:
```json
{
    "body": "Hi Jason,\n\nNote also that your patch would break the cache in the case of default/named arguments. Namely, when you have a function `def f(n=3): return n^2` then the values of `f()`, `f(3)` and `f(n=3)` should be identical, but they aren't when you have a special case for `f()`.\n\nThe patch that I am now preparing is quite thorough, attacking several spots that created overhead. It can now nearly compete with manual caching. I am currently adding more doctests and hope that I will be able to provide a patch later today.\n\nBest regards,\n\nSimon",
    "created_at": "2011-01-09T09:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77883",
    "user": "https://github.com/simon-king-jena"
}
```

Hi Jason,

Note also that your patch would break the cache in the case of default/named arguments. Namely, when you have a function `def f(n=3): return n^2` then the values of `f()`, `f(3)` and `f(n=3)` should be identical, but they aren't when you have a special case for `f()`.

The patch that I am now preparing is quite thorough, attacking several spots that created overhead. It can now nearly compete with manual caching. I am currently adding more doctests and hope that I will be able to provide a patch later today.

Best regards,

Simon



---

archive/issue_comments_077884.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-09T20:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77884",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077885.json:
```json
{
    "body": "Replying to [comment:4 davidloeffler]:\n> Might it not be better for `@`cached_method to store its cache as an attribute of the instance object, rather than having a single cache which stores the values for all instances of that class?\n\nIt was not the case that there was a single cache for all instances (the cache was in the instance for `cached_method` resp. in the parent of the instance for `cached_in_parent_method`). However, a part of the overhead came from the fact that the cached method *itself* has not been an attribute of the instance but of its class.\n\nI just attached a new patch that goes far beyond Jason's approach.\n\nThese examples show how the cached method performance is\nimproved by my patch:\n\n**__Using instance attributes__**\n\nPolynomial ideals have a cached method `groebner_basis`. Without\nmy patch, asking for `I.groebner_basis` would return a\n`CachedMethodCaller` - always a *new instance* whenever the cached\nmethod is requested. Of course, that's a waste of time. Therefore,\nI store the cached method caller as an attribute of the instance,\nwhich is done when the attribute is first requested:\n\n\n```\nsage: R.<x, y, z> = PolynomialRing(QQ, 3)\nsage: I = R*(x^3 + y^3 + z^3,x^4-y^4)\nsage: I.__dict__.has_key('groebner_basis')\nFalse\nsage: I.groebner_basis\nCached version of <function groebner_basis at 0x15a0668>\nsage: I.__dict__['groebner_basis']\nCached version of <function groebner_basis at 0x15a0668>\nsage: I.groebner_basis is I.groebner_basis # False without my patch\nTrue\n```\n\n\nThis already yields a considerable speedup. However, pickling posed\na problem: Since the cached method caller is in the instance's\ndictionary, it would be attempted to pickle it when the instance is\npickled. But functions can not be pickled.\n\nThe solution is \"creative\" (I hope you don't find it crazy - at least\nit works!):\n\n* `CachedMethodCaller` has a `__reduce__` method, that\n  creates a pickle - but when unpickling it, something else is created,\n  namely an instance of the new class `CachedMethodPickle`. It only knows\n  the name of the original cached method, and it knows the instance to\n  which it belongs.\n\n* Now, after unpickling, one wants to work with the cached method.\n  Working means: Requesting attributes (like `__call__`). `CachedMethodPickle`\n  has a `__getattr__` method, which first removes the entry of the\n  instance's dictionary pointing to it; so, it effectively commits suicide.\n\n* Since the `CachedMethodPickle` has been removed, the original cached\n  method is again available from the class of the instance.\n\nHere is an example:\n\n```\nsage: I.groebner_basis()\n[y^5*z^3 - 1/4*x^2*z^6 + 1/2*x*y*z^6 + 1/4*y^2*z^6, x^2*y*z^3 - x*y^2*z^3 + 2*y^3*z^3 + z^6, x*y^3 + y^4 + x*z^3, x^3 + y^3 + z^3]\n```\n\nWe now pickle and unpickle the ideal. The cached method\n`groebner_basis` is replaced by a placeholder::\n\n```\nsage: J = loads(dumps(I))\nsage: J.groebner_basis\nPickle of the cached method \"groebner_basis\"\n```\n\n\nBut as soon as any other attribute is requested from the\nplaceholder, it replaces itself by the cached method, and\nthe entries of the cache are actually preserved::\n\n```\nsage: J.groebner_basis.is_in_cache()\nTrue\nsage: J.groebner_basis\nCached version of <function groebner_basis at 0x...>\nsage: J.groebner_basis() == I.groebner_basis()\nTrue\n```\n\n\n**__Creating the cache key__**\n\n1. I found that most of the overhead comes from the computation\nof the cache key. It relies on `sage.misc.function_mangling.ArgumentFixer`.\nInternally, it works on lists and has some loops. So, I thought\nit would benefit from Cython - and indeed it does!\n\nMoreover, I made a shortpath in the method `fix_to_pos`: If there\nare no named arguments then the result is essentially the list of\npositional arguments plus the list of arguments with default value.\n\n2. Some more cache key improvements take place inside `sage.misc.cachefunc`.\nOriginally, the key was obtained by a method `get_key`, which was then\ncalling `_get_instance_key`. In order to reduce the overhead of calling\ntwo methods, I directly inserted the code of `_get_instance_key` and\nremoved that method.\n\n3. I also use Jason's idea of creating a shortpath for the common case\nof an empty argument list. However, if the argument list is empty,\nthere might still be arguments with a default value. But we want\nthat explicitly providing these default values yields the same cache\nkey - hence, the following would not work with Jason's patch (continuing\nthe example above):\n\n```\nsage: I.groebner_basis(algorithm='') is I.groebner_basis()\nTrue\n```\n\n\nThe solution is to compute the cache key for an empty argument list\n*once*, and store the result for later. That's another reason why it\nis good to have one `CachedMethodCaller` permanently attached to an\ninstance (rather than always creating a new one), since otherwise\ncaching of the default key would be difficult.\n\n**__Accessing the cache__**\n\nOriginally, a method `get_cache` was used to get the cache dictionary.\nIn some cases, that method used to call another one, `_get_instance_cache`.\nHence, again, there was an overhead of calling two methods.\n\nBy my patch, the cache is *always* available as an attribute of\nthe `CachedMethodCaller` instance - hence, access is superfast. There is\nalmost no memory problem, since it is simply a new pointer to a\ndictionary that is an attribute of the instance (resp. of its parent):\n\n```\nsage: I.groebner_basis.cache is I._cache__groebner_basis\nTrue\n```\n\n\nThere is an additional benefit of this approach: If the instance has\nno `__dict__` and does not accept an attribute to be set, it is still\npossible to cache the method. Similarly, if the parent of the instance\ndoes not accept attributes to be set, `cached_in_parent_method` would\nstill result in a cached method (but it would be cached in the instance,\nnot in its parent).\n\n**__Documentation__**\n\nI extended the documentation - but I did not cover `ClearCacheOnPickle`,\nwhich my patch does not change. Apart from that, the doctest coverage\nof `sage.misc.cachefunc` is complete. For `sage.misc.function_mangling`,\nthe coverage script complains \"Please add a `TestSuite(s).run()` doctest.\"\nI don't know were that comes from.\n\nOf course, all doctests pass for me. I did not test whether the documentation\nlooks nice in html.\n\n**__Performance__**\n\nLast but not least, what the ticket is about: Performance!\n\nHere is the setting:\n\n```\nsage: class Foo:\n....:     def __init__(self,P=None):\n....:         if P is None:\n....:             self._parent=self\n....:         else:\n....:             self._parent=P\n....:     @cached_method\n....:     def bar(self,m,n=3):\n....:         return m^n\n....:     @cached_in_parent_method\n....:     def barP(self,m,n=3):\n....:         return m^n\n....:     def parent(self):\n....:         return self._parent\n....:\nsage: F = Foo()\nsage: F_ZZ = Foo(ZZ)\n```\n\n\n__Without my patch__\n\n```\n# cache in F:\nsage: F.bar(2,3) is F.bar(2) is F.bar(2,n=3) is F.bar(n=3,m=2)\nTrue\nsage: timeit('F.bar(2)', number=10000)\n10000 loops, best of 3: 18 \u00c2\u00b5s per loop\nsage: timeit('F.bar(2,3)', number=10000)\n10000 loops, best of 3: 18.2 \u00c2\u00b5s per loop\nsage: timeit('F.bar(2,n=3)', number=10000)\n10000 loops, best of 3: 20.2 \u00c2\u00b5s per loop\nsage: timeit('F.bar(n=3,m=2)', number=10000)\n10000 loops, best of 3: 20.2 \u00c2\u00b5s per loop\n```\n\n\n```\n# cache in F as a parent of itself:\nsage: F.barP(2,3) is F.barP(2)  # BUG!\nFalse\nsage: F.barP.get_key(2,3)\n((<__main__.Foo instance at 0x4570d88>, 2, 3), ())\nsage: F.barP.get_key(2)\n((<__main__.Foo instance at 0x4570d88>, 2), ())\nsage: timeit('F.barP(2)', number=10000)\n10000 loops, best of 3: 21.9 \u00c2\u00b5s per loop\nsage: timeit('F.barP(2,3)', number=10000)\n10000 loops, best of 3: 22.4 \u00c2\u00b5s per loop\nsage: timeit('F.barP(2,n=3)', number=10000)\n10000 loops, best of 3: 23.8 \u00c2\u00b5s per loop\nsage: timeit('F.barP(n=3,m=2)', number=10000)\n10000 loops, best of 3: 24.5 \u00c2\u00b5s per loop\n```\n\n\n```\n# cache in ZZ, which does not allow attribute assignment\nsage: F_ZZ.barP(2)\nTraceback (most recent call last):\n...\nAttributeError: 'dictproxy' object has no attribute 'setdefault'\n```\n\n\n__With my patch__\n\n```\n# cache in F:\nsage: F.bar(2,3) is F.bar(2) is F.bar(2,n=3) is F.bar(n=3,m=2)\nTrue\nsage: timeit('F.bar(2)', number=10000)\n10000 loops, best of 3: 3.27 \u00c2\u00b5s per loop\nsage: timeit('F.bar(2,3)', number=10000)\n10000 loops, best of 3: 3.26 \u00c2\u00b5s per loop\nsage: timeit('F.bar(2,n=3)', number=10000)\n10000 loops, best of 3: 3.63 \u00c2\u00b5s per loop\nsage: timeit('F.bar(n=3,m=2)', number=10000)\n10000 loops, best of 3: 3.69 \u00c2\u00b5s per loop\n```\n\n\n```\n# cache in F as parent of itself:\n# The bug has disappeared\nsage: F.barP(2,3) is F.barP(2) is F.barP(2,n=3) is F.barP(n=3,m=2)\nTrue\nsage: timeit('F.barP(2)', number=10000)\n10000 loops, best of 3: 6.09 \u00c2\u00b5s per loop\nsage: timeit('F.barP(2,3)', number=10000)\n10000 loops, best of 3: 5.5 \u00c2\u00b5s per loop\nsage: timeit('F.barP(2,n=3)', number=10000)\n10000 loops, best of 3: 5.86 \u00c2\u00b5s per loop\nsage: timeit('F.barP(n=3,m=2)', number=10000)\n10000 loops, best of 3: 6.03 \u00c2\u00b5s per loop\n```\n\n\n```\n# cache in ZZ, which does not allow attribute assignment.\n# It works, since the cache is now automatically moved\n# to F_ZZ, as a last resort\nsage: F_ZZ.barP(2,3) is F_ZZ.barP(2) is F_ZZ.barP(2,n=3) is F_ZZ.barP(n=3,m=2)\nTrue\nsage: timeit('F_ZZ.barP(2)', number=10000)\n10000 loops, best of 3: 5.6 \u00c2\u00b5s per loop\nsage: timeit('F_ZZ.barP(2,3)', number=10000)\n10000 loops, best of 3: 5.56 \u00c2\u00b5s per loop\nsage: timeit('F_ZZ.barP(2,n=3)', number=10000)\n10000 loops, best of 3: 5.86 \u00c2\u00b5s per loop\nsage: timeit('F_ZZ.barP(n=3,m=3)', number=10000)\n10000 loops, best of 3: 6.1 \u00c2\u00b5s per loop\n```\n\n\nHere is the effect of using a shortpath:\n\n```\nsage: class BAR:\n....:     @cached_method\n....:     def bar(self,m=2,n=3):\n....:         return m^n\n....:\nsage: B = BAR()\nsage: B.bar() is B.bar(2,3)\nTrue\n```\n\n\nWithout my patch:\n\n```\nsage: timeit('B.bar(n=2,m=3)', number=10000)\n10000 loops, best of 3: 20.4 \u00c2\u00b5s per loop\nsage: timeit('B.bar()', number=10000)\n10000 loops, best of 3: 17.1 \u00c2\u00b5s per loop\n```\n\n\nWith my patch:\n\n```\nsage: timeit('B.bar(n=2,m=3)', number=10000)\n10000 loops, best of 3: 3.73 \u00c2\u00b5s per loop\nsage: timeit('B.bar()', number=10000)\n10000 loops, best of 3: 1.95 \u00c2\u00b5s per loop\n```\n",
    "created_at": "2011-01-09T20:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77885",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:4 davidloeffler]:
> Might it not be better for `@`cached_method to store its cache as an attribute of the instance object, rather than having a single cache which stores the values for all instances of that class?

It was not the case that there was a single cache for all instances (the cache was in the instance for `cached_method` resp. in the parent of the instance for `cached_in_parent_method`). However, a part of the overhead came from the fact that the cached method *itself* has not been an attribute of the instance but of its class.

I just attached a new patch that goes far beyond Jason's approach.

These examples show how the cached method performance is
improved by my patch:

**__Using instance attributes__**

Polynomial ideals have a cached method `groebner_basis`. Without
my patch, asking for `I.groebner_basis` would return a
`CachedMethodCaller` - always a *new instance* whenever the cached
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


**__Creating the cache key__**

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
*once*, and store the result for later. That's another reason why it
is good to have one `CachedMethodCaller` permanently attached to an
instance (rather than always creating a new one), since otherwise
caching of the default key would be difficult.

**__Accessing the cache__**

Originally, a method `get_cache` was used to get the cache dictionary.
In some cases, that method used to call another one, `_get_instance_cache`.
Hence, again, there was an overhead of calling two methods.

By my patch, the cache is *always* available as an attribute of
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

**__Documentation__**

I extended the documentation - but I did not cover `ClearCacheOnPickle`,
which my patch does not change. Apart from that, the doctest coverage
of `sage.misc.cachefunc` is complete. For `sage.misc.function_mangling`,
the coverage script complains "Please add a `TestSuite(s).run()` doctest."
I don't know were that comes from.

Of course, all doctests pass for me. I did not test whether the documentation
looks nice in html.

**__Performance__**

Last but not least, what the ticket is about: Performance!

Here is the setting:

```
sage: class Foo:
....:     def __init__(self,P=None):
....:         if P is None:
....:             self._parent=self
....:         else:
....:             self._parent=P
....:     @cached_method
....:     def bar(self,m,n=3):
....:         return m^n
....:     @cached_in_parent_method
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
....:     @cached_method
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

archive/issue_comments_077886.json:
```json
{
    "body": "Changing keywords from \"\" to \"cached method\".",
    "created_at": "2011-01-09T20:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77886",
    "user": "https://github.com/simon-king-jena"
}
```

Changing keywords from "" to "cached method".



---

archive/issue_comments_077887.json:
```json
{
    "body": "For the patchbot:\n\nApply trac8611_cached_method_overhaul.patch",
    "created_at": "2011-01-09T20:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77887",
    "user": "https://github.com/simon-king-jena"
}
```

For the patchbot:

Apply trac8611_cached_method_overhaul.patch



---

archive/issue_comments_077888.json:
```json
{
    "body": "I forgot to provide a comparison against an explicitly coded cache:\n\n```\nsage: class Foo:\n....:     @cached_method\n....:     def decorator_bar(self, n=15):\n....:         return sum(range(2**n))\n....:     def manual_bar(self, n=15):\n....:         try:\n....:             D = self._my_cache\n....:         except AttributeError:\n....:             D = self._my_cache = {}\n....:             D[n] = sum(range(2**n))\n....:         return D[n]\n....:\nsage: F = Foo()\nsage: F.decorator_bar() is F.decorator_bar()\nTrue\nsage: F.decorator_bar() == F.manual_bar()\nTrue\nsage: F.manual_bar() is F.manual_bar()\nTrue\nsage: timeit('F.manual_bar()', number=10000)\n10000 loops, best of 3: 1.02 \u00c2\u00b5s per loop\nsage: timeit('F.decorator_bar()', number=10000)\n10000 loops, best of 3: 1.71 \u00c2\u00b5s per loop\nsage: timeit('F.decorator_bar(15)', number=10000)\n10000 loops, best of 3: 3.05 \u00c2\u00b5s per loop\n```\n\n\nHence, the new version of cached methods can almost compete with an explicitly coded cache, but is of course much more comfortable for the programmer.",
    "created_at": "2011-01-09T21:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77888",
    "user": "https://github.com/simon-king-jena"
}
```

I forgot to provide a comparison against an explicitly coded cache:

```
sage: class Foo:
....:     @cached_method
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

archive/issue_comments_077889.json:
```json
{
    "body": "I forgot to mention another bug fix (that is also doctested). It is about the comparison of representations of symmetric groups:\n\n```\nsage: spc = SymmetricGroupRepresentation([3])\nsage: spc.important_info = 'Sage rules'\nsage: spc == SymmetricGroupRepresentation([3]) # this used to return False!\nTrue\n```\n\n\nThe ticket description states that the improvements concern the *critical* path (i.e., the value is already caught). Here is one more comparison, that also shows what happens in the non-critical path.\n\nSetting:\n\n```\nsage: class A:\n....:     @cached_method\n....:     def bar(self,x):\n....:         return x\n....:     @cached_in_parent_method\n....:     def barP(self,x):\n....:         return x\n....:     def parent(self):\n....:         return self\n....:     \nsage: a = A()\n```\n\n\nWithout my patch:\n\n```\n# The non-critical path:\nsage: time for x in range(10^6): b=a.bar(x)\nCPU times: user 24.97 s, sys: 0.16 s, total: 25.13 s\nWall time: 25.13 s\nsage: time for x in range(10^6): b=a.barP(x)\nCPU times: user 41.03 s, sys: 0.13 s, total: 41.16 s\nWall time: 41.17 s\n\n# The critical path (now the values are cached):\nsage: time for x in range(10^6): b=a.bar(x)\nCPU times: user 16.45 s, sys: 0.02 s, total: 16.47 s\nWall time: 16.47 s\nsage: time for x in range(10^6): b=a.barP(x)\nCPU times: user 20.47 s, sys: 0.02 s, total: 20.50 s\nWall time: 20.50 s\n```\n\n\nWith my patch:\n\n```\n# The non-critical path:\nsage: time for x in range(10^6): b=a.bar(x)\nCPU times: user 11.40 s, sys: 0.08 s, total: 11.48 s\nWall time: 11.48 s\nsage: time for x in range(10^6): b=a.barP(x)\nCPU times: user 27.89 s, sys: 0.12 s, total: 28.01 s\nWall time: 28.02 s\n\n# The critical path (now the values are cached):\nsage: time for x in range(10^6): b=a.bar(x)\nCPU times: user 3.09 s, sys: 0.01 s, total: 3.10 s\nWall time: 3.10 s\nsage: time for x in range(10^6): b=a.barP(x)\nCPU times: user 5.25 s, sys: 0.02 s, total: 5.26 s\nWall time: 5.26 s\n```\n\n\nHence, the patch improves all cases.",
    "created_at": "2011-01-10T07:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77889",
    "user": "https://github.com/simon-king-jena"
}
```

I forgot to mention another bug fix (that is also doctested). It is about the comparison of representations of symmetric groups:

```
sage: spc = SymmetricGroupRepresentation([3])
sage: spc.important_info = 'Sage rules'
sage: spc == SymmetricGroupRepresentation([3]) # this used to return False!
True
```


The ticket description states that the improvements concern the *critical* path (i.e., the value is already caught). Here is one more comparison, that also shows what happens in the non-critical path.

Setting:

```
sage: class A:
....:     @cached_method
....:     def bar(self,x):
....:         return x
....:     @cached_in_parent_method
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

archive/issue_comments_077890.json:
```json
{
    "body": "In the patch version that I've just attached, I also inserted the documentation of `sage.misc.cachedfunc` and (after cleaning the documentation) of `sage.misc.function_mangling` into the reference manual. I think the documentation looks nice, but perhaps the referee can have a look on it as well.",
    "created_at": "2011-01-10T09:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77890",
    "user": "https://github.com/simon-king-jena"
}
```

In the patch version that I've just attached, I also inserted the documentation of `sage.misc.cachedfunc` and (after cleaning the documentation) of `sage.misc.function_mangling` into the reference manual. I think the documentation looks nice, but perhaps the referee can have a look on it as well.



---

archive/issue_comments_077891.json:
```json
{
    "body": "Improved performance for cached methods; add documentation to reference manual; cache is_subcateory. Replaces Jason's patch",
    "created_at": "2011-01-12T17:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77891",
    "user": "https://github.com/simon-king-jena"
}
```

Improved performance for cached methods; add documentation to reference manual; cache is_subcateory. Replaces Jason's patch



---

archive/issue_comments_077892.json:
```json
{
    "body": "Attachment [trac8611_cached_method_overhaul.patch](tarball://root/attachments/some-uuid/ticket8611/trac8611_cached_method_overhaul.patch) by @simon-king-jena created at 2011-01-12 17:20:28\n\nI slightly changed the patch. But the small change has in fact a big impact:\n\nThe method `sage.categories.category.Category.is_subcategory` is used to test whether something is an object of a given category. Due to the omnipresence of categories in Sage, this test occurs very often. So, it should be optimised!\n\nI suggest that `is_subcategory` should be cached. I.e., the new patch version differs from the old one only in the line \"`@`cached_method\" in front of that method.\n\nI believe that the additional memory consumption is affordable: When starting Sage, there are precisely 55 categories, so, in the worst case, caching `is_subcategory` adds 55 cache dictionaries with 55 entries.\n\nThe impact on the overall performance is obvious:\nOn my machine, `sage -tp 4 sage` takes 1721.2 seconds without my patch, but 1643.8 seconds with my patch.\n\nHence, the average improvement is about 4.5%.",
    "created_at": "2011-01-12T17:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77892",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac8611_cached_method_overhaul.patch](tarball://root/attachments/some-uuid/ticket8611/trac8611_cached_method_overhaul.patch) by @simon-king-jena created at 2011-01-12 17:20:28

I slightly changed the patch. But the small change has in fact a big impact:

The method `sage.categories.category.Category.is_subcategory` is used to test whether something is an object of a given category. Due to the omnipresence of categories in Sage, this test occurs very often. So, it should be optimised!

I suggest that `is_subcategory` should be cached. I.e., the new patch version differs from the old one only in the line "`@`cached_method" in front of that method.

I believe that the additional memory consumption is affordable: When starting Sage, there are precisely 55 categories, so, in the worst case, caching `is_subcategory` adds 55 cache dictionaries with 55 entries.

The impact on the overall performance is obvious:
On my machine, `sage -tp 4 sage` takes 1721.2 seconds without my patch, but 1643.8 seconds with my patch.

Hence, the average improvement is about 4.5%.



---

archive/issue_comments_077893.json:
```json
{
    "body": "Apply trac8611_cached_method_overhaul.patch\n\n(for the patchbot)",
    "created_at": "2011-01-16T16:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77893",
    "user": "https://github.com/loefflerd"
}
```

Apply trac8611_cached_method_overhaul.patch

(for the patchbot)



---

archive/issue_comments_077894.json:
```json
{
    "body": "Replying to [comment:14 davidloeffler]:\n> Apply trac8611_cached_method_overhaul.patch\n> \n> (for the patchbot)\n\nThere already was such message for the patchbot.\n\nBut one question: On sage-devel, Robert Bradshaw reported that I need to rebase the patch. But the patchbot - at least in one attempt - succeeded. So, what is the status?\n\nUnfortunately, I seriously screwed up my Sage installations. Currently, my two ol installations are broken, and sadly I was unablee to build either sage-4.6.1 or sage-4.6.2.alpha0/1.\n\nCheers,\n\nSimon",
    "created_at": "2011-01-16T17:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77894",
    "user": "https://github.com/simon-king-jena"
}
```

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

archive/issue_comments_077895.json:
```json
{
    "body": "Replying to [comment:15 SimonKing]:\n> Replying to [comment:14 davidloeffler]:\n> > Apply trac8611_cached_method_overhaul.patch\n> > \n> > (for the patchbot)\n> \n> There already was such message for the patchbot.\n\nPatchbot's a bit pedantic about formatting of such messages. If you look at the records of the test runs it's done, you'll see that prior to today it was trying to apply both patches at once, and thus failing, and after I prodded it earlier, it did a new run which passed.\n\nI've got a working 4.6.2.alpha0 build, so I can test it against that tomorrow morning.",
    "created_at": "2011-01-16T20:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77895",
    "user": "https://github.com/loefflerd"
}
```

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

archive/issue_comments_077896.json:
```json
{
    "body": "Applies fine and passes doctests both using 4.6.2.alpha0 on my system, and using 4.6.1 with patchbot. I ran some tests and in the case of a method with no arguments it's something like 15 times faster than the old code and only a tiny bit slower than a hand-rolled cache. Code looks fine by eye, and it's great that you added these modules to the ref manual as well. Positive review.\n\nI'm looking forward to using %prun in future sage versions and not finding that 20% of the execution time has been spent in \"fix_to_pos\", which is frequently the case at the moment...",
    "created_at": "2011-01-17T11:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77896",
    "user": "https://github.com/loefflerd"
}
```

Applies fine and passes doctests both using 4.6.2.alpha0 on my system, and using 4.6.1 with patchbot. I ran some tests and in the case of a method with no arguments it's something like 15 times faster than the old code and only a tiny bit slower than a hand-rolled cache. Code looks fine by eye, and it's great that you added these modules to the ref manual as well. Positive review.

I'm looking forward to using %prun in future sage versions and not finding that 20% of the execution time has been spent in "fix_to_pos", which is frequently the case at the moment...



---

archive/issue_comments_077897.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-17T11:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77897",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077898.json:
```json
{
    "body": "Please use line breaks in the commit message if it is so long.  Make sure the first line is a short description of the patch with the ticket number.  Following lines can contain a longer description.",
    "created_at": "2011-01-23T13:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77898",
    "user": "https://github.com/jdemeyer"
}
```

Please use line breaks in the commit message if it is so long.  Make sure the first line is a short description of the patch with the ticket number.  Following lines can contain a longer description.



---

archive/issue_comments_077899.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-23T13:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77899",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_077900.json:
```json
{
    "body": "Apply only this patch",
    "created_at": "2011-01-23T15:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77900",
    "user": "https://github.com/loefflerd"
}
```

Apply only this patch



---

archive/issue_comments_077901.json:
```json
{
    "body": "Attachment [trac8611_cached_method_overhaul-fixed.patch](tarball://root/attachments/some-uuid/ticket8611/trac8611_cached_method_overhaul-fixed.patch) by @loefflerd created at 2011-01-23 15:17:01\n\nDone.",
    "created_at": "2011-01-23T15:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77901",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac8611_cached_method_overhaul-fixed.patch](tarball://root/attachments/some-uuid/ticket8611/trac8611_cached_method_overhaul-fixed.patch) by @loefflerd created at 2011-01-23 15:17:01

Done.



---

archive/issue_comments_077902.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-01-23T15:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77902",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_077903.json:
```json
{
    "body": "Replying to [comment:19 davidloeffler]:\n> Done.\n\nThank you!",
    "created_at": "2011-01-23T16:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77903",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:19 davidloeffler]:
> Done.

Thank you!



---

archive/issue_comments_077904.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77904",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_077905.json:
```json
{
    "body": "For the record, a related thread:\n\n- http://groups.google.com/group/sage-devel/browse_thread/thread/6607a3919c619345",
    "created_at": "2011-01-28T10:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8611#issuecomment-77905",
    "user": "https://github.com/nthiery"
}
```

For the record, a related thread:

- http://groups.google.com/group/sage-devel/browse_thread/thread/6607a3919c619345
