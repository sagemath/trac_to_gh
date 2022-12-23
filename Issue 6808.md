# Issue 6808: Implement a benchmark based on Karl Unterkofler's Mathematica benchmark

Issue created by migration from https://trac.sagemath.org/ticket/6808

Original creator: drkirkby

Original creation time: 2009-08-22 22:20:35

Assignee: cwitty

CC:  schilly

Keywords: benchmark

Karl Unterkofler has implemented various benchmarks for Mathematica. These are for specific versions of MMA 2.2, 3, 4, 5 6 and 7. 

http://www2.staff.fh-vorarlberg.ac.at/~ku/karl/timings70.html

Making one for Sage comparable to his latest Mathematica 7 benchmark would be useful, as it would allow a direct comparison of Sage and Mathematica on 15 specific tests. 

We have Karl's permission to do this. In an email send to me today it said:


*-- Email from Karl Unterkofler to David Kirkby August 22nd 2009 ---*


_Dear Dave,_

_the aim of my MMA benchmark is to give Mathematica users a decision support which platform is most suitable for their needs, e.g., should one use Vista or XP?, can one use Linux or Mac OS X?, which processor should one use 32- or 64-bit?, etc._

_Some time ago (1994) I also made a corresponding Maple benchmark (google: "Comparison of Mathematica on Various Computers") but there wasn't enough input from other users to keep this ongoing._

_I had to update the benchmark for new versions of MMA for several reasons, speed improvements, syntax changes, bugs, parallelization, etc., though I tried to keep as much as possible from the old code._

''I have no problem if you adopt my benchmark for use with Sage.
However a  reference to the original source would be nice.''

_Karl_




---

Comment by drkirkby created at 2010-08-29 01:29:13

I thought it work putting alist of the thing Karl'sbenchmark does.


```
Following calculations are performed

   1. Timing[N[Pi, 5000000]]][[1]]
   2. Timing[N[Sin[1/2], 3000000]][[1]]
   3. Timing[10000000!][[1]]
   4. Timing[FactorInteger[2^256 - 1]][[1]]
   5. Timing[PrimeQ[2^19937 - 1]][[1]]
   6. Timing[Eigenvalues[Table[Random[], {1200}, {1200}]]][[1]]
   7. Timing[Nest[BesselJ[0, #] &, 2, 11000]][[1]]
   8. Timing[Table[Together[c[k]], {k, 4, 24}]][[1]]
   9. Timing[Integrate[1/(1 + x^1005), x]][[1]]
  10. Timing[Table[N[WeierstrassP[n, {1, 1}]], {n, 40000}]][[1]]
  11. Sum[2 / Pi Integrate[Log[2 Cos[x/2]] * Cos[n x], {x, 0, Pi}], {n, 0, 15}]][[1]]
  12. Timing[Sum[HermiteH[n, z], {n, 1500}]][[1]]
  13. Timing[Expand[(a1 + a2 + a3 + a4 + a5 + a6 + a7)^29]][[1]]
  14. Timing[LinearSolve[RandomReal[{0, 1}, {6000, 6000}], RandomReal[{0, 1}, 6000]]][[1]]
  15. Timing[Eliminate[{a0*b0 == g0, a1*b0 + a0*b1 == g1,
      a2*b0 + 2*a1*b1 + a0*b2 == g2,
      3*a2*b1 + 3*a1*b2 - q1*g1 - g0*q11 == g3,
      -3*z*(a1*b0 - a0*b1) - q1*g2 - 7/2*q11*g1 - g0*q12 + 6*a2*b2 - 6*a1*b1*q1 == g4,
      g2 - 3*a1*b1 + q1*g0 == -1}, {a0, a1, a2, b0, b1, b2}]][[1]] 

where
c[2]   := c2; c[3] := c3; 
c[k_]  := 3/((2*k + 1)*(k - 3))*Sum[c[m]*c[k - m], {m, 2, k - 2}];
```



---

Comment by jason created at 2010-08-29 02:28:32

See http://www.mail-archive.com/sage-devel`@`googlegroups.com/msg27249.html for a long thread about this.
