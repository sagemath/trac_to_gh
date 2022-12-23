# Issue 1769: [with patch] Fast Pari <--> Sage p-adic capped relative element conversions

Issue created by migration from https://trac.sagemath.org/ticket/1769

Original creator: craigcitro

Original creation time: 2008-01-14 02:18:08

Assignee: craigcitro

I think the title pretty much says it all: I made the conversion back and forth between  t_PADIC and pAdicCappedRelativeElement significantly faster. Here are some timings:

BEFORE:

```
sage: R = Zp(5) ; x = R(123123123153)

sage: time for _ in range(30000): y = x._pari_()
CPU times: user 1.56 s, sys: 0.32 s, total: 1.88 s
Wall time: 2.09

sage: time for _ in range(30000): y = pari(x)
CPU times: user 1.62 s, sys: 0.32 s, total: 1.94 s
Wall time: 2.10

sage: time for _ in range(30000): z = R(y)
CPU times: user 2.91 s, sys: 0.23 s, total: 3.14 s
Wall time: 3.40

sage: z == x
 True
```


AFTER:

```
sage: R = Zp(5) ; x = R(123123123153)

sage: time for _ in range(30000): y = x._pari_()
CPU times: user 0.19 s, sys: 0.10 s, total: 0.29 s
Wall time: 0.32

sage: time for _ in range(30000): y = pari(x)
CPU times: user 0.28 s, sys: 0.11 s, total: 0.39 s
Wall time: 0.43

sage: time for _ in range(30000): z = R(y)
CPU times: user 0.98 s, sys: 0.01 s, total: 0.98 s
Wall time: 1.11

sage: z == x
 True
```


It's roughly 6-6.5X faster from Sage to Pari, and 3X faster in the other direction. I also got another 15-20% out of t_INT --> pAdicCappedRelativeElement conversions:

BEFORE:

```
sage: R = Zp(5) ; x = pari(987987987344)

sage: time for _ in range(30000): y = R(x)
CPU times: user 1.14 s, sys: 0.09 s, total: 1.23 s
Wall time: 1.34
```


AFTER:

```
sage: R = Zp(5) ; x = pari(987987987344)

sage: time for _ in range(30000): y = R(x)
CPU times: user 0.97 s, sys: 0.09 s, total: 1.06 s
Wall time: 1.15
```


I'm going to file a ticket in a moment to do the same for capped-abs and fixedmod types, because I don't feel like doing it right now, and someone could probably roughly copy-paste what I did in those cases without any knowledge of the Pari side of things.




---

Comment by craigcitro created at 2008-01-14 02:37:28

Changing status from new to assigned.


---

Attachment


---

Comment by craigcitro created at 2008-01-14 12:34:55

Adding one more small patch, that adds one initialization line that David Roe pointed out I forgot. The two patches should be applied in order.


---

Attachment


---

Comment by robertwb created at 2008-01-15 06:10:59

Looks good to me too.


---

Comment by mabshoff created at 2008-01-15 06:15:29

Resolution: fixed


---

Comment by mabshoff created at 2008-01-15 06:15:29

Both patches merged in Sage 2.10.alpha3
