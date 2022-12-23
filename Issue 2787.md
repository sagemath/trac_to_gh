# Issue 2787: make the interface to integrate() like the (new consistent) interface to diff()

Issue created by migration from https://trac.sagemath.org/ticket/2787

Original creator: jason

Original creation time: 2008-04-03 02:38:39

Assignee: was

CC:  kcrisman ktkohl

It would be nice if the following worked, if f was a function:


```
sage: integrate(f, x)

sage: # Double indefinite integral wrt x
sage: integrate(f, x, x)

sage: # limits and a double integral: x is the inner integral, y is the outer integral (note that this order is backwards from Mma...they think of nested integrals as int dx int dy function, so the first parameter is the outer integral in Mma.)
sage: integrate(f, (x, 0, 1), (y, 1, 2))
sage: integrate(f, (x, 0, y), (y, 1, 2))

sage: # Double integral, x is the inner integral, y is the outer integral
sage: integrate(f, x, y)
```



---

Comment by jwmerrill created at 2008-08-31 14:40:08

See also #1221.  It would be nice if the interface here was also consistent with the interface to plot, at least when a range is specified, since both take a function, a variable, and a range.


---

Comment by jwmerrill created at 2008-09-03 02:26:28

What do you propose to do about the following case:


```
# Current behavior, definite integral with x and y as bounds
sage: var('x,y')
sage: integrate(x^2,x,x,y)
y^3/3 - x^3/3

# Triple Integral, twice with respect to x, once with respect to y
sage: integrate(x^2,x,x,y)
x^4*y/12

# i.e. same as
sage: (x^2).integrate(x).integrate(x).integrate(y)
```



---

Comment by jason created at 2008-09-04 04:41:48

As noted in #1221, I would vote with the consensus from the devel list that the syntax integrate(f, x, a, b) be deprecated in favor of integrate(f, (x, a, b)). However, you're right that this would introduce a backwards-incompatible change.


---

Comment by kcrisman created at 2011-03-16 15:36:50

Changing priority from major to minor.


---

Comment by rws created at 2014-12-15 14:18:59

Changing priority from minor to major.


---

Comment by nbruin created at 2015-05-24 19:56:11

I would say that deprecating `integral(f(x),x,a,b)` for a definite integral will be too large a backward incompatible change to pull of.

The gain for multiple integrals is also a little tricky: The proposed order for integral(f(x,y),x,y) where x is inner and y is outer is definitely consistent with mathematical notation `int int f(x,y) dx dy` but it's opposite to python's iteration order `[ (i,j) for i in range(3) for j in range(3) ]`, where j iterates in the inner loop.

Also, the proposed notation is for multiple integrals, which in mathematics are usually written as multiple (nested) integrals anyway. Single integral notation is usually reserved for higher dimensional integrals (Lebesgue, usually), in which case no particular "integration order" is implies, and indeed the domain of integration might not allow for a direct translation into nested integrals.

The fact that integral has to both accommodate definite integrals and taking antiderivatives breaks the complete symmetry with the `diff` interface. It would be nice if the interface were more symmetrical, but I think there are good reasons why it's not. If a complete converse to `diff()` is required, perhaps we need `antiderivative()`, which doesn't need to accommodate definite integrals (although of course no-one would find its existence).


---

Comment by kcrisman created at 2015-05-26 12:20:57

I think one big meta-motivation behind this is that some competitor programs may be more consistent or at least allow multiple integrals this way?  Certainly it seems much more cumbersome in Sage - plus, you have to do them in the "right order" to get nice answers sometimes, I would guess, just like in calculus textbooks :)
