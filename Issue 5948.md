# Issue 5948: Coleman integrals of df*f

Issue created by migration from https://trac.sagemath.org/ticket/5948

Original creator: jen

Original creation time: 2009-04-30 15:12:20

Assignee: robertwb

CC:  mabshoff robertwb

This is a problem arising from the computation of iterated Coleman integrals. It seems that (single) Coleman integrals of df*f for f coming from the MW-reduction are wrong.

Here's the setup:

```
sage: R.<x> = QQ['x']
sage: E= HyperellipticCurve(x^3-4*x+4)
sage: K = Qp(5,10)
sage: EK = E.change_ring(K)
sage: P = EK(2,2)
sage: Q = EK(-2,-2)
sage: P = EK.teichmuller(P)
sage: Q = EK.teichmuller(Q)
sage: import sage.schemes.elliptic_curves.monsky_washnitzer as monsky_washnitzer
sage: M_frob, forms = monsky_washnitzer.matrix_of_frobenius_hyperelliptic(EK)
sage: f = forms[0]
```


We know that int(df df,P,Q) = 1/2*int(df,P,Q)<sup>2</sup>, where the integral
on the LHS is iterated and the integral on the RHS is a usual Coleman integral. Using a single Coleman integral to compute this gives


```
sage: 1/2*EK.coleman_integral(f.diff(),P,Q)^2
3*5^2 + 5^3 + 5^4 + 5^5 + 4*5^6 + 2*5^7 + 4*5^8 + 5^9 + 3*5^10 + 4*5^11 + O(5^12)
```

We also can expand int(df df,P,Q) = f(Q)*(f(Q)-f(P)) - int(df*f,P,Q) (*)

Now let's check the things on the RHS of (*)


```
sage: EK.coleman_integral(-f.diff(),P,Q) == f(Q[0],Q[1])-f(P[0],P[1])
True
```


So the first term is computed consistently (modulo the minor problem
with f.diff() -- see #5947). The second term is the problem, and here's why:
integrating by parts, we have
int(f*df,P,Q) + int(df*f, P,Q) = f<sup>2</sup>(Q)-f<sup>2</sup>(P), which gives
int(df*f,P, Q) = 1/2*(f<sup>2</sup>(Q)-f<sup>2</sup>(P)).                   (**)

Computing the LHS of (**)  gives:


```
sage: EK.coleman_integral(-f.diff()*f,P,Q)
2*5^2 + 2*5^3 + 2*5^4 + 5^6 + 5^7 + 4*5^8 + 2*5^10 + 3*5^11 + O(5^12)
```


Computing the RHS of (**) gives

```
sage: g = f^2
sage: 1/2*(g(Q[0],Q[1])-g(P[0],P[1]))
2*5^2 + 2*5^3 + 2*5^6 + 4*5^7 + 3*5^8 + 2*5^9 + 2*5^11 + O(5^12)
```


So they're good up to 2 digits, but no more. The RHS is the correct one:


```
sage: f(Q[0],Q[1])*(f(Q[0],Q[1])-f(P[0],P[1])) -
1/2*(g(Q[0],Q[1])-g(P[0],P[1])) ==
1/2*EK.coleman_integral(-f.diff(),P,Q)^2
True
```


Thus the bug is with 


```
EK.coleman_integral(-f0.diff()*f0,P,Q)
```


I looked at the code briefly, but at first glance, it doesn't look like the coercion into MonskyWashnitzerDifferentialRing changes much :


```
sage: EK.coleman_integral(-f0.diff()*f0,P,Q,True)         #skipping
the coercion step
2*5^2 + 2*5^3 + 2*5^4 + 5^6 + 5^7 + 4*5^8 + 5^11 + O(5^12)
sage: EK.coleman_integral(-f0.diff()*f0,P,Q,False)       #the usual
2*5^2 + 2*5^3 + 2*5^4 + 5^6 + 5^7 + 4*5^8 + 2*5^10 + 3*5^11 + O(5^12)
```


So maybe it's something with the reduction?


---

Comment by kedlaya created at 2009-05-19 05:07:38

There already seems to be trouble with tiny integrals. Check this out:

```
sage: R.<x> = QQ['x']
sage: E= HyperellipticCurve(x^3-4*x+4)
sage: K = Qp(5,10)
sage: EK = E.change_ring(K)
sage: P = EK(2, 2)
sage: Q = EK.teichmuller(P)
sage: import sage.schemes.elliptic_curves.monsky_washnitzer as monsky_washnitzer
sage: M_frob, forms = monsky_washnitzer.matrix_of_frobenius_hyperelliptic(EK)
sage: f = forms[0]
sage: u = f.parent().gens()[0]
sage: u
x
sage: u.diff()
2*y*1 dx/2y
sage: EK.coleman_integral(-u.diff(), P, Q)
5 + 5^2 + 5^3 + 2*5^4 + 5^5 + 3*5^6 + 3*5^7 + 4*5^8 + O(5^10) # wrong
sage: u(Q[0], Q[1]) - u(P[0], P[1])
5 + 2*5^2 + 5^3 + 3*5^4 + 4*5^5 + 2*5^6 + 3*5^7 + 3*5^9 + O(5^10) # right


---

Comment by robertwb created at 2009-05-19 09:41:59

I think line 65 in hyperelliptic_padic_field:62 should be

```
            I = sum([f_dt[n]/(n+1) for n in xrange(f_dt.degree()+1)]) # \int_0^1 f dt
```

though this doesn't solve the issue...


---

Comment by robertwb created at 2009-05-20 06:43:42

Negation bug at #5947


---

Attachment


---

Comment by robertwb created at 2009-05-20 07:43:30

Also has fix for #5947


---

Comment by jen created at 2009-05-21 06:06:00

The patch looks good and fixes the problems I had with iterated integrals.


---

Comment by mabshoff created at 2009-05-22 14:06:17

With this patch applied to my 4.0.rc1 merge tree I get one failure:

```
mabshoff@sage:/scratch/mabshoff/sage-4.0.rc1$ ./sage -t -long devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py
sage -t -long "devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py"
**********************************************************************
File "/scratch/mabshoff/sage-4.0.rc1/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 2647:
    sage: y.diff().reduce_fast()
Expected:
    (y, (0, 0))
Got:
    (y*1, (0, 0))
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_50
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-4.0.rc1/tmp/.doctest_monsky_washnitzer.py
         [10.3 s]
exit code: 1024
```


Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-22 14:14:14

Thinking about this for a minute: This is probably due to new symbolics, but I am still hesitant to merge this until the symbolics issue is resolved. Once it is the positive review should be reinstated.

Cheers,

Michael


---

Comment by robertwb created at 2009-05-22 19:28:53

This is unrelated to the new symbolics, and the doctest should be changed. (Here the results is an element of the special hyperelliptic quotient ring, which has sub-optimal but still correct printing for trivial elements.)


---

Attachment

Here's a new patch adding the one-line fix to the doctest.


---

Comment by jen created at 2009-05-24 23:46:04

Looks great!


---

Comment by mhansen created at 2009-06-01 05:33:14

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-06-01 05:33:14

Resolution: fixed
