# Issue 2849: Bug in elliptic curve cardinality for j=0 in char. 3

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-04-07 20:35:32

Assignee: cremona

Dustin Moody reported

```
    While working on some things, I found a bug in SAGE:

 sage:k.<a>=GF(3^5)

 sage:E=EllipticCurve(k,[-1,-1])

 sage:E.trace_of_frobenius()
 0

 This isn't correct.  It should be -27.  I also discovered you can get
around it.

 sage:E.cardinality_exhaustive()
 271

 sage:E.trace_of_frobenius()
 -27

 Somehow, doing .cardinality_exhaustive() fixes the bug.
```




---

Attachment


---

Comment by cremona created at 2008-04-07 20:52:37

Here's the patch:   A case where q=3 (mod 4) only worked for p>3 and was being used for p=3, odd degree.  Should be a trivial review.

Note that I am in the middle of implementing vastly better support for the cases j=0 and j=1728, which are not so straightforward in characterisitcs 2 and 3 but I am getting there!


---

Comment by AlexGhitza created at 2008-04-07 21:59:03

apply after trac2849.patch


---

Attachment

Looks fine and it fixes the issue.  I've added a mini-patch that puts in a doctest demonstrating the fixed status.

Apply both patches.


---

Comment by mabshoff created at 2008-04-07 22:20:12

Resolution: fixed


---

Comment by mabshoff created at 2008-04-07 22:20:12

Merged trac2849.patch and trac2849_doctest.patch in Sage 3.0.alpha3


---

Comment by cremona created at 2008-04-08 07:58:55

Replying to [comment:2 AlexGhitza]:
> Looks fine and it fixes the issue.  I've added a mini-patch that puts in a doctest demonstrating the fixed status.
> 

Thanks, Alex -- I should have done that but only remembered after uploading the patch.

> Apply both patches.
