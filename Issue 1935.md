# Issue 1935: [with patch, needs review] legendre_symbol currently quite slow

Issue created by migration from https://trac.sagemath.org/ticket/1935

Original creator: craigcitro

Original creation time: 2008-01-26 09:33:26

Assignee: craigcitro

The legendre_symbol command is pretty slow; this patch speeds it up a good bit. Here are some timings:

BEFORE:

```
sage: time for _ in range(10000): a = legendre_symbol(12,5)
CPU times: user 0.46 s, sys: 0.05 s, total: 0.52 s
Wall time: 0.52
```


AFTER:

```
sage: time for _ in range(10000): a = legendre_symbol(12,5)
CPU times: user 0.11 s, sys: 0.02 s, total: 0.13 s
Wall time: 0.13
```


However, it's still *much* slower than kronecker_symbol:

```
sage: time for _ in range(10000): a = kronecker_symbol(12,5)
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02
```


Here's most of the discrepancy:

```
sage: time for _ in range(10000): 5.is_prime()
CPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s
Wall time: 0.08
```


It's amusing, because there's no need for legendre_symbol to check whether or not its argument is prime, since under the hood it just calls kronecker. Of course, it would work when it shouldn't, which is probably bad. So this is a happy medium.

I suspect that this is still wildly slower than Pari, Magma, etc -- indeed, Magma can do that calculation about 250,000 times in the same time frame. It's not wildly important, but moving arith.py to Cython could help close that gap.


---

Attachment


---

Comment by mabshoff created at 2008-01-26 09:47:08

The patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-26 11:15:02

Resolution: fixed


---

Comment by mabshoff created at 2008-01-26 11:15:02

Merged in Sage 2.10.1.rc0
