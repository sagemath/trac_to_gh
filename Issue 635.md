# Issue 635: p-adic height gives incorrect precision

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-09-10 19:28:56

Assignee: was

If I ask for precision 10, I get precision 9:

```
sage: E = EllipticCurve("37a")
sage: P = E.gens()[0]
sage: h = E.padic_height(5, 10)
sage: h(P)
4*5 + 3*5^2 + 3*5^3 + 4*5^4 + 4*5^5 + 5^6 + 4*5^8 + O(5^9)
```


It didn't use to behave this way; it probably happened accidentally as a consequence of some changes chris wuthrich made, and it appears that the doctests were modified to make this behaviour the "correct" one. This should be fixed, because in the large prime case it ends up wasting a lot of time computing extra digits in intermediate steps.



---

Comment by dmharvey created at 2007-09-11 14:37:41

Changing status from new to assigned.


---

Comment by dmharvey created at 2007-09-11 14:37:41

Changing assignee from was to dmharvey.


---

Attachment

Attached patch fixes the precision problem, but seems to introduce some weird segfault-like issues when running long doctests. I have no idea why this is happening because I'm only touching high-level python code. My guess is that those issues are independent of this one.


---

Comment by dmharvey created at 2007-09-26 00:24:22

I've tried the same patch against 2.8.5. Pretty much the same thing happens: the ordinary doctests (on `ell_rational_field.py`) are all fine, but long doctests produce *intermittent* segfaults... on some invocations everything is fine, and sometimes it segfaults. I have tried debugging with gdb, but either (a) the problem doesn't occur, or (b) I get an empty stack trace.

I'm marking this as [with patch], because I think this patch is okay, and it's just exposing some other low-level bug somewhere else. If someone can track down the crasher that would be great.


---

Comment by was created at 2007-10-04 15:02:11

Changed to 2.8.7, since it will hopefully be in David Roe's patch already.


---

Comment by was created at 2007-10-13 07:19:07

Resolution: fixed
