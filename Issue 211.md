# Issue 211: speed up polynomial root finding

Issue created by migration from https://trac.sagemath.org/ticket/211

Original creator: was

Original creation time: 2007-01-23 23:15:09

Assignee: somebody


```
On Tue, 23 Jan 2007 14:09:56 -0800, Kiran S. Kedlaya <kedlaya@mit.edu> wrote:
 
> Here's a benchmark I just tried, which annoys me.
>  
> sage: def test1():
> ....:     P.<x> = PolynomialRing(RationalField())
> ....:     t = x^8 - 11*x^7 + x^5 - 1
> ....:     for _ in xrange(1000):
> ....:         t.complex_roots()
> ....:
> sage: time test1()
> CPU times: user 6.78 s, sys: 0.02 s, total: 6.80 s
> Wall time: 6.80
> sage: def test2():
> ....:     t = pari("x^8 - 11*x^7 + x^5 - 1")
> ....:     for _ in xrange(1000):
> ....:          t.polroots()
> ....:
> sage: time test2()
> CPU times: user 6.15 s, sys: 0.00 s, total: 6.15 s
> Wall time: 6.15
> sage: %magma
> magma: procedure test3()
> magma:     P<x> := PolynomialRing(RealField(53));
> magma:     u := x^8 - 11*x^7 + x^5 - 1;
> magma:     for i := 1 to 1000 do
> magma:         t := Roots(u);
> magma:     end for;
> magma: end procedure;
> magma: time test3();
>  Time: 1.200
>  
> The thing that bugs me is that Magma does not have some fancy
> proprietary algorithm for finding roots of a univariate polynomial; it
> uses PARI! So why are we so much slower?
 
Why do you think MAGMA uses PARI for this?  (And this isn't so much
a problem with SAGE but with PARI....  Try the same computation
directly in PARI and it is just as slow.)
 
If you really want the answer to only 53-bits precision, by the way,
numpy can do it much much faster than MAGMA. For example,
 
sage: import numpy
sage: f = numpy.array([1,-11,0,1,0,0,0,0,-1]))
sage: numpy.roots(f)
sage: array([ 10.99172314+0.j        ,  -0.72174425+0.j        ,
         -0.45332013+0.53432014j,  -0.45332013-0.53432014j,
          0.66182264+0.30451078j,   0.66182264-0.30451078j,
          0.15650805+0.67766101j,   0.15650805-0.67766101j])
sage: time v=[numpy.roots(f) for _ in range(1000)]
CPU times: user 0.28 s, sys: 0.00 s, total: 0.28 s
Wall time: 0.28
 
That's already about 5 times faster than MAGMA.  And I bet
that on larger degree numpy beats MAGMA by a lot more...
 
SAGE doesn't use numpy for root finding yet, partly because
numpy was added to SAGE only very recently, and I haven't
touched the root finding code in a while.
 
William
```



---

Comment by rlm created at 2007-08-18 19:25:14

In light of bug #442, this might be bad -- factoring input precise to 53 bits gives output precise to about 5 bits.


---

Comment by rlm created at 2007-08-18 20:33:01

In other words, numpy's speed is probably coming from its lack of accuracy. GSL gives highly accurate results, at least in the example given here:

http://www.gnu.org/software/gsl/manual/html_node/Roots-of-Polynomials-Examples.html


---

Comment by rlm created at 2007-08-18 20:36:57

in sage-2.8.1/local/lib/python2.5/site-packages/numpy/lib/polynomial.py, line 116 appears to be casting whatever float type is given to just float. This might be why numpy is giving inaccurate output.


---

Comment by mabshoff created at 2007-10-21 12:52:45

Carl Witty and John Voight have done some work in this area, so we should discuss what has been done and needs to be done (if any)

Cheers,

Michael


---

Comment by cwitty created at 2007-11-03 17:46:52

Changing assignee from somebody to cwitty.


---

Comment by cwitty created at 2007-11-03 17:46:52

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-25 18:27:17

Fixed by cwitty's code that went into 2.8.12.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-25 18:27:17

Resolution: fixed
