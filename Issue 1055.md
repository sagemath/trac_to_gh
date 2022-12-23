# Issue 1055: Don't factor discriminant for quadratic number fields

Issue created by migration from https://trac.sagemath.org/ticket/1055

Original creator: robertwb

Original creation time: 2007-11-01 20:27:44

Assignee: was

The current implementation of quadratic number fields calculates the discriminant on initialization, which can be expensive and is unnecessary. 

Elements are represented as a+b sqrt(D) / denom. I don't believe that we require D to be the discriminant, but this needs to be verified before a change is made. For efficiency reasons, it might be worth doing trial division to reduce squares of small prime powers from D, as smaller D yields faster arithmetic. 



---

Comment by was created at 2007-11-03 15:32:40

easy to fix?


---

Comment by robertwb created at 2007-11-03 17:06:18

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2007-11-03 22:17:38

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2007-11-06 21:56:07

applied to 2.8.12.rc0


---

Comment by mabshoff created at 2007-11-06 21:56:07

Resolution: fixed
