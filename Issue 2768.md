# Issue 2768: add comparison operators to the fast_float mechanism

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-02 05:47:22

Assignee: was

make it so that comparisons work too: return 0.0 if false, 1.0 if true.


---

Comment by jason created at 2008-04-02 06:32:36

Some timings:

original

```
sage: var('x y')
(x, y)
sage: eq=x<y
sage: %timeit eq(x=2, y=3)
10 loops, best of 3: 54.6 µs per loop
```


fast_float (after applying patch)

```
sage: var('x y')
(x, y)
sage: eq=x<y
sage: f=eq._fast_float_('x','y')
sage: %timeit f(2,3)
1000000 loops, best of 3: 422 ns per loop
```

and even with the overhead of converting back to bool

```
sage: %timeit bool(f(2,3))
1000000 loops, best of 3: 721 ns per loop
```



---

Comment by jason created at 2008-04-02 06:45:33

One more comparison:


```
sage: var('x y')
(x, y)
sage: x._fast_float_('x')
<sage.ext.fast_eval.FastDoubleFunc object at 0xa02a95c>
sage: f=x._fast_float_('x')
sage: g=y._fast_float_('y')
sage: f(2)<g(3)
True
sage: %timeit f(2)<g(3)
1000000 loops, best of 3: 723 ns per loop
```


So this could have been implemented without touching the fast_float code.  However, if I want just the floating point 0.0 and 1.0 values, this patch still wins.


---

Comment by jason created at 2008-04-02 06:51:21

More timings:


```
sage: sage: var('x y')
(x, y)
sage: sage: eq=x<y
sage: sage: f=eq._fast_float_('x','y')
sage: sage: %timeit f(2,3)
1000000 loops, best of 3: 438 ns per loop
sage: xin=RDF(2); yin=RDF(2)
sage: sage: %timeit f(xin,yin)
1000000 loops, best of 3: 499 ns per loop
sage: xin=float(2); yin=float(2);
sage: sage: %timeit f(xin,yin)
1000000 loops, best of 3: 389 ns per loop
```



---

Attachment


---

Comment by jason created at 2008-04-02 08:04:34

For a nice example of this patch being used, see #2770.


---

Comment by robertwb created at 2008-04-02 17:39:50

The code is nice and clean, but I don't think it should be applied. Expressions and equations are not interchangeable, and this can lead to some strange results. 


```
sage: f = (x == 1)
sage: g = (1 == x)
sage: bool(f+g)
True
sage: ff = f._fast_float_('x') + g._fast_float_('x')
sage: ff(0)
0.0
sage: ff(1)
2.0
sage: ff(2)
0.0
sage: list(ff)
['load 0', 'push 1.0', 'eq', 'push 1.0', 'load 0', 'eq', 'add']
```


Really, I think what should be implemented is piecewise functions for fast float, which would allow one to do things like #2770 nicely. One could also create a specialized wrapper that could handle the semantics of the two sides of the equations correctly (and maybe even do short-circuiting on the first false expression).


---

Comment by dmharvey created at 2008-05-01 06:13:10

What's happening with this ticket? It's been asleep for a month. Is there still further discussion, or is that code being withdrawn?


---

Comment by jason created at 2008-05-01 12:31:23

I've been busy and it's still on my todo list.  If someone wants to take it up, feel free.  Robert Bradshaw and I agreed on a compromise on sage-devel.


---

Comment by jason created at 2008-05-06 23:34:30

See http://groups.google.com/group/sage-devel/browse_thread/thread/861d35160afebfe6/14226ae55d50b7be?lnk=gst&q=fast_float#14226ae55d50b7be for Robert's approval, modulo removing the code from symbolic things.


---

Comment by jason created at 2008-05-06 23:44:05

Apply instead of the previous patch


---

Attachment

I updated the patch to remove the code in equations.py, per Robert's request.  Eventually it would be nice to have a SymbolicProposition class or something like that that would allow for easy characteristic functions (using this code to efficiently test for set membership up to certain numerical precision).


---

Comment by robertwb created at 2008-05-07 02:38:04

Yep, this looks good.


---

Comment by mabshoff created at 2008-05-07 08:35:41

Resolution: fixed


---

Comment by mabshoff created at 2008-05-07 08:35:41

Merged trac-2768-fast-float-cmp-2.patch in Sage 3.0.2.alpha0
