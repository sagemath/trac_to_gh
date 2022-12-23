# Issue 2325: segfault in p-adic extension() method

Issue created by migration from https://trac.sagemath.org/ticket/2325

Original creator: ncalexan

Original creation time: 2008-02-26 23:05:17

Assignee: was

CC:  ncalexan

Keywords: p-adic extension crash segfault ntl


```
sage: F = list(Qp(19)['x'](cyclotomic_polynomial(5)).factor())[0][0]
sage: L = Qp(19).extension(F, names='a')
fatal error:
   internal error: can't grow this _ntl_gbigint
exit...
/Users/ncalexan/sage-2.10.2.alpha0/local/bin/sage-sage: line 220: 21707 Abort trap              sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$@"

Process SAGE exited abnormally with code 134
```



---

Comment by mabshoff created at 2008-03-15 02:27:51

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-03-15 02:40:24

Nick,

I cannot reproduce this with 2.10.3 on sage.math. Can you verify on your 2.10.3 build that this is still a problem?

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-03-16 01:41:06

I am getting the same segfault under sage-2.10.3 and sage-2.10.4.alpha0, on two different machines running Gentoo Linux.


---

Comment by ncalexan created at 2008-03-16 19:07:59

Still crashes for me, 2.10.4.alpha0 (I think).


---

Comment by mabshoff created at 2008-04-11 20:54:12

This now works. I assume it was fixed by #2843:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.alpha3, Release Date: 2008-04-09                  |
| Type notebook() for the GUI, and license() for information.        |
sage: F = list(Qp(19)['x'](cyclotomic_polynomial(5)).factor())[0][0]
sage: L = Qp(19).extension(F, names='a')
sage: L
Unramified Extension of 19-adic Field with capped relative precision 20 in a defined 
by (1 + O(19^20))*x^2 + (5 + 2*19 + 10*19^2 + 14*19^3 + 7*19^4 + 13*19^5 + 5*19^6 + 
12*19^7 + 8*19^8 + 4*19^9 + 14*19^10 + 6*19^11 + 5*19^12 + 13*19^13 + 16*19^14 + 
4*19^15 + 17*19^16 + 8*19^18 + 4*19^19 + O(19^20))*x + (1 + O(19^20))
sage:
```


Can anybody confirm?

Cheers,

Michael


---

Comment by kedlaya created at 2008-04-11 21:02:10

Resolution: fixed


---

Comment by kedlaya created at 2008-04-11 21:02:10

This is fixed for me also, by applying the patch from #2843 against 3.0alpha3 (which was merged in alpha4). The general problem that was fixed by #2843 was passing NTL objects by value rather than reference, which triggered an NTL copy operation using the wrong context.


---

Comment by kedlaya created at 2008-04-18 13:46:57

Resolution changed from fixed to 


---

Comment by kedlaya created at 2008-04-18 13:46:57

Changing status from closed to reopened.


---

Comment by kedlaya created at 2008-04-18 13:46:57

Further investigation shows that this fails on my 32-bit laptop (and not on my 64-bit desktop), so I'm reopening. I think this is the same issue as #2928, so fixing one should fix the other. (It is indeed related to #2843, but the fix there seems insufficient to treat this.)


---

Comment by roed created at 2008-04-20 22:12:58

The fix for 2928 fixes this as well.


---

Attachment


---

Comment by kedlaya created at 2008-04-21 19:08:51

Since #2928 seems to fix this, but does not itself add any doctests, I propose to add a doctest here. See attached patch.


---

Comment by mabshoff created at 2008-04-26 03:39:00

Merged 9596.patch in Sage 3.0.1.alpha0


---

Comment by mabshoff created at 2008-04-26 03:39:00

Resolution: fixed
