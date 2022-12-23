# Issue 3887: [with patch, needs review] Bug in determinant

Issue created by migration from https://trac.sagemath.org/ticket/3887

Original creator: craigcitro

Original creation time: 2008-08-18 10:48:28

Assignee: craigcitro

CC:  cpernet

Here's a crazy bug:


```
sage: m = diagonal_matrix(ZZ, 68, [2]*66 + [1,1])
sage: m.det()
-73786800370889000442
sage: m.det(proof=False)
73786976294838206464
```


Amusingly, the `proof=False` one is correct. Fix is attached.


---

Attachment

Oops, I forgot to mention: Nils-Peter Skoruppa was the one who reported this.


---

Comment by craigcitro created at 2008-08-18 10:50:03

Changing status from new to assigned.


---

Comment by was created at 2008-08-23 00:01:20

positive review.  great find!


---

Comment by mabshoff created at 2008-08-23 00:10:23

Resolution: fixed


---

Comment by mabshoff created at 2008-08-23 00:10:23

Merged in Sage 3.1.2.alpha0.

Craig: Did Nils find or also fix the bug, i.e. does he get credit?

Cheers,

Michael


---

Comment by robertwb created at 2008-12-17 23:59:10

What hardware was this on? I'm having trouble reproducing this bug (after reverting your changes) and it immensely slows down hnf and det computations.


---

Comment by craigcitro created at 2008-12-18 00:13:42

This pops up on my MacBook Pro, and whatever hardware Nils was running on (his linux laptop, not sure beyond that). 

I just checked -- reverting this patch gets me the same error:


```
sage: diagonal_matrix(ZZ, 68, [2]*66 + [1,1]).det()
-73786800370889000442
```


The bound that gets determined in that function is also wrong -- in this case, the divisor it finds is 2, and the final determinant is 2^66:


```
sage: 2^66
73786976294838206464
sage: 2^66 < 10^20
True
sage: 2^66 < 10^20//2
False
```



---

Comment by robertwb created at 2008-12-18 00:18:28

Ah, so we just needed an extra factor of 2 in there (as we weren't taking into account the sign). I'm posting a patch.


---

Attachment


---

Comment by robertwb created at 2008-12-18 00:22:39

Resolution changed from fixed to 


---

Comment by robertwb created at 2008-12-18 00:22:39

Changing status from closed to reopened.


---

Comment by robertwb created at 2008-12-18 00:24:58

I'm going to move this to a new ticket.


---

Comment by robertwb created at 2008-12-18 00:24:58

Resolution: fixed


---

Comment by robertwb created at 2008-12-18 00:27:11

See #4823
