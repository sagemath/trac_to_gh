# Issue 653: Need LLL-optimize from pari

Issue created by migration from https://trac.sagemath.org/ticket/653

Original creator: jvoight

Original creation time: 2007-09-14 04:28:55

Assignee: was

It would be good to port polredabs() from pari--this runs LLL to find a "small" generator of a field.

From gp:

? ?polredabs
polredabs(x,{flag=0}): a smallest generating polynomial of the number field for 
the T2 norm on the roots, with smallest index for the minimal T2 norm. flag is 
optional, whose binary digit mean 1: give the element whose characteristic 
polynomial is the given polynomial. 4: give all polynomials of minimal T2 norm 
(give only one of P(x) and P(-x)). 16: partial reduction.

(Of course, this is part of the larger project of bringing the number fields up to speed...)


---

Comment by was created at 2007-09-14 04:41:10

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2007-10-21 14:21:12

I believe this issue has been fixed, but there is also malb's new LLL wrapper code.

Cheers,

Michael


---

Comment by cwitty created at 2007-10-26 05:05:13

polredabs() is in.

Hopefully we don't have to re-implement every computer algebra algorithm that uses LLL, just because we have a fast LLL now.  If so, that should be a separate ticket. :)


---

Comment by cwitty created at 2007-10-26 05:05:13

Resolution: fixed
