# Issue 1873: [with patch] elementary function expansion returns result in the wrong ring

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-01-20 22:22:55

Assignee: mhansen

CC:  sage-combinat

I'm using Sage 2.10 now. Expansion for elements in SFAElementary works
great now, but there is another problem: the expansion lies in the
wrong ring.

```
sage: e=SFAElementary(QQ)
sage: f=e([2]).expand(2)
sage: f
x0*x1
sage: f.parent()
Multivariate Polynomial Ring in x0, x1, x2 over Rational Field
```


The same code but for SFASchur results in:

```
sage: s=SFASchur(QQ)
sage: f=s([2]).expand(2)
sage: f
x0^2 + x0*x1 + x1^2
sage: f.parent()
Multivariate Polynomial Ring in x0, x1 over Rational Field
```



---

Attachment


---

Comment by mhansen created at 2008-01-20 22:27:07

Changing status from new to assigned.


---

Comment by ncalexan created at 2008-01-22 19:00:00

Looks fine to me, and appears to fix the ticket.

mhansen has the super-commit-bit in this area anyway, in my opinion :)


---

Comment by mabshoff created at 2008-01-23 04:06:25

Resolution: fixed


---

Comment by mabshoff created at 2008-01-23 04:06:25

Merged in Sage 2.10.1.alpha2
