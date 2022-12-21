# Issue 8643: The inverse of a morphism have the wrong domain and codomain

Issue created by migration from Trac.

Original creator: boussica

Original creation time: 2010-04-02 14:41:00

Assignee: Boussicault

Keywords: morphism, domain and codomain

In the categories of modules with basis, the domain (resp. codomain) of a morphism  have to be equals to the codomain (resp. domain) of it's inverse.

In the current modues_with_basis, it is not the case.


---

Comment by boussica created at 2010-04-02 14:52:34

Resolution: fixed


---

Comment by mvngu created at 2010-04-02 20:16:40

I assume you have read the [Trac guidelines](http://www.sagemath.org/doc/developer/trac.html), especially this [critical section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets). What you are doing is creating confusion for release managers by closing tickets without at least providing one reproducible sequence to steps to verify the fix.


---

Comment by nborie created at 2010-04-05 09:41:01

I just confirm Adrien had good reasons to close this ticket.

Please, for the next time, try to explain why you closed the ticket. For example here :

This bug has been reported and fixed by Jason in #7914.
