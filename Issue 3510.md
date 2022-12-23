# Issue 3510: sage charpoly woefully slower than Mma's for small integer matrices

Issue created by migration from https://trac.sagemath.org/ticket/3510

Original creator: jason

Original creation time: 2008-06-25 14:02:28

Assignee: was

CC:  schilly

This timing difference ought to be fixed...


```
sage: mathematica("time[expr_, reps_] := Timing[Do[ClearSystemCache[]; expr;, >
Null
sage: mathematica("time[expr_, reps_] := Timing[Do[ClearSystemCache[]; expr;, {reps}]][[1]]/reps")                                                              
Null
sage: mathematica("SetAttributes[time, HoldFirst]")                                                                                              
Null
sage: a=[random_matrix(ZZ,i,x=2^16) for i in xrange(50)]                  
sage: a=[random_matrix(ZZ,i,x=2^16) for i in xrange(25)]
sage: a=[random_matrix(ZZ,i,x=2^16) for i in xrange(1,25)]
sage: b=[mathematica(i) for i in a]                                                                                                                             
sage: mma_timings=[mathematica("time[CharacteristicPolynomial[%s,t],20]"%(m._name)) for m in b]                                                                 
sage: sage_timings=[timeit("a[i].charpoly(); a[i]._clear_cache()") for i in xrange(len(a))]                                                                     
125 loops, best of 3: 989 µs per loop
125 loops, best of 3: 2.83 ms per loop
25 loops, best of 3: 3.37 ms per loop
25 loops, best of 3: 3.99 ms per loop
25 loops, best of 3: 4.18 ms per loop
25 loops, best of 3: 4.18 ms per loop
25 loops, best of 3: 5.73 ms per loop
25 loops, best of 3: 6.66 ms per loop
25 loops, best of 3: 8.36 ms per loop
25 loops, best of 3: 8.57 ms per loop
25 loops, best of 3: 9.41 ms per loop
25 loops, best of 3: 11.6 ms per loop
25 loops, best of 3: 13.3 ms per loop
25 loops, best of 3: 13.3 ms per loop
25 loops, best of 3: 16.2 ms per loop
5 loops, best of 3: 17.9 ms per loop
5 loops, best of 3: 21.1 ms per loop
5 loops, best of 3: 24.6 ms per loop
5 loops, best of 3: 24.7 ms per loop
5 loops, best of 3: 28.4 ms per loop
5 loops, best of 3: 30.4 ms per loop
5 loops, best of 3: 33.2 ms per loop
5 loops, best of 3: 36.2 ms per loop
5 loops, best of 3: 36.6 ms per loop
sage: mma_timings 

[0.0004000500000010843,
 0.00019999999999930075,
 0.0004000000000011883,
 0.000600049999999279,
 0.0008000499999993819,
 0.0012001000000004176,
 0.0016001000000006246,
 0.0026001499999989217,
 0.004000250000001096,
 0.005000299999999682,
 0.007600499999999302,
 0.009800600000001224,
 0.014000900000001421,
 0.01760109999999937,
 0.021401350000000537,
 0.02840180000000124,
 0.03700230000000092,
 0.046602900000000586,
 0.058003650000001405,
 0.07060440000000084,
 0.08600534999999886,
 0.10280644999999965,
 0.12460779999999874,
 0.14660915000000047]
```




---

Comment by jason created at 2008-06-25 14:03:32

Wait...something seems wrong with my comparison...


---

Comment by jason created at 2008-06-25 14:11:15

Nope; Mma beats up through 10 vertices, it seems.  We're fine after that, though.


---

Comment by jason created at 2008-06-25 14:11:23

Changing priority from major to minor.


---

Comment by kedlaya created at 2017-09-23 02:49:04

I don't have access to Mathematica for comparison, but I just tried this in Sage and the timings seem to be much better than before. Can someone do a direct comparison to see if this ticket is still valid?

```
sage: a=[random_matrix(ZZ,i,x=2^16) for i in xrange(1,25)]
sage: sage_timings=[timeit("a[i].charpoly(); a[i]._clear_cache()") for i in xrange(len(a))]                                                                     
625 loops, best of 3: 721 µs per loop
625 loops, best of 3: 732 µs per loop
625 loops, best of 3: 798 µs per loop
625 loops, best of 3: 847 µs per loop
625 loops, best of 3: 909 µs per loop
625 loops, best of 3: 982 µs per loop
625 loops, best of 3: 1.1 ms per loop
625 loops, best of 3: 1.15 ms per loop
625 loops, best of 3: 1.32 ms per loop
625 loops, best of 3: 1.44 ms per loop
625 loops, best of 3: 1.57 ms per loop
125 loops, best of 3: 1.72 ms per loop
125 loops, best of 3: 1.99 ms per loop
125 loops, best of 3: 2.07 ms per loop
125 loops, best of 3: 2.38 ms per loop
125 loops, best of 3: 2.56 ms per loop
125 loops, best of 3: 2.95 ms per loop
125 loops, best of 3: 3.06 ms per loop
125 loops, best of 3: 3.48 ms per loop
125 loops, best of 3: 3.77 ms per loop
125 loops, best of 3: 4.27 ms per loop
125 loops, best of 3: 4.65 ms per loop
125 loops, best of 3: 5.05 ms per loop
125 loops, best of 3: 5.39 ms per loop
```

