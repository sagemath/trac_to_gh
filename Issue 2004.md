# Issue 2004: [with patch, needs review] padic_height_via_multiply

Issue created by migration from https://trac.sagemath.org/ticket/2004

Original creator: dmharvey

Original creation time: 2008-01-31 20:35:36

Assignee: was

Patches implement new algorithm for computing (good ordinary) p-adic heights, with improved asymptotics for the high precision case:


```
sage: E = EllipticCurve("37a")
sage: P = E.gens()[0]

sage: time E2 = E.padic_E2(5, 500)
CPU times: user 7.00 s, sys: 0.74 s, total: 7.74 s
Wall time: 7.76

sage: time h1 = E.padic_height(5, 500)(P)
CPU times: user 9.34 s, sys: 0.86 s, total: 10.19 s
Wall time: 10.22
sage: 10.22 - 7.76
2.46000000000000

sage: time h2 = E.padic_height_via_multiply(5, 500)(P)
CPU times: user 7.36 s, sys: 0.74 s, total: 8.10 s
Wall time: 8.12
sage: 8.12 - 7.76
0.359999999999999

sage: h1 == h2
True
```


So it's pretty much dominated by the computation of E2 now.

It's still fast for low precision too:


```
sage: time h1 = E.padic_height(5, 10)(P)
CPU times: user 0.08 s, sys: 0.00 s, total: 0.08 s
Wall time: 0.08

sage: time h2 = E.padic_height_via_multiply(5, 10)(P)
CPU times: user 0.07 s, sys: 0.00 s, total: 0.08 s
Wall time: 0.08

sage: h1 == h2
True
```


I wrote the code a few weeks ago, but the patches are still okay against 2.10.1.rc1.



---

Attachment


---

Attachment

you need to apply both patch files


---

Comment by cremona created at 2008-02-16 20:44:13

While not an expert on p-adic height computations (few people are, David H amongst them) this looks very well done to me.  It is particularly commendable that he refers to a paper (to appear) to justify things -- and one in an excellent journal too ;).  I am tempted to ask the person who refereed that paper to referee this implementation, but unfortunately I do not think that would be possible without breaking the journal's anonymity policy.


---

Comment by mabshoff created at 2008-02-17 23:39:22

Resolution: fixed


---

Comment by mabshoff created at 2008-02-17 23:39:22

Merged in Sage 2.10.2.alpha1
