# Issue 6199: Integer * int is slow

archive/issues_006199.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @robertwb\n\n\n```\nsage: a = 123\nsage: b = 456\nsage: c = 456r\nsage: timeit(\"a*b\")\n625 loops, best of 3: 312 ns per loop\nsage: timeit(\"a*c\")\n625 loops, best of 3: 2.99 \u00b5s per loop\n```\n\n\nDitto for +, -. If I understand the code correctly, there always is a coercion to Integer, which could be avoided. I'm not sure how to best fix this since the ring operators are not implemented in the Integer class itself.\n\nFor division and shift, see #6083 and #6118.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6199\n\n",
    "created_at": "2009-06-03T18:44:59Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Integer * int is slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6199",
    "user": "https://github.com/fredrik-johansson"
}
```
Assignee: somebody

CC:  @robertwb


```
sage: a = 123
sage: b = 456
sage: c = 456r
sage: timeit("a*b")
625 loops, best of 3: 312 ns per loop
sage: timeit("a*c")
625 loops, best of 3: 2.99 µs per loop
```


Ditto for +, -. If I understand the code correctly, there always is a coercion to Integer, which could be avoided. I'm not sure how to best fix this since the ring operators are not implemented in the Integer class itself.

For division and shift, see #6083 and #6118.

Issue created by migration from https://trac.sagemath.org/ticket/6199





---

archive/issue_comments_049409.json:
```json
{
    "body": "We could make an action on Integers by ints.",
    "created_at": "2009-06-05T11:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49409",
    "user": "https://github.com/robertwb"
}
```

We could make an action on Integers by ints.



---

archive/issue_events_006447.json:
```json
{
    "actor": "@craigcitro",
    "created_at": "2010-01-21T00:22:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6199#event-6447"
}
```



---

archive/issue_comments_049410.json:
```json
{
    "body": "So sadly, I think this is a wontfix. I tested this out, and at the expense of some ugly code, we get roughly a factor of 2 speedup -- and that's basically the best we can do. The problem is that the coercion model needs to look up a cached map to avoid the coercion to `Integer`; looking up this map and calling it takes long enough that a factor of 2 is the best we can get.\n\nFredrik, did you have code that was getting slowed down by this? Would a factor of two on this make a big difference for you?",
    "created_at": "2010-01-21T00:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49410",
    "user": "https://github.com/craigcitro"
}
```

So sadly, I think this is a wontfix. I tested this out, and at the expense of some ugly code, we get roughly a factor of 2 speedup -- and that's basically the best we can do. The problem is that the coercion model needs to look up a cached map to avoid the coercion to `Integer`; looking up this map and calling it takes long enough that a factor of 2 is the best we can get.

Fredrik, did you have code that was getting slowed down by this? Would a factor of two on this make a big difference for you?



---

archive/issue_comments_049411.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-01-21T00:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49411",
    "user": "https://github.com/craigcitro"
}
```

Resolution: wontfix



---

archive/issue_comments_049412.json:
```json
{
    "body": "Craig, thanks for investigating. This is, unfortunately, quite critical for improving mpmath's performance, and the only other solution is not to use sage.Integer.\n\nI haven't touched Cython in a while now, but... I'm still not clear about why Integer multiplication has to go through the generic ring multiplication code. Wouldn't it be possible to extend the coercion/operator code so that any subclass can overload it? Something like (in regular Python, made-up method names):\n\n\n```\nclass RingElement:\n    def __mul__(self, other):\n        self, other = self.coerce(other)\n        return self._mul_coerced(self, other)\n\nclass Integer(RingElement):\n    def __mul__(self, other):\n        if type(other) is int:\n            return self._mul_int(other)\n        return RingElement.__mul__(self, other)\n    def _mul_coerced(self, other):\n        # multiply two Integers\n```\n",
    "created_at": "2010-01-21T02:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49412",
    "user": "https://github.com/fredrik-johansson"
}
```

Craig, thanks for investigating. This is, unfortunately, quite critical for improving mpmath's performance, and the only other solution is not to use sage.Integer.

I haven't touched Cython in a while now, but... I'm still not clear about why Integer multiplication has to go through the generic ring multiplication code. Wouldn't it be possible to extend the coercion/operator code so that any subclass can overload it? Something like (in regular Python, made-up method names):


```
class RingElement:
    def __mul__(self, other):
        self, other = self.coerce(other)
        return self._mul_coerced(self, other)

class Integer(RingElement):
    def __mul__(self, other):
        if type(other) is int:
            return self._mul_int(other)
        return RingElement.__mul__(self, other)
    def _mul_coerced(self, other):
        # multiply two Integers
```




---

archive/issue_comments_049413.json:
```json
{
    "body": "Resolution changed from wontfix to ",
    "created_at": "2010-01-22T06:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49413",
    "user": "https://github.com/craigcitro"
}
```

Resolution changed from wontfix to 



---

archive/issue_comments_049414.json:
```json
{
    "body": "Hi Fredrik,\n\nWell, let's not give up hope yet. :) I'll give the full explanation of what's happening with the coercion system below, but first, I want to ask: is there any reason you couldn't just switch to using `sage.integer.Integer` everywhere, or at least in more places? (If you're worried about modifying existing code, the preparser can do the hard work for you, and we can definitely adapt it if needed.) Or, in other words, where are you getting all these Python `int`s from?\n\nAlso, I want to note that there's one more reason to not worry so much: arithmetic on Python `int`s is going to take at least a ~%20 performance hit in Python 3 (at least for the example at the top of this ticket).\n\nHere's what's happening with this code. Every object that derives from Sage's `Element` type goes through the coercion system. It does a lot of things for us: in particular, it makes things like \n\n```\nsage: R.<x> = ZZ[]\nsage: 1/2 + x\n1/2 + x\nsage: parent(1/2 + x)\nUnivariate Polynomial Ring in x over Rational Field\n```\n\nhappen without any hard work on the part of the user, and with a minimal amount of code duplication. So what you're suggesting above does in fact happen: the `__mul__` code ultimately calls into the `bin_op` method of the coercion model (which is itself an object, and has lots of useful methods; try `cm = get_coercion_model()` from the sage prompt), and that checks a few things in order for a multiplication, say `x*y`:\n\n* are the parents of `x` and `y` identical? If so, call the `_mul_` method. (This actually happens in `__mul__`.)\n* have we saved an action of `x.parent()` on `y.parent()`, or vice-versa? If so, apply that. If not, see if we can find one, and use it if we can.\n* can we coerce `x` and `y` into the same parent? If so, do it and then call `_mul_` on the result.\n* some other stuff.\n\nSo what's happening right now is that we're hitting the third bullet, i.e. we end up doing the coercion of the `int` into `ZZ`, as you noted in the ticket description. What I did was write some code that added an action of `int` objects on `ZZ`, which gets picked up in the second bullet above. This is the \"natural\" way to add this kind of thing to the coercion model. The problem is that it's still too slow for what you want: Robert wrote a custom dictionary for storing the actions, but it's still doing work on the order of hundreds of nanoseconds to get called and look it up. For most everything, this isn't so bad, but in your case, it's causing trouble. \n\nNow, that's saying that the \"right\" fix, i.e. use the coercion model the way it's intended, doesn't work out. Of course, that doesn't mean we don't have other options. I just sat down and hacked together a little code that short-circuits things earlier on (just before the second bullet above). It definitely works ... here's before:\n\n```\nsage: a = 123 ; b = 456 ; c = 456r ; y = polygen(ZZ)\nsage: a*c\n56088\nsage: %timeit a*c\n1000000 loops, best of 3: 1.27 us per loop\nsage: %timeit a*y\n1000000 loops, best of 3: 1.97 us per loop\nsage: %timeit a*b\n10000000 loops, best of 3: 150 ns per loop\n```\n\nand after:\n\n```\nsage: a = 123 ; b = 456 ; c = 456r ; y = polygen(ZZ)\nsage: a*c\n56088\nsage: %timeit a*c\n1000000 loops, best of 3: 207 ns per loop\nsage: %timeit a*b\n10000000 loops, best of 3: 149 ns per loop\nsage: %timeit a*y\n1000000 loops, best of 3: 1.99 us per loop\n```\n\nIn the case that it's not `Integer * int`, it's one test of a C `int` being nonzero and between two and four extra pointer comparisons on any call to `bin_op`. Mind you, that's going to happen for **every** binary arithmetic operation where the parents aren't identical, which is definitely a hefty price if you live in a world where you don't multiply `Integer * int` very often. I think we could eliminate the C `int` test, if we were crafty.\n\n(Side note: I got a ~10% performance regression on the `a*y` line above between 4.2 and 4.3 -- do either of you have both installed to try it out?)\n\nRobert, what are your thoughts? I know that \"Special cases aren't special enough to break the rules,\" and in general I don't like special-casing things. Plus, it's potentially less significant with Py3 on the horizon. But if it's really going to be a showstopper for Fredrik, we should at least think about it more. It's not like there are very many types where the operations are noticeably faster than a few lookups, so it's not opening a loophole that could be abused very much, I think.",
    "created_at": "2010-01-22T06:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49414",
    "user": "https://github.com/craigcitro"
}
```

Hi Fredrik,

Well, let's not give up hope yet. :) I'll give the full explanation of what's happening with the coercion system below, but first, I want to ask: is there any reason you couldn't just switch to using `sage.integer.Integer` everywhere, or at least in more places? (If you're worried about modifying existing code, the preparser can do the hard work for you, and we can definitely adapt it if needed.) Or, in other words, where are you getting all these Python `int`s from?

Also, I want to note that there's one more reason to not worry so much: arithmetic on Python `int`s is going to take at least a ~%20 performance hit in Python 3 (at least for the example at the top of this ticket).

Here's what's happening with this code. Every object that derives from Sage's `Element` type goes through the coercion system. It does a lot of things for us: in particular, it makes things like 

```
sage: R.<x> = ZZ[]
sage: 1/2 + x
1/2 + x
sage: parent(1/2 + x)
Univariate Polynomial Ring in x over Rational Field
```

happen without any hard work on the part of the user, and with a minimal amount of code duplication. So what you're suggesting above does in fact happen: the `__mul__` code ultimately calls into the `bin_op` method of the coercion model (which is itself an object, and has lots of useful methods; try `cm = get_coercion_model()` from the sage prompt), and that checks a few things in order for a multiplication, say `x*y`:

* are the parents of `x` and `y` identical? If so, call the `_mul_` method. (This actually happens in `__mul__`.)
* have we saved an action of `x.parent()` on `y.parent()`, or vice-versa? If so, apply that. If not, see if we can find one, and use it if we can.
* can we coerce `x` and `y` into the same parent? If so, do it and then call `_mul_` on the result.
* some other stuff.

So what's happening right now is that we're hitting the third bullet, i.e. we end up doing the coercion of the `int` into `ZZ`, as you noted in the ticket description. What I did was write some code that added an action of `int` objects on `ZZ`, which gets picked up in the second bullet above. This is the "natural" way to add this kind of thing to the coercion model. The problem is that it's still too slow for what you want: Robert wrote a custom dictionary for storing the actions, but it's still doing work on the order of hundreds of nanoseconds to get called and look it up. For most everything, this isn't so bad, but in your case, it's causing trouble. 

Now, that's saying that the "right" fix, i.e. use the coercion model the way it's intended, doesn't work out. Of course, that doesn't mean we don't have other options. I just sat down and hacked together a little code that short-circuits things earlier on (just before the second bullet above). It definitely works ... here's before:

```
sage: a = 123 ; b = 456 ; c = 456r ; y = polygen(ZZ)
sage: a*c
56088
sage: %timeit a*c
1000000 loops, best of 3: 1.27 us per loop
sage: %timeit a*y
1000000 loops, best of 3: 1.97 us per loop
sage: %timeit a*b
10000000 loops, best of 3: 150 ns per loop
```

and after:

```
sage: a = 123 ; b = 456 ; c = 456r ; y = polygen(ZZ)
sage: a*c
56088
sage: %timeit a*c
1000000 loops, best of 3: 207 ns per loop
sage: %timeit a*b
10000000 loops, best of 3: 149 ns per loop
sage: %timeit a*y
1000000 loops, best of 3: 1.99 us per loop
```

In the case that it's not `Integer * int`, it's one test of a C `int` being nonzero and between two and four extra pointer comparisons on any call to `bin_op`. Mind you, that's going to happen for **every** binary arithmetic operation where the parents aren't identical, which is definitely a hefty price if you live in a world where you don't multiply `Integer * int` very often. I think we could eliminate the C `int` test, if we were crafty.

(Side note: I got a ~10% performance regression on the `a*y` line above between 4.2 and 4.3 -- do either of you have both installed to try it out?)

Robert, what are your thoughts? I know that "Special cases aren't special enough to break the rules," and in general I don't like special-casing things. Plus, it's potentially less significant with Py3 on the horizon. But if it's really going to be a showstopper for Fredrik, we should at least think about it more. It's not like there are very many types where the operations are noticeably faster than a few lookups, so it's not opening a loophole that could be abused very much, I think.



---

archive/issue_comments_049415.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-01-22T06:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49415",
    "user": "https://github.com/craigcitro"
}
```

Changing status from closed to new.



---

archive/issue_events_006448.json:
```json
{
    "actor": "@craigcitro",
    "created_at": "2010-01-22T06:57:13Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6199#event-6448"
}
```



---

archive/issue_comments_049416.json:
```json
{
    "body": "If we're going to special case, we could override `__mul__` for Integer directly, rather than stick stuff in `Element.__mul__`. That's \"breaking the rules\" even more though. Alternatively, we could add a `cdef Element _mul_long(self, long n)` method which is checked for right after the parents aren't the same. This is a bit hackish, but would provide a good avenue for improvements for other types as well (QQ, RDF). Do we need addition as well? (No, I don't think this should be extended to other operands...)\n\nNote that \n\n\n```\nsage: timeit(\"a\", number=10**6)\n1000000 loops, best of 3: 58.1 ns per loop\n```\n\n\nso I wrote my own\n\n\n```\ndef time_mul(a, b, long n):\n    cdef long i\n    for i in range(n):\n        a*b\n```\n\n\nWith this, I did a special _mul_long method. \n\nBefore:\n\n```\nsage: a = 123 ; b = 456 ; c = 456r ; y = RDF(pi)\nsage: a*c, a*y\n(56088, 386.415896392)\nsage: %time time_mul(a,b, 10**7)\nCPU times: user 1.13 s, sys: 0.00 s, total: 1.13 s\nWall time: 1.13 s\nsage: %time time_mul(a,c, 10**7)\nCPU times: user 17.14 s, sys: 0.04 s, total: 17.18 s\nWall time: 17.25 s\nsage: %time time_mul(a,y, 10**7)\nCPU times: user 8.21 s, sys: 0.02 s, total: 8.24 s\nWall time: 8.25 s\n```\n\n\nAfter:\n\n```\nsage: a = 123 ; b = 456 ; c = 456r ; y = RDF(pi)\nsage: a*c, a*y\n(56088, 386.415896392)\nsage: %time time_mul(a,b, 10**7)\nCPU times: user 1.16 s, sys: 0.00 s, total: 1.16 s\nWall time: 1.17 s\nsage: %time time_mul(a,c, 10**7)\nCPU times: user 0.95 s, sys: 0.00 s, total: 0.96 s\nWall time: 0.96 s\nsage: %time time_mul(a,y, 10**7)\nCPU times: user 8.52 s, sys: 0.02 s, total: 8.54 s\nWall time: 8.57 s\n```\n\n\nI'm leaning towards it being worth it, on the right only, for * and + only. The cost is (on my machine) an extra 25ns per non-identical-parents operation, which are at the cheapest is at least 100s of ns.",
    "created_at": "2010-01-22T08:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49416",
    "user": "https://github.com/robertwb"
}
```

If we're going to special case, we could override `__mul__` for Integer directly, rather than stick stuff in `Element.__mul__`. That's "breaking the rules" even more though. Alternatively, we could add a `cdef Element _mul_long(self, long n)` method which is checked for right after the parents aren't the same. This is a bit hackish, but would provide a good avenue for improvements for other types as well (QQ, RDF). Do we need addition as well? (No, I don't think this should be extended to other operands...)

Note that 


```
sage: timeit("a", number=10**6)
1000000 loops, best of 3: 58.1 ns per loop
```


so I wrote my own


```
def time_mul(a, b, long n):
    cdef long i
    for i in range(n):
        a*b
```


With this, I did a special _mul_long method. 

Before:

```
sage: a = 123 ; b = 456 ; c = 456r ; y = RDF(pi)
sage: a*c, a*y
(56088, 386.415896392)
sage: %time time_mul(a,b, 10**7)
CPU times: user 1.13 s, sys: 0.00 s, total: 1.13 s
Wall time: 1.13 s
sage: %time time_mul(a,c, 10**7)
CPU times: user 17.14 s, sys: 0.04 s, total: 17.18 s
Wall time: 17.25 s
sage: %time time_mul(a,y, 10**7)
CPU times: user 8.21 s, sys: 0.02 s, total: 8.24 s
Wall time: 8.25 s
```


After:

```
sage: a = 123 ; b = 456 ; c = 456r ; y = RDF(pi)
sage: a*c, a*y
(56088, 386.415896392)
sage: %time time_mul(a,b, 10**7)
CPU times: user 1.16 s, sys: 0.00 s, total: 1.16 s
Wall time: 1.17 s
sage: %time time_mul(a,c, 10**7)
CPU times: user 0.95 s, sys: 0.00 s, total: 0.96 s
Wall time: 0.96 s
sage: %time time_mul(a,y, 10**7)
CPU times: user 8.52 s, sys: 0.02 s, total: 8.54 s
Wall time: 8.57 s
```


I'm leaning towards it being worth it, on the right only, for * and + only. The cost is (on my machine) an extra 25ns per non-identical-parents operation, which are at the cheapest is at least 100s of ns.



---

archive/issue_comments_049417.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-01-22T08:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49417",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_049418.json:
```json
{
    "body": "Thanks for working on this!\n\nIn mpmath, there are a lot of loops for fixed-point power series that basically look something like:\n\n\n```\nprec = counter_type(150)\ns = t = x = value_type(1) << prec\nk = counter_type(1)\nwhile t:\n    t = (t*x) >> prec\n    t = t*k//(4*k+1)\n    s += t\n    k += 1\n```\n\n\nBecause Python ints are significantly faster than Integers for small values and Integers are significantly faster than ints for large values, it's optimal to use counter_type = int and value_type = Integer. (It's even more optimal to Cythonize the same code, but I'm not there quite yet.) Shift and division were already fixed.\n\n> I'm leaning towards it being worth it, on the right only, for * and + only.\n\nUnfortunately I think it's equally common for the int to be on the left (this can be fixed, but it's hard to track down where it happens). Addition is not as important.",
    "created_at": "2010-01-22T11:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49418",
    "user": "https://github.com/fredrik-johansson"
}
```

Thanks for working on this!

In mpmath, there are a lot of loops for fixed-point power series that basically look something like:


```
prec = counter_type(150)
s = t = x = value_type(1) << prec
k = counter_type(1)
while t:
    t = (t*x) >> prec
    t = t*k//(4*k+1)
    s += t
    k += 1
```


Because Python ints are significantly faster than Integers for small values and Integers are significantly faster than ints for large values, it's optimal to use counter_type = int and value_type = Integer. (It's even more optimal to Cythonize the same code, but I'm not there quite yet.) Shift and division were already fixed.

> I'm leaning towards it being worth it, on the right only, for * and + only.

Unfortunately I think it's equally common for the int to be on the left (this can be fixed, but it's hard to track down where it happens). Addition is not as important.



---

archive/issue_comments_049419.json:
```json
{
    "body": "So what is the milestone for this ticket? Is it still a \"wontfix\"?",
    "created_at": "2010-01-22T14:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49419",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

So what is the milestone for this ticket? Is it still a "wontfix"?



---

archive/issue_comments_049420.json:
```json
{
    "body": "Robert:\n\nI think there are several places we could put the code -- if nothing else, it might be nice to keep it in `coerce.pyx`, so that it's the one place where all the \"rules\" for coercion appear. Also, if we ultimately wanted to implement such a pathway for something that isn't a `RingElement` (which is the `__mul__` we're going to need to put the code in), the code would be in the same place. \n\nAlso, I'd prefer to just go ahead and implement it for arithmetic on both sides -- we can do two type comparisons as `PY_TYPE_CHECK_EXACT`, and if need be, tell the branch predictor that they're unlikely (because they are in the general case, I think). I'm always suspicious of rules like \"keep the Python int on the right, because that's 10X faster.\" I'd also hate to have to make a comment in a patch review saying \"oh, this speeds up by a factor of 10 if you reverse the order of operands.\" I know these things exist elsewhere -- but that's no reason to add one more to the pile.  Plus, it's sure to lead to a ton of posts on the mailing list about it, where people think they've found a new \"bug.\" `:)`\n\nI suspect you're going to be on campus in a few hours -- we can chat about this then.\n\nFredrik: \n\nThat's a really good use-case. That said, I guess I don't understand why GMP/MPIR don't use unboxed immediate integers for small values, but given that I haven't played with the guts of the code, they probably know better than I do. It would be nice in your case, though -- you could have both `counter_type` and `value_type` be `Integer`. (Well, you might run into some issues when you only used small values, but in principle, anyway.)\n\nI'm curious: is this code going to be used as part of the \"core\" of mpmath, or will you just write the code so it takes advantage of Sage whenever it's available? (My impression was that you liked mpmath being pure Python.)",
    "created_at": "2010-01-22T18:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49420",
    "user": "https://github.com/craigcitro"
}
```

Robert:

I think there are several places we could put the code -- if nothing else, it might be nice to keep it in `coerce.pyx`, so that it's the one place where all the "rules" for coercion appear. Also, if we ultimately wanted to implement such a pathway for something that isn't a `RingElement` (which is the `__mul__` we're going to need to put the code in), the code would be in the same place. 

Also, I'd prefer to just go ahead and implement it for arithmetic on both sides -- we can do two type comparisons as `PY_TYPE_CHECK_EXACT`, and if need be, tell the branch predictor that they're unlikely (because they are in the general case, I think). I'm always suspicious of rules like "keep the Python int on the right, because that's 10X faster." I'd also hate to have to make a comment in a patch review saying "oh, this speeds up by a factor of 10 if you reverse the order of operands." I know these things exist elsewhere -- but that's no reason to add one more to the pile.  Plus, it's sure to lead to a ton of posts on the mailing list about it, where people think they've found a new "bug." `:)`

I suspect you're going to be on campus in a few hours -- we can chat about this then.

Fredrik: 

That's a really good use-case. That said, I guess I don't understand why GMP/MPIR don't use unboxed immediate integers for small values, but given that I haven't played with the guts of the code, they probably know better than I do. It would be nice in your case, though -- you could have both `counter_type` and `value_type` be `Integer`. (Well, you might run into some issues when you only used small values, but in principle, anyway.)

I'm curious: is this code going to be used as part of the "core" of mpmath, or will you just write the code so it takes advantage of Sage whenever it's available? (My impression was that you liked mpmath being pure Python.)



---

archive/issue_comments_049421.json:
```json
{
    "body": "Multiplication on the left has less to gain, as it's going to try to call int.__mul__ before falling back to this code. Do you think it's worth doubling the general case penalty to support a smaller relative gain? People who care about timings this small (e.g. mpmath) can follow such rules, or ideally write Cython directly. I wrote a mode once that was verbose about all the coercions used, I could resurrect that somewhere for more easily tracking down stuff like this. \n\nFWIW, I put `_mul_long` onto ModuleElement, not just RingElement. The extra indirection needed to put it in coerce.pyx will make it at least 50% or more slower, probably much more.",
    "created_at": "2010-01-22T19:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49421",
    "user": "https://github.com/robertwb"
}
```

Multiplication on the left has less to gain, as it's going to try to call int.__mul__ before falling back to this code. Do you think it's worth doubling the general case penalty to support a smaller relative gain? People who care about timings this small (e.g. mpmath) can follow such rules, or ideally write Cython directly. I wrote a mode once that was verbose about all the coercions used, I could resurrect that somewhere for more easily tracking down stuff like this. 

FWIW, I put `_mul_long` onto ModuleElement, not just RingElement. The extra indirection needed to put it in coerce.pyx will make it at least 50% or more slower, probably much more.



---

archive/issue_comments_049422.json:
```json
{
    "body": "Craig:\n\n> That said, I guess I don't understand why GMP/MPIR don't use unboxed immediate integers for small values, but given that I haven't played with the guts of the code, they probably know better than I do. It would be nice in your case, though -- you could have both counter_type and value_type be Integer. (Well, you might run into some issues when you only used small values, but in principle, anyway.) \n\nThis is actually on MPIR's list of \"development ideas\"; I think the only reason it isn't supported is that no one has written the code yet. Still, there are reasons to keep using Python ints: ints are a bit faster than custom types because they are special-cased in various places in the Python interpreter, and JITs can optimize them (psyco does a decent job with mpmath partly because of this -- maybe in the future we'll also have Unladen Swallow and PyPy).\n\n> I'm curious: is this code going to be used as part of the \"core\" of mpmath, or will you just write the code so it takes advantage of Sage whenever it's available? (My impression was that you liked mpmath being pure Python.)\n\nIt already uses sage.Integer when it's available. \n\nSince the core is fairly complex (and hence difficult to optimize), I've recently split everything cleanly into \"core\" and \"high level\" code. All the high level code can easily use different cores (or \"contexts\"). There is now both the standard multiprecision context, and a fully working machine-precision context (using float/complex) implemented in less than 300 lines of code. It should be possible to implement a light wrapper of Sage's real and complex numbers in close to 300 lines so that Sage can use all the high-level functions in mpmath \"natively\".\n\nStill, since Sage's numbers don't provide quite the same features as mpmath's core, it remains necessary to continue optimizing mpmath's core as well. This will eventually have to be done by rewriting more of it in Cython (already a few Cython helper functions are imported from Sage when available). But for now, fixing basic inefficiencies in the present code (such as this issue) seems worthwhile IMHO.",
    "created_at": "2010-01-22T19:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49422",
    "user": "https://github.com/fredrik-johansson"
}
```

Craig:

> That said, I guess I don't understand why GMP/MPIR don't use unboxed immediate integers for small values, but given that I haven't played with the guts of the code, they probably know better than I do. It would be nice in your case, though -- you could have both counter_type and value_type be Integer. (Well, you might run into some issues when you only used small values, but in principle, anyway.) 

This is actually on MPIR's list of "development ideas"; I think the only reason it isn't supported is that no one has written the code yet. Still, there are reasons to keep using Python ints: ints are a bit faster than custom types because they are special-cased in various places in the Python interpreter, and JITs can optimize them (psyco does a decent job with mpmath partly because of this -- maybe in the future we'll also have Unladen Swallow and PyPy).

> I'm curious: is this code going to be used as part of the "core" of mpmath, or will you just write the code so it takes advantage of Sage whenever it's available? (My impression was that you liked mpmath being pure Python.)

It already uses sage.Integer when it's available. 

Since the core is fairly complex (and hence difficult to optimize), I've recently split everything cleanly into "core" and "high level" code. All the high level code can easily use different cores (or "contexts"). There is now both the standard multiprecision context, and a fully working machine-precision context (using float/complex) implemented in less than 300 lines of code. It should be possible to implement a light wrapper of Sage's real and complex numbers in close to 300 lines so that Sage can use all the high-level functions in mpmath "natively".

Still, since Sage's numbers don't provide quite the same features as mpmath's core, it remains necessary to continue optimizing mpmath's core as well. This will eventually have to be done by rewriting more of it in Cython (already a few Cython helper functions are imported from Sage when available). But for now, fixing basic inefficiencies in the present code (such as this issue) seems worthwhile IMHO.



---

archive/issue_comments_049423.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-01-22T22:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49423",
    "user": "https://github.com/craigcitro"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_049424.json:
```json
{
    "body": "Robert -- looks good, just needs some doctests.",
    "created_at": "2010-01-22T22:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49424",
    "user": "https://github.com/craigcitro"
}
```

Robert -- looks good, just needs some doctests.



---

archive/issue_comments_049425.json:
```json
{
    "body": "Oh, and so I don't forget -- we also seemed to get a consensus that people wanted `Integer * int` and `int * Integer` to be fast. Fredrik, this probably means you don't have to worry too much about rewriting any code. `:)` There will probably be a **tiny** speed hit on `int * Integer` over `Integer * int`, because it has to fail on the `int`'s `__mul__` code before it will switch the args and try again.",
    "created_at": "2010-01-23T08:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49425",
    "user": "https://github.com/craigcitro"
}
```

Oh, and so I don't forget -- we also seemed to get a consensus that people wanted `Integer * int` and `int * Integer` to be fast. Fredrik, this probably means you don't have to worry too much about rewriting any code. `:)` There will probably be a **tiny** speed hit on `int * Integer` over `Integer * int`, because it has to fail on the `int`'s `__mul__` code before it will switch the args and try again.



---

archive/issue_comments_049426.json:
```json
{
    "body": "Attachment [6199-fast-int-mul.patch](tarball://root/attachments/some-uuid/ticket6199/6199-fast-int-mul.patch) by @robertwb created at 2010-01-24 08:26:04",
    "created_at": "2010-01-24T08:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49426",
    "user": "https://github.com/robertwb"
}
```

Attachment [6199-fast-int-mul.patch](tarball://root/attachments/some-uuid/ticket6199/6199-fast-int-mul.patch) by @robertwb created at 2010-01-24 08:26:04



---

archive/issue_comments_049427.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-24T08:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49427",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_049428.json:
```json
{
    "body": "OK, I've uploaded a new patch.",
    "created_at": "2010-01-24T08:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49428",
    "user": "https://github.com/robertwb"
}
```

OK, I've uploaded a new patch.



---

archive/issue_comments_049429.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-24T17:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49429",
    "user": "https://github.com/craigcitro"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_049430.json:
```json
{
    "body": "Looks good. One question, though: why do a test and use `mpz_add_ui` instead of just using `mpz_add_si`? It obviously works, I'm just wondering if you know something about the relative speed that I don't.",
    "created_at": "2010-01-24T17:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49430",
    "user": "https://github.com/craigcitro"
}
```

Looks good. One question, though: why do a test and use `mpz_add_ui` instead of just using `mpz_add_si`? It obviously works, I'm just wondering if you know something about the relative speed that I don't.



---

archive/issue_comments_049431.json:
```json
{
    "body": "oops, I tested with this fix but forgot to check it in",
    "created_at": "2010-01-31T12:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49431",
    "user": "https://github.com/robertwb"
}
```

oops, I tested with this fix but forgot to check it in



---

archive/issue_comments_049432.json:
```json
{
    "body": "Attachment [6199-fast-mul-fix.patch](tarball://root/attachments/some-uuid/ticket6199/6199-fast-mul-fix.patch) by @fredrik-johansson created at 2010-02-01 01:37:27\n\nI applied this and got roughly a 15% speedup for mpmath's test suite, with everything seemingly working, so +1 from me.",
    "created_at": "2010-02-01T01:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49432",
    "user": "https://github.com/fredrik-johansson"
}
```

Attachment [6199-fast-mul-fix.patch](tarball://root/attachments/some-uuid/ticket6199/6199-fast-mul-fix.patch) by @fredrik-johansson created at 2010-02-01 01:37:27

I applied this and got roughly a 15% speedup for mpmath's test suite, with everything seemingly working, so +1 from me.



---

archive/issue_comments_049433.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2010-02-01T21:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49433",
    "user": "https://github.com/robertwb"
}
```

apply only this patch



---

archive/issue_comments_049434.json:
```json
{
    "body": "Attachment [6199-fast-int-mul-all.patch](tarball://root/attachments/some-uuid/ticket6199/6199-fast-int-mul-all.patch) by @robertwb created at 2010-02-01 21:14:06\n\nAttached a new patch which cleans up subtraction and note about corner case.",
    "created_at": "2010-02-01T21:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49434",
    "user": "https://github.com/robertwb"
}
```

Attachment [6199-fast-int-mul-all.patch](tarball://root/attachments/some-uuid/ticket6199/6199-fast-int-mul-all.patch) by @robertwb created at 2010-02-01 21:14:06

Attached a new patch which cleans up subtraction and note about corner case.



---

archive/issue_comments_049435.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-01T21:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49435",
    "user": "https://github.com/robertwb"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_049436.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-01T21:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49436",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_049437.json:
```json
{
    "body": "The changes look good.",
    "created_at": "2010-02-02T20:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49437",
    "user": "https://github.com/mwhansen"
}
```

The changes look good.



---

archive/issue_comments_049438.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-02T20:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49438",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006449.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-02-11T14:51:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6199#event-6449"
}
```



---

archive/issue_comments_049439.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6199#issuecomment-49439",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
