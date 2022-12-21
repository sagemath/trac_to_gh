# Issue 3622: numerical fast integration using fast float

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-09 00:35:13

Assignee: robertwb

When you create a symbolic expression and numerically integrate it, Sage should use
the fast_float framework to do this (a bazzilion times!) faster than it does right now.


---

Attachment


---

Comment by ncalexan created at 2008-08-11 06:26:22

I would like to see tests that show that functionality is not lost, such as

```
sage: numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)
(3.333333333333333, 3.7007434154171883e-14)
sage: numerical_integral(sin(x)^3 + sin(x),  0, pi)
(3.333333333333333, 3.7007434154171883e-14)
```


Also, this does not always win.  I think that it is worthwhile, but is there a heuristic that should be applied sometimes?


```
sage: timeit('numerical_integral(sin(x)^3 + sin(x),  0, pi)')
25 loops, best of 3: 23.4 ms per loop
sage: timeit('numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)')
625 loops, best of 3: 900 Âµs per loop
sage: timeit('numerical_integral(cos(x)^7 + sin(x^11 + x),  0, pi)')
25 loops, best of 3: 33.5 ms per loop
sage: timeit('numerical_integral(lambda x: cos(x)^7 + sin(x^11 + x),  0, pi)')
5 loops, best of 3: 164 ms per loop
```


Finally, the following is just wrong:


```
sage: timeit('numerical_integral(lambda x: 0,  0, pi)')
625 loops, best of 3: 86.7 Âµs per loop
sage: timeit('numerical_integral(0,  0, pi)')
'sage.rings.integer.Integer' object is not callable
... repeated a few thousand times ...
'sage.rings.integer.Integer' object is not callable
5 loops, best of 3: 42.8 ms per loop
```



---

Comment by robertwb created at 2008-08-11 16:51:13

> I would like to see tests that show that functionality is not lost

Good point. 

> Also, this does not always win...


```
sage: f = lambda x: sin(x)^3 + sin(x)
sage: timeit('numerical_integral(f, 0, pi)')
625 loops, best of 3: 856 µs per loop
sage: f = sin(x)^3 + sin(x)
sage: timeit('numerical_integral(f, 0, pi)')
25 loops, best of 3: 15 ms per loop
sage: f = f._fast_float_(x)
sage: timeit('numerical_integral(f, 0, pi)')
625 loops, best of 3: 126 µs per loop
```


I guess we'll have to optimize the fast_float construction... I'll look into this more. 

> Finally, the following is just wrong:

Hmm... I'll look into this.


---

Comment by jwmerrill created at 2008-08-31 14:54:00

This is a duplicate of #2881, although maybe we should keep this version since it has comments and a patch.


---

Attachment

updated


---

Comment by robertwb created at 2008-09-02 03:49:37

one more optimization


---

Attachment

I added some more documentation to show that the old behavior is not lost. I also fixed it so constant functions work (that never worked before either, but it was an easy fix). 

Fast float construction has been optimized in the meantime, so now it's always faster. 


```
sage: f = lambda x: sin(x)^3 + sin(x)
sage: timeit('numerical_integral(f, 0, pi)')
625 loops, best of 3: 869 µs per loop
sage: f = sin(x)^3 + sin(x)
sage: timeit('numerical_integral(f, 0, pi)')
5 loops, best of 3: 134 µs per loop
```


(Note that `timeit('numerical_integral(sin(x)^3 + sin(x),  0, pi)')` is a bit unfair because it constructs the symbolic expression every loop, but this isn't a typical use case anyways...)


---

Comment by jwmerrill created at 2008-09-02 04:07:29

I'm curious how things compare when you put the lambda function in the loop vs putting the symbolic expression in the loop..  i.e.


```
sage: timeit('numerical_integral(lambda x: sin(x)^3 + sin(x), 0, pi)')
# vs.
sage: timeit('numerical_integral(sin(x)^3 + sin(x), 0, pi)')
```


If the construction of the fast float takes a long time compared to doing the whole integral with a lambda function, then this might not be a win.


---

Comment by jwmerrill created at 2008-09-02 04:26:26

I applied the last patch and gave it a try.  Here are the results:


```
sage: timeit('numerical_integral(lambda x: sin(x)^3 + sin(x), 0, pi)')
625 loops, best of 3: 1.09 ms per loop
sage: timeit('numerical_integral(sin(x)^3 + sin(x), 0, pi)')
5 loops, best of 3: 16.5 ms per loop
```


So at least in this example, the time to construct the fast_float function actually swamps the whole calculation using the faster to create but slower to evaluate lambda function.


---

Comment by robertwb created at 2008-09-02 04:28:58

The construction of the fast float object is now fast. This *is* included in the timings above (and is the bulk of the 134 microseconds). If we create the fast float item ahead of time we get 


```
sage: f = sin(x)^3 + sin(x)
sage: ff = f._fast_float_('x')
sage: timeit('numerical_integral(ff, 0, pi)')
625 loops, best of 3: 41.4 µs per loop
```


The problem in the loop you give is that it is recreating the symbolic expression sin(x)^3 + sin(x) every time, which is taking all the time, but that's not a typical use case.


---

Comment by jwmerrill created at 2008-09-02 05:22:00

Okay, I get it now.  Sorry to make you explain again.  Here are some more timings:


```
sage: timeit('e = lambda x: sin(x)^3 + sin(x)')
625 loops, best of 3: 288 ns per loop
sage: timeit('e = sin(x)^3 + sin(x)')
625 loops, best of 3: 103 µs per loop
sage: timeit("e._fast_float_('x')")
625 loops, best of 3: 49 µs per loop
sage: timeit('e._fast_float_()') #way slower
5 loops, best of 3: 96.3 ms per loop
sage: timeit("numerical_integral(e,0,pi)")
625 loops, best of 3: 111 µs per loop
sage: timeit("numerical_integral(sin(x)^3 + sin(x),0,pi)")
25 loops, best of 3: 25.6 ms per loop
```


Apparently it only takes 100 microseconds to create `sin(x)^3 + sin(x)`, 50 microseconds to turn it into a fast float, and 100 microseconds to execute the integration once that's done.  So when I put the function creation inside the loop, I would expect about 250 microseconds.  Where is the other 25.4 ms going?

That question aside, I'm now convinced this patch is a good idea, and the tests pass, so I gave it positive review.


---

Comment by robertwb created at 2008-09-02 05:35:38

That is a really good question. It's probably because something, somewhere, is caching something (but I've looked in the obvious places and I don't see what). But, as you said, that's orthogonal to the patch. Thanks for looking into this.


---

Comment by jwmerrill created at 2008-09-02 05:58:24

I think I found what is going on.  For a symbolic expression, the variables get cached after the first call to self.variables() or self.arguments().


```
sage: timeit('(sin(x)^3 + sin(x)).variables()')
25 loops, best of 3: 16.9 ms per loop
sage: f = sin(x)^3 + sin(x)
sage: timeit('f.variables()')
625 loops, best of 3: 6.61 µs per loop
```


I wonder if there's a way to speed up the first call to self.variables(), maybe in the special case that there is only one variable or something.


---

Comment by jwmerrill created at 2008-09-02 06:18:55

I did a little bit more searching, and it looks like the slow part of the first call to variables() is that the expression must be simplified to know the variables, and the simplification is farmed out to maxima.  So possibly this will get a lot faster once pynac gets integrated and simplify calls can be routed there.


---

Comment by robertwb created at 2008-09-02 07:18:50

Excellent. When I saw it was a matter of milliseconds, maxima slowness went under the radar for me (it's often worse than that, going through pexpect and all), but it looks like you're right. And it's a relief that it'll get faster. Thanks for tracking this down.


---

Comment by mabshoff created at 2008-09-02 10:11:04

Merged 3622-fast_float_integration.3.patch  in Sage 3.1.2.alpha4


---

Comment by mabshoff created at 2008-09-02 10:11:04

Resolution: fixed
