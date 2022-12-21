# Issue 4432: [with patch, needs review] symbolic gamma and factorial

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2008-11-03 19:55:10

Assignee: burcin

This patches adds symbolic gamma and factorial functions.

The symbolic factorial is named fact for now, so it does not clash with sage.rings.arith.factorial


---

Comment by whuss created at 2008-11-03 20:12:54

Changing assignee from burcin to whuss.


---

Comment by whuss created at 2008-11-04 07:42:17

See also #4433


---

Comment by mhansen created at 2008-11-04 21:01:01

Some initial comments.

The first patch still need a lot of doctests added.  The docstring in the second patch just needs to be reformatted.

Also, this shouldn't go in as is with the function named 'fact'.  #4433 changes this.


---

Comment by whuss created at 2008-11-06 10:50:57

The new patch keeps the algorithm keyword for the symbolic factorial.
It also keeps the docstrings from the nonsymbolic functions, plus some new doctests.


---

Comment by mhansen created at 2008-11-06 21:03:39

I added a patch which I think presents a cleaner solution for #4432 _and_ #4433.  What are your thoughts?


---

Attachment

improvements to gamma, apply after Mike's trac_4432.patch


---

Comment by burcin created at 2008-11-15 11:59:00

The call to `RR(x).gamma()` does not match the previous behavior of the gamma function. The following doesn't work with the given patches:


```
sage: gamma(QQbar(I))
<boom>
```


attachment:trac_4432-gamma.patch fixes this, and adds a few more doctests. 

I give Mike's patch a positive review. Mike, can you check my changes?


---

Comment by mhansen created at 2008-11-21 14:45:33

+1 to Burcin's patch.

Apply only the last two patches: trac_4432.patch and trac_4432-gamma.patch


---

Comment by mabshoff created at 2008-11-23 09:21:36

Wilfried,

in the future please make sure to post mercurial patches instead of diffs. This is also an issue with the other patches you have posted that far. I will commit any diff in your name, so that proper credit goes to you.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-23 09:42:50

There are two doctest failures with this patch:

```
sage -t -long devel/sage/sage/rings/arith.py                
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/arith.py", line 3011:
    sage: falling_factorial(1+I, I)
Expected:
    0.652965496420167 + 0.343065839816545*I
Got:
    gamma(I + 2)
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/arith.py", line 3074:
    sage: rising_factorial(1+I, I)
Expected:
    0.266816390637832 + 0.122783354006372*I
Got:
    gamma(2*I + 1)/gamma(I + 1)
**********************************************************************
```

Sounds like this will be easy to fix. I would also like to see if there are any performance regressions with this patch.

Cheers,

Michael


---

Comment by whuss created at 2008-11-24 15:43:48

Michael,

I probably have to read the Mercurial documentation.

I'm not sure if I measure the performance correctly, but if I do


```
def f(n):
    s = 0
    for i in xrange(n):
        s += factorial(2^i)
    return s.ndigits()

def g(n):
    s = 0
    for i in xrange(n):
        s += gamma((1.8)^i)
    return s

def h(n):
    set_random_seed(0)
    s = 0
    for i in xrange(n):
        s += gamma(random())
    return s

timeit('f(22)')
timeit('g(22)')
timeit('h(10^4)')
```


I get the following:

on sage-3.2 without the patch

```
5 loops, best of 3: 10.9 s per loop
125 loops, best of 3: 4.16 ms per loop
5 loops, best of 3: 5.38 s per loop
```


with trac_4432.patch

```
5 loops, best of 3: 10.9 s per loop
125 loops, best of 3: 4.18 ms per loop
5 loops, best of 3: 1.67 s per loop
```


with trac_4432.patch + trac_4432-gamma.patch

```
5 loops, best of 3: 10.9 s per loop
125 loops, best of 3: 4.17 ms per loop
5 loops, best of 3: 5.45 s per loop
```


So trac_4432.patch is much faster for small values of the gamma function
because we are not computing over the complex numbers.

Also only with trac_4432.patch

```
plot(gamma, 1, 4)
```

works. But this also doesn't work with the current code.

Greetings,

Wilfried


---

Comment by whuss created at 2008-11-24 16:09:07

make plotting of the gamma function work, fix doctests, apply after burchin's trac_4432-gamma.patch


---

Attachment

I fixed the doctests and the plotting of the gamma function, with
attachment:trac_4432-plot-doc.patch.

Also


```
sage: timeit('h(10^4)')
5 loops, best of 3: 1.68 s per loop
```


Greetings,

Wilfried


---

Comment by mhansen created at 2008-11-28 07:26:09

Looks good.


---

Comment by mhansen created at 2008-11-28 08:05:56

Apply all of the above patches.


---

Comment by mabshoff created at 2008-11-28 08:36:00

Resolution: fixed


---

Comment by mabshoff created at 2008-11-28 08:36:00

Merged all three patches in Sage 3.2.1.rc0
