# Issue 6393: Jacobi sums incorrect when exactly one chacater is trivial

Issue created by migration from https://trac.sagemath.org/ticket/6393

Original creator: wdj

Original creation time: 2009-06-24 11:33:13

Assignee: tbd

Example:


```
sage: G=DirichletGroup(5); X=G.list(); Y=X[0]; Z=X[1] 
sage: # Y is trivial and Z is quartic
sage: sum([Y(x)*Z(1-x) for x in IntegerModRing(5)])
 -1
sage: # The value -1 above is the correct value of the Jacobi sum J(Y, Z).
sage: Y.jacobi_sum(Z);    Z.jacobi_sum(Y)
0
0
sage: #The 0 values above are incorrect values of J(Y, Z).
```



---

Attachment

applies to 4.0.2.rc3 passes sage -testall


---

Comment by wdj created at 2009-06-24 14:42:43

Changing component from algebra to modular forms.


---

Comment by wdj created at 2009-06-24 14:42:43

Changing assignee from tbd to craigcitro.


---

Comment by davidloeffler created at 2009-07-14 19:36:10

Looks good to me, and doctests pass. I'm surprised this went so long without being spotted.


---

Comment by davidloeffler created at 2009-07-14 19:56:42

BTW, in the course of reviewing this I've realised that our Jacobi sum algorithm is absurdly slow, vastly slower than calculating the sums directly! I've just opened #6534 for this.


---

Comment by davidloeffler created at 2009-07-14 20:18:40

I'm about to upload a patch at #6534 which totally changes the way we calculate Jacobi sums, thus superseding this patch somewhat. I've made sure that it takes into account the issue you raised here.


---

Comment by mvngu created at 2009-07-16 16:33:45

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:16:42

Resolution: fixed


---

Comment by mvngu created at 2009-07-24 14:40:34

See #6613 for a follow up to this ticket.
