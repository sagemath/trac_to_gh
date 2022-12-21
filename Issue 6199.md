# Issue 6199: Integer * int is slow

Issue created by migration from Trac.

Original creator: fredrik.johansson

Original creation time: 2009-06-03 18:44:59

Assignee: somebody

CC:  robertwb


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


---

Comment by robertwb created at 2009-06-05 11:13:14

We could make an action on Integers by ints.


---

Comment by craigcitro created at 2010-01-21 00:22:50

So sadly, I think this is a wontfix. I tested this out, and at the expense of some ugly code, we get roughly a factor of 2 speedup -- and that's basically the best we can do. The problem is that the coercion model needs to look up a cached map to avoid the coercion to `Integer`; looking up this map and calling it takes long enough that a factor of 2 is the best we can get.

Fredrik, did you have code that was getting slowed down by this? Would a factor of two on this make a big difference for you?


---

Comment by craigcitro created at 2010-01-21 00:22:50

Resolution: wontfix


---

Comment by fredrik.johansson created at 2010-01-21 02:36:27

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

Comment by craigcitro created at 2010-01-22 06:57:13

Resolution changed from wontfix to 


---

Comment by craigcitro created at 2010-01-22 06:57:13

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

In the case that it's not `Integer * int`, it's one test of a C `int` being nonzero and between two and four extra pointer comparisons on any call to `bin_op`. Mind you, that's going to happen for *every* binary arithmetic operation where the parents aren't identical, which is definitely a hefty price if you live in a world where you don't multiply `Integer * int` very often. I think we could eliminate the C `int` test, if we were crafty.

(Side note: I got a ~10% performance regression on the `a*y` line above between 4.2 and 4.3 -- do either of you have both installed to try it out?)

Robert, what are your thoughts? I know that "Special cases aren't special enough to break the rules," and in general I don't like special-casing things. Plus, it's potentially less significant with Py3 on the horizon. But if it's really going to be a showstopper for Fredrik, we should at least think about it more. It's not like there are very many types where the operations are noticeably faster than a few lookups, so it's not opening a loophole that could be abused very much, I think.


---

Comment by craigcitro created at 2010-01-22 06:57:13

Changing status from closed to new.


---

Comment by robertwb created at 2010-01-22 08:29:06

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

Comment by robertwb created at 2010-01-22 08:29:06

Changing status from new to needs_info.


---

Comment by fredrik.johansson created at 2010-01-22 11:49:24

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

Comment by mvngu created at 2010-01-22 14:45:04

So what is the milestone for this ticket? Is it still a "wontfix"?


---

Comment by craigcitro created at 2010-01-22 18:15:06

Robert:

I think there are several places we could put the code -- if nothing else, it might be nice to keep it in `coerce.pyx`, so that it's the one place where all the "rules" for coercion appear. Also, if we ultimately wanted to implement such a pathway for something that isn't a `RingElement` (which is the `__mul__` we're going to need to put the code in), the code would be in the same place. 

Also, I'd prefer to just go ahead and implement it for arithmetic on both sides -- we can do two type comparisons as `PY_TYPE_CHECK_EXACT`, and if need be, tell the branch predictor that they're unlikely (because they are in the general case, I think). I'm always suspicious of rules like "keep the Python int on the right, because that's 10X faster." I'd also hate to have to make a comment in a patch review saying "oh, this speeds up by a factor of 10 if you reverse the order of operands." I know these things exist elsewhere -- but that's no reason to add one more to the pile.  Plus, it's sure to lead to a ton of posts on the mailing list about it, where people think they've found a new "bug." `:)`

I suspect you're going to be on campus in a few hours -- we can chat about this then.

Fredrik: 

That's a really good use-case. That said, I guess I don't understand why GMP/MPIR don't use unboxed immediate integers for small values, but given that I haven't played with the guts of the code, they probably know better than I do. It would be nice in your case, though -- you could have both `counter_type` and `value_type` be `Integer`. (Well, you might run into some issues when you only used small values, but in principle, anyway.)

I'm curious: is this code going to be used as part of the "core" of mpmath, or will you just write the code so it takes advantage of Sage whenever it's available? (My impression was that you liked mpmath being pure Python.)


---

Comment by robertwb created at 2010-01-22 19:22:14

Multiplication on the left has less to gain, as it's going to try to call int.__mul__ before falling back to this code. Do you think it's worth doubling the general case penalty to support a smaller relative gain? People who care about timings this small (e.g. mpmath) can follow such rules, or ideally write Cython directly. I wrote a mode once that was verbose about all the coercions used, I could resurrect that somewhere for more easily tracking down stuff like this. 

FWIW, I put `_mul_long` onto ModuleElement, not just RingElement. The extra indirection needed to put it in coerce.pyx will make it at least 50% or more slower, probably much more.


---

Comment by fredrik.johansson created at 2010-01-22 19:54:14

Craig:

> That said, I guess I don't understand why GMP/MPIR don't use unboxed immediate integers for small values, but given that I haven't played with the guts of the code, they probably know better than I do. It would be nice in your case, though -- you could have both counter_type and value_type be Integer. (Well, you might run into some issues when you only used small values, but in principle, anyway.) 

This is actually on MPIR's list of "development ideas"; I think the only reason it isn't supported is that no one has written the code yet. Still, there are reasons to keep using Python ints: ints are a bit faster than custom types because they are special-cased in various places in the Python interpreter, and JITs can optimize them (psyco does a decent job with mpmath partly because of this -- maybe in the future we'll also have Unladen Swallow and PyPy).

> I'm curious: is this code going to be used as part of the "core" of mpmath, or will you just write the code so it takes advantage of Sage whenever it's available? (My impression was that you liked mpmath being pure Python.)

It already uses sage.Integer when it's available. 

Since the core is fairly complex (and hence difficult to optimize), I've recently split everything cleanly into "core" and "high level" code. All the high level code can easily use different cores (or "contexts"). There is now both the standard multiprecision context, and a fully working machine-precision context (using float/complex) implemented in less than 300 lines of code. It should be possible to implement a light wrapper of Sage's real and complex numbers in close to 300 lines so that Sage can use all the high-level functions in mpmath "natively".

Still, since Sage's numbers don't provide quite the same features as mpmath's core, it remains necessary to continue optimizing mpmath's core as well. This will eventually have to be done by rewriting more of it in Cython (already a few Cython helper functions are imported from Sage when available). But for now, fixing basic inefficiencies in the present code (such as this issue) seems worthwhile IMHO.


---

Comment by craigcitro created at 2010-01-22 22:42:35

Changing status from needs_info to needs_work.


---

Comment by craigcitro created at 2010-01-22 22:42:35

Robert -- looks good, just needs some doctests.


---

Comment by craigcitro created at 2010-01-23 08:05:50

Oh, and so I don't forget -- we also seemed to get a consensus that people wanted `Integer * int` and `int * Integer` to be fast. Fredrik, this probably means you don't have to worry too much about rewriting any code. `:)` There will probably be a *tiny* speed hit on `int * Integer` over `Integer * int`, because it has to fail on the `int`'s `__mul__` code before it will switch the args and try again.


---

Attachment


---

Comment by robertwb created at 2010-01-24 08:27:30

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-01-24 08:27:30

OK, I've uploaded a new patch.


---

Comment by craigcitro created at 2010-01-24 17:45:16

Changing status from needs_review to positive_review.


---

Comment by craigcitro created at 2010-01-24 17:45:16

Looks good. One question, though: why do a test and use `mpz_add_ui` instead of just using `mpz_add_si`? It obviously works, I'm just wondering if you know something about the relative speed that I don't.


---

Comment by robertwb created at 2010-01-31 12:06:21

oops, I tested with this fix but forgot to check it in


---

Attachment

I applied this and got roughly a 15% speedup for mpmath's test suite, with everything seemingly working, so +1 from me.


---

Comment by robertwb created at 2010-02-01 21:13:02

apply only this patch


---

Attachment

Attached a new patch which cleans up subtraction and note about corner case.


---

Comment by robertwb created at 2010-02-01 21:14:06

Changing status from positive_review to needs_work.


---

Comment by robertwb created at 2010-02-01 21:14:31

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-02-02 20:00:28

The changes look good.


---

Comment by mhansen created at 2010-02-02 20:00:28

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 14:51:39

Resolution: fixed
