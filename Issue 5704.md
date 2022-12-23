# Issue 5704: Implementation of finding elliptic curves with prescribed reduction over QQ

Issue created by migration from https://trac.sagemath.org/ticket/5704

Original creator: cremona

Original creation time: 2009-04-07 09:40:41

Assignee: was

Keywords: elliptic curve

This enhancement implements (over QQ only) the algorithm in  "Finding
all elliptic curves with good reduction outside a given set of primes"
by John Cremona and Mark Lingham, Experimental Mathematics 16 No.3
(2007), 303-312.

This is a serious application of the S-integral point functions added last year.  I have a partial Magma implementation over number fields (partial since Magma does not have S-integral points over number fields either), which requires number field functionality not yet in Sage (pSelmer groups), which I know how to do but have not done;  I will put those on a separate ticket.

It is based on 3.4.1.rc0 + #5673 (2 patches) + #5685 (1 patch).


---

Attachment


---

Comment by rlm created at 2009-04-22 14:55:59

Merges cleanly with sage-3.4.1.rc3, passes all tests in sage/schemes/elliptic_curves.


---

Comment by mabshoff created at 2009-04-24 08:34:49

Resolution: fixed


---

Comment by mabshoff created at 2009-04-24 08:34:49

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 08:38:38

Ironically the new file schemes/elliptic_curves/ell_egros.py was not added to the reference manual :)

Cheers,

Michael


---

Comment by cremona created at 2009-04-24 08:51:36

Replying to [comment:4 mabshoff]:
> Ironically the new file schemes/elliptic_curves/ell_egros.py was not added to the reference manual :)
> 
> Cheers,
> 
> Michael
OK, I will do that!   We're still working on that chapter (Chris Wuthrich is doing some too). John
