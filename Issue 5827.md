# Issue 5827: crypto: subset sum problem for super-increasing sequences

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-04-20 03:15:33

Assignee: somebody

Keywords: knapsack cryptosystem, subset sum

The Merkle-Hellman knapsack public-key cryptosystem makes use of the subset sum problem for super-increasing sequences. The goal of this ticket is to first implement a class for solving the subset sum problem for super-increasing sequences. The long-term goal is to implement a module for knapsack cryptosystems. So the implementation contained on this ticket would be subsumed within the module.


---

Comment by mvngu created at 2009-04-20 03:21:27

The patch implements an algorithm for solving the subset sum problem for super-increasing sequences. This is useful in the Merkle-Hellman knapsack cryptosystem, which I plan to work on later.


---

Comment by mvngu created at 2009-04-24 09:20:53

based on Sage 3.4.1


---

Attachment

Only apply `trac_5827-subset-sum.2.patch`.


---

Attachment

based on Sage 4.0


---

Comment by mvngu created at 2009-06-01 08:14:28

Only apply `trac_5827-subset-sum.2.patch`. This patch depends on the patch at #6176.


---

Comment by mvngu created at 2009-06-01 08:14:28

Changing component from cryptography to numerical.


---

Comment by mvngu created at 2009-06-01 08:14:28

Changing keywords from "knapsack cryptosystem, subset sum" to "knapsack problems, subset sum".


---

Comment by mvngu created at 2009-06-01 08:14:28

Changing assignee from somebody to jkantor.


---

Comment by mhansen created at 2009-06-04 18:52:15

Resolution: fixed


---

Comment by mhansen created at 2009-06-04 18:52:15

Looks good to me.

Merged in 4.0.1.rc1.


---

Comment by mvngu created at 2009-06-05 05:49:27

I notice some typos in the code. This is addressed by #6222.
