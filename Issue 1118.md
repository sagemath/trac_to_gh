# Issue 1118: cputime should include the cpu times of all subprocesses

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-11-07 13:57:55

Assignee: was

Paul Zimmermann wrote:
"""
It seems the cpu time reported by SAGE does not include that of the spawned
processes


```
mermoz% sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.10, Release Date: 2007-10-28                      |
| Type notebook() for the GUI, and license() for information.        |
sage: p=65257526772644948764799212887702573391887715235981530343703506731
sage: time FindGroupOrder(p,489731259)
CPU times: user 0.87 s, sys: 0.07 s, total: 0.94 s
Wall time: 70.30
2^2 * 3^2 * 7 * 13 * 5521 * 589213 * 1103171 * 1149307 * 1310261 * 10091759 * 63065897 * 120597437 * 48024231181
```

I doubt the given cpu times take into account the PARI/GP computations. As a  comparison, Magma takes 55s for that computation on my computer.

The wall time is not very useful (my machine has a load of 3-4). It would be more useful to have to cpu time used by the spawned processes, or simply the total cpu time used by SAGE and those processes.
"""

Thus we should figure out how to do this in a portable way. May the POSIX gurus speak up!


---

Comment by malb created at 2007-11-07 14:42:54

I forgot to include the actual code that was run.


```
def FindGroupOrder(p,s):
   K = GF(p)
   v = K(4*s)
   u = K(s^2-5)
   x = u^3
   b = 4*x*v
   a = (v-u)^3*(3*u+v)
   A = a/b-2
   x = x/v^3
   b = x^3 + A*x^2 + x
   E = EllipticCurve(K,[0,b*A,0,b^2,0])
   return factor(E.cardinality())
```



---

Comment by malb created at 2009-08-25 19:20:10

This is a duplicate of #4761 and thus I am closing this ticket.


---

Comment by malb created at 2009-08-25 19:20:10

Resolution: duplicate
